# Generated by Django 4.2.1 on 2024-02-27 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
