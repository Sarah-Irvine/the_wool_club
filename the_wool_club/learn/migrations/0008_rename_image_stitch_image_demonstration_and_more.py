# Generated by Django 4.1.7 on 2023-03-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0007_remove_basicarticle_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stitch',
            old_name='image',
            new_name='image_demonstration',
        ),
        migrations.AddField(
            model_name='stitch',
            name='image_example',
            field=models.ImageField(default='default_stitch_example.jpeg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='stitch',
            name='skill_level',
            field=models.TextField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')]),
        ),
    ]