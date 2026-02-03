from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Fieldset, Submit
from .models import Teaching

class TeachingForm(forms.ModelForm):
    class Meta:
        model = Teaching
        exclude = ('fecha_creacion',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'

        self.helper.layout = Layout(
            Fieldset(
                'Datos Teaching',
                Row(
                    Column('title', css_class='col-md-6'),
                ),
                Row(
                    Column('price', css_class='col-md-4'),
                    Column('duracion_min', css_class='col-md-4'),
                    Column('estado', css_class='col-md-4'),
                ),
                Row(
                    Column('description', css_class='col-md-12'),
                ),
                Row(
                    Column('start_at', css_class='col-md-6'),
                    Column('end_at', css_class='col-md-6'),
                ),
            ),
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )
