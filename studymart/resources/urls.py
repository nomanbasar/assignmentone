from django.urls import path
from . import views

urlpatterns = [
    path('fc/', views.free_course),
    path('bg/', views.blog)
]