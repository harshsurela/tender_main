from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    # url(r'^google/',views.google_login,name="goo")
]
