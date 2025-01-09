# Generated by Django 5.1.4 on 2025-01-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_feature_remove_calltoaction_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/')),
                ('description', models.TextField()),
                ('rating', models.IntegerField(default=5)),
            ],
        ),
    ]