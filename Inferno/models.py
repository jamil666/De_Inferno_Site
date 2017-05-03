from django.db import models

# Create your models here.

class WFAccount(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Role = models.CharField(max_length=100, blank=True, null=True)
    Date_Of_Receipt = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Name


class Rank (models.Model):
    RankImage = models.FileField(blank=True, upload_to="Inferno/static/images/Ranks")

