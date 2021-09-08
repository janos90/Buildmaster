from django.forms import ModelForm, DateInput

from submissionform.models import Job


class DateInput(DateInput):
    input_type = 'date'


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('pre_nail_date', 'logged_date')
        widgets = {
            'pre_nail_date': DateInput(attrs={'class': 'form-control'}),
            'logged_date': DateInput(attrs={'class': 'form-control'}),
        }
