# Generated by Django 4.1.7 on 2023-03-20 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_stitch_how_to_alter_stitch_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicarticle',
            name='image',
        ),
    ]