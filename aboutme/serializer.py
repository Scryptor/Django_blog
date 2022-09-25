from rest_framework.serializers import ModelSerializer

from aboutme.models import AboutMe


class AboutMeSerializer(ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'
