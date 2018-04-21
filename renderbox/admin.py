from django.contrib import admin
from .models import *

admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobStatus)
admin.site.register(Client)
admin.site.register(ClientStatus)
admin.site.register(App)
admin.site.register(Group)
admin.site.register(Settings)
admin.site.register(Department)


