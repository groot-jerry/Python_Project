from django.contrib import admin

# Register your models here.

from technicians.models import Technician

admin.site.register(Technician)