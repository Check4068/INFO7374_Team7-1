from django.contrib import admin

# Register your models here.
from .models import Car
from .models import Neighbor

admin.site.register(Car)
admin.site.register(Neighbor)
