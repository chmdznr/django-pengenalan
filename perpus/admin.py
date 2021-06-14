from django.contrib import admin

# Register your models here.
from perpus.models import Kelompok, Buku


class KelompokAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'keterangan', 'created_at', 'update_at')


class BukuAdmin(admin.ModelAdmin):
    list_display = ('id', 'kelompok', 'judul', 'ringkasan', 'dokumen', 'created_at', 'update_at',)
    list_filter = ('kelompok', )


admin.site.register(Kelompok, KelompokAdmin)
admin.site.register(Buku, BukuAdmin)
