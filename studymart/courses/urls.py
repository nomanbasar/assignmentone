from django.urls import path
from . import views

urlpatterns = [
    path('', views.course),
    path('ds/', views.Data_Science),
    path('bd/', views.Big_Data),
    path('da/', views.Data_Analysis),
    path('dl/', views.Deep_Learning),
    
]