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
            padding: 4rem 3rem;
            border-radius: 14px;
            color: #ffffff;
            margin-bottom: 2.5rem;
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
            padding: 3rem;
            text-align: center;
            color: #ffffff;
            margin-top: 2.5rem;
        }
        .cta-strip h2 { color: #ffffff; }
        .cta-strip p { color: #d7dce5; margin-bottom: 1.5rem; }

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
st.markdown(
    "<div style='display:flex;justify-content:space-between;align-items:center;padding:0.5rem 0 1.2rem 0;'>"
    "<div style='font-family:Playfair Display, serif;font-size:1.4rem;font-weight:700;color:#10233f;'>Johannes Favi</div>"
    "</div>",
    unsafe_allow_html=True,
)

tabs = st.tabs(["Home", "About", "Services", "Speaking", "Advisory", "Contact"])

# ----------------------------------------------------------------------------
# HOME
# ----------------------------------------------------------------------------
with tabs[0]:
    st.markdown(
        """
        <div class="hero">
            <div class="subhead">STRATEGIC CONSULTING</div>
            <h1>Building Bridges Between Policy, Practice, and Human Experience</h1>
            <p>Strategic consulting for organizations working to strengthen communities, improve systems,
            and expand opportunity for immigrants and other underserved populations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Schedule a Consultation", key="home_cta1"):
            st.session_state["_scroll_contact"] = True
    with col2:
        st.link_button("Explore Services", "#services")

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
    for point in [
        "17+ years of executive leadership experience",
        "Expertise across policy, systems, and organizational strategy",
        "Strong background in research, planning, and implementation",
        "Deep commitment to equity, access, and community impact",
    ]:
        st.markdown(f"<div class='stat-line'>&#9670;&nbsp;&nbsp;{point}</div>", unsafe_allow_html=True)

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
    st.link_button("Contact Me →", "#contact")

# ----------------------------------------------------------------------------
# ABOUT
# ----------------------------------------------------------------------------
with tabs[1]:
    st.markdown("<div class='section-label'>About</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Who I Work With</div>", unsafe_allow_html=True)
    st.write(
        "I partner with foundations, nonprofits, universities, healthcare systems, government "
        "agencies, employers, philanthropic institutions, and cross-sector teams committed to "
        "strengthening communities and improving outcomes."
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
    col1, col2 = st.columns(2)
    with col1:
        st.button("Discuss Your Project", key="about_cta1")
    with col2:
        st.link_button("Book a Strategy Call", f"mailto:{CONTACT_EMAIL}?subject=Strategy%20Call%20Request")

# ----------------------------------------------------------------------------
# SERVICES
# ----------------------------------------------------------------------------
with tabs[2]:
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
        st.button("View All Services", key="services_cta1")
    with col2:
        st.link_button("Request a Custom Engagement", f"mailto:{CONTACT_EMAIL}?subject=Custom%20Engagement%20Request")

# ----------------------------------------------------------------------------
# SPEAKING
# ----------------------------------------------------------------------------
with tabs[3]:
    st.markdown("<div class='section-label'>Speaking</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Speaking & Training</div>", unsafe_allow_html=True)
    st.write(
        "I am available for conferences, university lectures, leadership retreats, community "
        "forums, and executive convenings — bringing practical, research-grounded insight to "
        "audiences working across immigration, policy, housing, and nonprofit leadership."
    )
    st.markdown(
        "<div class='card'><h4>Formats</h4><p>Keynotes, panel moderation, customized workshops, "
        "leadership retreats, and university lectures — tailored to your audience and objectives.</p></div>",
        unsafe_allow_html=True,
    )
    st.link_button("Inquire About Speaking", f"mailto:{CONTACT_EMAIL}?subject=Speaking%20Inquiry")

# ----------------------------------------------------------------------------
# ADVISORY
# ----------------------------------------------------------------------------
with tabs[4]:
    st.markdown("<div class='section-label'>Advisory</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Advisory Support</div>", unsafe_allow_html=True)
    st.write(
        "I provide long-term advisory support and fractional executive leadership for organizations "
        "that need strategic guidance and steady leadership — whether navigating a specific "
        "initiative or building longer-term institutional capacity."
    )
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
with tabs[5]:
    st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Get in Touch</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Let's Talk About Your Project</div>", unsafe_allow_html=True)
    st.write(
        "Send a message below, or email directly at "
        f"[{CONTACT_EMAIL}](mailto:{CONTACT_EMAIL})."
    )

    # Real HTML form posted to FormSubmit — delivers straight to the inbox
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
        <input type="hidden" name="_subject" value="New inquiry — Johannes Favi consulting site">
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
                    status.textContent = "Message sent — thank you. I'll be in touch soon.";
                    form.reset();
                }} else {{
                    status.className = 'cf-status err';
                    status.textContent = 'Something went wrong sending this — please email '
                        + '{CONTACT_EMAIL}' + ' directly. (' + JSON.stringify(result.json) + ')';
                }}
                status.style.display = 'block';
            }})
            .catch(function (err) {{
                status.className = 'cf-status err';
                status.textContent = 'Network error — please email {CONTACT_EMAIL} directly instead. (' + err + ')';
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
        f"from FormSubmit to {CONTACT_EMAIL} — it must be confirmed once (check spam/promotions "
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
