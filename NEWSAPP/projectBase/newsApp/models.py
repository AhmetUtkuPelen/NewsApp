from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from user.models import*
from django.contrib.auth.models import User


# Create your models here.

# ! IN ORDER TO DEFINE A CATEGORY FOR NEWS ! #

class NewsCategory(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

# ! CREATE NEWS ON ADMIN PANEL AND CHOOSE CATEGORY ! #

class CreateNews(models.Model):
    name = models.CharField(max_length=1000)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add = True , blank = True , null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='media')
    slug = models.SlugField(default= "" , blank = True , unique = True)
    category = models.ForeignKey(NewsCategory , on_delete=models.CASCADE , null=True)
    creation_time = models.DateTimeField(auto_now=True)
    approx_read_time = models.IntegerField(default=0)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args , kwargs)
    
    def __str__(self):
        return self.name


# ! USER COMMENT FORM ! #

class Comment(models.Model):
    name = models.CharField(max_length=1000)
    mail = models.EmailField(max_length = 1500)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add = True , blank = True , null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    

# ! USER PROFESSION - MAYBE ???? ! # 
class Profession(models.Model):
    name = models.CharField(max_length=50)
    relationship = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
# ! CREATE NEWS FOR USERS ! #

class UserCreateNews(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(("description"))
    image = models.ImageField(upload_to='images',blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title