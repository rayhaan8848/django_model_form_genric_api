from django import forms
from .models import Yatri


class YatriForm(forms.ModelForm):
    class Meta:
        model=Yatri
        fields=['name','age','email']
            
        