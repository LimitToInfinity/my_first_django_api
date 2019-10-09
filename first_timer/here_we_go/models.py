from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class HereWeGo(models.Model):
    name = models.CharField(max_length=50)
    speed = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(999)])