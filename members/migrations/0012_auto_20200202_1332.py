# Generated by Django 2.2.5 on 2020-02-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20191224_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile-images/'),
        ),
    ]
