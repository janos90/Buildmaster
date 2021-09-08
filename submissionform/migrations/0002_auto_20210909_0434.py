# Generated by Django 3.2.7 on 2021-09-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissionform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='alteration_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='architraves_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='ceiling_batten_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='client_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='client_mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='client_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='detailer_contact_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='detailer_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='discount_group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='door_hardware_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='fascia_type_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='frame_truss_margin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='interior_doors_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_location',
            field=models.CharField(choices=[('AUC', 'Auckland'), ('WAI', 'Waikato')], default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='job',
            name='pre_nail_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='roof_material_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='scotia_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='skirting_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='special_trusses_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='truss_penetrations_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
