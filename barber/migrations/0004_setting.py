# Generated by Django 3.2.4 on 2021-06-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0003_commentmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blogs_img1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('blogs_img2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('blogs_img3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img7', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gallery_img8', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=200)),
            ],
        ),
    ]
