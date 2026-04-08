import streamlit as st
from pyDatalog import pyDatalog

# Initialize pyDatalog only once using session state
if 'kb_initialized' not in st.session_state:
    pyDatalog.clear()
    
    # Declare variables
    pyDatalog.create_terms('Pest, Chemical, Disease, Tool, Control, Group, RuleName')
    
    # Declare predicates
    pyDatalog.create_terms('pest, disease, insecticide, miticide, fungicide, natural_solution')
    pyDatalog.create_terms('biopesticide, biocontrol, controls_pest, controls_disease, has_irac_group')
    pyDatalog.create_terms('has_frac_group, is_systemic, is_translaminar, is_contact, is_stomach_poison')
    pyDatalog.create_terms('is_protectant, is_fungistat, is_post_harvest, is_selective, is_non_selective')
    pyDatalog.create_terms('application_method, is_organic, is_ipm_tool, find_pest_control')
    pyDatalog.create_terms('find_disease_control, is_ipm_choice, is_biological_or_natural')
    pyDatalog.create_terms('is_organic_control, is_high_resistance_risk, get_irac_group, get_frac_group')
    pyDatalog.create_terms('resistance_management_strategy, preferred_application, high_risk_application')
    pyDatalog.create_terms('is_fungicide_protectant, is_physical_control, ipm_cultural_rule')
    pyDatalog.create_terms('resistance_rule, application_rule, fungicide_rule, ipm_rule')
    
    # --- FACTS: PESTS ---
    pyDatalog.assert_fact('pest', 'avocado_thrips')
    pyDatalog.assert_fact('pest', 'boring_beetles')
    pyDatalog.assert_fact('pest', 'ambrosia_beetles')
    pyDatalog.assert_fact('pest', 'polyphagous_shothole_borer')
    pyDatalog.assert_fact('pest', 'avocado_lace_bug')
    pyDatalog.assert_fact('pest', 'mites')
    pyDatalog.assert_fact('pest', 'persea_mite')
    pyDatalog.assert_fact('pest', 'avocado_brown_mite')
    pyDatalog.assert_fact('pest', 'sixspotted_mite')
    pyDatalog.assert_fact('pest', 'caterpillars')
    pyDatalog.assert_fact('pest', 'western_avocado_leafroller')
    pyDatalog.assert_fact('pest', 'omnivorous_looper')
    pyDatalog.assert_fact('pest', 'scale_insects')
    pyDatalog.assert_fact('pest', 'greenhouse_thrips')
    
    # --- FACTS: DISEASES ---
    pyDatalog.assert_fact('disease', 'phytophthora_root_rot')
    pyDatalog.assert_fact('disease', 'laurel_wilt')
    pyDatalog.assert_fact('disease', 'anthracnose')
    pyDatalog.assert_fact('disease', 'cercospora_spot')
    
    # --- FACTS: INSECTICIDES & MITICIDES ---
    insecticides = ['abamectin', 'spinetoram', 'spinosad', 'spirotetramat', 'imidacloprid',
                    'dinotefuran', 'sabadilla', 'emamectin_benzoate', 'pyrethroids',
                    'permethrin', 'bifenthrin', 'malathion', 'fenpropathrin', 'pyrethrin']
    for insect in insecticides:
        pyDatalog.assert_fact('insecticide', insect)
    
    pyDatalog.assert_fact('miticide', 'spirodiclofen')
    
    # --- FACTS: FUNGICIDES ---
    fungicides = ['phosphonates', 'fosetyl_al', 'potassium_phosphite', 'metalaxyl',
                  'propiconazole', 'copper', 'azoxystrobin', 'strobilurin', 'prochloraz']
    for fung in fungicides:
        pyDatalog.assert_fact('fungicide', fung)
    
    # --- FACTS: BIOLOGICALS ---
    natural_sols = ['horticultural_oil', 'insecticidal_soap', 'neem_oil', 'wettable_sulfur']
    for sol in natural_sols:
        pyDatalog.assert_fact('natural_solution', sol)
    
    biopests = ['bt', 'beauveria_bassiana']
    for bio in biopests:
        pyDatalog.assert_fact('biopesticide', bio)
    
    biocontrols = ['predatory_mites', 'parasitic_wasps', 'generalist_predators']
    for bc in biocontrols:
        pyDatalog.assert_fact('biocontrol', bc)
    
    # --- ASSOCIATIONS: PEST CONTROLS ---
    pest_controls = [
        ('abamectin', 'avocado_thrips'), ('spinetoram', 'avocado_thrips'),
        ('spinosad', 'avocado_thrips'), ('spirotetramat', 'avocado_thrips'),
        ('imidacloprid', 'avocado_thrips'), ('dinotefuran', 'avocado_thrips'),
        ('sabadilla', 'avocado_thrips'), ('emamectin_benzoate', 'boring_beetles'),
        ('pyrethroids', 'boring_beetles'), ('malathion', 'boring_beetles'),
        ('fenpropathrin', 'boring_beetles'), ('sanitation', 'polyphagous_shothole_borer'),
        ('imidacloprid', 'avocado_lace_bug'), ('pyrethrin', 'avocado_lace_bug'),
        ('neem_oil', 'avocado_lace_bug'), ('abamectin', 'persea_mite'),
        ('spirodiclofen', 'persea_mite'), ('horticultural_oil', 'mites'),
        ('wettable_sulfur', 'mites'), ('predatory_mites', 'mites'),
        ('bt', 'caterpillars'), ('spinosyns', 'caterpillars'),
        ('pyrethroids', 'caterpillars'), ('natural_enemies', 'scale_insects'),
        ('horticultural_oil', 'scale_insects'), ('insecticidal_soap', 'scale_insects'),
        ('parasitic_wasps', 'scale_insects'), ('beauveria_bassiana', 'ambrosia_beetles'),
        ('beauveria_bassiana', 'avocado_thrips'), ('trichogramma', 'caterpillars')
    ]
    for chem, pest_name in pest_controls:
        pyDatalog.assert_fact('controls_pest', chem, pest_name)
    
    # --- ASSOCIATIONS: DISEASE CONTROLS ---
    disease_controls = [
        ('phosphonates', 'phytophthora_root_rot'), ('metalaxyl', 'phytophthora_root_rot'),
        ('cultural_control_mulch', 'phytophthora_root_rot'),
        ('cultural_control_drainage', 'phytophthora_root_rot'),
        ('cultural_control_gypsum', 'phytophthora_root_rot'),
        ('propiconazole', 'laurel_wilt'), ('sanitation', 'laurel_wilt'),
        ('copper', 'anthracnose'), ('azoxystrobin', 'anthracnose'),
        ('prochloraz', 'anthracnose'), ('cultural_control_pruning', 'anthracnose'),
        ('copper', 'cercospora_spot')
    ]
    for chem, dis in disease_controls:
        pyDatalog.assert_fact('controls_disease', chem, dis)
    
    # --- PROPERTIES ---
    irac_groups = [
        ('abamectin', '6'), ('emamectin_benzoate', '6'), ('spinosad', '5'),
        ('spinetoram', '5'), ('spirotetramat', '23'), ('spirodiclofen', '23'),
        ('imidacloprid', '4A'), ('dinotefuran', '4A'), ('pyrethroids', '3A'),
        ('permethrin', '3A'), ('bifenthrin', '3A'), ('fenpropathrin', '3A'),
        ('pyrethrin', '3A'), ('malathion', '1B'), ('bt', '11A'), ('sabadilla', 'UN')
    ]
    for chem, group in irac_groups:
        pyDatalog.assert_fact('has_irac_group', chem, group)
    
    frac_groups = [
        ('phosphonates', 'P07'), ('metalaxyl', '4'), ('propiconazole', '3'),
        ('prochloraz', '3'), ('copper', 'M01'), ('azoxystrobin', '11'),
        ('strobilurin', '11')
    ]
    for chem, group in frac_groups:
        pyDatalog.assert_fact('has_frac_group', chem, group)
    
    # Chemical properties
    systemic_chems = ['spirotetramat', 'imidacloprid', 'dinotefuran', 
                      'emamectin_benzoate', 'phosphonates', 'propiconazole']
    for chem in systemic_chems:
        pyDatalog.assert_fact('is_systemic', chem)
    
    pyDatalog.assert_fact('is_translaminar', 'abamectin')
    
    contact_chems = ['pyrethroids', 'malathion', 'fenpropathrin', 'spirodiclofen',
                     'horticultural_oil', 'insecticidal_soap']
    for chem in contact_chems:
        pyDatalog.assert_fact('is_contact', chem)
    
    pyDatalog.assert_fact('is_stomach_poison', 'sabadilla')
    pyDatalog.assert_fact('is_protectant', 'copper')
    pyDatalog.assert_fact('is_protectant', 'azoxystrobin')
    pyDatalog.assert_fact('is_fungistat', 'phosphonates')
    pyDatalog.assert_fact('is_post_harvest', 'prochloraz')
    pyDatalog.assert_fact('is_selective', 'bt')
    pyDatalog.assert_fact('is_non_selective', 'horticultural_oil')
    
    # --- ORGANIC & IPM FACTS ---
    organic_items = ['spinosad', 'sabadilla', 'pyrethrin', 'horticultural_oil',
                     'wettable_sulfur', 'bt', 'neem_oil', 'insecticidal_soap']
    for item in organic_items:
        pyDatalog.assert_fact('is_organic', item)
    
    ipm_tools = ['bt', 'horticultural_oil', 'insecticidal_soap', 'neem_oil',
                 'predatory_mites', 'parasitic_wasps', 'beauveria_bassiana']
    for tool in ipm_tools:
        pyDatalog.assert_fact('is_ipm_tool', tool)
    
    # --- RULES ---
    find_pest_control(Pest, Chemical) <= pest(Pest) & controls_pest(Chemical, Pest)
    find_disease_control(Disease, Chemical) <= disease(Disease) & controls_disease(Chemical, Disease)
    is_ipm_choice(Tool) <= is_ipm_tool(Tool)
    is_biological_or_natural(Control) <= natural_solution(Control)
    is_biological_or_natural(Control) <= biopesticide(Control)
    is_biological_or_natural(Control) <= biocontrol(Control)
    is_organic_control(Control) <= is_organic(Control)
    get_irac_group(Chemical, Group) <= has_irac_group(Chemical, Group)
    get_frac_group(Chemical, Group) <= has_frac_group(Chemical, Group)
    
    st.session_state.kb_initialized = True

