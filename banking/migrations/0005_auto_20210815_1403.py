# Generated by Django 3.0.7 on 2021-08-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_after'),
    ]

    operations = [
        migrations.AlterField(
            model_name='after',
            name='receiver',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='after',
            name='sender',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='balance',
            name='email',
            field=models.EmailField(max_length=300, unique=True),
        ),
    ]
