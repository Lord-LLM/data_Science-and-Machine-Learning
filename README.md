
# Avocado Pest and Disease Knowledge Base

This project is an expert system developed using Python, Streamlit, and pyDatalog. It functions as a logic-based decision support tool for avocado cultivation, allowing users to query a knowledge base for pest control methods, disease treatments, and chemical properties.

## Overview

The application uses Logic Programming (Datalog) to infer relationships between specific agricultural problems and their solutions. Unlike standard database lookups, this system uses logical rules to determine if a specific control method is suitable based on criteria such as organic certification, Integrated Pest Management (IPM) suitability, and resistance management groups (IRAC/FRAC).

## Key Features

  * **Pest Control Search:** detailed mapping of pests (e.g., Avocado Thrips, Ambrosia Beetles) to specific chemical and biological controls.
  * **Disease Management:** Identification of treatments for common avocado diseases like Root Rot and Anthracnose.
  * **Category Filtering:** Ability to filter solutions by type, including Organic, Biological, and IPM tools.
  * **Chemical Property Analysis:** detailed lookup for chemical attributes, including:
      * IRAC (Insecticide Resistance Action Committee) Groups.
      * FRAC (Fungicide Resistance Action Committee) Groups.
      * Systemic vs. Contact action.
      * Selectivity and safety profiles.

## Technologies Used

  * **Python 3.x:** Core programming language.
  * **Streamlit:** Web framework for the user interface.
  * **pyDatalog:** Logic programming engine for Python.

## Installation

1.  Clone the repository or download the source code.

2.  Ensure you have Python installed.

3.  Install the required dependencies using pip:

    ```bash
    pip install streamlit pyDatalog
    ```

## Usage

1.  Navigate to the directory containing the script.

2.  Run the application using the Streamlit CLI:

    ```bash
    streamlit run app.py
    ```

    *(Note: Replace `app.py` with the actual filename of your script)*

3.  The application will open in your default web browser.

## Logic Implementation Details

The knowledge base is constructed using pyDatalog terms and predicates. Due to the threading model of Streamlit, the logic engine is re-initialized on every script run to ensure thread safety.

### Logical Predicates

  * **pest(P):** Defines valid pests.
  * **disease(D):** Defines valid diseases.
  * **controls\_pest(Chemical, Pest):** Fact linking a control to a pest.
  * **controls\_disease(Chemical, Disease):** Fact linking a control to a disease.
  * **has\_irac\_group/has\_frac\_group:** Defines resistance management classifications.
