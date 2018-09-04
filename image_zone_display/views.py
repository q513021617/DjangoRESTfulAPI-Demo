from django.shortcuts import render
from rest_framework import permissions,viewsets,renderers,generics
from rest_framework.decorators import api_view
from django.views.generic import View

from image_zone_display.models import Image
from image_zone_display.serializers import ImageSerializer

# Create your views here.


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageViewSetDetail(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset=Image.objects.all()
    serializer_class = ImageSerializer


def index(request):
    if(request.method=='GET'):
        context = {"msg": "GET请求成功！", "code": 0}
        return render(request, 'index.html', {'context':context})

