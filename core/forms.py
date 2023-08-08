from core.models import Projects_Data
from django import forms

class Data_form(forms.ModelForm):
    class Meta:
        model = Projects_Data
        fields = "__all__"
