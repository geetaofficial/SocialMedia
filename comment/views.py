from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from comment.models import Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages
from post.models import Post

# Create your views here.
class AllComments(LoginRequiredMixin, ListView):

    template_name = 'Comment_list.html'
    model = Comment
    paginate_by = 3

class CommentDetail(DetailView):
    model = Comment
    form_class =CommentForm
    template_name = 'post_detail.html'

class CreateComment(CreateView):

    model = Comment
    fields = ('posts', 'content')
    template_name = 'publicpost_list.html'









