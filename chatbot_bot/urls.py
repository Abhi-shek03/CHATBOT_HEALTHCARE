from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/', views.page, name='page'),
    path('chatbot_bot/<str:input>', views.input, name='input'),
]