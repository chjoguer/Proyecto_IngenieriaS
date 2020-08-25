# Generated by Django 3.0.1 on 2020-08-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0005_auto_20200822_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_tema',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio/', verbose_name='Audio del tema'),
        ),
        migrations.AlterField(
            model_name='imagenes_tema',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='Imagen del tema'),
        ),
        migrations.AlterField(
            model_name='videos_tema',
            name='video',
            field=models.FileField(blank=True, upload_to='video/', verbose_name='Video del tema'),
        ),
    ]