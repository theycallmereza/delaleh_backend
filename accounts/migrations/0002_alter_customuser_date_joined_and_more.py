# Generated by Django 4.2 on 2025-01-14 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="The date and time when the user was created.",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(help_text="The user's first name.", max_length=63),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Indicates whether the user is currently active.",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Indicates whether the user has staff (admin) permissions.",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(help_text="The user's last name.", max_length=63),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="mobile_number",
            field=models.CharField(
                help_text="The user's mobile number, used as the unique identifier for authentication.",
                max_length=31,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                help_text="The user's username, which must be unique across the system.",
                max_length=127,
                unique=True,
            ),
        ),
    ]
