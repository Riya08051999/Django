# Generated by Django 3.0.6 on 2021-01-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizer',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
