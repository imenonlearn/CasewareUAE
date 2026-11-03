import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components

import site_config as cfg
from content import (
    CATEGORIES, CHANGES, COMPARISON, FAQS, GUIDES, HIGHLIGHT_PRODUCTS, INSIGHTS, PRODUCTS,
    PROOF_STATS, RESOURCE_LINKS, SECURITY_FACTS, SEGMENTS, SERVICES, WHY_US,
)
from styles import CSS

ROOT = Path(__file__).parent
# Logos normally live in assets/, but also work if uploaded next to app.py
ASSETS = ROOT / "assets" if (ROOT / "assets" / "logo.png").exists() else ROOT
LOGO = ASSETS / "logo.png"              # official Caseware logo, dark text (optional)
LOGO_WHITE = ASSETS / "logo_white.png"  # official Caseware logo, white text (optional)
LEEDS_LOGO = ASSETS / "leeds_logo.png"  # Leeds Software Solutions logo (optional)

PRODUCT_BY_NAME = {p["name"]: p for p in PRODUCTS}
SEGMENT_BY_SLUG = {s["slug"]: s for s in SEGMENTS}

st.set_page_config(page_title=cfg.SITE_NAME, page_icon=":material/analytics:", layout="wide")


# ---------------------------------------------------------------- helpers

def seo(title: str) -> None:
    """Browser-tab and search title for the current page (brief 8.1)."""
    st.set_page_config(page_title=title)


def html(markup: str) -> None:
    # Collapse to one line so Markdown never treats indented HTML as a code block
    st.markdown(" ".join(line.strip() for line in markup.splitlines()), unsafe_allow_html=True)


def g(text: str) -> str:
    return f'<span class="cw-grad">{text}</span>'


def lead_grad(text: str, words: int = 3) -> str:
    """Colour the first few words of a headline with the brand gradient."""
    parts = text.split(" ")
    return f'{g(" ".join(parts[:words]))} {" ".join(parts[words:])}'


def btn(label: str, page: str, style: str = "", new_tab: bool = False) -> str:
    target = "_blank" if new_tab else "_self"
    return f'<a class="cw-btn {style}" href="{page}" target="{target}">{label}</a>'


def tel(number: str, cls: str = "") -> str:
    return f'<a class="{cls}" href="tel:{number.replace(" ", "")}">{number}</a>'


def wa_url() -> str:
    return f"https://wa.me/{cfg.WHATSAPP}?text={quote(cfg.WHATSAPP_MESSAGE)}" if cfg.WHATSAPP else ""


def img_tag(path: Path, cls: str, alt: str) -> str:
    data = base64.b64encode(path.read_bytes()).decode()
    return f'<img class="{cls}" src="data:image/png;base64,{data}" alt="{alt}">'


def map_url() -> str:
    return f"https://www.google.com/maps/search/?api=1&query={quote(cfg.MAP_QUERY)}"


_ICON = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
SOCIAL_ICONS = {
    "LinkedIn": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 11v6"/><path d="M8 7.5v.01"/>'
                '<path d="M12 17v-6"/><path d="M12 13.5c0-1.5 1-2.5 2.5-2.5S17 12 17 13.5V17"/>',
    "YouTube": '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.5v5l4.5-2.5z"/>',
}
WHATSAPP_ICON = _ICON.format(
    '<path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.3z"/>'
    '<path d="M9 8.5c0 3.2 2.3 6 5.5 6.5l1-1.4-1.8-.9-.8.8c-1-.4-2-1.4-2.4-2.4l.8-.8-.9-1.8z"/>'
)


def social_links(cls: str = "") -> str:
    """LinkedIn and YouTube icons (the priority channels). Each becomes a link once its address is set."""
    urls = {"LinkedIn": cfg.LINKEDIN_URL, "YouTube": cfg.YOUTUBE_URL}
    items = []
    for name, paths in SOCIAL_ICONS.items():
        icon = _ICON.format(paths)
        if urls[name]:
            items.append(f'<a href="{urls[name]}" target="_blank" title="{name}" aria-label="{name}">{icon}</a>')
        else:
            items.append(f'<span title="{name}" aria-label="{name}">{icon}</span>')
    return f'<div class="cw-social {cls}">{"".join(items)}</div>'


