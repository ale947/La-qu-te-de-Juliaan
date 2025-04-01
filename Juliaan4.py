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

# Ajout de la musique
audio_file = "votre_piste_audio.mp3"  # Remplacez par le chemin du fichier audio que vous choisirez
st.audio(audio_file, start_time=0, format="audio/mp3", loop=True)  # L'option loop=True fait que la musique tourne en boucle

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
        with open("Quête de Juliaan bis.ppsx", "rb") as f:
            st.download_button(
                label="Suite de la quête Divine",
                data=f,
                file_name="Quête de Juliaan bis.ppsx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow"
            )
    else:
        st.error("Certaines réponses sont incorrectes. Suivez la voix de Juliaan.")
