from django.contrib import admin
from .models import *


class JobsFields(admin.ModelAdmin):
    list_display =[f.name for f in Job._meta.fields]


admin.site.register(Job, JobsFields)
admin.site.register(Task)
admin.site.register(Frame)
admin.site.register(JobCategory)
admin.site.register(JobStatus)
admin.site.register(Client)
admin.site.register(ClientStatus)
admin.site.register(App)
admin.site.register(AppPlugin)
admin.site.register(Group)
admin.site.register(Settings)
admin.site.register(Department)


