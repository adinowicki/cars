from django.db import models
from rest_framework import mixins, viewsets

from . import models as cars_models
from . import serializers


class CarViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.CarSerializer
    queryset = (
        cars_models.Car.objects.all()
        .annotate(avg_rating=models.Avg("ratings__rating"))
        .order_by("pk")
    )


class RateViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.RateSerializer


class PopularViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.PopularCarSerializer
    queryset = (
        cars_models.Car.objects.all()
        .annotate(rates_number=models.Count("ratings"))
        .order_by("-rates_number", "pk")
    )
