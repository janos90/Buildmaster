import logging

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from submissionform.forms import JobForm
from submissionform.models import Job

logger = logging.getLogger(__name__)


class JobListView(ListView):
    model = Job
    template_name = 'jobs.html'


class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'


class CreateJobView(CreateView):
    model = Job
    template_name = 'add_job.html'
    form_class = JobForm

    def form_valid(self, form):
        form.instance.rep = self.request.user.rep
        logger.error('form validated!')
        form.save()

        return super().form_valid(form)

    success_url = reverse_lazy('home')


class UpdateJobView(UpdateView):
    model = Job
    template_name = 'update_job.html'
    fields = '__all__'


class DeleteJobView(DeleteView):
    model = Job
    template_name = 'delete_job.html'
    success_url = reverse_lazy('job-list')
