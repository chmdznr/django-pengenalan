from django.db import models


# Create your models here.

class Kelompok(models.Model):
    nama = models.CharField(max_length=150)
    keterangan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Daftar Kelompok Dokumen'

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=150)
    ringkasan = models.TextField(blank=True)
    dokumen = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Daftar Buku'
