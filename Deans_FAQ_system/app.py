# app.py

import streamlit as st
from dean_data import KNOWLEDGE_BASE, TOTAL_FAQS, CATEGORIES
from dean_logic import process_query

st.set_page_config(page_title="Dean's Office FAQ", page_icon="📘", layout="centered")

st.title("Dean's Office FAQ System")
st.caption("Type your question and get the best matching answer. Powered by your Isabelle logic, ported to Python.")

# Sidebar: filters and info
with st.sidebar:
    st.header("Filters")
    category = st.selectbox("Category (optional)", options=["All"] + CATEGORIES, index=0)
    st.markdown("---")
    st.metric(label="Total FAQs", value=TOTAL_FAQS)
    st.markdown("Use categories to narrow results.")

# Main query input
query = st.text_input("Ask a question", placeholder="e.g., GPA requirement to graduate, how to get a transcript, registration dates")

if st.button("Search"):
    cat_filter = None if category == "All" else category
    answer, best = process_query(query, category_filter=cat_filter)

    # Show result
    if best:
        st.subheader("Best match")
        st.write(f"• Category: {best.cat}")
        st.write(f"• Question: {best.question}")
        st.success(answer)
    else:
        st.warning(answer)

# Expandable list of all FAQs
with st.expander("Browse all FAQs"):
    for f in KNOWLEDGE_BASE:
        st.markdown(f"**Category:** {f.cat}")
        st.markdown(f"**Question:** {f.question}")
        st.markdown(f"**Answer:** {f.answer}")
        st.markdown(f"**Keywords:** {', '.join(f.keywords)}")
        st.markdown("---")