# Generated by Django 5.0.4 on 2024-05-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0014_alter_house_publisheddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='publishedDate',
            field=models.DateTimeField(),
        ),
    ]
