# Generated by Django 4.2.2 on 2024-02-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
    ]