# --- STREAMLIT UI ---
st.set_page_config(page_title="Avocado Pest KB", page_icon="🥑", layout="wide")
st.title("🥑 Avocado Pest & Disease Knowledge Base")
st.write("An expert system using Datalog to find control methods for avocado cultivation.")

# SECTION 1: PEST CONTROLS
st.header("1. Find Pest Controls")

# Query all pests
try:
    all_pests_query = pest(Pest)
    all_pests_result = all_pests_query.data if all_pests_query.data else []
    all_pests = sorted([p[0] for p in all_pests_result])
except Exception as e:
    st.error(f"Error querying pests: {e}")
    all_pests = []

if all_pests:
    selected_pest = st.selectbox("Select a Pest:", options=all_pests)
    
    # Run Query
    try:
        pest_controls_query = find_pest_control(selected_pest, Chemical)
        pest_controls_result = pest_controls_query.data if pest_controls_query.data else []
        
        st.write(f"**Controls for {selected_pest.replace('_', ' ').title()}:**")
        if pest_controls_result:
            controls = [{"Control Method": c[1].replace('_', ' ').title()} for c in pest_controls_result]
            st.dataframe(controls, use_container_width=True, hide_index=True)
        else:
            st.info("No controls found in the knowledge base.")
    except Exception as e:
        st.error(f"Error finding pest controls: {e}")

