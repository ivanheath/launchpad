from django.db import models
import datetime

class maintenance(models.Model):
    maint_name = models.CharField(max_length=50)
    maint_time = models.DateTimeField("Maintenance_Time")
    ticket_number = models.CharField(max_length=50)
    ticket_link = models.URLField()
    company = models.CharField(max_length=50)
