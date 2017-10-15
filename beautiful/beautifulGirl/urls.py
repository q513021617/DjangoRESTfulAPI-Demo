# author: Jhon
# coding=utf-8
from rest_framework import routers
from .views import GirlSet
router = routers.DefaultRouter()
router.register(r'girl', GirlSet)
