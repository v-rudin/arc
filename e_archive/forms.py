from django import forms
from .models import DiadocDocument
from django.forms.widgets import DateInput


class DateTimeInput(DateInput):
    format_key = "%d/%m/%Y %H:%M"
    input_type = 'date'


class DiadocDocumentForm(forms.ModelForm):
    class Meta:
        model = DiadocDocument
        fields = ['doc_brief', 'doc_type', 'doc_number', 'doc_date', 'doc_description']
        widgets = {
            'date': DateInput(format=('%d/%m/%Y'),
                              attrs={'type': 'date',
                                     'placeholder': "DD/MM/YY"}),
        }
