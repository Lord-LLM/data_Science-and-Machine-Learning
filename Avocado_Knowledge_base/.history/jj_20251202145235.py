

# --- STREAMLIT UI ---
st.set_page_config(page_title="Avocado Pest KB", page_icon="🥑", layout="wide")
st.title("🥑 Avocado Pest & Disease Knowledge Base")
st.write("An expert system using Datalog to find control methods for avocado cultivation.")

# SECTION 1: PEST CONTROLS
st.header("1. Find Pest Controls")

try:
    all_pests_query = pest(Pest)
    all_pests_result = all_pests_query.data if hasattr(all_pests_query, 'data') and all_pests_query.data else []
    all_pests = sorted([p[0] for p in all_pests_result])
except Exception as e:
    st.error(f"Error querying pests: {e}")
    all_pests = []

if all_pests:
    selected_pest = st.selectbox("Select a Pest:", options=all_pests, key='pest_select')
    
    try:
        pest_controls_query = find_pest_control(selected_pest, Chemical)
        pest_controls_result = pest_controls_query.data if hasattr(pest_controls_query, 'data') and pest_controls_query.data else []
        
        st.write(f"**Controls for {selected_pest.replace('_', ' ').title()}:**")
        if pest_controls_result:
            controls = [{"Control Method": c[1].replace('_', ' ').title()} for c in pest_controls_result]
            st.dataframe(controls, use_container_width=True, hide_index=True)
        else:
            st.info("No controls found in the knowledge base.")
    except Exception as e:
        st.error(f"Error finding pest controls: {e}")
else:
    st.warning("No pests loaded in the knowledge base.")

# SECTION 2: DISEASE CONTROLS
st.header("2. Find Disease Controls")

try:
    all_diseases_query = disease(Disease)
    all_diseases_result = all_diseases_query.data if hasattr(all_diseases_query, 'data') and all_diseases_query.data else []
    all_diseases = sorted([d[0] for d in all_diseases_result])
except Exception as e:
    st.error(f"Error querying diseases: {e}")
    all_diseases = []

if all_diseases:
    selected_disease = st.selectbox("Select a Disease:", options=all_diseases, key='disease_select')
    
    try:
        disease_controls_query = find_disease_control(selected_disease, Chemical)
        disease_controls_result = disease_controls_query.data if hasattr(disease_controls_query, 'data') and disease_controls_query.data else []
        
        st.write(f"**Controls for {selected_disease.replace('_', ' ').title()}:**")
        if disease_controls_result:
            controls = [{"Control Method": c[1].replace('_', ' ').title()} for c in disease_controls_result]
            st.dataframe(controls, use_container_width=True, hide_index=True)
        else:
            st.info("No controls found in the knowledge base.")
    except Exception as e:
        st.error(f"Error finding disease controls: {e}")
else:
    st.warning("No diseases loaded in the knowledge base.")

# SECTION 3: CONTROL TYPES
st.header("3. Query by Control Type")
col1, col2, col3 = st.columns(3)

if col1.button("🌱 Organic Controls", key='organic_btn'):
    try:
        organic_query = is_organic_control(Control)
        results = organic_query.data if hasattr(organic_query, 'data') and organic_query.data else []
        if results:
            st.subheader("Organic Controls")
            controls = [{"Control": r[0].replace('_', ' ').title()} for r in results]
            st.dataframe(controls, use_container_width=True, hide_index=True)
        else:
            st.info("No organic controls found.")
    except Exception as e:
        st.error(f"Error querying organic controls: {e}")

if col2.button("🔬 IPM Tools", key='ipm_btn'):
    try:
        ipm_query = is_ipm_choice(Tool)
        results = ipm_query.data if hasattr(ipm_query, 'data') and ipm_query.data else []
        if results:
            st.subheader("IPM Tools")
            tools = [{"Tool": r[0].replace('_', ' ').title()} for r in results]
            st.dataframe(tools, use_container_width=True, hide_index=True)
        else:
            st.info("No IPM tools found.")
    except Exception as e:
        st.error(f"Error querying IPM tools: {e}")

if col3.button("🐛 Bio/Natural Controls", key='bio_btn'):
    try:
        bio_query = is_biological_or_natural(Control)
        results = bio_query.data if hasattr(bio_query, 'data') and bio_query.data else []
        if results:
            st.subheader("Biological & Natural Controls")
            controls = [{"Control": r[0].replace('_', ' ').title()} for r in results]
            st.dataframe(controls, use_container_width=True, hide_index=True)
        else:
            st.info("No biological/natural controls found.")
    except Exception as e:
        st.error(f"Error querying bio/natural controls: {e}")

# SECTION 4: CHEMICAL PROPERTIES
st.header("4. Check Chemical Properties")

try:
    insect_query = insecticide(Chemical)
    fungi_query = fungicide(Chemical)
    insect_result = insect_query.data if hasattr(insect_query, 'data') and insect_query.data else []
    fungi_result = fungi_query.data if hasattr(fungi_query, 'data') and fungi_query.data else []
    all_insecticides = [c[0] for c in insect_result]
    all_fungicides = [f[0] for f in fungi_result]
    all_chemicals = sorted(list(set(all_insecticides + all_fungicides)))
except Exception as e:
    st.error(f"Error querying chemicals: {e}")
    all_chemicals = []

if all_chemicals:
    selected_chemical = st.selectbox("Select a Chemical:", options=all_chemicals, key='chemical_select')
    
    try:
        irac_query = get_irac_group(selected_chemical, Group)
        frac_query = get_frac_group(selected_chemical, Group)
        systemic_query = is_systemic(selected_chemical)
        organic_query = is_organic(selected_chemical)
        
        irac_result = irac_query.data if hasattr(irac_query, 'data') and irac_query.data else []
        frac_result = frac_query.data if hasattr(frac_query, 'data') and frac_query.data else []
        systemic_result = systemic_query.data if hasattr(systemic_query, 'data') and systemic_query.data else []
        organic_result = organic_query.data if hasattr(organic_query, 'data') and organic_query.data else []
        
        st.write(f"**Properties for {selected_chemical.replace('_', ' ').title()}:**")
        props_found = False
        
        if irac_result:
            st.info(f"🎯 **IRAC Group:** {irac_result[0][1]}")
            props_found = True
        if frac_result:
            st.info(f"🎯 **FRAC Group:** {frac_result[0][1]}")
            props_found = True
        if systemic_result:
            st.success("✅ **Systemic:** Yes")
            props_found = True
        if organic_result:
            st.success("🌱 **Organic:** Yes")
            props_found = True
        if not props_found:
            st.write("No specific properties found in KB for this chemical.")
    except Exception as e:
        st.error(f"Error checking chemical properties: {e}")
else:
    st.warning("No chemicals loaded in the knowledge base.")

st.markdown("---")
st.markdown("💡 **Tip:** Rotate between different IRAC/FRAC groups to manage resistance.")
if all_pests and all_diseases and all_chemicals:
    st.markdown("📚 **Knowledge Base Stats:** {} Pests | {} Diseases | {} Chemicals".format(
        len(all_pests), len(all_diseases), len(all_chemicals)
    ))