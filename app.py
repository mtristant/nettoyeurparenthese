import streamlit as st

def nettoyer_ordonnance(texte: str) -> str:
    out = []
    bracket_depth = 0
    paren_depth = 0

    for ch in texte:
        if ch == '[':
            bracket_depth += 1
            continue
        if ch == ']':
            if bracket_depth > 0:
                bracket_depth -= 1
            continue

        if ch == '(':
            paren_depth += 1
            continue
        if ch == ')':
            if paren_depth > 0:
                paren_depth -= 1
            continue

        if bracket_depth == 0 and paren_depth == 0:
            out.append(ch)

    lignes = [l.rstrip() for l in "".join(out).splitlines()]
    resultat = "\n".join(l for l in lignes if l.strip() != "")
    return resultat.strip()

st.set_page_config(page_title="Nettoyeur d'ordonnances", layout="wide")
st.title("Nettoyeur d'ordonnances")
st.caption("Supprime tout ce qui est entre [ ... ] et ( ... ), y compris les cas imbriqués. Ignore aussi les crochets orphelins.")

texte = st.text_area("Collez l’ordonnance ici", height=350)

if st.button("Nettoyer", use_container_width=True):
    st.session_state["resultat"] = nettoyer_ordonnance(texte)

st.text_area("Résultat", value=st.session_state.get("resultat", ""), height=350)
