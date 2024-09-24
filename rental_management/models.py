from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Flat(models.Model):
    flat_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.flat_number


class Unit(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[("occupied", "Occupied"), ("vacant", "Vacant")],
        default="vacant",
    )

    def __str__(self):
        return f" {self.name}"


class Tenant(models.Model):
    name = models.CharField(null=True, max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(null=True, max_length=15)
    flat = models.ForeignKey("Flat", on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.ForeignKey("Unit", on_delete=models.SET_NULL, null=True, blank=True)
    rent = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def rental_history(self):
        return self.rentcollection_set.all()

    def current_status(self):
        return "Occupied" if self.is_active else "Vacated"


class RentCollection(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    water_bill = models.DecimalField(max_digits=10, decimal_places=2)
    gas_bill = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    wifi_charge = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )  # Define total field
    payment_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Calculate the total based on tenant's rent and other charges
        self.total = (
            self.tenant.rent  # Rent comes from the Tenant model
            + self.water_bill
            + self.gas_bill
            + self.service_charge
            + self.wifi_charge
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Rent for {self.tenant.name}"


class Invoice(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    rent_collection = models.OneToOneField(RentCollection, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice for {self.tenant.first_name} {self.tenant.last_name} on {self.date}"
