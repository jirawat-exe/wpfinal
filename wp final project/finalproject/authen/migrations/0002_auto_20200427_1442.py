# Generated by Django 3.0.5 on 2020-04-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_fname',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cus_lname',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cus_nname',
            field=models.TextField(),
        ),
    ]