def confidentiality_statement() -> str:
    region = f" in {cfg.CLOUD_HOSTING_REGION}" if cfg.CLOUD_HOSTING_REGION else ""
    return (
        f"{cfg.BRAND_NAME} treats every client's information as strictly confidential. Data in Caseware "
        f"Cloud is hosted by Caseware{region}, and Leeds accesses client files only when a client asks for "
        "support. Our sales, onboarding and support teams operate independently of any audit or advisory practice."
    )


def topbar() -> None:
    contacts = []
    if cfg.EMAIL:
        contacts.append(f'<a href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a>')
    if cfg.PHONE:
        contacts.append(f"Tel: {tel(cfg.PHONE)}")
    if cfg.MOBILE:
        contacts.append(f"Mobile: {tel(cfg.MOBILE)}")
    if cfg.WHATSAPP:
        contacts.append(f'<a class="cw-wa-link" href="{wa_url()}" target="_blank" title="Chat on WhatsApp" '
                        f'aria-label="Chat on WhatsApp">{WHATSAPP_ICON}</a>')
    floating = (f'<a class="cw-wa-float" href="{wa_url()}" target="_blank" aria-label="Chat on WhatsApp">'
                f'{WHATSAPP_ICON}</a>') if cfg.WHATSAPP else ""
    html(f"""
        <section class="cw-bleed cw-topbar">
            <div class="cw-wrap">
                <div class="cw-topleft">{social_links()}<span>{cfg.TOPBAR_TEXT}</span></div>
                <div class="cw-contacts">{''.join(f'<span>{c}</span>' for c in contacts)}<a class="cw-top-cta" href="contact" target="_self">Book a demo</a></div>
            </div>
            {floating}
        </section>
    """)


