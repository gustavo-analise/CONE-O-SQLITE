# Criando e ativando o ambiente virtual (comandos do terminal)
# python -m venv venv
# .\venv\Scripts\activate

import sqlite3  # Importa a biblioteca SQLite3 para trabalhar com banco de dados

# Conecta (ou cria) o banco de dados 'loja.db'
connector = sqlite3.connect('loja.db')

# Cria um cursor para executar comandos SQL
cursor = connector.cursor()

# Criação da tabela 'vendas' com os seguintes campos:
# - Id: identificador único da venda (chave primária)
# - valor_venda: valor da venda (não nulo)
# - cliente_id: referência ao cliente que realizou a compra
cursor.execute(""" 
CREATE TABLE vendas (
    Id INTEGER PRIMARY KEY NOT NULL,
    valor_venda NUM NOT NULL, 
    cliente_id INTEGER NOT NULL,  -- Corrigido "Integet" para "INTEGER"
    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
) 
""")

# Inserindo registros de vendas na tabela 'vendas'
cursor.execute("INSERT INTO vendas VALUES (1, 16.90, 1)")
cursor.execute("INSERT INTO vendas VALUES (2, 86.00, 2)")
cursor.execute("INSERT INTO vendas VALUES (3, 7.02, 3)")
cursor.execute("INSERT INTO vendas VALUES (4, 50.50, 4)")
cursor.execute("INSERT INTO vendas VALUES (5, 77.99, 5)")

# Confirma as alterações no banco de dados
connector.commit()

# Consulta os dados da tabela 'vendas' unindo com 'clientes' pelo cliente_id
cursor.execute(""" 
SELECT * FROM vendas v
JOIN clientes c ON v.cliente_id = c.id
""")

# Obtém os resultados da consulta e os imprime
vendas = cursor.fetchall()
print(vendas)

# Fecha a conexão com o banco de dados
connector.close()

# Comando para executar o script no terminal
# python .\LOJA_CONNECT.py



