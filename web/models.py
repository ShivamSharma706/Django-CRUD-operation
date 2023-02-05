from django.db import models

# Create your models here.

class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)


class Uploadimg(models.Model):
    uname=models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    caption=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.firstname + " " + self.lastname
                