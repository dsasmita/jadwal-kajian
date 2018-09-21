from django.urls import path

from . import views

app_name = 'kajian'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('kajian', views.ListView.as_view(), name='list'),
    path('kajian-<int:pk>', views.DetailView.as_view(), name='detail'),
]