import base64
import streamlit as st
import streamlit.components.v1 as components

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Johannes Favi | Strategic Consulting",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CONTACT_EMAIL = "contactcageddreams@gmail.com"

CAGED_DREAMS_URL = "https://cageddreams.com/"
CAGED_DREAMS_FILM_URL = "https://www.youtube.com/watch?v=9tPgUSNf22Y"
TASK_FORCE_REPORT_URL = (
    "https://www.ilga.gov/Documents/Reports/ReportsSubmitted/"
    "6390RSGAEmail14131RSGAAttachReport%20of%20the%20Task%20Force%20on%20Black%20Immigrants_12-29-2025.pdf"
)


def _img_to_data_uri(path: str) -> str:
    """Read a local image file and return it as a base64 data URI,
    so it can be embedded directly inside an HTML/markdown block."""
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"


HERO_PHOTO_URI = _img_to_data_uri("assets/johannes-favi-hero.jpg")

ORG_LOGOS = [
    ("assets/logos/logo-bridge-communities.png", "Bridge Communities"),
    ("assets/logos/logo-uchicago.png", "University of Chicago"),
    ("assets/logos/logo-uic.png", "University of Illinois Chicago"),
    ("assets/logos/logo-depaul.png", "DePaul University"),
    ("assets/logos/logo-nijc.png", "National Immigrant Justice Center"),
    ("assets/logos/logo-dwn.png", "Detention Watch Network"),
    ("assets/logos/logo-ccga.png", "Chicago Council on Global Affairs"),
    ("assets/logos/logo-icdi.png", "Illinois Community for Displaced Immigrants"),
    ("assets/logos/logo-illinois-gov.png", "State of Illinois"),
    ("assets/logos/logo-clg.png", "Catholic Lawyers Guild of Chicago"),
    ("assets/logos/logo-harris.png", "University of Chicago Harris School of Public Policy"),
    ("assets/logos/logo-healing-horizons.png", "Healing Horizons"),
]
ORG_LOGO_URIS = [(_img_to_data_uri(path), alt) for path, alt in ORG_LOGOS]
ORG_LOGO_URI_MAP = {alt: uri for uri, alt in ORG_LOGO_URIS}

# Curated subset for the homepage strip (8 recognizable logos).
HOME_FEATURED_LOGOS = [
    "State of Illinois", "University of Chicago", "University of Illinois Chicago",
    "DePaul University", "Bridge Communities", "National Immigrant Justice Center",
    "Chicago Council on Global Affairs", "Detention Watch Network",
]

GOV_ORGS = [
    "Office of the Governor of Illinois", "Illinois Department of Human Rights",
    "Illinois Task Force on Black Immigrants", "Office of Congressman Jes\u00fas \u201cChuy\u201d Garc\u00eda",
    "City of Chicago", "Cook County Government", "DuPage County Government",
    "Illinois Housing Development Authority", "State of Illinois",
]

NONPROFIT_ORGS = [
    "Bridge Communities", "Illinois Community for Displaced Immigrants",
    "National Immigrant Justice Center", "Detention Watch Network",
    "United African Organization", "Chicago Refugee Coalition", "ICIRR",
    "New American Leaders", "Change Collective", "DuPage PADS", "RefugeeOne",
    "The Resurrection Project", "Centro Romero", "Ascend Justice",
    "Community Renewal Society", "Caged Dreams", "Chicago Council on Global Affairs",
    "Healing Horizons",
]

HEALTHCARE_ORGS = [
    "Ann & Robert H. Lurie Children's Hospital", "Rush", "CommunityHealth",
    "Coalition for Immigrant Mental Health", "Behavioral Health Providers",
]

EMPLOYER_CATEGORIES = [
    "Manufacturing", "Healthcare", "Hospitality", "Human Resources",
    "Corporate Social Responsibility", "Small Businesses",
]

UNIVERSITY_ORGS = [
    "University of Chicago", "University of Chicago Harris School of Public Policy",
    "University of Illinois Chicago", "DePaul University", "Loyola University Chicago",
    "Boston University", "Northeastern Illinois University", "UCLA",
    "University of Tennessee",
]

FOUNDATION_ORGS = [
    "Chicago Community Trust", "MacArthur Foundation", "Crossroads Fund",
    "Walder Foundation", "Dignity for Families Fund", "Phalarope Foundation",
    "Odyssey Impact",
]

FAITH_ORGS = [
    "Catholic Lawyers Guild of Chicago", "Chicago Religious Leadership Network",
    "Darst Center", "Archdiocese of Chicago", "Viator House of Hospitality",
    "Su Casa Catholic Worker", "Holy Spirit Sisters", "Elmhurst Presbyterian Church",
    "Wellington UCC", "Sanctuary Working Group",
]


