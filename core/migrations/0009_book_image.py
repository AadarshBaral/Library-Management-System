# Generated by Django 4.1.4 on 2022-12-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_issued_date_of_issue_issued_date_of_return_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/Books'),
        ),
    ]
