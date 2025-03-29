from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shopName = models.CharField(max_length=100, null=True, blank=False)
    brand = models.CharField(max_length=100, null=True, blank=False)
    description = models.CharField(max_length=100, null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageUrl = models.CharField(max_length=500, null=True, blank=False)

    def __str__(self):
        return f"{self.id}"
