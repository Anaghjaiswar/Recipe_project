# Generated by Django 5.1.2 on 2024-10-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='recipes/'),
        ),
    ]