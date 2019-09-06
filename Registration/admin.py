from django.contrib import admin
from Registration.models import Candidate,Voter

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('candidate_name','area','party_name','verified'))
    list_filter = ('candidate_name','area','party_name','verified'))
    search_fields = ('candidate_name','area','party_name','verified'))

class VoterAdmin(admin.ModelAdmin):
    list_display = ('voter_name','area','voter_dob','verified'))
    list_filter = ('voter_name','area','voter_dob','verified'))
    search_fields = ('voter_name','area','voter_dob','verified'))

admin.site.register(Candidate,RegisterAdmin)
admin.site.register(Voter,VoterAdmin)

# Register your models here.
