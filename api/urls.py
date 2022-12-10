from django.urls import path
from . import views


urlpatterns = [
    path('animal', views.ListAnimalView.as_view()),
    path('animal/create', views.CreateAnimalView.as_view()),
    path('animal/<int:model_id>', views.DetailAnimalView.as_view()),

    path('animal_type', views.ListAnimalTypeView.as_view()),
    path('animal_type/create', views.CreateAnimalTypeView.as_view()),
    path('animal_type/<int:model_id>', views.DetailAnimalTypeView.as_view()),

    path('appointment', views.ListAppointmentView.as_view()),
    path('appointment/create', views.CreateAppointmentView.as_view()),
    path('appointment/<int:model_id>', views.DetailAppointmentView.as_view()),
]
