from django.db import models

# Create your models here.
class GuestLog(models.Model):
    content = models.TextField()

    def __str__(self) -> str:
        return super().__str__()

class GuestComment(models.Model):
    logID = models.IntegerField()
    comment = models.TextField()

    def __str__(self) -> str:
        return super().__str__()