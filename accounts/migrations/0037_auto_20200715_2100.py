# Generated by Django 2.2.9 on 2020-07-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20200715_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='Provider_company',
        ),
        migrations.AddField(
            model_name='entry',
            name='Provider_Company',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
