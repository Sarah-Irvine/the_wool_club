# Generated by Django 4.1.7 on 2023-03-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0009_alter_stitch_image_demonstration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stitch',
            name='image_demonstration',
            field=models.ImageField(default='knitting_steps.jpg', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='stitch',
            name='image_example',
            field=models.ImageField(default='default_stitch_example.jpg', upload_to='uploads/'),
        ),
    ]
