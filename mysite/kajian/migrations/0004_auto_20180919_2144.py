# Generated by Django 2.1.1 on 2018-09-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kajian', '0003_auto_20180919_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='ustad',
            field=models.ManyToManyField(blank=True, null=True, to='kajian.Ustad'),
        ),
    ]
