import streamlit as st
import webbrowser

# Définition des questions
questions = [
    {"question": "Par quel méthode barbare est morte Marie Madeleine ?", "reponse": "La lapidation"},
    {"question": "Comment s'appelle la femelle du cochon ?", "reponse": "La truie"},
    {"question": "Quel est le mot le plus long de la langue française ?", "reponse": "Intergouvernementalisations"},
    {"question": "Comment appelle t'on les habitants de la commune de Y ?", "reponse": "Les ypsiloniens"}
]

# Initialisation de l'index de la question
if "index_question" not in st.session_state:
    st.session_state.index_question = 0
    st.session_state.score = 0

# Affichage de la question actuelle
if st.session_state.index_question < len(questions):
    question_actuelle = questions[st.session_state.index_question]
    st.write(f"**{question_actuelle['question']}**")

    reponse_utilisateur = st.text_input("Votre réponse :")

    if st.button("Valider"):
        if reponse_utilisateur.strip().lower() == question_actuelle["reponse"].lower():
            st.success("Bonne réponse !")
            st.session_state.index_question += 1
            st.session_state.score += 1
            st.experimental_rerun()
        else:
            st.error("Mauvaise réponse, essaye encore !")
else:
    st.success("Bravo ! Tu as répondu à toutes les questions !")
    if st.button("Lire la Bible en ligne"):
        webbrowser.open("https://www.aelf.org/bible")
