import streamlit as st

# Définition des questions
questions = [
    {"question": "Par quelle méthode barbare est morte Marie Madeleine ?", "reponse": "La lapidation"},
    {"question": "Comment s'appelle la femelle du cochon ?", "reponse": "La truie"},
    {"question": "Quel est le mot le plus long de la langue française ?", "reponse": "Intergouvernementalisations"},
    {"question": "Comment appelle-t-on les habitants de la commune de Y ?", "reponse": "Les ypsiloniens"}
]

# Initialisation de l'état
if "index_question" not in st.session_state:
    st.session_state.index_question = 0
    st.session_state.score = 0
    st.session_state.reponse_utilisateur = ""

# Affichage de la question actuelle
if st.session_state.index_question < len(questions):
    question_actuelle = questions[st.session_state.index_question]
    st.write(f"**{question_actuelle['question']}**")

    # Champ de réponse utilisateur
    reponse_utilisateur = st.text_input("Votre réponse :", value="", key=f"reponse_{st.session_state.index_question}")

    # Validation de la réponse
    if st.button("Valider"):
        if reponse_utilisateur.strip().lower() == question_actuelle["reponse"].lower():
            st.success("Bonne réponse !")
            st.session_state.index_question += 1  # Passer à la question suivante
            st.session_state.score += 1
            st.experimental_rerun()
        else:
            st.error("Mauvaise réponse, essaye encore !")
else:
    st.success(f"Bravo ! Tu as répondu à toutes les questions avec un score de {st.session_state.score}/{len(questions)} 🎉")

    # Ajout du lien cliquable vers la Bible
    st.markdown("[📖 Lire la Bible en ligne](https://www.aelf.org/bible)")
