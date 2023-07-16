from django.urls import path, include
from . import views

app_name='todolist'

urlpatterns = [
    path('', views.main, name="main"),
    path('write/', views.write, name="write"),
    path('rewrite/<int:id>', views.rewrite, name="rewrite"),
    path('delete/<int:id>', views.delete, name='delete'),
]
