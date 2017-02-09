from django.db import models

# Create your models here.
class Roster(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=2)
    points = models.FloatField()
    rebounds = models.FloatField()
    assists = models.FloatField()
    steals = models.FloatField()
    blocks = models.FloatField()
    college = models.CharField(max_length=10)


    def __str__(self):
        return self.name
