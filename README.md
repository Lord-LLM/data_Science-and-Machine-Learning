#  Gemini Function Calling Example

This repository contains a simple Python script demonstrating **Function Calling** (also known as Tool Use) with the Gemini API via the `google-genai` SDK in a Google Colab environment.

The example shows how the Gemini model can intelligently determine when to call a predefined function (`display_cities`) based on a natural language prompt, and correctly formulate the arguments for that function.

##  Features

  * **Function Calling:** Instructs the Gemini model to utilize a Python function defined in the user's code.
  * **Colab Authentication:** Uses `google.colab.auth` for seamless authentication within a Colaboratory notebook.
  * **Explicit Tool Configuration:** Demonstrates how to configure the generation request to specify which tools (functions) the model can use.
  * **Result Parsing:** Extracts and prints the recommended function name and its arguments from the model's response.

## Prerequisites

1.  **Google Cloud Project:** You must have an active Google Cloud project.
2.  **API Enabled:** Ensure the **Vertex AI API** is enabled in your Google Cloud project.
3.  **Google Colab:** This script is designed to run in a [Google Colab environment](https://colab.research.google.com/).

##  Setup

### 1\. Installation

Install the necessary libraries in your Colab notebook:

```bash
pip install google-genai
```

### 2\. Authentication

The script uses a standard Colab authentication mechanism. When executed in a notebook, it will prompt you to log in to your Google Account.

```python
import google.colab.auth
google.colab.auth.authenticate_user()
```

### 3\. Configure Your Project ID

**Crucially**, you must replace the placeholder `"Project-id"` with your actual Google Cloud Project ID in the script:

```python
# The client setup in the code
client = Client(
    vertexai=True,
    project="YOUR_ACTUAL_PROJECT_ID_HERE", # <--- UPDATE THIS
    location="us-central1"
)
```

##  Code Overview

### 1\. Function Definition

The `display_cities` function is defined with Python type hints and a docstring. The docstring is essential because the Gemini model reads it to understand the function's **purpose** and its **arguments**.

```python
def display_cities(cities: list[str], preferences: Optional[str] = None):
    # ... docstring ...
    return cities
```

### 2\. Gemini Client Initialization

A `Client` is initialized, pointing to the Vertex AI service and specifying your project and region.

### 3\. Generation Request

The `client.models.generate_content` call is the core of the script:

  * **`model`**: Uses the fast `gemini-2.0-flash-001` model.
  * **`contents`**: The user's prompt: `"I'd like to take a ski trip with my family but I'm not sure where to go?"`
  * **`tools`**: The list containing the available function (`display_cities`) is passed here.
  * **`automatic_function_calling`**: Set to `disable=True` to explicitly demonstrate that we are configuring the tool use manually.
  * **`tool_config`**: Forces the model to use the Function Calling feature (`mode='ANY'`), ensuring it returns a function call instead of a natural language response.

### 4\. Output

The model's response is inspected for the recommended function call, and the results are printed:

```
Function Name: display_cities
Function Args: {'preferences': 'ski trip'}
```

The model correctly analyzed the prompt ("ski trip") and mapped it to the `preferences` argument of the `display_cities` function.

##  Next Steps

To execute the actual function call, you would typically take the **Function Name** and **Function Args** from the output, execute the function in your code, and then send the function's result back to the Gemini model to get a final, user-friendly natural language response.
