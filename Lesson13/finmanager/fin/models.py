from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=250)
    type_of_category = models.BooleanField(default=False) # if false this means for expensive category
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}: {self.description}"


class Losses(models.Model):
    lose_name = models.ForeignKey(TypeLosses, on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}{self.lose_name} - {self.total}"