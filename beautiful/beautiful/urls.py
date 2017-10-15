from django.conf.urls import url, include
from django.contrib import admin
from beautifulGirl import views
from beautifulGirl.urls import router
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^api/beautifulGirl/', include(router.urls)),
]
