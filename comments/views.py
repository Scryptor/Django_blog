from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from comments.models import Comments
from comments.serializer import CommentsSerializer


class CommentsView(ModelViewSet):
    queryset = Comments.objects.filter(active=True)
    serializer_class = CommentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['date']
    filterset_fields = ['article']
