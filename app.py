import streamlit as st
from src.analyzer import analyze_offer

st.set_page_config(page_title="InternShield", page_icon="🛡️", layout="centered")

st.title("🛡️ InternShield")
st.subheader("Simple Internship Offer Risk Analyzer")
st.write(
    "InternShield analyses an internship offer using three concepts: "
    "**TF-IDF**, **Rule-Based Systems**, and **Fuzzy Logic**."
)
st.info(
    "This tool estimates risk from the information provided. "
    "It does not independently verify a company or guarantee that an offer is genuine."
)

with st.form("offer_form"):
    offer_text = st.text_area(
        "Paste the internship offer description",
        height=220,
        placeholder="Paste the complete internship message or job description here..."
    )

    st.markdown("### Additional information")
    col1, col2 = st.columns(2)
    with col1:
        fee = st.selectbox(
            "Does the company ask for money?",
            ["Unknown", "Yes", "No"]
        )
        interview = st.selectbox(
            "Was an interview conducted?",
            ["Unknown", "Yes", "No"]
        )
    with col2:
        recruiter = st.selectbox(
            "Is the recruiter independently verified?",
            ["Unknown", "Yes", "No"]
        )
        company = st.selectbox(
            "Is the company independently verified?",
            ["Unknown", "Yes", "No"]
        )

    submitted = st.form_submit_button("Analyse Internship", type="primary")

if submitted:
    if not offer_text.strip():
        st.error("Please enter an internship description first.")
    else:
        result = analyze_offer(
            offer_text=offer_text,
            fee=fee,
            interview=interview,
            recruiter=recruiter,
            company=company
        )

        st.divider()
        st.header("Assessment Result")

        score = result["risk_score"]
        risk = result["risk_level"]
        if risk == "Low":
            st.success(f"Risk Level: {risk}")
        elif risk == "Medium":
            st.warning(f"Risk Level: {risk}")
        else:
            st.error(f"Risk Level: {risk}")

        st.metric("Overall Risk Score", f"{score:.1f} / 100")
        st.progress(int(score))

        left, right = st.columns(2)
        left.metric("TF-IDF text score", f'{result["tfidf_score"]:.1f}/100')
        right.metric("Rule-based score", f'{result["rule_score"]:.1f}/100')

        st.subheader("Rule-Based Findings")
        if result["rule_findings"]:
            for finding in result["rule_findings"]:
                st.write(f"• {finding}")
        else:
            st.write("No suspicious rule was triggered by the supplied information.")

        st.subheader("How was the result calculated?")
        st.write(
            "The text was analysed using TF-IDF to calculate a warning-term score. "
            "The rule-based system checked the additional answers. "
            "Fuzzy logic combined the ML risk score and rule risk score "
            "to produce the final risk level."
        )

        st.caption(
            "A Low score does not prove an offer is genuine. Always verify the "
            "company and recruiter through independent, official sources."
        )
