import streamlit as st
from src.analyzer import analyze_offer

st.set_page_config(
    page_title="InternShield | Internship Offer Risk Analyzer",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# InternShield - UI only
# Backend analyzer remains unchanged.
# -----------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #102D59;
    --blue: #1E4F89;
    --blue2: #2F70B8;
    --pale: #EAF3FF;
    --line: #D8E4F4;
    --muted: #526987;
    --green: #159B6C;
    --amber: #D18A20;
    --red: #D94B57;
}
.stApp {
    background: #F5F8FD;
    color: var(--navy);
    font-family: 'Inter', sans-serif;
}
.block-container {
    max-width: 1320px;
    padding-top: 1.0rem;
    padding-bottom: 2.5rem;
}
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

/* Slim navigation strip from the reference */
.topbar {
    min-height: 48px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 7px 20px;
    margin: 0 0 2px;
    background: linear-gradient(90deg, #E5F0FF, #DCEBFF);
    border: 1px solid #D5E5FA;
    border-bottom: 1px solid #C7DAF2;
    color: #123B70;
}
.topbar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.05rem;
    font-weight: 800;
    letter-spacing: -.35px;
}
.topbar-brand svg { width: 30px; height: 34px; display: block; }
.topbar-tagline {
    color: #173B6B;
    font-size: .68rem;
    font-style: italic;
    font-weight: 700;
}

