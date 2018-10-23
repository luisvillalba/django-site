from django import forms
from home.models import AuthorModel

class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class AuthorModelForm(forms.ModelForm):
    instagram = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta():
        model = AuthorModel
        exclude = ('user',)
