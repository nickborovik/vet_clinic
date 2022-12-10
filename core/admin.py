from django.contrib import admin
from core.models import Animal, AnimalType, Appointment


for model in [Animal, AnimalType, Appointment]:
    admin.site.register(model)
