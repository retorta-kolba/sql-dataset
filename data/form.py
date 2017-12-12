from django import forms
from data.models import *
class DataForm(forms.Form):
    #task = forms.ModelMultipleChoiceField(Task.objects.all())
    text = forms.CharField(label='', required=False)
    sciencefields = forms.ModelMultipleChoiceField(ScienceField.objects.all(), label='Темы', required=False)
    
    #only_active = forms.BooleanField(label="Только активные программисты",required=False)
    #status = forms.MultipleChoiceField(Task.STATUSES, label='Статусы')