# Generated by Django 2.2.9 on 2020-06-29 20:01

import accounts.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200629_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Met_Ocean_Conditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prevailing_winds', models.CharField(blank=True, max_length=1000, null=True)),
                ('Predominant_current', models.CharField(blank=True, max_length=1000, null=True)),
                ('Average_wave_height', models.CharField(blank=True, max_length=1000, null=True)),
                ('Average_swell_height_and_period', models.CharField(blank=True, max_length=1000, null=True)),
                ('What_is_the_tidal_range_if_applicable', models.CharField(blank=True, max_length=1000, null=True)),
                ('Location_subject_to_restrictive_Met_conditions', models.CharField(blank=True, max_length=1000, null=True)),
                ('STS_Location_covered_by_forecasting_service', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='met_ocean_conditions',
            field=djongo.models.fields.EmbeddedModelField(model_container=accounts.models.Met_Ocean_Conditions, model_form_class=accounts.models.Met_Ocean_ConditionsForm, null=True),
        ),
    ]
