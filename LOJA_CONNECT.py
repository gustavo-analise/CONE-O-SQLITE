#python -m venv venv
# #.\venv\Scripts\activate
import sqlite3
connector = sqlite3.connect('loja.db')

cursor = connector.cursor()

cursor.execute(""" create table vendas (Id Integer Primary Key not null,
                valor_venda NUM not null, 
               cliente_id Integet Not null,
               foreign key (cliente_id) references clientes (id))""")

cursor.execute("insert into vendas values(1, 16.90, 1 )")
cursor.execute("insert into vendas values(2, 86.00,2 )")
cursor.execute("insert into vendas values(3, 7.02,3 )")
cursor.execute("insert into vendas values(4, 50.50,4 )")
cursor.execute("insert into vendas values(5, 77.99,5)")
connector.commit()
cursor.execute("""select * FROM vendas v
                  join clientes c on v.cliente_id=c.id """)
vendas =  cursor.fetchall()
print(vendas)
connector.close()
#python .\LOJA_CONNECT.py



