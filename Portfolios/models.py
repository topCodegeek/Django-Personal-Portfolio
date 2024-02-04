from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 200)
    profile_picture = models.ImageField(upload_to = "Portfolios/Thumages")
    def __str__(self):
        return self.name