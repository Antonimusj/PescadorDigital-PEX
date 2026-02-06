🐟 Sistema de Gestão - Colônia de Pesca (Projeto PEX)

Este projeto foi desenvolvido como parte do Projeto de Extensão (PEX) do meu curso, com o objetivo de modernizar os processos de uma Colônia de Pescadores real.



📝 O Desafio (A Dor do Cliente)

Antes deste sistema, a colônia realizava todo o controle de seus associados de forma manual, utilizando cadernos e folhas de papel. Isso gerava:



Extrema dificuldade para encontrar registros.



Falta de segurança dos dados.



Impossibilidade de gerar relatórios ou buscas rápidas por CPF.



💡 A Solução

Desenvolvi um sistema web robusto que digitaliza todo esse processo, permitindo o cadastro, edição, busca e exclusão de pescadores de forma instantânea e segura.



🛠️ Tecnologias e Metodologia

Este projeto foi construído utilizando uma abordagem híbrida de aprendizado e aceleração:



Back-end: Django 5.x (Python) com lógica de validação de CPF (Módulo 11).



Banco de Dados: Sistema Inteligente de Fallback. O sistema tenta conectar ao MySQL; caso não detecte o servidor, muda automaticamente para SQLite (Portátil).



Front-end: Desenvolvido com Bootstrap 5 e Crispy Forms.



Inteligência Artificial \& Estudos: Grande parte da interface visual e refinamentos de código foram acelerados com o uso de IA, enquanto a arquitetura e fluxo de dados foram baseados em estudos dirigidos através de tutoriais especializados (YouTube).



🚀 Diferenciais Técnicos

Triagem Inteligente: A tela inicial valida o CPF. Se o pescador já existe, ele é exibido; se não, o sistema abre o cadastro com o CPF já preenchido.



UX Moderna: Notificações de sucesso que desaparecem sozinhas e máscaras de entrada (jQuery Mask) para evitar erros de digitação.



Lançador Silencioso: Inclusão de scripts .vbs e .bat que permitem iniciar o sistema em modo "aplicativo", escondendo o terminal do Django e abrindo o navegador automaticamente.



⚙️ Como Rodar o Projeto

Prepare o ambiente:



Bash

python -m venv .venv

source .venv/bin/activate  # No Windows: .venv\\Scripts\\activate

pip install -r requirements.txt

Configure o Banco:



Se usar MySQL, rode o script create\_db.py.



Rode as migrações: python manage.py migrate.



Inicie o Sistema:



Basta clicar no arquivo abrir\_sistema.vbs para rodar em modo silencioso.



📄 Licença

Projeto desenvolvido para fins educacionais e de extensão acadêmica.




👤 Autor



José Antônio da Silva Estudante de Ciência de Dados (3º Semestre) na Faculdade Descomplica.











---







---



\### 🤝 Conecte-se comigo

Para discussões sobre Engenharia de Dados, parcerias em projetos de Sports Analytics ou oportunidades profissionais:



\[!\[LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/jose-antonio-da-silva-ds)

\[!\[Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge\&logo=Kaggle\&logoColor=white)](https://www.kaggle.com/antonimusarch)



---







