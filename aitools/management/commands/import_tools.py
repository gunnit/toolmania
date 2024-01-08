import openpyxl
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from aitools.models import Tool

class Command(BaseCommand):
    help = 'Import tools from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The Excel file path')

    def handle(self, *args, **options):
        # Open the workbook and select the first worksheet
        wb = openpyxl.load_workbook(options['file_path'])
        ws = wb.active

        # Iterate over the rows and create Tool instances
        for row in ws.iter_rows(min_row=2):  # Assuming first row is header
            name = row[0].value
            image_url = row[1].value
            license_type = row[2].value
            short_description = row[3].value
            tags = row[4].value
            url = row[5].value
            rating = row[6].value
            future_link = row[7].value
            category = row[8].value
            subcategory = row[9].value
            urlname = row[10].value
            description = row[11].value

            # Create and save the Tool instance
            tool, created = Tool.objects.get_or_create(
                name=name,
                defaults={
                    'image_url': image_url,
                    'license_type': license_type,
                    'short_description': short_description,
                    'tags': tags,
                    'description': description,
                    'url': url,
                    'rating': rating,
                    'category': category,
                    'subcategory': subcategory,
                    'slug': slugify(urlname),
                    # 'logo': handle_logo_upload(urlname),  # You need to implement this if you want to upload files
                    # Add any other fields that need to be populated
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created tool: {tool.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Tool already exists: {tool.name}'))

        self.stdout.write(self.style.SUCCESS('Import process completed'))
