from django.shortcuts import render

#Models
from .models import Blogs

# Create your views here.
def blogs(request):
    firtsBlog = Blogs.objects.first()
    blogs = Blogs.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs, 'firtsBlog': firtsBlog})

def blog(request, id):
    blog = Blogs.objects.get(id=id)
    return render(request, 'blog.html', {'blog': blog})