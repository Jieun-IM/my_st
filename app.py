import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''a+ar^1+ar^2+ar^3''')

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male", "Female"])

st.checkbox('yes')

container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

