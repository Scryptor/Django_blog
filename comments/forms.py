from django import forms
from comments.models import Comments
from blog.models import Article


class CommentForm(forms.ModelForm):
    article = forms.ModelChoiceField(queryset=Article.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Comments
        fields = ["author_name", "text", "article"]
