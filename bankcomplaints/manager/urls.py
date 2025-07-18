from django.urls import path
from . import views

urlpatterns = [
    path('complaints/', views.manager_complaints_view, name='manager_complaints'),
] 