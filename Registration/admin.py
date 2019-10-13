  
from django.contrib import admin
from Registration.models import Candidate,Voter

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('candidate_name','area','party_name')
    list_filter = ('candidate_name','area','party_name')
    search_fields = ('candidate_name','area','party_name')

class VoterAdmin(admin.ModelAdmin):
    list_display = ('voter_name','area','voter_dob')
    list_filter = ('voter_name','area','voter_dob')
    search_fields = ('voter_name','area','voter_dob')

admin.site.register(Candidate,RegisterAdmin)
admin.site.register(Voter,VoterAdmin)

# Register your models here.
