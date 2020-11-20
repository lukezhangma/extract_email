from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('get_emails/', include('process_email.urls')),
    path('admin/', admin.site.urls),
]
