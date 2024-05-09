"""
Sample module
"""
# urls.py
from django.urls import path
from .views import SendEmailAPIView

urlpatterns = [
    path('', SendEmailAPIView.as_view(), name='send_email'),
]