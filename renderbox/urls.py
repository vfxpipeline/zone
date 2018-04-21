from django.conf.urls import url
from . import views
from . import api

urlpatterns = [
    url(r'^myjobs/$', views.myjobs_view, name='myjobs_view'),
    url(r'^renderbox/$', views.renderbox_view, name='renderbox_view'),

    url(r'^api/renderbox/client/$', api.ClientAPI.as_view(), name='client_api'),
    url(r'^api/renderbox/client/(?P<client_id>\d+)/$', api.ClientDataAPI.as_view(), name='client_data_api'),
    url(r'^api/renderbox/job/$', api.JobAPI.as_view(), name='job_api'),

]
