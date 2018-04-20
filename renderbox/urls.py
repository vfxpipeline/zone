from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^myjobs/$', views.myjobs_view, name='myjobs_view'),
    url(r'^renderbox/$', views.renderbox_view, name='renderbox_view')
]
