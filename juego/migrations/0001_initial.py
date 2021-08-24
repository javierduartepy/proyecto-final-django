# Generated by Django 3.2.6 on 2021-08-22 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'categoria',
                'db_table': 'categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'nivel',
                'db_table': 'niveles',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField()),
                ('imagen', models.URLField(blank=True, null=True, verbose_name='Link de la imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='juego.categoria')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='juego.nivel')),
            ],
            options={
                'verbose_name': 'pregunta',
                'db_table': 'preguntas',
                'ordering': ['pregunta'],
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.TextField()),
                ('correcto', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='juego.pregunta')),
            ],
            options={
                'verbose_name': 'opcion',
                'db_table': 'opciones',
                'ordering': ['opcion'],
            },
        ),
    ]