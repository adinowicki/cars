from django.core import validators
from django.db import models


class Car(models.Model):
    make = models.CharField(
        max_length=64,
    )
    model = models.CharField(
        max_length=64,
    )

    class Meta:
        unique_together = ["make", "model"]

    def __str__(self):
        return f"{self.make} {self.model}"


class Rate(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="ratings",
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ],
    )

    def __str__(self):
        return f"{self.car.make} {self.car.model}: {self.rating}"
