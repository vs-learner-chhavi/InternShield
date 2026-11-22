from src.text_model import predict_text_risk, predict_scam
from src.rules import check_rules
from src.fuzzy import calculate_fuzzy_risk


def analyze_offer(offer_text, fee, interview, recruiter, company):

    tfidf_score = predict_text_risk(offer_text)

    model_score, model_prediction = predict_scam(offer_text)

    rule_score, findings = check_rules(
        fee=fee,
        interview=interview,
        recruiter=recruiter,
        company=company
    )

    final_score, risk_level = calculate_fuzzy_risk(
        model_score,
        rule_score
    )

    return {
        "tfidf_score": tfidf_score,
        "model_score": model_score,
        "model_prediction": model_prediction,
        "rule_score": rule_score,
        "risk_score": final_score,
        "risk_level": risk_level,
        "rule_findings": findings
    }
