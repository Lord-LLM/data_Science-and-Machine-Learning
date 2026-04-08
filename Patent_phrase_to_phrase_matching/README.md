US Patent Phrase to Phrase Matching
This notebook demonstrates a solution for the US Patent Phrase to Phrase Matching Kaggle competition. The goal is to determine the degree of semantic similarity between two phrases, given the context of a patent.

Overview
The notebook covers the following steps:

Data Loading and Exploration: Loading the training and test datasets and performing basic exploratory data analysis.
Data Preprocessing: Creating a combined input string for the model and tokenizing the data using a pre-trained tokenizer.
Model Training: Fine-tuning a pre-trained DeBERTa model for sequence classification on the training data.
Prediction and Submission: Making predictions on the test data and generating a submission file in the required format.
Data
The competition provides the following files:

train.csv: Training data with id, anchor, target, context, and score columns.
test.csv: Test data with id, anchor, target, and context columns.
sample_submission.csv: A sample submission file.
Dependencies
The notebook uses the following libraries:

pandas
datasets
transformers
scipy
numpy
kaggle
These libraries are installed within the notebook environment.

Running the Notebook
Clone the repository: If applicable, clone the repository containing this notebook.
Install dependencies: Ensure you have the necessary libraries installed (as listed above). The notebook includes code to install them if running in a Kaggle environment.
Set up Kaggle credentials: If running outside of Kaggle, set up your Kaggle credentials to download the dataset.
Run the cells: Execute the notebook cells sequentially.
Model
The model used is microsoft/deberta-v3-small from the Hugging Face Transformers library, fine-tuned for sequence classification with a single output neuron representing the similarity score.

Training Details
Batch Size: 128
Epochs: 4
Learning Rate: 8e-5
Optimizer: AdamW with weight decay
Learning Rate Scheduler: Cosine with warmup
Evaluation Metric: Pearson correlation coefficient
Results
The model's performance is evaluated using the Pearson correlation coefficient between the predicted scores and the true scores on the test set.

Submission
The notebook generates a submission.csv file with the predicted scores for the test set, which can be submitted to the Kaggle competition.
