# Linear Regression from Scratch – Auto MPG Dataset  

## Inspiration  

This project is inspired by **Andrew Ng’s Machine Learning Specialization**, where the emphasis is on understanding machine learning fundamentals by building algorithms from the ground up instead of relying on high-level libraries like scikit-learn.  

The goal is to **implement Linear Regression from scratch** using only `numpy` and `pandas`, while handling all key ML steps manually: preprocessing, feature scaling, feature engineering, cost function design, optimization, and evaluation.  

---

##  Features of This Project  

### Custom Preprocessing  
- Manual handling of missing values (e.g., horsepower column).  
- Feature scaling (standardization).  
- Encoding categorical variables (origin, car names).  

### Custom Implementation (No sklearn for model)  
- Linear Regression implemented with Gradient Descent.  
- Support for **learning rate tuning**.  
- Support for **L2 Regularization (Ridge)**.  
- Mean Squared Error (MSE) as custom loss function.  

### Exploratory Data Analysis (EDA)  
- Visualizations to uncover trends, multicollinearity, and relationships.  
- Correlation heatmaps and scatter plots to detect issues.  

### Experimentation  
- Manual fine-tuning of hyperparameters like learning rate and regularization strength.  
- Training/testing split and performance comparison.  

---

## Dataset – Auto MPG  

The dataset contains information about fuel consumption and car features such as cylinders, displacement, horsepower, weight, acceleration, model year, origin, and car name.  

- **Target**: `mpg` (miles per gallon)  
- **Features**: All other numerical/categorical attributes  

---

## Key Learnings  
- Building ML algorithms step-by-step builds intuition.  
- Preprocessing is as important as modeling.  
- Custom loss and optimization loops provide insight into how ML frameworks (like sklearn) actually work.  
- Feature scaling, encoding, and handling missing values directly affect convergence and performance.  

---

## Acknowledgements  
- Inspired by **Andrew Ng’s Machine Learning Specialization**.  
- Dataset: [UCI Auto MPG dataset](https://archive.ics.uci.edu/ml/datasets/auto+mpg).  
