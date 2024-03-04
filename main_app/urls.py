from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tots/', views.tot_index, name='tot-index'),
  path('tots/<int:tot_id>/', views.tot_detail, name='tot-detail'),
]