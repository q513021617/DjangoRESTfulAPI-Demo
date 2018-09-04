from django.conf.urls import url, include
from django.contrib import admin
from beautiful.beautifulGirl import views
from beautiful.beautifulGirl.urls import router
import sys
sys.path.append('/home/jhon/PycharmProjects/DjangoRESTfulAPI-Demo/beautiful')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^api/beautifulGirl/', include(router.urls)),
]
