from django.contrib import admin
from question.models import question,Reward
from Registration.models import Voter,Candidate

def Add_Candidate(modeladmin, request, queryset):
    for que in queryset:
        date= que.mnth
        cand=Candidate.objects.all()
        for x in cand:
            s2=Reward(v_Id=x)
            s2.q_id=que
            s2.month=date
            s2.save()
        voter=Voter.objects.all()
        for y in voter:
            y.flag1=0
            y.save()

Add_Candidate.short_description = 'Add Candidate in Reward'

class QueAdmin(admin.ModelAdmin):
    list_display = ('Que','mnth')
    list_filter = ('Que','mnth')
    search_fields = ('Que','mnth')
    actions = [Add_Candidate, ]  # <-- Add the list action function here

class RewardAdmin(admin.ModelAdmin):
    list_display = ('v_Id','month','reward')
    list_filter = ('v_Id','month','reward')
    search_fields = ('v_Id','month','reward')

admin.site.register(question,QueAdmin)
admin.site.register(Reward,RewardAdmin)
# Register your models here.
