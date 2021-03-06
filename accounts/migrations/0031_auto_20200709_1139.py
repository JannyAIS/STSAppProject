# Generated by Django 2.2.9 on 2020-07-09 10:39

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20200707_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='Local_piloting_additional_information',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='Cargos_permitted',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Oil'), (2, 'LPG'), (3, 'Chemicals'), (4, 'LNG'), (5, 'All cargoes permitted')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='Is_local_piloting_assistance_required',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=1000, null=True),
        ),
    ]
