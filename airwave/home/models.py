from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
from django.urls import reverse

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)
class Category(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
    

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True,unique=True)
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User,related_name='blog_posts')
    category= models.CharField(max_length=1000, default='coding')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
class Comment(models.Model):
    post = models.ForeignKey(BlogModel ,null=True,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



    
    


