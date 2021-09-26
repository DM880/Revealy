from .models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from weasyprint import HTML


class UploadCoverForm(forms.ModelForm):

    class Meta:
        model = ProfileInfo
        fields = ['cover_image']

    def __init__(self, *args, **kwargs):
        super(UploadCoverForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.layout = Layout(
        #     'cover_image'
        # )


class UploadProfileImgForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UploadProfileImgForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    class Meta:
        model = ProfileInfo
        fields = ['profile_image']


# class DeleteUserForm(forms.Form):
#     choices = forms.ChoiceField(required = True, widget=forms.RadioSelect(attrs={'name' : 'choice'}), initial=1)