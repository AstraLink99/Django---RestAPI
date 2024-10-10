from django.db import models

class Student(models.Model):

    GENDERS = (
        ("F","Female"),
        ("M","Male")
    )
    name = models.CharField(max_length=100)
    rollno = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=1 , choices=GENDERS)
    percentage = models.FloatField()

    institute = models.ForeignKey("Institute",on_delete= models.CASCADE ,null=True , blank=True)

    def __str__(self):
       return self.name
class Institute(models.Model):

    Types = (
        ("c", "college"),
        ("h","highschool")
    )
    name = models.CharField(max_length=100)
    type_of_institute = models.CharField(max_length=1, choices=Types)

    def __str__(self):
       return self.name

    