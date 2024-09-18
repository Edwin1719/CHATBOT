# Importar las librerías necesarias
from langchain_openai import ChatOpenAI
import streamlit as st
import json
from st_social_media_links import SocialMediaIcons

# Inicializar el modelo
llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key="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")

# Incluir logo a la izquierda y título a la derecha
st.markdown("""
    <div style='background-color: #333333; padding: 10px; border-radius: 10px; display: flex; align-items: center;'>
        <img src='https://w7.pngwing.com/pngs/576/346/png-transparent-business-analytics-computer-icons-predictive-analytics-business-intelligence-lean-miscellaneous-angle-business-intelligence-thumbnail.png' alt='Logo de la Empresa' style='width: 100px; margin-right: 20px;'>
        <h1 style='color: white; font-size: 32px;'>CHATBOT INTELIGENCIA DE NEGOCIOS</h1>
    </div>
    """, unsafe_allow_html=True)

# Inicializar el historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = [
    {"role": "system", "content": """
        Eres el asistente virtual para la empresa Inteligencia de Negocios liderada por el Ingeniero Industrial Edwin Quintero Alzate CEO y fundador de la compañia y que esta Ubicada en la Ciudad de Pereira Colombia. 
        Tu objetivo es proporcionar una experiencia amigable y personalizada. Debes ayudar a los usuarios a conocer más sobre los productos y servicios de la empresa para aumentar las ventas. Tus tareas son:
        1. Saludar a los usuarios de forma cordial.
        2. Proporcionar información precisa y actualizada sobre los servicios y productos que ofrece la empresa. Esto incluye:
           - Descripción de servicios de Machine Learning, IA, Visualizacion de datos con Power BI, automatización con Python, análisis de datos, etc.
           - Precios detallados, teniendo en cuenta que se cobra por hora trabajada en dolares y que el precio para Machine Leraning es de 100 USD, para Visualizacion de Datos 80 USD, para Automatizacion 90 USD y para Inteligencia Artificial 120 USD todo ello dependiendo de la complejidad del proyecto, tamaño de los datos y otros factores importantes, incluyendo tambien posibles descuentos y paquetes.
           - Casos de éxito y cómo nuestros servicios han ayudado a otras empresas.
        3. Identificar el tipo de usuario (potencial, recurrente, corporativo) para adaptar las recomendaciones.
        4. Responder preguntas generales sobre la empresa, como ubicación, horarios de atención, y redes sociales.
        5. Asistir en la programación de citas de ventas o demostraciones para los servicios, discriminando si la cita será vía telefónica, chat o videoconferencia.
        6. Sugerir productos y servicios con base en las necesidades expresadas por el usuario.
        7. Informar sobre promociones, descuentos especiales y ofertas temporales.
        8. Redirigir al usuario a un agente de ventas o soporte técnico cuando sea necesario para finalizar el proceso de compra.
    """}
]
# Mostrar mensajes del historial del chat al recargar la app
for message in st.session_state.messages:
    # No mostramos el mensaje del sistema en la interfaz
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Reaccionar a la entrada del usuario
if prompt := st.chat_input("Hola escribe tu mensaje.."):
    # Mostrar el mensaje del usuario en el contenedor de mensajes
    st.chat_message("user").markdown(prompt)
    
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Crear una copia de los mensajes para pasar al modelo
    messages = st.session_state.messages.copy()

    # Generar la respuesta del asistente
    response = llm.invoke(messages).content
    
    # Mostrar la respuesta del asistente en el contenedor de mensajes
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Agregar la respuesta al historial del chat
    st.session_state.messages.append({"role": "assistant", "content": response})

# Pie de página con información del desarrollador y logos de redes sociales
st.markdown("""
---
**Desarrollador:** Edwin Quintero Alzate/
**Email:** egqa1975@gmail.com/
**Tel:** +57-3217199749
""")

social_media_links = [
    "https://www.facebook.com/edwin.quinteroalzate",
    "https://www.linkedin.com/in/edwinquintero0329/",
    "https://github.com/Edwin1719"]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()
