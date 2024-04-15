from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio_site/home.html')

def about(request):
    return render(request, 'portfolio_site/about.html')

def gallery(request):
    return render(request, 'portfolio_site/gallery.html')

def contact(request):
    return render(request, 'portfolio_site/contact.html')