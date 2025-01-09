from django.db import models
from PIL import Image
from tinymce.models import HTMLField

import uuid

class YourModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Other fields...

class About(models.Model):
    title = models.CharField(max_length=200, default="About")
    description = models.TextField()
    point_1 = models.CharField(max_length=200, blank=True, null=True)
    point_2 = models.CharField(max_length=200, blank=True, null=True)
    point_3 = models.CharField(max_length=200, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    read_more_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., 'bi bi-activity')")
    description = models.TextField()
    delay = models.IntegerField(default=0, help_text="Animation delay in milliseconds")

    def __str__(self):
        return self.title




class CallToAction(models.Model):
    title = HTMLField(max_length=200, help_text="Title for the CTA")
    description = HTMLField(help_text="Description for the CTA")
    button_text = models.CharField(max_length=100, default="Call To Action")
    button_link = models.URLField(help_text="URL for the button")
    clicks = models.PositiveIntegerField(default=0, help_text="Number of times the CTA has been clicked")

    def __str__(self):
        return self.title



class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)  # Store the icon class (e.g., bi-archive)
    image = models.ImageField(upload_to='features/', null=True, blank=True)  # New image field

    def __str__(self):
        return self.title



class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    description = models.TextField()
    rating = models.IntegerField(default=5)  # To store star ratings

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/')
    github_link = models.URLField(max_length=500, blank=True, null=True)
    demo_link = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="portfolio_images/")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize image
        img = Image.open(self.image.path)
        if img.height > 600 or img.width > 800:
            output_size = (800, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name


 
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    author_image = models.ImageField(upload_to='author_images/')
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)  # Ensure this field exists, if required

    def __str__(self):
        return self.title
