# Generated by Django 4.1.7 on 2023-03-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_stitch_basicarticle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stitch',
            name='image',
            field=models.ImageField(default='knitting_steps.jpeg', upload_to=''),
        ),
    ]
