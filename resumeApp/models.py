from django.db import models

# Create your models here.

class resumeModel(models.Model):
    ProfilePicture=models.ImageField(upload_to='static/picture', null=True)
    FullName=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    Phone=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    CareerObjective=models.TextField(null=True)
    Skills=models.CharField(max_length=50,null=True)
    Certification=models.CharField(max_length=50,null=True)
    Projects=models.CharField(max_length=50,null=True)
    References=models.CharField(max_length=50,null=True)


class educationModel(models.Model):
    Degree=models.CharField(max_length=50,null=True)
    Institution=models.CharField(max_length=50,null=True)
    GraduationYear=models.CharField(max_length=50,null=True)


class workModel(models.Model):
    Company=models.CharField(max_length=50,null=True)
    Position=models.CharField(max_length=50,null=True)
    StartDate=models.CharField(max_length=50,null=True)
    EndDate=models.CharField(max_length=50,null=True)
