from question.views import QA,review
from django.conf.urls import url


urlpatterns = [
    url(r'^qa/$', QA),
    url(r'^review/$', review),
    ]
