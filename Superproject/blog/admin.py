from django.contrib import admin
from blog.models import Post, Rubrics


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "rubric", "created_at", "hidden")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("hidden",)
    list_filter = ("hidden", "rubric")


@admin.register(Rubrics)
class RubricsAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
