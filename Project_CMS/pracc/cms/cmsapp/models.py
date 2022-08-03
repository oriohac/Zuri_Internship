from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    #users
    username = models.CharField(max_length=40, unique= True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    #templates
    website = models.FileField(blank=True, upload_to='cmsapp_sites/')
    image =  models.ImageField(blank=True, upload_to ='cmsapp_images/')
    siteicon = models.ImageField(blank=True, upload_to ='cmsapp_icon/')
    site_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    #templates contents
    title = models.CharField(max_length=120)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )
    def __str__(self):
        return self.title
    class Meta:
       ordering = ['-created']
class Users(models.Model):
    username = models.CharField(max_length=40, unique= True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)