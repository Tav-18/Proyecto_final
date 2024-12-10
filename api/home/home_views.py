from django.shortcuts import render

# Create your views here.

def home_views(request):
    template_name = "index.html"
    
    return render(request, template_name)

def camera_views(request):
    template_name = "camera.html"
    
    return render(request, template_name)
