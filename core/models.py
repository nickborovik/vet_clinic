from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50, blank=False)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField(blank=True)

    def __str__(self):
        return f'{self.animal_type}: {self.name}, {self.birth_date}'


class Appointment(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.animal_id.name} - {self.date}'
