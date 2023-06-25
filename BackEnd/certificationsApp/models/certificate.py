from django.db import models
from .user import User
import uuid

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    person_id = models.CharField('person_id', max_length=200)
    city = models.CharField('city', max_length=200)
    name = models.CharField('name', max_length=200)
    description = models.CharField('description', max_length=512)
    date = models.DateField('date', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name