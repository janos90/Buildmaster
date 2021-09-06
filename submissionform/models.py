from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

from members.models import Supplier, Rep


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

    JOB_LOCATIONS = [

        ('AUc', 'Auckland'),
        ('WAI', 'Waikato'),
    ]

    job_location = models.CharField(
        choices=JOB_LOCATIONS,
        default=0,
        max_length=3
    )

    # Client info
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=255)
    client_mobile = models.CharField(max_length=255)
    rep = models.ForeignKey(Rep, on_delete=models.CASCADE)
    logged_date = models.DateField()
    client_address = models.TextField()
    client_email = models.EmailField()

    # Detailer info
    detailer_name = models.CharField(max_length=255)
    detailer_contact_number = models.CharField(max_length=255)

    # email list info
    email_skip = models.BooleanField()
    email_arie = models.BooleanField()
    email_luci = models.BooleanField()
    email_vip = models.BooleanField()
    email_jason = models.BooleanField()
    email_to = models.EmailField()
    suppliers = models.ManyToManyField(Supplier)

    # checkboxes
    # section 1
    truss_layout_ps1_only = models.BooleanField()
    full_buildable_layouts = models.BooleanField()
    detailing = models.BooleanField()
    steel_reinforcing = models.BooleanField()
    pre_bent_r_steel = models.BooleanField()
    rib_raft = models.BooleanField()
    masonry = models.BooleanField()
    concrete = models.BooleanField()
    # section 2
    pre_nail = models.BooleanField()
    trusses = models.BooleanField()
    rafters = models.BooleanField()
    roof_pack = models.BooleanField()
    random = models.BooleanField()
    sub_floor = models.BooleanField()
    mid_floor = models.BooleanField()
    deck = models.BooleanField()
    j_frame = models.BooleanField()
    # _section_3
    cladding = models.BooleanField()
    insulation_only = models.BooleanField()
    insulation_installed = models.BooleanField()
    plasterboard = models.BooleanField()
    plasterboard_dts = models.BooleanField()
    internal_linings = models.BooleanField()
    internal_doors = models.BooleanField()
    # _section_4
    timber_fascia = models.BooleanField()
    marley_gutter_dp = models.BooleanField()
    roofing = models.BooleanField()
    aluminium_joinery = models.BooleanField()
    pergola = models.BooleanField()
    retaining_wall = models.BooleanField()

    WINDZONES = [
        (0, 'No Wind'),
        (1, 'Low Wind'),
        (2, 'Medium Wind'),
        (3, 'High Wind'),
        (4, 'Very High Wind'),
        (5, 'Extra High Wind'),
    ]
    wind_zone = models.IntegerField(
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
        choices=CORROSION_ZONES,
        default=0
    )

    # Note product required for the following
    interior_doors_notes = models.CharField(max_length=255)
    door_hardware_notes = models.CharField(max_length=255)
    scotia_notes = models.CharField(max_length=255)
    skirting_notes = models.CharField(max_length=255)
    architraves_notes = models.CharField(max_length=255)
    fascia_type_notes = models.CharField(max_length=255)
    ceiling_batten_notes = models.CharField(max_length=255)
    roof_material_notes = models.CharField(max_length=255)
    truss_penetrations_notes = models.CharField(max_length=255)
    special_trusses_notes = models.CharField(max_length=255)

    alteration_notes = models.TextField()

    # file uploads
    plan_file = models.FileField(null=True, blank=True, upload_to="jobs/dog-profiles")
    engineer_plans_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    window_door_plan_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    specification_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    dwg_floor_plan_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")

    # information in plans
    dimensioned_floor_on_plan = models.BooleanField()
    elevations_on_plan = models.BooleanField()
    cross_section_on_plan = models.BooleanField()
    roof_pitch_on_plan = models.BooleanField()
    electrical_plan_on_plan = models.BooleanField()
    rafters_design_and_sizing_on_plan = models.BooleanField()

    def __str__(self):
        return self.name + " " + self.rep.user.get_full_name()

    def get_absolute_url(self):
        return reverse('job-detail', args=(str(self.id)))
