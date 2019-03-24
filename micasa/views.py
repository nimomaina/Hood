from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from . forms import *
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url = '/accounts/login')
def home(request):
    hoods = Hood.objects.all()
    business = Business.objects.all()
    posts = Post.objects.all()

    return render(request,'home.html',locals())

@login_required(login_url = '/accounts/login')
def all_hoods(request):

    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Hood.objects.get(pk=request.user.join.hood_id.id)
            businesses = Business.objects.filter(hood=request.user.join.hood_id.id)
            posts = Post.objects.filter(hood=request.user.join.hood_id.id)
            comments = Comments.objects.all()
            print(posts)
            return render(request, "hood.html", locals())
        else:
            neighbourhoods = Hood.objects.all()
            return render(request, 'hood.html', locals())
    else:
        neighbourhoods = Hood.objects.all()

        return render(request, 'hood.html', locals())


def search_category(request):
    location = Location.objects.all()
    category = Category.objects.all()
    if 'Category' in request.GET and request.GET["Category"]:
        category = request.GET.get("Category")
        searched_image = Picture.search_by_category(category)
        message = f"{category}"

        return render(request,'category/searched.html', {"message":message,"Category":searched_image})

    else:
        message = "You haven't searched for anything"
        return render(request,'category/searched.html',{"message":message})


def filter_location(request):
    locations = Location.objects.all()
    location = request.GET.get("location")

    searched_image = Picture.filter_by_location(location)
    message = f"{location}"

    return render(request,'category/location.html', {"message":message,"location":searched_image, "locations":locations})



