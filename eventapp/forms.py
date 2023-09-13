from django import forms
from .models import Detail

class Detailform(forms.ModelForm):
    class Meta:
        model=Detail
        fields={'fullname','email','phone'}