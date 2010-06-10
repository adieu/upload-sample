from django import forms
from upload.models import StorageModel

class StorageForm(forms.ModelForm):
    class Meta:
        model = StorageModel
