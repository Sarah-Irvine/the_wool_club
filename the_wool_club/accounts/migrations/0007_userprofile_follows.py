# Generated by Django 4.1.7 on 2023-03-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='accounts.userprofile'),
        ),
    ]