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

container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('choose a planet', ['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)

st.number_input('Pick a number', 0, 10)
st.text_input('Email adress')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favourite color')

st.sidebar.title("This is written inside the sidebar")
with st.sidebar
  st.button("Click")
  st.radio("Pick your gender", ["Male", "Female"])
