from audioop import reverse
from unicodedata import category
from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
# Create your views here.
from django.views.generic import CreateView
from .form import *
from django.contrib.auth import logout
def CategoryView(request, cats):
    category_posts=BlogModel.objects.filter(category=cats)
    return render(request,'categories.html',{'category_posts':category_posts})



class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):

        return reverse_lazy("blog_detail", kwargs={'pk': self.kwargs['pk']})
    


def LikeView(request, pk ):
    post=get_object_or_404(BlogModel,id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("blog_detail",args=[str(pk)]))

def logout_view(request):
    logout(request)
    return redirect('/')


def home(request,**kwargs):

    context = {'blogs' : BlogModel.objects.all()}
    return render(request , 'home.html' , context)

def login_view(request):
    return render(request , 'login.html')

def blog_detail(request , pk):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(pk = pk).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog_detail.html' , context)


def see_blog(request):
    context = {}
    
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] =  blog_objs
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'see_blog.html' ,context)


def add_blog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
                category = form.cleaned_data['category']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image,
                category = category,
            )
            print(blog_obj)
            return redirect('/add-blog/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)
def blog_update(request , slug):
    context = {}
    try:
        
        
        blog_obj = BlogModel.objects.get(slug = slug)
       
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
        
        
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'update_blog.html' , context)

def blog_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/see-blog/')


def  register_view(request):
    return render(request , 'register.html')



def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')
