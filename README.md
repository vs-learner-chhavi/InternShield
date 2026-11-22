# InternShield

**Be Safe. Intern Smart.**

InternShield is a Streamlit-based tool that helps students review internship offers for potential warning signs. It analyses the offer description using a TF-IDF-based text warning score, checks additional information through predefined IF-THEN rules, and combines the two signals using fuzzy logic.

> **Disclaimer:** InternShield provides an educational risk estimate based on the information entered. It does not independently verify companies or recruiters, and its scores are not probabilities of fraud. A low score does not guarantee that an offer is genuine.

## Features

- **TF-IDF text analysis:** Converts the offer description into numerical features and calculates a warning score using a predefined set of suspicious terms.
- **Rule-based checks:** Evaluates answers about upfront fees, interviews, recruiter verification, and company verification.
- **Fuzzy risk assessment:** Combines the text and rule-based scores to produce an overall risk score and a Low, Medium, or High risk category.
- **Explanation of findings:** Displays the rule-based warning signals that were triggered.

## How it works

1. Paste the internship offer description into the app.
2. Answer the additional questions about payment, interview status, and independent verification.
3. InternShield calculates a TF-IDF text warning score.
4. The rule-based system calculates a score from the additional answers.
5. Fuzzy logic combines both scores and displays the overall assessment.

The text score is a transparent, term-based warning score. **It is not a separately trained fraud-classification model.**

## Tech stack

| Technology | Purpose |
| --- | --- |
| Python | Core application logic |
| Streamlit | Interactive web interface |
| scikit-learn | TF-IDF vectorization |
| CSV | Stores the sample offer descriptions used to fit the TF-IDF vocabulary |

## Project structure

```text
InternShield/
├── app.py
├── requirements.txt
├── data/
│   └── sample_offers.csv
└── src/
    ├── __init__.py
    ├── analyzer.py
    ├── fuzzy.py
    ├── rules.py
    └── text_model.py
```

- `app.py` — Streamlit interface for entering and analysing offers.
- `src/analyzer.py` — Connects the text analysis, rule checks, and fuzzy risk calculation.
- `src/text_model.py` — Fits the TF-IDF vectorizer on the included sample descriptions and calculates the text warning score.
- `src/rules.py` — Applies the predefined IF-THEN checks to the user's answers.
- `src/fuzzy.py` — Combines the two scores and assigns the final risk category.
- `data/sample_offers.csv` — Small educational dataset containing example offer descriptions.

## Getting started

### Requirements

- Python 3.10 or later
- pip

### 1. Clone the repository

```bash
git clone https://github.com/vs-learner-chhavi/InternShield.git
cd InternShield
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal (usually http://localhost:8501). Open it in your browser to use InternShield.

No separate model-training command is required. The TF-IDF vectorizer is fitted on the included sample descriptions when the application imports the text-analysis module.

## Understanding the scores

- **TF-IDF text score:** Measures the share of the offer's TF-IDF weight associated with the predefined warning terms. It is a text-based indicator, not a probability.
- **Rule-based score:** Adds risk points for selected answers: an upfront fee, no interview, an unverified recruiter, or an unverified company. Unknown answers do not add points.
- **Overall risk score:** Fuzzy logic combines the text and rule-based signals and assigns a Low, Medium, or High category.

## Limitations and safe use

- The included dataset is small and intended for educational demonstration, not reliable real-world fraud detection.
- The TF-IDF component uses predefined warning terms; it does not understand the full meaning or context of an offer.
- The app relies on the information entered by the user. It does not browse the internet or independently verify an organisation, recruiter, email address, or job posting.
- A low score does not prove that an offer is legitimate, and a high score is not definitive proof of fraud.
- Do not share sensitive identity or banking information with an unverified recruiter. Check opportunities through the organisation's official website and independently confirmed contact details.

---

**InternShield · Be Safe. Intern Smart.**
