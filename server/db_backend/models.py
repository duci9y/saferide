from django.contrib.gis.db import models

# Create your models here.
class User(models.Model):
    uuid        = models.CharField(max_length=60)
    abuse_lock  = models.BooleanField(default=False)

    def __str__(self):
        return self.uuid

class Ride(models.Model):
    start_loc = models.PointField(null=True)
    end_loc   = models.PointField(null=True)
    rider_uid = models.ForeignKey(
            'auth.User', on_delete=models.CASCADE,
    )
