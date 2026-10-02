import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

import site_config as cfg
from content import FAQS, GUIDES, PRODUCTS, RESOURCE_LINKS, SERVICES, SOLUTIONS, WHY_US
from styles import CSS

ROOT = Path(__file__).parent
# Logos normally live in assets/, but also work if uploaded next to app.py
ASSETS = ROOT / "assets" if (ROOT / "assets" / "logo.png").exists() else ROOT
LOGO = ASSETS / "logo.png"              # official Caseware logo, dark text (optional)
LOGO_WHITE = ASSETS / "logo_white.png"  # official Caseware logo, white text (optional)

st.set_page_config(page_title=cfg.SITE_NAME, page_icon=":material/analytics:", layout="wide")


def html(markup: str) -> None:
    # Collapse to one line so Markdown never treats indented HTML as a code block
    st.markdown(" ".join(line.strip() for line in markup.splitlines()), unsafe_allow_html=True)


def g(text: str) -> str:
    return f'<span class="cw-grad">{text}</span>'


def btn(label: str, page: str, style: str = "") -> str:
    return f'<a class="cw-btn {style}" href="{page}" target="_self">{label}</a>'


def topbar() -> None:
    contacts = []
    if cfg.EMAIL:
        contacts.append(f'<a href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a>')
    if cfg.PHONE:
        contacts.append(f"<span>{cfg.PHONE}</span>")
    html(f"""
        <section class="cw-bleed cw-topbar">
            <div class="cw-wrap">
                <span>Distributor of Caseware software in the United Arab Emirates</span>
                <span>{' &nbsp;|&nbsp; '.join(contacts)}</span>
            </div>
            <a class="cw-header-cta" href="contact" target="_self">Contact Sales</a>
        </section>
    """)


def hero(title: str, text: str, buttons: str = "", small: bool = True) -> None:
    topbar()
    html(f"""
        <section class="cw-bleed cw-hero {'small' if small else ''}">
            <div class="cw-wrap">
                <div class="cw-h1" role="heading" aria-level="1">{title}</div>
                <p class="cw-lead">{text}</p>
                {f'<div class="cw-btns">{buttons}</div>' if buttons else ''}
            </div>
        </section>
    """)


def panel(stats) -> str:
    items = "".join(f'<div class="cw-stat"><b>{big}</b><span>{small}</span></div>' for big, small in stats)
    wordy = "text" if any(len(big) > 10 for big, _ in stats) else ""
    return f'<div class="cw-panel {wordy}">{items}</div>'


def split(heading: str, body: str, stats, panel_first: bool = False) -> None:
    text = f'<div><div class="cw-h2 cw-grad" role="heading" aria-level="2">{heading}</div>{body}</div>'
    parts = (panel(stats), text) if panel_first else (text, panel(stats))
    html(f'<section class="cw-bleed"><div class="cw-wrap"><div class="cw-split">{parts[0]}{parts[1]}</div></div></section>')


def out_cards(cards, columns: int = 2) -> str:
    items = "".join(
        f'<div class="cw-out {"pink" if i % 2 else ""}"><div class="cw-h3">{title}</div>{body}</div>'
        for i, (title, body) in enumerate(cards)
    )
    return f'<div class="cw-grid{columns}">{items}</div>'


def cta() -> None:
    html(f"""
        <section class="cw-bleed cw-cta">
            <div class="cw-wrap">
                <div class="cw-h2" role="heading" aria-level="2">Ready to modernise your audit and reporting?</div>
                <p>We help organisations in the UAE simplify complexity, improve consistency and deliver
                work they can stand behind across audit, assurance and financial reporting.</p>
                <div class="cw-btns">{btn('Contact Us', 'contact', 'white')}{btn('Book a Demo', 'contact')}</div>
            </div>
        </section>
    """)