# SECTION 2: DISEASE CONTROLS
st.header("2. Find Disease Controls")

try:
    all_diseases_query = disease(Disease)
    all_diseases_result = all_diseases_query.data if all_diseases_query.data else []
    all_diseases = sorted([d[0] for d in all_diseases_result])
except Exception as e:
    st.error(f"Error querying diseases: {e}")
    all_diseases = []

if all_diseases:
    selected_disease = st.selectbox("Select a Disease:", options=all_diseases)
    
    try:
        disease_controls_query = find_disease_control(selected_disease, Chemical)
        disease_controls_result = disease_controls_query.data if disease_controls_query.data else []
        
        st.write(f"**Controls for {selected_disease.replace('_', ' ').title()}:**")
        if disease_controls_result:
            controls = [{"Control Method": c[1].replace('_', ' ').title()} for c in disease_controls_result]
            st.dataframe(controls, use_container_width=True, hide_index=True)
        else:
            st.info("No controls found in the knowledge base.")
    except Exception as e:
        st.error(f"Error finding disease controls: {e}")

# SECTION 3: CONTROL TYPES
st.header("3. Query by Control Type")
col1, col2, col3 = st.columns(3)

if col1.button("🌱 Organic Controls"):
    try:
        organic_query = is_organic_control(Control)
        results = organic_query.data if organic_query.data else []
        if results:
            st.subheader("Organic Controls")
            controls = [{"Control": r[0].replace('_', ' ').title()} for r in results]
            st.dataframe(controls, use_container_width=True, hide_index=True)
        else:
            st.info("No organic controls found.")
    except Exception as e:
        st.error(f"Error querying organic controls: {e}")

