# Generated by Django 3.2.16 on 2023-01-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurAlarm',
            fields=[
                ('id_primary', models.IntegerField(primary_key=True, serialize=False)),
                ('tools', models.CharField(max_length=20)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id_primary', models.IntegerField(primary_key=True, serialize=False)),
                ('tools', models.CharField(max_length=20)),
                ('fabs', models.CharField(max_length=20)),
            ],
        ),
    ]
