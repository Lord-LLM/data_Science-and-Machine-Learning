# # faq_logic.py

# import re
# from typing import List, Optional, Tuple
# from dean_data import FAQEntry, KNOWLEDGE_BASE, SYNONYMS

# # Lowercase (ASCII-focused)
# def to_lowercase(s: str) -> str:
#     return s.lower()

# # Tokenize: split on non-alphanumeric, keep only non-empty tokens, lowercase
# def tokenize(s: str) -> List[str]:
#     tokens = re.split(r"[^A-Za-z0-9]+", s)
#     tokens = [to_lowercase(t) for t in tokens if t]
#     return tokens

# def get_synonyms(keyword: str) -> List[str]:
#     return SYNONYMS.get(keyword, [])

# # Score logic (replicates your Isabelle design)
# # - exact keyword hit: 3
# # - synonym hit: 2
# # - substring match: 1 (token in keyword or keyword in token)
# # - question similarity: +1 per common token
# def keyword_hit_score(tok: str, kw: str) -> int:
#     if tok == kw:
#         return 3
#     if tok in get_synonyms(kw):
#         return 2
#     if kw in tok or tok in kw:  # simple substring check
#         return 1
#     return 0

# def score_entry(f: FAQEntry, toks: List[str]) -> int:
#     ks = [to_lowercase(k) for k in f.keywords]
#     keyword_scores = 0
#     for kw in ks:
#         for tok in toks:
#             keyword_scores += keyword_hit_score(tok, kw)

#     q_tokens = tokenize(f.question)
#     common = sum(1 for t in q_tokens if t in toks)
#     return keyword_scores + common

# def find_best(faqs: List[FAQEntry], toks: List[str]) -> Optional[FAQEntry]:
#     best: Optional[FAQEntry] = None
#     best_score = -1
#     for f in faqs:
#         sc = score_entry(f, toks)
#         if sc > best_score:
#             best = f
#             best_score = sc
#     return best

# def process_query(q: str, category_filter: Optional[str] = None) -> Tuple[str, Optional[FAQEntry]]:
#     toks = tokenize(q)
#     candidates = [f for f in KNOWLEDGE_BASE if (category_filter is None or f.cat == category_filter)]
#     best = find_best(candidates, toks)
#     if best is None:
#         return "I'm sorry — I could not find a matching answer. Please rephrase your question or contact the Dean's office.", None
#     return best.answer, best

# faq_logic.py

import re
from typing import List, Optional, Tuple
from dean_data import FAQEntry, KNOWLEDGE_BASE, SYNONYMS

# -------------------------
# Helper: lowercase + tokenize
# -------------------------

def to_lowercase(s: str) -> str:
    """Convert string to lowercase (ASCII only)."""
    return s.lower()

def tokenize(s: str) -> List[str]:
    """
    Split a string into tokens:
    - split on non-alphanumeric characters
    - lowercase each token
    - ignore empty tokens
    """
    tokens = re.split(r"[^A-Za-z0-9]+", s)
    return [to_lowercase(t) for t in tokens if t]

# -------------------------
# Synonym lookup
# -------------------------

def get_synonyms(keyword: str) -> List[str]:
    """Return synonyms for a keyword (lowercased)."""
    return SYNONYMS.get(keyword, [])

# -------------------------
# Matching primitives
# -------------------------

def keyword_hit_score(tok: str, kw: str) -> int:
    """
    Compute score for a token against a keyword:
    - exact keyword hit: 3 points
    - synonym hit: 2 points
    - substring match: 1 point
    - otherwise: 0
    """
    if tok == kw:
        return 3
    if tok in get_synonyms(kw):
        return 2
    if kw in tok or tok in kw:
        return 1
    return 0

def score_entry(f: FAQEntry, toks: List[str]) -> int:
    """
    Compute score for an FAQ entry given tokenized query:
    - sum of keyword hit scores
    - plus number of common tokens with the FAQ question
    """
    ks = [to_lowercase(k) for k in f.keywords]
    keyword_scores = 0
    for kw in ks:
        for tok in toks:
            keyword_scores += keyword_hit_score(tok, kw)

    q_tokens = tokenize(f.question)
    common = sum(1 for t in q_tokens if t in toks)

    return keyword_scores + common

def find_best(faqs: List[FAQEntry], toks: List[str]) -> Optional[FAQEntry]:
    """Find the FAQ entry with the highest score (ties → first encountered)."""
    best: Optional[FAQEntry] = None
    best_score = -1
    for f in faqs:
        sc = score_entry(f, toks)
        if sc > best_score:
            best = f
            best_score = sc
    return best

# -------------------------
# Public query function
# -------------------------

def process_query(q: str, category_filter: Optional[str] = None) -> Tuple[str, Optional[FAQEntry]]:
    """
    Public query function:
    - preprocess query: lowercase + tokenize
    - find best FAQ entry by score
    - optional category filter
    """
    toks = tokenize(q)
    candidates = [f for f in KNOWLEDGE_BASE if (category_filter is None or f.cat == category_filter)]
    best = find_best(candidates, toks)
    if best is None:
        return "I'm sorry — I could not find a matching answer. Please rephrase your question or contact the Dean's office.", None
    return best.answer, best

# -------------------------
# Utilities
# -------------------------

def get_all_questions() -> List[str]:
    """Return all FAQ questions."""
    return [f.question for f in KNOWLEDGE_BASE]

def total_faqs() -> int:
    """Return total number of FAQs."""
    return len(KNOWLEDGE_BASE)
