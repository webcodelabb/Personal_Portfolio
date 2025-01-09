from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import portfolio_view
from .views import contact_view

urlpatterns = [
    path('', views.body, name='body'),
    path('about/', views.about_view, name='about'),
    path('cta/click/<int:cta_id>/', views.track_click, name='track_click'),
    path('features/', views.features_view, name='features'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
    path('skills/', views.skills_view, name='skills'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('faq/', views.faq_view, name='faq'),
    path("contact/", contact_view, name="contact"),
    path('blog/', views.blog_view, name='blog'),
    path('api/recent-blogs/', views.recent_blogs_api, name='recent_blogs_api'),    
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



