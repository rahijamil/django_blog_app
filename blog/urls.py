from django.urls import path
from . import views

urlpatterns = [
  path('<slug:category_slug>/', views.category_detail, name='category_detail'),
  path('<slug:category_slug>/<slug:post_slug>', views.post_detail, name='post_detail')
]