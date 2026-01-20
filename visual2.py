# visual.py
import streamlit as st
import pyDatalog
from datalog import load_kb

# ---------------- LOAD KB ----------------
kb = load_kb()

causes = kb["causes"]
root_related_disease = kb["root_related_disease"]
fruit_disease = kb["fruit_disease"]

pest_basic = kb["pest_basic"]
category_basic = kb["category_basic"]
controls_basic = kb["controls_basic"]
type_basic = kb["type_basic"]

pest = kb["pest"]
controls_pest = kb["controls_pest"]
fungal_disease = kb["fungal_disease"]
controls_disease = kb["controls_disease"]
symptoms = kb["symptoms"]
has_symptom = kb["has_symptom"]

Chemical = kb["Chemical"]
D = kb["D"]

insecticide = kb["insecticide"]
miticide = kb["miticide"]
fungicide = kb["fungicide"]
natural_solution = kb["natural_solution"]
biopesticide = kb["biopesticide"]
biocontrol = kb["biocontrol"]

is_systemic = kb["is_systemic"]
is_translaminar = kb["is_translaminar"]
is_contact = kb["is_contact"]
is_stomach_poison = kb["is_stomach_poison"]
is_protectant = kb["is_protectant"]
is_fungistat = kb["is_fungistat"]
is_post_harvest = kb["is_post_harvest"]
is_selective = kb["is_selective"]
is_non_selective = kb["is_non_selective"]
is_organic = kb["is_organic"]
application_method = kb["application_method"]


def control_classification(c):
    classes = []
    if insecticide(c): classes.append("insecticide")
    if miticide(c): classes.append("miticide")
    if fungicide(c): classes.append("fungicide")
    if natural_solution(c): classes.append("natural_solution")
    if biopesticide(c): classes.append("biopesticide")
    if biocontrol(c): classes.append("biocontrol")
    return classes or ["unclassified"]


def control_properties(c):
    props = []
    if is_systemic(c): props.append("systemic")
    if is_translaminar(c): props.append("translaminar")
    if is_contact(c): props.append("contact")
    if is_stomach_poison(c): props.append("stomach_poison")
    if is_protectant(c): props.append("protectant")
    if is_fungistat(c): props.append("fungistat")
    if is_post_harvest(c): props.append("post_harvest")
    if is_selective(c): props.append("selective")
    if is_non_selective(c): props.append("non_selective")
    if is_organic(c): props.append("organic")
    return props or ["no attributes listed"]



st.title("🌱 Avocado Expert System")
st.write("Powered by pyDatalog + Streamlit")

plant = "UserPlant"



# ---------------- DISEASE DIAGNOSTICS ----------------
st.header("Disease Diagnosis")

selected_symptoms = st.multiselect(
    "Select observed symptoms:",
    symptoms
)

if st.button("Analyze Diseases"):
    for s in selected_symptoms:
        +has_symptom(plant, s)

    #Detected Diseases
    st.subheader("Detected Diseases")

    diseases_query = pyDatalog.ask(f"has_disease('{plant}', D)")
    diseases_found = [d[0] for d in diseases_query.answers] if diseases_query else []

    if not diseases_found:
        st.write("No diseases detected.")
    else:
        for disease in diseases_found:
            st.markdown(f"### {disease}")

  
            root_check = pyDatalog.ask(f"root_related_disease('{disease}')")
            fruit_check = pyDatalog.ask(f"fruit_disease('{disease}')")
            if root_check:
                st.write("**Type:** Root-related disease")
            elif fruit_check:
                st.write("**Type:** Fruit-related disease")
            else:
                st.write("**Type:** Other / Unknown")

  
            st.write("**Associated Symptoms:**")
            causes_query = pyDatalog.ask(f"causes('{disease}', C)")
            if causes_query:
                for c in causes_query.answers:
                    st.write(f"- {c[0]}")
            else:
                st.write("- None listed")

    #Likely Diseases
    st.subheader("Likely Diseases (2+ matching symptoms)")

    likely_query = pyDatalog.ask(f"likely_disease('{plant}', D)")
    likely_found = [d[0] for d in likely_query.answers] if likely_query else []

    if likely_found:
        for d in likely_found:
            st.write(f"- {d}")
    else:
        st.write("- None strongly indicated")


#-----------------------Basic Pest Control------------------------------
st.header(" Basic Pest Control")


# Get all pests
all_basic_pests = [p[0] for p in pyDatalog.ask('pest_basic(P)').answers or []]

if not all_basic_pests:
    st.write("No basic pests found in the knowledge base.")
else:
    pest_options = ["Select a pest..."] + all_basic_pests
    selected_pest = st.selectbox("Select a pest:", pest_options)
    if selected_pest != "Select a pest...":
        st.markdown(f"### {selected_pest}")

        # Category
        cat = pyDatalog.ask(f"category_basic('{selected_pest}', C)").answers
        if cat:
            st.write("**Category:**", cat[0][0])
        else:
            st.write("**Category:** Not listed")

        # Controls
        st.write("**Controls:**")
        ctrls = pyDatalog.ask(f"controls_basic(C, '{selected_pest}')").answers
        if ctrls:
            for c in ctrls:
                chem = c[0]

                # Type of chemical
                t = pyDatalog.ask(f"type_basic('{chem}', T)").answers
                type_str = f" ({t[0][0]})" if t else ""

                st.write(f"- {chem}{type_str}")
        else:
            st.write("No controls listed.")



#----------------------Advanced System-------------------------------------
st.subheader("Inspect Pest or Disease Controls")
inspect_target = st.text_input(
    "Enter a pest or disease name to inspect advanced control details:",
    placeholder="e.g. scale_insects or anthracnose"
)

if inspect_target:

    #Pest
    if pest(inspect_target):
        st.markdown(f"## Detailed Controls for Pest: `{inspect_target}`")

        ctrls = controls_pest(Chemical, inspect_target)
        if not ctrls:
            st.write("No controls available.")
        else:
            for row in ctrls:
                c = row[0]
                st.markdown(f"### {c}")

                st.write("**Classification:**",
                         ", ".join(control_classification(c)))

                st.write("**Properties:**",
                         ", ".join(control_properties(c)))

    #Disease
    elif fungal_disease(inspect_target):
        st.markdown(f"## Detailed Controls for Disease: `{inspect_target}`")

        ctrls = controls_disease(Chemical, inspect_target)
        if not ctrls:
            st.write("No controls available.")
        else:
            for row in ctrls:
                c = row[0]
                st.markdown(f"### {c}")

                st.write("**Classification:**",
                         ", ".join(control_classification(c)))

                st.write("**Properties:**",
                         ", ".join(control_properties(c)))

    else:
        st.warning("Target not recognized as a known pest or disease.")
