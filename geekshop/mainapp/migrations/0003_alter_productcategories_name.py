# Generated by Django 3.2.6 on 2022-06-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_productcateries_productcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategories',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
