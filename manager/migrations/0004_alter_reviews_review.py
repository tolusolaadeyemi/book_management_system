# Generated by Django 3.2.9 on 2022-03-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_rename_book_reviews_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.CharField(default='', max_length=100),
        ),
    ]
