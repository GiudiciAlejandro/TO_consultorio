from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Paciente

class Pac_form(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'

    def clean_birthdate(self):
        nacimiento = self.cleaned_data['birthdate']
        print(nacimiento)

        #Check date is not in past.
        if nacimiento < datetime.date.today():
            raise ValidationError(_('La fecha de nacimiento es incorrecta'))

        # Return the cleaned data.
        return nacimiento
