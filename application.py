import streamlit as st

col1, col2 = st.columns(2)


with col1:
    st.subheader(':red[Simple Interest]')
    p = st.number_input('Principle: ',key='a')
    t = st.number_input('Time: ',key='b')
    r = st.number_input('Interest Rate: ',key='c')

    if st.button('Calculate',key='abc'):
        st.write(f'The Interest amount for {t} years is {p*t*r}')

with col2:
    st.subheader(':red[Compound Interest]')
    pri = st.number_input('Principle: ',key='d')
    tim = st.number_input('Time: ',key='e')
    rat = st.number_input('Interest Rate: ',key='f')

    if st.button('Calculate',key='xyz'):
        st.write(f'The Interest amount for {t} years is {pri*tim*rat}')