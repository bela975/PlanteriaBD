import streamlit as st
from PIL import Image
import pandas as pd
import mysql.connector

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
    query = f"DELETE FROM {table} WHERE {condition_column}= %s"
    cursor.execute(query, (condition_value,))
    conn.commit()
    st.success(f'Dados deletados de {table} com sucesso.')

#update
def update_data(table, condition_column, condition_value, key_column, key):
    query = f"UPDATE {table} SET {condition_column} = %s WHERE {key_column}= %s"
    cursor.execute(query, (condition_value,key))
    conn.commit()
    st.success(f'Dados atualizados em {table} com sucesso.')


# def select_data(table):
#         query = f"SELECT * FROM {table}" 
#         print("Generated query:", query)          
#         cursor.execute(query)
#         data = cursor.fetchall()
#         return data
        
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
    

st.title("Planteria")
menu = st.subheader("a melhor loja de plantas do planeta")
pages = st.sidebar.selectbox("Selecione a Página", ("Menu Principal","Operações"))

if pages =="Menu Principal":
    st.write("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
elif pages == "Operações":
    operation = st.sidebar.selectbox("Selecione a operação", ("Inserir", "Deletar", "Atualizar", "Select"))
    table = st.sidebar.selectbox("Selecione a tabela para alterar", ("pessoa", "funcionario", "cliente", "servico", "produto", "pedido","pagamento_pedido"))

#efetuando as operações

    if operation == "Inserir":
        if table == "pessoa":
            CPF_pessoa = str(st.text_input("CPF"))
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
            CPF_funcionario = st.text_input("CPF_f")
            cargo_funcionario = st.text_input("cargo")
            salario_funcionario = st.number_input("Salario",min_value=1420)
            data_contratação_funcionario = st.date_input("data contratação")
            frequencia_funcionario = st.number_input("frequencia")
            
            if st.button("Inserir"):
                insert_data(table, (CPF_funcionario,cargo_funcionario, salario_funcionario,data_contratação_funcionario,frequencia_funcionario))
        

        elif table == "cliente":
            CPF_cliente = st.number_input("CPF_c",min_value=11111111111)

            if st.button("Inserir"):
                insert_data(table, (CPF_cliente))


        elif table == "servico":
            id_servico = st.number_input("id serviço",max_value=9999)
            data_recebimento_servico = st.date_input("data de recebimento")
            data_entrega_servico = st.date_input("data de entrega")
            custo_servico = st.number_input("custo")
            descricao_servico = st.text_input("descricao",max_chars=200)


            if st.button("Inserir"):
                insert_data(table, (id_servico,data_recebimento_servico,data_entrega_servico,custo_servico,descricao_servico))

        elif table == "produto":
            id_produto = st.number_input("id produto", max_value=9999)
            categoria_produto = st.text_input("categoria",max_chars=50)
            preco_produto = st.number_input("preço")
            qnt_exemplares_produto = st.number_input("quantidade")

            if st.button("Inserir"):
                insert_data(table, (id_produto,categoria_produto,preco_produto,qnt_exemplares_produto))
                
                
        elif table =="pedido":
            CPF_comprador_pedido = st.number_input("CPF do comprador",min_value=11111111111)
            id_pedido = st.number_input("id pedido",max_value=9999)
            id_produto_pedido = st.number_input("id produto pedido",max_value=9999)

            if st.button("Inserir"):
                insert_data(table, (CPF_comprador_pedido,id_pedido,id_produto_pedido))

        elif table == "pagamento_pedido":
            id_pagamento = st.number_input("id pagamento",max_value=999999)
            preco_total_pagamento = st.number_input("preço total",min_value=0)
            quantidade_pagamento = st.number_input("quantidade")
            data_compra_pagamento = st.date_input("data do pagamento")
            

            if st.button("Inserir"):
                insert_data(table, (id_pagamento,preco_total_pagamento,quantidade_pagamento, data_compra_pagamento))
        


#nao funcional ainda
    elif operation == "Deletar":
        if table == "pessoa":
            CPF_pessoa = st.text_input("CPF da pessoa a ser deletada")
            if st.button("Deletar"):
                delete_data(table, "CPF", CPF_pessoa)

    elif operation == "Atualizar":
        if table == "pessoa":
            CPF_pessoa = st.text_input("CPF") 
            novo_email = st.text_input("Novo Email da Pessoa")
            if st.button("Atualizar"):
                update_data(table, "email", novo_email, "CPF", CPF_pessoa)
                
    elif operation == 'Select':
        if table == "pessoa":
            data = select_data(table, "CPF")
            dataSelected = st.text_input("CPF")
            st.write("Dados da tabela pessoa:")
            df = pd.DataFrame(data, columns=['CPF', 'nome', 'email', 'cep','bairro','rua','numero','complemento'])
            st.dataframe(df.set_index('CPF'), width=800)
