# Generated by Django 4.1.5 on 2023-01-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_app_app_store_app_google_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='company_logo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
