# Generated by Django 4.0.4 on 2022-05-30 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_alter_preinscripcion_aceptado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partido',
            old_name='marcado_visita',
            new_name='marcador_visita',
        ),
    ]