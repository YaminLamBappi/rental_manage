from django import forms
from .models import Tenant, Unit, Flat, RentCollection


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = "__all__"  # Adjust if you want to exclude certain fields


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = "__all__"


class RentCollectionForm(forms.ModelForm):
    class Meta:
        model = RentCollection
        fields = "__all__"
