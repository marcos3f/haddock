from django.urls import path

from . import views

app_name = 'haddock'
urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.telaregistro, name='telaregistro'),
    path('what/', views.what, name='what'),
    path('equipe/', views.equipe, name='equipe'),
    path('how/', views.how, name='how'),
    path('requisicao/', views.requisicao, name='requisicao'),
    path('login/',views.login_view, name='login_view'),
]
