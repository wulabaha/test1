# Generated by Django 2.1.4 on 2020-05-20 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0004_entry_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='image',
        ),
    ]
