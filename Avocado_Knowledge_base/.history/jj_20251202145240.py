import streamlit as st
from pyDatalog import pyDatalog

# --- 1. DECLARE TERMS (MUST RUN EVERY TIME) ---
# This ensures Python knows what 'Pest', 'Chemical', etc. are on every rerun.
pyDatalog.create_terms('Pest, Chemical, Disease, Tool, Control, Group, RuleName, Symptom, Plant, S1, S2, D, P, S')
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
pyDatalog.create_terms('sanitation, natural_enemies, cultural_control_mulch')
pyDatalog.create_terms('cultural_control_drainage, cultural_control_gypsum')
pyDatalog.create_terms('cultural_control_pruning, trichogramma, spinosyns')
pyDatalog.create_terms('fungal_disease, causes, has_symptom, has_disease, likely_disease')
pyDatalog.create_terms('root_related_disease, fruit_disease')
pyDatalog.create_terms('pest_basic, pesticide_basic, controls_basic, type_basic, category_basic')
pyDatalog.create_terms('effective_basic, organic_option_basic, fungal_treatment_basic')

# --- 2. INITIALIZE LOGIC (RUN ONCE) ---
if 'kb_initialized' not in st.session_state:
    pyDatalog.clear()
    
    # --- GROUP 16: DISEASES & SYMPTOMS ---
    diseases = [
        "root_rot", "anthracnose", "sunblotch", "verticillium_wilt",
        "scab", "sooty_mold", "avocado_black_streak", "phytophthora_canker",
        "armillaria_root_rot", "dothiorella_fruit_rot", "colletotrichum_gloeosporioides_rot",
        "laurel_wilt", "powdery_mildew", "fusarium_dieback", "algal_leaf_spot",
        "bacterial_spot", "stem_end_rot", "rhizoctonia_root_rot", "fruit_spot",
        "avocado_cercospora", "pink_disease", "branch_canker", "botryosphaeria_canker",
        "black_mold_rot", "sclerotinia_rot", "seed_rot", "avocado_declinine",
        "nutrient_deficiency_chlorosis", "manganese_toxicity", "salt_stress",
        "phytophthora_root_rot", "cercospora_spot"
    ]
    
    # Disease-symptom mapping
    causes_data = {
        "root_rot": ["root_decay", "root_discoloration", "stunted_growth", "foliage_wilt", "leaf_yellowing"],
        "anthracnose": ["fruit_lesions", "fruit_dark_spots", "fruit_soft_rot", "leaf_spots", "fruit_mummification"],
        "sunblotch": ["leaf_mottling", "fruit_discoloration", "bark_cracking", "leaf_distortion"],
        "verticillium_wilt": ["wilting_leaves", "vein_discoloration", "branch_dieback", "leaf_browning"],
        "scab": ["sunken_lesions", "leaf_spots", "fruit_dark_spots", "fruit_cracks"],
        "sooty_mold": ["sooty_coating", "leaf_scorching", "leaf_drop"],
        "avocado_black_streak": ["black_stem_patches", "trunk_bleeding", "bark_cracking", "branch_cracking"],
        "phytophthora_canker": ["stem_canker", "oozing_dark_resin", "canker_on_branches"],
        "phytophthora_root_rot": ["root_decay", "root_discoloration", "trunk_bleeding"],
        "armillaria_root_rot": ["white_mycelium", "root_decay", "stem_drying"],
        "laurel_wilt": ["leaf_necrosis", "vein_discoloration", "foliage_thinning"],
        "powdery_mildew": ["powdery_white_growth", "leaf_curling", "leaf_shedding"],
        "fusarium_dieback": ["stem_pitting", "dead_shoots", "buds_failing", "vascular_discoloration"],
        "cercospora_spot": ["leaf_spots", "leaf_browning"],
    }
    
    for dis, syms in causes_data.items():
        pyDatalog.assert_fact('disease', dis)
        for sym in syms:
            pyDatalog.assert_fact('causes', dis, sym)
    
    # --- FACTS: PESTS ---
    pests = [
        'avocado_thrips', 'boring_beetles', 'ambrosia_beetles',
        'polyphagous_shothole_borer', 'avocado_lace_bug', 'mites',
        'persea_mite', 'avocado_brown_mite', 'sixspotted_mite',
        'caterpillars', 'western_avocado_leafroller', 'omnivorous_looper',
        'scale_insects', 'greenhouse_thrips'
    ]
    for p in pests:
        pyDatalog.assert_fact('pest', p)
    
    # --- FACTS: INSECTICIDES & MITICIDES ---
    insecticides = [
        'abamectin', 'spinetoram', 'spinosad', 'spirotetramat', 'imidacloprid',
        'dinotefuran', 'sabadilla', 'emamectin_benzoate', 'pyrethroids',
        'permethrin', 'bifenthrin', 'malathion', 'fenpropathrin', 'pyrethrin'
    ]
    for insect in insecticides:
        pyDatalog.assert_fact('insecticide', insect)
    
    pyDatalog.assert_fact('miticide', 'spirodiclofen')
    
    # --- FACTS: FUNGICIDES ---
    fungicides = [
        'phosphonates', 'fosetyl_al', 'potassium_phosphite', 'metalaxyl',
        'propiconazole', 'copper', 'azoxystrobin', 'strobilurin', 'prochloraz'
    ]
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
    
    # --- DEFINE RULES ---
    # Note: We do NOT need to assign from pyDatalog.terms here.
    # The variables (Pest, Chemical) are already in scope from Step 1.
    
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

# The rest of your Streamlit UI code goes here...
# You can now use 'pest(Pest)' and 'find_pest_control(Pest, Chemical)' directly.

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