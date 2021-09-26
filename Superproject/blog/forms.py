import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "hidden", "rubric"]
        widgets = {
            "title": forms.TextInput(attrs = {
                "class": "form-control"
            }
            ),
            "content": forms.Textarea(attrs = {
                "class": "form-control",
                "rows": 7
            }
            ),
            "rubric": forms.Select(attrs = {
                "class": "form-control"
            }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("There should be no numbers at the beginning")
        return title
