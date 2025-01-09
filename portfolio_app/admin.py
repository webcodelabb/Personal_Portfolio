from django.contrib import admin
from .models import About, Service, CallToAction, Feature, Testimonial, Skill, Project, FAQ, Contact,  Blog



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message", "created_at")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_editable = ('description',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'delay')
    search_fields = ('title',)



@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text', 'clicks')
    list_editable = ('button_text',)
    readonly_fields = ('clicks',)



class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    search_fields = ('title', 'description')

admin.site.register(Feature, FeatureAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'rating')  # Columns visible in the admin list view
    list_filter = ('rating',)  # Add a filter by rating
    search_fields = ('name', 'position', 'description')  # Add a search bar for these fields
    fields = ('name', 'position', 'image', 'description', 'rating')  # Order and fields in the admin form
    list_editable = ('rating',)  # Allow rating to be editable directly in the list view
    ordering = ('-rating', 'name')  # Default ordering by rating (highest first)

admin.site.register(Testimonial, TestimonialAdmin)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'github_link', 'demo_link')
    search_fields = ('title', 'technologies', 'github_link', 'demo_link')
    fields = ('title', 'description', 'technologies', 'image', 'github_link', 'demo_link')

 
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)




# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'published_date')
    search_fields = ('title', 'content', 'author')
    list_filter = ('category', 'published_date')
    prepopulated_fields = {'slug': ('title',)}  # If you have a slug field
