import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Relatório Mensal JK")

#Roupas

with st.container():
    st.title("JK roupas e calçados")
    st.subheader("Movimentação mensal sobre as vendas de roupas e calçados")
    st.write("---")
    st.subheader("Informações sobre as vendas de roupas masculinas e femininas no mês de Novembro")


@st.cache_data
def carregar_dados_roupasm():
    tabela_roupasm = pd.read_csv("Vendas_Joao.csv", encoding="latin1")
    return tabela_roupasm


with st.container():
    st.write("---")
st.subheader("Roupas masculinas vendidas no mês de novembro por João:")
qtde_dias_1 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_1")
num_dias = int(qtde_dias_1.replace("D", " "))
dados = carregar_dados_roupasm()
dados = dados[:num_dias]
st.area_chart(dados, x="Data", y="Quantidade")

@st.cache_data
def carregar_dados_roupasf():
    tabela_roupasf = pd.read_csv("Vendas_Katia.csv", encoding="latin1")
    return tabela_roupasf


with st.container():
    st.write("---")
st.subheader("Roupas femininas vendidas no mês de novembro por Kátia:")
qtde_dias_2 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_2")
num_dias = int(qtde_dias_2.replace("D", " "))
dados = carregar_dados_roupasf()
dados = dados[:num_dias]
st.area_chart(dados, x="Data", y="Quantidade")


with st.container():
    st.write("---")
st.subheader("Valor faturado com vendas de roupas masculinas no mês de novembro por João:")
qtde_dias_3 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_3")
num_dias = int(qtde_dias_3.replace("D", " "))
dados = carregar_dados_roupasm()
dados = dados[:num_dias]
st.bar_chart(dados, x="Data", y="Valor Total (R$)")


with st.container():
    st.write("---")
st.subheader("Valor faturado com vendas de roupas femininas no mês de novembro por Kátia:")
qtde_dias_4 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_4")
num_dias = int(qtde_dias_4.replace("D", " "))
dados = carregar_dados_roupasf()
dados = dados[:num_dias]
st.bar_chart(dados, x="Data", y="Valor Total (R$)")


st.write("---")


#Calçados


@st.cache_data
def carregar_dados_calcadosm():
    tabela_calcadosm = pd.read_csv("Calcados_Joao.csv", encoding="latin1")
    return tabela_calcadosm

with st.container():
    st.write("---")
    st.subheader("Informações sobre as vendas de calçados masculinos e femininos no mês de Novembro")


with st.container():
    st.write("---")
st.subheader("Calçados masculinos vendidos no mês de novembro por João:")
qtde_dias_5 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_5")
num_dias = int(qtde_dias_5.replace("D", " "))
dados = carregar_dados_calcadosm()
dados = dados[:num_dias]
st.area_chart(dados, x="Data", y="Quantidade")

@st.cache_data
def carregar_dados_calcadosf():
    tabela_calcadosf = pd.read_csv("Calcados_Katia.csv", encoding="latin1")
    return tabela_calcadosf

with st.container():
    st.write("---")
st.subheader("Calçados femininos vendidos no mês de novembro por Kátia:")
qtde_dias_6 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_6")
num_dias = int(qtde_dias_6.replace("D", " "))
dados = carregar_dados_calcadosf()
dados = dados[:num_dias]
st.area_chart(dados, x="Data", y="Quantidade")

with st.container():
    st.write("---")
st.subheader("Valor faturado com vendas de calçados masculinos no mês de novembro por João:")
qtde_dias_7 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_7")
num_dias = int(qtde_dias_7.replace("D", " "))
dados = carregar_dados_calcadosm()
dados = dados[:num_dias]
st.bar_chart(dados, x="Data", y="Valor Total (R$)")

with st.container():
    st.write("---")
st.subheader("Valor faturado com vendas de calçados femininos no mês de novembro por Kátia:")
qtde_dias_8 = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"], key="dias_8")
num_dias = int(qtde_dias_8.replace("D", " "))
dados = carregar_dados_calcadosf()
dados = dados[:num_dias]
st.bar_chart(dados, x="Data", y="Valor Total (R$)")

