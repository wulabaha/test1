# Generated by Django 2.1.4 on 2020-05-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='entry_images', verbose_name='网页配图'),
        ),
    ]