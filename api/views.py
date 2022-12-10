from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from core.models import Animal, AnimalType, Appointment
from .serializers import AnimalSerializer, AnimalTypeSerializer, AppointmentSerializer
from .mixins import ListModelView, CreateModelView, DetailModelView


# Animal views
class ListAnimalView(ListModelView):
    model = Animal
    model_serializer = AnimalSerializer


class CreateAnimalView(CreateModelView):
    model = Animal
    model_serializer = AnimalSerializer


class DetailAnimalView(DetailModelView):
    model = Animal
    model_serializer = AnimalSerializer


# Animal Type views
class ListAnimalTypeView(ListModelView):
    model = AnimalType
    model_serializer = AnimalTypeSerializer


class CreateAnimalTypeView(CreateModelView):
    model = AnimalType
    model_serializer = AnimalTypeSerializer


class DetailAnimalTypeView(DetailModelView):
    model = AnimalType
    model_serializer = AnimalTypeSerializer


# Appointment views
class ListAppointmentView(ListModelView):
    model = Appointment
    model_serializer = AppointmentSerializer


class CreateAppointmentView(CreateModelView):
    model = Appointment
    model_serializer = AppointmentSerializer


class DetailAppointmentView(DetailModelView):
    model = Appointment
    model_serializer = AppointmentSerializer
