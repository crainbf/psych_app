from django.db import models

# Create your models here.
class TrialResponse(models.Model):
	stim_color = models.CharField(max_length=16)
	response_color = models.CharField(max_length=16)
	reaction_time = models.IntegerField()