# Generated by Django 3.2.6 on 2021-09-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
    ]
