from django.db import models
import geocoder

token = 'pk.eyJ1IjoibWFja2xhcmsiLCJhIjoiY2t4ZWcyNTVhMXlkNDJvbzFsMGxvYTZ5MCJ9.LJqdd-tSk1E72RaEAQm7MQ'

# Create your models here.
class Address(models.Model):
    address = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=token)
        g = g.latlng
        self.latitude = g[0]
        self.longitude = g[1]
        return super(Address, self).save(*args, **kwargs) 