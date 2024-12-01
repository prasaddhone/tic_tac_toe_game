from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('game/', views.game_view, name='game'),  # Change game to game_view here
    path('result/<str:result>/', views.result_view, name='result'),
]
