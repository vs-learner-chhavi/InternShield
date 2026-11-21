def check_rules(fee, interview, recruiter, company):
    """
    Simple IF-THEN rules.
    Unknown answers do not automatically count as safe or suspicious.
    """
    score = 0
    findings = []

    if fee == "Yes":
        score += 40
        findings.append("High risk: the offer asks for an upfront payment.")
    if interview == "No":
        score += 15
        findings.append("Concern: no interview was conducted.")
    if recruiter == "No":
        score += 25
        findings.append("High risk: the recruiter is not independently verified.")
    if company == "No":
        score += 20
        findings.append("Concern: the company is not independently verified.")

    return min(score, 100), findings
