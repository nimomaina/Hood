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

    return render(request,'home.html',locals())


@login_required(login_url='/accounts/login')
def upload_hood(request):
    current_user = request.user

    if request.method == 'POST':
        hoodform = HoodForm(request.POST, request.FILES)
        if hoodform.is_valid():
            upload = hoodform.save(commit=False)
            upload.save()
            return redirect('home_page')
    else:
        hoodform = HoodForm()
    return render(request, 'upload-hood.html', locals())


def search_category(request):
    location = Location.objects.all()
    category = Category.objects.all()
    if 'Category' in request.GET and request.GET["Category"]:
        category = request.GET.get("Category")
        searched_image = Business.search_by_category(category)
        message = f"{category}"

        return render(request,'category/searched.html', {"message":message,"Category":searched_image})

    else:
        message = "You haven't searched for anything"
        return render(request,'category/searched.html',{"message":message})


def filter_location(request):
    locations = Location.objects.all()
    location = request.GET.get("location")

    searched_image = Hood.filter_by_location(location)
    message = f"{location}"

    return render(request,'category/location.html', {"message":message,"location":searched_image, "locations":locations})



