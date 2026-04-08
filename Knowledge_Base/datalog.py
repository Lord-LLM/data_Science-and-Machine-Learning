from pyDatalog import pyDatalog


pyDatalog.create_terms(
    'Plant, Disease, Symptom, S1, S2, causes, has_symptom, has_disease, likely_disease, '
    'find_pest_control, root_related_disease, fruit_disease, pests, pesticides, '
    
    'pest_basic, pesticide_basic, controls_basic, type_basic, category_basic, '
    'effective_basic, organic_option_basic, fungal_treatment_basic, '
    'query_eff_p, query_eff_s, query_eff_t, query_eff_l, query_eff_f, query_eff_r, '
    'query_org_p, query_org_s, query_org_t, query_org_l, query_org_f, query_org_r, '
    'query_fun_p, query_fun_s, query_fun_t, query_fun_l, query_fun_f, query_fun_r, '
    
    'P, C, G, Plant, Disease, Symptom, S1, S2, P, C, G, D, S, '
    'sanitation, natural_enemies, cultural_control_mulch, cultural_control_drainage, '
    'cultural_control_gypsum, cultural_control_pruning, trichogramma, spinosyns, '
    'Pest, Chemical, Tool, Control, Group, RuleName, pest, fungal_disease, insecticide, '
    'miticide, fungicide, natural_solution, biopesticide, biocontrol, controls_pest, '
    'controls_disease, has_irac_group, has_frac_group, is_systemic, is_translaminar, '
    'is_contact, is_stomach_poison, is_protectant, is_fungistat, is_post_harvest, '
    'is_selective, is_non_selective, application_method, is_organic, is_ipm_tool, '
    'find_disease_control, is_ipm_choice, is_biological_or_natural, is_organic_control, '
    'is_high_resistance_risk, get_irac_group, get_frac_group, resistance_management_strategy, '
    'preferred_application, high_risk_application, is_fungicide_protectant, is_physical_control, '
    'ipm_cultural_rule, resistance_rule, application_rule, fungicide_rule, ipm_rule'
)

