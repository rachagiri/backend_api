"""
URL configuration for backend_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    http post http://127.0.0.1:8000/api/token/ username=admin password=RuSh@2022

    http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1ODg2ODQ0LCJpYXQiOjE2OTU4ODY1NDQsImp0aSI6IjczZGU3OWZkMjk2YTQ4NjI4NzQ0YjA3ZjUzNzNmMzhjIiwidXNlcl9pZCI6MX0.Law129oOaNrwAc3IAehXjNSIun-Uyp8TDAKOhUFvUG8"

    http http://127.0.0.1:8000/api/token/refresh/ refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTk3Mjk0NCwiaWF0IjoxNjk1ODg2NTQ0LCJqdGkiOiI3YmU3NzE0MzZiNDA0M2Y0ODYyNTUwMzUzMjlmZTc2ZiIsInVzZXJfaWQiOjF9.ogE3j_rqSauv61vwifFqWZ5ylm0j8K3S652i7B0MTa0
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path ('api-auth/', include('rest_framework.urls')),
]
