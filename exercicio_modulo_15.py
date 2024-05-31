import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber para embarques e desembarques na cidade de Nova York')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Crie um elemento de texto e informe ao leitor que os dados estão sendo carregados.
data_load_state = st.text('Carregando dados...')
# Carregue 10.000 linhas de dados no dataframe.
data = load_data(10000)
# Notifique o leitor de que os dados foram carregados com sucesso.
data_load_state.text("Feito! (usando st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Número de coletas por hora')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Mapa de todas as coletas')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Mapa de todas as coletas as {hour_to_filter}:00')
st.map(filtered_data)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Mapa de todas as coletas as {hour_to_filter}:00')
st.map(filtered_data)

#---------------------------------------------------------------------------------------------

st.title('Segunda parte da atividade')

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"Esta página foi executada {st.session_state.counter} vezes.")
st.button("Executar novamente")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

#---------------------------------------------------------------------------------------------

st.title('Terceira parte da atividade')

@st.cache_data 
def load_data2(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data2("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

#---------------------------------------------------------------------------------------------
st.title('Quarta parte da atividade')

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))