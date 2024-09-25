from django.shortcuts import render, get_object_or_404, redirect
from .models import Tenant, Unit, Flat, RentCollection
from .forms import TenantForm, UnitForm, FlatForm, RentCollectionForm
from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "rental_management/dashboard.html")


@login_required
def dashboard(request):
    tenants = Tenant.objects.count()
    flats = Flat.objects.count()
    units = Unit.objects.count()
    total_rent_collected = RentCollection.objects.count()

    return render(
        request,
        "rental_management/dashboard.html",
        {
            "tenants": tenants,
            "flats": flats,
            "units": units,
            "total_rent_collected": total_rent_collected,
        },
    )


@login_required
def tenant_list(request):
    tenants = Tenant.objects.all()
    flats = Flat.objects.all()  # Fetch all flats
    units = Unit.objects.all()  # Fetch all units

    # Optionally, you could add filtering logic here if needed

    context = {
        "tenants": tenants,
        "flats": flats,
        "units": units,
    }
    return render(request, "rental_management/tenant_list.html", context)


@login_required
def tenant_create(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            unit = tenant.unit
            if unit:
                unit.status = "occupied"
                unit.save()
            return redirect("tenant_list")
    else:
        form = TenantForm()

    return render(request, "rental_management/tenant_form.html", {"form": form})


@login_required
def tenant_edit(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == "POST":
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect("tenant_list")
    else:
        form = TenantForm(instance=tenant)
    return render(request, "rental_management/tenant_form.html", {"form": form})


@login_required
def tenant_delete(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == "POST":
        tenant.delete()
        return redirect("tenant_list")
    return render(
        request, "rental_management/tenant_confirm_delete.html", {"tenant": tenant}
    )


@login_required
def flat_list(request):
    flats = Flat.objects.all()
    return render(request, "rental_management/flat_list.html", {"flats": flats})


@login_required
def flat_create(request):
    if request.method == "POST":
        form = FlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flat_list")
    else:
        form = FlatForm()
    return render(request, "rental_management/flat_form.html", {"form": form})


@login_required
def flat_edit(request, pk):
    flat = get_object_or_404(Flat, pk=pk)
    if request.method == "POST":
        form = FlatForm(request.POST, instance=flat)
        if form.is_valid():
            form.save()
            return redirect("flat_list")
    else:
        form = FlatForm(instance=flat)
    return render(request, "rental_management/flat_form.html", {"form": form})


@login_required
def flat_delete(request, pk):
    flat = get_object_or_404(Flat, pk=pk)
    if request.method == "POST":
        flat.delete()
        return redirect("flat_list")
    return render(request, "rental_management/flat_confirm_delete.html", {"flat": flat})


@login_required
def unit_list(request):
    units = Unit.objects.all()
    return render(request, "rental_management/unit_list.html", {"units": units})


@login_required
def unit_create(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("unit_list")
    else:
        form = UnitForm()
    return render(request, "rental_management/unit_form.html", {"form": form})


@login_required
def unit_edit(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == "POST":
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect("unit_list")
    else:
        form = UnitForm(instance=unit)
    return render(request, "rental_management/unit_form.html", {"form": form})


@login_required
def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == "POST":
        unit.delete()
        return redirect("unit_list")
    return render(request, "rental_management/unit_confirm_delete.html", {"unit": unit})


@login_required
def rent_collection_list(request):
    rent_collections = RentCollection.objects.all()
    return render(
        request,
        "rental_management/rent_collection_list.html",
        {"rent_collections": rent_collections},
    )


@login_required
def rent_collection_create(request):
    if request.method == "POST":
        form = RentCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rent_collection_list")
        else:
            print(form.errors)  # This will help identify validation issues
    else:
        form = RentCollectionForm()

    return render(
        request, "rental_management/rent_collection_form.html", {"form": form}
    )


@login_required
def search_tenant(request):
    query = request.GET.get("query", "")
    tenants = Tenant.objects.filter(name__icontains=query) | Tenant.objects.filter(
        phone_number__icontains=query
    )

    tenant_list = [
        {"id": tenant.id, "name": tenant.name, "phone_number": tenant.phone_number}
        for tenant in tenants
    ]

    return JsonResponse({"tenants": tenant_list})


@login_required
def tenant_details(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)

    tenant_data = {
        "name": tenant.name,
        "flat": {"flat_number": tenant.flat.flat_number},
        "unit": {"name": tenant.unit.name},
        "phone_number": tenant.phone_number,
        "email": tenant.email,
        "rent": tenant.rent,
    }

    return JsonResponse(tenant_data)


@login_required
def rent_collection_edit(request, pk):
    rent_collection = get_object_or_404(RentCollection, pk=pk)
    if request.method == "POST":
        form = RentCollectionForm(request.POST, instance=rent_collection)
        if form.is_valid():
            form.save()
            return redirect("rent_collection_list")
    else:
        form = RentCollectionForm(instance=rent_collection)
    return render(
        request, "rental_management/rent_collection_form.html", {"form": form}
    )


@login_required
def rent_collection_delete(request, pk):
    rent_collection = get_object_or_404(RentCollection, pk=pk)
    if request.method == "POST":
        rent_collection.delete()
        return redirect("rent_collection_list")
    return render(
        request,
        "rental_management/rent_collection_confirm_delete.html",
        {"rent_collection": rent_collection},
    )
