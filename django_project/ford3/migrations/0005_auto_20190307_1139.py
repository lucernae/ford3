# Generated by Django 2.1.5 on 2019-03-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0004_auto_20190307_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='telephone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
