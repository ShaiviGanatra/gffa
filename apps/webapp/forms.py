from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . models import Film

class FilmForm(forms.ModelForm):
    """Form created for updating Film entity"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Film
        fields = '__all__'
