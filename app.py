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


def _img_to_data_uri(path: str) -> str:
    """Read a local image file and return it as a base64 data URI,
    so it can be embedded directly inside an HTML/markdown block."""
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"


HERO_PHOTO_URI = _img_to_data_uri("assets/johannes-favi-hero.jpg")

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

        /* Media banner */
        .media-banner {
            background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
            border-radius: 14px;
            padding: 2.6rem;
            text-align: center;
            color: #ffffff;
            margin-bottom: 2rem;
        }
        .media-banner h1 { color: #ffffff; margin-bottom: 0.4rem; }
        .media-banner p { color: var(--gold); font-size: 1.05rem; margin: 0; }

        .placeholder-card {
            background: #f7f5f0;
            border: 1px dashed #d8d0bd;
            border-radius: 10px;
            padding: 1.3rem 1.4rem;
            color: var(--gray);
            font-size: 0.92rem;
            margin-bottom: 0.8rem;
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
            .card {
                padding: 1.1rem 1.2rem;
            }
            .featured-project {
                padding: 1.6rem 1.4rem;
            }
            .media-banner {
                padding: 1.8rem 1.3rem;
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
PAGES = ["Home", "About", "Services", "Speaking", "Advisory", "Media", "Testimonials", "Contact"]
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
    ("Chicago City Council Recognition", "Recognized during National Hispanic Heritage Month by Alderman Andre Vasquez."),
    ("Freedom Fellow, Detention Watch Network", "National leadership fellowship advancing alternatives to immigration detention."),
    ("Chicago Council Emerging Leader", "Civic Leadership Academy, University of Chicago Harris School of Public Policy."),
]

SCREENINGS = ["University of Chicago", "UIC", "DePaul", "Princeton", "Boston University", "Maine Film Center"]

TESTIMONIAL_CATEGORIES = [
    ("Government", 2),
    ("Nonprofit", 2),
    ("Academic", 2),
    ("Speaking Engagements", 1),
]

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

    # ---- Recognition ----
    st.markdown("<div class='section-label'>Recognition</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Selected Recognition</div>", unsafe_allow_html=True)
    st.markdown(
        "".join(f"<span class='tag-gold'>{title}</span>" for title, _ in RECOGNITION),
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
    t_cols = st.columns(3)
    for i in range(3):
        with t_cols[i]:
            st.markdown(
                f"<div class='placeholder-card'>Testimonial {i + 1}<br><em>Coming soon</em></div>",
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

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Leadership ----
    st.markdown("<div class='section-label'>Leadership</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Current & Previous Roles</div>", unsafe_allow_html=True)

    st.markdown("<h4 style='color:#10233f;margin-bottom:0.6rem;'>Current</h4>", unsafe_allow_html=True)
    current_roles = [
        ("Founder & CEO", "Caged Dreams"),
        ("Director of Program Housing", "Bridge Communities"),
        ("Board Member", "Interfaith Community for Detained Immigrants"),
        ("Member", "Chicago New Arrivals Cabinet"),
    ]
    cur_cols = st.columns(2)
    for i, (role, org) in enumerate(current_roles):
        with cur_cols[i % 2]:
            st.markdown(
                f"<div class='card' style='margin-bottom:0.6rem;'><h4 style='margin-bottom:0.15rem;'>{role}</h4>"
                f"<p>{org}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<h4 style='color:#10233f;margin:1rem 0 0.6rem 0;'>Previous</h4>", unsafe_allow_html=True)
    previous_roles = [
        ("Deputy Director", "Illinois Community for Displaced Immigrants"),
        ("Freedom Fellow", "Detention Watch Network"),
    ]
    prev_cols = st.columns(2)
    for i, (role, org) in enumerate(previous_roles):
        with prev_cols[i % 2]:
            st.markdown(
                f"<div class='card' style='margin-bottom:0.6rem;'><h4 style='margin-bottom:0.15rem;'>{role}</h4>"
                f"<p>{org}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Awards & Recognition ----
    st.markdown("<div class='section-label'>Awards & Recognition</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Honors</div>", unsafe_allow_html=True)
    for title, desc in RECOGNITION:
        st.markdown(
            f"<div class='card' style='margin-bottom:0.6rem;'><h4 style='margin-bottom:0.15rem;'>{title}</h4>"
            f"<p>{desc}</p></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ---- Collaborations ----
    st.markdown("<div class='section-label'>Collaborations</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Selected Collaborations</div>", unsafe_allow_html=True)
    st.write(
        "Johannes has collaborated with government agencies, universities, nonprofits, foundations, "
        "and community organizations to improve outcomes for immigrant and underserved communities."
    )
    collaborations = [
        "Bridge Communities", "Illinois Community for Displaced Immigrants",
        "Interfaith Community for Detained Immigrants", "Detention Watch Network",
        "National Immigrant Justice Center", "Illinois Coalition for Immigrant and Refugee Rights",
        "Midwest Immigration Bond Fund", "Simmons Center for Global Chicago",
        "University of Chicago", "University of Illinois Chicago", "DePaul University",
        "Lewis University", "Santa Clara University", "Loyola School of New York",
        "Chicago Religious Leadership Network", "Chicago Refugee Coalition", "6000 Moms",
        "Progressives for Change", "Elmhurst Rotary Club", "Darst Center", "Save the Children",
    ]
    st.markdown(
        "".join(f"<span class='tag'>{c}</span>" for c in collaborations),
        unsafe_allow_html=True,
    )

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
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Discuss Your Project", key="about_cta1", use_container_width=True):
            go_to("Contact")
            st.rerun()
    with col2:
        st.link_button("Book a Strategy Call", f"mailto:{CONTACT_EMAIL}?subject=Strategy%20Call%20Request")

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
        ("Public Policy & Government Relations",
         "Translating research into policy action through analysis, advocacy strategy, and "
         "stakeholder engagement."),
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

    cols = st.columns(2)
    for i, (title, desc) in enumerate(services):
        with cols[i % 2]:
            st.markdown(
                f"<div class='card'><h4>{title}</h4><p>{desc}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
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
    st.markdown(
        """
        <div class="media-banner">
            <h1>Caged Dreams</h1>
            <p>A documentary on immigration detention, mental health, and healing.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    trailer_col1, trailer_col2 = st.columns(2)
    with trailer_col1:
        st.link_button("Watch Full Film", CAGED_DREAMS_FILM_URL, use_container_width=True)
    with trailer_col2:
        st.link_button("Visit Caged Dreams", CAGED_DREAMS_URL, use_container_width=True)

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

# ----------------------------------------------------------------------------
# TESTIMONIALS
# ----------------------------------------------------------------------------
elif st.session_state.page == "Testimonials":
    st.markdown("<div class='section-label'>Testimonials & Endorsements</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>What Collaborators Say</div>", unsafe_allow_html=True)
    st.write(
        "Endorsements from university faculty, nonprofit leaders, government officials, "
        "collaborators, and conference organizers will be added here as they are collected."
    )

    counter = 1
    for category, count in TESTIMONIAL_CATEGORIES:
        st.markdown(f"<div class='section-label' style='margin-top:1.4rem;'>{category}</div>", unsafe_allow_html=True)
        t_cols = st.columns(count if count > 1 else 1)
        for i in range(count):
            with t_cols[i]:
                st.markdown(
                    f"<div class='placeholder-card'>Testimonial {counter}<br><em>Coming soon</em></div>",
                    unsafe_allow_html=True,
                )
            counter += 1

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
    f"<div style='text-align:center;color:#9aa0a8;font-size:0.85rem;padding-bottom:1rem;'>"
    f"© 2026 Johannes Favi &nbsp;·&nbsp; Strategic Consulting &nbsp;·&nbsp; "
    f"<a href='mailto:{CONTACT_EMAIL}' style='color:#9aa0a8;'>{CONTACT_EMAIL}</a></div>",
    unsafe_allow_html=True,
)
