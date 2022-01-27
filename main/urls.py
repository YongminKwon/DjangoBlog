from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.posting, name="posting"),
    path('new_post/', views.new_post),
    path('<int:pk>/remove/', views.remove_post),
    path('<int:pk>/edit/',views.edit_post),
]
