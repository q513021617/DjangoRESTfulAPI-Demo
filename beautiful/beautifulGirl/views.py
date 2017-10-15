from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from beautifulGirl.models import Beautiful
from beautifulGirl.serializers import GirlSerializer


class GirlSet(viewsets.ModelViewSet):
    queryset = Beautiful.objects.all()
    serializer_class = GirlSerializer


@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        context = {"msg": "请求成功！", "code": 0}
        return render(request, 'index.html', context)


