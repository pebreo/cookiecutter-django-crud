import floppyforms as forms
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Form(forms.ModelForm):
    class Meta:
        model = {{ cookiecutter.model_name }}

