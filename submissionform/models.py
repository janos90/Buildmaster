from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

from members.models import Supplier


class Job(models.Model):
    # bts info
    creation_date = models.DateField(auto_now_add=True)

    # Office use info
    frame_truss_margin = models.CharField(max_length=255)
    discount_group = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)

    # job info
    job_name = models.CharField(max_length=255)
    job_company = models.CharField(max_length=255)
    pre_nail_date = models.DateField()
    site_address = models.TextField()
    job_location = models.TextField()

    # Client info
    client = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    rep = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    logged_date = models.DateField()
    client_address = models.TextField()

    # Detailer info
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)

    # email list info
    email_skip = models.BooleanField()
    email_arie = models.BooleanField()
    email_luci = models.BooleanField()
    email_vip = models.BooleanField()
    email_jason = models.BooleanField()
    email_to = models.EmailField()

    suppliers = models.ManyToManyField(Supplier)

    WINDZONES = [
        (0, 'NONE'),
        (1, 'LOW'),
        (2, 'MEDIUM'),
        (3, 'HIGH'),
        (4, 'VERY_HIGH'),
        (5, 'EXTRA_HIGH'),
    ]
    wind_zone = models.IntegerField(
        max_length=1,
        choices=WINDZONES,
        default=0
    )

    CORROSION_ZONES = [

        (0, 'ZONE_A_None'),
        (1, 'ZONE_B_LOW'),
        (2, 'ZONE_C_MEDIUM'),
        (3, 'ZONE_D_HIGH'),
    ]

    corrosion_zone = models.IntegerField(
        max_length=1,
        choices=CORROSION_ZONES,
        default=0
    )

    # Note product required for the following
    interior_doors_notes = models.BooleanField()
    door_hardware_notes = models.BooleanField()
    scotia_notes = models.BooleanField()
    skirting_notes = models.BooleanField()
    architraves_notes = models.BooleanField()
    fascia_type_notes = models.BooleanField()
    ceiling_batten_notes = models.BooleanField()
    roof_material_notes = models.BooleanField()
    truss_penetrations_notes = models.BooleanField()
    special_trusses_notes = models.BooleanField()

    alteration_notes = models.TextField()

    # file uploads
    plan_file = models.FileField(null=True, blank=True, upload_to="jobs/dog-profiles")
    engineer_plans_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    window_door_plan_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    specification_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    dwg_floor_plan_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")

    # information in plans
    dimensioned_floor_on_plan = models.CharField(max_length=255)
    elevations_on_plan = models.CharField(max_length=255)
    cross_section_on_plan = models.CharField(max_length=255)
    roof_pitch_on_plan = models.CharField(max_length=255)
    electrical_plan_on_plan = models.CharField(max_length=255)
    rafters_design_and_sizing_on_plan = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " " + self.rep.user.get_full_name()

    def get_absolute_url(self):
        return reverse('job-detail', args=(str(self.id)))
