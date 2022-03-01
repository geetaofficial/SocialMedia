from urllib import request
from django.shortcuts import render, redirect
from .models import Post
from comment.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect


# Create your views here.


class AllPosts(LoginRequiredMixin, ListView):

    template_name = 'post_list.html'
    model = Post
    paginate_by = 3
    def get_queryset(self):
        queryset = ListView.get_queryset(self)
        my_post = queryset.filter(user=self.request.user)
        return my_post


class PostDetail(LoginRequiredMixin, DetailView):

    template_name = 'post_detail.html'
    model = Post



class CreatePost(LoginRequiredMixin,  CreateView):

    model = Post
    fields = ('title', 'img', 'caption','private')
    template_name = 'post_form.html'
    # success_message = "post was updated successfully"

    # success_url=reverse_lazy('post-detail')

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.request.user
        # form.save()
        messages.success(self.request,'Post Created Successfully.')
        return CreateView.form_valid(self, form, *args, **kwargs)



class UpdatePost(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Post
    fields = ("title", "img", "caption", "user")
    template_name = 'post_form.html'
    success_url = reverse_lazy('all-posts')
    # success_message = "post was updated successfully"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        if not form.instance.user == self.request.user:
                messages.warning(self.request,'you can not change the user.')
                form.instance.user = self.request.user
        else:
            messages.success(self.request,'post was updated successfully')              
        return UpdateView.form_valid(self, form) 

    def dispatch(self, request, *args, **kwargs):
        # print('dispatch hi deside karta hai k  kaha jana hai like get ya post ya put ya wahtever')
        obj = self.get_object()
        if not obj.user == self.request.user:
            messages.warning(self.request, 'You do not have permission')
            return HttpResponseRedirect(self.success_url)
        return UpdateView.dispatch(self, request, *args, **kwargs)


class DeletePost(DeleteView):

    model = Post
    fields = '__all__'
    template_name = 'post_del.html'
    success_url = reverse_lazy('all-posts')

    def dispatch(self, request, *args, **kwargs):
        # print('dispatch hi deside karta hai k  kaha jana hai like get ya post ya put ya wahtever')
        obj = self.get_object()
        if not obj.user == self.request.user:
            messages.warning(self.request, 'You do not have permission')
            return HttpResponseRedirect(self.success_url)
        return DeleteView.dispatch(self, request, *args, **kwargs)

class PublicPostListView(ListView):
    template_name = 'publicpost_list.html'
    model = Post
    # queryset = Post.objects.filter(private=False)
    queryset = Post.objects.public_post()
    paginate_by = 3