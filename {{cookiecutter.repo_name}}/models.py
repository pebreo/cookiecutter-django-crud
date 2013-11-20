from django.core.urlresolvers import reverse
from django.db import models


class {{ cookiecutter.model_name }}(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '{{ cookiecutter.model_name }} ({})'.format(self.id or 'Unsaved')

    def get_absolute_url(self):
        return reverse('{{ cookiecutter.model_name|lower }}_detail', args=[str(self.id)])

