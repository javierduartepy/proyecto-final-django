# Generated by Django 3.2.6 on 2021-08-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='nombre',
            field=models.TextField(),
        ),
    ]
