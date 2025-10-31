#  Neural Network from Scratch: Titanic Survival Prediction

This Jupyter notebook demonstrates how to build and train a machine learning model, starting with simple **Logistic Regression** and progressing to a basic **Deep Neural Network**, using only core PyTorch functions without relying on higher-level modules like `torch.nn`. The model is trained on the classic Titanic dataset to predict passenger survival.

---

##  Setup and Data Cleaning

### 1. Environment and Imports

The notebook imports essential libraries for data science and deep learning:
* **`torch`**, **`numpy`**, **`pandas`** for data handling and computation.
* **`fastai.data.transforms`** for data splitting.

### 2. Data Loading & Cleaning
* Loads the `train.csv` file from the Titanic competition dataset.
* **Handles Missing Values:** Missing values in the DataFrame are filled using the **mode** of each column.

### 3. Feature Engineering & Preprocessing
* **Feature Dominance Fix:** The `Fare` column, which has a wide distribution, is stabilized using a **log transformation** (`LogFare = log(Fare + 1)`) to prevent it from dominating the model's training process.
* **One-Hot Encoding:** Categorical features like `Sex`, `Pclass`, and `Embarked` are converted into numerical columns using **one-hot encoding** (`pd.get_dummies()`).
* **Normalization:** The continuous features (`Age`, `SibSp`, `Parch`, `LogFare`) are **normalized** by dividing each column by its maximum value, ensuring all features are scaled between 0 and 1.
* The final features are combined into a PyTorch tensor, **`t_indep`**, and the target variable, `Survived`, becomes **`t_dep`**.

---

## Model Building and Training

The core of the notebook implements essential machine learning functions from the ground up.

### Key Functions Implemented

| Function | Purpose |
| :--- | :--- |
| `calc_preds(coeffs, indeps)` | **Prediction (Forward Pass):** Calculates the model's output. It performs the linear layer, then applies the **Sigmoid function** to transform the output into a probability between $0$ and $1$. |
| `calc_loss(coeffs, indeps, deps)` | **Loss Calculation:** Uses the **Mean Absolute Error (MAE)**, $\sum | \text{preds} - \text{targets} | / N$, as the loss function to measure prediction accuracy. |
| `update_coeffs(coeffs, lr)` | **Gradient Descent:** Adjusts the model's parameters (`coeffs`) based on the calculated gradients and the learning rate (`lr`). It also calls `coeffs.grad.zero_()` to reset gradients. |
| `one_epoch(coeffs, lr)` | **Single Training Iteration:** Runs one full pass over the training data, performing the forward pass, backpropagation (`loss.backward()`), and parameter update. |
| `train_model(epochs, lr)` | **Training Loop:** Initializes coefficients and iterates through the `one_epoch` function for a specified number of epochs. |

### 1. Initial Simple Model (Logistic Regression)
The model starts with simple **linear layer** followed by **Sigmoid activation** to perform logistic regression.

* **Prediction:** $P(\text{Survived}) = \sigma(\text{Features} \cdot \text{Coefficients})$
* The model achieves an initial validation **accuracy of approximately $82.58\%$**.

### 2. Deep Neural Network
The structure is extended to a two-layer (one hidden layer) neural network to improve predictive power:
* **Layer 1:** Input $\rightarrow$ Linear Transformation $\rightarrow$ **ReLU Activation**
    * `res = F.relu(indeps@l1)`
* **Layer 2:** Hidden Layer $\rightarrow$ Linear Transformation $\rightarrow$ **Sigmoid Activation**
    * `res = res@l2 + const`
    * `return torch.sigmoid(res)`

This network uses the **ReLU (Rectified Linear Unit)** activation for the hidden layer and **Sigmoid** for the final output (for binary classification probability). The final deep learning model also achieves a validation **accuracy of approximately $82.58\%$**, demonstrating that even on a small dataset like Titanic, complex models may not dramatically outperform well-tuned linear models.

---

## 🔬 Model Evaluation

The model's performance is measured using:
* **Loss:** Monitored during training to ensure it is consistently decreasing.
* **Accuracy:** Calculated on the **validation set** by comparing the predicted probability (using a threshold of $0.5$) to the true survival target.

$$\text{Accuracy} = \frac{\text{Number of correct predictions}}{\text{Total number of predictions}}$$

The function `acc(coeffs)` is defined to easily calculate this metric on the validation set.
