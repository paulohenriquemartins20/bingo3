# Generated by Django 3.2.19 on 2023-10-18 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_permisoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='permisoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomeunico', models.TextField(max_length=20)),
                ('numeros', models.IntegerField()),
                ('pisx', models.TextField(max_length=13)),
            ],
        ),
    ]