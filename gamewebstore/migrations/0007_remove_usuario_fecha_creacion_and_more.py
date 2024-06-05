# Generated by Django 5.0.6 on 2024-06-03 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamewebstore', '0006_remove_usuario_fecha_creación_usuario_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_creacion',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO'), ('O', 'OTRO')], max_length=1),
        ),
    ]