def footer() -> None:
    operator = cfg.LEGAL_NAME or cfg.SITE_NAME
    if LOGO_WHITE.exists():
        data = base64.b64encode(LOGO_WHITE.read_bytes()).decode()
        brand = f'<img class="cw-flogo" src="data:image/png;base64,{data}" alt="Caseware">'
    else:
        brand = '<div class="cw-word">caseware<small>UAE</small></div>'
    lines = [f'<p class="cw-small">{cfg.ADDRESS}</p>' if cfg.ADDRESS else ""]
    if cfg.PHONE:
        lines.append(f'<p class="cw-small">Sales: <a class="cw-accent" href="tel:{cfg.PHONE}">{cfg.PHONE}</a></p>')
    if cfg.EMAIL:
        lines.append(f'<p class="cw-small"><a class="cw-accent" href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a></p>')
    if cfg.LINKEDIN_URL:
        lines.append(f'<p class="cw-small"><a class="cw-accent" href="{cfg.LINKEDIN_URL}">LinkedIn</a></p>')
    product_links = "".join(f'<a href="products" target="_self">{p["name"]}</a>' for p in PRODUCTS[:5])
    html(f"""
        <section class="cw-bleed cw-footer">
            <div class="cw-wrap">
                <div class="cw-fgrid">
                    <div>
                        {brand}
                        <p>Audit, assurance and financial reporting software, supported in the UAE.</p>
                        {''.join(lines)}
                    </div>
                    <div>
                        <div class="cw-fh">Company</div>
                        <a href="about" target="_self">About Us</a>
                        <a href="services" target="_self">Services</a>
                        <a href="knowledge" target="_self">Knowledge</a>
                        <a href="contact" target="_self">Contact</a>
                    </div>
                    <div>
                        <div class="cw-fh">Explore</div>
                        <a href="products" target="_self">Products</a>
                        <a href="solutions" target="_self">Solutions</a>
                        <a href="contact" target="_self">Book a Demo</a>
                    </div>
                    <div>
                        <div class="cw-fh">Products</div>
                        {product_links}
                    </div>
                </div>
                <div class="cw-legal">
                    <p>Caseware and the Caseware logo are registered trademarks of Caseware International Inc.
                    Product availability and features may vary by region.</p>
                    <p>© {operator}. Distributor of Caseware software in the United Arab Emirates.</p>
                </div>
            </div>
        </section>
    """)


def sector_cards(cards) -> str:
    return '<div class="cw-cards">' + "".join(cards) + "</div>"


def home() -> None:
    hero(
        f"{g('Audit and reporting software')} built for the realities of the {g('UAE market')}",
        "Caseware UAE supplies and supports software for audit, assurance and financial "
        "reporting. Our solutions help practice firms, corporate finance teams and public sector bodies "
        "improve consistency, strengthen compliance and simplify complex workflows.",
        btn("Contact Sales", "contact") + btn("Explore Products", "products", "white"),
        small=False,
    )
    split(
        "Designed for the way audit and finance teams work",
        "<p>We go beyond supplying software. We help organisations get more from their Caseware solutions: "
        "simpler day-to-day audit, assurance and reporting processes, with better consistency, visibility "
        "and long-term efficiency.</p>",
        [
            ("130", "countries where Caseware is used"),
            ("1988", "the year Caseware was founded"),
            ("IFRS + ISA", "aligned content and methodology"),
            ("UAE", "local licensing, training and support"),
        ],
    )
    cards = [
        f'<div class="cw-sector"><div class="cw-h3">{s["title"]}</div><p>{s["text"]}</p>'
        f'{btn("Explore &nbsp;&rarr;", "solutions", "sm")}</div>'
        for s in SOLUTIONS
    ]
    html(f"""
        <section class="cw-bleed cw-dark">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Solutions by sector</div>
                {sector_cards(cards)}
            </div>
        </section>
    """)
    split(
        "Built with the UAE market in mind",
        "<p>Organisations in the UAE need both flexibility and control. Our solutions are practical to "
        "adopt, scale as you grow and align with local requirements and international standards.</p>"
        "<ul>"
        "<li>Financial statements under IFRS and IFRS for SMEs</li>"
        "<li>Audits performed under International Standards on Auditing</li>"
        "<li>Audited accounts for free zone and mainland requirements</li>"
        "<li>Reliable year-end figures to support UAE Corporate Tax returns</li>"
        "</ul>",
        [(title, text) for title, text in WHY_US],
        panel_first=True,
    )
    featured = [(p["name"], f'<p>{p["tagline"]}</p>') for p in PRODUCTS[:4]]
    html(f"""
        <section class="cw-bleed cw-light deco">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Supporting better outcomes across every engagement</div>
                {out_cards(featured)}
                <div class="cw-btns" style="margin-top:40px">{btn('Explore All Products', 'products')}</div>
            </div>
        </section>
    """)
    cta()
    footer()


