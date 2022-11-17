from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, CreateView
from blog.models import Post
from blog.forms import EditUserProfileForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User

@login_required(login_url='/blog/login/')
def index(request):
    posts = Post.objects.order_by('-date_published').all()
    return render(request, 'blog/index.html', {"posts": posts})


class ListPost(ListView):
    model=Post

class CreatePost(CreateView):
    model=Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")

class DetailPost(DetailView):
    model=Post

class UpdatePost(UpdateView):
    model=Post
    fields=['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("index-blog")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "blog/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username']
    success_url = reverse_lazy("blog-login")

class DetailProfile(DetailView):
    model=Post


class UpdateUserView(generic.UpdateView):
    form_class = EditUserProfileForm
    success_url = reverse_lazy("Home")
    template_name = "authors/edit_user_profile.html"
    

    def get_object(slef):
        return slef.request.user
