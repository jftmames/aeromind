import streamlit as st

st.set_page_config(page_title="AeroMind AI", layout="wide")

# Encabezado principal
st.markdown("""
# ✈️ AeroMind AI
### Intelligent Load & Fuel Optimization for Sustainable Aviation
""")

# Menú lateral
st.sidebar.title("Menú de Navegación")
st.sidebar.markdown("""
- Inicio
- Producto
- Beneficios
- Casos de uso
- Demo
- Contacto
""")

# Sección: ¿Qué hacemos?
st.header("🚀 Nuestra Misión")
st.write("""
AeroMind AI utiliza algoritmos avanzados de inteligencia artificial para optimizar la distribución de carga y el consumo de combustible en aeronaves comerciales. Nuestra solución ayuda a las aerolíneas a reducir costes operativos, mejorar la sostenibilidad y cumplir con normativas medioambientales.
""")

# Sección: Producto
st.header("🧠 Nuestro Producto")
st.markdown("""
- **Optimización de carga**: distribución inteligente para máxima eficiencia.
- **Rutas eficientes**: planificación adaptada a condiciones reales.
- **Reducción de consumo**: IA que ahorra hasta un 10% de combustible.
- **Dashboard en tiempo real**: visualización de KPIs operativos.
""")

# Sección: Beneficios
st.header("📈 Beneficios Cuantificables")
col1, col2, col3 = st.columns(3)
col1.metric("🔋 Ahorro combustible", "-10%", "Confirmado")
col2.metric("🌱 CO₂ evitado", "890 kg/vuelo", "↓")
col3.metric("💸 Ahorro mensual", "+75.000 €", "Estimado")

# Sección: Casos de uso
st.header("✈️ Casos de Uso Reales")
st.markdown("""
- Rutas transatlánticas con condiciones meteorológicas variables
- Carga variable en vuelos intercontinentales
- Integración con flotas híbridas y tradicionales
""")

# Sección: Demo
st.header("🧪 Prueba nuestra Demo")
st.markdown("Prueba la simulación [aquí](https://aeroptimize-demo.streamlit.app/) para ver el sistema en acción.")

# Sección: Contacto
st.header("📬 Contacto")
st.markdown("""
¿Quieres una demo personalizada o conocer cómo AeroMind AI puede integrarse en tu flota? Escríbenos:

📧 contacto@aeromind.ai  
🌐 www.aeromind.ai
""")

# Footer
st.markdown("""
---
© 2025 AeroMind AI. Todos los derechos reservados.
""")
