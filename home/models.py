from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=122)
    user_feedback = models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.name
    
class Registration(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    
    def __str__(self) -> str:
        return self.title




