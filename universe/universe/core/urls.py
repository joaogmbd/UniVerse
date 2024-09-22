from django.urls import path
from core.views import index, login
from . import views



app_name = 'core'

urlpatterns = [
    path('', index),
    path('login/', views.login, name='login'),
    path('produto', views.produto, name = 'produto'),
    path('index', views.index, name ='index' ),
    path('registrar', views.registrar, name ='registrar' ),
    path('atletica', views.atletica, name ='atletica' ),
    path('carrinho', views.carrinho, name ='carrinho' )
]