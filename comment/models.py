from django.db import models
from django.urls import reverse

# Create your models here.

class Comment(models.Model):
    posts = models.ForeignKey('post.Post',on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']    

    # def post_class_list(self):
    #     p = [s.id for s in self.posts.all()]
    #     return p

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("comment-detail", kwargs={"pk": self.pk})

    # def get_update_url(self):
    #     return reverse("comment-update", kwargs={"pk": self.pk})


    # def get_delete_url(self):
    #     return reverse("comment-delete", kwargs={"pk": self.pk})
