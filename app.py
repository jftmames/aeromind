import streamlit as st

st.set_page_config(page_title="AeroMind AI", layout="wide")

# Sidebar de navegación funcional
st.sidebar.title("Menú de Navegación")
seccion = st.sidebar.radio("Ir a:", [
    "Inicio",
    "Producto",
    "Beneficios",
    "Casos de uso",
    "Demo",
    "Contacto"
])

# Secciones según la selección\if seccion == "Inicio":
    st.title("✈️ AeroMind AI")
    st.subheader("Intelligent Load & Fuel Optimization for Sustainable Aviation")
    st.markdown("""
    AeroMind AI utiliza algoritmos avanzados de inteligencia artificial para optimizar la distribución de carga y el consumo de combustible en aeronaves comerciales. Nuestra solución ayuda a las aerolíneas a reducir costes operativos, mejorar la sostenibilidad y cumplir con normativas medioambientales.
    """)

elif seccion == "Producto":
    st.header("🧠 Nuestro Producto")
    st.markdown("""
    - **Optimización de carga**: distribución inteligente para máxima eficiencia.
    - **Rutas eficientes**: planificación adaptada a condiciones reales.
    - **Reducción de consumo**: IA que ahorra hasta un 10% de combustible.
    - **Dashboard en tiempo real**: visualización de KPIs operativos.
    """)

elif seccion == "Beneficios":
    st.header("📈 Beneficios Cuantificables")
    col1, col2, col3 = st.columns(3)
    col1.metric("🔋 Ahorro combustible", "-10%", "Confirmado")
    col2.metric("🌱 CO₂ evitado", "890 kg/vuelo", "↓")
    col3.metric("💸 Ahorro mensual", "+75.000 €", "Estimado")

elif seccion == "Casos de uso":
    st.header("✈️ Casos de Uso Reales")
    st.markdown("""
    - Rutas transatlánticas con condiciones meteorológicas variables
    - Carga variable en vuelos intercontinentales
    - Integración con flotas híbridas y tradicionales
    """)

elif seccion == "Demo":
    st.header("🧪 Prueba nuestra Demo")
    st.markdown("Prueba la simulación [aquí](https://aeroptimize-demo.streamlit.app/) para ver el sistema en acción.")

elif seccion == "Contacto":
    st.header("📬 Contacto")
    st.markdown("""
    ¿Quieres una demo personalizada o conocer cómo AeroMind AI puede integrarse en tu flota? Escríbenos:

    📧 contacto@aeromind.ai  
    
    """)

# Footer general
st.markdown("""
---
© 2025 AeroMind AI. Todos los derechos reservados.
""")
