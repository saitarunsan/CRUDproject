from django.db import models

# Create your models here.
class ClientInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("ClientInfo")
        verbose_name_plural = ("ClientInfo")

    def __str__(self):
        return self.name