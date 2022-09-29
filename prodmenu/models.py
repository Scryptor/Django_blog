from django.db import models


class Prodmenu(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)
    creation_date = models.DateTimeField("дата создания", auto_now_add=True)
    type_id = models.ForeignKey("ProdmenuType", on_delete=models.PROTECT)
    image = models.ImageField("фото", upload_to="blog/imgs", default="",
                              blank=True)
    times_eaten = models.IntegerField("Сколько раз поели", default=0)
    last_time_eaten = models.DateField("последний раз ели", default="2000-01-01")
    active = models.BooleanField("активное", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class ProdmenuType(models.Model):
    type_name = models.CharField("Тип", max_length=100)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Тип еды"
        verbose_name_plural = "Типы еды"
