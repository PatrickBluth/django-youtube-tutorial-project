# Generated by Django 2.0.3 on 2018-12-21 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_page_lenth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='page_lenth',
        ),
    ]
