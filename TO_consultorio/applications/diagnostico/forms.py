from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Diagnostico

class Form_diagnostico(forms.ModelForm):

    class Meta:
        model = Diagnostico
        fields = '__all__'

    def clean_diagnostic(self):
        diagnostico = self.cleaned_data['diagnostic']

        #Check if len is greater than 2 
        if diagnostico.len < 2:
            raise ValidationError(_('El nombre del diagnóstico debe tener más de 2 caracteres'))

        # Return the cleaned data.
        return diagnostico