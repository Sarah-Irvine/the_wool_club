# Generated by Django 4.1.7 on 2023-03-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_alter_stitch_image_demonstration_and_more'),
        ('accounts', '0002_userprofile_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='saved',
            field=models.ManyToManyField(blank=True, related_name='saved', to='learn.stitch'),
        ),
    ]
