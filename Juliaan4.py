import streamlit as st 

# Questions et réponses correctes
questions = [
    {"question": "Par quel méthode barbare est morte Marie Madeleine ?", "correct_answer": "La lapidation"},
    {"question": "Comment s'appelle la femelle du cochon ?", "correct_answer": "La truie"},
    {"question": "Quel est le mot le plus long de la langue française ?", "correct_answer": "Intergouvernementalisations"},
    {"question": "Comment appelle t'on les habitants de la commune de Y ?", "correct_answer": "Les ypsiloniens"}
]

# Fonction pour vérifier si les réponses sont correctes
def check_answers(responses):
    return all(responses[i].lower() == questions[i]["correct_answer"].lower() for i in range(len(questions)))

# Interface Streamlit
st.title("Epreuve de Jésus")

# Ajouter l'audio en arrière-plan
audio_file = "Epic Battle Music (No Copyright) Dragon Castle by @Makai-symphony.mp3"  # Remplacez ce chemin par le vôtre
st.audio(audio_file, start_time=0, format="audio/mp3", autoplay=True, loop=True)

# Variables pour stocker les réponses des utilisateurs
responses = []

# Pose les questions et récupère les réponses
for i, q in enumerate(questions):
    response = st.text_input(q["question"], key=i)
    responses.append(response)

# Vérifie les réponses après que l'utilisateur ait rempli toutes les questions
if st.button("Soumettre"):
    if check_answers(responses):
        st.success("Félicitations, vous avez toutes les bonnes réponses !")
        # Ajoutez ici le lien pour télécharger un fichier
        with open("Quête de Juliaan bis new.ppsx", "rb") as f:
            st.download_button(
                label="Suite de la quête Divine",
                data=f,
                file_name="Quête de Juliaan bis new.ppsx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow"
            )
    else:
        st.error("Certaines réponses sont incorrectes. Suivez la voix de Juliaan.")
