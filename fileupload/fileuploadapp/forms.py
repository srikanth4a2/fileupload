from django import forms
from .models import UserSong

class UserSongForm(forms.ModelForm):

    class Meta:
        model = UserSong
        fields = '__all__'
