from django.db import models


# Create your models here.

class Rack(models.Model):
  UserName = models.CharField(max_length=30)
  Sequence=models.IntegerField(auto_created=True)
  Code=models.CharField(max_length=10,unique=True)
  Rows=models.IntegerField()
  Columns=models.CharField(max_length=10)
  ShortName=models.CharField(max_length=15)
  StandardName=models.CharField(max_length=50)
  Description=models.CharField(max_length=250)
  Remarks=models.CharField(max_length=250)
  Active=models.BooleanField()
  AddedBy=models.CharField(max_length=30)
  AddedDate=models.DateTimeField()
  UpdatedBy=models.CharField(max_length=30)
  UpdatedDate=models.DateTimeField()
  
    # The ForeignKey links this Rack to one StorageLocation
  StorageLocationId = models.ForeignKey(
        'storagelocations.StorageLocation', # AppName.ModelName
        on_delete=models.CASCADE,
        related_name='storagelocations'
    )

   
  def __str__(self):
    return f"{self.Code}"