# Generated by Django 3.1.1 on 2020-12-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201216_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]