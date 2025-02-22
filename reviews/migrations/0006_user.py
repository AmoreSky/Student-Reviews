# Generated by Django 5.1.2 on 2024-10-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_rename_lecturer_or_course_review_lecturer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('matric_number', models.IntegerField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
