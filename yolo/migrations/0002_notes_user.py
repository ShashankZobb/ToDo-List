# Generated by Django 4.1 on 2022-08-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.CharField(default='shashank', max_length=100),
        ),
    ]
