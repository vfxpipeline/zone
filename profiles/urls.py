from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^register', views.register_view, name='register'),
    url(r'^profile/$', views.profile_view, name='profile_view'),
    url(r'^profile/(?P<profile_id>\d+)/$', views.other_profile_view, name='other_profile_view'),
]

