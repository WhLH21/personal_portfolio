# Generated by Django 4.1.2 on 2022-10-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_date_alter_blog_description_alter_blog_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(blank=True, upload_to="blog/images/"),
        ),
    ]
