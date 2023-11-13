from django.urls import path
from . import views

app_name = 'auth_manager'
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]
