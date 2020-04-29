from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from .models import Complaint,Feedback
# from causes.models import Catagory


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content',]