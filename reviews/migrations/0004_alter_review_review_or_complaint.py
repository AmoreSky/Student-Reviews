# Generated by Django 5.1.2 on 2024-10-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_review_complaint_review_review_or_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_or_complaint',
            field=models.TextField(max_length=100000),
        ),
    ]
