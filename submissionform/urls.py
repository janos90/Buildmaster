from django.urls import path
from django.views.generic import TemplateView

from .views import JobListView, CreateJobView, UpdateJobView, DeleteJobView, JobDetailView

urlpatterns = [
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('jobs/list', JobListView.as_view(), name='job-list'),
    path('jobs/create', CreateJobView.as_view(), name='job-create'),
    path('jobs/<int:pk>/update', UpdateJobView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete', DeleteJobView.as_view(), name='job-delete'),
    path('jobs/<int:pk>/detail', JobDetailView.as_view(), name='job-detail'),
]