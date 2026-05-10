from django.db import models



# Create your models here.

class Bin(models.Model):
  UserName = models.CharField(max_length=30)
  Sequence=models.IntegerField(auto_created=True)
  Code=models.CharField(max_length=10,unique=True)
  Rows=models.IntegerField()
  Columns=models.CharField(max_length=10)
  AddedBy=models.CharField(max_length=30)
  AddedDate=models.DateTimeField()
  UpdatedBy=models.CharField( max_length=30)
  UpdatedDate=models.DateTimeField()
  
    # The ForeignKey links this Bin to one Rack
  RackId = models.ForeignKey(
        'racks.Rack', # AppName.ModelName
        on_delete=models.CASCADE,
        related_name='racks'
    )

   
  def __str__(self):
    return f"{self.Code}"