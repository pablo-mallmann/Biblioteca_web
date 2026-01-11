from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros-emprestados/', views.livros_emprestados, name='livros_emprestados'), # Nova rota
    path('livro/<int:livro_id>/', views.detalhe_livro, name='detalhe_livro'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/<int:usuario_id>/', views.detalhe_usuario, name='detalhe_usuario'),
]