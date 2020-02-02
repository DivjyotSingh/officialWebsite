# Generated by Django 2.2.5 on 2020-02-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0012_auto_20200202_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('members', models.ManyToManyField(blank=True, related_name='achivement_members', to='members.Member')),
            ],
        ),
    ]
