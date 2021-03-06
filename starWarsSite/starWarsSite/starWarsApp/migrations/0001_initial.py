# Generated by Django 3.0.8 on 2020-07-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Planeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('texto_apertura', models.TextField()),
                ('director', models.CharField(max_length=120)),
                ('productores', models.CharField(max_length=120)),
                ('personaje', models.ManyToManyField(to='starWarsApp.Personaje')),
                ('planeta', models.ManyToManyField(to='starWarsApp.Planeta')),
            ],
            options={
                'ordering': ('titulo',),
            },
        ),
    ]
