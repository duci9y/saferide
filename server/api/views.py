from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, DriverSerializer, RideSerializer
from .models import User, Driver, Ride


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('uuid')
    serializer_class = UserSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by('on_duty')
    serializer_class = DriverSerializer


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().order_by('active')
    serializer_class = RideSerializer
