from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('index/', views.index_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('create_entry/', views.create_entry, name='create_entry'),
    path('entry/<int:entry_id>/', views.view_entry, name='view_entry'),
    path('entry/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
    path('entry/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),
    path('send-support-message/', views.send_support_message, name='send_support_message'),
]
