from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from blog.models import Article


class BlogSerializer(ModelSerializer):
    num_comments = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'creation_date', 'full_text', 'preview', 'num_comments']
