from django.db import models

# Create your models here.


class bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_request = models.TextField(black=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
