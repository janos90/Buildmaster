from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class Entity(models.Model):
    parent = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.parent + " " + self.name


class Rep(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
    )
    image = models.ImageField(null=True, blank=True, upload_to="images/rep/")
    phone = models.CharField(max_length=255)
    bio = RichTextField(blank=True, null=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() + " " + self.entity.name

    def get_absolute_url(self):
        return reverse('home')


class Supplier(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
    )
    image = models.ImageField(null=True, blank=True, upload_to="images/supplier/")
    phone = models.CharField(max_length=255)
    bio = RichTextField(blank=True, null=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() + " " + self.entity.name

    def get_absolute_url(self):
        return reverse('home')

