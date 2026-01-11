from django.shortcuts import render, get_object_or_404
from .models import Livro, Emprestimo, Usuario 
from django.db.models import Q
from django.utils import timezone

def dashboard(request):
    hoje = timezone.now().date()
    total_livros = Livro.objects.count()
    total_usuarios = Usuario.objects.count() 
    emprestimos_ativos = Emprestimo.objects.filter(data_devolucao_real__isnull=True)
    livros_emprestados = emprestimos_ativos.count()
    atrasados = emprestimos_ativos.filter(data_previsao_devolucao__lt=hoje).order_by('data_previsao_devolucao')
    total_atrasados = atrasados.count()
    
    livros_disponiveis = total_livros - livros_emprestados
    ultimos_emprestimos = Emprestimo.objects.order_by('-data_saida')[:5]

    contexto = {
        'total_livros': total_livros,
        'total_usuarios': total_usuarios,
        'livros_emprestados': livros_emprestados,
        'livros_disponiveis': livros_disponiveis,
        'ultimos_emprestimos': ultimos_emprestimos,
        'atrasados': atrasados,
        'total_atrasados': total_atrasados,
    }
    return render(request, 'acervo/dashboard.html', contexto)

def livros_emprestados(request):
    
    livros = Livro.objects.filter(
        emprestimo__data_devolucao_real__isnull=True
    ).exclude(
        emprestimo__isnull=True
    ).distinct()
    
    return render(request, 'acervo/lista_livros.html', {
        'livros': livros, 
        'titulo_personalizado': 'Emprestimos em andamento'
    })

def lista_livros(request):
    query = request.GET.get('busca')
    if query:
        livros = Livro.objects.filter(
            Q(titulo__icontains=query) | 
            Q(autor__icontains=query) | 
            Q(genero__icontains=query) | 
            Q(id__iexact=query)
        )
    else:
        livros = Livro.objects.all()
    return render(request, 'acervo/lista_livros.html', {'livros': livros})

def detalhe_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    historico = Emprestimo.objects.filter(livro=livro).order_by('-data_saida')
    return render(request, 'acervo/detalhe_livro.html', {'livro': livro, 'historico': historico})

def lista_usuarios(request):
    query = request.GET.get('busca')
    if query:
        usuarios = Usuario.objects.filter(
            Q(nome__icontains=query) | 
            Q(cpf__icontains=query) | 
            Q(id__iexact=query)
        )
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'acervo/lista_usuarios.html', {'usuarios': usuarios})

def detalhe_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    historico = Emprestimo.objects.filter(usuario=usuario).order_by('-data_saida')
    return render(request, 'acervo/detalhe_usuario.html', {'usuario': usuario, 'historico': historico})