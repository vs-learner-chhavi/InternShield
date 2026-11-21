# InternShield — Simple AI Project

InternShield is a beginner-friendly internship offer risk analyser built using only three syllabus concepts:

1. **TF-IDF (Unit II):** Converts offer text into numerical features.
2. **Rule-Based System (Unit II):** Applies simple IF-THEN rules to the information supplied by the user.
3. **Fuzzy Logic (Unit III):** Combines the two risk scores and produces Low, Medium or High risk.

## 1. Project flow

Internship description
→ TF-IDF text analysis
→ Rule-Based System
→ Fuzzy Logic
→ Final risk assessment

## 2. Requirements

- Python 3.10 or later
- Internet connection only to install the packages for the first time

## 3. Setup on Windows PowerShell

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

The app will open in your browser. The sample dataset is already included. The TF-IDF vocabulary and word weights are prepared automatically when the app starts; you do not need to run a separate training command.

## 4. How the three concepts work

### Concept 1 — TF-IDF

TF-IDF means Term Frequency–Inverse Document Frequency. It converts words in internship descriptions into numerical values. Words that are useful for distinguishing documents can receive higher weights.

The TF-IDF assigns numerical weights to words in the offer. The program adds the weights of selected warning terms and calculates a simple text warning score. This keeps the project limited to the three selected syllabus concepts.

**Viva point:** TF-IDF converts text into numerical features. In this project, the weights of selected warning terms are used to create a simple text warning score. There is no separate machine-learning classifier.

### Concept 2 — Rule-Based System

The program checks four conditions:

- If the offer asks for an upfront payment, add 40 risk points.
- If no interview was conducted, add 15 points.
- If the recruiter is not independently verified, add 25 points.
- If the company is not independently verified, add 20 points.

Unknown answers do not add points. The total is capped at 100.

**Viva point:** A rule-based system uses predefined IF-THEN statements to make decisions.

### Concept 3 — Fuzzy Logic

Fuzzy logic handles situations that are not simply true or false. It calculates membership in three categories:

- Low
- Medium
- High

The app averages the ML score and rule score, calculates membership values, and combines them into one final score. It then displays:

- Below 35: Low risk
- 35 to below 65: Medium risk
- 65 or above: High risk

**Viva point:** Fuzzy logic helps represent degrees of risk instead of treating every offer as completely safe or completely fraudulent.

## 5. Important limitations

- The included dataset is small and educational. It is not suitable for real-world fraud detection.
- Model scores are not calibrated probabilities that an offer is fraudulent.
- The app does not browse the internet or independently verify companies or recruiters.
- A low risk score does not prove that an internship is genuine.
- Always verify an offer through the company's official website and independently confirmed contact details.

## 6. Project files

- `app.py` — Streamlit user interface.
- `src/text_model.py` — TF-IDF text analysis.
- `src/rules.py` — IF-THEN rules.
- `src/fuzzy.py` — Fuzzy risk calculation.
- `src/analyzer.py` — Connects the three concepts.
- `data/sample_offers.csv` — Small example training dataset.
