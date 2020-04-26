from django.db import models

class datisd(models.Model):
    r_type = models.CharField(max_length=30)
    r_status = models.CharField(max_length=30)
    r_count = models.PositiveIntegerField()