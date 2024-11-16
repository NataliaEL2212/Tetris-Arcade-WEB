import streamlit as st
import pandas as pd

# Nombre y ID de la hoja de Google Sheets
sheet_name = 'Prueba_ESP32C3'
sheet_id = '1Snk1X2fo2bdDaMAv-65TKFtHfwKhnH7yZWj8xtBoj5E'

# URL para exportar la hoja de cálculo en formato CSV
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Leer los datos de Google Sheets
data = pd.read_csv(url)

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Mostrar datos en Streamlit
st.title("Datos desde Google Sheets")

# Mostrar todo el DataFrame
st.subheader("Tabla Completa de Datos")
st.dataframe(df[['USER', 'SCORE', 'FECHA']])


