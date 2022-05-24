from django.db import models

# Create your models here.
class Products(models.Model):
    title = CharField(max_length=255)
    description = CharField
    price = DecimalField
    inventory_quantity = IntegerField