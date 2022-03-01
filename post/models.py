from turtle import title
from django.db import models
from django.urls import reverse
# Create your models here.

class PostManager(models.Manager):

    def public_post(self):
        return super().get_queryset().filter(private=False)
    
    def get_total_public_post(self):
        return super().get_queryset().filter(private=False).count()



class Post(models.Model):
    title = models.CharField(max_length=126, blank=True)
    img = models.ImageField(upload_to='posts', null=True, blank=True)
    caption = models.CharField(max_length=256, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    private = models.BooleanField(default=True)
    # comment = models.ForeignKey('comment.Comment', on_delete=models.CASCADE, default='comment')
    objects = PostManager()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update", kwargs={"pk": self.pk})


    def get_delete_url(self):
        return reverse("delete", kwargs={"pk": self.pk})




