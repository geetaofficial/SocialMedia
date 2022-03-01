from django.urls import path, include
from .views import AllPosts, CreatePost, UpdatePost, DeletePost, PostDetail, PublicPostListView



urlpatterns = [
    path('all/',AllPosts.as_view(), name='all-posts'),
    path('detail/<int:pk>/',PostDetail.as_view(), name='post-detail'),
    path('create/',CreatePost.as_view(), name='create'),
    path('update/<int:pk>/',UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>/',DeletePost.as_view(), name='delete'),
    path('public-posts/',PublicPostListView.as_view(), name='public-posts'),
    ]