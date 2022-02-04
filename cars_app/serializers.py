from rest_framework import serializers

import nhtsa

from . import models


class CarSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = models.Car
        fields = (
            "id",
            "make",
            "model",
            "avg_rating",
        )

    def validate(self, data):
        make = data.get("make")
        model = data.get("model")
        if not nhtsa.make_exists(make=make):
            raise serializers.ValidationError(
                {"make": f'make "{make}" doesn\'t exist'}
            )
        if not nhtsa.model_exists(make=make, model=model):
            raise serializers.ValidationError(
                {"model": f'model "{model}" doesn\'t exist'}
            )
        return data


class RateSerializer(serializers.ModelSerializer):
    car_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Car.objects.all().values_list("id", flat=True)
    )

    class Meta:
        model = models.Rate
        fields = (
            "car_id",
            "rating",
        )


class PopularCarSerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField()

    class Meta:
        model = models.Car
        fields = (
            "id",
            "make",
            "model",
            "rates_number",
        )
