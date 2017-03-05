from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



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

    def clean_name(self):
        data = self.cleaned_data['name']
        if(data.split('.') != 'yml'):
            raise ValidationError(_('Invalid playbook name - must be a yml type. eg: ntp.yml'))
        return data

    def clean_playbook_text(self):
        data = self.cleaned_data['playbook_text']
        #TODO: check playbook syntax
        return data


    class Meta:
        model = Playbook

