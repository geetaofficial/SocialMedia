from .views import Home
from django.urls import path, include
from .views import CustomLoginView, SignupView, ConfirmLogoutView, CustomLogoutView
from .views import ProfileDetail, UpdateProfile, DeleteProfile, AllProfiles


urlpatterns = [
    path('', Home.as_view(), name ='home'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('signup/',SignupView.as_view(), name='signup'),
    path('logout-confirm/',ConfirmLogoutView.as_view(), name='logout-confirm'),
    path('logout/',CustomLogoutView.as_view(), name='logout'),    
    path('all-profile/',AllProfiles.as_view(), name='all-profiles'),
    path('detail-profile/<int:pk>/',ProfileDetail.as_view(), name='profile-detail'),
    path('update-profile/<int:pk>/',UpdateProfile.as_view(), name='update-profile'),
    path('delete-profile/<int:pk>/',DeleteProfile.as_view(), name='delete-profile'),
]