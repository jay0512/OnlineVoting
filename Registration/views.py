from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from Registration.models import Voter,Candidate
from vote.models import Votes
from question.models import Reward
import datetime
from datetime import timedelta



def register(request):
    p = {}
    p.update(csrf(request))
    return render_to_response('registration1.html', p)

def auth(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    name = request.POST.get('name', '')
    dob = request.POST.get('dob', '')
    gender=request.POST.get('gen','')
    area=request.POST.get('area','')

    p=Voter.objects.filter(vunm=username).exists()
    q=Candidate.objects.filter(cunm=username).exists()
    if(p or q):
        q1={}
        dict={'repeat':True}
        q1.update(dict)
        q1.update(csrf(request))
        return render_to_response('registration1.html', q1)


    today=datetime.date.today()
    d=datetime.date(int(dob.split('-')[0]),int(dob.split('-')[1]),int(dob.split('-')[2]))
    diff = today.year - d.year
    print(diff)
    if username!='' and password!='':

        if diff<=18 :
            q1={}
            dict={'age':True}
            q1.update(dict)
            q1.update(csrf(request))
            return render_to_response('registration1.html', q1)

        if diff>=18 :
            s = Voter(vunm = username ,vpass = password , voter_name = name  , voter_dob = dob , gender = gender , area=area ,flag = 0 ,flag1=0)
            s.save()
            #if choose=='candidate':
            #    s = Candidate(cunm = username ,cpass = password , candidate_name = name  , candidate_dob = dob , gender = gender , reward = 0 , flag = 0)
            #    s.save()
            #    can=Candidate.objects.get(cunm=username)
            #    s1=Votes(vid=can ,vote=0)
            #    s1.save()
            #    s2=Reward(v_Id=can)
            #    s2.save()
            return HttpResponseRedirect('/vote/home/')
    else:
        return HttpResponseRedirect('/loginmodule/login/')
