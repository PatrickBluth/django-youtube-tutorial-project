# Generated by Django 2.0.3 on 2018-12-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='page_lenth',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]