# Generated by Django 4.1.3 on 2022-11-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesList', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='procuts',
            new_name='products',
        ),
        migrations.AddField(
            model_name='recipe',
            name='desc',
            field=models.TextField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
