from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from Insta.models import Post

class HelloWorld(TemplateView):
  template_name = 'test.html'

class PostsView(ListView):
  model = Post
  template_name = 'index.html'

class PostDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'make_post.html'
  fields = '__all__'
  login_url = 'login'

class PostUpdateView(UpdateView):
  model = Post
  template_name = 'update_post.html'
  fields = ['title']

class PostDeleteView(DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy("posts")

class SignUp(CreateView):
  form_class = CustomUserCreationForm
  template_name = 'signup.html'
  success_url = reverse_lazy("login")