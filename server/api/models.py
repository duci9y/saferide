from django.contrib.gis.db import models

# Create your models here.
class User(models.Model):
    uuid        = models.CharField(max_length=60)
    abuse_lock  = models.BooleanField(default=False)
    datetime_created    = models.DateTimeField(auto_now_add=True)
    datetime_updated    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uuid

class Ride(models.Model):
    start_loc           = models.PointField(null=True)
    end_loc             = models.PointField(null=True)
    datetime_created    = models.DateTimeField(auto_now_add=True)
    datetime_updated    = models.DateTimeField(auto_now=True)
    rider_uid           = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
    )
