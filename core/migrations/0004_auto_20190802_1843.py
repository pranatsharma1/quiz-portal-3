# Generated by Django 2.2.2 on 2019-08-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190802_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='university_roll_no',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='negative_marks',
            field=models.IntegerField(default=1),
        ),
    ]
