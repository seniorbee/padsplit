# Generated by Django 3.2.3 on 2021-05-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_address_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Title'),
        ),
    ]
