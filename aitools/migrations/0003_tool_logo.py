# Generated by Django 5.0.1 on 2024-01-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aitools', '0002_tool_created_at_tool_license_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='tool_logos/'),
        ),
    ]