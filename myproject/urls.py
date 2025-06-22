from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  # ✅ Render templates

def home(request):
    return render(request, "home.html")

def login_page(request):  # ✅ New login UI view
    return render(request, "login.html")

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),  # ✅ Add this
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
