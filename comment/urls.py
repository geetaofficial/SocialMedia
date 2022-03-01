from django.urls import path, include
from .views import AllComments, CreateComment, CommentDetail

urlpatterns = [
    path('all-comments/',AllComments.as_view(), name='all-comments'),
    path('detail-comment/<int:pk>/',CommentDetail.as_view(), name='comment-detail'),
    path('create-comment/',CreateComment.as_view(), name='create-comment'),
    # path('update/<int:pk>/',UpdatePost.as_view(), name='update'),
    # path('delete/<int:pk>/',DeletePost.as_view(), name='delete'),
    # path('public-posts/',PublicPostListView.as_view(), name='public-posts'),
    ]