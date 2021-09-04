from django.forms import ModelForm

from submissionform.models import Job


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('name', 'breed', 'height', 'weight', 'birthday', 'owner', 'image')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'breed': TextInput(attrs={'class': 'form-control'}),
            'height': NumberInput(attrs={'class': 'form-control'}),
            'weight': NumberInput(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control'}),
            'owner': Select(attrs={'class': 'form-control'})
        }
