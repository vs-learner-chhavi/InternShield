from src.text_model import predict_text_risk
from src.rules import check_rules
from src.fuzzy import calculate_fuzzy_risk


def analyze_offer(offer_text, fee, interview, recruiter, company):
    """
    Main project function:
    1. TF-IDF analyses the offer text and calculates a warning-term score.
    2. IF-THEN rules inspect the user's answers.
    3. Fuzzy logic combines both scores.
    """
    tfidf_score = predict_text_risk(offer_text)
    rule_score, findings = check_rules(
        fee=fee,
        interview=interview,
        recruiter=recruiter,
        company=company
    )
    final_score, risk_level = calculate_fuzzy_risk(tfidf_score, rule_score)

    return {
        "tfidf_score": tfidf_score,
        "rule_score": rule_score,
        "risk_score": final_score,
        "risk_level": risk_level,
        "rule_findings": findings
    }
