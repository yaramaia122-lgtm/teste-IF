import streamlit as st

st.title("Refatorador de Código com IA")

code_input = st.text_area("Cole seu código sujo aqui:")

if st.button("Analisar com IA"):
    # Aqui você simula o que a IA faria ou ensina eles a colarem 
    # o output do ChatGPT em um campo de resposta
    st.subheader("Sugestão de Melhoria:")
    st.code("# O código limpo apareceria aqui...", language='python')
    st.success("Dica da IA: Use nomes de variáveis mais descritivos!")
