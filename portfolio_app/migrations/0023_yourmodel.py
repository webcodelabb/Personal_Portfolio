# Generated by Django 5.1.4 on 2025-01-09 11:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0022_alter_calltoaction_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]