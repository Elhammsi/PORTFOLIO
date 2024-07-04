from django.urls import path
from . import views


urlpatterns = [
    path('', views.starting_page, name='start_page'),
    path('portfolio_details/<int:id>/', views.portfolio_details, name='portfolio_details'),
]
 