if col2.button("🔬 IPM Tools"):
    try:
        ipm_query = is_ipm_choice(Tool)
        results = ipm_query.data if ipm_query.data else []
        if results:
            st.subheader("IPM Tools")
            tools = [{"Tool": r[0].replace('_', ' ').title()} for r in results]
            st.dataframe(tools, use_container_width=True, hide_index=True)
        else:
            st.info("No IPM tools found.")
    except Exception as e:
        st.error(f"Error querying IPM tools: {e}")

if col3.button("🐛 Bio/Natural Controls"):
    try:
        bio_query = is_biological_or_natural(Control)
        results = bio_query.data if bio_query.data else []
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

# Combine lists for dropdown
try:
    insect_query = insecticide(Chemical)
    fungi_query = fungicide(Chemical)
    insect_result = insect_query.data if insect_query.data else []
    fungi_result = fungi_query.data if fungi_query.data else []
    all_insecticides = [c[0] for c in insect_result]
    all_fungicides = [f[0] for f in fungi_result]
    all_chemicals = sorted(list(set(all_insecticides + all_fungicides)))
except Exception as e:
    st.error(f"Error querying chemicals: {e}")
    all_chemicals = []

if all_chemicals:
    selected_chemical = st.selectbox("Select a Chemical:", options=all_chemicals)
    
    try:
        # Check properties
        irac_query = get_irac_group(selected_chemical, Group)
        frac_query = get_frac_group(selected_chemical, Group)
        systemic_query = is_systemic(selected_chemical)
        organic_query = is_organic(selected_chemical)
        
        irac_result = irac_query.data if irac_query.data else []
        frac_result = frac_query.data if frac_query.data else []
        systemic_result = systemic_query.data if systemic_query.data else []
        organic_result = organic_query.data if organic_query.data else []
        
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

st.markdown("---")
st.markdown("💡 **Tip:** Rotate between different IRAC/FRAC groups to manage resistance.")
st.markdown("📚 **Knowledge Base Stats:** {} Pests | {} Diseases | {} Chemicals".format(
    len(all_pests) if all_pests else 0,
    len(all_diseases) if all_diseases else 0,
    len(all_chemicals) if all_chemicals else 0
))