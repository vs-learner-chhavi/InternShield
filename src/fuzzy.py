
def membership_low(value):
    if value <= 20:
        return 1.0
    if value >= 45:
        return 0.0
    return (45 - value) / 25


def membership_medium(value):
    if value <= 25 or value >= 75:
        return 0.0
    if value <= 50:
        return (value - 25) / 25
    return (75 - value) / 25


def membership_high(value):
    if value <= 40:
        return 0.0
    if value >= 60:
        return 1.0
    return (value - 40) / 20


def calculate_fuzzy_risk(tfidf_score, rule_score):

    # Membership values for TF-IDF score
    text_low = membership_low(tfidf_score)
    text_medium = membership_medium(tfidf_score)
    text_high = membership_high(tfidf_score)

    # Membership values for rule-based score
    rule_low = membership_low(rule_score)
    rule_medium = membership_medium(rule_score)
    rule_high = membership_high(rule_score)

    # Fuzzy IF-THEN rules
    low_strength = min(text_low, rule_low)

    medium_strength = max(
        min(text_medium, rule_medium),
        min(text_low, rule_medium),
        min(text_medium, rule_low)
    )

    high_strength = max(text_high, rule_high)

    # Output values for each category
    low_output = 15
    medium_output = 50
    high_output = 85

    numerator = (
        low_strength * low_output
        + medium_strength * medium_output
        + high_strength * high_output
    )

    denominator = (
        low_strength + medium_strength + high_strength
    )

    final_score = numerator / denominator if denominator else 0

    if final_score < 35:
        risk_level = "Low"
    elif final_score < 60:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return round(final_score, 1), risk_level
