from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Site(models.Model):
    name = models.CharField(max_length=64)


class Prey(models.TextChoices):
    DAPNHIA = "DAPNHIA", "Daphnia"


class SiteYearMonthDepthMixin(models.Model):
    class Meta:
        abstract = True
        indexes = [models.Index(fields=["site", "year", "month"])]

    depth = models.FloatField(help_text="Depth in meters")
    year = models.IntegerField()
    month = models.IntegerField(
        help_text="Month (1-12)",
        validators=[MinValueValidator(1), MaxValueValidator(12)],
    )
    site = models.ForeignKey("data_entities.Site", on_delete=models.CASCADE)


class PreyData(SiteYearMonthDepthMixin):
    species = models.CharField(max_length=64, choices=Prey.choices)
    abundance = models.IntegerField()


class Bathymetry(models.Model):
    elevation = models.FloatField()
    area2d = models.FloatField()
    site = models.ForeignKey("data_entities.Site", on_delete=models.CASCADE)

    @property
    def elevation_feet(self):
        return self.elevation * 3.28084


class Temperature(SiteYearMonthDepthMixin):
    temperature = models.FloatField(help_text="Temperature in degrees C")
