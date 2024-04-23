# Generated by Django 5.0.4 on 2024-04-23 11:35

import realEstate.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0002_rename_officeimage_imageoffice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(null=True, upload_to=realEstate.models.agentFileName)),
                ('likedHouses', models.ManyToManyField(blank=True, to='realEstate.house')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
