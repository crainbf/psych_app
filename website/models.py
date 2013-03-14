from django.db import models


# Create your models here.
class TrialResponse(models.Model):
    participant_id = models.IntegerField()
    stim_color = models.CharField(max_length=16, verbose_name='Stimulus Color')
    stim_word = models.CharField(max_length=16, verbose_name='Stimulus Word')
    response_color = models.CharField(max_length=16, verbose_name='Response Color')
    reaction_time = models.IntegerField()
    session_number = models.IntegerField()

    def __unicode__(self):
        return u'Participant %s. Reaction Time: %s' % (self.participant_id, self.reaction_time)
