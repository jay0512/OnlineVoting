from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render
from Registration.models import Voter,Candidate
from question.models import Reward
from vote.models import Votes,Election
from django.db.models import Sum,Max
from django.template import RequestContext
from django.template import Context
from django.db.models import Q


def home(request):
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
        #return HttpResponseRedirect('/loginmodule/login/')
    p={'user1':request.session['user']}
    q1.update(p)
    print(p)
    q1.update(csrf(request))
    return render_to_response('home.html', q1)

def vote1(request):
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
        #return HttpResponseRedirect('/loginmodule/login/')
    q1.update(csrf(request))
    area=Voter.objects.get(vunm=x)
    li=list(Candidate.objects.filter(area=area.area))
    #li=Candidate.objects.order_by('-reward').all()[:3]
    #lt=Candidate.objects.values('cunm').annotate(reward_count=Count('reward')).order_by('-reward_count')[:5]
    #ca=Candidate.objects.values_list('cunm')
    #can={'cand':li}
    q1['cc']=li
    #c.update(can)
    user=Voter.objects.get(vunm=x)
    if user.flag :
        dict={'voteOnce':True}
        q1.update(dict)
    q1.update(csrf(request))
    return render_to_response('castVote.html', q1)

def castVote(request):
    q1={}
    try:
        x1=request.session['user']
        print ("hello check",str(x1))
    except Exception as e:
        print("check")
        dict1={'invalid':True}
        q1.update(dict1)
        q1.update(csrf(request))
        return render_to_response('Login1.html', q1)
        #return HttpResponseRedirect('/loginmodule/login/')
    q1.update(csrf(request))

    p=request.GET.get("candidate",'')
    q=Candidate.objects.get(cunm=p)

    val=Voter.objects.get(vunm=x1)

    date =Election.objects.latest('Edate').Edate
    x=Votes.objects.get(vid=q.id,ElectionDate=date)
    x.vote=x.vote + 1
    x.save()
    val.flag=1
    val.save()
    return render_to_response('thnxVote.html', q1)

#def showResult(request):
#    q1={}
#    try:
#        x=request.session['user']
#        print ("hello check",str(x))
#    except Exception as e:
#        print("check")
#        dict={'invalid':True}
#        q1.update(dict)
#        q1.update(csrf(request))
#        return render_to_response('Login1.html', q1)
        #return HttpResponseRedirect('/loginmodule/login/')

#    total=Votes.objects.aggregate(Sum('vote'))
#    can=Votes.objects.all()
#    for i in can:
#        temp=can.vid
#        cand[i]=temp.candidate_name
#        result[i]=100*(can.vote/total)
#    q1.update(csrf(request))
#    return render_to_response('showResult.html', q1)

def result(request):
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
        #return HttpResponseRedirect('/loginmodule/login/')

    date =Election.objects.latest('Edate').Edate
    total=Votes.objects.filter(ElectionDate=date).aggregate(Sum('vote'))
    #can=Votes.objects.order_by('-vid__reward').order_by('-vote').all()[:3]
    area=Voter.objects.get(vunm=x)
    cand=(Candidate.objects.filter(area=area.area))
    result=[]
    votes=[]
    for i in cand:
        v=Votes.objects.get(vid=i,ElectionDate=date)
        votes.append(v.vote)
        result.append(100*(v.vote/total['vote__sum']))
        #print(cand)
        #print(result)
    q1['name']=cand
    q1['per']=result
    q1['headcount']=votes

    voteper=[]
    vtotal=len(Voter.objects.all())
    voted=len(Voter.objects.filter(flag=1).all())
    voteper.append(round(100*(voted/vtotal)))
    voteper.append(round(100-100*(voted/vtotal)))
    q1['voteper']=voteper

    v=[]
    parties=Candidate.objects.values_list('party_name', flat=True).distinct()
    for q in parties:
        count=Votes.objects.filter(vid__party_name=q,ElectionDate=date).aggregate(Sum('vote'))
        v.append(round(100*(count['vote__sum']/total['vote__sum'])))

    q1['partyper']=v
    q1['party1']=parties
    j=[]
    area=Candidate.objects.values_list('area', flat=True).distinct()
    for q in area:
        vote=Votes.objects.filter(vid__area=q,ElectionDate=date).aggregate(Max('vote'))['vote__max']
        cand=Votes.objects.filter(vid__area=q,ElectionDate=date,vote=vote).all()
        print(cand)
        j.append(cand)
    q1['warea']=area
    q1['wvote']=j

    q1.update(csrf(request))
    return render_to_response('showResult.html', q1)

