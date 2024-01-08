# Generated by Django 5.0.1 on 2024-01-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('subcategory', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField(blank=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('developer', models.CharField(blank=True, max_length=100)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
        ),
    ]
