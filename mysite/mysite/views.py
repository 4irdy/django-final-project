from django.shortcuts import render
from .models import Photo

def portfolio_view(request):
    photos = Photo.objects.all()  # Fetch all photos from the database
    return render(request, 'portfolio/portfolio.html', {'photos': photos})

def gallery_view(request):
    photos = Photo.objects.all()
    return render(request, 'portfolio/gallery.html', {'photos': photos})
