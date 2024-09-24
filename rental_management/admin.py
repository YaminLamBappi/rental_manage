from django.contrib import admin
from .models import Unit, Flat, Tenant, RentCollection, Invoice

admin.site.register(Unit)
admin.site.register(Flat)
admin.site.register(Tenant)
admin.site.register(RentCollection)
admin.site.register(Invoice)
