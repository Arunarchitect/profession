from django.db import models
from django.utils import timezone


# Create your models here.

class job(models.Model):
    date = models.DateTimeField('Date', default=timezone.now)
    work = models.CharField(max_length=100)

    def __str__(self):
        return self.works


    @property
    def slug(self):
        return self.job_slug
    
    class Meta:
        verbose_name_plural = "job"
        ordering = ['date']