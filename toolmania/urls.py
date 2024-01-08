from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This line includes the admin URLs
    path('', include('aitools.urls')),  # Include your app's URLs here
]
