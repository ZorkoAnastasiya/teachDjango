from django import template
from blog.models import Rubrics


register = template.Library()


@register.simple_tag(name = "list_rubrics")
def get_rubrics():
    return Rubrics.objects.all()


@register.inclusion_tag("blog/list_rubrics.html")
def show_rubrics():
    rubrics = Rubrics.objects.all()
    return {"rubrics": rubrics}
