from django.contrib import admin
from .models import Usuario, Livro, Emprestimo
from django.utils import timezone

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email')
    search_fields = ('nome', 'cpf') 

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'genero', 'exibir_status')
    list_filter = ('genero', 'editora')
    search_fields = ('titulo', 'autor', 'id') 

    def exibir_status(self, obj):
        return obj.status
    exibir_status.short_description = 'Disponibilidade'

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_saida', 'data_previsao_devolucao', 'status_devolucao')
    list_filter = ('data_saida', 'data_previsao_devolucao')
    search_fields = ('livro__titulo', 'usuario__nome')
    autocomplete_fields = ['livro', 'usuario'] 

    def status_devolucao(self, obj):
        if obj.data_devolucao_real:
            return "✅ Devolvido"
        if obj.data_previsao_devolucao < timezone.now().date():
            return "⚠️ ATRASADO"
        return "⏳ Em andamento"