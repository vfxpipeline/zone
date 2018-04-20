from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class EmploymentStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Designation(models.Model):
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department


class Skill(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill


class Profile(models.Model):
    """
    User Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status_choice = (('online', 'Online'), ('offline', 'Offline'), ('production', 'Production'))
    status = models.CharField(choices=status_choice, max_length=50, null=True, blank=True)
    user_group_choice = (('admin', 'Admin'), ('artist', 'Artist'), ('production', 'Production'),
                         ('management', 'Management'))
    user_group = models.CharField(choices=user_group_choice, max_length=50, null=True, blank=True)
    account_creation_date = models.DateTimeField(auto_now_add=True)
    home_page = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    password_changed = models.BooleanField(default=False, blank=True)
    employee_id = models.CharField(max_length=50, null=True, unique=True, blank=True)
    official_name = models.CharField(max_length=200, null=True, blank=True)
    nick_name = models.CharField(max_length=50, null=True, blank=True)

    def upload_photo_dir(self, filename):
        ext = filename.split('.')[-1]
        path = 'profiles/photo/{}.{}'.format(self.employee_id, ext)
        return path

    photo = models.ImageField(upload_to=upload_photo_dir, default='/icons/default/user.png', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender_choice = (
                    ('male', 'Male'),
                    ('female', 'Female')
                    )
    gender = models.CharField(max_length=10, choices=gender_choice,  null=True, blank=True)
    marital_choice = (
                    ('single', 'Single'),
                    ('married', 'Married')
                    )
    marital_status = models.CharField(max_length=10, choices=marital_choice, null=True,  blank=True)
    # contact details
    address_1 = models.CharField(max_length=200, null=True, blank=True)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    address_city = models.CharField(max_length=100, null=True, blank=True)
    address_state = models.CharField(max_length=50, null=True, blank=True)
    address_zip = models.CharField(max_length=50, null=True, blank=True)
    address_country = models.CharField(max_length=50, null=True, blank=True)
    work_email = models.CharField(max_length=50, null=True, blank=True)
    other_email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    #Jobs Details
    employment_status = models.ForeignKey(EmploymentStatus, on_delete=models.CASCADE, related_name='employment_status', null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='+',  null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+',  null=True, blank=True)
    skill = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
