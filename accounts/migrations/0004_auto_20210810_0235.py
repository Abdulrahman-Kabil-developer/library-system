# Generated by Django 3.2.5 on 2021-08-10 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210728_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='collageID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationalID',
            field=models.IntegerField(default=0),
        ),
    ]
