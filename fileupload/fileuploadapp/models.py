from django.db import models

class UserSong(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField()

    def __unicode__(self):
        return self.title
