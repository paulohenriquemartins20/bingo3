# Generated by Django 3.2.19 on 2023-10-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_datanumero'),
    ]

    operations = [
        migrations.CreateModel(
            name='datanumero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d', models.TextField(max_length=10)),
                ('n', models.IntegerField()),
                ('video', models.TextField(max_length=100)),
            ],
        ),
    ]
