import streamlit as st
import random

maal_ke_types = {
    "Daaru": (40, 70, "Sir ne itna pi liya ki exam aur attendance dono ek jaise lagne lage – dono mein zero! 🍻"),
    "Cigarette": (50, 80, "Sir ka dimaag bhi cigarette ki tarah slow burn ho raha tha, isiliye answer sheet ka bhi dhuaan udda diya. 🚬💨"),
    "Weed (Gaanja)": (60, 90, "Sir ne itna chill maara ki har answer 'Broo, vibes matter' likh ke full marks de diya! 🌿🔥"),
    "Bhang": (30, 60, "Sir ko laga CBSE ka paper check kar rahe hain, isiliye sabko alag-alag range ke marks diye. 🤯"),
    "LSD": (70, 100, "Sir ko exam sheets rainbow dikh rahi thi, isliye sabko 100/100 ka trip lag gaya! 🌈🌀"),
    "Cocaine": (80, 100, "Speed mein check kara, aankh band karke sabko full marks uda diye! 🚀"),
    "MDMA (Ecstasy)": (75, 95, "Sir itne pyaar mein the ki har answer sheet pe ❤️ mark karke full marks de diya! 😍"),
    "Heroine": (20, 50, "Sir toh aise doob gaye jaise Titanic, bas marks bhi waise hi le dooba. 😵‍💫"),
    "Ketamine": (10, 40, "Sir toh half coma mein the, bas likhne wale ke naam ke hisaab se marks daal diye. 😵"),
}

st.title("Professor Ka Maal Calculator 💨")
choice = st.selectbox("Kaunsa maal lagta hai professor ne phooka tha?", list(maal_ke_types.keys()))

if st.button("Calculate Marks"):
    marks_range = maal_ke_types[choice][:2]
    joke = maal_ke_types[choice][2]
    marks = random.randint(*marks_range)

    st.success(f"Tere marks: {marks}/100 🎉")
    st.write(f"{joke}")
