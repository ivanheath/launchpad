from django.db import models
from django.utils import timezone
import datetime
from django.dispatch import dispatcher
from django.db.models import signals
#from main.views import news_added

class newsitem(models.Model):
    user_name = models.CharField(max_length=200)
    news_title = models.CharField(max_length=200)
    news_body = models.TextField(blank=True)
    pub_date = models.DateTimeField('published date')


#dispatcher.connect(main.views.news_added, signal=signals.post_save, sender=newsitem)
