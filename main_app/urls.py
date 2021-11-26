from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('about/', views.about, name='about'),
  path('memories/', views.memories_index, name='memories_index'),
  path('memories/<int:memory_id>/', views.memories_detail, name='memories_detail'),
  path('memories/create', views.MemoryCreate.as_view(), name='memories_create'),
  path('memories/<int:pk>/update/', views.MemoryUpdate.as_view(), name='memories_update')
]