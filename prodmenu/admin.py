from django.contrib import admin

from prodmenu.models import Prodmenu, ProdmenuType


# Register your models here.
@admin.register(Prodmenu)
class ProdMenuAdmin(admin.ModelAdmin):
    list_display = ["name", "active", 'image']
    ordering = ["-active"]


@admin.register(ProdmenuType)
class ProdmenuTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
