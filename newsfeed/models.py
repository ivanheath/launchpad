from django.db import models
import datetime

class newsitem(models.Model):
    user_name = models.CharField(max_length=200)
    news_title = models.CharField(max_length=200)
    news_body = models.TextField(blank=True)
    pub_date = models.DateTimeField('published date')
    receiver_name = models.CharField(max_length=200)

