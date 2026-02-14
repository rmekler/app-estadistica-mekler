import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. Configuración de la página web (Pestaña del navegador)
st.set_page_config(page_title="Calculadora Normal | Rafa Mekler", page_icon="📊", layout="centered")

# Título principal
st.title('📊 Calculadora de Distribución Normal')
st.write('Configura los parámetros de tu población, elige el área a calcular y ajusta el deslizador para ver los resultados en tiempo real.')

# 2. Controles de Parámetros de la Población (Media y Desviación)
st.markdown("### 1. Parámetros de la Población")
col_mu, col_sigma = st.columns(2)
with col_mu:
    # Por defecto inicia en 0 (Estándar), pero se puede cambiar a cualquier número
    mu = st.number_input('Media (μ):', value=0.0, step=0.1)
with col_sigma:
    # Por defecto inicia en 1, no puede ser menor a 0.01 (la desviación no puede ser 0)
    sigma = st.number_input('Desviación Estándar (σ):', min_value=0.01, value=1.0, step=0.1)

# 3. Controles interactivos para el cálculo de Probabilidad
st.markdown("### 2. Cálculo de Probabilidad")
col_area, col_x = st.columns(2)

with col_area:
    tipo_area = st.radio(
        "¿Qué área deseas calcular?",
        ("Del Centro (μ) al Valor X", "Cola Izquierda (Menor a X)", "Cola Derecha (Mayor a X)")
    )

with col_x:
    # ¡Magia pura! El deslizador ajusta sus límites automáticamente según la media y desviación que ingreses
    limite_inf = mu - 4 * sigma
    limite_sup = mu + 4 * sigma
    x_end = st.slider('Selecciona tu Valor de Análisis (X):', 
                      min_value=float(limite_inf), 
                      max_value=float(limite_sup), 
                      value=float(mu + sigma), # Inicia 1 desviación estándar a la derecha
                      step=0.01)

# 4. Cálculos Matemáticos Internos
# Calculamos la Z automáticamente para que el estudiante siga viendo su relación con la tabla
z_calculada = (x_end - mu) / sigma

# Ejes completos
x_line = np.linspace(limite_inf, limite_sup, 1000)
y_line = norm.pdf(x_line, mu, sigma)

# Lógica del sombreado y probabilidad
if tipo_area == "Del Centro (μ) al Valor X":
    x_fill = np.linspace(min(mu, x_end), max(mu, x_end), 100)
    area = abs(norm.cdf(x_end, mu, sigma) - norm.cdf(mu, mu, sigma))
elif tipo_area == "Cola Izquierda (Menor a X)":
    x_fill = np.linspace(limite_inf, x_end, 100)
    area = norm.cdf(x_end, mu, sigma)
else: # Cola Derecha
    x_fill = np.linspace(x_end, limite_sup, 100)
    area = 1 - norm.cdf(x_end, mu, sigma)

prob_pct = area * 100
y_fill = norm.pdf(x_fill, mu, sigma)

# 5. Crear la Gráfica Visual
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x_line, y_line, color='#0077b6', lw=2)
ax.fill_between(x_fill, y_fill, color='#00b4d8', alpha=0.6)

# Ajuste automático del techo de la gráfica para que no choque el texto
ax.set_ylim(bottom=0, top=max(y_line) * 1.15)
ax.set_xlabel('Valores de X', fontsize=11, fontweight='bold')
ax.set_ylabel('Densidad de Probabilidad', fontsize=11, fontweight='bold')

# Líneas guía
ax.axvline(x=mu, color='black', lw=1, linestyle='--') # Centro (Media)
ax.axvline(x=x_end, color='red', lw=1.5, alpha=0.8)   # Corte seleccionado

# Caja de Resultados estática en la esquina superior izquierda
texto_resultados = f"Probabilidad = {prob_pct:.2f}%\nValor Z = {z_calculada:.2f}"
ax.text(0.03, 0.82, texto_resultados, 
        transform=ax.transAxes, color='#0077b6', fontweight='bold', fontsize=11,
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='#0077b6', boxstyle='round,pad=0.3'))

ax.set_title(f'Distribución Normal N(μ={mu}, σ={sigma})')

# 6. Mostrar la gráfica en la web
st.pyplot(fig)

# 7. --- SECCIÓN DE CRÉDITOS Y DERECHOS DE AUTOR ---
st.markdown("---") # Línea divisoria elegante
st.markdown("""
<div style='text-align: center; color: #666666; font-size: 14px;'>
    <strong>Desarrollado por:</strong> Miguel "Rafa" Mekler Granillo | 
    <em>Herramienta interactiva desarrollada para fines <br> académicos y de análisis estadístico.<br> 
    Se permite su uso libre para la docencia y el aprendizaje en el aula | México, 2026</em>
</div>
""", unsafe_allow_html=True)