from django.contrib import admin
from django.urls import path
from image_zone_display import views
from rest_framework.routers import DefaultRouter,url


image_detail=views.ImageViewSet.as_view({'get':'find'})
image_list=views.ImageViewSet.as_view({'get':'list','post':'create'})
image_edit=views.ImageViewSetDetail.as_view()

router=DefaultRouter()
router.register('images',views.ImageViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('imageslist/',image_list,name='image_list'),
    url(r'^imagesdetail/(?P<pk>[0-9]+)$',image_edit,name='image_list'),

]
