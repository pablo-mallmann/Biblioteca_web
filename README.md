Sistema de Gestão de Biblioteca Comunitária
Este projeto é uma aplicação de software desenvolvida como parte de uma atividade de extensão universitária para facilitar a gestão de acervos e empréstimos de livros de forma gratuita e eficiente.

Funcionalidades
Painel de Controle (Dashboard): Visão geral de estatísticas (total de livros, disponíveis, emprestados e usuários ativos).

Gestão de Acervo: Cadastro, busca e visualização detalhada de livros.

Controle de Usuários: Cadastro flexível e consulta de leitores.

Sistema de Empréstimos: Registro de saídas com prazos automáticos e alertas de atraso.

Busca Inteligente: Autocomplete em campos de seleção para lidar com grandes volumes de dados.

Tecnologias Utilizadas
Python: Linguagem principal do projeto.

Django: Framework web para o desenvolvimento da aplicação.

SQLite: Banco de dados relacional (utilizado para persistência de dados localmente).

HTML/CSS: Interface personalizada com foco em usabilidade.

Pré-requisitos
Antes de começar, você precisará ter instalado em sua máquina:

Python 3.x

Git

Instalação e Configuração
Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

Clone o repositório:

Bash

git clone https://github.com/pablo-mallmann/Biblioteca_web.git
cd Biblioteca_web
Crie e ative um ambiente virtual:

Bash

# No Windows
python -m venv venv
venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Prepare o Banco de Dados: Como o banco de dados original é ignorado pelo Git, execute as migrações para criar a estrutura necessária:

Bash

python manage.py migrate
Crie um usuário administrador: Para acessar a área de cadastro e administração:

Bash

python manage.py createsuperuser
(Opcional) Carregar dados de teste: Caso o projeto possua um arquivo de fixtures (dados_teste.json), você pode carregar dados iniciais com:

Bash

python manage.py loaddata dados_teste.json
Como Executar
Inicie o servidor de desenvolvimento:

Bash

python manage.py runserver
Acesse a aplicação em: http://127.0.0.1:8000/

Observações para o Desenvolvedor
Mídias: As imagens das capas de livros são armazenadas localmente na pasta midia/ e não são enviadas para o repositório por questões de privacidade e economia de espaço.

IDs: O sistema utiliza identificadores únicos (IDs) visíveis para diferenciar usuários homônimos e edições diferentes do mesmo livro.

