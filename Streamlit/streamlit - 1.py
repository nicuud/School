import streamlit as st

st.title('Da?')

st_name = st.text_input('Enter your name', 'Nicu')

st.write(f'SALUT {st_name}!!!')
