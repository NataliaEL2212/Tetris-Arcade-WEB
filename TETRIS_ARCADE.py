import streamlit as st
import matplotlib.pyplot as plt
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

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Wallpoet&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&family=Wallpoet&display=swap');
    /* Cambiar el color de fondo global */
    body {
        background-color: white;
    }
    /* Opcional: Cambiar el color del contenedor principal */
    .stApp {
        background-color: black;
        color: white;
    }
    .titulo {
        font-size: 160px !important; /* Tamaño del título */
        color: #13a7fd;  /* Color del título */
        font-weight: bold;
        text-align: center; /* Centrar el título */
        margin-bottom: -30px;
    }
    .subtitulo {
        font-size: 55px !important; /* Tamaño del subtítulo */
        color: blanco;  /* Color del subtítulo */
        text-align: center; /* Centrar el subtítulo */
    }
    .subsubtitulo {
        font-size: 30px !important; /* Tamaño del subtítulo */
        color: blanco;  /* Color del subtítulo */
        text-align: center; /* Centrar el subtítulo */
    }
    .space {
        font-size: 35px !important; /* Tamaño del subtítulo */
        color: black;  /* Color del subtítulo */
        text-align: center; /* Centrar el subtítulo */
    }
    /* Cambiar la fuente global */
    body {
        color: white !important; /* Forzar texto blanco */
        font-size: 20px;
        font-family: 'Courier New', monospace; /* Cambia por la fuente que desees */
        text-align: center; /* Centrar el body */
    }

    /* Cambiar la fuente del título */
    h1 {
        font-family: 'Comic Sans MS', cursive, sans-serif; 
        color: #FF5733; /* Cambiar el color del título */
    }

    /* Cambiar la fuente del subtítulo */
    h2 {
        font-family: 'Georgia', serif;
        color: #4CAF50;
    }

    /* Cambiar la fuente de los párrafos */
    p {
        font-family: 'Wallpoet', sans-serif;
        font-size: 16px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.image("logo_pucp.png", width=200,use_container_width=False)

# Mostrar el título con CSS personalizado
st.markdown('<p class="titulo">TETRIS</p>', unsafe_allow_html=True)

st.image("arcade.gif", width=500,use_container_width=True)
st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)
st.image("tetris_mark.jpg", width=300,use_container_width=True)
st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)


# Mostrar el subtítulo con CSS personalizado
st.markdown('<p class="subtitulo">TOP 3</p>', unsafe_allow_html=True)
st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)

# Datos del podio

# Obtener datos para el podio
users = [df["USER2"].iloc[0], df["USER1"].iloc[0], df["USER3"].iloc[0]]  # Orden: derecha, centro, izquierda
scores = [int(df["SCORE2"].iloc[0]), int(df["SCORE1"].iloc[0]), int(df["SCORE3"].iloc[0])]  # Convertir a enteros

# Colores para cada posición
colors = ["#009ac8", "#ffa300", "#d10161"]  # Colores para las barras del podio (izquierda, centro, derecha)

# Crear el gráfico del podio
fig, ax = plt.subplots(figsize=(6, 4))
fig.patch.set_facecolor('black') 

# Dibujar las barras del podio
bars = ax.bar(["3rd", "1st", "2nd"], scores, color=colors, edgecolor="black", linewidth=2)

# Añadir texto en las barras
for bar, user, score in zip(bars, users, scores):
    # Nombre del usuario encima de la barra
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 8,
        user,
        ha="center",
        fontsize=14,
        color="white",
        weight="bold",
    )
    # Puntaje dentro de la barra
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() / 2,
        str(score),
        ha="center",
        fontsize=14,
        color="white",
        weight="bold",
    )

# Personalizar diseño
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

# Mostrar el gráfico del podio en Streamlit
st.pyplot(fig)

# Para la tabla general:

st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)
st.image("tetris_mark.jpg", width=300,use_container_width=True)
st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitulo">PUNTAJES GLOBALES</p>', unsafe_allow_html=True)
st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)

df_limited = df[['USER', 'SCORE', 'FECHA']]

# Convertir DataFrame a HTML con estilos personalizados
table_html = df_limited.to_html(classes='styled-table', index=False)

# Estilos CSS personalizados para la tabla
st.markdown(
    """
    <style>
    .table-container {
        max-height: 600px; /* Altura máxima para la tabla */
        overflow-y: auto; /* Barra de desplazamiento vertical */
        margin: 0 auto; /* Centrar la tabla */
        padding: 10px;
        background-color: black; /* Fondo negro */
        border: 1px solid white; /* Borde alrededor del contenedor */
        border-radius: 10px; /* Bordes redondeados */
    }
    .styled-table {
        border-collapse: collapse;
        font-size: 18px;
        font-family: 'Courier New', monospace;
        min-width: 400px;
        color: white; /* Texto blanco */
        background-color: black; /* Fondo negro */
        width: 100%;
    }
    .styled-table thead tr {
        background-color: #333333; /* Fondo oscuro para encabezados */
        color: white; /* Texto blanco */
        text-align: center;
    }
    .styled-table th,
    .styled-table td {
        border: 1px solid white; /* Bordes blancos */
        padding: 12px 15px;
        text-align: center; /* Centrar texto */
    }
    .styled-table tbody tr {
        border-bottom: 1px solid #dddddd;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Mostrar la tabla HTML con un contenedor con barra deslizable
st.markdown('<div class="table-container">' + table_html + '</div>', unsafe_allow_html=True)
st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)

st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)
st.image("tetris_mark.jpg", width=300,use_container_width=True)
st.markdown('<p class="space">ESPACIO</p>', unsafe_allow_html=True)

st.markdown('<p class="subsubtitulo">SOBRE EL PROYECTO</p>', unsafe_allow_html=True)

st.markdown('<body></body>', unsafe_allow_html=True)
st.markdown('<body>Este proyecto fue creado para el curso de Sistemas Digitales durante el semestre 2024-2, titulado TETRIS ARCADE. Integra una TM4C123GH6PM y un ESP32C3 para emular el juego Tetris, incluyendo una pantalla Nokia5110, pulsadores y un buzzer.</body>', unsafe_allow_html=True)
st.markdown('<body></body>', unsafe_allow_html=True)
st.markdown('<body>Desarrollado mediante Code Composer, Arduino IDE y Visual Studio Code.</body>', unsafe_allow_html=True)
st.markdown('<body>Integrado con Apps Script y Streamlit Cloud.</body>', unsafe_allow_html=True)
st.markdown('<body></body>', unsafe_allow_html=True)
st.markdown('<body>Autores:</body>', unsafe_allow_html=True)
st.markdown('<body>-Natalia Escudero Lay</body>', unsafe_allow_html=True)
st.markdown('<body>-Santiago Tarazona</body>', unsafe_allow_html=True)
