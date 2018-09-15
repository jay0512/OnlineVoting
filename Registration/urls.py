from django.urls import path
from Registration.views import register,auth
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^register/$', register),
    url(r'^auth/$', auth),
    ]
