from django import forms
from django.forms import fields
from django.forms.widgets import TextInput
from .models import Write

class WriteForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'제목 입력',
            }
        )
    )
    contents = forms.CharField(
        max_length=500,
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'내용 입력',
            }
        )
    )
    class Meta:
        model = Write
        fields = '__all__'