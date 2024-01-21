

from django.urls import path
from . import views
app_name = 'winnie'
urlpatterns = [
    path('', views.home_view, name='home'),  # Example URL pattern for home_view
    path('StartTrial/', views.starttrial, name='StartTrial'),
    path('Products/',views.products,name='Products'),
]