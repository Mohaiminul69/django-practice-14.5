from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("form_fields.urls")),
    path("", include("model_fields.urls")),
]
