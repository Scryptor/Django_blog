from django.contrib import admin
from comments.models import Comments


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["article", "author_name", "text", "date", "active"]
