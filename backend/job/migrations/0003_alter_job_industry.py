# Generated by Django 4.0.5 on 2022-06-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_candidatesapplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.CharField(choices=[('Business', 'Business'), ('Information Technology', 'It'), ('Banking', 'Banking'), ('Education/Training', 'Education'), ('Telecommunication', 'Telecommunication'), ('Healthcare', 'Heathcare'), ('Others', 'Others')], default='Business', max_length=30),
        ),
    ]