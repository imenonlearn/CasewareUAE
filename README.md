# Caseware UAE website (Streamlit)

## Files

| File | What it is |
| --- | --- |
| `app.py` | The website (pages, layout, styling) |
| `site_config.py` | Your company name, email, phone, address - **edit this first** |
| `content.py` | Product, solution and service text |
| `styles.py` | Colours, fonts and section styling |
| `assets/logo.png`, `assets/logo_white.png` | Optional: the official Caseware logo (dark text for the header, white text for the footer). Until these exist the site shows a plain text wordmark |
| `requirements.txt` | Tells Streamlit Cloud what to install |
| `.streamlit/config.toml` | Colours and theme |

## Run on your PC

```bash
python -m streamlit run app.py
```

## Publish free on Streamlit Community Cloud

1. Sign in at https://github.com (create a free account if you do not have one).
2. Create a new **public** repository, e.g. `casewareuae`.
3. On the repository page choose **Add file > Upload files** and drag in everything
   inside this folder, including the `.streamlit` folder. Commit.
4. Go to https://share.streamlit.io and sign in with GitHub.
5. Click **Create app > Deploy a public app from GitHub**, then set:
   - Repository: `your-username/casewareuae`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: `casewareuae` (gives you `https://casewareuae.streamlit.app`)
6. Click **Deploy**. The site is live in a couple of minutes.

To update the site later, edit the files on GitHub; Streamlit redeploys automatically.

## Using casewareuae.com

Streamlit Community Cloud only serves apps on `*.streamlit.app` addresses and does
not support custom domains. To use `casewareuae.com`:

1. Register the domain with a registrar (this is a paid, yearly fee).
2. In the registrar's settings, add **domain forwarding** (a 301 redirect) from
   `casewareuae.com` and `www.casewareuae.com` to `https://casewareuae.streamlit.app`.

Visitors who type `casewareuae.com` land on the site; the address bar then shows the
`streamlit.app` address.
