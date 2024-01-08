from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('tool/<int:tool_id>/', views.tool_detail, name='tool_detail'),
    path('search/', views.search, name='search'),  # Regular search
    path('search_tools/', views.search_tools, name='search_tools'),  # AJAX search
]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
