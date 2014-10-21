from django.db import models


class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u"{}".format(self.url)

class Location(models.Model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    class Meta:
        unique_together = (('country', 'region', 'city'),)

    def __unicode__(self):
        return u"{}, {} {}".format(self.city, self.country, self.region)

class View(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, related_name='views')
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True, related_name='views')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return u"{}, {} @ {}".format(self.ip_address, self.location, self.date)
