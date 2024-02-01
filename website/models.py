from django.db import models

class AllUsers01(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name
