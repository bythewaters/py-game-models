# Generated by Django 4.0.2 on 2024-07-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]