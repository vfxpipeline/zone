from django.db import models
from profiles.models import Profile, Department


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
        return self.os_username


class Group(models.Model):
    """
    Groups can be used to organize your farm based on machine configurations (e.g., specs, installed software, etc).
    For example, if you have several 64-bit machines with 3ds Max installed, you could assign them to groups like
    3dsmax, or 3dsmax_64bit, or simply 3D. Groups have no impact on the order in which Jobs are rendered,
    they just help to ensure that Jobs render on machines with proper an appropriate hardware/software setup.
    If you don’t care about grouping your machines, you can simply use the default ‘none’ Group.
    """
    name = models.CharField(max_length=50)
    client = models.ManyToManyField(Client)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="icons/apps", default='icons/apps/default.png', null=True, blank=True)
    win_exe = models.CharField(max_length=255)
    linux_exe = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class JobCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='+')
    name = models.CharField(max_length=255, null=True, blank=True )
    comment = models.CharField(max_length=255, null=True, blank=True)
    assign_clients = models.ManyToManyField(Client, blank=True)
    group = models.ManyToManyField(Group, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    file_size = models.FloatField(null=True, blank=True)
    project_path = models.CharField(max_length=255, null=True, blank=True)
    output_path = models.CharField(max_length=255, null=True, blank=True)
    priority_choice = (('low', 'Low'),
                       ('normal', 'Normal'),
                       ('medium', 'Medium'),
                       ('high', 'High'),
                       ('critical', 'Critical')
                       )
    priority = models.CharField(max_length=50, default='low', choices=priority_choice,  blank=True)
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='+')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+')
    file_path = models.CharField(max_length=255)
    status = models.ForeignKey(JobStatus, default=5, on_delete=models.CASCADE, related_name='+')
    start_frame = models.FloatField()
    end_frame = models.FloatField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    submit_user = models.ForeignKey(Profile, related_name='submit_user')
    chunk_size = models.IntegerField(default=1)
    submit_pc = models.CharField(max_length=100, null=True, blank=True)
    submit_ip = models.GenericIPAddressField(null=True, blank=True)
    post_complete = (
        ('nothing', 'Nothing'),
        ('movie', 'Build Movie'),
        ('archive', 'Archive'),
                     ('restart', 'Restart'),
                     ('shutdown', 'Shutdown'),
                     ('delete', 'Delete')
                     )
    on_job_complete = models.CharField(max_length=50, default='nothing', choices=post_complete, null=True, blank=True)


class Task(models.Model):
    """
    Job will split into small multiple task and split into all available clients
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(JobStatus, on_delete=models.CASCADE)
    start_frame = models.FloatField()
    wip_frame = models.FloatField()
    end_frame = models.FloatField()
    complete_frames = models.CharField(max_length=255)
    error_frames = models.CharField(max_length=255)
    queued_frames = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    process_id = models.IntegerField()
    progress = models.FloatField()


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name