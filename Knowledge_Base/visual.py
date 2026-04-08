import streamlit as st
from pyDatalog import pyDatalog
from datalog import load_kb

# Load the knowledge base once
kb_data = load_kb()
symptoms = kb_data["symptoms"]
has_symptom = kb_data["has_symptom"]
has_disease = kb_data["has_disease"]
likely_disease = kb_data["likely_disease"]
find_pest_control = kb_data["find_pest_control"]
D = kb_data["D"]
Chemical = kb_data["Chemical"]
pests = kb_data["pests"]
pesticides = kb_data["pesticides"]

st.title("🌱 Avocado Disease & Pest Expert System")
st.write("Powered by pyDatalog + Streamlit")

# ----------- DISEASE DIAGNOSTICS -----------
st.header("🔍 Diagnose a Disease")

selected_symptoms = st.multiselect(
    "Select symptoms:",
    symptoms
)

plant = "UserPlant"

# Add user symptoms
for s in selected_symptoms:
    +has_symptom(plant, s)

if st.button("Analyze Disease"):
    st.subheader("Possible Diseases")
    st.write(has_disease(plant, D))

    st.subheader("Likely Diseases (2+ symptom matches)")
    st.write(likely_disease(plant, D))


# ----------- PEST CONTROL -----------
st.header("🐛 Pest Control Finder")

user_pest = st.text_input("Enter a pest (example: avocado_thrips):")

if st.button("Find Controls"):
    st.subheader("Recommended Chemicals / Tools")
    result = find_pest_control(user_pest, Chemical)
    st.write(result)