def logout(request):
    q1={}
    q1.update(csrf(request))
    del request.session['user']
    return render_to_response('Login1.html',q1)

def AboutUs(request):
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

    state=list(Candidate.objects.values('area').distinct())
    q1['state']=state

    comp=request.GET.get('candidate1')
    comp2=request.GET.get('candidate2')
    p=request.GET.get('city')
    can=Candidate.objects.all()
    if(p):
        y=[]
        z=[]
        y1=[]
        z1=[]
        y2=[]
        z2=[]
        y3=[]
        z3=[]
        q=Candidate.objects.filter(area=p)
        print(q)
        for data in q:
            r=Reward.objects.filter(v_Id=data).all()
            s=Votes.objects.filter(vid=data).all()
            for rate in r:
                z.append(rate.reward)
                z1.append(rate.month)
            y.append(z)
            y1.append(z1)
            z=[]
            z1=[]
            for vote in s:
                z2.append(vote.ElectionDate.year)
                z3.append(vote.vote)
            y2.append(z2)
            y3.append(z3)
            z2=[]
            z3=[]
        q1['candid']=q
        q1['rate']=y
        q1['ratevote']=y3
        q1['ratemonth']=y1
        q1['voteyr']=y2
    else:
        y=[]
        z=[]
        y1=[]
        z1=[]
        y2=[]
        z2=[]
        y3=[]
        z3=[]

        q=Candidate.objects.all()[:3]
        for data in q:
            r=Reward.objects.filter(v_Id=data).all()
            s=Votes.objects.filter(vid=data).all()
            for rate in r:
                z.append(rate.reward)

                z1.append(rate.month.strftime("%b"))
            y.append(z)
            y1.append(z1)
            z=[]
            z1=[]
            for vote in s:
                z2.append(vote.ElectionDate.year)
                z3.append(vote.vote)
            y2.append(z2)
            y3.append(z3)
            z2=[]
            z3=[]
        q1['candid']=q
        q1['rate']=y
        q1['ratevote']=y3
        q1['ratemonth']=y1
        q1['voteyr']=y2


    if(comp and comp2):
        dict={'compare':True}
        q1.update(dict)
        y=[]
        z=[]
        y1=[]
        z1=[]
        y2=[]
        z2=[]
        y3=[]
        z3=[]
        qq=Candidate.objects.filter(Q(candidate_name=comp)|Q(candidate_name=comp2))
        for data in qq:
            r=Reward.objects.filter(v_Id=data).all()
            s=Votes.objects.filter(vid=data).all()
            for rate in r:
                z.append(rate.reward)

                z1.append(rate.month.strftime("%b"))
            y.append(z)
            y1.append(z1)
            z=[]
            z1=[]
            for vote in s:
                z2.append(vote.ElectionDate.year)
                z3.append(vote.vote)
            y2.append(z2)
            y3.append(z3)
            z2=[]
            z3=[]
        q1['candid1']=qq
        q1['rate1']=y
        q1['ratevote1']=y3
        q1['ratemonth1']=y1
        q1['voteyr1']=y2
    q1['candidlist']=can
    q1.update(csrf(request))
    return render_to_response('AboutUs.html', q1)
