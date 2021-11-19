from django import forms
from .models import State, Attraction

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = "__all__"
