from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import json

from .serializers import UserSerializer, DriverSerializer, RideSerializer
from .models import User, Driver, Ride


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post', 'get'], name='Create a new ride')
    def create_ride(cls, request, pk=None):
        # NOTE: request.data returns a query dictionary, not regular dict
        driver_obj = Driver.objects.all().first()
        serializer = DriverSerializer(driver_obj, context={'request': request})

        user_obj = User.objects.get(pk=pk)
        serializer = UserSerializer(user_obj, context={'request': request})

        if (user_obj.abuse_lock):
            return Response('Ride denied - user is abuse locked', status=status.HTTP_403_FORBIDDEN)

        request_data = request.data.__getitem__('abuse_lock')

        return Response(request_data, status=status.HTTP_200_OK)
        # return Response(serializer.data, status=status.HTTP_200_OK)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by('on_duty')
    serializer_class = DriverSerializer


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().order_by('active')
    serializer_class = RideSerializer
