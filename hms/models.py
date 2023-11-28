from django.db import models

# Create your models here.
class dataHMS(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    nama = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    height = models.CharField(max_length=200, blank=True, null=True)
    weight = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    tgl_masuk = models.DateField(blank=True, null=True)
    diagnosis = models.CharField(max_length=200, blank=True, null=True)
    bed = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'data_hms'