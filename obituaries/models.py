from django.db import models

class Obituary(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name

