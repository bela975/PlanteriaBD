import streamlit as st
from PIL import Image
import pandas as pd
import mysql.connector

#conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Du-cajujo4",
    database="planteria1"
)

cursor = conn.cursor()

#insert
def insert_data(table, data):
    query = f"INSERT INTO {table} VALUES ({', '.join(['%s']*len(data))})"
    cursor.execute(query, data)
    conn.commit()
    st.success(f'Dados inseridos em {table}.')

#delete
def delete_data(table, condition_column, condition_value):
    query = f"DELETE FROM {table} WHERE {condition_column} = %s"
    cursor.execute(query, (condition_value,))
    conn.commit()
    st.success(f'Dados deletados de {table}.')


#update
def update_data(table, set_column, set_value, condition_column, condition_value):
    query = f"UPDATE {table} SET {set_column} = %s WHERE {condition_column} = %s"
    cursor.execute(query, (set_value, condition_value))
    conn.commit()
    st.success(f'Dados atualizados em {table}.')

#select
def select_data(table, data):
    query = f"SELECT * FROM {table}"  
    print("Generated query:", query)         
    cursor.execute(query)
    data = cursor.fetchall()
    return data

#select
def select_data(table, condition=None):
    if condition:
        query = f"SELECT * FROM {table} WHERE {condition}"
    else:
        query = f"SELECT * FROM {table}"

    print("Generated query:", query)
    cursor.execute(query)
    data = cursor.fetchall()
    return data


#interface
st.title("Planteria")
menu = st.subheader("Por Leonardo, Maria Júlia e Isabela")
pages = st.sidebar.selectbox("Selecione a Página", ("Menu Principal","Operações"))

