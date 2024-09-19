# Importar las librerías necesarias
from langchain_openai import ChatOpenAI
import streamlit as st
import os  # Usado para leer las variables de entorno
from st_social_media_links import SocialMediaIcons

# Leer la API key desde las variables de entorno
api_key = os.getenv('OPENAI_API_KEY')

# Verificar si la API key está configurada
if not api_key:
    st.error("Error: OPENAI_API_KEY no está configurada. Revisa la configuración de secretos en Streamlit Cloud.")
else:
    # Inicializar el modelo
    llm = ChatOpenAI(model="gpt-4", temperature=0, api_key=api_key)

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
                Eres el asistente virtual para la empresa Inteligencia de Negocios liderada por el Ingeniero Industrial Edwin Quintero Alzate CEO y fundador de la compañia. 
                Debes ayudar a los usuarios a conocer más sobre los productos y servicios para aumentar las ventas. Tus tareas son:
                1. Saludar a los usuarios cordialmente.
                2. Proporcionar información precisa sobre los servicios.
                3. Adaptar las recomendaciones según el tipo de usuario.
                4. Sugerir productos y servicios basados en las necesidades del usuario.
                5. Informar sobre promociones, descuentos y casos de éxito.
            """}
        ]

    # Mostrar mensajes del historial del chat al recargar la app
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Reaccionar a la entrada del usuario
    if prompt := st.chat_input("Hola, escribe tu mensaje..."):
        st.chat_message("user").markdown(prompt)

        # Agregar el mensaje del usuario al historial
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generar la respuesta del asistente
        response = llm.invoke(st.session_state.messages).content

        # Mostrar la respuesta del asistente
        st.chat_message("assistant").markdown(response)

        # Agregar la respuesta al historial del chat
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Pie de página con información del desarrollador y redes sociales
    st.markdown("""
    ---
    **Desarrollador:** Edwin Quintero Alzate  
    **Email:** egqa1975@gmail.com  
    **Tel:** +57-3217199749  
    """)

    social_media_links = [
        "https://www.facebook.com/edwin.quinteroalzate",
        "https://www.linkedin.com/in/edwinquintero0329/",
        "https://github.com/Edwin1719"
    ]

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render()