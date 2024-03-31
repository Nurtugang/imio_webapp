from django import forms
from .models import Materials


class MaterialsForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = '__all__'  # Use all fields from the model
