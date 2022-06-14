from django.contrib import admin

# Register your models here.
from .models import BlogModel , Profile, Category , Comment


admin.site.register(BlogModel)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)