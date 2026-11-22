# 🛡️ InternShield
### AI-Powered Internship Scam Detection System

InternShield is an AI-powered internship offer analysis system designed to help students identify potentially fraudulent internship opportunities before sharing personal information or making payments.

It combines **Natural Language Processing (NLP), Machine Learning, Rule-Based Systems, and Fuzzy Logic** to analyze internship descriptions and additional information provided by users.

The system generates an overall risk score, classifies the offer into a risk category, and highlights potential warning signals.

---

## 🚀 Key Features

- **AI-Based Text Analysis:** Uses TF-IDF to convert internship descriptions into numerical text features.
- **Machine Learning Classification:** Uses Multinomial Naive Bayes to predict whether an internship offer is likely genuine or fraudulent.
- **Rule-Based Detection:** Evaluates additional information such as registration fees, recruiter verification, interview procedures, and company verification.
- **Fuzzy Logic:** Combines machine learning and rule-based scores to calculate an overall risk score.
- **Risk Classification:** Categorizes internship offers into Low, Medium, and High Risk.
- **Interactive Interface:** Provides a Streamlit-based interface for submitting and analyzing internship offers.
- **Warning Signals:** Displays findings from the rule-based detection system.

---

## 🧠 How InternShield Works

InternShield uses four main components to analyze an internship offer.

### 1. TF-IDF (Text Feature Extraction)

TF-IDF (Term Frequency–Inverse Document Frequency) converts textual internship descriptions into numerical representations.

It helps identify important words and phrases in an offer that can be used by the machine learning model.

InternShield uses:
- Lowercase text processing
- English stop-word removal
- Unigrams and bigrams
- A maximum of 20,000 features

The application also calculates a separate heuristic suspicious-text score using a predefined list of suspicious terms.

### 2. Multinomial Naive Bayes

A Multinomial Naive Bayes classifier is trained on the processed internship dataset.

It learns patterns associated with genuine and fraudulent internship descriptions.

The classifier produces:
- Predicted category: Likely Genuine or Likely Fake
- Estimated scam-class probability

### 3. Rule-Based Detection

The rule-based system evaluates additional information supplied by the user.

| Condition | Risk Points |
|---|---:|
| Company asks for money | +40 |
| No interview conducted | +15 |
| Recruiter not independently verified | +25 |
| Company not independently verified | +20 |

The total score is capped at 100.

### 4. Fuzzy Logic

Fuzzy Logic combines the Naive Bayes scam probability and rule-based score.

Both inputs are evaluated using three membership categories:

- Low
- Medium
- High

The fuzzy inference system applies IF–THEN rules, aggregates their strengths, and calculates a final risk score using weighted output values.

The final score is classified as:

| Risk Score | Risk Level |
|---|---|
| Below 35 | Low |
| 35–59.9 | Medium |
| 60–100 | High |

---

## 🔄 System Architecture

```text
           User Input
                |
                v
       Internship Description
                |
         Additional Questions
                |
        +-------+-------+
        |               |
        v               v
   TF-IDF +          Rule-Based
   Naive Bayes        Detection
        |               |
        v               v
   Scam Probability   Rule Score
        |               |
        +-------+-------+
                |
                v
           Fuzzy Logic
                |
                v
        Final Risk Score
                |
                v
       Low / Medium / High
                |
                v
        Streamlit Dashboard
```

---

## 📊 Dataset

InternShield uses a synthetic internship-offer dataset containing **10,000 records**.

| Category | Records |
|---|---:|
| Genuine Internship Offers | 5,000 |
| Fraudulent Internship Offers | 5,000 |
| Total | 10,000 |

Dataset columns:

- `description`: Internship offer description.
- `is_scam`: Classification label (0 = Genuine, 1 = Fraudulent).

The dataset is preprocessed to remove empty descriptions, invalid labels, duplicate records, and conflicting descriptions.

**Note:** The dataset is synthetically generated and should not be considered a substitute for a large, independently verified collection of real internship offers.

---

## 📈 Model Evaluation

The Naive Bayes model was evaluated using an 80:20 stratified train-test split.

- Training records: 8,000
- Testing records: 2,000

### Evaluation Results

| Metric | Score |
|---|---:|
| Accuracy | 96.55% |
| Precision | 96.69% |
| Recall | 96.40% |
| F1 Score | 96.54% |
| PR-AUC | 96.34% |

### Confusion Matrix

| | Predicted Genuine | Predicted Fake |
|---|---:|---:|
| Actual Genuine | 967 | 33 |
| Actual Fake | 36 | 964 |

These results represent performance on the synthetic dataset's held-out test split. They do not establish equivalent performance on real-world internship offers.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset processing |
| Scikit-learn | TF-IDF and Naive Bayes |
| NumPy | Numerical operations |
| Joblib | Saving and loading trained models |
| Streamlit | Interactive web application |
| Fuzzy Logic | Final risk assessment |

---

## 📁 Project Structure

```text
InternShield/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── internshield_synthetic_dataset.csv
│   │
│   └── processed/
│       └── internship_offers.csv
│
├── models/
│   ├── tfidf_vectorizer.pkl
│   └── naive_bayes_model.pkl
│
└── src/
    ├── __init__.py
    ├── data_preprocessing.py
    ├── train_model.py
    ├── evaluate_model.py
    ├── text_model.py
    ├── rules.py
    ├── fuzzy.py
    └── analyzer.py
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/vs-learner-chhavi/InternShield.git
```

### 2. Navigate to the project directory

```bash
cd InternShield
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Prepare the dataset

```bash
python -m src.data_preprocessing
```

### 6. Train the model

```bash
python -m src.train_model
```

This generates the trained TF-IDF vectorizer and Naive Bayes model inside the `models/` directory.

### 7. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🧪 Testing and Evaluation

Evaluate the model:

```bash
python -m src.evaluate_model
```

---

## ⚠️ Limitations

- The model is trained on a synthetic dataset, so its predictions may not generalize to real-world internship scams.
- Naive Bayes probabilities are model estimates and are not necessarily calibrated real-world fraud probabilities.
- The rule-based system depends on the accuracy of information entered by the user.
- The system does not independently verify company registrations, recruiter identities, or internship offers.
- A low-risk classification does not guarantee that an internship offer is genuine.

InternShield should be treated as a preliminary risk-assessment tool, not a definitive fraud verification service.

---

## 🔮 Future Improvements

- Evaluate the system on independently collected, real-world internship offers.
- Integrate explainable AI techniques to highlight suspicious words and phrases.
- Add company and recruiter verification through reliable external sources.
- Improve detection of phishing links and suspicious communication patterns.
- Develop a browser extension for analyzing internship offers directly from websites.
- Expand the dataset with diverse, independently verified examples.
- Improve model evaluation through cross-validation and probability calibration.

---


*InternShield — Helping students make safer internship decisions through AI.*