from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError

def data_padrao_devolucao():
    return timezone.now().date() + timedelta(days=7)

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        
        return f"{self.nome} (ID: {self.id})"

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    editora = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    class Meta:
        ordering = ['titulo'] 

    def __str__(self):
        
        return f"{self.titulo} (ID: {self.id})"

    @property
    def status(self):
        
        ultimo_emprestimo = self.emprestimo_set.filter(data_devolucao_real__isnull=True).last()
        if ultimo_emprestimo:
            return f"Emprestado (Devolução: {ultimo_emprestimo.data_previsao_devolucao})"
        return "Disponível"

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_saida = models.DateField(auto_now_add=True)
    data_previsao_devolucao = models.DateField(default=data_padrao_devolucao)
    data_devolucao_real = models.DateField(null=True, blank=True)

    def clean(self):
        
        if not self.pk: 
            livro_ocupado = Emprestimo.objects.filter(livro=self.livro, data_devolucao_real__isnull=True).exists()
            if livro_ocupado:
                
                raise ValidationError(f"O livro '{self.livro}' já está emprestado no momento.")

    def __str__(self):
        
        return f"{self.livro} -> {self.usuario}"