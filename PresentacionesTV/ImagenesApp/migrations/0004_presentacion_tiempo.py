# Generated by Django 4.2.4 on 2023-08-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImagenesApp', '0003_alter_archivo_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion',
            name='tiempo',
            field=models.IntegerField(default=20),
        ),
    ]
