# Generated by Django 2.1.7 on 2019-04-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
