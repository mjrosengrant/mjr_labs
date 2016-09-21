from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
"""Administrative Settings."""

from django.contrib import admin
from .models import CustomKit, Kit, OrageneKit


# Register your models here.
admin.site.register(Kit)
admin.site.register(CustomKit)
admin.site.register(OrageneKit)