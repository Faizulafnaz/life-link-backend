# Generated by Django 4.2.5 on 2023-11-03 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_messagerequest_id_accepted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagerequest',
            old_name='id_accepted',
            new_name='is_accepted',
        ),
    ]
