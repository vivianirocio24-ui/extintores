from datetime import datetime
import pandas as pd
import streamlit as st

# Configuración de la página para vista móvil
st.set_page_config(
    page_title="Control de Matafuegos", page_icon="🧯", layout="centered"
)

st.title("🧯 Control de Extintores en Campo")
st.markdown("Usa la cámara para capturar el código o ingresa los datos abajo.")

# 📷 Cámara nativa (Funciona en todos los celulares y PCs sin instalar nada raro)
foto_codigo = st.camera_input("📷 Tomar foto al Código del Matafuego")

codigo_detectado = ""
if foto_codigo is not None:
  st.success("¡Foto capturada con éxito!")
  # Aquí puedes asignar un identificador o procesar la lectura
  codigo_detectado = "EXTINTOR-CAPTURADO"

# Campo de texto opcional por si prefieren escribirlo o usar pistola lectora
serie_input = st.text_input("Nº de Serie / Código manual", value=codigo_detectado)

# Archivo local simulado como base de datos
DB_FILE = "base_matafuegos.xlsx"


@st.cache_data
def cargar_datos():
  try:
    return pd.read_excel(DB_FILE)
  except FileNotFoundError:
    return pd.DataFrame(
        columns=[
            "Serie",
            "Agente",
            "Fabricacion",
            "Vencimiento_Carga",
            "Vencimiento_PH",
        ]
    )


df = cargar_datos()
