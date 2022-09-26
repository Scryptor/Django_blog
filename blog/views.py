from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from blog.models import Article
from blog.serializer import BlogSerializer
from comments.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.forms import BlogFilterForm
from django.db.models import Q, Count
from comments.models import Comments


class PagePagination(PageNumberPagination):
    page_size = 3


class BlogView(ModelViewSet):
    queryset = Article.objects.all()

    def get_queryset(self):
        return Article.objects.annotate(
            num_comments=Count("comments")
        ).filter(active=True)

    serializer_class = BlogSerializer
    pagination_class = PagePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['creation_date']
    search_fields = ['title', 'full_text']


def blog_app(request):
    return render(request, 'blog/blog_app.html')


def blog_list(request):
    blog = Article.objects.annotate(num_comments=Count("comments")).filter(active=True)
    blog = blog.order_by("-creation_date")
    form = BlogFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["query"]:
            blog = blog.filter(
                Q(title__icontains=form.cleaned_data["query"].strip()) |
                Q(full_text__icontains=form.cleaned_data["query"].strip())
            )
    return render(request, "blog/blog_list.html", {"blog": blog})


def blog_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, active=True)
    comment = Comments.objects.filter(article=article_id, active=True)
    comment = comment.order_by("date")
    form = CommentForm(request.POST or None, initial={"article": article})
    if request.method == "POST":
        if form.is_valid():
            form.save()
            url = reverse("article", kwargs={"article_id": article.id})
            return HttpResponseRedirect(f"{url}")

    return render(request, "blog/blog_article.html", {
        "article": article,
        "comment": comment,
        "form": form,
        "sent": request.GET.get("sent")
    })
