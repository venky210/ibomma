
from django import forms
from ibomma_app.models import *
class UserMF(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}


class ProfileMF(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']
