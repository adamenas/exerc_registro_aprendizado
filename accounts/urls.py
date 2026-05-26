# padrões de url para contas
from django.urls import path, include
from .import views

app_name = 'accounts'
urlpatterns = [
    # inclui urls de autenticação default
    path('', include('django.contrib.auth.urls')),
    # página de cadastro
    path('register/', views.register, name='register'),
]