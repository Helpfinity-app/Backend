# Generated by Django 5.0.6 on 2024-08-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion', '0002_anxitey_depression'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotion',
            name='feeling_rate',
            field=models.IntegerField(default=50),
        ),
    ]
