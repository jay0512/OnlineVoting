from django.contrib import admin
from vote.models import Election,Votes
from Registration.models import Voter,Candidate

# Register your models here.
def SetElection(modeladmin, request, queryset):
    for elction in queryset:
        date= elction.Edate
        cand=Candidate.objects.all()
        for x in cand:
            s2=Votes(vid=x)
            s2.elec_id=elction
            s2.ElectionDate = date
            s2.save()

        voter=Voter.objects.all()
        for y in voter:
            y.flag=0
            y.save()

SetElection.short_description = 'Set Election'

class ElectionAdmin(admin.ModelAdmin):
    list_display = ('StartTime','EndTime')
    list_filter = ('StartTime','EndTime')
    search_fields = ('StartTime','EndTime')
    actions = [SetElection, ]

class voteAdmin(admin.ModelAdmin):
    list_display = ('vid','ElectionDate','vote')
    list_filter = ('vid','ElectionDate','vote')
    search_fields = ('vid','ElectionDate','vote')

admin.site.register(Election,ElectionAdmin)
admin.site.register(Votes,voteAdmin)
