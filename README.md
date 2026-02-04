🐟 Sistema de Gestão - Colônia de Pesca (Projeto PEX)
Este projeto foi desenvolvido como parte do Projeto de Extensão (PEX) do meu curso de Ciência de Dados, com o objetivo de modernizar os processos de uma Colônia de Pescadores real que operava exclusivamente com registros em papel.

📝 O Desafio (A Dor do Cliente)
Antes deste sistema, a colônia realizava todo o controle de seus associados de forma manual, utilizando cadernos. Isso gerava:

Extrema dificuldade e lentidão para encontrar registros.

Vulnerabilidade e falta de backup dos dados.

Impossibilidade de gerar relatórios ou realizar buscas rápidas por CPF.

💡 A Solução
Desenvolvi um sistema web robusto que digitaliza todo esse processo, permitindo o gerenciamento completo (CRUD) de pescadores de forma instantânea, segura e com validações automatizadas.

🛠️ Tecnologias e Metodologia
Este projeto utiliza uma abordagem moderna de desenvolvimento e engenharia de dados:

Back-end: Django 5.x (Python) com lógica de validação de CPF (Algoritmo Módulo 11).

Front-end: Interface responsiva com Bootstrap 5, Crispy Forms e máscaras dinâmicas com jQuery Mask.

Inteligência Artificial & Estudos: A interface visual e refinamentos de código foram acelerados com o uso de IA, enquanto a arquitetura e o fluxo de dados foram consolidados através de estudos dirigidos e documentações técnicas.

🚀 Diferenciais Técnicos e Resiliência
O sistema foi projetado com foco em Alta Disponibilidade e Confiabilidade de Dados:

Arquitetura de Banco Híbrido (Fallback): O sistema tenta conectar ao MySQL como banco principal. Caso o servidor não seja detectado, ele alterna automaticamente para SQLite, garantindo que o atendimento ao pescador nunca seja interrompido.

Sincronização Automática (Data Sync): Implementei um script de reconciliação (sync_db.py) que é executado na inicialização. Se houver dados salvos no SQLite (modo offline), o sistema os move automaticamente para o MySQL assim que a conexão é restabelecida, tratando duplicatas via lógica de INSERT IGNORE.

Triagem Inteligente: A tela inicial valida o CPF em tempo real. Se o pescador já existe, ele é exibido; se não, o sistema abre o cadastro com o CPF já preenchido.

UX & Automação: Notificações auto-dismiss (fecham sozinhas) e um Lançador Silencioso (.vbs/.bat) que oculta o terminal e inicia o sistema como um aplicativo nativo.

⚙️ Como Rodar o Projeto

Prepare o ambiente:

Bash



python -m venv .venv



source .venv/bin/activate  # No Windows: .venv\\Scripts\\activate



pip install -r requirements.txt
Configure o Banco:

Se desejar usar MySQL, certifique-se de que o serviço está rodando e use o script criar_banco.py.

Rode as migrações: python manage.py migrate.

Inicie o Sistema:

Basta clicar no arquivo abrir_sistema.vbs para rodar o servidor em segundo plano e abrir o navegador automaticamente.


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









