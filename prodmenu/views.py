from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from prodmenu.models import Prodmenu
from prodmenu.serializer import ProdmenuSerializer


# Create your views here.
class ProdmenuView(ModelViewSet):
    queryset = Prodmenu.objects.filter(active=True)
    serializer_class = ProdmenuSerializer


def prodmenu_app(request):
    return render(request, 'prodmenu/prodmenu_app.html')