def products() -> None:
    hero(
        f"The {g('Caseware')} product suite",
        "Connected tools covering the full engagement: audit, review and financial statements.",
    )
    categories = ["All"] + sorted({p["category"] for p in PRODUCTS})
    html('<div class="cw-space"></div>')
    choice = st.radio("Filter by category", categories, horizontal=True, label_visibility="collapsed")
    cards = []
    for p in PRODUCTS:
        if choice != "All" and p["category"] != choice:
            continue
        features = "".join(f"<li>{f}</li>" for f in p["features"])
        cards.append((
            p["name"],
            f'<span class="cw-tag">{p["category"]}</span>'
            f'<p class="cw-tagline">{p["tagline"]}</p><p>{p["summary"]}</p>'
            f'<ul>{features}</ul><p class="cw-for">Ideal for: {p["ideal_for"]}</p>',
        ))
    html(f'<section class="cw-bleed cw-light tight"><div class="cw-wrap">{out_cards(cards)}</div></section>')
    cta()
    footer()


def solutions() -> None:
    hero(
        f"Solutions for {g('every team')}",
        "Whether you sign audit opinions, prepare accounts or test controls, there is a Caseware set-up for your team.",
    )
    cards = [
        f'<div class="cw-sector"><div class="cw-h3">{s["title"]}</div><p>{s["text"]}</p>'
        f'<div>{"".join(f"""<span class="cw-tag line">{name}</span>""" for name in s["products"])}</div></div>'
        for s in SOLUTIONS
    ]
    html(f"""
        <section class="cw-bleed cw-dark">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Solutions by sector</div>
                <div class="cw-cards" style="grid-template-columns:repeat(auto-fit,minmax(420px,1fr))">{''.join(cards)}</div>
            </div>
        </section>
    """)
    cta()
    footer()


def services() -> None:
    hero(
        f"{g('More than')} a licence",
        "We stay with you after the sale: set-up, training and ongoing support from a local team.",
    )
    html(f"""
        <section class="cw-bleed cw-light deco">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Services we offer</div>
                {out_cards([(title, f'<p>{text}</p>') for title, text in SERVICES], columns=3)}
            </div>
        </section>
    """)
    steps = [
        ("1", "Discover", "We learn how your team works today."),
        ("2", "Demonstrate", "A live demo using scenarios relevant to you."),
        ("3", "Deploy", "Licensing, installation and templates set up."),
        ("4", "Develop", "Training and support as your team grows."),
    ]
    cards = [
        f'<div class="cw-sector"><span class="cw-num cw-grad">{n}</span><div class="cw-h3">{title}</div><p>{text}</p></div>'
        for n, title, text in steps
    ]
    html(f"""
        <section class="cw-bleed cw-dark">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">How we get you started</div>
                {sector_cards(cards)}
            </div>
        </section>
    """)
    cta()
    footer()


def knowledge() -> None:
    hero(
        f"{g('Knowledge')} hub",
        "Practical guidance, answers to common questions and links to official Caseware resources.",
    )
    html(f"""
        <section class="cw-bleed cw-light deco">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Getting more from Working Papers</div>
                {out_cards([(title, f'<p>{text}</p>') for title, text in GUIDES], columns=3)}
            </div>
        </section>
    """)
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQS)
    html(f"""
        <section class="cw-bleed cw-dark">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Frequently asked questions</div>
                <div class="cw-faq">{faqs}</div>
            </div>
        </section>
    """)
    links = [
        (title, f'<p>{text}</p><p style="margin-top:16px"><a class="cw-btn sm" href="{url}" target="_blank">Open &nbsp;&rarr;</a></p>')
        for title, text, url in RESOURCE_LINKS
    ]
    html(f"""
        <section class="cw-bleed cw-light">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Official Caseware resources</div>
                {out_cards(links, columns=3)}
            </div>
        </section>
    """)
    cta()
    footer()


