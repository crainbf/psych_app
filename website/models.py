from django.db import models


# Create your models here.
class TrialResponse(models.Model):
    participant_id = models.IntegerField()
    stim_color = models.CharField(max_length=16)
    stim_word = models.CharField(max_length=16)
    response_color = models.CharField(max_length=16)
    reaction_time = models.IntegerField()

