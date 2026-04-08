import streamlit as st
from pyDatalog import pyDatalog


pyDatalog.clear()

# 1. DECLARE TERMS 
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

#2. LOAD FACTS (REMOVED SESSION STATE GUARD) 

# GROUP 16: DISEASES & SYMPTOMS 
diseases = [
    "root_rot", "anthracnose", "sunblotch", "verticillium_wilt",
    "scab", "sooty_mold", "avocado_black_streak", "phytophthora_canker",
    "armillaria_root_rot", "laurel_wilt", "powdery_mildew", "fusarium_dieback",
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

# FACTS: PESTS -
pests = [
    'avocado_thrips', 'boring_beetles', 'ambrosia_beetles',
    'polyphagous_shothole_borer', 'avocado_lace_bug', 'mites',
    'persea_mite', 'caterpillars', 'scale_insects'
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

# FACTS: FUNGICIDES -
fungicides = [
    'phosphonates', 'fosetyl_al', 'potassium_phosphite', 'metalaxyl',
    'propiconazole', 'copper', 'azoxystrobin', 'strobilurin', 'prochloraz'
]
for fung in fungicides:
    pyDatalog.assert_fact('fungicide', fung)

#  FACTS: BIOLOGICALS 
natural_sols = ['horticultural_oil', 'insecticidal_soap', 'neem_oil', 'wettable_sulfur']
for sol in natural_sols:
    pyDatalog.assert_fact('natural_solution', sol)

biopests = ['bt', 'beauveria_bassiana']
for bio in biopests:
    pyDatalog.assert_fact('biopesticide', bio)

biocontrols = ['predatory_mites', 'parasitic_wasps', 'generalist_predators']
for bc in biocontrols:
    pyDatalog.assert_fact('biocontrol', bc)

# ASSOCIATIONS: PEST CONTROLS 
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

# ASSOCIATIONS: DISEASE CONTROLS 
disease_controls = [
    ('phosphonates', 'phytophthora_root_rot'), ('metalaxyl', 'phytophthora_root_rot'),
    ('cultural_control_mulch', 'phytophthora_root_rot'),
    ('cultural_control_drainage', 'phytophthora_root_rot'),
    ('cultural_control_gypsum', 'phytophthora_root_rot'),
    ('propiconazole', 'laurel_wilt'), ('sanitation', 'laurel_wilt'),
    ('copper', 'anthracnose'), ('azoxystrobin', 'anthracnose'),
    ('prochloraz', 'anthracnose'), ('cultural_control_pruning', 'anthracnose'),
    ('copper', 'cercospora_spot'), ("root_rot", "favorable_soil_conditions"),
    ("root_rot", "certified_disease_free_nursery_stock"),
    ("root_rot", "resistant_rootstocks"),
    ("root_rot", "prevent_soil_movement"),
    ("root_rot", "irrigation_management"),
    ("root_rot", "mulch"),
    ("root_rot", "gypsum"),
    ("root_rot", "phosphonates"),
    ("root_rot", "fosetyl_al"),
    ("root_rot", "potassium_phosphite"),
    ("root_rot", "metalaxyl"),
    ("sunblotch", "remove_infected_trees"),
    ("sunblotch", "certified_disease_free_stock"),
    ("sunblotch", "disinfect_tools"),
    ("sunblotch", "stump_treatment_with_herbicide"),
    ("sunblotch", "avoid_grafting_from_infected"),
    ("verticillium_wilt", "prune_dead_branches"),
    ("verticillium_wilt", "optimal_irrigation"),
    ("verticillium_wilt", "fertilization"),
    ("verticillium_wilt", "plant_mexican_rootstocks"),
    ("verticillium_wilt", "remove_dead_trees"),
    ("verticillium_wilt", "sterilize_tools"),
    ("verticillium_wilt", "benomyl"),
    ("verticillium_wilt", "azoxystrobin"),
    ("verticillium_wilt", "captan"),
    ("verticillium_wilt", "thiram"),
    ("verticillium_wilt", "carbendazim"),
    ("verticillium_wilt", "trifloxystrobin"),
    ("scab", "copper_fungicide"),
    ("scab", "sulfur"),
    ("scab", "pruning"),
    ("scab", "resistant_varieties"),
    ("scab", "avoid_overhead_irrigation"),
    ("scab", "benomyl"),
    ("scab", "copper_oxychloride"),
    ("scab", "copper_hydroxide"),
    ("scab", "sulfur_plus_copper_sulfate"),
    ("sooty_mold", "control_honeydew_insects"),
    ("sooty_mold", "horticultural_oil"),
    ("sooty_mold", "insecticidal_soap"),
    ("sooty_mold", "neem_oil"),
    ("sooty_mold", "wash_with_detergent"),
    ("sooty_mold", "liquid_copper_fungicide"),
    ("sooty_mold", "selective_insecticides"),
    ("avocado_black_streak", "good_fertilizer"),
    ("avocado_black_streak", "irrigation_practices"),
    ("avocado_black_streak", "prevent_stress"),
    ("avocado_black_streak", "remove_diseased_parts"),
    ("avocado_black_streak", "high_quality_water"),
    ("phytophthora_canker", "favorable_soil_conditions"),
    ("phytophthora_canker", "certified_disease_free_stock"),
    ("phytophthora_canker", "pruning_tools_disinfection"),
    ("phytophthora_canker", "cut_out_infected_tissue"),
    ("phytophthora_canker", "phosphonates"),
    ("phytophthora_canker", "fosetyl_al"),
    ("phytophthora_canker", "potassium_phosphonate"),
    ("phytophthora_canker", "metalaxyl"),
    ("phytophthora_canker", "avoid_wetting_trunks"),
    ("armillaria_root_rot", "good_drainage"),
    ("armillaria_root_rot", "avoid_excess_irrigation"),
    ("armillaria_root_rot", "remove_infected_trees"),
    ("armillaria_root_rot", "remove_stumps"),("armillaria_root_rot", "fumigation"),
    ("armillaria_root_rot", "air_drying_roots"),("armillaria_root_rot", "gypsum"),
    ("armillaria_root_rot", "phosphonates"),
    ("powdery_mildew", "sulfur"),("powdery_mildew", "neem_oil"),
    ("powdery_mildew", "potassium_bicarbonate"),("powdery_mildew", "baking_soda_solution"),
    ("powdery_mildew", "prune_affected_parts"),("powdery_mildew", "avoid_overhead_watering"),
    ("powdery_mildew", "horticultural_oil"),("powdery_mildew", "lime_sulfur"),
    ("fusarium_dieback", "remove_infested_branches"),("fusarium_dieback", "chip_wood_onsite"),
    ("fusarium_dieback", "solarize_branches"),("fusarium_dieback", "sterilize_tools"),
    ("fusarium_dieback", "avoid_moving_infested_material"),("fusarium_dieback", "tebuconazole"),
    ("fusarium_dieback", "carbendazim"),("fusarium_dieback", "debacarb"),
    ("fusarium_dieback", "metconazole"),("fusarium_dieback", "emamectin_benzoate"),
    ("fusarium_dieback", "propiconazole"),("fusarium_dieback", "bifenthrin")
]
for chem, dis in disease_controls:
    pyDatalog.assert_fact('controls_disease', chem, dis)

# ADMINISTRATION INSTRUCTIONS (SIMPLE FOR FARMERS)
admin_instructions = {
    'abamectin': 'Apply as foliar spray: 10-20 fl oz/acre in 100+ gal water. Use ground or air equipment. Repeat every 7-10 days if needed. Wear PPE (gloves, eyewear, coveralls). Avoid bees; apply evenings. Wash hands after use. Store in cool, dry place away from children.',
    'spinetoram': 'Apply 5-10 oz/acre as foliar spray. Target eggs/larvae. Repeat every 7-14 days. Max 2 apps/season. Use with oil if specified. Wear PPE. Apply in calm weather; avoid drift to bees. Store securely.',
    'spinosad': 'Mix 1-2 oz/gal water; spray to wet leaves. Apply every 7-10 days. Safe for organics; max 6 apps/year. Wear PPE. Apply evenings to avoid bees. Wash produce before eating.',
    'spirotetramat': 'Apply 8-10 fl oz/acre foliar in 100+ gal water. Repeat after 14 days if needed. Max 25 oz/year. Wear PPE. Avoid runoff. Store in original container.',
    'imidacloprid': 'Apply 8-16 fl oz/acre as soil drench or foliar. Dilute in 100+ gal water. Max 0.5 lb AI/year. Wear PPE. Avoid bees and water bodies.',
    'dinotefuran': 'Trunk injection: 0.1-0.4 g/tree. Soil drench: 0.2-0.4 lb AI/acre. Consult expert for dosing. Wear PPE. Restricted in some areas; check local regs.',
    'sabadilla': 'Apply as dust or spray: 1-2 lb/acre. Stomach poison; repeat as needed. Wear PPE. Limited data; use cautiously.',
    'emamectin_benzoate': 'Apply 3-6 oz/acre foliar. Mix with water; spray every 7-14 days. Max 2 apps/season. Wear PPE. Apply evenings.',
    'pyrethroids': 'Apply 2-8 oz/acre foliar. Repeat every 7-10 days. Avoid bees; apply evenings. Wear PPE.',
    'permethrin': 'Apply 4-8 oz/acre foliar in 25-400 gal water. Repeat as needed; max per label. Wear PPE.',
    'bifenthrin': 'Apply 0.04-0.2 lb AI/acre foliar in 50+ gal water. Repeat every 7-14 days. Wear PPE. Avoid water bodies.',
    'malathion': 'Apply 1-1.5 pt/acre foliar in 25-400 gal water. Repeat every 7-10 days. Wear PPE.',
    'fenpropathrin': 'Apply 16-21 fl oz/acre in 75+ gal water. Max 2 apps/season. Evening application. Wear PPE. Avoid bees.',
    'pyrethrin': 'Apply 1-4 oz/gal water; spray to wet. Repeat every 5-7 days. Organic option. Wear PPE.',
    'spirodiclofen': 'Apply 18-20 fl oz/acre foliar in 50+ gal water. One app/season. Early infestation. Wear PPE.',
    'phosphonates': 'Apply as soil drench or foliar: 1-3 qt/100 gal. Repeat every 2-4 weeks. Wear PPE.',
    'fosetyl_al': 'Apply 2-5 lb/acre foliar or drench. Repeat every 30-60 days. Buffer for injection. Wear PPE.',
    'potassium_phosphite': 'Apply 2-4 L/ha foliar or injection. Every 4-6 weeks during root flushes. Wear PPE.',
    'metalaxyl': 'Apply 1-4 qt/acre soil drench. Incorporate; repeat 8-12 weeks. Wear PPE.',
    'propiconazole': 'Apply 6-8 fl oz/acre foliar. Repeat every 14-21 days. Max 4 apps/year. Wear PPE.',
    'copper': 'Apply 2-4 lb/acre foliar. Every 7-14 days during wet weather. Wear PPE.',
    'azoxystrobin': 'Apply 6-12 fl oz/acre foliar. Every 14-28 days. Max 3 apps/year. Wear PPE.',
    'strobilurin': 'Apply 0.1-0.25 lb AI/acre. Rotate groups. Every 14-28 days. Wear PPE.',
    'prochloraz': 'Apply 0.2-0.4 lb/acre post-harvest dip or spray. 30-60 sec contact. Wear PPE.',
    'horticultural_oil': 'Mix 1-2% v/v; spray to wet. Every 7-14 days. Avoid hot sun. Wear PPE.',
    'insecticidal_soap': 'Mix 1-2 tbsp/gal; spray undersides. Every 4-7 days. Test first. Wear PPE.',
    'neem_oil': 'Mix 1 tbsp/gal + soap; spray every 7-14 days. Evening application. Wear PPE.',
    'wettable_sulfur': 'Apply 2-30 lb/acre dust or spray. Every 7-10 days. Avoid >90°F. Wear PPE.',
    'bt': 'Apply 0.5-2 lb/acre; spray young larvae. Every 7 days. Wear PPE.',
    'beauveria_bassiana': 'Apply 1-2 lb/acre foliar. Every 7-14 days. Humid conditions. Wear PPE.',
    # Cultural controls (non-chemical)
    'sanitation': 'Remove and destroy infected plant material. Clean tools with bleach (1:10). Do this weekly during outbreaks. No PPE needed, but wear gloves.',
    'cultural_control_mulch': 'Apply 3-4 inches of organic mulch around trees, keeping 6 inches from trunk. Renew annually. Improves soil health; no chemicals.',
    'cultural_control_drainage': 'Improve field drainage by adding channels or raised beds. Avoid overwatering. Check soil weekly.',
    'cultural_control_gypsum': 'Apply 1-2 tons/acre to soil and incorporate. Test soil pH first; repeat every 2 years.',
    'cultural_control_pruning': 'Prune affected branches 6 inches below symptoms. Disinfect tools between cuts. Do in dry weather.',
    'favorable_soil_conditions': 'Ensure well-drained soil with pH 6-7. Test and amend soil before planting.',
    'certified_disease_free_nursery_stock': 'Buy from certified nurseries. Inspect roots before planting.',
    'resistant_rootstocks': 'Use resistant varieties like Dusa or Toro Canyon. Plant in healthy soil.',
    'prevent_soil_movement': 'Clean equipment to avoid spreading soil. Use barriers in fields.',
    'irrigation_management': 'Water deeply but infrequently. Use drip irrigation to avoid wet trunks.',
    'mulch': 'Apply 4-6 inches around base, away from trunk. Renew seasonally.',
    'gypsum': 'Apply 500-1000 lbs/acre for saline soils. Incorporate and water in.',
    'remove_infected_trees': 'Uproot and burn infected trees. Replace with resistant stock.',
    'disinfect_tools': 'Soak tools in 10% bleach for 5 min between uses.',
    'stump_treatment_with_herbicide': 'Apply glyphosate to fresh stumps. Follow label for dosage.',
    'avoid_grafting_from_infected': 'Only graft from healthy trees. Test scions if possible.',
    'prune_dead_branches': 'Cut dead wood back to healthy tissue. Dispose properly.',
    'optimal_irrigation': 'Water 1-2 times/week deeply. Monitor soil moisture.',
    'fertilization': 'Apply balanced NPK fertilizer 3-4 times/year. Soil test first.',
    'plant_mexican_rootstocks': 'Choose Mexican race rootstocks for resistance.',
    'remove_dead_trees': 'Uproot and destroy. Solarize soil if possible.',
    'sterilize_tools': 'Use alcohol or bleach on tools after each cut.',
    'benomyl': 'Apply as foliar spray: 0.5-1 lb/100 gal. Every 14 days. Wear PPE.',
    'captan': 'Apply 2-4 lb/acre foliar. Every 7-14 days. Wear PPE.',
    'thiram': 'Apply as seed treatment or foliar: Follow label. Wear PPE.',
    'carbendazim': 'Apply 0.5-1 g/L foliar. Repeat every 10-14 days. Wear PPE.',
    'trifloxystrobin': 'Apply 2-4 oz/acre. Rotate with other groups. Wear PPE.',
    'copper_fungicide': 'Apply 2-4 lb/acre foliar. Every 7 days in wet weather. Wear PPE.',
    'sulfur': 'Apply as dust: 20-30 lb/acre. Avoid hot days. Wear PPE.',
    'pruning': 'Thin canopy for air flow. Dispose clippings. Do annually.',
    'resistant_varieties': 'Plant scab-resistant like Lamb Hass. Consult nursery.',
    'avoid_overhead_irrigation': 'Use drip systems. Water at base.',
    'copper_oxychloride': 'Apply 2-3 g/L foliar. Every 10-14 days. Wear PPE.',
    'copper_hydroxide': 'Apply 1-2 lb/100 gal. Repeat as needed. Wear PPE.',
    'sulfur_plus_copper_sulfate': 'Mix per label; apply foliar. Wear PPE.',
    'control_honeydew_insects': 'Manage aphids/scale with soaps/oils.',
    'wash_with_detergent': 'Mix mild soap; wash leaves gently. Rinse.',
    'liquid_copper_fungicide': 'Apply diluted per label. Every 7-10 days.',
    'selective_insecticides': 'Use targeted products like imidacloprid sparingly.',
    'good_fertilizer': 'Apply NPK 10-5-20 at 1 lb/tree quarterly.',
    'irrigation_practices': 'Deep water 20-30 gal/tree weekly.',
    'prevent_stress': 'Shade young trees; mulch to retain moisture.',
    'remove_diseased_parts': 'Cut and burn affected streaks.',
    'high_quality_water': 'Use low-salinity water; test regularly.',
    'cut_out_infected_tissue': 'Remove canker with sterile knife; paint wound.',
    'potassium_phosphonate': 'Inject or drench: 1-2 qt/tree. Every 3 months.',
    'avoid_wetting_trunks': 'Use low-angle sprinklers or drip.',
    'good_drainage': 'Plant on mounds; add organic matter.',
    'avoid_excess_irrigation': 'Water only when top 2 inches dry.',
    'remove_infected_trees': 'Uproot and burn. Replace soil if possible.',
    'remove_stumps': 'Dig out and treat with fungicide.',
    'fumigation': 'Use methyl bromide per regulations (restricted).',
    'air_drying_roots': 'Expose roots briefly during replanting.',
    'potassium_bicarbonate': 'Mix 1 tbsp/gal; spray weekly. Organic.',
    'baking_soda_solution': '1 tsp soda + soap/gal; spray every 7 days.',
    'avoid_overhead_watering': 'Water at base to reduce humidity.',
    'lime_sulfur': 'Apply dormant spray: Dilute per label.',
    'remove_infested_branches': 'Prune 12 inches below infestation.',
    'chip_wood_onsite': 'Chip and compost wood away from trees.',
    'solarize_branches': 'Cover piles with plastic for 4-6 weeks in sun.',
    'avoid_moving_infested_material': 'Quarantine affected areas.',
    'tebuconazole': 'Apply 4-8 oz/acre foliar. Every 14 days.',
    'debacarb': 'Apply per label for dieback; foliar spray.',
    'metconazole': 'Apply 3-6 oz/acre. Rotate fungicides.'
}

#  PROPERTIES 
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

# ORGANIC & IPM FACTS 
organic_items = ['spinosad', 'sabadilla', 'pyrethrin', 'horticultural_oil',
                 'wettable_sulfur', 'bt', 'neem_oil', 'insecticidal_soap']
for item in organic_items:
    pyDatalog.assert_fact('is_organic', item)

ipm_tools = ['bt', 'horticultural_oil', 'insecticidal_soap', 'neem_oil',
             'predatory_mites', 'parasitic_wasps', 'beauveria_bassiana']
for tool in ipm_tools:
    pyDatalog.assert_fact('is_ipm_tool', tool)

#  DEFINE RULES (RUN EVERY TIME) 
find_pest_control(Pest, Chemical) <= pest(Pest) & controls_pest(Chemical, Pest)
find_disease_control(Disease, Chemical) <= disease(Disease) & controls_disease(Chemical, Disease)
is_ipm_choice(Tool) <= is_ipm_tool(Tool)
is_biological_or_natural(Control) <= natural_solution(Control)
is_biological_or_natural(Control) <= biopesticide(Control)
is_biological_or_natural(Control) <= biocontrol(Control)
is_organic_control(Control) <= is_organic(Control)
get_irac_group(Chemical, Group) <= has_irac_group(Chemical, Group)
get_frac_group(Chemical, Group) <= has_frac_group(Chemical, Group)

#  STREAMLIT UI 
st.set_page_config(page_title="Avocado Pest KB", page_icon="🥑", layout="wide")
st.title("🥑 Avocado Pest & Disease Knowledge Base")
st.write("An expert system using Datalog to find control methods for avocado cultivation.")

# SECTION 1: PEST CONTROLS
st.header("1. Find Pest Controls")

try:
    # Query all pests to populate the dropdown
    all_pests_query = pest(Pest)
    all_pests_result = all_pests_query.data if hasattr(all_pests_query, 'data') and all_pests_query.data else []
    all_pests = sorted([p[0] for p in all_pests_result])
except Exception as e:
    st.error(f"Error querying pests: {e}")
    all_pests = []

if all_pests:
    selected_pest = st.selectbox("Select a Pest:", options=all_pests, key='pest_select')
    
    try:
        # Query: find_pest_control('specific_pest', Variable)
        # Result format: [('chemical_name',), ('another_chemical',)] -> Only 1 item per tuple!
        pest_controls_query = find_pest_control(selected_pest, Chemical)
        pest_controls_result = pest_controls_query.data if hasattr(pest_controls_query, 'data') and pest_controls_query.data else []
        
        st.write(f"**Controls for {selected_pest.replace('_', ' ').title()}:**")
        if pest_controls_result:
            controls = []
            for c in pest_controls_result:
                chem = c[0]
                instr = admin_instructions.get(chem, "Follow product label and consult a local agricultural expert for safe use.")  # Default if missing
                controls.append({"Control Method": chem.replace('_', ' ').title(), "Instructions": instr})
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
            controls = []
            for c in disease_controls_result:
                chem = c[0]
                instr = admin_instructions.get(chem, "Follow product label and consult a local agricultural expert for safe use.")
                controls.append({"Control Method": chem.replace('_', ' ').title(), "Instructions": instr})
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
        # When querying properties of a KNOWN chemical, the result only contains the property value (Index 0)
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
            #
            st.info(f"🎯 **IRAC Group:** {irac_result[0][0]}")
            props_found = True
        if frac_result:
            # FIX: Use [0][0] instead of [0][1]
            st.info(f"🎯 **FRAC Group:** {frac_result[0][0]}")
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