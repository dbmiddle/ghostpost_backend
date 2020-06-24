from django.conf.urls import include, url

from api.views import BoastsAndRoastsViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'boastsandroasts', BoastsAndRoastsViewSet, basename='boastandroasts')

urlpatterns = [
    url(r'^api/', include(router.urls))
]
