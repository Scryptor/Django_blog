from django import forms


class BlogFilterForm(forms.Form):
    query = forms.CharField(label="описание", required=False)
