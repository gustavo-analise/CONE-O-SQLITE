# Conexão SQLITE com Python 
Este projeto demonstra a conexão e interação com um banco de dados SQLite utilizando a linguagem Python. O objetivo principal é criar e manipular tabelas, estabelecer relações entre elas e realizar consultas para extrair informações relevantes.

# Requisitos
Para executar este projeto, você precisará instalar as seguintes dependências:

sqlite3: Esta biblioteca já vem instalada com o Python, então não é necessário instalá-la separadamente.

# Etapas
- Criação da tabela clientes:

Utilizando o terminal e o comando sqlite, foi criada a tabela clientes com as colunas necessárias para armazenar informações sobre os clientes.
Foi realizada uma consulta SELECT * FROM clientes para confirmar a criação da tabela e sua estrutura.
- Conexão com o banco de dados:

O ambiente virtual do Python (venv) foi ativado para isolar as dependências do projeto.
A biblioteca sqlite3 do Python foi utilizada para estabelecer a conexão com o banco de dados SQLite.
- Criação da tabela vendas:

Foi criada a tabela vendas com as colunas relevantes para registrar as vendas.
A coluna cliente_id foi adicionada à tabela vendas para estabelecer uma relação com a tabela clientes, permitindo identificar qual cliente realizou cada venda.
- Interação entre as tabelas:

Através do código Python no arquivo LOJA_CONNECT.py, foram realizadas operações de inserção de dados nas tabelas clientes e vendas, demonstrando a interação entre elas.
Foi utilizado o comando python .\LOJA_CONNECT.py no terminal para executar o script Python e realizar as operações no banco de dados.
- Confirmação da interação:

Para confirmar a interação entre as tabelas, foi realizada uma consulta INNER JOIN para combinar informações das tabelas clientes e vendas em um único resultado, demonstrando a relação entre elas.
# Observações
Este projeto demonstra um exemplo básico de conexão e interação com um banco de dados SQLite utilizando Python.
As tabelas e colunas utilizadas podem ser adaptadas de acordo com as necessidades específicas do projeto.
As operações de inserção e consulta podem ser expandidas para incluir outras funcionalidades, como atualização e exclusão de dados.
