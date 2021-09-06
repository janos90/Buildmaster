from django.forms import ModelForm

from submissionform.models import Job


class JobForm(ModelForm):
    class Meta:
        model = Job
