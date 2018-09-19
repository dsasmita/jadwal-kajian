from django.urls import path

from . import views

app_name = 'kajian'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]