def hero(title: str, text: str, buttons: str = "", small: bool = True, badge: str = "", strip: str = "") -> None:
    topbar()
    html(f"""
        <section class="cw-bleed cw-hero {'small' if small else ''}">
            <div class="cw-wrap">
                {f'<div class="cw-hero-badge">{badge}</div>' if badge else ''}
                <div class="cw-h1" role="heading" aria-level="1">{title}</div>
                <p class="cw-lead">{text}</p>
                {f'<div class="cw-btns">{buttons}</div>' if buttons else ''}
                {f'<div class="cw-trust">{strip}</div>' if strip else ''}
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


def balanced_columns(count: int, most: int) -> int:
    """Columns that keep rows full: all in one row if they fit, else the largest even split, e.g. 9 -> 3, 4 -> 2."""
    if count <= most:
        return max(count, 1)
    for cols in range(most, 1, -1):
        if count % cols == 0:
            return cols
    return most


def out_cards(cards, columns: int | None = None) -> str:
    cols = columns or balanced_columns(len(cards), 3)
    items = "".join(
        f'<div class="cw-out {"pink" if i % 2 else ""}"><div class="cw-h3">{title}</div>{body}</div>'
        for i, (title, body) in enumerate(cards)
    )
    return f'<div class="cw-grid{cols}">{items}</div>'


def sector_cards(cards) -> str:
    """Dark outlined cards, all in one row when there are six or fewer."""
    cols = balanced_columns(len(cards), 6)
    return f'<div class="cw-cards cols-{cols}">' + "".join(cards) + "</div>"


def dark_cards(title: str, cards, anchor: str = "") -> None:
    """Dark band of outlined cards. `cards` is a list of (title, text, link_html)."""
    items = [
        f'<div class="cw-sector"><div class="cw-h3">{t}</div><p>{text}</p>{link}</div>'
        for t, text, link in cards
    ]
    # Five or six cards get a wider band so each card keeps a readable width
    wide = "wide" if len(items) >= 5 else ""
    html(f"""
        <section class="cw-bleed cw-dark" {f'id="{anchor}"' if anchor else ''}>
            <div class="cw-wrap {wide}">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">{title}</div>
                {sector_cards(items)}
            </div>
        </section>
    """)


def light_cards(title: str, cards, columns: int | None = None, deco: bool = False, after: str = "") -> None:
    html(f"""
        <section class="cw-bleed cw-light {'deco' if deco else ''}">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">{title}</div>
                {out_cards(cards, columns)}
                {after}
            </div>
        </section>
    """)


def faq_section(title: str, faqs) -> None:
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    html(f"""
        <section class="cw-bleed cw-dark">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">{title}</div>
                <div class="cw-faq">{items}</div>
            </div>
        </section>
    """)


def cta(heading: str = "See Caseware on one of your own engagements",
        text: str = ("Book a 45-minute demo with a Leeds specialist. We will walk through an audit file "
                     "using a trial balance structured like yours."),
        primary: str = "Book a demo", primary_link: str = "contact") -> None:
    whatsapp = btn("Chat on WhatsApp", wa_url(), "white", new_tab=True) if cfg.WHATSAPP else ""
    html(f"""
        <section class="cw-bleed cw-cta">
            <div class="cw-wrap">
                <div class="cw-h2" role="heading" aria-level="2">{heading}</div>
                <p>{text}</p>
                <div class="cw-btns">{btn(primary, primary_link)}{whatsapp}</div>
            </div>
        </section>
    """)


def footer() -> None:
    brand = img_tag(LOGO_WHITE, "cw-flogo", "Caseware logo") if LOGO_WHITE.exists() \
        else '<div class="cw-word">caseware<small>UAE</small></div>'
    lines = []
    if LEEDS_LOGO.exists():
        lines.append(f'<div class="cw-leeds">{img_tag(LEEDS_LOGO, "", cfg.BRAND_NAME + " logo")}</div>')
    lines.append(f'<p class="cw-small"><b>{cfg.LEGAL_NAME}</b></p>')
    if cfg.TRADE_LICENCE:
        lines.append(f'<p class="cw-small">{cfg.TRADE_LICENCE}</p>')
    if cfg.ADDRESS:
        lines.append(f'<p class="cw-small">{cfg.ADDRESS} · '
                     f'<a class="cw-accent" href="{map_url()}" target="_blank">View on map</a></p>')
    if cfg.PO_BOX:
        lines.append(f'<p class="cw-small">{cfg.PO_BOX}</p>')
    if cfg.PHONE:
        lines.append(f'<p class="cw-small">Tel: {tel(cfg.PHONE, "cw-accent")}</p>')
    if cfg.MOBILE:
        lines.append(f'<p class="cw-small">Mobile: {tel(cfg.MOBILE, "cw-accent")}</p>')
    if cfg.WHATSAPP:
        lines.append(f'<p class="cw-small"><a class="cw-accent" href="{wa_url()}" target="_blank">Chat on WhatsApp</a></p>')
    if cfg.EMAIL:
        lines.append(f'<p class="cw-small"><a class="cw-accent" href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a></p>')
    if cfg.WEBSITE:
        lines.append(f'<p class="cw-small">{cfg.WEBSITE}</p>')
    lines.append(social_links())
    segment_links = "".join(f'<a href="{s["slug"]}" target="_self">{s["nav"]}</a>' for s in SEGMENTS)
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
                        <a href="about" target="_self">About</a>
                        <a href="why-caseware" target="_self">Why Caseware</a>
                        <a href="services" target="_self">Services</a>
                        <a href="insights" target="_self">Insights</a>
                        <a href="customer-resources" target="_self">Customer resources</a>
                        <a href="contact" target="_self">Contact</a>
                    </div>
                    <div>
                        <div class="cw-fh">Who it's for</div>
                        {segment_links}
                    </div>
                    <div>
                        <div class="cw-fh">Explore</div>
                        <a href="products" target="_self">Products</a>
                        <a href="contact" target="_self">Book a demo</a>
                        <a href="trust" target="_self">Trust and data security</a>
                    </div>
                </div>
                <div class="cw-legal">
                    <p class="cw-legal-links">
                        <a href="privacy-policy" target="_self">Privacy policy</a> ·
                        <a href="cookie-policy" target="_self">Cookie policy</a> ·
                        <a href="terms-of-use" target="_self">Terms of use</a> ·
                        <a href="trust" target="_self">Trust and data security</a>
                    </p>
                    <p>Caseware is a trademark of Caseware International Inc. Product availability and features may vary by region.</p>
                    <p>© {cfg.LEGAL_NAME}. Authorised Caseware Distributor for the United Arab Emirates.</p>
                </div>
            </div>
        </section>
    """)


