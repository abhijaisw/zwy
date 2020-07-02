from django.shortcuts import render, get_object_or_404
from .models import Blog, Image

# Create your views here.

def Blogindex(request):
    arti=Blog.objects.all()
    return render(request, "blog/blog.html", {'arti':arti})



def Blogdetails(request, id):
    blo_detail=get_object_or_404(Blog.objects.all(), pk=id)
    return render(request, "blog/single-blog.html",{'blo_detail':blo_detail})


def gellary(request):
	img = Image.objects.all()
	return render(request, 'main/gellary.html', {'img':img})