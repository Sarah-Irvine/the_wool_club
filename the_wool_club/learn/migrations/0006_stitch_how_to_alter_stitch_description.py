# Generated by Django 4.1.7 on 2023-03-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_alter_stitch_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='stitch',
            name='how_to',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stitch',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
