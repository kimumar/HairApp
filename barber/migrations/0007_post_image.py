# Generated by Django 3.2.4 on 2021-06-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0006_auto_20210622_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
