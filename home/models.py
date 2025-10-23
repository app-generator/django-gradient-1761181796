# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Device(models.Model):

    #__Device_FIELDS__
    device_id = models.IntegerField(null=True, blank=True)
    vehicle_no = models.CharField(max_length=255, null=True, blank=True)
    device_imei = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)

    #__Device_FIELDS__END

    class Meta:
        verbose_name        = _("Device")
        verbose_name_plural = _("Device")


class Location(models.Model):

    #__Location_FIELDS__
    latitude = models.IntegerField(null=True, blank=True)
    logitude = models.IntegerField(null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    course = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    moving = models.BooleanField()

    #__Location_FIELDS__END

    class Meta:
        verbose_name        = _("Location")
        verbose_name_plural = _("Location")



#__MODELS__END
