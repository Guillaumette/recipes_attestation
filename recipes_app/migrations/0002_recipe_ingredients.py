# Generated by Django 5.0.4 on 2024-04-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='', help_text='Перечислите ингредиенты и их количество'),
            preserve_default=False,
        ),
    ]
