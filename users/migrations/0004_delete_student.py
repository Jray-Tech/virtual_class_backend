# Generated by Django 3.1.5 on 2021-01-31 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_is_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
