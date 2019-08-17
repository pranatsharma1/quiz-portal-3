# Generated by Django 2.2.2 on 2019-08-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_categorymarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymarks',
            name='correct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='categorymarks',
            name='incorrect',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='categorymarks',
            name='unanswered',
            field=models.IntegerField(default=0),
        ),
    ]
