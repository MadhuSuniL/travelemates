from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TripsData  # replace with your model


@admin.register(TripsData)
class MyModelAdmin(ImportExportModelAdmin):
    pass
