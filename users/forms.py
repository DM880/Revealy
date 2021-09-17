from .models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class UploadCoverForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(UploadCoverForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)

    class Meta:
        model = ProfileInfo
        fields = ['cover_image']


class UploadProfileImgForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ['profile_image']

