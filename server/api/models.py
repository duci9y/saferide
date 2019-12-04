from django.contrib.gis.db import models
from django.contrib.auth.models import User as dj_user

# Users Table
class User(models.Model):
    uuid                = models.CharField(max_length=60, primary_key=True)
    datetime_created    = models.DateTimeField(auto_now_add=True)
    datetime_updated    = models.DateTimeField(auto_now=True)
    abuse_lock          = models.BooleanField(default=False)
    active              = models.BooleanField(default=True)

    def __str__(self):
        return self.uuid


# Drivers Table
class Driver(models.Model):
    user                = models.OneToOneField(dj_user,
                                               on_delete=models.CASCADE)
    current_loc         = models.PointField(null=True)
    on_duty             = models.BooleanField(default=False)
    datetime_created    = models.DateTimeField(auto_now_add=True)
    datetime_updated    = models.DateTimeField(auto_now=True)
    active              = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name

    def as_dict(self):
        return {'user': self.user.pk,
                'current_loc': str(self.current_loc),
                'on_duty': self.on_duty,
                'datetime_created': str(self.datetime_created),
                'datetime_updated': str(self.datetime_updated),
                'active': self.active
                }


# Rides Table
class Ride(models.Model):
    start_loc           = models.PointField(null=True)
    end_loc             = models.PointField(null=True)
    datetime_created    = models.DateTimeField(auto_now_add=True)
    datetime_updated    = models.DateTimeField(auto_now=True)
    datetime_ended      = models.DateTimeField(null=True)
    active              = models.BooleanField(default=True)
    cofirmed            = models.BooleanField(default=False)
    completed           = models.BooleanField(default=False)
    abuse_locked        = models.BooleanField(default=False)
    rider               = models.ForeignKey(User,
                                            on_delete=models.CASCADE,
                                            null=True)
    driver              = models.ForeignKey(Driver,
                                            on_delete=models.CASCADE,
                                            null=True)

    def __str__(self):
        if self.abuse_locked:
            return "Locked ride at " % self.datetime_created

        return "Ride at %s" % self.datetime_created
