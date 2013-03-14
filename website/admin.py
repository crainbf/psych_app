from django.contrib import admin
from website.models import TrialResponse


class TrialResponseAdmin(admin.ModelAdmin):
    list_display = ('participant_id', 'session_number', 'reaction_time')
    list_filter = ('participant_id','session_number',)
    ordering = ('participant_id',)


admin.site.register(TrialResponse, TrialResponseAdmin)
