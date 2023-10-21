from django.contrib import admin

from teams_api.models import Team, Participant

# Register your models here.
admin.site.register(Team)
admin.site.register(Participant)