def about() -> None:
    hero(f"About {g('Caseware UAE')}", cfg.ABOUT_US)
    split(
        "About Caseware",
        "<p>Caseware is a global provider of software for the audit and accounting profession. Founded in "
        "1988 and headquartered in Toronto, Canada, its solutions are used by accounting firms, "
        "corporations and government bodies in 130 countries.</p>"
        '<p style="margin-top:22px"><a class="cw-btn" href="https://www.caseware.com" target="_blank">Visit caseware.com</a></p>',
        [("130", "countries"), ("1988", "founded"), ("Toronto", "headquarters"), ("Global", "audit and accounting platform")],
    )
    operated = f"<p style='margin-top:14px'>Operated by {cfg.LEGAL_NAME}.</p>" if cfg.LEGAL_NAME else ""
    split(
        "Our role in the UAE",
        "<p>As the distributor for the UAE, we are your local point of contact for Caseware products: "
        "advice on the right solution, licensing, onboarding, training and day-to-day support.</p>" + operated,
        [(title, text) for title, text in WHY_US],
        panel_first=True,
    )
    cta()
    footer()


def contact() -> None:
    hero(
        f"Request a {g('demo or a quote')}",
        "Tell us a little about your organisation and we will get back to you.",
    )
    html('<div class="cw-space"></div>')
    form_col, info_col = st.columns([3, 2], gap="large")

    with form_col:
        with st.form("enquiry"):
            name = st.text_input("Name *")
            company = st.text_input("Company *")
            email = st.text_input("Email *")
            phone = st.text_input("Phone")
            interest = st.multiselect("Products of interest", [p["name"] for p in PRODUCTS])
            users = st.selectbox("Number of users", ["1-5", "6-20", "21-50", "50+"])
            message = st.text_area("How can we help?")
            submitted = st.form_submit_button("Prepare enquiry", type="primary")

        if submitted:
            if not (name.strip() and company.strip() and "@" in email):
                st.error("Please enter your name, company and a valid email address.")
            elif not cfg.EMAIL:
                st.warning("Enquiry email is not configured yet. Set EMAIL in site_config.py.")
            else:
                body = (
                    f"Name: {name}\nCompany: {company}\nEmail: {email}\nPhone: {phone}\n"
                    f"Products: {', '.join(interest) or 'Not specified'}\nUsers: {users}\n\n{message}"
                )
                subject = f"Caseware enquiry from {company}"
                mailto = f"mailto:{cfg.EMAIL}?subject={quote(subject)}&body={quote(body)}"
                st.success("Your enquiry is ready. Click below to send it from your email app.")
                st.link_button("Send enquiry by email", mailto, type="primary")

    with info_col:
        st.subheader("Get in touch", anchor=False)
        details = [
            ("Email", cfg.EMAIL and f"[{cfg.EMAIL}](mailto:{cfg.EMAIL})"),
            ("Phone", cfg.PHONE),
            ("Address", cfg.ADDRESS),
            ("Hours", cfg.OFFICE_HOURS),
        ]
        shown = [f"**{label}**  \n{value}" for label, value in details if value]
        if shown:
            st.markdown("\n\n".join(shown))
        else:
            st.caption("Contact details will appear here once added to site_config.py.")
        if cfg.WHATSAPP:
            st.link_button("Chat on WhatsApp", f"https://wa.me/{cfg.WHATSAPP}")
        if cfg.LINKEDIN_URL:
            st.link_button("Follow us on LinkedIn", cfg.LINKEDIN_URL)
    html('<div class="cw-space"></div>')
    footer()


PAGES = [
    st.Page(home, title="Home", url_path="home", default=True),
    st.Page(products, title="Products", url_path="products"),
    st.Page(solutions, title="Solutions", url_path="solutions"),
    st.Page(services, title="Services", url_path="services"),
    st.Page(knowledge, title="Knowledge", url_path="knowledge"),
    st.Page(about, title="Who We Are", url_path="about"),
    st.Page(contact, title="Contact Us", url_path="contact"),
]

st.markdown(CSS, unsafe_allow_html=True)
if LOGO.exists():
    st.logo(str(LOGO), size="large")
else:
    # Text wordmark until the official logo file is added to assets/
    st.logo(
        "data:image/svg+xml;utf8,"
        + quote(
            '<svg xmlns="http://www.w3.org/2000/svg" width="190" height="40">'
            '<text x="0" y="29" font-family="Arial, Helvetica, sans-serif" font-size="29" font-weight="700" '
            'letter-spacing="-1" fill="#1A1B1D">caseware'
            '<tspan dx="7" font-size="15" letter-spacing="0" fill="#FF645C">UAE</tspan></text></svg>'
        ),
        size="large",
    )
st.navigation(PAGES, position="top").run()
