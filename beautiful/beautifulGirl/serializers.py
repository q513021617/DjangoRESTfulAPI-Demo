from django.contrib.auth.models import User, Group
from rest_framework import serializers
from beautifulGirl.models import Beautiful


class GirlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beautiful
        fields = ("id", "GirlName", "ImageUrl")
