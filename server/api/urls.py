from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'rides', views.RideViewSet)
router.register(r'users/create_ride', views.RideViewSet, basename='rides')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
