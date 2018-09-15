from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render
from Registration.models import Voter,Candidate

def login(request):
    q1 = {}
    q1.update(csrf(request))
    return render_to_response('Login1.html', q1)
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    #if not username or not password:
    #    return HttpResponseRedirect('/loginmodule/invalidlogin/')
    p1=Voter.objects.filter(vunm=username , vpass=password)
    #print(username + password + p1.vunm + p1.vpass)
    p=Voter.objects.filter(vunm=username , vpass=password).exists()
    q=Candidate.objects.filter(cunm=username , cpass=password).exists()
    if p or q:
            request.session['user']=username
            return HttpResponseRedirect('/vote/home/')
    else:
        q1={}
        dict={'wrong':True}
        q1.update(dict)
        q1.update(csrf(request))
        return render_to_response('Login1.html', q1)

#def invalidlogin(request):
#    return render_to_response('invalidlogin.html')
