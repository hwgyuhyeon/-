from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.bookadd, name='bookadd'),
    path('add/<int:log_id>', views.commentadd, name='commentadd')
]