def prose(title: str, body: str) -> None:
    """Plain text page section, used for the legal pages."""
    html(f'<section class="cw-bleed cw-prose"><div class="cw-wrap"><div class="cw-prose-inner">'
         f'<div class="cw-h2 cw-grad" role="heading" aria-level="2">{title}</div>{body}</div></div></section>')


# ---------------------------------------------------------------- pages

def home() -> None:
    seo("Caseware UAE · ISA Audit & IFRS Reporting Software")
    hero(
        f"{g('ISA-aligned audits.')} {g('IFRS-ready reporting.')} Inspection-ready files.",
        f"Caseware is the audit and financial reporting platform used by firms, corporates and government "
        f"bodies in {cfg.CASEWARE_COUNTRIES} countries. In the UAE, {cfg.BRAND_NAME} licenses, sets up and "
        "supports it locally, so your team runs every engagement on one defensible methodology.",
        btn("Book a demo", "contact") + btn("Find your solution", "#who-its-for", "white"),
        small=False,
        strip="Authorised Caseware Distributor <i>·</i> ISA and IFRS aligned <i>·</i> Local training and support in the UAE",
    )
    dark_cards(
        "Who it's for",
        [(s["nav"], s["tile"], btn("Explore &nbsp;&rarr;", s["slug"], "sm")) for s in SEGMENTS],
        anchor="who-its-for",
    )
    split(
        "Why UAE firms choose Caseware",
        "<p>Audit regulators across the region expect files that show how risk drove the work. Caseware builds "
        "that discipline into every engagement: risk assessment linked to procedures, linked to evidence, "
        "linked to the financial statements. Reviews are faster, roll-forward takes minutes, and every file "
        "follows the same standard.</p>",
        PROOF_STATS,
    )
    light_cards(
        "Product highlights",
        [
            (name, f'<p>{PRODUCT_BY_NAME[name]["tagline"]}</p>'
                   f'<p style="margin-top:16px">{btn("See the product &nbsp;&rarr;", "products", "sm")}</p>')
            for name in HIGHLIGHT_PRODUCTS
        ],
        deco=True,
    )
    dark_cards(
        "What's changing for UAE auditors and preparers",
        [(t, text, btn("Read more &nbsp;&rarr;", link, "sm")) for t, text, link in CHANGES],
    )
    cta()
    footer()


def products() -> None:
    seo("Caseware Products in the UAE · Leeds Software Solutions")
    hero(
        f"One platform, from {g('trial balance to signed opinion')}",
        "Caseware connects audit methodology, working papers, financial statements and client collaboration, "
        "so nothing is re-keyed and every number traces back to its source.",
    )
    html('<div class="cw-space"></div>')
    choice = st.radio("Filter by category", ["All"] + CATEGORIES, horizontal=True, label_visibility="collapsed")
    cards = []
    for p in PRODUCTS:
        if choice != "All" and choice not in p["categories"]:
            continue
        tags = "".join(f'<span class="cw-tag">{c}</span>' for c in p["categories"])
        features = "".join(f"<li>{f}</li>" for f in p["features"])
        cards.append((
            p["name"],
            f'{tags}<p class="cw-tagline">{p["tagline"]}</p><p>{p["summary"]}</p>'
            f'<ul>{features}</ul><p class="cw-for">Ideal for: {p["ideal_for"]}</p>',
        ))
    html(f'<section class="cw-bleed cw-light tight"><div class="cw-wrap">{out_cards(cards)}</div></section>')
    cta()
    footer()


