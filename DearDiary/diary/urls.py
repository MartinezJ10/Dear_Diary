from django.urls import path

from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('add_page/', views.add_page, name='add_page'),
    path('update_page/<int:pk>/', views.update_page, name='update_page'),
    path('delete_page/<int:pk>/', views.delete_page, name='delete_page'),

    path('page/<int:pk>/', views.page, name='page'),
]
