from django.urls import path
from . import views

urlpatterns = [
    path('reset-locations/', views.ResetLocationsAPIVIew.as_view()),
]