/* Main hero: large shield and text at left, laptop illustration at right */
.hero-shell {
    display: grid;
    grid-template-columns: minmax(0, 1.25fr) minmax(300px, .9fr);
    align-items: center;
    gap: 22px;
    min-height: 230px;
    padding: 15px 20px 12px;
    background: linear-gradient(105deg, #F8FBFF 0%, #EFF6FF 100%);
    border: 1px solid #E1ECFA;
    border-top: 0;
}
.hero-copy {
    display: flex;
    align-items: center;
    min-width: 0;
    gap: 20px;
}
.hero-shield {
    width: 92px;
    min-width: 92px;
    height: 112px;
}
.hero-divider {
    width: 2px;
    height: 90px;
    background: #173B6B;
    opacity: .9;
}
.hero-text h1 {
    margin: 0 0 3px;
    color: #10376C;
    font-size: clamp(2rem, 3.2vw, 2.65rem);
    line-height: 1.04;
    font-weight: 800;
    letter-spacing: -1.2px;
}
.hero-text h2 {
    margin: 3px 0 7px;
    color: #16477F;
    font-size: clamp(1rem, 1.55vw, 1.28rem);
    line-height: 1.2;
    font-weight: 750;
}
.hero-text p {
    margin: 0;
    max-width: 570px;
    color: #173B6B;
    font-size: .82rem;
    line-height: 1.5;
}
.hero-illustration {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.hero-illustration svg {
    width: min(100%, 410px);
    height: auto;
    display: block;
}

/* Disclaimer bar */
.notice {
    background: #DCEBFF;
    border: 1px solid #AFCDF5;
    border-left: 5px solid #2F70B8;
    border-radius: 9px;
    padding: 10px 14px;
    color: #173B6B;
    font-size: .78rem;
    line-height: 1.5;
    margin: 12px 0 20px;
}

/* Form and result area */
.section-title {
    color: #102D59;
    font-weight: 800;
    font-size: 1.2rem;
    margin: 0 0 4px;
}
.section-subtitle { color: #71839B; font-size: .84rem; margin-bottom: 17px; }
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #DCE6F2;
    border-radius: 18px;
    padding: 20px 22px;
    box-shadow: 0 8px 24px rgba(16,45,89,.045);
}
.stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: #D6E2F0 !important;
    background: #FBFDFF !important;
}
.stTextArea textarea { min-height: 190px; }
.stTextArea label, .stSelectbox label {
    color: #29466D !important;
    font-weight: 650 !important;
}
.stButton > button, .stFormSubmitButton > button {
    background: #1E4F89 !important;
    color: white !important;
    border: 0 !important;
    border-radius: 10px !important;
    padding: .68rem 1.25rem !important;
    font-weight: 750 !important;
    min-height: 45px;
    width: 100%;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: #163D70 !important;
    border: 0 !important;
}
.result-label {
    color: #71839B;
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.risk-number {
    color: #102D59;
    font-size: 2.7rem;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.2;
}
.risk-pill {
    display: inline-block;
    border-radius: 30px;
    padding: 6px 13px;
    font-size: .8rem;
    font-weight: 800;
    margin: 8px 0 15px;
}
.finding {
    background: #F6F9FE;
    border: 1px solid #E1EAF5;
    border-radius: 10px;
    padding: 10px 12px;
    margin: 7px 0;
    color: #344F70;
    font-size: .88rem;
}
.metric-box {
    background: #F5F8FD;
    border: 1px solid #E1EAF5;
    border-radius: 12px;
    padding: 13px;
}
.metric-name { color: #71839B; font-size: .75rem; font-weight: 700; }
.metric-value { color: #173B6B; font-size: 1.35rem; font-weight: 800; margin-top: 4px; }
.footer {
    text-align: center;
    color: #8797AB;
    font-size: .78rem;
    padding: 28px 0 5px;
}
@media (max-width: 760px) {
    .hero-shell { grid-template-columns: 1fr; padding: 18px 14px; }
    .hero-illustration svg { max-width: 330px; }
    .hero-copy { gap: 12px; }
    .hero-shield { width: 68px; min-width: 68px; height: 88px; }
    .hero-divider { height: 76px; }
    .topbar { padding: 7px 10px; }
}
</style>
""", unsafe_allow_html=True)

# Slim top navigation
st.markdown("""
<div class="topbar">
  <div class="topbar-brand">
    <svg viewBox="0 0 64 72" role="img" aria-label="InternShield logo" xmlns="http://www.w3.org/2000/svg">
      <path d="M32 3 L57 12 L55 39 Q51 57 32 68 Q13 57 9 39 L7 12 Z" fill="#123F78"/>
      <path d="M32 11 L49 17 L47 38 Q44 51 32 59 Q20 51 17 38 L15 17 Z" fill="#1F5B9D"/>
      <path d="M17 30 L32 22 L47 30 L32 38 Z" fill="#FFFFFF"/>
      <path d="M22 34 L22 42 Q32 49 42 42 L42 34 L32 40 Z" fill="#FFFFFF"/>
      <path d="M47 30 L47 43" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>
      <circle cx="47" cy="45" r="2.5" fill="#FFFFFF"/>
    </svg>
    <span>InternShield</span>
  </div>
  <div class="topbar-tagline">Be Safe. Intern Smart.</div>
</div>

<div class="hero-shell">
  <div class="hero-copy">
    <svg class="hero-shield" viewBox="0 0 120 145" role="img" aria-label="Shield and graduation cap" xmlns="http://www.w3.org/2000/svg">
      <path d="M60 4 L108 22 L105 76 Q98 116 60 139 Q22 116 15 76 L12 22 Z" fill="#103F7C"/>
      <path d="M60 15 L96 29 L94 75 Q88 106 60 124 Q32 106 26 75 L24 29 Z" fill="#174F91"/>
      <path d="M24 62 L60 43 L96 62 L60 81 Z" fill="#FFFFFF"/>
      <path d="M39 70 L39 87 Q60 102 81 87 L81 70 L60 82 Z" fill="#FFFFFF"/>
      <path d="M96 62 L96 91" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
      <circle cx="96" cy="94" r="3" fill="#FFFFFF"/>
    </svg>
    <div class="hero-divider"></div>
    <div class="hero-text">
      <h1>InternShield</h1>
      <h2>Simple Internship Offer Risk Analyzer</h2>
      <p>Paste an internship offer and let InternShield help you spot<br>
      potential risks using TF-IDF, Naive Bayes, Rule-Based Systems and Fuzzy Logic.</p>
    </div>
  </div>

  <div class="hero-illustration">
    <svg viewBox="0 0 430 190" role="img" aria-label="Laptop showing internship offer with magnifying glass and warning sign" xmlns="http://www.w3.org/2000/svg">
      <path d="M40 74 C45 32 86 24 119 39 C143 -2 195 0 220 31 C257 4 305 17 317 52 C364 42 399 76 390 117 C386 153 355 169 319 161 L92 166 C43 163 18 125 40 74Z" fill="#D8E8FF"/>
      <path d="M75 45 C91 34 107 47 105 64 L94 101 C90 117 65 117 57 101 C45 79 54 55 75 45Z" fill="#C8DEFF"/>
      <path d="M328 105 C351 86 376 97 379 120 C382 143 357 158 337 147Z" fill="#C4DCFF"/>
      <path d="M164 26 L184 10 L204 28 L192 52 L172 48Z" fill="#C4DCFF"/>
      <rect x="132" y="35" width="177" height="116" rx="10" fill="#243F78"/>
      <rect x="139" y="42" width="163" height="99" rx="5" fill="#F8FBFF"/>
      <rect x="151" y="53" width="139" height="19" rx="3" fill="#DCEBFF"/>
      <text x="160" y="66" font-family="Arial,sans-serif" font-size="10" font-weight="700" fill="#173B6B">INTERNSHIP OFFER</text>
      <rect x="151" y="81" width="102" height="7" rx="3.5" fill="#C4D3E8"/>
      <rect x="151" y="96" width="119" height="7" rx="3.5" fill="#C4D3E8"/>
      <rect x="151" y="111" width="91" height="7" rx="3.5" fill="#C4D3E8"/>
      <path d="M115 151 L327 151 L347 169 Q350 174 340 175 L101 175 Q92 174 98 168Z" fill="#536B9B"/>
      <path d="M101 169 L340 169" stroke="#A8B8D2" stroke-width="3"/>
      <circle cx="276" cy="112" r="29" fill="#FFFFFF" stroke="#4778B8" stroke-width="7"/>
      <path d="M297 134 L337 171" stroke="#17477F" stroke-width="12" stroke-linecap="round"/>
      <path d="M276 91 L294 125 L258 125 Z" fill="#F0444E"/>
      <path d="M276 101 L276 113" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
      <circle cx="276" cy="119" r="2.5" fill="#FFFFFF"/>
      <path d="M326 29 L335 12 M343 39 L359 30 M347 53 L365 53" stroke="#1476E8" stroke-width="4" stroke-linecap="round"/>
      <circle cx="79" cy="100" r="22" fill="#FFFFFF" opacity=".95"/>
      <path d="M68 100 L76 108 L91 90" fill="none" stroke="#4C91D8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>

<div class="notice">
  <strong>ⓘ</strong> &nbsp; This tool estimates risk from the information provided. It does not independently verify a company or guarantee that an offer is genuine.
</div>
""", unsafe_allow_html=True)

# Main form and assessment panels
form_col, result_col = st.columns([1.08, 0.92], gap="large")

with form_col:
    with st.container(border=True):
        st.markdown('<div class="section-title">Review an internship offer</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Paste the offer and answer a few quick questions.</div>', unsafe_allow_html=True)

        with st.form("offer_form", clear_on_submit=False):
            offer_text = st.text_area(
                "Internship offer description",
                height=205, 
                placeholder="Paste the complete internship message, email, or job description here..."
            )
            st.markdown("**Additional information**")
            c1, c2 = st.columns(2)
            with c1:
                fee = st.selectbox("Does the company ask for money?", ["Unknown", "Yes", "No"])
                interview = st.selectbox("Was an interview conducted?", ["Unknown", "Yes", "No"])
            with c2:
                recruiter = st.selectbox("Is the recruiter independently verified?", ["Unknown", "Yes", "No"])
                company = st.selectbox("Is the company independently verified?", ["Unknown", "Yes", "No"])
            submitted = st.form_submit_button("Analyse Internship Offer")

with result_col:
    with st.container(border=True):
        st.markdown('<div class="section-title">Risk assessment</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Your analysis will appear here after submission.</div>', unsafe_allow_html=True)

        if "internshield_result" not in st.session_state:
            st.markdown("""
            <div style="text-align:center;padding:28px 8px 24px;">
              <div style="font-size:54px;margin-bottom:12px;">🛡️</div>
              <div style="font-size:1.05rem;font-weight:800;color:#173B6B;">Ready when you are</div>
              <div style="font-size:.86rem;color:#71839B;line-height:1.6;margin-top:7px;">
                Submit an internship offer to see its estimated risk score,
                warning signals, and assessment breakdown.
              </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            result = st.session_state["internshield_result"]
            score = float(result["risk_score"])
            risk = str(result["risk_level"])
            if risk.lower() == "low":
                risk_color, risk_bg = "#159B6C", "#E6F6F0"
            elif risk.lower() == "medium":
                risk_color, risk_bg = "#B7791F", "#FFF5DF"
            else:
                risk_color, risk_bg = "#D94B57", "#FDECEE"

            st.markdown(f"""
            <div class="result-label">Overall risk score</div>
            <div class="risk-number">{score:.1f}<span style="font-size:1rem;color:#8292A7;font-weight:600;"> / 100</span></div>
            <span class="risk-pill" style="color:{risk_color};background:{risk_bg};"> {risk.upper()} RISK </span>
            """, unsafe_allow_html=True)
            st.progress(max(0, min(100, int(round(score)))))
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f"""
                <div class="metric-box">
                <div class="metric-name">TF-IDF SCORE</div>
                <div class="metric-value">{float(result["tfidf_score"]):.1f}<span style="font-size:.8rem;"> / 100</span></div>
                </div>
                """, unsafe_allow_html=True)
            with m2:
                st.markdown(f"""
                <div class="metric-box">
                <div class="metric-name">NAIVE BAYES SCORE</div>
                <div class="metric-value">{float(result["model_score"]):.1f}<span style="font-size:.8rem;"> / 100</span></div>
                <div style="font-size:.75rem;color:#526987;margin-top:4px;">{result["model_prediction"]}</div>
                </div>
                """, unsafe_allow_html=True)
            with m3:
                st.markdown(f"""
                <div class="metric-box">
                <div class="metric-name">RULE-BASED SCORE</div>
                <div class="metric-value">{float(result["rule_score"]):.1f}<span style="font-size:.8rem;"> / 100</span></div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("**Warning signals and findings**")
            findings = result["rule_findings"]
            if findings:
                for finding in findings:
                    st.markdown(f'<div class="finding">• {finding}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="finding">No suspicious rule was triggered by the supplied information.</div>', unsafe_allow_html=True)

            st.markdown("""
            <div style="font-size:.78rem;color:#71839B;line-height:1.55;margin-top:15px;">
                TF-IDF extracts text features, Naive Bayes predicts the offer category,
                the rule-based system checks additional answers, and fuzzy logic combines
                the model and rule-based scores.
            </div>
            """, unsafe_allow_html=True)

# Run the existing backend only when the form is submitted.
if submitted:
    if not offer_text.strip():
        st.error("Please enter an internship description first.")
    else:
        try:
            result = analyze_offer(
                offer_text=offer_text,
                fee=fee,
                interview=interview,
                recruiter=recruiter,
                company=company
            )
            st.session_state["internshield_result"] = result
            st.rerun()
        except Exception as exc:
            st.error(f"Analysis could not be completed: {exc}")

st.markdown("""
<div class="footer">
  InternShield · Be Safe. Intern Smart. · An assistive risk estimate, not a guarantee.
</div>
""", unsafe_allow_html=True)
