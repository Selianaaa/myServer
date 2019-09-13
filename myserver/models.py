from django.contrib.postgres.fields import ArrayField

from django.db import models


class Item(models.Model):
    id = models.UUIDField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    image_vector = ArrayField(
        models.FloatField(),
        null=True,
    )
    image_width = models.IntegerField(null=True)


    class Meta:
        db_table = 'items'
