"""Site styling: current Caseware brand look (coral-to-blue gradient, League Spartan, dark bands)."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;500;600;700&display=swap');

:root {
    --cw-grad-text: linear-gradient(90deg, #FF645B 0%, #EE5A98 22%, #1C5EED 45%, #1C5EED 100%);
    --cw-grad-btn: linear-gradient(90deg, #FF645C 0%, #E956AF 100%);
    --cw-dark: #1A1B1D;
    --cw-coral: #FF645C;
    --cw-pink: #E956AF;
    --cw-blue: #1C4DFF;
}

/* ---------- Streamlit shell ---------- */
html, body, .stApp, .stApp p, .stApp li, .stApp label, .stApp button, .stApp input, .stApp textarea,
.stApp a, .stApp span, .stApp h1, .stApp h2, .stApp h3 { font-family: 'League Spartan', sans-serif; }
.stApp span[data-testid="stIconMaterial"] { font-family: 'Material Symbols Rounded'; }
.stAppHeader { background: #fff; border-bottom: 1px solid #ececec; }
.stAppHeader a, .stAppHeader span { color: #737373; font-weight: 500; font-size: 16px; }
img.stLogo { height: 27px; width: auto; max-width: none; }
[data-testid="stLogoLink"] { flex-shrink: 0; }
.stMainBlockContainer { padding: 3.75rem 0 0 0 !important; max-width: none !important; }
.stMainBlockContainer > div[data-testid="stVerticalBlock"] { gap: 0; }
.stMainBlockContainer > div[data-testid="stVerticalBlock"] > div:not(:has(.cw-bleed)) {
    max-width: 1140px; width: 100%; margin: 0 auto 1.1rem auto; padding: 0 20px;
}
.stMainBlockContainer > div[data-testid="stVerticalBlock"] > div:first-child { margin-bottom: 0 !important; }
.cw-space { height: 44px; }
.stApp [data-testid="stMarkdownContainer"]:has(.cw-bleed) { margin-bottom: 0 !important; }
.stButton button, .stFormSubmitButton button, .stLinkButton a { border-radius: 15px; font-weight: 600; }
.stButton button[kind="primary"], .stFormSubmitButton button[kind="primaryFormSubmit"],
.stLinkButton a[kind="primary"] { background: var(--cw-grad-btn); border: 0; color: #fff; }
[data-testid="stForm"] { border-radius: 15px; border-top: 5px solid var(--cw-blue); background: #fff; }

/* ---------- Shared ---------- */
.cw-bleed { width: 100%; font-family: 'League Spartan', sans-serif; }
.cw-wrap { max-width: 1140px; margin: 0 auto; padding: 0 20px; position: relative; }
.stApp .cw-bleed p, .stApp .cw-bleed li { font-size: 16px; line-height: 1.75; margin: 0; }
.stApp .cw-bleed a { text-decoration: none; }
.cw-grad { background: var(--cw-grad-text); -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent; }
.cw-h2 { font-size: 35px; font-weight: 700; line-height: 1.43; margin: 0 0 22px 0; display: inline-block; }
.cw-h3 { font-size: 22px; font-weight: 700; line-height: 1.2; margin: 0 0 16px 0; color: var(--cw-dark); }
.cw-btns { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }
.stApp .cw-bleed a.cw-btn { display: inline-block; padding: 18px 25px 15px; border-radius: 15px; font-weight: 600;
    font-size: 16px; line-height: 1; color: #fff; background: var(--cw-grad-btn); transition: transform .15s; }
.stApp .cw-bleed a.cw-btn:hover { transform: translateY(-2px); }
.stApp .cw-bleed a.cw-btn.white { background: linear-gradient(90deg, #fff 0%, #eee 100%); color: var(--cw-coral); }
.stApp .cw-bleed a.cw-btn.sm { padding: 8px 18px 5px; border-radius: 10px; align-self: flex-start;
    background: linear-gradient(180deg, #FF645C 0%, #E956AF 100%); }

/* ---------- Top bar + header button ---------- */
.cw-topbar { background: #303333; color: #fff; font-size: 15px; padding: 11px 0 9px; }
.cw-topbar .cw-wrap { display: flex; justify-content: space-between; gap: 6px 24px; flex-wrap: wrap; }
.stApp .cw-topbar a { color: #fff; font-weight: 500; }
.stApp a.cw-header-cta { position: fixed; top: 9px; right: 28px; z-index: 1000000; padding: 14px 22px 11px;
    border-radius: 15px; background: var(--cw-grad-btn); color: #fff; font-weight: 600; font-size: 16px;
    line-height: 1; text-decoration: none; }

/* ---------- Hero ---------- */
.cw-hero { color: #fff; text-align: center; padding: 100px 0 110px;
    background:
        radial-gradient(circle at 12% 85%, rgba(255,100,92,.38), transparent 38%),
        radial-gradient(circle at 88% 30%, rgba(255,100,92,.26), transparent 32%),
        radial-gradient(circle at 50% 120%, rgba(28,94,237,.55), transparent 52%),
        radial-gradient(rgba(255,255,255,.13) 1px, transparent 1.6px) 0 0 / 22px 22px,
        #0A0B0F; }
.cw-hero.small { padding: 70px 0 76px; }
.cw-h1 { font-size: 50px; font-weight: 700; line-height: 1.3; max-width: 860px; margin: 0 auto 22px; color: #fff; }
.stApp .cw-bleed p.cw-lead { font-size: 22px; line-height: 1.5; max-width: 1060px; margin: 0 auto 34px; color: #fff; }
.cw-hero.small p.cw-lead { margin-bottom: 0; max-width: 820px; }

/* ---------- Split (text + panel) ---------- */
.cw-split { display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: center; padding: 100px 0; }
.cw-split p, .cw-split li { color: #000; }
.cw-split ul { margin: 14px 0 0 0; padding-left: 20px; }
.cw-panel { border-radius: 15px; min-height: 350px; padding: 40px; display: grid; grid-template-columns: 1fr 1fr;
    gap: 30px; align-content: center;
    background:
        radial-gradient(circle at 0% 100%, rgba(255,100,92,.55), transparent 55%),
        radial-gradient(circle at 100% 0%, rgba(28,77,255,.6), transparent 55%),
        radial-gradient(circle at 80% 100%, rgba(233,86,175,.4), transparent 45%),
        var(--cw-dark); }
.cw-stat b { display: block; font-size: 34px; font-weight: 700; color: #fff; line-height: 1.15; }
.cw-panel.text .cw-stat b { font-size: 23px; }
.cw-stat span { color: #e6e6e6; font-size: 16px; line-height: 1.4; display: block; margin-top: 4px; }

/* ---------- Dark band with sector cards ---------- */
.cw-dark { text-align: center; padding: 100px 0 110px;
    background:
        radial-gradient(circle at 12% 55%, rgba(84,60,160,.22), transparent 30%),
        radial-gradient(circle at 88% 60%, rgba(160,60,110,.16), transparent 28%),
        var(--cw-dark); }
.cw-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(235px, 1fr)); gap: 30px;
    margin-top: 48px; text-align: left; }
.cw-sector { position: relative; display: flex; flex-direction: column; border: 1px solid #fff;
    border-top: 5px solid #4257F5; border-radius: 15px; padding: 32px 30px 30px;
    background:
        linear-gradient(180deg, rgba(26,27,29,.96) 35%, rgba(26,27,29,.72) 100%),
        radial-gradient(circle at 75% 105%, rgba(255,140,60,.9), transparent 55%),
        radial-gradient(circle at 15% 105%, rgba(28,77,255,.9), transparent 55%),
        var(--cw-dark); }
.cw-sector::before { content: ""; position: absolute; left: -12px; top: -20px; width: 36px; height: 40px;
    background: linear-gradient(45deg, #FF645C 20%, #E956AF 60%, #7B5CFF 100%);
    clip-path: polygon(100% 0, 100% 100%, 0 100%); }
.cw-sector .cw-h3 { color: #fff; margin-bottom: 20px; }
.stApp .cw-bleed .cw-sector p { color: #fff; flex: 1; margin-bottom: 22px; }
.cw-num { font-size: 40px; font-weight: 700; line-height: 1; margin-bottom: 14px; display: inline-block; }

/* ---------- Light band with outcome cards ---------- */
.cw-light { position: relative; padding: 90px 0; text-align: center; overflow: hidden; }
.cw-light.deco::before { content: ""; position: absolute; top: 0; right: 0; width: 45%; height: 100%;
    background: linear-gradient(180deg, rgba(255,100,92,.5) 0%, rgba(233,86,175,.22) 50%, rgba(255,255,255,0) 92%);
    clip-path: polygon(56% 0, 100% 0, 100% 100%, 0 86%); }
.cw-light.tight { padding: 40px 0 70px; }
.cw-grid2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 44px; text-align: left; }
.cw-grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 44px; text-align: left; }
.cw-light.tight .cw-grid2, .cw-light.tight .cw-grid3 { margin-top: 0; }
.cw-out { background: #fff; border: 1px solid #E4E4E8; border-top: 5px solid var(--cw-blue); border-radius: 15px;
    padding: 26px 30px 24px; }
.cw-out.pink { border-top-color: var(--cw-pink); }
.cw-out p { color: #000; }
.stApp .cw-bleed .cw-out p.cw-tagline { font-weight: 600; margin-bottom: 8px; }
.cw-out ul { margin: 12px 0 0 0; padding-left: 20px; }
.stApp .cw-bleed .cw-out p.cw-for { color: #6b6b6b; font-size: 14px; margin-top: 12px; }
.cw-tag { display: inline-block; padding: 5px 12px 2px; border-radius: 10px; font-size: 13px; font-weight: 600;
    color: #fff; background: var(--cw-grad-btn); margin: 0 6px 12px 0; }
.cw-tag.line { background: none; border: 1px solid #fff; }

/* ---------- Call to action ---------- */
.cw-cta { text-align: center; color: #fff; padding: 120px 0 130px;
    background: linear-gradient(180deg, #FF645C 0%, #A85A9C 38%, #5C5FD6 75%, #5062E0 100%); }
.cw-cta .cw-h2 { font-size: 40px; line-height: 1.375; color: #fff; max-width: 700px; display: block; margin: 0 auto 22px; }
.stApp .cw-bleed.cw-cta p { color: #fff; font-size: 18px; max-width: 980px; margin: 0 auto 34px; }

/* ---------- Footer ---------- */
.cw-footer { background: var(--cw-dark); color: #fff; padding: 52px 0 40px; }
.cw-fgrid { display: grid; grid-template-columns: 1.5fr 1fr 1fr 1.5fr; gap: 34px; }
.cw-word { font-size: 40px; font-weight: 600; letter-spacing: -1.5px; line-height: 1; margin-bottom: 18px; color: #fff; }
.cw-word small { font-size: 17px; letter-spacing: 0; margin-left: 6px; }
.cw-footer img.cw-flogo { height: 32px; margin: 0 0 18px -5px; display: block; }
.stApp .cw-bleed.cw-footer p { color: #fff; line-height: 1.5; margin-bottom: 14px; }
.stApp .cw-bleed.cw-footer p.cw-small { font-size: 14px; margin-bottom: 4px; }
.cw-fh { font-size: 19px; font-weight: 700; margin-bottom: 22px; }
.stApp .cw-bleed.cw-footer a { color: #fff; display: block; margin-bottom: 14px; font-size: 16px; }
.stApp .cw-bleed.cw-footer a.cw-accent { color: #FF5C7A; display: inline; }
.cw-legal { border-top: 1px solid #38393C; margin-top: 40px; padding-top: 24px; text-align: center; }
.stApp .cw-bleed.cw-footer .cw-legal p { font-size: 13.5px; color: #cfcfcf; margin-bottom: 6px; }

@media (max-width: 860px) {
    .cw-h1 { font-size: 34px; }
    .stApp .cw-bleed p.cw-lead { font-size: 18px; }
    .cw-h2 { font-size: 28px; }
    .cw-cta .cw-h2 { font-size: 30px; }
    .cw-hero { padding: 64px 0 70px; }
    .cw-split { grid-template-columns: 1fr; gap: 36px; padding: 60px 0; }
    .cw-split .cw-panel { order: 2; }
    .cw-grid2, .cw-grid3 { grid-template-columns: 1fr; }
    .cw-fgrid { grid-template-columns: 1fr 1fr; }
    .cw-dark, .cw-light { padding: 64px 0; }
    .cw-cta { padding: 76px 0 84px; }
    .stApp a.cw-header-cta { display: none; }
    .cw-light.deco::before { opacity: .35; }
}
</style>
"""
