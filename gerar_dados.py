import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from acervo.models import Livro, Usuario

def gerar_cpf():
    """Gera um número de CPF fictício formatado."""
    return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"

def gerar_dados():
    
    nomes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Ítalo', 'Juliana']
    sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Alves', 'Pereira', 'Lima', 'Gomes']
    ruas = ['Rua das Flores', 'Av. Central', 'Rua Sete de Setembro', 'Rua XV de Novembro', 'Av. Brasil']
    bairros = ['Centro', 'Bairro Operário', 'Jardim América', 'Vila Nova', 'Planalto']
    
    print("Gerando 250 usuários...")
    cpfs_gerados = set() 

    for i in range(250):
        nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)} {random.choice(sobrenomes)}"
        email = f"user{i}_{random.randint(1000, 9999)}@email.com"
        telefone = f"(51) 9{random.randint(8000, 9999)}-{random.randint(1000, 9999)}"
        endereco = f"{random.choice(ruas)}, {random.randint(1, 1000)} - {random.choice(bairros)}"
        
        cpf = gerar_cpf()
        while cpf in cpfs_gerados:
            cpf = gerar_cpf()
        cpfs_gerados.add(cpf)
        
        Usuario.objects.create(
            nome=nome_completo, 
            email=email, 
            telefone=telefone,
            endereco=endereco,
            cpf=cpf # Campo adicionado para satisfazer a restrição UNIQUE
        )

    # --- Gerar 950 Livros ---
    titulos_base = [
        ('Dom Casmurro', 'Machado de Assis'), ('1984', 'George Orwell'), 
        ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry'), ('A Hora da Estrela', 'Clarice Lispector'),
        ('O Alquimista', 'Paulo Coelho'), ('Ensaio sobre a Cegueira', 'José Saramago'),
        ('Cem Anos de Solidão', 'Gabriel García Márquez'), ('Grande Sertão: Veredas', 'Guimarães Rosa')
    ]
    generos = ['Ficção', 'Romance', 'Terror', 'Biografia', 'História', 'Ciência']

    print("Gerando 950 livros...")
    for i in range(0):
        base = random.choice(titulos_base)
        titulo = f"{base[0]} - Edição {i+1}"
        autor = base[1]
        genero = random.choice(generos)
        
        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            genero=genero,
        
        )

    print("Carga de dados finalizada com sucesso!")

if __name__ == '__main__':
    gerar_dados()