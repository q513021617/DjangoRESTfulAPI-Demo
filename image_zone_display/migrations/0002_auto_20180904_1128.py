# Generated by Django 2.1.1 on 2018-09-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_zone_display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.CharField(max_length=100),
        ),
    ]
