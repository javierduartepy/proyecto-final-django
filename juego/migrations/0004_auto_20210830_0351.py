# Generated by Django 3.2.6 on 2021-08-30 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0003_puntuacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nivel',
            options={'ordering': ['pk'], 'verbose_name': 'nivele'},
        ),
        migrations.AlterModelOptions(
            name='pregunta',
            options={'ordering': ['pk'], 'verbose_name': 'pregunta'},
        ),
    ]
