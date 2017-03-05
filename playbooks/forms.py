from django import forms
from django.contrib.auth.models import User

from .models import Album, Song, Playbook


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PlaybookForm(forms.Form):
    name = forms.CharField()
    playbook_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Playbook

