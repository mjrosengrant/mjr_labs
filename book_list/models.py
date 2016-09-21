from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
import datetime

# http://django-polymorphic.readthedocs.io/en/stable/
from polymorphic.models import PolymorphicModel

class Kit(PolymorphicModel):
    slug = models.SlugField()

    INACTIVE = 0
    ACTIVE = 1
    REGISTERED = 2
    STATUS_CHOICES = (
        (INACTIVE, 'Inactive'),
        (ACTIVE, 'Active'),
        (REGISTERED, 'Registered')
    )
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=INACTIVE)

    def test(self):
        print "This comes from Kit Model!"

    def __unicode__(self):
        return self.slug

class OrageneKit(Kit):
    tube_barcode = models.CharField(max_length=14)
    work_order = models.PositiveIntegerField(null=True, blank=True)
    part_number = models.CharField(max_length=64, null=True, blank=True)
    lot_number = models.CharField(max_length=64, null=True, blank=True)
    box_number = models.PositiveSmallIntegerField(null=True, blank=True)
    tray_number = models.PositiveSmallIntegerField(null=True, blank=True)
    package_barcode = models.CharField(max_length=14, null=True, blank=True)

    def __unicode__(self):
        return self.slug


class CustomKit(Kit):
    # Small detail about where this kit came from
	origin = models.CharField(max_length=64, null=True, blank=True, help_text="Brief description of where this kit came from")
