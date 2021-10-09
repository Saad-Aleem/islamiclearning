from abc import abstractproperty
from django.db import models

# Create your models here.
class develop(models.Model):
    article_id = models.AutoField
    article_topic = models.CharField(max_length=100, default='none')
    article_img = models.ImageField(upload_to='{{MEDIA_URL}}', default='{{MEDIA_URL}}sunset.jpg')
    article_category = models.CharField(max_length=50, choices=(('PSY','Psychology'), ('EDU','Educational Philosophy')), default='Psychology')
    writer_name = models.CharField(max_length=50, default='none')
    para1 = models.TextField(default='Para')
    para2 = models.TextField(default='Para')
    para3 = models.TextField(default='Para')
    para4 = models.TextField(default='Para')
    para5 = models.TextField(default='Para')
    para6 = models.TextField(default='Para')
