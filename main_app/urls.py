from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('tots/', views.tot_index, name='tot-index'),
  path('tots/<int:tot_id>/', views.tot_detail, name='tot-detail'),
  path('tots/create/', views.TotCreate.as_view(), name='tot-create'),
  path('tots/<int:pk>/update/', views.TotUpdate.as_view(), name='tot-update'),
  path('tots/<int:pk>/delete/', views.TotDelete.as_view(), name='tot-delete'),
  path('tots/<int:tot_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('tots/<int:tot_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
  path('accounts/signup/', views.signup, name='signup'),
]