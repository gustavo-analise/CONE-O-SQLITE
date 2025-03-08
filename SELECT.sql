-- Seleciona todos os registros da tabela CLIENTES
SELECT * FROM CLIENTES;

-- Seleciona todos os registros da tabela VENDAS
SELECT * FROM VENDAS;

-- Realiza um INNER JOIN entre as tabelas CLIENTES e VENDAS para trazer informações combinadas
SELECT 
    C.ID,         -- ID do cliente
    C.NOME,       -- Nome do cliente
    C.CPF,        -- CPF do cliente
    V.VALOR_VENDA,-- Valor da venda realizada
    V.cliente_id  -- ID do cliente na tabela VENDAS (chave estrangeira)
FROM CLIENTES C
INNER JOIN VENDAS V 
ON C.Id = V.cliente_id; -- A condição de junção relacionando os clientes às suas respectivas vendas
