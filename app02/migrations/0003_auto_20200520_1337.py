# Generated by Django 2.1.4 on 2020-05-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_auto_20200520_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='网页配图'),
        ),
    ]
