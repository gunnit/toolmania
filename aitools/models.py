from django.db import models
from django.utils.text import slugify

class Tool(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)
    subcategory = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    short_name = models.CharField(max_length=200, null=True, blank=True)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image_url = models.URLField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    developer = models.CharField(max_length=100, blank=True)
    rating = models.CharField(max_length=100, blank=True)
    license_type = models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='tool_logos/', blank=True, null=True)
    # SEO fields
    seo_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=155, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
