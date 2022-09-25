from django.db import models
from blog.models import Article


class Comments(models.Model):
    article = models.ForeignKey(Article, verbose_name="Запись",
                                on_delete=models.CASCADE)
    author_name = models.CharField("имя автора", max_length=30, default="Гость")
    text = models.TextField("текст комментария", default="")
    date = models.DateTimeField("дата создания", auto_now_add=True)
    active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарий"
        ordering = ["-date"]
