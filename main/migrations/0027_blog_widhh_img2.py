# Generated by Django 4.1.5 on 2023-01-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_blog_widhh_people_model_photo_blog_post_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_widhh',
            name='img2',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]