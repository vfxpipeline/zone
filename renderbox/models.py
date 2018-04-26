from django.db import models
from profiles.models import Profile


class Settings(models.Model):
    windows_repository_path = models.CharField(max_length=255)
    linux_repository_path = models.CharField(max_length=255)


class JobStatus(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="icons/status")

    def __str__(self):
        return self.name


class ClientStatus(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="icons/status")

    def __str__(self):
        return self.name


class Client(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.ForeignKey(ClientStatus, null=True, blank=True)
    os_platform = models.CharField(max_length=50, null=True, blank=True)
    os_name = models.CharField(max_length=50, null=True, blank=True)
    os_username = models.CharField(max_length=50, null=True, blank=True)
    os_arch = models.CharField(max_length=50, null=True, blank=True)
    host_name = models.CharField(max_length=50, null=True, blank=True)
    idle_time = models.FloatField(null=True, blank=True)  # in seconds
    rendering_time = models.FloatField(null=True, blank=True)  # in seconds
    up_time = models.CharField(max_length=50, null=True, blank=True)
    cpu_name = models.CharField(max_length=100, null=True, blank=True)
    cpu_core = models.IntegerField(null=True, blank=True)
    l2_cache = models.IntegerField(null=True, blank=True)
    l3_cache = models.IntegerField(null=True, blank=True)
    cpu_usage = models.FloatField(null=True, blank=True)
    total_ram = models.CharField(max_length=50, null=True, blank=True)
    ram_usage = models.FloatField(null=True, blank=True)
    available_ram = models.CharField(max_length=50, null=True, blank=True)
    gpu_card = models.CharField(max_length=50, null=True, blank=True)
    gpu_memory = models.CharField(max_length=50, null=True, blank=True)
    network_adapter = models.CharField(max_length=50, null=True, blank=True)
    network_speed = models.CharField(max_length=50, null=True, blank=True)
    ip_address = models.GenericIPAddressField(unique=True)
    mac_address = models.CharField(max_length=50, unique=True)
    client_register_time = models.DateTimeField(auto_now_add=True)
    sync_interval = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.host_name


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    """
    Groups can be used to organize your farm based on projects
    If you don’t care about grouping your machines, you can simply use the default ‘none’ Group.
    """
    name = models.CharField(max_length=50)
    client = models.ManyToManyField(Client)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class App(models.Model):
    """
    MAYA, HOUDINI, NUKE, REALFLOW
    """
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="icons/apps", default='icons/apps/default.png', blank=True)
    win_exe = models.CharField(max_length=255, null=True, blank=True)
    linux_exe = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class AppPlugin(models.Model):
    """

    """
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='+')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="icons/apps", default='icons/apps/default.png', blank=True)
    win_exe = models.CharField(max_length=255, null=True, blank=True)
    linux_exe = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}_{}".format(self.app.name, self.name)


class JobCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='+')
    plugin = models.ForeignKey(AppPlugin, on_delete=models.CASCADE, related_name='+')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+')
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='+')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='+')

    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255, null=True, blank=True)
    status = models.ForeignKey(JobStatus, default=5, on_delete=models.CASCADE, related_name='+')
    priority_choice = (('low', 'Low'),
                       ('normal', 'Normal'),
                       ('medium', 'Medium'),
                       ('high', 'High'),
                       ('critical', 'Critical'))
    priority = models.CharField(max_length=50, default='low', choices=priority_choice, blank=True)
    post_complete = (('nothing', 'Nothing'),
                     ('movie', 'Build Movie'),
                     ('archive', 'Archive'),
                     ('restart', 'Restart'),
                     ('shutdown', 'Shutdown'),
                     ('delete', 'Delete'))
    on_job_complete = models.CharField(max_length=50, default='nothing', choices=post_complete, blank=True)

    start_frame = models.FloatField()
    end_frame = models.FloatField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    submit_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='submit_by')
    submit_pc = models.CharField(max_length=100)
    submit_ip = models.GenericIPAddressField()

    chunk_size = models.IntegerField(default=1)
    file_path = models.CharField(max_length=255)
    file_size = models.FloatField()
    project_path = models.CharField(max_length=255, null=True, blank=True)
    output_path = models.CharField(max_length=255, null=True, blank=True)

    assign_clients = models.ManyToManyField(Client, blank=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.app.name, self.plugin.name, self.category, self.name)


class Task(models.Model):
    """
    Job will split into small multiple task and split into all available clients
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='+')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='+')
    process_id = models.IntegerField()
    status = models.ForeignKey(JobStatus, on_delete=models.CASCADE, related_name='+')
    progress = models.FloatField()
    start_frame = models.FloatField()
    end_frame = models.FloatField()
    wip_frame = models.FloatField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.job


class Frame(models.Model):
    """
    Task Frame information
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='+')
    frame_number = models.FloatField()
    status = models.ForeignKey(JobStatus, on_delete=models.CASCADE, related_name='+')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)


