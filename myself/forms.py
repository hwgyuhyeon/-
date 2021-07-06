from django.db.models import fields
from .models import *
from django import forms

class GuestForm(forms.ModelForm):
    class Meta:
        model = GuestLog
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = GuestComment
        fields = ['comment']