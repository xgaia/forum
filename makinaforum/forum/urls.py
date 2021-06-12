from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thread/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.AddView.as_view(), name='add'),
]
