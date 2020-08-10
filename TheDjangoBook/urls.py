from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('apps/', include('myapp.urls')),
    path('newYear', include('newYear.urls')),
    path('', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('ai/', include('airlines.urls')),
]