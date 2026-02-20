import re
import streamlit as st

def nettoyer_ordonnance(texte):
    while re.search(r"\[.*?\]", texte):
        texte = re.sub(r"\[.*?\]", "", texte)
    
    while re.search(r"\(.*?\)", texte):
        texte = re.sub(r"\(.*?\)", "", texte)
    
    lignes = [ligne.strip() for ligne in texte.split("\n")]
    return "\n".join(lignes)

st.title("Nettoyeur d'ordonnances")

texte = st.text_area("Collez l'ordonnance ici")

if st.button("Nettoyer"):
    st.text_area("Résultat", nettoyer_ordonnance(texte))
