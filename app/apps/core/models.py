from django.db import models

# Create your models here.

class CodeQuality(models.Model):
    name = models.CharField(max_length=50)


class Site(models.Model):
    adr = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=60)
    CodeQuality = models.ForeignKey(CodeQuality, on_delete=models.CASCADE, related_name="site")
