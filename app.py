import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male", "Female"])
