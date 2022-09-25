from django.db import models
from ckeditor.fields import RichTextField


class AboutMe(models.Model):
    fio = models.CharField("ФИО", max_length=30)
    birthday = models.DateField("День рождения")
    nik = models.CharField("Ник", max_length=15)
    avatar = models.ImageField("Аватар", upload_to="blog/imgs", default="",
                               blank=True)
    contacts_tg = models.CharField("Телеграм", max_length=100)
    contacts_vk = models.CharField("Вконтакте", max_length=100)
    contacts_youtube = models.CharField("Youtube", max_length=100)
    contacts_habr = models.CharField("habr", max_length=100)
    contacts_pikabu = models.CharField("Пикабу", max_length=100)

    about = RichTextField("Обо мне", blank=True, null=True)

    class Meta:
        verbose_name = "я"
        verbose_name_plural = "я"
