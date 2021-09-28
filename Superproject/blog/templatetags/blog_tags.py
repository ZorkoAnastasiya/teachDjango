from django import template
from blog.models import Rubrics


register = template.Library()


@register.inclusion_tag("blog/list_rubrics.html")
def show_rubrics():
    rubrics = Rubrics.objects.all()
    return {"rubrics": rubrics}
