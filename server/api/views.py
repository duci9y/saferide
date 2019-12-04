from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from json import dumps

from .serializers import UserSerializer, DriverSerializer, RideSerializer
from .models import User, Driver, Ride


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post', 'get'], name='Create a new ride')
    def create_ride(self, request, pk=None):
        driver_obj = Driver.objects.all().first()
        serializer = DriverSerializer(driver_obj, context={'request': request})

        user_obj = User.objects.get(pk=pk)
        serializer = UserSerializer(user_obj, context={'request': request})

        # if (user_obj.abuse_lock):
        #     print('Cannot provide a ride to user (abuse_lock active)')
        # else:
            # add driver and user to ride-entry
            # push new entry to ride-Table

        return Response(serializer.data, status=status.HTTP_200_OK)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by('on_duty')
    serializer_class = DriverSerializer


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().order_by('active')
    serializer_class = RideSerializer
