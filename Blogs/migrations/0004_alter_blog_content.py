# Generated by Django 4.2.2 on 2023-07-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0003_rename_blogs_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(),
        ),
    ]
