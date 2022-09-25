from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from aboutme.models import AboutMe
from aboutme.serializer import AboutMeSerializer


class AboutMeView(ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer



def aboutme_app(request):
    return render(request, 'aboutme/aboutme_app.html')
