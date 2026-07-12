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
            margin-bottom: 2.5rem;
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
            font-size: 2.6rem;
            line-height: 1.25;
            margin-bottom: 0.8rem;
        }
        .hero .subhead {
            font-size: 1.15rem;
            color: var(--gold);
            font-weight: 500;
            margin-bottom: 1.2rem;
        }
        .hero p {
            font-size: 1.02rem;
            color: #e6e9ef;
            max-width: 720px;
            line-height: 1.7;
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

        .contact-form-wrap iframe {
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# NAVIGATION
# ----------------------------------------------------------------------------
PAGES = ["Home", "About", "Services", "Speaking", "Advisory", "Contact"]
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
                    <p>Strategic consulting for organizations working to strengthen communities, improve systems,
                    and expand opportunity for immigrants and other underserved populations.</p>
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

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Introduction</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>A Practical, People-Centered Approach</div>", unsafe_allow_html=True)
    st.write(
        "I help governments, nonprofits, universities, healthcare systems, and businesses create "
        "practical, people-centered solutions that lead to measurable impact. With more than 17 years "
        "of executive leadership experience, I bring expertise in immigration, housing, workforce "
        "development, nonprofit strategy, community engagement, and policy implementation."
    )
    st.write(
        "I combine executive leadership, policy expertise, research, and lived experience to help "
        "organizations turn complex challenges into clear, actionable strategies. My approach is "
        "collaborative, practical, and grounded in the belief that systems can be more effective, "
        "more compassionate, and more equitable."
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Why Work With Me</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>From Complexity to Clarity</div>", unsafe_allow_html=True)
    st.write(
        "I bring a human-centered and highly practical approach to every engagement. Clients work "
        "with me when they need a trusted thought partner, an experienced facilitator, or a strategic "
        "advisor who can help move from complexity to clarity and from ideas to implementation."
    )
    points = [
        ("17+ years of executive leadership experience", "https://www.linkedin.com/in/johannesfavi/"),
        ("Expertise across policy, systems, and organizational strategy", None),
        (
            "Strong background in research, planning, and implementation",
            "https://www.ilga.gov/Documents/Reports/ReportsSubmitted/6390RSGAEmail14131RSGAAttachReport%20of%20the%20Task%20Force%20on%20Black%20Immigrants_12-29-2025.pdf",
        ),
        ("Deep commitment to equity, access, and community impact", None),
    ]
    for text, url in points:
        label = f"<a href='{url}' target='_blank' style='color:inherit;text-decoration:underline;text-decoration-color:#c9a86a;'>{text}</a>" if url else text
        st.markdown(f"<div class='stat-line'>&#9670;&nbsp;&nbsp;{label}</div>", unsafe_allow_html=True)

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
    st.markdown("<div class='section-title'>Who I Work With</div>", unsafe_allow_html=True)
    st.write(
        "I partner with foundations, nonprofits, universities, healthcare systems, government "
        "agencies, employers, philanthropic institutions, and cross-sector teams committed to "
        "strengthening communities and improving outcomes."
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Career Highlights</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Selected Experience</div>", unsafe_allow_html=True)
    highlights = [
        ("Director of Program Housing", "Bridge Communities", "Oct 2025 - Present", None),
        ("Advisor, Immigrant, Migrant & Refugee Rights", "Chicago Mayor's Office", "May 2024 - Present", None),
        (
            "Appointed Member, Black Immigrants Task Force",
            "Office of the Governor of Illinois",
            "Jan 2025 - Dec 2025",
            "https://www.ilga.gov/Documents/Reports/ReportsSubmitted/6390RSGAEmail14131RSGAAttachReport%20of%20the%20Task%20Force%20on%20Black%20Immigrants_12-29-2025.pdf",
        ),
        ("Deputy Director & Board Member", "Illinois Community for Displaced Immigrants (ICDI)", "May 2020 - Apr 2025", None),
        ("Emerging Leaders Fellow", "Chicago Council on Global Affairs", "Dec 2024 - Nov 2025", None),
        ("Inaugural Freedom Fellow", "Detention Watch Network", "Oct 2023 - Sep 2024", None),
        ("Immigration Advisory Council Member", "Cook County State's Attorney's Office", "Jan 2024 - Dec 2024", None),
    ]
    for role, org, dates, link in highlights:
        title_html = (
            f"<a href='{link}' target='_blank' style='color:#10233f;text-decoration:underline;"
            f"text-decoration-color:#c9a86a;'>{role}</a>"
            if link else role
        )
        extra = "  ·  <span style='color:#b8924a;'>Read the report ↗</span>" if link else ""
        st.markdown(
            f"<div class='card' style='margin-bottom:0.6rem;'>"
            f"<h4 style='margin-bottom:0.15rem;'>{title_html}{extra}</h4>"
            f"<p style='margin-bottom:0.1rem;'>{org}</p>"
            f"<p style='color:#9aa0a8;font-size:0.82rem;margin:0;'>{dates}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Signature Expertise</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Areas of Focus</div>", unsafe_allow_html=True)
    areas = [
        "Immigration policy & systems", "Workforce development", "Housing & homelessness",
        "Community health", "Mental health access", "Nonprofit strategy",
        "Organizational leadership", "Public policy", "Economic mobility",
        "Cross-sector partnerships", "International talent retention",
        "Research & policy analysis", "Program design & evaluation",
        "Community engagement", "Human-centered leadership",
    ]
    st.markdown(
        "".join([f"<span class='tag'>{a}</span>" for a in areas]),
        unsafe_allow_html=True,
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

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
        "Johannes is a proud father of three. He enjoys outdoor activities, traveling, and "
        "exploring cultures around the world with his partner and kids. He is also a passionate "
        "home cook, known for bringing the bold, comforting flavors of his native Benin to the "
        "table and sharing them generously with family and friends."
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
        components.html(contact_form_html, height=400, scrolling=False)
        st.markdown("</div>", unsafe_allow_html=True)

    st.caption(
        "Note: the first message sent from a given URL triggers a one-time confirmation email "
        f"from FormSubmit to {CONTACT_EMAIL}; it must be confirmed once (check spam/promotions "
        "too) before messages start arriving normally. This applies separately to localhost and "
        "to your deployed site, since FormSubmit ties activation to the sending domain."
    )

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
