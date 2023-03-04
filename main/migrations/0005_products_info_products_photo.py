# Generated by Django 4.1.5 on 2023-01-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_best'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='products_photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]