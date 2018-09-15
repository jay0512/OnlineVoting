from django.urls import path
from vote.views import castVote, result,home,vote1,logout,AboutUs
from django.conf.urls import url

urlpatterns = [
    url(r'^home/$', home),
    url(r'^vote1/$', vote1),
    url(r'^castVote/$', castVote),
    url(r'^result/$', result),
    url(r'^AboutUs/$', AboutUs),
    url(r'^logout/$',logout),
    ]
