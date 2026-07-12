# Johannes Favi — Consulting Website (Streamlit)

A single-page consulting website built with Streamlit, styled in navy/gold with a
Playfair Display + Inter typeface pairing. Includes a working contact form that
delivers directly to **contactcageddreams@gmail.com** with no backend or email
credentials to manage.

## What's inside
- `app.py` — the full site (Home, About, Services, Speaking, Advisory, Contact)
- `requirements.txt` — the one dependency (Streamlit)

## Run it locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open the local URL Streamlit prints (usually `http://localhost:8501`).

## How the contact form works
The Contact tab embeds a real HTML `<form>` that posts to
[FormSubmit](https://formsubmit.co/) — a free service that forwards form
submissions straight to an inbox with zero setup on your end. It's used instead
of Streamlit's built-in form because Streamlit forms can't send email on their
own; this way you don't need to manage SMTP credentials or app passwords.

**One-time activation step:** the very first message anyone submits will
trigger a confirmation email from FormSubmit to `contactcageddreams@gmail.com`.
Someone with access to that inbox needs to click the confirmation link once —
after that, every future submission arrives normally with no further action
needed.

If you'd rather not depend on a third-party form service, the alternative is
sending mail directly via Gmail's SMTP with an "app password" stored in
Streamlit secrets — happy to build that version instead if you prefer it.

## Deploying to Streamlit Community Cloud (free)

1. **Create the GitHub repo**
   - Go to https://github.com/new under your account (`anamariaUIC`)
   - Name it something like `johannes-favi-consulting`
   - Keep it public (required for the free tier of Streamlit Community Cloud)
   - Don't initialize with a README (you already have the files here)

2. **Push these files to the repo**
   ```bash
   cd johannes-favi-site
   git init
   git add app.py requirements.txt README.md
   git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/anamariaUIC/johannes-favi-consulting.git
   git push -u origin main
   ```

3. **Deploy on Streamlit Community Cloud**
   - Go to https://share.streamlit.io and sign in with GitHub
   - Click **"New app"**
   - Select the `anamariaUIC/johannes-favi-consulting` repo, branch `main`,
     and main file `app.py`
   - Click **Deploy** — it will build and give you a live URL like
     `https://johannes-favi-consulting.streamlit.app`

4. **Confirm the contact form**
   - Once live, submit a test message through the Contact tab
   - Check `contactcageddreams@gmail.com` for the FormSubmit confirmation
     email and click the confirmation link
   - Submit a second test message to confirm delivery works end to end

5. **Optional: custom domain**
   - Streamlit Community Cloud apps live on a `*.streamlit.app` subdomain by
     default. A custom domain (e.g. `johannesfavi.com`) requires either
     upgrading to a paid host that supports custom domains, or setting up a
     DNS redirect/CNAME to the `.streamlit.app` URL if your registrar
     supports it.

## Customizing later
- Swap in a professional headshot: add an image file to the repo and drop
  `st.image("headshot.jpg")` near the top of the Home or About tab.
- Add a real bio paragraph with more personal/career detail once you have
  final copy — right now the About section uses the "Who I Work With" and
  "Signature Expertise" content from your provided homepage layout.
- Colors are controlled by the CSS variables at the top of `app.py`
  (`--navy`, `--gold`, `--off-white`) if you want to adjust the palette.
