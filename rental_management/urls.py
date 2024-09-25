from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Dashboard view
    path("dashboard/", views.dashboard, name="dashboard"),
    # Tenant views
    path("tenants/", views.tenant_list, name="tenant_list"),
    path("tenants/add/", views.tenant_create, name="add_tenant"),
    path("tenants/edit/<int:pk>/", views.tenant_edit, name="edit_tenant"),
    path("tenants/delete/<int:pk>/", views.tenant_delete, name="delete_tenant"),
    # Flat views
    path("flats/", views.flat_list, name="flat_list"),
    path("flats/add/", views.flat_create, name="add_flat"),
    path("flats/edit/<int:pk>/", views.flat_edit, name="edit_flat"),
    path("flats/delete/<int:pk>/", views.flat_delete, name="delete_flat"),
    # Unit views
    path("units/", views.unit_list, name="unit_list"),
    path("units/add/", views.unit_create, name="add_unit"),
    path("units/edit/<int:pk>/", views.unit_edit, name="edit_unit"),
    path("units/delete/<int:pk>/", views.unit_delete, name="delete_unit"),
    # Rent Collection views
    path("rent-collections/", views.rent_collection_list, name="rent_collection_list"),
    path(
        "rent-collections/add/",
        views.rent_collection_create,
        name="add_rent_collection",
    ),
    path(
        "rent-collections/edit/<int:pk>/",
        views.rent_collection_edit,
        name="edit_rent_collection",
    ),
    path(
        "rent-collections/delete/<int:pk>/",
        views.rent_collection_delete,
        name="delete_rent_collection",
    ),
    path("search_tenant/", views.search_tenant, name="search_tenant"),
    path(
        "tenant_details/<int:tenant_id>/", views.tenant_details, name="tenant_details"
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
