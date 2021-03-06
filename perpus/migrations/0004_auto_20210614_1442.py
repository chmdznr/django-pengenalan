# Generated by Django 3.2.4 on 2021-06-14 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perpus', '0003_kelompok_update_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kelompok',
            options={'verbose_name_plural': 'Daftar Kelompok Dokumen'},
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=150)),
                ('ringkasan', models.TextField(blank=True)),
                ('dokumen', models.FileField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('kelompok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpus.kelompok')),
            ],
            options={
                'verbose_name_plural': 'Daftar Buku',
            },
        ),
    ]
