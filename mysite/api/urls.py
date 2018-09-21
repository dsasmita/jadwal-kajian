from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'/schedule', views.ScheduleViewSet)
router.register(r'/mosque', views.MosqueViewSet)
router.register(r'/city', views.CityViewSet)
router.register(r'/province', views.ProvinceViewSet)
router.register(r'/ustad', views.UstadViewSet)

app_name = 'api'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]