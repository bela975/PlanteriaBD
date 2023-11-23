import streamlit as st
from PIL import Image
import pandas as pd
from db_config import db_config
from db_connection import create_conn


#definindo as operações
#insert
def insert_data(table, data):
    conn = create_conn()

    if conn is not None:
        cursor = conn.cursor()
        query = f"INSERT INTO {table} VALUES ({', '.join(['%s']*len(data))})"
        cursor.execute(query, data)
        conn.commit()
        st.success(f'Dados inseridos em {table}.')

        cursor.close()
        conn.close()

#delete
def delete_data(table, condition_column, condition_value):
    conn = create_conn()
    if conn is not None:
        cursor = conn.cursor()

        query = f"DELETE FROM {table} WHERE {condition_column} = %s"

        cursor.execute(query, (condition_value,))

        conn.commit()

        st.success(f'Dados deletados de {table} com sucesso.')

        cursor.close()
        conn.close()

#update
def update_data(table, set_column, set_value, condition_column, condition_value):
    conn = create_conn()
    if conn is not None:
        cursor = conn.cursor()
        query = f"UPDATE {table} SET {set_column} = %s WHERE {condition_column} = %s"
        cursor.execute(query, (set_value, condition_value))

        conn.commit()

        st.success(f'Dados atualizados em {table} com sucesso.')

        cursor.close()
        conn.close()


#select
def select_data(table):
    conn = create_conn()
    if conn is not None:
        cursor = conn.cursor()
        query = f"SELECT * FROM {table}"           
        cursor.execute(query)
        rows = cursor.fetchall()
        # Print each row
        for row in rows:
            print(row) 

        cursor.close()
        conn.close()

#interface
#vamo deixar esse site mais bonitinho
st.set_page_config(page_title = "Planteria Oficial", page_icon=":tada:", layout= "wide")
st.title("Planteria")
st.subheader("a melhor loja de plantas do planeta")
pages = st.sidebar.selectbox("Selecione a Página", ("Menu Principal","Operações"))
if pages =="Menu Principal":
    st.write("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
elif pages == "Operações":
    operation = st.sidebar.selectbox("Selecione a operação", ("Inserir", "Deletar", "Atualizar", "Select"))
    table = st.sidebar.selectbox("Selecione a tabela para alterar", ("pessoa", "funcionario", "cliente", "servico", "produto", "pedido","pagamento_pedido"))

#efetuando as operações

    if operation == "Inserir":
        if table == "pessoa":
            CPF_pessoa = st.number_input("CPF", min_value=11111111111)
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
            salario_funcionario = st.number_input("Salario",min_value=1420)
            data_contratação_funcionario = st.date_input("data contratação")
            frequencia_funcionario = st.number_input("frequencia")

            if st.button("Inserir"):
                insert_data(table, (CPF_funcionario,salario_funcionario,data_contratação_funcionario,frequencia_funcionario))
        

        elif table == "cliente":
            CPF_cliente = st.number_input("CPF_c",min_value=11111111111)

            if st.button("Inserir"):
                insert_data(table, (CPF_cliente))


        elif table == "servico":
            custo_servico = st.number_input("custo")
            descricao_servico = st.text_input("descricao",max_chars=200)
            data_recebimento_servico = st.date_input("data de recebimento")
            data_entrega_servico = st.date_input("data de entrega")
            id_servico = st.number_input("id serviço",max_value=9999)

            if st.button("Inserir"):
                insert_data(table, (custo_servico,descricao_servico,data_entrega_servico,data_recebimento_servico,id_servico))

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
            data_compra_pagamento = st.date_input("data do pagamento")
            preco_total_pagamento = st.number_input("preço total",min_value=0)
            quantidade_pagamento = st.number_input("quantidade")

            if st.button("Inserir"):
                insert_data(table, (id_pagamento,data_compra_pagamento,preco_total_pagamento,quantidade_pagamento))
        


#nao funcional ainda
    elif operation == "Deletar":
        if table == "pessoa":
            CPF_pessoa = st.number_input("CPF da pessoa a ser deletada", min_value=0)
            if st.button("Deletar"):
                delete_data(table, "CPF_pessoa", CPF_pessoa)

    elif operation == "Atualizar":
        if table == "pessoa":
            CPF_pessoa = st.number_input("pessoa a ser atualizado", min_value=0)
            novo_nome = st.text_input("Novo Nome da Pessoa")
            if st.button("Atualizar"):
                update_data(table, "nome", novo_nome, "CPF_pessoa", CPF_pessoa)
                
    elif operation == 'Select':
        if table == "pessoa":
            data = select_data(table)
            st.write("Dados da tabela pessoa:")
            df = pd.DataFrame(data, columns=["CPF", "nome"])
            st.dataframe(df.set_index('CPF'), width=800)
        if table == 'aluno':
            data = select_data(table)
            st.write("Dados da tabela Aluno:")
            df = pd.DataFrame(data, columns=["Matrícula do aluno", "Nota do vestibular", "Codigo do curso"])
            st.dataframe(df.set_index('Matrícula do aluno'), width=800)
        if table == 'busca - créditos totais':
            matricula_aluno = st.number_input("Matrícula do aluno", min_value=0)
            if st.button("Buscar"):
                result = select_data(matricula_aluno)
                st.write(f"Total de créditos do aluno: {result}")
