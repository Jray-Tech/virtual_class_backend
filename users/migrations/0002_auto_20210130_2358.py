# Generated by Django 3.1.5 on 2021-01-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_tutor',
            field=models.BooleanField(),
        ),
    ]
