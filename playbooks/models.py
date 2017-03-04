from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title




#Static tables

class OfekApp(models.Model):
    user = models.ForeignKey(User)
    application = models.CharField(max_length=30)

class Inventory(models.Model):
    user = models.ForeignKey(User)
    hostname = models.CharField(max_length=20)

class Playbook(models.Model):
    CRON = (
        ('hour', 'hour'),
        ('day', 'day'),
        ('week', 'week'),
    )
    user = models.ForeignKey(User)
    duration = models.CharField(max_length=4, choices=CRON, default='hour')
    playbook_path = models.FilePathField(path='/etc/ansible/playbooks/' + duration, match='*.yml', recursive=False, max_length=200)


#Logic table for playbook per app

class App_Playbook(models.Model):
    user = models.ForeignKey(User)
    hostname_pk = models.IntegerField()
    playbook_pk = models.IntegerField()




