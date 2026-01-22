from django.shortcuts import render, get_object_or_404
from .models import Livro, Emprestimo, Usuario 
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator

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
    ).distinct().order_by('titulo')
    
    return render(request, 'acervo/lista_livros.html', {
        'livros': livros, 
        'titulo_personalizado': 'Empréstimos em andamento'
    })

def lista_livros(request):
    query = request.GET.get('busca')
    if query:
        livros_list = Livro.objects.filter(
            Q(titulo__icontains=query) | 
            Q(autor__icontains=query) | 
            Q(genero__icontains=query) | 
            Q(id__iexact=query)
        ).order_by('titulo')
    else:
        livros_list = Livro.objects.all().order_by('titulo')
    
    paginator = Paginator(livros_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'acervo/lista_livros.html', {
        'livros': page_obj, 
        'busca': query
    })

def detalhe_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    historico = Emprestimo.objects.filter(livro=livro).order_by('-data_saida')
    return render(request, 'acervo/detalhe_livro.html', {'livro': livro, 'historico': historico})

def lista_usuarios(request):
    query = request.GET.get('busca')
    if query:
        usuarios_list = Usuario.objects.filter(
            Q(nome__icontains=query) | 
            Q(cpf__icontains=query) | 
            Q(id__iexact=query)
        ).order_by('nome')
    else:
        usuarios_list = Usuario.objects.all().order_by('nome')
    
    paginator = Paginator(usuarios_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'acervo/lista_usuarios.html', {
        'usuarios': page_obj, 
        'busca': query
    })

def detalhe_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    historico = Emprestimo.objects.filter(usuario=usuario).order_by('-data_saida')
    return render(request, 'acervo/detalhe_usuario.html', {'usuario': usuario, 'historico': historico})