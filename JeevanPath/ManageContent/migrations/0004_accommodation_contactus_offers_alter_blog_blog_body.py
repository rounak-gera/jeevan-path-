# Generated by Django 5.2 on 2025-05-06 08:31

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ManageContent", "0003_alter_blog_blog_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="Accommodation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=400)),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                (
                    "slide_image_1",
                    models.ImageField(
                        upload_to="accommodation/", verbose_name="Image 1"
                    ),
                ),
                (
                    "slide_image_2",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="accommodation/",
                        verbose_name="Image 2",
                    ),
                ),
                (
                    "slide_image_3",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="accommodation/",
                        verbose_name="Image 3",
                    ),
                ),
                (
                    "slide_image_4",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="accommodation/",
                        verbose_name="Image 4",
                    ),
                ),
                ("button_name", models.CharField(max_length=100)),
                ("redirect_to", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=400)),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "alternative_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "alternative_phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("address", models.CharField(max_length=400)),
                ("facebook_link", models.URLField(blank=True, null=True)),
                ("instagram_link", models.URLField(blank=True, null=True)),
                ("twitter_link", models.URLField(blank=True, null=True)),
                ("linkedin_link", models.URLField(blank=True, null=True)),
                ("youtube_link", models.URLField(blank=True, null=True)),
                ("whatsapp_link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Offers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=400)),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
                ),
                ("image", models.ImageField(upload_to="offers/")),
                ("location", models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name="blog",
            name="blog_body",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Blog Body"),
        ),
    ]
