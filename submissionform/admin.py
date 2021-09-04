from django.contrib import admin

from members.models import Entity, Rep, Supplier
from submissionform.models import Job

# Register your models here.
admin.site.register(Entity)
admin.site.register(Job)
admin.site.register(Rep)
admin.site.register(Supplier)