def render_org_sector(label, description, org_names, gold_tags=False):
    """Render a sector of organizations: real logos where available,
    clean text tags for everything else."""
    st.markdown(f"<div class='section-label'>{label}</div>", unsafe_allow_html=True)
    st.write(description)
    logo_orgs = [o for o in org_names if o in ORG_LOGO_URI_MAP]
    text_orgs = [o for o in org_names if o not in ORG_LOGO_URI_MAP]
    if logo_orgs:
        logo_html = "".join(
            f"<img src='{ORG_LOGO_URI_MAP[o]}' alt='{o}' title='{o}'>" for o in logo_orgs
        )
        st.markdown(f"<div class='logo-strip'>{logo_html}</div>", unsafe_allow_html=True)
        st.write("")
    if text_orgs:
        tag_class = "tag-gold" if gold_tags else "tag"
        st.markdown(
            "".join(f"<span class='{tag_class}'>{o}</span>" for o in text_orgs),
            unsafe_allow_html=True,
        )
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# GLOBAL STYLE
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --navy: #10233f;
            --navy-light: #1c3a63;
            --gold: #b8924a;
            --off-white: #faf8f4;
            --gray: #6b7280;
        }

        /* Force a light background regardless of device/browser dark mode,
           in case the app hasn't picked up .streamlit/config.toml yet. */
        html, body,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stHeader"] {
            background-color: #ffffff !important;
        }

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        #MainMenu, footer, header {visibility: hidden;}

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3rem;
            max-width: 1100px;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            color: var(--navy);
        }

        /* Hero */
        .hero {
            background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
            padding: 3rem 3rem;
            border-radius: 14px;
            color: #ffffff;
            margin-bottom: 2rem;
        }
        .hero-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2.5rem;
        }
        .hero-text { flex: 1.4; min-width: 0; }
        .hero-photo {
            flex: 1;
            display: flex;
            justify-content: flex-end;
        }
        .hero-photo img {
            width: 100%;
            max-width: 260px;
            border-radius: 14px;
            box-shadow: 0 12px 28px rgba(0,0,0,0.35);
            object-fit: cover;
            border: 3px solid rgba(255,255,255,0.12);
        }
        .hero h1 {
            color: #ffffff;
            font-size: 2.5rem;
            line-height: 1.25;
            margin-bottom: 0.8rem;
        }
        .hero .subhead {
            font-size: 1.1rem;
            color: var(--gold);
            font-weight: 500;
            margin-bottom: 1.2rem;
        }
        .hero p {
            font-size: 1.0rem;
            color: #e6e9ef;
            max-width: 720px;
            line-height: 1.7;
        }
        .hero-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1.1rem;
        }
        .hero-badge {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.25);
            color: #f2ede1;
            font-size: 0.8rem;
            font-weight: 500;
            padding: 0.35rem 0.8rem;
            border-radius: 20px;
        }

        /* Checklist */
        .checklist {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem 1.6rem;
            margin: 0.6rem 0 0.4rem 0;
        }
        .checklist-item {
            color: var(--navy);
            font-size: 0.92rem;
        }
        .checklist-item .check {
            color: var(--gold);
            font-weight: 700;
            margin-right: 0.35rem;
        }

        /* Credibility strip */
        .credibility-wrap {
            text-align: center;
            padding: 0.5rem 0 1.8rem 0;
        }
        .credibility-label {
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--gray);
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.9rem;
        }

        /* Featured organizations logo strip */
        .logo-strip {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;
            gap: 2.2rem 2.6rem;
            padding: 1.6rem 1rem;
            background: var(--off-white);
            border-radius: 12px;
        }
        .logo-strip img {
            height: 34px;
            width: auto;
            object-fit: contain;
        }

        /* Section headers */
        .section-label {
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--gold);
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.3rem;
        }
        .section-title {
            font-size: 1.8rem;
            margin-bottom: 1.2rem;
        }

        /* Cards */
        .card {
            background: var(--off-white);
            border: 1px solid #eae6dd;
            border-left: 3px solid var(--gold);
            border-radius: 10px;
            padding: 1.4rem 1.5rem;
            margin-bottom: 1rem;
            height: 100%;
        }
        .card h4 {
            color: var(--navy);
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1.05rem;
            margin-bottom: 0.5rem;
        }
        .card p {
            color: var(--gray);
            font-size: 0.94rem;
            line-height: 1.55;
            margin: 0;
        }

        .stat-line {
            font-size: 0.98rem;
            color: var(--navy);
            padding: 0.5rem 0;
            border-bottom: 1px solid #eee;
        }

        /* Stat / impact cards */
        .stat-card {
            background: var(--off-white);
            border: 1px solid #eae6dd;
            border-radius: 10px;
            padding: 1.3rem 0.8rem;
            text-align: center;
            height: 100%;
        }
        .stat-number {
            font-family: 'Playfair Display', serif;
            font-size: 2.1rem;
            font-weight: 700;
            color: var(--gold);
            line-height: 1.1;
        }
        .stat-label {
            font-size: 0.82rem;
            color: var(--navy);
            margin-top: 0.3rem;
        }

        /* Featured project box */
        .featured-project {
            background: var(--navy);
            border-radius: 14px;
            padding: 2.4rem 2.6rem;
            color: #ffffff;
        }
        .featured-project .section-label { color: var(--gold); }
        .featured-project h2 { color: #ffffff; margin-bottom: 0.7rem; }
        .featured-project .quote {
            font-style: italic;
            color: var(--gold);
            font-size: 1.05rem;
            margin-bottom: 1rem;
        }
        .featured-project p {
            color: #d7dce5;
            line-height: 1.7;
            font-size: 0.98rem;
        }

        .placeholder-card {
            background: #f7f5f0;
            border: 1px dashed #d8d0bd;
            border-radius: 10px;
            padding: 1.3rem 1.4rem;
            color: var(--gray);
            font-size: 0.92rem;
            margin-bottom: 0.8rem;
        }

        .press-item {
            border-bottom: 1px solid #eee;
            padding: 0.9rem 0;
        }
        .press-item:last-child {
            border-bottom: none;
        }
        .press-item .press-title {
            color: var(--navy);
            font-weight: 600;
            font-size: 0.98rem;
            margin-bottom: 0.15rem;
        }
        .press-item .press-meta {
            color: var(--gold);
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.35rem;
        }
        .press-item .press-desc {
            color: var(--gray);
            font-size: 0.9rem;
            line-height: 1.55;
        }
        .press-item .press-link {
            display: inline-block;
            color: var(--navy) !important;
            text-decoration: underline;
            text-decoration-color: #c9a86a;
            font-size: 0.85rem;
            font-weight: 600;
            margin-top: 0.45rem;
        }
        .press-item .press-link:hover {
            color: var(--gold) !important;
        }

        .testimonial-card {
            background: var(--off-white);
            border: 1px solid #eae6dd;
            border-radius: 10px;
            padding: 1.4rem 1.5rem;
            margin-bottom: 0.8rem;
            height: 100%;
        }
        .testimonial-card .quote-mark {
            color: var(--gold);
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            line-height: 1;
        }
        .testimonial-card .quote-text {
            color: var(--gray);
            font-style: italic;
            font-size: 0.92rem;
            margin: 0.3rem 0 0.7rem 0;
        }
        .testimonial-card .quote-attribution {
            color: var(--navy);
            font-size: 0.85rem;
            font-weight: 600;
        }
        .testimonial-card .quote-role {
            color: var(--gray);
            font-size: 0.8rem;
            margin-top: 0.1rem;
        }

        /* Timeline */
        .timeline-row {
            display: flex;
            gap: 1.2rem;
            margin-bottom: 1.1rem;
        }
        .timeline-year {
            flex: 0 0 90px;
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            color: var(--gold);
            font-size: 1.15rem;
            padding-top: 0.1rem;
        }
        .timeline-items {
            flex: 1;
            border-left: 2px solid #eae6dd;
            padding-left: 1.1rem;
        }
        .timeline-items div {
            color: var(--navy);
            font-size: 0.94rem;
            padding: 0.15rem 0;
        }

        /* Speaking engagements table */
        .speak-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        .speak-table th {
            text-align: left;
            color: var(--gold);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 0.5rem 0.6rem;
            border-bottom: 2px solid #eae6dd;
        }
        .speak-table td {
            padding: 0.6rem 0.6rem;
            border-bottom: 1px solid #f0ede5;
            color: var(--navy);
        }
        .speak-table tr:last-child td {
            border-bottom: none;
        }

        /* Who I Work With category cards */
        .category-card {
            background: var(--off-white);
            border: 1px solid #eae6dd;
            border-radius: 10px;
            padding: 1.1rem 1.2rem;
            margin-bottom: 0.7rem;
            height: 100%;
        }
        .category-card h4 {
            color: var(--navy);
            font-size: 0.98rem;
            margin-bottom: 0.4rem;
        }
        .category-card p {
            color: var(--gray);
            font-size: 0.86rem;
            margin: 0;
            line-height: 1.5;
        }

        .cta-strip {
            background: var(--navy);
            border-radius: 14px;
            padding: 2rem 3rem;
            text-align: center;
            color: #ffffff;
            margin-top: 2.5rem;
            margin-bottom: 1.4rem;
        }
        .cta-strip h2 { color: #ffffff; margin-bottom: 0.6rem; }
        .cta-strip p { color: #d7dce5; margin-bottom: 0; }

        /* Buttons */
        div.stButton > button, div.stLinkButton > a {
            background-color: var(--gold) !important;
            color: var(--navy) !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.55rem 1.4rem !important;
            font-weight: 600 !important;
            transition: 0.2s ease-in-out;
        }
        div.stButton > button:hover, div.stLinkButton > a:hover {
            background-color: #a37d38 !important;
            color: #ffffff !important;
        }

        .ghost-btn a {
            display: inline-block;
            border: 1.5px solid #ffffff55;
            color: #ffffff !important;
            padding: 0.5rem 1.3rem;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.92rem;
        }

        .divider {
            height: 1px;
            background: #e7e2d8;
            margin: 2.2rem 0;
        }

        .tag {
            display: inline-block;
            background: #f1ede3;
            color: var(--navy);
            padding: 0.35rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            margin: 0.2rem 0.3rem 0.2rem 0;
        }

        .tag-gold {
            display: inline-block;
            background: rgba(184, 146, 74, 0.18);
            color: var(--gold);
            padding: 0.35rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin: 0.2rem 0.3rem 0.2rem 0;
        }

        .contact-form-wrap iframe {
            border: none;
        }

        /* ---------------- Mobile responsiveness ---------------- */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1rem;
            }
            .hero {
                padding: 1.75rem 1.25rem;
            }
            .hero-inner {
                flex-direction: column;
                gap: 1.4rem;
            }
            .hero-photo {
                justify-content: center;
                order: -1;
            }
            .hero-photo img {
                max-width: 190px;
            }
            .hero h1 {
                font-size: 1.65rem;
                line-height: 1.3;
            }
            .hero .subhead {
                font-size: 0.85rem;
            }
            .hero p {
                font-size: 0.92rem;
            }
            .section-title {
                font-size: 1.4rem;
            }
            .logo-strip {
                gap: 1.3rem 1.6rem;
                padding: 1.2rem 0.8rem;
            }
            .logo-strip img {
                height: 26px;
            }
            .card {
                padding: 1.1rem 1.2rem;
            }
            .featured-project {
                padding: 1.6rem 1.4rem;
            }
            .cta-strip {
                padding: 1.5rem 1.25rem;
            }
            .cta-strip h2 {
                font-size: 1.3rem;
            }
            .cta-strip p {
                font-size: 0.9rem;
            }
            .tag, .tag-gold {
                font-size: 0.78rem;
                padding: 0.3rem 0.65rem;
            }
            .stat-number {
                font-size: 1.6rem;
            }
        }

        @media (max-width: 480px) {
            .hero h1 {
                font-size: 1.4rem;
            }
            .hero-photo img {
                max-width: 150px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# NAVIGATION
# ----------------------------------------------------------------------------
PAGES = ["Home", "About", "Partners", "Services", "Speaking", "Advisory", "Media", "Impact", "Testimonials", "Contact"]
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go_to(page_name: str):
    st.session_state.page = page_name

st.markdown(
    """
    <style>
        .st-key-nav_bar button {
            background: transparent !important;
            color: #10233f !important;
            border: none !important;
            border-bottom: 3px solid transparent !important;
            border-radius: 0 !important;
            font-weight: 500 !important;
            padding: 0.3rem 0.2rem 0.6rem 0.2rem !important;
            box-shadow: none !important;
        }
        .st-key-nav_bar button:hover {
            color: #b8924a !important;
            background: transparent !important;
            border-bottom: 3px solid #e6d5b0 !important;
        }
        .nav-active {
            color: #b8924a;
            font-weight: 600;
            border-bottom: 3px solid #b8924a;
            padding: 0.3rem 0.2rem 0.6rem 0.2rem;
            display: inline-block;
        }
        .brand-name {
            font-family: 'Playfair Display', serif;
            font-size: 2.1rem;
            font-weight: 700;
            color: #10233f;
            line-height: 1.15;
        }
        .brand-subtitle {
            font-size: 0.95rem;
            color: #6b7280;
            letter-spacing: 0.5px;
        }
        .header-row {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            padding: 0.3rem 0 0.6rem 0;
        }
        .linkedin-link {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: #10233f;
            color: #ffffff !important;
            text-decoration: none !important;
            padding: 0.5rem 1.1rem;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 600;
        }
        .linkedin-link:hover { background: #1c3a63; }

        .st-key-nav_bar div[data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
            gap: 0.15rem 0.5rem !important;
        }
        .st-key-nav_bar div[data-testid="stColumn"] {
            width: auto !important;
            flex: 0 0 auto !important;
            min-width: 0 !important;
        }
        .st-key-nav_bar button,
        .nav-active {
            white-space: nowrap;
        }

        @media (max-width: 768px) {
            .header-row {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.6rem;
            }
            .brand-name {
                font-size: 1.6rem;
            }
            .linkedin-link {
                font-size: 0.8rem;
                padding: 0.4rem 0.9rem;
            }
            .st-key-nav_bar button,
            .nav-active {
                font-size: 0.82rem !important;
                padding: 0.25rem 0.1rem 0.45rem 0.1rem !important;
                white-space: nowrap;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='header-row'>"
    "<div><div class='brand-name'>Johannes Favi</div>"
    "<div class='brand-subtitle'>Strategic Consulting</div></div>"
    "<a class='linkedin-link' href='https://www.linkedin.com/in/johannesfavi/' target='_blank'>"
    "in&nbsp; LinkedIn ↗</a>"
    "</div>",
    unsafe_allow_html=True,
)

with st.container(key="nav_bar"):
    nav_cols = st.columns(len(PAGES))
    for i, p in enumerate(PAGES):
        with nav_cols[i]:
            if p == st.session_state.page:
                st.markdown(f"<span class='nav-active'>{p}</span>", unsafe_allow_html=True)
            else:
                if st.button(p, key=f"nav_{p}", use_container_width=True):
                    go_to(p)
                    st.rerun()

st.markdown("<div class='divider' style='margin-top:0.5rem;'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# SHARED DATA
# ----------------------------------------------------------------------------
RECOGNITION = [
    ("Jeanne & Joseph Sullivan Human Rights Award", "Awarded for leadership advancing immigrant rights and human dignity."),
    ("Special Service Award, Catholic Lawyers Guild of Chicago", "Recognizing outstanding service to immigrant communities."),
    ("Illinois Task Force on Black Immigrants", "Appointed member of the statewide advisory body established by the Illinois General Assembly."),
    ("Chicago City Council Recognition", "Recognized during National Hispanic Heritage Month by Alderman Andre Vasquez."),
    ("Freedom Fellow, Detention Watch Network", "National leadership fellowship advancing alternatives to immigration detention."),
    ("Chicago Council Emerging Leader", "Civic Leadership Academy, University of Chicago Harris School of Public Policy."),
]

TASK_FORCE_AREAS = [
    "Housing", "Workforce Development", "Education", "Healthcare",
    "Economic Opportunity", "Public Safety", "Civic Participation",
]

# Each press item: (headline, source, date, description, link_text, link_url)
PRESS_FEATURED = [
    ("Detained Immigrants Turn to the Courts to Protect Themselves From COVID-19", "WBEZ Chicago", "April 23, 2020",
     "WBEZ reported on Johannes Favi's release from immigration detention following emergency federal "
     "litigation during the COVID-19 pandemic. The article examined the health risks facing detained "
     "immigrants and the impact of prolonged detention on families.",
     "Read the article",
     "https://www.wbez.org/race-class-communities/2020/04/23/detained-immigrants-turn-to-the-courts-to-protect-themselves-from-covid-19"),
    ("Illinois Sets National Precedent in Banning Immigration Detention", "Truthout", "December 16, 2021",
     "Johannes was interviewed about his experience spending more than ten months in immigration "
     "detention and his advocacy supporting Illinois legislation that ended local government contracts "
     "with immigration detention facilities.",
     "Read the article",
     "https://truthout.org/articles/illinois-sets-national-precedent-in-banning-immigration-detention/"),
    ("Illinois Law Ending Immigration Detention in 2022 Hits a Snag", "WBEZ Chicago", "January 4, 2022",
     "Johannes was featured as a formerly detained immigrant and advocate working to end immigration "
     "detention in Illinois.",
     "Read the article",
     "https://www.wbez.org/race-class-communities/2022/01/04/illinois-law-ending-immigration-detention-in-2022-hits-a-snag"),
    ("ICE Camps Are Not Untouchable: How Communities Can Push Back", "Truthout", "May 28, 2026",
     "Johannes was referenced as a Chicago-area advocate whose lived experience and relationships with "
     "detained immigrants help expose conditions inside immigration detention facilities.",
     "Listen and read",
     "https://truthout.org/audio/ice-camps-are-not-untouchable-heres-how-communities-can-push-back/"),
]

DOCUMENTARY_COVERAGE = [
    ("On World Mental Health Day, Detention Watch Network Premieres Caged Dreams", "Detention Watch Network", "October 10, 2023",
     "The official premiere announcement introduced the documentary and highlighted Johannes's experience "
     "as a formerly detained immigrant and advocate.",
     "Read the announcement",
     "https://www.detentionwatchnetwork.org/pressroom/releases/2023/on-world-mental-health-day-detention-watch-network-premieres-caged-dreams"),
    ("Caged Dreams Presented by the Maine Film Center", "Maine Film Center and Waterville Creates", "February 2, 2024",
     "The Maine Film Center featured Caged Dreams as part of its public film programming and identified "
     "Johannes as the documentary's director and one of its featured storytellers.",
     "View the feature",
     "https://www.watervillecreates.org/shows/caged-dreams/"),
]

PERSONAL_STORY = [
    ("NIJC Sues Illinois Jail to Release Immigrants at Severe Risk During COVID-19", "National Immigrant Justice Center", "April 9, 2020",
     "Johannes was identified as one of the immigrants represented in emergency federal litigation seeking "
     "the release of medically vulnerable people from the Jerome Combs Detention Center during the "
     "COVID-19 pandemic.",
     "Read the release",
     "https://immigrantjustice.org/press-release/nijc-sues-illinois-jail-to-release-immigrants-in-ice-custody-who-face-severe-risk-during-covid-19-pandemic/"),
    ("\u201cI Think Every Day About the People Who Are Still in Detention\u201d", "National Immigrant Justice Center", "May 13, 2020",
     "In this first-person profile, Johannes described nearly one year in immigration detention, "
     "separation from his family, the birth of his child during detention, and his testimony before "
     "members of Congress.",
     "Read Johannes's story",
     "https://immigrantjustice.org/blog/i-think-every-day-about-the-people-who-are-still-in-detention-who-should-not-be-there-johanness-story/"),
    ("COVID-19 Habeas Litigation: Delome Johannes Favi", "National Immigrant Justice Center", "2020",
     "This legal case profile documents Johannes's detention, medical vulnerability, federal habeas "
     "petition, and court-ordered release.",
     "View the case profile",
     "https://immigrantjustice.org/for-attorneys/cases/covid-19-habeas-litigation/"),
    ("Johannes Tells Congress About ICE Detention During COVID-19", "National Immigrant Justice Center", "2020",
     "Johannes testified about immigration detention conditions, family separation, and the risks faced "
     "by detained people during the pandemic.",
     "Watch the testimony",
     "https://www.youtube.com/watch?v=EDT4BVSeMcg"),
]

PROFILES = [
    ("Johannes Favi, Emerging Leader", "Chicago Council on Global Affairs",
     "The Chicago Council profile highlights Johannes's immigration advocacy, nonprofit leadership, "
     "public policy work, and the development of Caged Dreams.",
     "Read the profile",
     "https://globalaffairs.org/emerging-leaders/johannes-favi"),
    ("Johannes Favi, Change Collective Member", "Obama Foundation Change Collective",
     "This profile presents Johannes's work advancing immigrant mental health, leadership development, "
     "and community-centered solutions.",
     "Read the profile",
     "https://change-collective.org/members/favi-johannes/"),
    ("Johannes Favi Professional Profile", "University of Chicago Center for Effective Government",
     "The University of Chicago profile highlights Johannes's nonprofit leadership, immigrant advocacy, "
     "and participation in the Civic Leadership Academy.",
     "Read the profile",
     "https://effectivegov.uchicago.edu/people/johannes-favi"),
]

UNIVERSITY_PROGRAMS = [
    ("Chicago Style: Caged Dreams, The Trauma of Chicago's Migrant Crisis", "University of Chicago Institute of Politics", "March 29, 2024",
     "Johannes participated in a screening and public conversation examining immigration detention, "
     "trauma, mental health, and Chicago's response to newly arrived immigrants.",
     "View the event",
     "https://politics.uchicago.edu/events/speaker-series/chicago-style-caged-dreams-the-trauma-of-chicagos-migrant-crisis"),
    ("Civic Cinema: Caged Dreams", "University of Illinois Chicago", "March 12, 2024",
     "Johannes joined a post-screening panel focused on immigration detention, mental health, and "
     "community advocacy.",
     "View the event",
     "https://live.today.uic.edu/events/civic-cinema-caged-dreams/"),
    ("Johannes Favi: Caged Dreams Discussion", "DePaul University", "May 28, 2025",
     "Johannes discussed the documentary, the long-term consequences of immigration detention, and the "
     "importance of trauma-informed support for immigrant communities.",
     "View the event",
     "https://events.depaul.edu/event/johannes-favi-caged-dreams-discussion"),
]

GOV_POLICY_PRESS = [
    ("Illinois Task Force on Black Immigrants Releases Final Report", "State of Illinois", "March 2, 2026",
     "Johannes was quoted as a member of the Illinois Task Force on Black Immigrants, addressing housing, "
     "opportunity, and the experiences of Black immigrant communities across Illinois.",
     "Read the release",
     "https://www.illinois.gov/news/release.html?releaseid=32254"),
]

AWARDS_PRESS = [
    ("Jeanne and Joseph Sullivan Human Rights Award", "National Immigrant Justice Center", "2021",
     "Johannes received the Jeanne and Joseph Sullivan Human Rights Award in recognition of his courage, "
     "leadership, and commitment to immigrant justice.",
     "Visit the National Immigrant Justice Center",
     "https://immigrantjustice.org/"),
]

DOCUMENTARY_LINKS = [
    ("Watch and learn more", "https://www.detentionwatchnetwork.org/caged-dreams"),
    ("View the official film listing", "https://filmfreeway.com/CagedDreams898"),
]

ADDITIONAL_MEDIA_TOPICS = [
    "Immigration detention and deportation", "Mental health and trauma",
    "Affordable housing and family stability", "Black immigrant experiences",
    "Public policy and civic leadership", "Community-based advocacy",
    "Immigrant integration and belonging",
]

AS_FEATURED_IN = [
    "WBEZ Chicago", "Truthout", "National Immigrant Justice Center", "Detention Watch Network",
    "Chicago Council on Global Affairs", "Obama Foundation Change Collective",
    "University of Chicago", "Maine Film Center",
]

SCREENINGS = ["University of Chicago", "UIC", "DePaul", "Princeton", "Boston University", "Maine Film Center"]

CURRENT_ROLES = [
    ("Founder & CEO", "Caged Dreams"),
    ("Director of Program Housing", "Bridge Communities"),
    ("Board Member", "Interfaith Community for Detained Immigrants"),
    ("Member", "Chicago New Arrivals Cabinet"),
]

PREVIOUS_ROLES = [
    ("Deputy Director", "Illinois Community for Displaced Immigrants"),
    ("Freedom Fellow", "Detention Watch Network"),
]

WHO_I_WORK_WITH = {
    "Government": ["City of Chicago agencies", "State of Illinois offices", "County government partners"],
    "Universities": ["University of Chicago", "University of Illinois Chicago", "DePaul University"],
    "Nonprofits": ["Bridge Communities", "Illinois Community for Displaced Immigrants", "Detention Watch Network"],
    "Foundations": ["Regional and national grantmaking foundations"],
    "Healthcare Organizations": ["Community and behavioral health providers"],
    "Faith Communities": ["Chicago Religious Leadership Network", "Interfaith Community for Detained Immigrants"],
    "Employers": ["Employers seeking immigration and workforce integration guidance"],
}

SPEAKING_ENGAGEMENTS = [
    ("2025", "DePaul University", "Caged Dreams Discussion"),
    ("2024", "University of Chicago", "Chicago Style"),
    ("2024", "University of Illinois Chicago", "Civic Cinema"),
    ("2024", "African Studies Association", "Annual Meeting"),
    ("2024", "DuPage Immigrant Integration Forum", "Featured Speaker"),
    ("2023", "DePaul University", "Sanctuary Panel"),
    ("2020", "U.S. House Judiciary Committee", "Congressional Testimony"),
]

TIMELINE = [
    ("2019", ["Immigration detention experience"]),
    ("2020", ["Congressional testimony", "National advocacy"]),
    ("2021", ["Illinois Way Forward advocacy", "Jeanne & Joseph Sullivan Human Rights Award"]),
    ("2022", ["Chicago migrant response leadership"]),
    ("2023", ["Caged Dreams documentary", "Founder of Caged Dreams", "Chicago New Arrivals Cabinet"]),
    ("2024", ["Civic Leadership Academy", "University speaking tour", "Catholic Lawyers Guild Special Service Award"]),
    (
        "2025 to 2026",
        [
            "Director of Program Housing, Bridge Communities",
            "Selected to serve on the Illinois Task Force on Black Immigrants",
            "Contributed to statewide policy recommendations",
            "Chicago Council Emerging Leader",
        ],
    ),
]

TESTIMONIALS = {
    "Government": [
        (
            "Johannes has a unique skill for facilitating connection and will continue to be a force for positive change.",
            "Jim Bennett",
            "Director, Illinois Department of Human Rights; Chair, Black Immigration Task Force",
        ),
        (
            "Johannes is a trusted leader whose character and commitment to others make a meaningful impact.",
            "Dr. Ariel G. Schwartz",
            "Executive Director, Global Leadership Programs, Chicago Council on Global Affairs",
        ),
    ],
    "Nonprofit": [
        (
            "Thank you for the contagious energy and valuable insights you shared. The way you connected "
            "with attendees made the symposium truly engaging.",
            "DePaul Migration Collaborative",
            "DePaul University",
        ),
        (
            "Johannes' story and advocacy work were incredibly powerful. Students left deeply inspired by his work.",
            "Sarah Sherman-Stokes",
            "Associate Director, Immigrants' Rights & Human Trafficking Program, Boston University School of Law",
        ),
    ],
    "Academic": [
        (
            "Students left curious and inspired after hearing your experiences in public service.",
            "Milvia Rodriguez",
            "Executive Program Director, University of Chicago Harris School of Public Policy",
        ),
        (
            "Your willingness to share your experiences and invest in students left a lasting impression on me.",
            "Jessica Perez",
            "Economics Honors & Political Science Graduate, DePaul University",
        ),
    ],
    "Speaking Engagements": [
        (
            "Your testimony and thoughtful presentation made a meaningful impact, and our attendees truly "
            "appreciated your contributions.",
            "Anne Lawrence",
            "DEIB Director-Elect, Junior League of Chicago",
        ),
    ],
}


def render_press_section(items, with_date=True):
    """Render a list of press citations, each with a real source link."""
    html = ""
    for entry in items:
        if with_date:
            headline, source, date, desc, link_text, link_url = entry
            meta = f"{source} &middot; {date}"
        else:
            headline, source, desc, link_text, link_url = entry
            meta = source
        html += (
            f"<div class='press-item'><div class='press-title'>{headline}</div>"
            f"<div class='press-meta'>{meta}</div>"
            f"<div class='press-desc'>{desc}</div>"
            f"<a class='press-link' href='{link_url}' target='_blank'>{link_text} &#8599;</a></div>"
        )
    st.markdown(html, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# HOME
# ----------------------------------------------------------------------------
if st.session_state.page == "Home":
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-inner">
                <div class="hero-text">
                    <div class="subhead">STRATEGIC CONSULTING</div>
                    <h1>Building Bridges Between Policy, Practice, and Human Experience</h1>
                    <p>Strategic consulting for governments, nonprofits, universities, healthcare systems,
                    foundations, and mission-driven organizations seeking practical, human-centered solutions
                    in immigration, housing, workforce development, organizational leadership, and public policy.</p>
                    <div class="hero-badges">
                        <span class="hero-badge">Founder, Caged Dreams</span>
                        <span class="hero-badge">Director, Bridge Communities</span>
                        <span class="hero-badge">Illinois Task Force on Black Immigrants</span>
                        <span class="hero-badge">Congressional Witness</span>
                    </div>
                </div>
                <div class="hero-photo">
                    <img src="{HERO_PHOTO_URI}" alt="Johannes Favi">
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Schedule a Consultation", key="home_cta1", use_container_width=True):
            go_to("Contact")
            st.rerun()
    with col2:
        if st.button("Explore Services", key="home_cta2", use_container_width=True):
            go_to("Services")
            st.rerun()

    # ---- Credibility strip ----
    st.markdown(
        "<div class='credibility-wrap'>"
        "<div class='credibility-label'>Trusted By Communities. Recognized By Institutions.</div>"
        "<span class='tag'>Founder & CEO, Caged Dreams</span>"
        "<span class='tag'>Director of Program Housing, Bridge Communities</span>"
        "<span class='tag'>Former Deputy Director, Illinois Community for Displaced Immigrants</span>"
        "<span class='tag'>Board Member, Interfaith Community for Detained Immigrants</span>"
        "<span class='tag'>Graduate, Civic Leadership Academy (University of Chicago)</span>"
        "<span class='tag'>Freedom Fellow, Detention Watch Network</span>"
        "</div>",
        unsafe_allow_html=True,
    )

    # ---- Trusted by Organizations Across Sectors ----
    st.markdown("<div class='section-label'>Trusted by Organizations Across Sectors</div>", unsafe_allow_html=True)
    st.write(
        "Johannes has collaborated with government agencies, universities, healthcare systems, "
        "nonprofit organizations, foundations, employers, and faith communities to strengthen "
        "public systems, expand opportunity, and improve outcomes for immigrant and underserved "
        "communities."
    )
    home_logo_html = "".join(
        f"<img src='{ORG_LOGO_URI_MAP[name]}' alt='{name}' title='{name}'>"
        for name in HOME_FEATURED_LOGOS
    )
    st.markdown(f"<div class='logo-strip'>{home_logo_html}</div>", unsafe_allow_html=True)
    st.write("")
    if st.button("View All Partners", key="home_view_partners"):
        go_to("Partners")
        st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Current Leadership ----
    st.markdown("<div class='section-label'>Current Leadership</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>What Johannes Is Doing Now</div>", unsafe_allow_html=True)
    cl_cols = st.columns(2)
    for i, (role, org) in enumerate(CURRENT_ROLES):
        with cl_cols[i % 2]:
            st.markdown(
                f"<div class='card' style='margin-bottom:0.6rem;'><h4 style='margin-bottom:0.15rem;'>{role}</h4>"
                f"<p>{org}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Featured Expertise ----
    st.markdown("<div class='section-label'>Featured Expertise</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Where I Add the Most Value</div>", unsafe_allow_html=True)
    st.markdown(
        "".join(
            f"<span class='tag'>{a}</span>"
            for a in [
                "Immigration policy & systems", "Housing & homelessness",
                "Workforce development", "Nonprofit strategy & leadership",
                "Public policy & government relations",
            ]
        ),
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("See All Services", key="home_see_services"):
        go_to("Services")
        st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Impact by the Numbers ----
    st.markdown("<div class='section-label'>Impact</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Selected Impact</div>", unsafe_allow_html=True)
    stats = [
        ("17+", "Years of Leadership"),
        ("&#127963;", "Statewide Policy Leadership"),
        ("25+", "Speaking Engagements"),
        ("10+", "Universities"),
        ("6+", "Awards & Fellowships"),
        ("5+", "National Media Features"),
        ("1", "Nationally Screened Documentary"),
    ]
    stat_cols = st.columns(3)
    for i, (number, label) in enumerate(stats):
        with stat_cols[i % 3]:
            st.markdown(
                f"<div class='stat-card'><div class='stat-number'>{number}</div>"
                f"<div class='stat-label'>{label}</div></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Featured Project: Caged Dreams ----
    fp_img_col1, fp_img_col2, fp_img_col3 = st.columns([1, 1.1, 1])
    with fp_img_col2:
        st.markdown(
            """
            <style>
                .st-key-home_flyer_wrap img {
                    border-radius: 10px;
                    box-shadow: 0 14px 32px rgba(16, 35, 63, 0.28);
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        with st.container(key="home_flyer_wrap"):
            st.image("assets/caged-dreams-flyer.jpg", use_container_width=True)

    st.write("")
    st.markdown(
        """
        <div class="featured-project">
            <div class="section-label">Featured Initiative</div>
            <h2>Caged Dreams</h2>
            <div class="quote">Transforming lived experience into policy change, education, and healing.</div>
            <p>Caged Dreams began as an award-recognized documentary exploring the mental health
            consequences of immigration detention. Today it has grown into a broader initiative dedicated
            to supporting newly arrived immigrants through mental health advocacy, education, storytelling,
            and community partnerships.</p>
            <p>The documentary has been screened at universities, community organizations, and public forums
            across the United States, creating dialogue about immigration detention, trauma, resilience,
            and systems change.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    fp_col1, fp_col2, fp_col3 = st.columns(3)
    with fp_col1:
        st.link_button("Visit Caged Dreams", CAGED_DREAMS_URL, use_container_width=True)
    with fp_col2:
        st.link_button("Watch Full Film", CAGED_DREAMS_FILM_URL, use_container_width=True)
    with fp_col3:
        if st.button("Learn More", key="home_learn_more", use_container_width=True):
            go_to("Media")
            st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Recognition & Public Leadership ----
    st.markdown("<div class='section-label'>Recognition & Public Leadership</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Selected Recognition</div>", unsafe_allow_html=True)
    st.markdown(
        "".join(f"<span class='tag-gold'>{title}</span>" for title, _ in RECOGNITION),
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- State Policy Leadership ----
    st.markdown("<div class='section-label'>State Policy Leadership</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'><h4>&#127482;&#127480; Illinois Task Force on Black Immigrants</h4>"
        "<p>Johannes Favi served as a member of the Illinois Task Force on Black Immigrants, a statewide "
        "advisory body established by the Illinois General Assembly to examine the experiences of Black "
        "immigrants and develop policy recommendations for Illinois. As Director of Program Housing at "
        "Bridge Communities, he contributed expertise on housing, immigrant integration, and community "
        "development to a report addressing education, healthcare, workforce development, economic "
        "opportunity, housing, and civic participation.</p></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    spl_col1, spl_col2 = st.columns(2)
    with spl_col1:
        st.link_button("Read Official State Report", TASK_FORCE_REPORT_URL, use_container_width=True)
    with spl_col2:
        if st.button("Public Policy Services", key="home_policy_services", use_container_width=True):
            go_to("Services")
            st.rerun()

    st.write("**Statewide Policy Leadership**")
    st.markdown(
        "<div class='checklist'>"
        + "".join(f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>" for a in TASK_FORCE_AREAS)
        + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Speaking preview ----
    st.markdown("<div class='section-label'>Speaking</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Featured Speaking</div>", unsafe_allow_html=True)
    st.markdown(
        "".join(f"<span class='tag'>{s}</span>" for s in [
            "University of Chicago", "University of Illinois Chicago", "DePaul University",
            "African Studies Association", "Illinois Black Immigrant Task Force", "Congressional Testimony",
        ]),
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("See Speaking", key="home_see_speaking"):
        go_to("Speaking")
        st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Testimonials preview ----
    st.markdown("<div class='section-label'>Testimonials</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>What Collaborators Say</div>", unsafe_allow_html=True)
    preview_testimonials = [entries[0] for entries in TESTIMONIALS.values()][:3]
    t_cols = st.columns(3)
    for i, (quote, name, role) in enumerate(preview_testimonials):
        with t_cols[i]:
            st.markdown(
                "<div class='testimonial-card'>"
                "<div class='quote-mark'>&ldquo;</div>"
                f"<div class='quote-text'>{quote}</div>"
                f"<div class='quote-attribution'>{name}</div>"
                f"<div class='quote-role'>{role}</div>"
                "</div>",
                unsafe_allow_html=True,
            )
    if st.button("See All Testimonials", key="home_see_testimonials"):
        go_to("Testimonials")
        st.rerun()

    # ---- Final CTA ----
    st.markdown(
        """
        <div class="cta-strip">
            <h2>Ready to Build Something Meaningful?</h2>
            <p>If your organization is navigating a complex challenge and needs a strategic partner
            who understands both systems and people, I would welcome the opportunity to connect.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Contact Me →", key="home_cta3"):
        go_to("Contact")
        st.rerun()

# ----------------------------------------------------------------------------
# ABOUT
# ----------------------------------------------------------------------------
elif st.session_state.page == "About":
    st.markdown("<div class='section-label'>About</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Executive Biography</div>", unsafe_allow_html=True)

    bio_col1, bio_col2 = st.columns([2, 1])
    with bio_col1:
        st.write(
            "Johannes Favi is a strategic consultant, nonprofit executive, human rights advocate, and "
            "community leader dedicated to building stronger systems that expand opportunity for "
            "underserved communities."
        )
        st.write(
            "His work spans immigration, housing, workforce development, nonprofit leadership, "
            "organizational strategy, public policy, and community engagement."
        )
        st.write(
            "Johannes previously served as Deputy Director of the Illinois Community for Displaced "
            "Immigrants (ICDI), where he led strategic planning, fundraising, organizational development, "
            "and statewide advocacy initiatives. He played an important role in campaigns supporting "
            "immigrant rights, including advocacy efforts surrounding the Illinois Way Forward Act, "
            "legislation that ended local government contracts for immigrant detention in Illinois."
        )
        st.write(
            "Today he serves as Director of Program Housing at Bridge Communities, where he continues "
            "advancing housing stability and long-term solutions for vulnerable populations."
        )
        st.write(
            "As founder of Caged Dreams, Johannes combines storytelling, research, policy, and community "
            "engagement to improve mental health access and strengthen support systems for immigrant "
            "communities."
        )
    with bio_col2:
        st.image("assets/johannes-favi-about.jpg", use_container_width=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Leadership ----
    st.markdown("<div class='section-label'>Leadership</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Current & Previous Roles</div>", unsafe_allow_html=True)

    st.markdown("<h4 style='color:#10233f;margin-bottom:0.6rem;'>Current</h4>", unsafe_allow_html=True)
    cur_cols = st.columns(2)
    for i, (role, org) in enumerate(CURRENT_ROLES):
        with cur_cols[i % 2]:
            st.markdown(
                f"<div class='card' style='margin-bottom:0.6rem;'><h4 style='margin-bottom:0.15rem;'>{role}</h4>"
                f"<p>{org}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<h4 style='color:#10233f;margin:1rem 0 0.6rem 0;'>Previous</h4>", unsafe_allow_html=True)
    prev_cols = st.columns(2)
    for i, (role, org) in enumerate(PREVIOUS_ROLES):
        with prev_cols[i % 2]:
            st.markdown(
                f"<div class='card' style='margin-bottom:0.6rem;'><h4 style='margin-bottom:0.15rem;'>{role}</h4>"
                f"<p>{org}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<h4 style='color:#10233f;margin:1.2rem 0 0.6rem 0;'>Public Leadership</h4>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'><h4>Illinois Task Force on Black Immigrants</h4>"
        "<p>Johannes served on the Illinois Task Force on Black Immigrants, established by the Illinois "
        "General Assembly to study barriers affecting Black immigrant communities and recommend policy "
        "solutions for state government.</p>"
        "<p style='margin-top:0.6rem;'>Working alongside leaders from government agencies, nonprofit "
        "organizations, universities, and community organizations, he contributed expertise in housing "
        "systems, immigrant integration, and community development.</p></div>",
        unsafe_allow_html=True,
    )
    st.write("**The Task Force's recommendations span:**")
    st.markdown(
        "<div class='checklist'>"
        + "".join(f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>" for a in TASK_FORCE_AREAS)
        + "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.link_button("Download State Report", TASK_FORCE_REPORT_URL)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Timeline ----
    st.markdown("<div class='section-label'>Journey</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Timeline</div>", unsafe_allow_html=True)
    for year, items in TIMELINE:
        items_html = "".join(f"<div>{item}</div>" for item in items)
        st.markdown(
            f"<div class='timeline-row'><div class='timeline-year'>{year}</div>"
            f"<div class='timeline-items'>{items_html}</div></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Recognition & Public Leadership ----
    st.markdown("<div class='section-label'>Recognition & Public Leadership</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Honors</div>", unsafe_allow_html=True)
    for title, desc in RECOGNITION:
        st.markdown(
            f"<div class='card' style='margin-bottom:0.6rem;'><h4 style='margin-bottom:0.15rem;'>{title}</h4>"
            f"<p>{desc}</p></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Who I Work With ----
    st.markdown("<div class='section-label'>Who I Work With</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Partners by Sector</div>", unsafe_allow_html=True)
    wiww_items = list(WHO_I_WORK_WITH.items())
    wiww_cols = st.columns(2)
    for i, (category, examples) in enumerate(wiww_items):
        with wiww_cols[i % 2]:
            st.markdown(
                f"<div class='category-card'><h4>{category}</h4><p>{', '.join(examples)}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Cross-Sector Leadership ----
    st.markdown("<div class='section-label'>Cross-Sector Leadership</div>", unsafe_allow_html=True)
    st.write(
        "Johannes has built partnerships across government, higher education, healthcare, "
        "nonprofit organizations, philanthropy, employers, and faith communities to strengthen "
        "public systems and improve community outcomes."
    )
    if st.button("Explore Partners", key="about_explore_partners"):
        go_to("Partners")
        st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Beyond the Work ----
    st.markdown(
        """
        <style>
            .st-key-family_photos img {
                border-radius: 8px;
                display: block;
            }
            .st-key-family_photos [data-testid="stHorizontalBlock"] {
                gap: 0.6rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div class='section-label'>Beyond the Work</div>", unsafe_allow_html=True)
    with st.container(key="family_photos"):
        pcol1, pcol2, pcol3 = st.columns(3, gap="small")
        with pcol1:
            st.image("assets/johannes-favi-family.jpg", use_container_width=True)
        with pcol2:
            st.image("assets/johannes-favi-family2.jpg", use_container_width=True)
        with pcol3:
            st.image("assets/johannes-favi-family3.jpg", use_container_width=True)
    st.write(
        "While policy and organizational leadership define Johannes' professional work, they are "
        "rooted in deeply personal values. Johannes is a proud father of three whose experiences as "
        "both a parent and an immigrant continue to shape his approach to leadership, service, and "
        "community building. He believes lasting systems change begins with listening, empathy, and "
        "investing in people's dignity."
    )
    st.write(
        "Outside of his professional work, Johannes enjoys outdoor activities, traveling, and "
        "exploring cultures around the world with his partner and kids. He is also a passionate home "
        "cook, known for bringing the bold, comforting flavors of his native Benin to the table and "
        "sharing them generously with family and friends."
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.write("**Interested in working together? Schedule a consultation.**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Discuss Your Project", key="about_cta1", use_container_width=True):
            go_to("Contact")
            st.rerun()
    with col2:
        st.link_button("Book a Strategy Call", f"mailto:{CONTACT_EMAIL}?subject=Strategy%20Call%20Request")

# ----------------------------------------------------------------------------
# PARTNERS
# ----------------------------------------------------------------------------
elif st.session_state.page == "Partners":
    st.markdown("<div class='section-label'>Organizations & Institutions</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Working Across Sectors</div>", unsafe_allow_html=True)
    st.write(
        "Johannes partners with organizations across government, higher education, healthcare, "
        "philanthropy, nonprofit leadership, and community development to design practical "
        "solutions that strengthen organizations and improve outcomes."
    )
    st.write(
        "His collaborative approach brings together diverse stakeholders to address complex "
        "challenges through strategy, policy, research, leadership, and community engagement."
    )
    st.caption(
        "The organizations below represent selected institutions with which Johannes has "
        "collaborated through leadership roles, advisory work, public policy initiatives, "
        "speaking engagements, research, coalition-building, or community partnerships. "
        "Inclusion does not imply endorsement or an ongoing formal partnership."
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    render_org_sector(
        "Government",
        "Collaborating with government leaders to strengthen public policy, improve service "
        "delivery, and expand opportunity for immigrant and underserved communities.",
        GOV_ORGS,
    )
    render_org_sector(
        "Nonprofits",
        "Partnering with nonprofit organizations to strengthen leadership, develop programs, "
        "improve organizational strategy, and build more equitable systems.",
        NONPROFIT_ORGS,
    )
    render_org_sector(
        "Healthcare",
        "Supporting healthcare providers working to improve access, integration, mental health, "
        "and community well-being.",
        HEALTHCARE_ORGS,
    )

    st.markdown("<div class='section-label'>Employers</div>", unsafe_allow_html=True)
    st.write(
        "Helping employers attract, retain, and successfully integrate international talent "
        "while building inclusive workplaces."
    )
    st.markdown(
        "".join(f"<span class='tag-gold'>{c}</span>" for c in EMPLOYER_CATEGORIES),
        unsafe_allow_html=True,
    )
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    render_org_sector(
        "Universities",
        "Collaborating with universities through public lectures, research partnerships, policy "
        "discussions, documentary screenings, and leadership development.",
        UNIVERSITY_ORGS,
    )
    render_org_sector(
        "Foundations",
        "Supporting philanthropic organizations seeking practical strategies to strengthen "
        "communities and expand opportunity.",
        FOUNDATION_ORGS,
    )
    render_org_sector(
        "Faith Communities",
        "Faith communities have played an important role throughout Johannes' career, serving as "
        "trusted partners in welcoming immigrants, advancing human dignity, and building stronger "
        "communities.",
        FAITH_ORGS,
    )

    st.write("**Interested in working together? Schedule a consultation.**")
    if st.button("Schedule a Consultation", key="partners_cta1"):
        go_to("Contact")
        st.rerun()

# ----------------------------------------------------------------------------
# SERVICES
# ----------------------------------------------------------------------------
elif st.session_state.page == "Services":
    st.markdown("<div id='services'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>What I Do</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Services Overview</div>", unsafe_allow_html=True)

    services = [
        ("Immigration & Workforce Integration",
         "Helping institutions attract, retain, and successfully integrate international talent."),
        ("Housing & Human Services",
         "Supporting organizations serving vulnerable populations through housing strategy, "
         "service delivery redesign, and program improvement."),
        ("Nonprofit Leadership & Organizational Development",
         "Helping mission-driven organizations strengthen leadership, align strategy, and build "
         "effective systems."),
        ("Public Policy & Government Advisory",
         "Advising statewide initiatives and translating community needs into practical policy "
         "recommendations, grounded in direct experience at the intersection of policy and "
         "implementation."),
        ("Research & Data Consulting",
         "Turning complex information into actionable insight through evaluation, reports, and "
         "data storytelling."),
        ("Community Engagement",
         "Building authentic relationships through listening sessions, facilitation, and "
         "partnership development."),
        ("Training, Speaking, and Advisory Services",
         "Offering customized workshops, keynote speaking, strategic facilitation, and ongoing "
         "advisory support."),
    ]

    st.markdown(
        """
        <style>
            .st-key-services_photo img {
                border-radius: 10px;
            }
            .st-key-services_photo {
                margin-bottom: 1rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(2)
    with cols[1]:
        with st.container(key="services_photo"):
            st.image("assets/johannes-favi-services.jpg", use_container_width=True)
    for i, (title, desc) in enumerate(services):
        with cols[i % 2]:
            st.markdown(
                f"<div class='card'><h4>{title}</h4><p>{desc}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Public Policy & Government Advisory</div>", unsafe_allow_html=True)
    st.write(
        "Organizations frequently seek guidance at the intersection of policy, implementation, and "
        "community engagement. Johannes brings experience advising statewide initiatives and "
        "translating community needs into practical policy recommendations."
    )
    st.write("**Selected experience includes**")
    policy_experience = [
        "Illinois Task Force on Black Immigrants",
        "Illinois Way Forward advocacy",
        "Congressional testimony",
        "Chicago New Arrivals Cabinet",
        "Housing systems strategy",
    ]
    st.markdown(
        "<div class='checklist'>"
        + "".join(f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>" for a in policy_experience)
        + "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.link_button("Read State Report", TASK_FORCE_REPORT_URL)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Who I Work With</div>", unsafe_allow_html=True)
    who_categories = ["Government", "Universities", "Healthcare", "Foundations", "Nonprofits", "Employers"]
    who_cols = st.columns(3)
    for i, category in enumerate(who_categories):
        with who_cols[i % 3]:
            if st.button(category, key=f"who_{category}", use_container_width=True):
                go_to("Partners")
                st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.write("**Need strategic guidance? Book a discovery call.**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Discuss Your Project", key="services_cta1", use_container_width=True):
            go_to("Contact")
            st.rerun()
    with col2:
        st.link_button("Request a Custom Engagement", f"mailto:{CONTACT_EMAIL}?subject=Custom%20Engagement%20Request")

# ----------------------------------------------------------------------------
# SPEAKING
# ----------------------------------------------------------------------------
elif st.session_state.page == "Speaking":
    st.markdown("<div class='section-label'>Speaking</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Speaking & Training</div>", unsafe_allow_html=True)
    st.write(
        "I am available for conferences, university lectures, leadership retreats, community "
        "forums, and executive convenings, bringing practical, research-grounded insight to "
        "audiences working across immigration, policy, housing, and nonprofit leadership."
    )
    st.image(
        "assets/johannes-favi-speaking.jpg",
        caption="Panelist, DePaul Migration Collaborative Symposium",
        use_container_width=True,
    )
    st.markdown(
        "<div class='card'><h4>Formats</h4><p>Keynotes, panel moderation, customized workshops, "
        "leadership retreats, and university lectures, tailored to your audience and objectives.</p></div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Featured Documentary</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'><h4>Caged Dreams</h4><p>Screenings and talks exploring immigration "
        "detention, mental health, and systems change, presented alongside the documentary "
        "Caged Dreams.</p></div>",
        unsafe_allow_html=True,
    )
    st.write("**Featured screenings**")
    st.markdown(
        "".join(f"<span class='tag'>{s}</span>" for s in SCREENINGS),
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Selected Speaking Engagements</div>", unsafe_allow_html=True)
    rows_html = "".join(
        f"<tr><td>{year}</td><td>{org}</td><td>{event}</td></tr>"
        for year, org, event in SPEAKING_ENGAGEMENTS
    )
    st.markdown(
        f"""
        <table class="speak-table">
            <thead><tr><th>Year</th><th>Organization</th><th>Event</th></tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.write("**Trusted By**")
    trusted_by_names = [
        "State of Illinois", "University of Chicago",
        "University of Chicago Harris School of Public Policy",
        "University of Illinois Chicago", "DePaul University",
    ]
    trusted_by_html = "".join(
        f"<img src='{ORG_LOGO_URI_MAP[name]}' alt='{name}' title='{name}'>" for name in trusted_by_names
    )
    st.markdown(f"<div class='logo-strip'>{trusted_by_html}</div>", unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.write("**Planning a conference or leadership retreat? Let's talk.**")
    st.link_button("Inquire About Speaking", f"mailto:{CONTACT_EMAIL}?subject=Speaking%20Inquiry")

# ----------------------------------------------------------------------------
# ADVISORY
# ----------------------------------------------------------------------------
elif st.session_state.page == "Advisory":
    st.markdown("<div class='section-label'>Advisory</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Advisory Support</div>", unsafe_allow_html=True)
    st.write(
        "I provide long-term advisory support and fractional executive leadership for organizations "
        "that need strategic guidance and steady leadership, whether navigating a specific "
        "initiative or building longer-term institutional capacity."
    )
    st.image("assets/johannes-favi-advisory.jpg", use_container_width=True)
    st.markdown(
        "<div class='card'><h4>Engagement Models</h4><p>Ongoing strategic advisory, fractional "
        "executive leadership, and project-based consulting for foundations, nonprofits, "
        "universities, and government partners.</p></div>",
        unsafe_allow_html=True,
    )
    st.link_button("Explore Advisory Services", f"mailto:{CONTACT_EMAIL}?subject=Advisory%20Services%20Inquiry")

# ----------------------------------------------------------------------------
# MEDIA
# ----------------------------------------------------------------------------
elif st.session_state.page == "Media":
    st.markdown("<div class='section-label'>Media & Press</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Coverage & Public Leadership</div>", unsafe_allow_html=True)
    st.write(
        "Johannes Favi has been featured in local and national media for his work on immigration "
        "detention, mental health, housing, public policy, and community advocacy. His story and "
        "leadership have appeared in news coverage, documentaries, university publications, "
        "government releases, interviews, and public-interest media."
    )
    st.write("**As Featured In**")
    st.markdown(
        "".join(f"<span class='tag'>{o}</span>" for o in AS_FEATURED_IN),
        unsafe_allow_html=True,
    )
    st.write("")
    st.write("**Institutional Recognition**")
    media_logo_names = ["University of Chicago", "University of Illinois Chicago", "DePaul University", "State of Illinois"]
    media_logo_html = "".join(
        f"<img src='{ORG_LOGO_URI_MAP[name]}' alt='{name}' title='{name}'>" for name in media_logo_names
    )
    st.markdown(f"<div class='logo-strip'>{media_logo_html}</div>", unsafe_allow_html=True)
    st.write("")

    st.markdown(
        """
        <style>
            .st-key-flyer_wrap img {
                border-radius: 10px;
                box-shadow: 0 14px 32px rgba(16, 35, 63, 0.28);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    flyer_col1, flyer_col2, flyer_col3 = st.columns([1, 1.4, 1])
    with flyer_col2:
        with st.container(key="flyer_wrap"):
            st.image("assets/caged-dreams-flyer.jpg", use_container_width=True)

    st.write("")
    trailer_col1, trailer_col2 = st.columns(2)
    with trailer_col1:
        st.link_button("Watch Full Film", CAGED_DREAMS_FILM_URL, use_container_width=True)
    with trailer_col2:
        st.link_button("Visit Caged Dreams", CAGED_DREAMS_URL, use_container_width=True)
    st.markdown(
        "<div style='text-align:center;margin-top:0.6rem;'>"
        + " &nbsp;&middot;&nbsp; ".join(
            f"<a class='press-link' href='{url}' target='_blank'>{text} &#8599;</a>"
            for text, url in DOCUMENTARY_LINKS
        )
        + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Synopsis</div>", unsafe_allow_html=True)
    st.write(
        "Caged Dreams began as an award-recognized documentary exploring the mental health "
        "consequences of immigration detention. Today it has grown into a broader initiative "
        "dedicated to supporting newly arrived immigrants through mental health advocacy, "
        "education, storytelling, and community partnerships."
    )
    st.write(
        "The documentary has been screened at universities, community organizations, and public "
        "forums across the United States, creating dialogue about immigration detention, trauma, "
        "resilience, and systems change."
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Screenings</div>", unsafe_allow_html=True)
    st.markdown(
        "".join(f"<span class='tag'>{s}</span>" for s in SCREENINGS),
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Awards</div>", unsafe_allow_html=True)
    st.markdown(
        "".join(f"<span class='tag-gold'>{title}</span>" for title, _ in RECOGNITION),
        unsafe_allow_html=True,
    )
    render_press_section(AWARDS_PRESS)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Featured Government Publication</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'><h4>Illinois General Assembly</h4>"
        "<p><strong>Report of the Task Force on Black Immigrants</strong></p>"
        "<p style='margin-top:0.5rem;'>Johannes served as a member of the statewide task force helping "
        "develop recommendations addressing housing, healthcare, workforce development, education, and "
        "civic participation.</p></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.link_button("Download Report", TASK_FORCE_REPORT_URL)
    render_press_section(GOV_POLICY_PRESS)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Featured Media</div>", unsafe_allow_html=True)
    render_press_section(PRESS_FEATURED)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Documentary Coverage</div>", unsafe_allow_html=True)
    render_press_section(DOCUMENTARY_COVERAGE)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Personal Story & Advocacy</div>", unsafe_allow_html=True)
    render_press_section(PERSONAL_STORY)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Profiles & Leadership Features</div>", unsafe_allow_html=True)
    render_press_section(PROFILES, with_date=False)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>University & Public Programs</div>", unsafe_allow_html=True)
    render_press_section(UNIVERSITY_PROGRAMS)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Additional Media</div>", unsafe_allow_html=True)
    st.write(
        "Johannes has also participated in television interviews, public discussions, podcasts, "
        "university programs, conferences, and community forums focused on:"
    )
    st.markdown(
        "<div class='checklist'>"
        + "".join(f"<span class='checklist-item'><span class='check'>&#10003;</span>{t}</span>" for t in ADDITIONAL_MEDIA_TOPICS)
        + "</div>",
        unsafe_allow_html=True,
    )
    st.caption("Additional archived interviews and appearances will be added as permanent links become publicly available.")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.write("**Media Inquiries**")
    st.write(
        "For interviews, speaking engagements, documentary screenings, panel discussions, or media "
        "inquiries, contact Johannes Favi, immigrant advocate, nonprofit leader, filmmaker, and "
        "public-policy practitioner."
    )
    st.write("**Looking for an expert source or speaker? Get in touch.**")
    if st.button("Contact Me", key="media_cta1"):
        go_to("Contact")
        st.rerun()

# ----------------------------------------------------------------------------
# IMPACT
# ----------------------------------------------------------------------------
elif st.session_state.page == "Impact":
    st.markdown("<div class='section-label'>Impact</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Turning Experience into Systems Change</div>", unsafe_allow_html=True)
    st.write(
        "Throughout his career, Johannes has worked at the intersection of public policy, nonprofit "
        "leadership, housing, mental health, and community engagement. His work has contributed to "
        "legislative advocacy, informed public policy, strengthened organizations, and helped build "
        "more inclusive systems for immigrants and underserved communities. Whether advising "
        "organizations, collaborating with government partners, or educating future leaders, his "
        "focus remains the same: creating practical, people-centered solutions that produce lasting "
        "impact."
    )
    st.image("assets/johannes-favi-impact.jpg", use_container_width=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Policy Change ----
    st.markdown("<div class='section-label'>Policy Change</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Advancing Policies that Strengthen Communities</div>", unsafe_allow_html=True)
    st.write(
        "Johannes has contributed to statewide advocacy efforts that helped shape conversations "
        "around immigrant rights, community integration, and equitable public policy. As former "
        "Deputy Director of the Illinois Community for Displaced Immigrants (ICDI), he worked "
        "alongside elected officials, nonprofit leaders, and community organizations in advocacy "
        "efforts surrounding the Illinois Way Forward Act, landmark legislation that ended local "
        "government contracts for immigrant detention facilities in Illinois."
    )
    st.write(
        "More recently, Johannes served on the Illinois Task Force on Black Immigrants, contributing "
        "to recommendations submitted to the Illinois General Assembly addressing housing, workforce "
        "development, healthcare, education, economic opportunity, and civic participation. His "
        "policy work reflects a commitment to ensuring that community voices are translated into "
        "practical, evidence-informed solutions."
    )
    st.write("**Featured Work**")
    st.markdown(
        "<div class='checklist'>"
        + "".join(
            f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>"
            for a in ["Illinois Way Forward advocacy", "Illinois Task Force on Black Immigrants",
                      "Public policy strategy", "Government advisory"]
        )
        + "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.link_button("Read the Illinois Task Force Report", TASK_FORCE_REPORT_URL)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Public Leadership ----
    st.markdown("<div class='section-label'>Public Leadership</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Leading Conversations That Influence Public Policy</div>", unsafe_allow_html=True)
    st.write(
        "Johannes has brought lived experience together with policy expertise to inform conversations "
        "at the local, state, and national levels. In 2020, he shared testimony before the U.S. House "
        "Judiciary Committee, providing firsthand insight into immigration detention during the "
        "COVID-19 pandemic and advocating for more humane approaches to immigration policy."
    )
    st.write(
        "Beyond legislative engagement, he has advised public officials, participated in statewide "
        "initiatives, and worked with government agencies and community partners to improve services "
        "for immigrant and underserved populations."
    )
    st.write("**Selected Leadership**")
    st.markdown(
        "<div class='checklist'>"
        + "".join(
            f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>"
            for a in ["Congressional testimony", "Chicago New Arrivals Cabinet",
                      "Illinois Task Force on Black Immigrants", "Cross-sector policy collaboration"]
        )
        + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Housing Systems ----
    st.markdown("<div class='section-label'>Housing Systems</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Building Housing Solutions That Support Long-Term Stability</div>", unsafe_allow_html=True)
    st.write(
        "Housing is more than shelter; it is the foundation for health, employment, education, and "
        "community participation. As Director of Program Housing at Bridge Communities, Johannes "
        "leads initiatives that strengthen housing access and long-term stability for vulnerable "
        "individuals and families."
    )
    st.write(
        "His experience spans emergency response, housing strategy, systems coordination, immigrant "
        "integration, and program development. By connecting housing providers, nonprofit "
        "organizations, government agencies, and community partners, he helps create practical "
        "solutions that address both immediate needs and long-term outcomes."
    )
    st.write("**Areas of Focus**")
    st.markdown(
        "<div class='checklist'>"
        + "".join(
            f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>"
            for a in ["Housing strategy", "Homelessness response", "Program development",
                      "Systems coordination", "Community partnerships"]
        )
        + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Mental Health ----
    st.markdown("<div class='section-label'>Mental Health</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Promoting Healing Through Storytelling and Advocacy</div>", unsafe_allow_html=True)
    st.write(
        "Following his own experience with immigration detention, Johannes founded Caged Dreams, an "
        "initiative dedicated to raising awareness of the mental health impacts of detention and "
        "displacement while promoting healing through education, advocacy, and community support."
    )
    st.write(
        "The project began with the documentary Caged Dreams, which has been screened at "
        "universities, community organizations, and public forums throughout the United States. "
        "Today, Caged Dreams continues to foster dialogue around trauma, resilience, and immigrant "
        "mental health while working to expand access to culturally responsive support for newly "
        "arrived communities."
    )
    st.write("**Featured Initiative**")
    st.markdown(
        "<div class='checklist'>"
        + "".join(
            f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>"
            for a in ["Founder & CEO, Caged Dreams", "Documentary filmmaker",
                      "Mental health advocacy", "Community education"]
        )
        + "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    mh_col1, mh_col2 = st.columns(2)
    with mh_col1:
        st.link_button("Visit Caged Dreams", CAGED_DREAMS_URL, use_container_width=True)
    with mh_col2:
        st.link_button("Watch Full Film", CAGED_DREAMS_FILM_URL, use_container_width=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Public Education ----
    st.markdown("<div class='section-label'>Public Education</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Translating Complex Issues into Actionable Knowledge</div>", unsafe_allow_html=True)
    st.write(
        "Johannes is an experienced speaker and educator who has presented to universities, "
        "professional associations, nonprofit organizations, government agencies, and community "
        "groups across the United States."
    )
    st.write(
        "His presentations combine lived experience, policy expertise, research, and practical "
        "leadership to help audiences better understand immigration, housing, organizational "
        "leadership, public policy, and community engagement."
    )
    st.write("**Selected speaking engagements include**")
    st.markdown(
        "".join(f"<span class='tag'>{s}</span>" for s in [
            "University of Chicago", "University of Illinois Chicago", "DePaul University",
            "African Studies Association Annual Meeting", "DuPage Immigrant Integration Forum",
            "Civic Cinema Series", "Community leadership forums",
        ]),
        unsafe_allow_html=True,
    )
    st.write("")
    st.write(
        "Whether delivering a keynote, facilitating a workshop, or leading a policy discussion, "
        "Johannes focuses on helping audiences move from awareness to action."
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Community Building ----
    st.markdown("<div class='section-label'>Community Building</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Creating Partnerships That Strengthen Communities</div>", unsafe_allow_html=True)
    st.write(
        "Meaningful change requires collaboration across sectors. Throughout his career, Johannes has "
        "built partnerships connecting nonprofits, universities, government agencies, healthcare "
        "organizations, foundations, faith communities, and grassroots leaders around shared goals."
    )
    st.markdown(
        "<div class='checklist'>"
        + "".join(
            f"<span class='checklist-item'><span class='check'>&#10003;</span>{a}</span>"
            for a in ["Government", "Universities", "Healthcare", "Foundations",
                      "Faith Communities", "Employers", "Community Organizations"]
        )
        + "</div>",
        unsafe_allow_html=True,
    )
    st.write(
        "By bringing together diverse perspectives and building trust across institutions, Johannes "
        "helps organizations move beyond isolated initiatives toward coordinated, sustainable "
        "solutions that create lasting community impact."
    )
    st.write("")
    if st.button("View Partner Network", key="impact_view_partners"):
        go_to("Partners")
        st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Closing ----
    st.markdown("<div class='section-label'>Closing</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Creating Impact Through Partnership</div>", unsafe_allow_html=True)
    st.write(
        "Every organization faces complex challenges that require thoughtful leadership, practical "
        "strategy, and meaningful collaboration. Johannes partners with mission-driven organizations "
        "to strengthen systems, develop effective strategies, and translate ideas into measurable "
        "results."
    )
    st.write(
        "Whether supporting public agencies, nonprofit organizations, universities, healthcare "
        "systems, or foundations, his approach combines policy expertise, organizational leadership, "
        "and lived experience to help clients build stronger communities and achieve lasting impact."
    )
    st.write("")
    close_col1, close_col2 = st.columns(2)
    with close_col1:
        if st.button("Schedule a Consultation", key="impact_cta1", use_container_width=True):
            go_to("Contact")
            st.rerun()
    with close_col2:
        if st.button("Explore Services", key="impact_cta2", use_container_width=True):
            go_to("Services")
            st.rerun()

# ----------------------------------------------------------------------------
# TESTIMONIALS
# ----------------------------------------------------------------------------
elif st.session_state.page == "Testimonials":
    st.markdown("<div class='section-label'>Testimonials & Endorsements</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>What Collaborators Say</div>", unsafe_allow_html=True)
    st.write(
        "Endorsements from university faculty, nonprofit leaders, government officials, "
        "collaborators, and conference organizers."
    )

    for category, entries in TESTIMONIALS.items():
        st.markdown(f"<div class='section-label' style='margin-top:1.4rem;'>{category}</div>", unsafe_allow_html=True)
        t_cols = st.columns(len(entries) if len(entries) > 1 else 1)
        for i, (quote, name, role) in enumerate(entries):
            with t_cols[i]:
                st.markdown(
                    "<div class='testimonial-card'>"
                    "<div class='quote-mark'>&ldquo;</div>"
                    f"<div class='quote-text'>{quote}</div>"
                    f"<div class='quote-attribution'>{name}</div>"
                    f"<div class='quote-role'>{role}</div>"
                    "</div>",
                    unsafe_allow_html=True,
                )

# ----------------------------------------------------------------------------
# CONTACT
# ----------------------------------------------------------------------------
elif st.session_state.page == "Contact":
    st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Get in Touch</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Let's Talk About Your Project</div>", unsafe_allow_html=True)
    st.write(
        "Send a message below, or email directly at "
        f"[{CONTACT_EMAIL}](mailto:{CONTACT_EMAIL})."
    )

    # Real HTML form posted to FormSubmit, delivers straight to the inbox
    # above with no backend or email credentials required.
    contact_form_html = f"""
    <style>
        body {{ font-family: 'Inter', sans-serif; margin: 0; }}
        .cf-input, .cf-textarea {{
            width: 100%;
            padding: 0.7rem 0.9rem;
            margin-bottom: 0.9rem;
            border: 1px solid #d8d3c6;
            border-radius: 6px;
            font-size: 0.95rem;
            font-family: 'Inter', sans-serif;
            box-sizing: border-box;
        }}
        .cf-textarea {{ resize: vertical; min-height: 110px; }}
        .cf-label {{
            font-size: 0.82rem;
            font-weight: 600;
            color: #10233f;
            margin-bottom: 0.3rem;
            display: block;
        }}
        .cf-submit {{
            background-color: #b8924a;
            color: #10233f;
            border: none;
            padding: 0.65rem 1.6rem;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
        }}
        .cf-submit:hover {{ background-color: #a37d38; color: #ffffff; }}
        .cf-row {{ display: flex; gap: 1rem; }}
        .cf-row > div {{ flex: 1; }}

        @media (max-width: 480px) {{
            .cf-row {{ flex-direction: column; gap: 0; }}
            .cf-input, .cf-textarea {{ font-size: 16px; }}
        }}
        .cf-status {{
            display: none;
            margin-top: 0.8rem;
            padding: 0.7rem 0.9rem;
            border-radius: 6px;
            font-size: 0.9rem;
        }}
        .cf-status.ok {{ background: #e7f4ea; color: #1e6b34; border: 1px solid #bfe3c8; }}
        .cf-status.err {{ background: #fbeaea; color: #99281f; border: 1px solid #f0c4c1; }}
        .cf-submit[disabled] {{ opacity: 0.6; cursor: default; }}
    </style>
    <form id="cf-form">
        <input type="hidden" name="_subject" value="New inquiry: Johannes Favi consulting site">
        <input type="hidden" name="_template" value="table">

        <div class="cf-row">
            <div>
                <label class="cf-label">Full Name</label>
                <input class="cf-input" type="text" name="Name" required>
            </div>
            <div>
                <label class="cf-label">Email Address</label>
                <input class="cf-input" type="email" name="Email" required>
            </div>
        </div>

        <label class="cf-label">Organization</label>
        <input class="cf-input" type="text" name="Organization">

        <label class="cf-label">How can I help?</label>
        <textarea class="cf-textarea" name="Message" required></textarea>

        <button class="cf-submit" type="submit" id="cf-submit-btn">Send Message</button>
        <div class="cf-status" id="cf-status"></div>
    </form>

    <script>
        const form = document.getElementById('cf-form');
        const btn = document.getElementById('cf-submit-btn');
        const status = document.getElementById('cf-status');

        form.addEventListener('submit', function (e) {{
            e.preventDefault();
            btn.disabled = true;
            btn.textContent = 'Sending...';
            status.style.display = 'none';

            const data = new FormData(form);

            fetch('https://formsubmit.co/ajax/{CONTACT_EMAIL}', {{
                method: 'POST',
                headers: {{ 'Accept': 'application/json' }},
                body: data
            }})
            .then(function (res) {{ return res.json().then(function (json) {{ return {{ ok: res.ok, json: json }}; }}); }})
            .then(function (result) {{
                if (result.ok && result.json && result.json.success !== 'false') {{
                    status.className = 'cf-status ok';
                    status.textContent = "Message sent. Thank you, I'll be in touch soon.";
                    form.reset();
                }} else {{
                    status.className = 'cf-status err';
                    status.textContent = 'Something went wrong sending this, please email '
                        + '{CONTACT_EMAIL}' + ' directly. (' + JSON.stringify(result.json) + ')';
                }}
                status.style.display = 'block';
            }})
            .catch(function (err) {{
                status.className = 'cf-status err';
                status.textContent = 'Network error, please email {CONTACT_EMAIL} directly instead. (' + err + ')';
                status.style.display = 'block';
            }})
            .finally(function () {{
                btn.disabled = false;
                btn.textContent = 'Send Message';
            }});
        }});
    </script>
    """
    with st.container():
        st.markdown("<div class='contact-form-wrap'>", unsafe_allow_html=True)
        components.html(contact_form_html, height=470, scrolling=False)
        st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center;color:#9aa0a8;font-size:0.82rem;padding-bottom:0.6rem;max-width:640px;margin:0 auto;'>"
    "Working with organizations across government, higher education, healthcare, nonprofit "
    "leadership, philanthropy, employers, and community organizations.</div>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<div style='text-align:center;color:#9aa0a8;font-size:0.85rem;padding-bottom:1rem;'>"
    f"© 2026 Johannes Favi &nbsp;·&nbsp; Strategic Consulting &nbsp;·&nbsp; "
    f"<a href='mailto:{CONTACT_EMAIL}' style='color:#9aa0a8;'>{CONTACT_EMAIL}</a></div>",
    unsafe_allow_html=True,
)
