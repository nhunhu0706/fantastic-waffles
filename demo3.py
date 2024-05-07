import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:
  a = st.number_input('a')
with col2:
  radio = st.radio('Phep toan', ('\+', '\-', 'x', ':'), horizontal=True)
with col3:
  b = st.number_input('b')
ans = st.number_input('Nhap ket qua')
cal = 0

if radio == '\+':
    cal = a + b
elif radio == '\-':
    cal = a - b
elif radio == 'x':
    cal = a*b
elif radio == ':':
    cal = a/b
if st.button('Kiem tra'):
    if cal == ans:
        st.success('Dung')
        st.balloons()
    else:
        st.error(f'Sai, dap so dung la {cal}')