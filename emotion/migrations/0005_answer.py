# Generated by Django 5.0.6 on 2024-09-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion', '0004_alter_emotion_effect_alter_emotion_negative_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('level', models.IntegerField(default=1)),
            ],
        ),
    ]
