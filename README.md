# 🩺 Diabetes Prediction Using Machine Learning

A Machine Learning-based web application that predicts whether a person is likely to have diabetes based on important health and medical parameters.

The project uses a trained Machine Learning model with **Python, Scikit-learn, Pandas, and Streamlit** and provides an interactive interface where users can enter their health information and receive a prediction.

> **Disclaimer:** This project is intended for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used as a substitute for professional medical advice.

---

## 🚀 Project Overview

Diabetes is a common chronic disease that can be influenced by several health-related factors. This project demonstrates how Machine Learning can be used for a **binary classification problem** to predict diabetes based on patient-related features.

The trained model is saved as `model.pkl`, while `scaler.pkl` is used for feature scaling. The Streamlit application loads these files and generates a prediction from the user's input.

---

## ✨ Features

* 🩺 Diabetes prediction using Machine Learning
* 📊 Interactive Streamlit web interface
* 🤖 Pre-trained Machine Learning model
* 📏 Feature scaling using a saved scaler
* 👤 User input for multiple health parameters
* ⚡ Instant prediction
* 🧠 BMI and age-group feature handling
* 📓 Model training notebook included

---

## 🛠️ Technologies Used

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| Python           | Programming language                  |
| Pandas           | Data manipulation                     |
| Scikit-learn     | Machine Learning                      |
| Streamlit        | Web application                       |
| Pickle           | Model serialization                   |
| Jupyter Notebook | Model development and experimentation |

---

## 📋 Input Features

The application accepts the following parameters:

* **Pregnancies**
* **Glucose**
* **Blood Pressure**
* **Skin Thickness**
* **Insulin**
* **BMI**
* **Diabetes Pedigree Function**
* **Age**

The application also derives additional features such as:

* BMI category
* Age groups

These features are prepared before being passed to the trained model.

---

## 🔄 Machine Learning Workflow

```text
User Input
    ↓
Data Preprocessing
    ↓
Feature Engineering
    ↓
Feature Scaling
    ↓
Trained ML Model
    ↓
Prediction
    ↓
Diabetic / Not Diabetic
```

### Model Pipeline

1. Load and explore the dataset
2. Perform data preprocessing
3. Perform feature engineering
4. Create additional BMI and age-group features
5. Scale the input features
6. Train the Machine Learning model
7. Save the trained model as `model.pkl`
8. Save the scaler as `scaler.pkl`
9. Build the Streamlit application
10. Generate diabetes predictions

---

## 📂 Project Structure

```text
Diabetes-Prediction/
│
├── app.py
├── modelTraining.ipynb
├── model.pkl
├── scaler.pkl
├── .gitignore
├── LICENSE
└── README.md
```

### File Description

| File                  | Description                            |
| --------------------- | -------------------------------------- |
| `app.py`              | Streamlit application                  |
| `modelTraining.ipynb` | Model training and experimentation     |
| `model.pkl`           | Trained Machine Learning model         |
| `scaler.pkl`          | Feature scaler used by the application |
| `.gitignore`          | Git ignored files                      |
| `LICENSE`             | Project license                        |
| `README.md`           | Project documentation                  |

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vikaskatariya30/Diabetes-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd Diabetes-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install pandas scikit-learn streamlit
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

You can then enter the required health parameters and click the **Predict** button to generate the result.

---

## 🖥️ Application

The application provides an interactive form where users can enter:

```text
Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age
```

The model then returns one of two predictions:

```text
Diabetic
```

or

```text
Not Diabetic
```

---

## 📊 Machine Learning

This project is implemented as a **binary classification** problem.

The model receives processed health-related features and predicts the target class:

| Output | Meaning      |
| ------ | ------------ |
| `0`    | Not Diabetic |
| `1`    | Diabetic     |

The trained model and preprocessing scaler are stored using Python's `pickle` module and loaded by the Streamlit application.

---

## 🧠 Feature Engineering

The application creates additional features from the original input data.

### BMI Category

BMI is used to derive BMI-related categorical features.

### Age Groups

Age is converted into groups including:

* 30–40
* 40–50
* 50–60
* 60+

These engineered features are then included in the model input.

---

## 📈 Future Improvements

The project can be further improved by adding:

* [ ] Model accuracy and evaluation metrics
* [ ] Confusion matrix
* [ ] Precision, Recall and F1-score
* [ ] ROC-AUC curve
* [ ] Multiple ML model comparison
* [ ] Prediction probability
* [ ] Improved UI/UX
* [ ] Input validation
* [ ] Data visualization dashboard
* [ ] Model explainability using SHAP
* [ ] Cloud deployment
* [ ] Docker support
* [ ] Automated CI/CD pipeline

---

## ⚠️ Disclaimer

This application is an **educational Machine Learning project**.

Predictions generated by this application should **not be considered a medical diagnosis**. Real-world medical applications require clinically validated datasets, appropriate evaluation, external validation, regulatory considerations, and professional medical oversight.

---

## 👨‍💻 Author

**Vikas Katariya**

* GitHub: [vikaskatariya30](https://github.com/vikaskatariya30)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for more information.
