# Generated by Django 3.2.5 on 2021-07-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='collageID',
            field=models.IntegerField(default=0, max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationalID',
            field=models.IntegerField(default=0, max_length=15),
        ),
    ]
