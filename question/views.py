from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from question.models import question,Reward
from Registration.models import Candidate
from Registration.models import Voter
from datetime import datetime

# Create your views here.

def QA(request):
    q1={}
    try:
        x=request.session['user']
        print ("hello check",str(x))
    except Exception as e:
        print("check")
        dict={'invalid':True}
        q1.update(dict)
        q1.update(csrf(request))
        return render_to_response('Login1.html', q1)
    date =question.objects.latest('mnth').mnth
    qa=question.objects.get(mnth=date)
    q1['que']=qa.Que
    #print(qa.Que)
    area=Voter.objects.get(vunm=x)
    cand=list(Candidate.objects.filter(area=area.area))
    q1['cand']=cand
    q1.update(csrf(request))
    vtr=Voter.objects.get(vunm=x)

    if vtr.flag1 :
        dict={'answered':True}
        q1.update(dict)
        q1.update(csrf(request))

    return render_to_response('QA.html', q1)

def review(request):
    q1={}
    try:
        x=request.session['user']
        print ("hello check",str(x))
    except Exception as e:
        print("check")
        dict={'invalid':True}
        q1.update(dict)
        q1.update(csrf(request))
        return render_to_response('Login1.html', q1)
    elect=request.GET.get('candidate','')
    cand=Candidate.objects.get(cunm=elect)

    date =question.objects.latest('mnth').mnth
    p=Reward.objects.get(month=date,v_Id=cand.id)
    p.reward=p.reward+1
    p.save()

    vtr=Voter.objects.get(vunm=x)

    if vtr.flag1 :
        dict={'answered':True}
        q1.update(dict)
        q1.update(csrf(request))

    else:
        vtr.flag1=1
        vtr.save()
        q1.update(csrf(request))
        return render_to_response('QAthnx.html', q1)
