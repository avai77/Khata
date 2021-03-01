from django.db import models
# Create your models here.

class Category(models.Model):
    typeOfAd = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.typeOfAd

    class Meta:
        verbose_name_plural = "Categories"