def segment_page(slug: str) -> None:
    s = SEGMENT_BY_SLUG[slug]
    seo(s["seo_title"])
    demo_link = f"contact?segment={slug}"
    hero(lead_grad(s["headline"]), s["sub"], btn(s["cta"], demo_link))
    if s["challenges"]:
        light_cards("The challenge", [(t, f"<p>{text}</p>") for t, text in s["challenges"]])
    heading = "How Caseware helps" if slug == "audit-quality" else "How Caseware solves it"
    dark_cards(heading, [(t, text, "") for t, text in s["solves"]])
    light_cards(
        "Products used",
        [(name, f'<p>{PRODUCT_BY_NAME[name]["tagline"]}</p>') for name in s["products"]],
        after=f'<div class="cw-btns" style="margin-top:36px">{btn("See all products", "products")}</div>',
    )
    if s["faqs"]:
        faq_section("Frequently asked questions", s["faqs"])
    if s.get("disclaimer"):
        html(f'<section class="cw-bleed cw-note"><div class="cw-wrap"><p>{s["disclaimer"]}</p></div></section>')
    cta(heading=s["cta"], text="Talk to a Leeds specialist about your team, your files and your next engagement.",
        primary=s["cta"], primary_link=demo_link)
    footer()


def make_segment_page(slug: str):
    def page() -> None:
        segment_page(slug)
    page.__name__ = slug.replace("-", "_")
    return page


