from django.urls import path
from practice import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('', views.dashboard, name='dashboard')

]
