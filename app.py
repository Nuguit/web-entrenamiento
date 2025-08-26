import streamlit as st

st.markdown(
    """
    <style>
        .stApp {
            background-color: #C6EBAE; 
        }

        
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="font-size: 80px; color:#FFFFFF;">PalMotion</h1>
        <h3 style="font-size: 30px; color:#117A65;">No hay excusas</h3>
    </div>
""", unsafe_allow_html=True)

st.image("principal.png", use_container_width=True)

st.markdown("""
<div style="text-align:center; font-size:20px; margin-bottom:30px;">
Bienvenido a <strong>PalMotion</strong>, donde pensamos que el entorno debe ser un aliciente para moverse y estar en forma.
Si quieres reconciliarte con el deporte, este es tu sitio. <strong>¿Comenzamos?</strong>
</div>
""", unsafe_allow_html=True)


defaults = {
    "step": 1,
    "edad": None,
    "entreno": None,
    "tipo_entreno": None
}
for var, default in defaults.items():
    if var not in st.session_state:
        st.session_state[var] = default


ejercicios = {
    "Casa": {
        "Tren Inferior": [
            {"titulo": "Sentadillas con silla", "descripcion": "3 series de 15 repeticiones. Descanso de 45 segundos entre series.", "imagen": "c1.png"},
            {"titulo": "Zancadas hacia atrás", "descripcion": "3 series de 10 repeticiones por pierna. Descanso de 45 segundos entre series.", "imagen": "c2.png"},
           {"titulo": "Sentadilla isométrica en la pared", "descripcion": "2 series de 30 repeticiones. Descanso de 45 segundos.", "imagen": "c5.png"},
            {"titulo": "Elevación de talones", "descripcion": "3 series de 20 repeticiones. Descanso de 30 segundos.", "imagen": "c4.png"},
            {"titulo": "Puente de glúteos", "descripcion": "3 series de 15 repeticiones. Descanso de 30 segundos.", "imagen": "c3.png"}
            
        ],
        "Tren Superior": [
            {"titulo": "Flexiones apoyando rodillas", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "c6.png"},
            {"titulo": "Fondos en silla", "descripcion": "3 series de 12 repeticiones. Descanso de 45 segundos.", "imagen": "c7.png"},
            {"titulo": "Remo con botellas", "descripcion": "3 series de 12 repeticiones. Descanso de 45 segundos", "imagen": "c8.png"},
            {"titulo": "Press de hombros con botellas", "descripcion": "3 series de 12 repeticiones. Descanso de 45 segundos.", "imagen": "c9.png"},
            {"titulo": "Plancha con apoyo de rodillas", "descripcion": "2 series de 25 segundos. Descanso de 45 segundos.", "imagen": "c10.png"}
        ],
        "Ejercicios Genéricos": [
            {"titulo": "Jumping Jacks", "descripcion": "3 series de 30 segundos. Descanso de 30 segundos.", "imagen": "c11.png"},
            {"titulo": "Sentadilla con brazo al frente", "descripcion": "3 series de 15 repeticiones. Descanso de 45 segundos.", "imagen": "c12.png"},
            {"titulo": "Flexión apoyando rodillas + plancha", "descripcion": "3 series de 10 flexiones + 10 segundos de plancha. Descanso de 60 segundos.", "imagen": "c13.png"},
            {"titulo": "Puente de glúteos + elevación de pierna", "descripcion": "3 series de 10 repeticiones por pierna. Descanso de 45 segundos.", "imagen": "c14.png"},
            {"titulo": "Estiramientos finales", "descripcion": "5 minutos.", "imagen": "c15.png"}
        ]
    },
    "Aire Libre": {
        "Tren Inferior": [
            {"titulo": "Sentadillas", "descripcion": "30 minutos de trote suave.", "imagen": "n1.png"},
            {"titulo": "Zancadas caminando", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n2.png"},
            {"titulo": "Sentadilla isométrica apoyado", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n5.png"},
            {"titulo": "Elevaciones de talones", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n4.png"},
            {"titulo": "Puente de glúteos", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n3.png"}
            
        ],
        "Tren Superior": [
            {"titulo": "Flexiones con rodillas apoyadas", "descripcion": "3 series de 12 repeticiones.", "imagen": "n6.png"},
            {"titulo": "Fondos en banco o roca baja", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n7.png"},
            {"titulo": "Remo invertido", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n8.png"},
            {"titulo": "Press de hombros con peso", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n9.png"},
            {"titulo": "Plancha", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n10.png"}
        ],
        "Ejercicios Genéricos": [
            {"titulo": "Caminata rápida o trote suave (10min)", "descripcion": "5-10 minutos para piernas y espalda.", "imagen": "n11.png"},
            {"titulo": "Saltos laterales pequeños", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n12.png"},
            {"titulo": "Sentadilla con brazos al frente", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n13.png"},
            {"titulo": "Escaladores", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n14.png"},
            {"titulo": "Estiramientos", "descripcion": "3 series de 10-12 repeticiones.", "imagen": "n15.png"}
        ]
    },
    "Gimnasio": {
        "Tren Inferior": [
            {"titulo": "Sentadillas con barra", "descripcion": "4 series de 12 repeticiones. Descanso de 90 segundos", "imagen": "g1.png"},
            {"titulo": "Prensa de piernas", "descripcion": "3 series de 12 repeticiones. Descanso de 60 segundos", "imagen": "g2.png"},
            {"titulo": "Zancadas con mancuernas", "descripcion": "3 series de 10 repeticiones por pierna. Descanso de 60 segundos", "imagen": "g3.png"},
            {"titulo": "Elevaciones de talones", "descripcion": "3 series de 20 repeticiones. Descanso de 30 segundos", "imagen": "g4.png"},
            {"titulo": "Hip trust", "descripcion": "3 series de 15 repeticiones. Descanso de 60 segundos", "imagen": "g5.png"}
        ],
        "Tren Superior": [
            {"titulo": "Press de banca", "descripcion": "4 series de 12 repeticiones. Descanso de 90 segundos", "imagen": "g6.png"},
            {"titulo": "Dominadas o jalón al pecho", "descripcion": "3 series de 10 repeticiones. Descanso de 90 segundos", "imagen": "g7.png"},
            {"titulo": "Remo con barra", "descripcion": "3 series de 12 repeticiones. Descanso de 60 segundos", "imagen": "g10.png"},
            {"titulo": "Curl bíceps con barra", "descripcion": "3 series de 12 repeticiones. Descanso de 60 segundos", "imagen": "g8.png"},
            {"titulo": "Fondo de tríceps", "descripcion": "3 series de 12 repeticiones. Descanso de 60 segundos", "imagen": "g9.png"}
        ],
        "Ejercicios Genéricos": [
            {"titulo": "Sentadillas con barra", "descripcion": "3 series de 10 repeticiones. Descanso de 60 segundos.", "imagen": "g11.png"},
            {"titulo": "Press de banca", "descripcion": "3 series de 10 repeticiones. Descanso de 60 segundos", "imagen": "g12.png"},
            {"titulo": "Remo con mancuernas", "descripcion": "3 series de 10 repeticiones. Descanso de 60 segundos", "imagen": "g13.png"},
            {"titulo": "Zancadas alternas", "descripcion": "3 series de 10 repeticiones por pierna. Descanso de 60 segundos", "imagen": "g14.png"},
            {"titulo": "Press militar", "descripcion": "3 series de 10 repeticiones. Descanso de 60 segundos", "imagen": "g15.png"},
            {"titulo": "Plancha", "descripcion": "3 repeticiones de 30-60 segundos. Descanso de 30 segundos", "imagen": "n10.png"}
        ]
    }
}


if st.session_state.step == 1:
    st.session_state.edad = st.slider("Elige tu edad:", 14, 100, 25, key="edad_slider")
    if st.button("Siguiente", key="btn1"):
        st.session_state.step = 2

elif st.session_state.step == 2:
    opciones_entreno = ["Casa", "Aire Libre", "Gimnasio"]
    st.radio("¿Dónde piensas entrenar?", opciones_entreno, key="entreno_radio")
    if st.button("Siguiente", key="btn2"):
        st.session_state.entreno = st.session_state.entreno_radio
        st.session_state.step = 3

elif st.session_state.step == 3:
    opciones_tipo = ["Tren Inferior", "Tren Superior", "Ejercicios Genéricos"]
    st.radio("¿Qué quieres entrenar?", opciones_tipo, key="tipo_radio")
    if st.button("Siguiente", key="btn3"):
        st.session_state.tipo_entreno = st.session_state.tipo_radio
        st.session_state.step = 4

elif st.session_state.step == 4:
    
    left, center, right = st.columns([1, 2, 1])

    with center:
        
        st.markdown(
            "<h3 style='text-align:center;'>¿Estás seguro de tus respuestas?</h3>",
            unsafe_allow_html=True
        )

        
        c1, c2 = st.columns(2)

        # Botones a ancho completo de su columna
        si = c1.button("Sí", key="btn_si", use_container_width=True)
        no = c2.button("No", key="btn_no", use_container_width=True)

    # 3) Manejo de eventos
    if si:
        st.session_state.step = 5
    if no:
        st.session_state.step = 1




elif st.session_state.step == 5:
    if not st.session_state.entreno or not st.session_state.tipo_entreno:
        st.error("⚠️ No se han guardado correctamente tus elecciones. Vuelve atrás y selecciona de nuevo.")
        st.session_state.step = 1
    else:
        st.markdown("<h2 style='text-align:center;'>¡Tu plan de entrenamiento personalizado!</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; font-size:20px;'>Has elegido entrenar en <strong>{st.session_state.entreno}</strong> y enfocarte en <strong>{st.session_state.tipo_entreno}</strong>.</p>", unsafe_allow_html=True)

        
        plan = ejercicios[st.session_state.entreno][st.session_state.tipo_entreno]
        num_cols = 2
        for i in range(0, len(plan), num_cols):
            cols = st.columns(num_cols)
            for j, ejercicio in enumerate(plan[i:i+num_cols]):
                with cols[j]:
                    st.markdown(f"""
                        <div style="
                            text-align:center; 
                            padding:15px; 
                            border:1px solid #ccc; 
                            border-radius:15px; 
                            box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
                            margin-bottom:10px; 
                            background-color:#FFFFFF;">
                            <h3 style="font-size:20px; color:#117A65;">{ejercicio['titulo']}</h3>
                        </div>
                    """, unsafe_allow_html=True)
                    st.image(ejercicio['imagen'], use_container_width=True)
                    st.markdown(f"<p style='text-align:center; font-size:16px;'>{ejercicio['descripcion']}</p>", unsafe_allow_html=True)