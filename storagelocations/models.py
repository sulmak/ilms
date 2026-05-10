from django.db import models

# Create your models here.
class StorageLocation(models.Model):
  UserName = models.CharField(max_length=30)
  Sequence=models.IntegerField(auto_created=True)
  Code=models.CharField(max_length=10,unique=True)
  ShortName=models.CharField(max_length=15)
  StandardName=models.CharField(max_length=50)
  Description=models.CharField(null=True, max_length=250)
  Remarks=models.CharField(null=True, max_length=250)
  Active=models.BooleanField()
  AddedBy=models.CharField(null=True,max_length=30)
  AddedDate=models.DateTimeField(null=True, blank=True)
  AddedFromIP=models.CharField(null=True,max_length=15)
  UpdatedBy=models.CharField(null=True,max_length=30)
  UpdatedDate=models.DateTimeField(null=True, blank=True)
  UpdatedFromIP=models.CharField(null=True,max_length=15)
  
    # Add other location fields here

  def __str__(self):
    return f"{self.UserName}"
