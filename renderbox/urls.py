from django.conf.urls import url
from . import views
from . import api

urlpatterns = [
    url(r'^myjobs/$', views.myjobs_view, name='myjobs_view'),
    url(r'^renderbox/$', views.renderbox_view, name='renderbox_view'),

    url(r'^api/renderbox/client/$', api.ClientAPI.as_view(), name='client_api'),
    url(r'^api/renderbox/client/(?P<client_id>\d+)/$', api.ClientEditAPI.as_view(), name='client_edit_api'),
    url(r'^api/renderbox/job/$', api.JobAPI.as_view(), name='job_api'),
    url(r'^api/renderbox/job/(?P<job_id>\d+)/$', api.JobEditAPI.as_view(), name='job_edit_api')

]
