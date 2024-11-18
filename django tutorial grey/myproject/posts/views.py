from django.shortcuts import render
from .models import post
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    posts= post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{'posts':posts})

def post_page(request,slug):    
    Post= post.objects.get(slug=slug)
    return render(request,'posts/post_page.html',{'Post':Post})

@login_required(login_url = "/users/login/")
def post_new(request):
    return render(request,'posts/post_new.html')