def load_kb():
    pyDatalog.clear()
    
    # Variables
    Plant = pyDatalog.Variable()
    S1 = pyDatalog.Variable()
    S2 = pyDatalog.Variable()
    Disease = pyDatalog.Variable()
    Symptom = pyDatalog.Variable()
    P = pyDatalog.Variable()
    C = pyDatalog.Variable()
    G = pyDatalog.Variable()





    #WORK 1: DISEASES & SYMPTOMS

    # Disease list
    diseases = [
        "root_rot", "anthracnose", "sunblotch", "verticillium_wilt",
        "scab", "sooty_mold", "avocado_black_streak", "phytophthora_canker",
        "armillaria_root_rot", "dothiorella_fruit_rot", "colletotrichum_gloeosporioides_rot",
        "laurel_wilt", "powdery_mildew", "fusarium_dieback", "algal_leaf_spot",
        "bacterial_spot", "stem_end_rot", "rhizoctonia_root_rot", "fruit_spot",
        "avocado_cercospora", "pink_disease", "branch_canker", "botryosphaeria_canker",
        "black_mold_rot", "sclerotinia_rot", "seed_rot", "avocado_declinine",
        "nutrient_deficiency_chlorosis", "manganese_toxicity", "salt_stress"
    ]

    # Symptom list
    symptoms = [
        "wilting_leaves", "leaf_yellowing", "leaf_drop", "root_decay",
        "stem_canker", "bark_cracking", "fruit_lesions", "fruit_dark_spots",
        "fruit_soft_rot", "pink_spores", "white_mycelium", "leaf_spots",
        "leaf_browning", "branch_dieback", "trunk_bleeding", "stem_girdling",
        "vein_discoloration", "leaf_distortion", "sunken_lesions", "sooty_coating",
        "powdery_white_growth", "seed_discoloration", "seed_rot_symptom", "black_stem_patches",
        "root_discoloration", "stunted_growth", "fruit_shrinkage", "fruit_premature_drop",
        "leaf_curling", "canker_on_branches", "pitting_on_stem", "rancid_odor_fruit",
        "leaf_scorching", "fruit_cracks", "leaf_chlorosis", "pale_leaf_color",
        "orange_spore_masses", "oozing_dark_resin", "black_mold_growth", "marginal_leaf_burning",
        "branch_cracking", "foliage_thinning", "root_girdling", "water_soaked_lesions",
        "fungal_sclerotia", "fungal_mats", "gall_like_growth", "vascular_discoloration",
        "leaf_shedding", "discolored_bark", "mushy_fruit", "leaf_mottling",
        "fruit_mummification", "leaf_silvering", "fruit_discoloration", "fruit_peeling_easily",
        "root_softening", "dead_shoots", "buds_failing", "stem_pitting",
        "stem_drying", "fruit_sunken_black_spots", "fruit_color_change", "leaf_necrosis",
        "branch_sagging", "fruit_hardening", "salt_crust_on_soil", "leaf_margin_chlorosis",
        "foliage_wilt"
    ]



    # Mapping symptoms 
    causes_data = {
        "root_rot":                      ["root_decay", "root_discoloration", "stunted_growth", "foliage_wilt", "leaf_yellowing"],
        "anthracnose":                   ["fruit_lesions", "fruit_dark_spots", "fruit_soft_rot", "leaf_spots", "fruit_mummification"],
        "sunblotch":                     ["leaf_mottling", "fruit_discoloration", "bark_cracking", "leaf_distortion"],
        "verticillium_wilt":             ["wilting_leaves", "vein_discoloration", "branch_dieback", "leaf_browning"],
        "scab":                          ["sunken_lesions", "leaf_spots", "fruit_dark_spots", "fruit_cracks"],
        "sooty_mold":                    ["sooty_coating", "leaf_scorching", "leaf_drop"],
        "avocado_black_streak":          ["black_stem_patches", "trunk_bleeding", "bark_cracking", "branch_cracking"],
        "phytophthora_canker":           ["stem_canker", "oozing_dark_resin", "canker_on_branches"],
        "armillaria_root_rot":           ["white_mycelium", "root_decay", "stem_drying"],
        "dothiorella_fruit_rot":         ["fruit_dark_spots", "fruit_soft_rot", "rancid_odor_fruit"],
        "laurel_wilt":                   ["leaf_necrosis", "vein_discoloration", "foliage_thinning"],
        "powdery_mildew":                ["powdery_white_growth", "leaf_curling", "leaf_shedding"],
        "fusarium_dieback":              ["stem_pitting", "dead_shoots", "buds_failing", "vascular_discoloration"],
        "algal_leaf_spot":               ["leaf_spots", "orange_spore_masses"],
        "bacterial_spot":                ["water_soaked_lesions", "fruit_spot", "leaf_spots"],
        "stem_end_rot":                  ["fruit_soft_rot", "fruit_peeling_easily"],
        "rhizoctonia_root_rot":          ["root_softening", "leaf_drop"],
        "avocado_cercospora":            ["leaf_spots", "fruit_dark_spots"],
        "pink_disease":                  ["pink_spores", "branch_canker"],
        "branch_canker":                 ["canker_on_branches", "bark_cracking"],
        "botryosphaeria_canker":         ["stem_girdling", "branch_dieback"],
        "black_mold_rot":                ["black_mold_growth", "fruit_sunken_black_spots"],
        "sclerotinia_rot":               ["fungal_sclerotia", "fungal_mats"],
        "seed_rot":                      ["seed_rot_symptom", "seed_discoloration"],
        "nutrient_deficiency_chlorosis": ["leaf_chlorosis", "pale_leaf_color"],
        "manganese_toxicity":            ["leaf_margin_chlorosis"],
        "salt_stress":                   ["marginal_leaf_burning", "salt_crust_on_soil"]
    }

    # Load disease facts
    for disease, syms in causes_data.items():
        for sym in syms:
            +causes(disease, sym)



    # Rule definitions
    has_disease(Plant, Disease) <= (has_symptom(Plant, Symptom) & causes(Disease, Symptom))

    likely_disease(Plant, Disease) <= (
        has_symptom(Plant, S1) &
        has_symptom(Plant, S2) &
        (S1 != S2) &
        causes(Disease, S1) &
        causes(Disease, S2)
    )

    root_related_disease(D) <= (D == "root_rot")
    root_related_disease(D) <= (D == "armillaria_root_rot")
    root_related_disease(D) <= (D == "rhizoctonia_root_rot")

    fruit_disease(D) <= causes(D, "fruit_lesions")
    fruit_disease(D) <= causes(D, "fruit_dark_spots")
    fruit_disease(D) <= causes(D, "fruit_soft_rot")






    # EPOCH 2: BASIC PESTS / PESTICIDES

    # Pests 
    pests = [
        "armoredscale", "thrips", "perseamite",
        "avocadolacebug", "fruitfly", "rootrotphytophthora"
    ]

    for p in pests:
        +pest_basic(p)

    # Pesticides 
    pesticides = [
        "abamectin", "spinosad", "azadirachtin",
        "mineraloil", "copperfungicide",
        "bacillusthuringiensis", "deltamethrin"
    ]

    for p in pesticides:
        +pesticide_basic(p)

    # Controls 
    controls_data = [
        ("abamectin","perseamite"),
        ("mineraloil","armoredscale"),
        ("azadirachtin","armoredscale"),
        ("spinosad","thrips"),
        ("spinosad","fruitfly"),
        ("bacillusthuringiensis","fruitfly"),
        ("copperfungicide","rootrotphytophthora"),
        ("deltamethrin","avocadolacebug")
    ]

    for p, s in controls_data:
        +controls_basic(p, s)

    # Type 
    type_data = [
        ("abamectin","miticide"),
        ("spinosad","organic"),
        ("azadirachtin","organic"),
        ("mineraloil","horticulturaloil"),
        ("copperfungicide","fungicide"),
        ("bacillusthuringiensis","bioinsecticide"),
        ("deltamethrin","pyrethroid")
    ]

    for p, t in type_data:
        +type_basic(p, t)

    # Category 
    category_data = [
        ("perseamite","mite"),
        ("armoredscale","scaleinsect"),
        ("thrips","insect"),
        ("avocadolacebug","insect"),
        ("fruitfly","insect"),
        ("rootrotphytophthora","fungus")
    ]

    for p, c in category_data:
        +category_basic(p, c)

    # Rules 
    effective_basic(P, S) <= controls_basic(P, S)
    organic_option_basic(S, P) <= (controls_basic(P, S) & type_basic(P, "organic"))
    fungal_treatment_basic(S, P) <= (category_basic(S, "fungus") & type_basic(P, "fungicide"))

    # Query predicates 
    query_eff_p(P) <= effective_basic(P, "perseamite")
    query_eff_s(P) <= effective_basic(P, "armoredscale")
    query_eff_t(P) <= effective_basic(P, "thrips")
    query_eff_l(P) <= effective_basic(P, "avocadolacebug")
    query_eff_f(P) <= effective_basic(P, "fruitfly")
    query_eff_r(P) <= effective_basic(P, "rootrotphytophthora")

    query_org_p(P) <= organic_option_basic("perseamite", P)
    query_org_s(P) <= organic_option_basic("armoredscale", P)
    query_org_t(P) <= organic_option_basic("thrips", P)
    query_org_l(P) <= organic_option_basic("avocadolacebug", P)
    query_org_f(P) <= organic_option_basic("fruitfly", P)
    query_org_r(P) <= organic_option_basic("rootrotphytophthora", P)

    query_fun_p(P) <= fungal_treatment_basic("perseamite", P)
    query_fun_s(P) <= fungal_treatment_basic("armoredscale", P)
    query_fun_t(P) <= fungal_treatment_basic("thrips", P)
    query_fun_l(P) <= fungal_treatment_basic("avocadolacebug", P)
    query_fun_f(P) <= fungal_treatment_basic("fruitfly", P)
    query_fun_r(P) <= fungal_treatment_basic("rootrotphytophthora", P)



    # EPOCH 3: ADVANCED PEST / DISEASE / CHEMICAL CONTROL SYSTEM


    # PESTS
    +pest('avocado_thrips')
    +pest('boring_beetles')
    +pest('ambrosia_beetles')
    +pest('polyphagous_shothole_borer')
    +pest('avocado_lace_bug')
    +pest('mites')
    +pest('persea_mite')
    +pest('avocado_brown_mite')
    +pest('sixspotted_mite')
    +pest('caterpillars')
    +pest('western_avocado_leafroller')
    +pest('omnivorous_looper')
    +pest('scale_insects')
    +pest('greenhouse_thrips')
    +pest('armoredscale')
    +pest('thrips')
    +pest('perseamite')
    +pest('fruitfly')
    +pest('rootrotphytophthora')
    



    # DISEASES
    +fungal_disease('phytophthora_root_rot')
    +fungal_disease('laurel_wilt')
    +fungal_disease('anthracnose')
    +fungal_disease('cercospora_spot')
    +fungal_disease('rootrotphytophthora')


    # CHEMICALS — INSECTICIDES & MITICIDES
    +insecticide('abamectin')
    +insecticide('spinetoram')
    +insecticide('spinosad')
    +insecticide('spirotetramat')
    +insecticide('imidacloprid')
    +insecticide('dinotefuran')
    +insecticide('sabadilla')
    +insecticide('emamectin_benzoate')
    +insecticide('pyrethroids')
    +insecticide('permethrin')
    +insecticide('bifenthrin')
    +insecticide('malathion')
    +insecticide('fenpropathrin')
    +insecticide('pyrethrin')
    +insecticide('spinosad')
    +insecticide('deltamethrin')
    +insecticide('azadirachtin')
    +miticide('spirodiclofen')
    +miticide('abamectin')


    # CHEMICALS — FUNGICIDES
    +fungicide('phosphonates')
    +fungicide('fosetyl_al')
    +fungicide('potassium_phosphite')
    +fungicide('metalaxyl')
    +fungicide('propiconazole')
    +fungicide('copper')
    +fungicide('azoxystrobin')
    +fungicide('strobilurin')
    +fungicide('prochloraz')
    +fungicide('copperfungicide')


    # NATURAL SOLUTIONS / BIOCONTROLS
    +natural_solution('horticultural_oil')
    +natural_solution('insecticidal_soap')
    +natural_solution('neem_oil')
    +natural_solution('wettable_sulfur')
    +natural_solution('mineraloil')

    +biopesticide('bt')
    +biopesticide('bacillusthuringiensis')
    +biopesticide('beauveria_bassiana')

    +biocontrol('predatory_mites')
    +biocontrol('parasitic_wasps')
    +biocontrol('generalist_predators')


    # PEST CONTROL FACTS
    +controls_pest('abamectin', 'avocado_thrips')
    +controls_pest('spinetoram', 'avocado_thrips')
    +controls_pest('spinosad', 'avocado_thrips')
    +controls_pest('spirotetramat', 'avocado_thrips')
    +controls_pest('imidacloprid', 'avocado_thrips')
    +controls_pest('dinotefuran', 'avocado_thrips')
    +controls_pest('sabadilla', 'avocado_thrips')

    +controls_pest('emamectin_benzoate', 'boring_beetles')
    +controls_pest('pyrethroids', 'boring_beetles')
    +controls_pest('malathion', 'boring_beetles')
    +controls_pest('fenpropathrin', 'boring_beetles')

    +controls_pest('sanitation', 'polyphagous_shothole_borer')

    +controls_pest('imidacloprid', 'avocado_lace_bug')
    +controls_pest('pyrethrin', 'avocado_lace_bug')
    +controls_pest('neem_oil', 'avocado_lace_bug')
    +controls_pest('deltamethrin', 'avocado_lace_bug')

    +controls_pest('abamectin', 'persea_mite')
    +controls_pest('spirodiclofen', 'persea_mite')

    +controls_pest('horticultural_oil', 'mites')
    +controls_pest('wettable_sulfur', 'mites')
    +controls_pest('predatory_mites', 'mites')

    +controls_pest('bt', 'caterpillars')
    +controls_pest('spinosyns', 'caterpillars')
    +controls_pest('pyrethroids', 'caterpillars')

    +controls_pest('natural_enemies', 'scale_insects')
    +controls_pest('horticultural_oil', 'scale_insects')
    +controls_pest('insecticidal_soap', 'scale_insects')
    +controls_pest('parasitic_wasps', 'scale_insects')

    +controls_pest('beauveria_bassiana', 'ambrosia_beetles')
    +controls_pest('beauveria_bassiana', 'avocado_thrips')

    +controls_pest('trichogramma', 'caterpillars')
    +controls_pest('abamectin', 'perseamite')

    +controls_pest('mineraloil', 'armoredscale')
    +controls_pest('azadirachtin', 'armoredscale')

    +controls_pest('spinosad', 'thrips')
    +controls_pest('spinosad', 'fruitfly')
    +controls_pest('bacillusthuringiensis', 'fruitfly')




    # DISEASE CONTROL FACTS
    +controls_disease('phosphonates', 'phytophthora_root_rot')
    +controls_disease('metalaxyl', 'phytophthora_root_rot')
    +controls_disease('cultural_control_mulch', 'phytophthora_root_rot')
    +controls_disease('cultural_control_drainage', 'phytophthora_root_rot')
    +controls_disease('cultural_control_gypsum', 'phytophthora_root_rot')

    +controls_disease('propiconazole', 'laurel_wilt')
    +controls_disease('sanitation', 'laurel_wilt')

    +controls_disease('copper', 'anthracnose')
    +controls_disease('azoxystrobin', 'anthracnose')
    +controls_disease('prochloraz', 'anthracnose')
    +controls_disease('cultural_control_pruning', 'anthracnose')

    +controls_disease('copper', 'cercospora_spot')

    +controls_disease('copperfungicide', 'rootrotphytophthora')



    # CHEMICAL ATTRIBUTES
    +is_systemic('spirotetramat')
    +is_systemic('imidacloprid')
    +is_systemic('dinotefuran')
    +is_systemic('emamectin_benzoate')
    +is_systemic('phosphonates')
    +is_systemic('propiconazole')

    +is_translaminar('abamectin')
    +is_translaminar('abamectin')

    +is_contact('pyrethroids')
    +is_contact('malathion')
    +is_contact('fenpropathrin')
    +is_contact('spirodiclofen')
    +is_contact('horticultural_oil')
    +is_contact('insecticidal_soap')
    +is_contact('mineraloil')
    +is_contact('deltamethrin')

    +is_stomach_poison('sabadilla')

    +is_protectant('copper')
    +is_protectant('copperfungicide')
    +is_protectant('azoxystrobin')

    +is_fungistat('phosphonates')

    +is_post_harvest('prochloraz')

    +is_selective('bt')

    +is_non_selective('horticultural_oil')

    +application_method('foliar_spray')
    +application_method('aerial_application')
    +application_method('soil_drench')
    +application_method('trunk_injection')

    +is_organic('spinosad')
    +is_organic('sabadilla')
    +is_organic('pyrethrin')
    +is_organic('horticultural_oil')
    +is_organic('wettable_sulfur')
    +is_organic('bt')
    +is_organic('neem_oil')
    +is_organic('insecticidal_soap')
    +is_organic('spinosad')
    +is_organic('azadirachtin')
    +is_organic('mineraloil')
    +is_organic('bacillusthuringiensis')
    pyDatalog.create_terms('C, G')

    # LOGIC RULES
    find_pest_control(Pest, Chemical) <= (
        pest(Pest) & controls_pest(Chemical, Pest)
    )

    find_disease_control(Disease, Chemical) <= (
        fungal_disease(Disease) & controls_disease(Chemical, Disease)
    )

    
    return {
        "symptoms": symptoms,
        "diseases": diseases,
        "has_symptom": has_symptom,
        "has_disease": has_disease,
        "likely_disease": likely_disease,
        "find_pest_control": find_pest_control,
        "D": D,
        "Chemical": Chemical,
        "pests": pests,           
        "pesticides": pesticides,
        "causes": causes,
        "root_related_disease": root_related_disease,
        "fruit_disease": fruit_disease,

        "pest_basic": pest_basic,
        "category_basic": category_basic,
        "controls_basic": controls_basic,
        "type_basic": type_basic,

        "pest": pest,
        "controls_pest": controls_pest,
        "fungal_disease": fungal_disease,
        "controls_disease": controls_disease,
        "insecticide": insecticide,
        "miticide": miticide,
        "fungicide": fungicide,
        "natural_solution": natural_solution,
        "biopesticide": biopesticide,
        "biocontrol": biocontrol,

        "is_systemic": is_systemic,
        "is_translaminar": is_translaminar,
        "is_contact": is_contact,
        "is_stomach_poison": is_stomach_poison,
        "is_protectant": is_protectant,
        "is_fungistat": is_fungistat,
        "is_post_harvest": is_post_harvest,
        "is_selective": is_selective,
        "is_non_selective": is_non_selective,
        "is_organic": is_organic,
        "application_method": application_method,

    }