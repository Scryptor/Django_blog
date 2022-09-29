from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from prodmenu.models import Prodmenu


class ProdmenuSerializer(ModelSerializer):
    class Meta:
        model = Prodmenu
        fields = '__all__'
