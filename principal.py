import pessoaOOP as p
import streamlit as st

p1 = p.Pessoa()

st.title("Programação Orientada a Objetos em Streamlit")

coluna1, coluna2 = st.columns(2)

with coluna1:
    allnomes = []
    allidades = []
    st.subheader("Função 1: Pessoa mais velha")
    
    p1.nome = st.text_input("Nome da pessoa 1")
    p1.idade = st.number_input("Idade da Pessoa 1", min_value=0, step=1)
    allnomes.append(p1.nome)
    allidades.append(p1.idade)

    p1.nome = st.text_input("Nome da pessoa 2")
    p1.idade = st.number_input("Idade da Pessoa 2", min_value=0, step=1)
    allnomes.append(p1.nome)
    allidades.append(p1.idade)


    if st.button("Enviar"):
        if p1.idade[0] > p1.idade[1]:
            st.write(f"A pessoa mais velha é {p1.nome[0]}")
        else:
            st.write(f"A pessoa mais velha é {p1.nome[1]}")


with coluna2:

    st.subheader("Função 2: Salário Médio dos Funcionários")

    nome1 = st.text_input("Nome da pessoa 1", key='nome1')
    salario1 = st.number_input("Salário da Pessoa 1", min_value=0, step=1)

    nome2 = st.text_input("Nome da pessoa 2", key='nome2')
    salario2 = st.number_input("Salário da Pessoa 2", min_value=0, step=1)

    salarioMedio = (salario1 + salario2) / 2
    if st.button("Enviar", key="botao2"):
        st.write(f"O salário médio dos funcionários é R${salarioMedio:.2f}")