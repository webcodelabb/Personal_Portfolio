# Generated by Django 5.1.4 on 2025-01-08 14:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0019_alter_calltoaction_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltoaction',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='Description for the CTA'),
        ),
    ]