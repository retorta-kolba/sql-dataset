from django import forms
from data.models import *
class DataForm(forms.Form):
    #task = forms.ModelMultipleChoiceField(Task.objects.all())
    text = forms.CharField(label='Название', required=False)
    fieldtext = forms.CharField(label='Название поля', required=False)
    sciencefields = forms.ModelMultipleChoiceField(ScienceField.objects.all(), label='Темы', required=False)
    authors = forms.ModelMultipleChoiceField(Author.objects.all(), label='Автор', required=False)
    startdate = forms.DateField(label='с', required=False)
    enddate = forms.DateField(label='по', required=False)
    
    
    #only_active = forms.BooleanField(label="Только активные программисты",required=False)
    #status = forms.MultipleChoiceField(Task.STATUSES, label='Статусы')