# Generated by Django 4.1.7 on 2023-03-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='sheep.jpg', upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill_level',
            field=models.TextField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner'),
        ),
    ]
