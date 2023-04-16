from django.db import models

class Holliday(models.Model):
  id = models.AutoField(primary_key=True)
  celebration = models.CharField(max_length=200)
  date = models.DateField
