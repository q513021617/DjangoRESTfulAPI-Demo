from rest_framework import serializers
from image_zone_display.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ("id", "image_title", "image_url","image_description")
