from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

from members.models import Supplier, Rep


class Job(models.Model):
    # bts info
    creation_date = models.DateField(auto_now_add=True)

    # Office use info
    frame_truss_margin = models.CharField(max_length=255, null=True, blank=True)
    discount_group = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)

    # job info
    job_name = models.CharField(max_length=255)
    job_company = models.CharField(max_length=255)
    pre_nail_date = models.DateField(null=True, blank=True)
    site_address = models.TextField()

    JOB_LOCATIONS = [

        ('AUC', 'Auckland'),
        ('WAI', 'Waikato'),
    ]

    job_location = models.CharField(
        choices=JOB_LOCATIONS,
        default=0,
        max_length=3
    )

    # Client info
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=255, null=True, blank=True)
    client_mobile = models.CharField(max_length=255, null=True, blank=True)
    rep = models.ForeignKey(Rep, on_delete=models.CASCADE)
    logged_date = models.DateField()
    client_address = models.TextField()
    client_email = models.EmailField(null=True, blank=True)

    # Detailer info
    detailer_name = models.CharField(max_length=255, null=True, blank=True)
    detailer_contact_number = models.CharField(max_length=255, null=True, blank=True)

    # email list info
    email_skip = models.BooleanField(default=False)
    email_arie = models.BooleanField(default=False)
    email_luci = models.BooleanField(default=False)
    email_vip = models.BooleanField(default=False)
    email_jason = models.BooleanField(default=False)
    email_to = models.EmailField(null=True, blank=True)
    suppliers = models.ManyToManyField(Supplier)

    # checkboxes
    # section 1
    truss_layout_ps1_only = models.BooleanField(default=False)
    full_buildable_layouts = models.BooleanField(default=False)
    detailing = models.BooleanField(default=False)
    steel_reinforcing = models.BooleanField(default=False)
    pre_bent_r_steel = models.BooleanField(default=False)
    rib_raft = models.BooleanField(default=False)
    masonry = models.BooleanField(default=False)
    concrete = models.BooleanField(default=False)
    # section 2
    pre_nail = models.BooleanField(default=False)
    trusses = models.BooleanField(default=False)
    rafters = models.BooleanField(default=False)
    roof_pack = models.BooleanField(default=False)
    random = models.BooleanField(default=False)
    sub_floor = models.BooleanField(default=False)
    mid_floor = models.BooleanField(default=False)
    deck = models.BooleanField(default=False)
    j_frame = models.BooleanField(default=False)
    # _section_3
    cladding = models.BooleanField(default=False)
    insulation_only = models.BooleanField(default=False)
    insulation_installed = models.BooleanField(default=False)
    plasterboard = models.BooleanField(default=False)
    plasterboard_dts = models.BooleanField(default=False)
    internal_linings = models.BooleanField(default=False)
    internal_doors = models.BooleanField(default=False)
    # _section_4
    timber_fascia = models.BooleanField(default=False)
    marley_gutter_dp = models.BooleanField(default=False)
    roofing = models.BooleanField(default=False)
    aluminium_joinery = models.BooleanField(default=False)
    pergola = models.BooleanField(default=False)
    retaining_wall = models.BooleanField(default=False)

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
    interior_doors_notes = models.CharField(max_length=255, null=True, blank=True)
    door_hardware_notes = models.CharField(max_length=255, null=True, blank=True)
    scotia_notes = models.CharField(max_length=255, null=True, blank=True)
    skirting_notes = models.CharField(max_length=255, null=True, blank=True)
    architraves_notes = models.CharField(max_length=255, null=True, blank=True)
    fascia_type_notes = models.CharField(max_length=255, null=True, blank=True)
    ceiling_batten_notes = models.CharField(max_length=255, null=True, blank=True)
    roof_material_notes = models.CharField(max_length=255, null=True, blank=True)
    truss_penetrations_notes = models.CharField(max_length=255, null=True, blank=True)
    special_trusses_notes = models.CharField(max_length=255, null=True, blank=True)

    alteration_notes = models.TextField(null=True, blank=True)

    # file uploads
    plan_file = models.FileField(null=True, blank=True, upload_to="jobs/dog-profiles")
    engineer_plans_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    window_door_plan_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    specification_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")
    dwg_floor_plan_file = models.FileField(null=True, blank=True, upload_to="images/dog-profiles")

    # information in plans
    dimensioned_floor_on_plan = models.BooleanField(default=False)
    elevations_on_plan = models.BooleanField(default=False)
    cross_section_on_plan = models.BooleanField(default=False)
    roof_pitch_on_plan = models.BooleanField(default=False)
    electrical_plan_on_plan = models.BooleanField(default=False)
    rafters_design_and_sizing_on_plan = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.rep.user.get_full_name()

    def get_absolute_url(self):
        # return reverse('job-detail', args=str(self.id))
        return reverse('home')