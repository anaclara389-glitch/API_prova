import streamlit as st
from consumidor_api import consultar_clima

st.set_page_config(page_title="Clima em Tempo Real", layout="centered")

st.title("Clima em Tempo Real")
st.write("Dados meteorológicos de Jaraguá do Sul - SC")

if st.button("Consultar novamente"):
    st.rerun()

try:
    with st.spinner("Consultando a API..."):
        dados = consultar_clima()

    st.success("Consulta concluída.")

    st.subheader("Condições atuais")

    st.metric("Temperatura", f"{dados['temperatura']:.1f} °C")
    st.metric("Umidade relativa", f"{dados['umidade_relativa']:.0f} %")
    st.metric("Sensação térmica", f"{dados['sensacao_termica']:.1f} °C")
    st.metric("Precipitação", f"{dados['precipitacao']:.1f} mm")
    st.metric("Velocidade do vento", f"{dados['velocidade_vento']:.1f} km/h")

    st.caption(f"Horário informado pela API: {dados['horario']}")

except Exception as erro:
    st.error(f"Erro durante a consulta: {erro}")
