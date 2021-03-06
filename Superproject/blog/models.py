from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy


User = get_user_model()


class Rubrics(models.Model):
    objects = models.Manager()

    title = models.CharField(
        max_length = 150,
        db_index = True,
        verbose_name = "rubric"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        return reverse_lazy(
            "blog:rubric",
            kwargs = {"rubric_id": self.pk})

    class Meta:
        verbose_name = "rubric"
        verbose_name_plural = "rubrics"
        ordering = ["id"]


class Post(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length = 150)
    content = models.TextField(
        blank = True,
        null = True
    )
    created_at = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(
        upload_to = "photos/",
        blank = True
    )
    hidden = models.BooleanField(default = False)
    rubric = models.ForeignKey(
        Rubrics,
        on_delete = models.PROTECT,
        null = True
    )
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        return reverse_lazy("blog:single_post", kwargs = {"pk": self.pk})

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-created_at", "title"]
