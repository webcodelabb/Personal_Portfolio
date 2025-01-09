from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import About, Service, CallToAction, Feature, Testimonial, Skill, Project, FAQ, Contact, Blog
from django.contrib import messages
from .forms import ContactForm
from django.template import loader, Context



def body(request):
    about = About.objects.first()
    services = Service.objects.all()
    call_to_action = CallToAction.objects.first()  # Fetch the first CTA entry
    features = Feature.objects.all()  # Fetch the features
    testimonials = Testimonial.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    faqs = FAQ.objects.all()
    contacts = Contact.objects.all()
    recent_blogs = Blog.objects.order_by('-published_date')[:4]

    return render(request, 'body.html', {
        'about': about,
        'services': services,
        'call_to_action': call_to_action, 
        'features': features,
        'testimonials' : testimonials,
        'skills' : skills,
        'projects': projects,
        'faqs' : faqs,
        'contacts': contacts,
        'recent_blogs': recent_blogs,      
    })


def faq_view(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs
    }
    return render(request, 'fax.html', context)





def portfolio_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio.html', context)



def testimonials_view(request):
    testimonials = Testimonial.objects.all()
    for testimonial in testimonials:
        testimonial.filled_stars = range(testimonial.rating)
        testimonial.empty_stars = range(5 - testimonial.rating)

    context = {
        "testimonials": testimonials,
    }
    return render(request, "testimonials.html", context)


def track_click(request, cta_id):
    cta = get_object_or_404(CallToAction, id=cta_id)
    cta.clicks += 1
    cta.save()
    return redirect(cta.button_link)

def about_view(request):
    # Fetch the first entry from the About table
    about = About.objects.first()  # Or use get_object_or_404
    return render(request, 'main.html', {'about': about})


def services_view(request):
    services = Service.objects.all()
    return render(request, 'main.html', {'services': services})

def features_view(request):
    # Fetch all Feature entries from the database
    features = Feature.objects.all()  # Fetching the features from the database
    return render(request, 'main.html', {'features': features})  # Passing features to the template


def skills_view(request):
    skills = Skill.objects.all()
    return render(request, 'main.html', {'skills': skills})





def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    else:
        form = ContactForm()
    
    return render(request, "main.html", {"form": form})



def blog_view(request):
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog.html', {'blogs': blogs})


from django.http import JsonResponse
from .models import Blog

def recent_blogs_api(request):
    # Get pagination parameters from query string
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 4))
    start = (page - 1) * limit
    end = start + limit

    # Fetch blogs ordered by published_date
    blogs = Blog.objects.order_by('-published_date')[start:end]

    # Format data for JSON response
    blog_data = [
        {
            'title': blog.title,
            'slug': blog.slug,
            'category': blog.category,
            'author': blog.author,
            'published_date': blog.published_date.strftime('%b %d, %Y'),
            'image_url': blog.image.url if blog.image else '',
            'author_image_url': blog.author_image.url if blog.author_image else '',
            'detail_url': f'/blog/{blog.id}/',  # Construct URL for blog detail page
        }
        for blog in blogs
    ]

    return JsonResponse(blog_data, safe=False)


def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog.html', {'blog': blog})

