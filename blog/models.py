from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField("заголовок", max_length=100)
    full_text = RichTextField("текст", blank=True, null=True)
    creation_date = models.DateTimeField("дата создания", auto_now_add=True)
    preview = models.ImageField("превью", upload_to="blog/imgs", default="",
                                blank=True)
    active = models.BooleanField("активное", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["-creation_date"]

