from django import forms
from upload.models import UploadModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
