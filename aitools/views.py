from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import Tool
from django.http import JsonResponse

# Home page view
def home(request):
    tools_list = Tool.objects.all()
    paginator = Paginator(tools_list, 10)  # Show 10 tools per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'aitools/home.html', {'page_obj': page_obj})

def tool_detail(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, 'aitools/tool_detail.html', {'tool': tool})

@csrf_exempt
def search(request):
    query = request.GET.get('q', '')
    if query:
        tools = Tool.objects.filter(name__icontains=query)[:10]  # Limit results for performance
        results = [
            {
                'name': tool.name,
                'short_description': tool.short_description,
                'url': tool.url,
                'image_url': tool.image_url,
                'rating': tool.rating,  # Ensure your Tool model has a rating field
                'category': tool.category,  # Ensure your Tool model has a category field
                'id': tool.id  # Needed for the URL in the card
                # Add any other fields required for your card here
            } 
            for tool in tools
        ]
    else:
        results = []
    return JsonResponse(results, safe=False)  # Return the results as JSON

def search_tools(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX request here
        query = request.GET.get('q', '')
        category = request.GET.get('category', '')
        subcategory = request.GET.get('subcategory', '')
        license_type = request.GET.get('license_type', '')
        
        tools = Tool.objects.all()
        
        if query:
            tools = tools.filter(name__icontains=query)
        if category:
            tools = tools.filter(category=category)
        if subcategory:
            tools = tools.filter(subcategory=subcategory)
        if license_type:
            tools = tools.filter(license_type=license_type)  # Added line
        
        results = list(tools.values('name', 'short_description', 'url', 'image_url', 'category', 'subcategory', 'license_type')[:10])
        return JsonResponse(results, safe=False)
    else:
        # Initial page load
        categories = Tool.objects.values_list('category', flat=True).distinct()
        subcategories = Tool.objects.values_list('subcategory', flat=True).distinct()
        return render(request, 'aitools/search_tools.html', {
            'categories': categories,
            'subcategories': subcategories
        })