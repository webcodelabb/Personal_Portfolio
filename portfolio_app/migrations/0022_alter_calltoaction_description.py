# Generated by Django 5.1.4 on 2025-01-08 22:17

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0021_alter_calltoaction_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltoaction',
            name='description',
            field=tinymce.models.HTMLField(help_text='Description for the CTA'),
        ),
    ]