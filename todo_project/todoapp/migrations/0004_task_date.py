# Generated by Django 4.1.3 on 2022-12-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_remove_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1992-03-4'),
            preserve_default=False,
        ),
    ]
