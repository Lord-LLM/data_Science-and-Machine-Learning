#  Custom Logistic Regression on Employee Attrition

This project implements **Logistic Regression from scratch ** and applies it to the **IBM HR Analytics Employee Attrition Dataset**.  
The goal is to predict whether an employee is likely to leave the company (**Attrition: Yes/No**).

---

##  Dataset
- **Source**: [IBM HR Analytics Employee Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
- **Target**: `Attrition` (1 = Yes, 0 = No)  
- **Features**: Age, JobRole, MonthlyIncome, YearsAtCompany, Overtime, JobSatisfaction, etc.  

---

## Project Workflow
1. Load and explore dataset  
2. Preprocess data  
   - One-hot encode categorical variables  
   - Scale numerical features  
   - Encode target (Yes → 1, No → 0)  
3. Implement Logistic Regression from scratch  
   - Sigmoid function  
   - Binary cross-entropy loss  
   - Gradient descent  
   - Training loop with loss tracking  
4. Evaluate model  
   - Accuracy, Precision, Recall, F1  
   - Confusion Matrix  
   - Training loss curve  

---
