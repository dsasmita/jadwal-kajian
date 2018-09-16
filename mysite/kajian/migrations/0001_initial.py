# Generated by Django 2.1.1 on 2018-09-16 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mosque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=256, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kajian.City')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ustad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('profile_excerpt', models.CharField(blank=True, max_length=256, null=True)),
                ('profile', models.TextField(blank=True, null=True)),
                ('link_youtube', models.CharField(blank=True, max_length=256, null=True)),
                ('link_fb', models.CharField(blank=True, max_length=256, null=True)),
                ('link_instagram', models.CharField(blank=True, max_length=256, null=True)),
                ('link_twitter', models.CharField(blank=True, max_length=256, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='ustad')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kajian.Province'),
        ),
    ]
