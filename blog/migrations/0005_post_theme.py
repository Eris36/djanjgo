# Generated by Django 2.2 on 2019-08-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190711_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
