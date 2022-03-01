from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from PIL import Image
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.


# class CustomUserManager(UserManager):
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)


#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return UserManager._create_user(self,None, email, password, **extra_fields)


class CustomUser(AbstractUser):
    """User Model"""
    email = models.EmailField(unique=True,)
    # username=None
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    # objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'



    


    

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profiles', null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    website= models.CharField(max_length=256, null=True, blank=True)
    bio = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} Profile'

    def get_absolute_url(self):
        return reverse("profile-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update-profile", kwargs={"pk": self.pk})


    def get_delete_url(self):
        return reverse("delete-profile", kwargs={"pk": self.pk})


# create the user profile is a new user created
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


# attached a post save signal to the user model
post_save.connect(create_user_profile, sender=CustomUser)