from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.reviews, name = 'reviews'),
    path('signup/', views.signup, name = 'signup'),
    path('thank_you/', views.thank_you, name = 'thank_you')
]