if pages =="Menu Principal":
    st.write("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
elif pages == "Operações":
    operation = st.sidebar.selectbox("Selecione a operação", ("Inserir", "Deletar", "Atualizar", "Select"))
    table = st.sidebar.selectbox("Selecione a tabela para alterar", ("pessoa", "funcionario", "cliente", "tipo_servico", "servico", "produto", "pedido","pagamento_pedido"))

    if operation == "Inserir":
        if table == "pessoa":
            CPF_pessoa = str(st.number_input("CPF", min_value=11111111111))
            nome_pessoa = st.text_input("Nome")
            email_pessoa = st.text_input("Email",max_chars=100)
            CEP_pessoa = st.number_input("CEP",max_value=99999999) 
            bairro_pessoa = st.text_input("Bairro",max_chars=40)
            rua_pessoa = st.text_input("Rua",max_chars=40)
            numero_rua_pessoa = st.number_input("Numero",max_value=999)
            complentento_pessoa = st.text_input("Complemento")

            if st.button("Inserir"):
                insert_data(table, (CPF_pessoa, nome_pessoa,email_pessoa,CEP_pessoa,
    bairro_pessoa,rua_pessoa,numero_rua_pessoa,complentento_pessoa))
        

        elif table == "funcionario":
            CPF_funcionario = st.number_input("CPF_f",min_value=11111111111)
            cargo_funcionario = st.text_input("cargo")

            salario_funcionario = st.number_input("Salario",min_value=1420)
            data_contratação_funcionario = st.date_input("data contratação")
            frequencia_funcionario = st.number_input("frequencia")

            if st.button("Inserir"):
                insert_data(table, (CPF_funcionario,salario_funcionario,data_contratação_funcionario,frequencia_funcionario))
        

        elif table == "cliente":
            CPF_cliente = st.number_input("CPF_c",min_value=11111111111)

            if st.button("Inserir"):
                insert_data(table, (CPF_cliente))

        elif table == "tipo_servico":
            id_tipo_servico = st.number_input("id_serviço", max_value=9999)
            descricao_tipo_servico = st.text_input("descricao", max_chars=200)

            if st.button("Inserir"):
                insert_data(table, (id_tipo_servico, descricao_tipo_servico))


        elif table == "servico":
            id_tipo_servico_s = st.number_input("id tipo serviço", max_value=9999)
            id_servico = st.number_input("id serviço",max_value=9999)
            data_recebimento_servico = st.date_input("data de recebimento")
            data_entrega_servico = st.date_input("data de entrega")
            custo_servico = st.number_input("custo")
            descricao_servico = st.text_input("descricao",max_chars=200)

            if st.button("Inserir"):
                insert_data(table, (id_tipo_servico_s, id_servico, data_recebimento_servico,data_entrega_servico,custo_servico,descricao_servico))


        elif table == "produto":
            id_produto = st.number_input("id produto", max_value=9999)
            categoria_produto = st.text_input("categoria",max_chars=50)
            preco_produto = st.number_input("preço")
            qnt_exemplares_produto = st.number_input("quantidade", format="%d", step = 1)

            if st.button("Inserir"):
                insert_data(table, (id_produto,categoria_produto,preco_produto,qnt_exemplares_produto))
                
                
        elif table =="pedido":
            CPF_comprador_pedido = st.number_input("CPF do comprador",min_value=11111111111)
            id_pedido = st.number_input("id pedido",max_value=9999)
            id_produto_pedido = st.number_input("id produto pedido",max_value=9999)
            data_pedido = st.date_input("data pedido")

            if st.button("Inserir"):
                insert_data(table, (CPF_comprador_pedido,id_pedido,id_produto_pedido,data_pedido))

        elif table == "pagamento_pedido":
            id_pagamento = st.number_input("id_pagamento",max_value=999999)
            preco_total_pagamento = st.number_input("preço total",min_value=0)
            quantidade_pagamento = st.number_input("quantidade", format="%d",step=1)
            data_compra_pagamento = st.date_input("data do pagamento")

            if st.button("Inserir"):
                insert_data(table, (id_pagamento,preco_total_pagamento,quantidade_pagamento,data_compra_pagamento))
        

    elif operation == "Deletar":
        if table == "pessoa":
            CPF_pessoa = str(st.number_input("CPF da pessoa a ser deletada: ", min_value=11111111111))
            if st.button("Deletar"):
                delete_data(table, "CPF", CPF_pessoa)
    
        elif table == "funcionario":
            CPF_funcionario = str(st.number_input("CPF do funcionário a ser deletado: ", min_value=11111111111))
            if st.button("Deletar"):
                delete_data(table, "CPF_f", CPF_funcionario)
        
        elif table == "cliente":
            CPF_cliente = str(st.number_input("CPF do cliente a ser deletado: ", min_value=11111111111))
            if st.button("Deletar"):
                delete_data(table, "CPF_c", CPF_cliente)
        
        elif table == "tipo_servico":
            id_tipo_servico = st.number_input("ID da categoria de serviço a ser deletada: ", max_value=9999)
            if st.button("Deletar"):
                delete_data(table, id_tipo_servico)
        
        elif table == "servico":
            id_servico = st.number_input("ID do serviço a ser deletado", max_value=9999)
            if st.button("Deletar"):
                delete_data(table, id_servico)

        elif table == "produto":
            id_produto = st.number_input("ID do produto a ser excluido: ", max_value=9999)
            if st.button("Deletar"):
                delete_data(table, id_produto)
        
        elif table == "pedido":
            id_pedido = st.number_input("ID do pedido a ser excluido: ", max_value=9999)
            if st.button("Deletar"):
                delete_data(table, id_pedido)
        
        elif table == "pagamento_pedido":
            id_pagamento = st.number_input("ID do pagamento a ser excluido: ", max_value=9999)
            if st.button("Deletar"):
                delete_data(table, id_pagamento)
        

    elif operation == "Atualizar":
        if table == "pessoa":
            CPF_pessoa = str(st.number_input("CPF", min_value=11111111111, format="%d"))
            novo_email = st.text_input("Novo email da pessoa: ")
            if st.button("Atualizar"):
                update_data(table, "email", novo_email, "CPF", CPF_pessoa)

        elif table == "funcionario":
            CPF_funcionario = str(st.number_input("CPF do funcionário", min_value=11111111111))
            novo_salario = st.number_input("Novo salário do funcionário: ")
            if st.button("Atualizar"):
                update_data(table, "salario", novo_salario, "CPF_f", CPF_funcionario)
        
        elif table == "servico":
            id_servico = st.number_input("Id do serviço",max_value=9999)
            novo_custo = st.number_input("Novo custo será: ", max_value=999999)
            if st.button("Atualizar"):
                update_data(table, "novo custo", novo_custo, "id_servico", id_servico)

        elif table == "produto":
            id_produto = st.number_input("Id do produto", max_value=9999)
            nova_qtd = st.number_input("Nova quantidade do produto: ", max_value=9999999)
            if st.button("Atualizar"):
                update_data(table, "nova quantidade", nova_qtd, "id_produto", id_produto)

        elif table == "pagamento_pedido":
            id_pagamento = st.number_input("Id do pagamento: ", max_value=9999)
            novo_total = st.number_input("O novo total da compra é: ", max_value=99999999)
            if st.button("Atualizar"):
                update_data(table, "novo total da compra", novo_total, "id_pagamento", id_pagamento)
                
    elif operation == 'Select':

        if table == "pessoa":
            data = select_data(table)
            st.write("Dados da tabela pessoa:")
            df = pd.DataFrame(data, columns=["CPF", "nome", "email", "CEP", "bairro", "rua", "numero", "complemento"])
            st.dataframe(df.set_index('CPF'), width=800)
    
        elif table == 'funcionario':
            data = select_data(table)
            st.write("Dados da tabela Funcionário:")
            df = pd.DataFrame(data, columns=["CPF_f", "salario_funcionario", "data_contratacao", "frequencia"])
            st.dataframe(df.set_index('CPF_f'), width=800)

            

cursor.close()
conn.close()

