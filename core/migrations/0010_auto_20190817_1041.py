# Generated by Django 2.0.6 on 2019-08-17 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190817_0808'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categorymarks',
            unique_together=set(),
        ),
    ]