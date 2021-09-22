from django.db import models


class Post(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length = 150)
    content = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(upload_to = "photos/", blank = True)
    hidden = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        return f"/blog/{self.pk}/"

