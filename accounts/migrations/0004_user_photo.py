# Generated by Django 4.1.4 on 2024-03-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='profile_photo/default.png', upload_to='profile_photo'),
        ),
    ]