def why_caseware() -> None:
    seo("Why Caseware · Audit Software vs Excel")
    hero(
        f"Why audit and finance teams {g('move to Caseware')}",
        "Spreadsheets and generic tools can record work. Caseware structures it, links it and proves it.",
    )
    rows = "".join(f"<tr><th>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in COMPARISON)
    html(f"""
        <section class="cw-bleed cw-light">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Spreadsheets versus Caseware</div>
                <div class="cw-table-wrap"><table class="cw-table">
                    <thead><tr><th>What matters</th><th>Excel and shared drives</th><th>Caseware</th></tr></thead>
                    <tbody>{rows}</tbody>
                </table></div>
            </div>
        </section>
    """)
    split(
        "What you get in the UAE",
        "<p>Caseware gives your teams one methodology and one engagement file. Leeds Software Solutions "
        "licenses it, sets it up and supports it locally.</p>",
        PROOF_STATS,
        panel_first=True,
    )
    cta()
    footer()


def services() -> None:
    seo("Caseware Onboarding, Training & Support UAE")
    hero(
        f"{g('More than')} a licence",
        "We stay with you after the sale: set-up, training and ongoing support from a local team.",
    )
    light_cards("Services we offer", [(t, f"<p>{text}</p>") for t, text in SERVICES], columns=4, deco=True)
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


def insights() -> None:
    seo("Insights · Audit and Reporting in the UAE · Caseware UAE")
    hero(
        f"{g('Insights')}",
        "Articles, guides and webinar recordings on the standards and regulations shaping audit and "
        "financial reporting in the UAE.",
    )
    cards = [
        (title, f'<span class="cw-tag soon">Coming soon</span>'
                f'<p>Related: <a href="{slug}" target="_self">{SEGMENT_BY_SLUG[slug]["nav"]}</a></p>')
        for title, slug in INSIGHTS
    ]
    light_cards("Coming up", cards, columns=3, deco=True)
    dark_cards(
        "Already a Caseware user?",
        [("Customer resources", "Practical tips for Working Papers, answers to common questions and links to "
          "official Caseware support.", btn("Open &nbsp;&rarr;", "customer-resources", "sm"))],
    )
    cta()
    footer()


def customer_resources() -> None:
    seo("Customer Resources · Caseware UAE")
    hero(
        f"{g('Customer')} resources",
        "Practical guidance for existing users, answers to common questions and links to official Caseware resources.",
    )
    light_cards("Getting more from Working Papers", [(t, f"<p>{text}</p>") for t, text in GUIDES], deco=True)
    faq_section("Frequently asked questions", FAQS)
    light_cards(
        "Official Caseware resources",
        [(t, f'<p>{text}</p><p style="margin-top:16px">{btn("Open &nbsp;&rarr;", url, "sm", new_tab=True)}</p>')
         for t, text, url in RESOURCE_LINKS],
    )
    cta()
    footer()


def about() -> None:
    seo(f"About {cfg.BRAND_NAME} · Caseware UAE")
    badge = img_tag(LEEDS_LOGO, "", cfg.BRAND_NAME + " logo") if LEEDS_LOGO.exists() else ""
    hero(f"About {g(cfg.BRAND_NAME)}", cfg.ABOUT_US, badge=badge)
    split(
        "About Caseware",
        "<p>Caseware is a global provider of software for the audit and accounting profession. Founded in "
        f"{cfg.CASEWARE_FOUNDED} and headquartered in Toronto, Canada, its solutions are used by accounting "
        f"firms, corporations and government bodies in {cfg.CASEWARE_COUNTRIES} countries.</p>"
        '<p style="margin-top:22px"><a class="cw-btn" href="https://www.caseware.com" target="_blank">Visit caseware.com</a></p>',
        [(cfg.CASEWARE_COUNTRIES, "countries"), (cfg.CASEWARE_FOUNDED, "founded"),
         ("Toronto", "headquarters"), ("Global", "audit and accounting platform")],
    )
    split(
        "Our role in the UAE",
        "<p>As the authorised distributor for the UAE, we are your local point of contact for Caseware: "
        "advice on the right solution, licensing, onboarding, training and day-to-day support.</p>",
        WHY_US,
        panel_first=True,
    )
    html(f"""
        <section class="cw-bleed cw-dark">
            <div class="cw-wrap">
                <div class="cw-h2 cw-grad" role="heading" aria-level="2">Our commitment</div>
                <p class="cw-commit">{confidentiality_statement()}</p>
                <div class="cw-btns" style="margin-top:30px">{btn("Trust and data security", "trust", "sm")}</div>
            </div>
        </section>
    """)
    cta()
    footer()


def trust() -> None:
    seo("Trust and Data Security · Caseware UAE")
    hero(
        f"Trust and {g('data security')}",
        "How client data is protected in Caseware, and how we handle it as your local partner.",
    )
    light_cards("How Caseware Cloud protects your data",
                [(t, f"<p>{text}</p>") for t, text in SECURITY_FACTS], columns=3, deco=True,
                after='<p class="cw-source">Source: Caseware security certifications. Certificates and the SOC 3 '
                      'report are available from <a href="https://trust.caseware.com/" target="_blank">trust.caseware.com</a>.</p>')
    region = (f"Caseware Cloud data for UAE customers is hosted in {cfg.CLOUD_HOSTING_REGION}."
              if cfg.CLOUD_HOSTING_REGION else
              "Caseware Cloud runs in several regions. Ask us which hosting region applies to your licence.")
    dark_cards(
        "Where your data lives",
        [
            ("Caseware Cloud", region, ""),
            ("Caseware Working Papers", "Desktop engagement files are stored on your own computers or network, "
             "under your firm's control.", ""),
            ("Our commitment", confidentiality_statement(), ""),
        ],
    )
    cta()
    footer()


def contact() -> None:
    seo(f"Contact Caseware UAE · {cfg.BRAND_NAME}")
    hero(
        f"Book a {g('demo')} or speak to a specialist",
        "Tell us about your organisation and we will arrange a demo using scenarios like yours.",
    )
    html('<div class="cw-space"></div>')
    segment_names = [s["nav"] for s in SEGMENTS] + ["Other"]
    preset = SEGMENT_BY_SLUG.get(st.query_params.get("segment", ""), {}).get("nav")
    form_col, info_col = st.columns([3, 2], gap="large")

    with form_col:
        with st.form("enquiry"):
            name = st.text_input("Name *")
            organisation = st.text_input("Organisation *")
            role = st.text_input("Role")
            email = st.text_input("Email *")
            phone = st.text_input("Phone")
            segment = st.selectbox("Which best describes you?", segment_names,
                                   index=segment_names.index(preset) if preset else 0)
            users = st.selectbox("Number of users", ["1-5", "6-20", "21-50", "50+"])
            message = st.text_area("How can we help?")
            consent = st.checkbox(f"I agree to receive occasional updates from {cfg.BRAND_NAME} about Caseware "
                                  "products and events.")
            submitted = st.form_submit_button("Prepare enquiry", type="primary")

        if submitted:
            if not (name.strip() and organisation.strip() and "@" in email):
                st.error("Please enter your name, organisation and a valid email address.")
            elif not cfg.EMAIL:
                st.warning("Enquiry email is not configured yet. Set EMAIL in site_config.py.")
            else:
                body = (
                    f"Name: {name}\nOrganisation: {organisation}\nRole: {role}\nEmail: {email}\nPhone: {phone}\n"
                    f"Segment: {segment}\nUsers: {users}\nMarketing consent: {'Yes' if consent else 'No'}\n\n{message}"
                )
                subject = f"Caseware demo request ({segment}) from {organisation}"
                mailto = f"mailto:{cfg.EMAIL}?subject={quote(subject)}&body={quote(body)}"
                st.success("Your enquiry is ready. Click below to send it from your email app.")
                st.link_button("Send enquiry by email", mailto, type="primary")
        st.caption(f"{confidentiality_statement()} See [Trust and data security](trust) and our "
                   "[privacy policy](privacy-policy).")

    with info_col:
        st.subheader("Get in touch", anchor=False)
        details = [
            ("Company", cfg.LEGAL_NAME),
            ("Address", cfg.ADDRESS and f"{cfg.ADDRESS}  \n{cfg.PO_BOX}"),
            ("Tel", cfg.PHONE and f"[{cfg.PHONE}](tel:{cfg.PHONE.replace(' ', '')})"),
            ("Mobile", cfg.MOBILE and f"[{cfg.MOBILE}](tel:{cfg.MOBILE.replace(' ', '')})"),
            ("Email", cfg.EMAIL and f"[{cfg.EMAIL}](mailto:{cfg.EMAIL})"),
            ("Working hours", cfg.OFFICE_HOURS),
        ]
        st.markdown("\n\n".join(f"**{label}**  \n{value}" for label, value in details if value))
        if cfg.WHATSAPP:
            st.link_button("Chat on WhatsApp", wa_url(), type="primary")
        components.iframe(f"https://maps.google.com/maps?q={quote(cfg.MAP_QUERY)}&output=embed", height=260)
        html(social_links("on-light"))
    html('<div class="cw-space"></div>')
    footer()


def privacy_policy() -> None:
    seo("Privacy Policy · Caseware UAE")
    hero("Privacy policy", "How we handle personal information you share with us. Last updated 3 November 2026.")
    contact_line = f"email {cfg.EMAIL} or call {cfg.PHONE}" if cfg.EMAIL else f"call {cfg.PHONE}"
    prose("Who we are", f"""
        <p>This website is operated by {cfg.LEGAL_NAME} ("Leeds", "we"), {cfg.ADDRESS}, {cfg.PO_BOX}.
        We are the authorised distributor of Caseware software in the United Arab Emirates.</p>
        <h3>What we collect</h3>
        <p>When you use the enquiry form, we collect the details you enter: your name, organisation, role, email
        address, phone number, the segment that describes you, the number of users and your message. The form
        prepares an email in your own email app; nothing you type is stored on this website. We receive your
        details when you send that email. We also receive personal information when you call us, message us on
        WhatsApp or email us directly.</p>
        <h3>How we use it</h3>
        <ul>
            <li>To reply to your enquiry, arrange a demo and prepare a quote.</li>
            <li>To provide licences, onboarding, training and support if you become a customer.</li>
            <li>To send occasional updates about Caseware products and events, only if you have agreed to this.
            You can withdraw consent at any time.</li>
        </ul>
        <h3>Who we share it with</h3>
        <p>We share your details with Caseware International Inc. where this is needed to process a licence or
        a support request, and with service providers that help us run our business, such as email and website
        hosting providers. We do not sell personal information.</p>
        <h3>How long we keep it</h3>
        <p>We keep personal information for as long as needed to deal with your enquiry and any resulting
        business relationship, or longer where the law requires it.</p>
        <h3>Your rights</h3>
        <p>Under the UAE Personal Data Protection Law (Federal Decree-Law No. 45 of 2021) you can ask to access,
        correct or delete your personal information, and to withdraw your consent to marketing. To make a
        request, {contact_line}.</p>
        <h3>This website</h3>
        <p>Our website hosting provider processes technical information, such as IP addresses, to deliver the
        site and keep it secure. See our cookie policy for more detail.</p>
        <h3>Changes</h3>
        <p>We may update this policy. The date at the top shows when it last changed.</p>
    """)
    footer()


def cookie_policy() -> None:
    seo("Cookie Policy · Caseware UAE")
    hero("Cookie policy", "Which cookies this website uses. Last updated 3 November 2026.")
    prose("Cookies on this website", """
        <p>We do not set advertising or analytics cookies on this website, and we do not track you across
        other websites.</p>
        <p>The platform that hosts this website may use cookies or similar browser storage that are strictly
        necessary to deliver the pages and keep the site secure. These do not identify you personally.</p>
        <h3>If this changes</h3>
        <p>If we add analytics or marketing tools in future, we will ask for your consent before setting any
        non-essential cookies and will update this page.</p>
        <h3>Managing cookies</h3>
        <p>You can block or delete cookies in your browser settings. Blocking strictly necessary cookies may
        stop parts of the website from working.</p>
    """)
    footer()


def terms_of_use() -> None:
    seo("Terms of Use · Caseware UAE")
    hero("Terms of use", "The terms that apply when you use this website. Last updated 3 November 2026.")
    prose("Using this website", f"""
        <p>This website is operated by {cfg.LEGAL_NAME}. By using it you agree to these terms.</p>
        <h3>Information only</h3>
        <p>Content on this website is general information about Caseware products and our services. It is not
        professional, legal or tax advice. Product availability and features may vary by region and may change;
        please contact us to confirm what applies to you.</p>
        <h3>Trademarks</h3>
        <p>Caseware and the Caseware logo are trademarks of Caseware International Inc. and are used with
        permission. Other names and logos belong to their respective owners.</p>
        <h3>Links to other websites</h3>
        <p>We link to websites we do not control, such as caseware.com. We are not responsible for their
        content or availability.</p>
        <h3>Liability</h3>
        <p>We take care to keep this website accurate, but we provide it "as is". To the extent permitted by
        law, we are not liable for any loss arising from use of this website.</p>
        <h3>Governing law</h3>
        <p>These terms are governed by the laws of the United Arab Emirates.</p>
    """)
    footer()


# ---------------------------------------------------------------- navigation

PAGES = {
    "": [
        st.Page(home, title="Home", url_path="home", default=True),
        st.Page(products, title="Products", url_path="products"),
        st.Page(why_caseware, title="Why Caseware", url_path="why-caseware"),
        st.Page(services, title="Services", url_path="services"),
        st.Page(insights, title="Insights", url_path="insights"),
        st.Page(about, title="About", url_path="about"),
        st.Page(contact, title="Contact", url_path="contact"),
        # Linked from the footer only; hidden from the menu by CSS
        st.Page(customer_resources, title="Customer resources", url_path="customer-resources"),
        st.Page(trust, title="Trust and data security", url_path="trust"),
        st.Page(privacy_policy, title="Privacy policy", url_path="privacy-policy"),
        st.Page(cookie_policy, title="Cookie policy", url_path="cookie-policy"),
        st.Page(terms_of_use, title="Terms of use", url_path="terms-of-use"),
    ],
    "Who it's for": [
        st.Page(make_segment_page(s["slug"]), title=s["nav"], url_path=s["slug"]) for s in SEGMENTS
    ],
}

st.markdown(CSS, unsafe_allow_html=True)
if LOGO.exists():
    st.logo(str(LOGO), size="large")
st.navigation(PAGES, position="top").run()
