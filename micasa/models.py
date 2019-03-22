from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField

# Create your models here.



class Hood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.CharField(max_length=50)

    class Meta:
        ordering = ['-pk']

    def save_hood(self):
        self.save()


    def delete_hood(self):
        self.delete()

    def __str__(self):

        return self.name


    @classmethod
    def search_hood(cls, search_term):
        hood = Hood.objects.filter(title__icontains=search_term)
        return hood


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile/',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length = 255,null = True)
    email = models.EmailField(null = True)
    full_name = models.CharField(max_length=255, null=True)
    hood = models.ForeignKey(Hood,null=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user=id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user=id).first()
        return details

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    hood = models.ForeignKey(Hood)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()



    @classmethod
    def search_business(cls, search_term):
        business = Business.objects.filter(business_name__icontains=search_term)
        return business






