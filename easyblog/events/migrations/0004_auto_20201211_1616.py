# Generated by Django 3.1.4 on 2020-12-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_stitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=models.ImageField(default='img', upload_to='event_images/'),
        ),
    ]