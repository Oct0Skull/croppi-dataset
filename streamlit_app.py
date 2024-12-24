import streamlit as st
import numpy as np
import pandas as pd

# Show the page title and description.
st.title('Elementos de interfaz :iphone:')

###
# Static Table
###
st.header('Static Table')
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns = ('col %d' % i for i in range(20)))
st.table(dataframe)


###
# Dinamuc DF
###
st.header('Dynamic Data Frame')
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns = ('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0)) # 👈 resalta el valor máz de cada columna


###
# Chart
###
st.header('Line Chart')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a', 'b', 'c'])

st.line_chart(chart_data)


###
# Map
###
st.header('Map')
#19.432608, -99.133209.
map_data = pd.DataFrame(
    np.random.randn(250,2) / [50,50] + [19.43,-99.13],
    columns = ['lat', 'lon'])

st.map(map_data)


###
# Slider
###
st.header('Slider')
x= st.slider('x') # 👈 this is a widget
st.write(x,'squared is ', x*x)


###
# Text input
###
st.header('Text Input')
st.text_input("Your name", key="name")

st.session_state.name 


###
# Check Box
###
st.header('Check Box')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a', 'b', 'c'])
    
    chart_data


###
# Columns
###
st.header('Columns')
left_column, right_column = st.columns(2)

# Left column
left_column.subheader('Left column') # 👈 se aplica la funcion sobre el nombre del objeto de posicion que creamos
left_column.button('Press me!')      # objeto de posición: left_column 

# Rigth column using with
with right_column:
    st.subheader('Right column')
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Raivenclaw", "Hufflepuff", "slytherin"))
    st.write(f'You are in {chosen} house! ')


###
# Slidebar items
###

# Selectbox
st.sidebar.subheader('Selectbox')       # 👈 Barra lateral oculta/muestra
add_selectbox = st.sidebar.selectbox(
    'How do you like to be contacted',
    ('Email', 'Home phone','Mobile phone')
)

# Slider
st.sidebar.subheader('Slider')
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0) 
)


