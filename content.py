"""Site copy: products, segments, services and supporting pages. Edit freely.

Copy follows the Leeds website brief v1.1 (3 November 2026), with "onboarding"
used in place of "implementation" throughout.
"""

# Product filters, in display order (brief 5.2)
CATEGORIES = [
    "External audit",
    "Consolidation and reporting",
    "Internal audit and analytics",
    "Cloud platform",
    "AI and automation",
]

PRODUCTS = [
    {
        "name": "Caseware Working Papers",
        "categories": ["External audit", "Consolidation and reporting", "Internal audit and analytics"],
        "tagline": "One engagement file, from trial balance to signed financial statements.",
        "summary": (
            "Plan, perform and review assurance and financial reporting engagements "
            "in one integrated file. Import the trial balance once and every lead "
            "sheet, working paper and financial statement stays in step."
        ),
        "features": [
            "Trial balance import from most accounting and ERP systems",
            "Automatic lead sheets, grouping and adjusting journal entries",
            "Linked financial statements that update as balances change",
            "Sign-off, review notes, issues and full roll-forward each year",
            "Multi-user access with SmartSync for teams working on and off site",
        ],
        "ideal_for": "Audit firms, group finance teams preparing consolidations, accounting practices",
    },
    {
        "name": "Caseware Cloud",
        "categories": ["Cloud platform", "Internal audit and analytics"],
        "tagline": "Your whole practice in one secure workspace, with client requests tracked to closure.",
        "summary": (
            "The cloud platform that connects your practice. Manage engagements, "
            "collaborate with clients and run Caseware cloud apps from a single, "
            "secure workspace available anywhere."
        ),
        "features": [
            "Central engagement and client management",
            "Secure document exchange and client request (PBC) tracking",
            "Role-based permissions and activity history",
            "Firm-wide dashboards across engagements",
            "Works with Working Papers through cloud integration",
        ],
        "ideal_for": "Firms with multiple offices or hybrid teams; internal audit functions working across entities",
    },
    {
        "name": "Caseware Audit International",
        "categories": ["External audit"],
        "tagline": "A risk-based ISA methodology, built in, so every file meets the same standard.",
        "summary": (
            "Guided audit workflows built around the ISAs. The engagement adapts to "
            "the risks you identify, so teams perform the work that matters and "
            "leave out what does not apply."
        ),
        "features": [
            "ISA-aligned methodology content, updated as standards change",
            "Risk assessment that drives the audit programme",
            "Guided procedures, checklists and completion steps",
            "Consistent files across engagements and offices",
            "Integrated review and sign-off",
        ],
        "ideal_for": "Audit firms preparing for quality inspections; firms applying ISQM 1",
    },
    {
        "name": "Caseware Financials (IFRS)",
        "categories": ["Consolidation and reporting"],
        "tagline": "IFRS financial statements straight from the trial balance, with notes that stay in step.",
        "summary": (
            "Produce complete, presentation-ready financial statements directly from "
            "the trial balance. Notes, totals and cross-references stay consistent "
            "automatically, cutting the time spent on formatting and checking."
        ),
        "features": [
            "IFRS and IFRS for SMEs statement formats and disclosures",
            "Statements, notes and schedules linked to the trial balance",
            "Automatic rounding, casting and cross-referencing",
            "Roll forward to next year with comparatives in place",
            "Firm-standard templates for a consistent look",
        ],
        "ideal_for": "Accounting practices, corporate reporting teams, entities filing for UAE Corporate Tax",
    },
    {
        "name": "Group consolidation in Caseware Working Papers",
        "categories": ["Consolidation and reporting"],
        "tagline": "Consolidate entities and produce IFRS group statements in one controlled file.",
        "summary": (
            "Bring each entity's trial balance into one group file, record the "
            "consolidation entries and report on the consolidated balances, with a "
            "clear trail from every entity to the group numbers."
        ),
        "features": [
            "Trial balances for each entity combined in one group file",
            "Intercompany eliminations recorded as consolidation entries",
            "Foreign currency translation for entities reporting in other currencies",
            "Ownership percentages and non-controlling interests",
            "Group financial statements produced from the consolidated balances",
        ],
        "ideal_for": "Group CFOs, financial controllers and reporting managers",
    },
    {
        "name": "Caseware Extractly",
        "categories": ["AI and automation"],
        "tagline": "Smart vouching and reconciliation inside Excel.",
        "summary": (
            "Extract data from invoices, statements and other source documents and "
            "match it against your records automatically, turning hours of manual "
            "vouching into minutes."
        ),
        "features": [
            "Automated data extraction from source documents",
            "Matching of extracted data to ledger records",
            "Works inside Excel, where audit teams already work",
            "Clear exceptions list for follow-up",
        ],
        "ideal_for": "Audit teams doing substantive testing and reconciliations",
    },
    {
        "name": "Caseware Validate",
        "categories": ["AI and automation"],
        "tagline": "AI-powered review of financial statements.",
        "summary": (
            "Check financial statements for casting errors, internal "
            "inconsistencies and prior-year mismatches before they reach the "
            "partner or the client."
        ),
        "features": [
            "Automated casting and cross-checking of statements and notes",
            "Flags inconsistencies within the document",
            "Reduces disclosure risk and review time",
        ],
        "ideal_for": "Reviewers, technical teams and quality control",
    },
    {
        "name": "Caseware AiDA",
        "categories": ["AI and automation"],
        "tagline": "An AI digital assistant built into the Caseware Cloud platform.",
        "summary": (
            "AiDA is Caseware's AI-powered digital assistant, purpose-built for audit "
            "and accounting. It works inside Caseware Cloud, so help is available "
            "in the context of the engagement your team is working on."
        ),
        "features": [
            "Part of the Caseware Cloud platform",
            "Purpose-built for audit and accounting work",
            "Used alongside your existing engagement files",
        ],
        "ideal_for": "Firms using Caseware Cloud. Ask us about availability in the UAE.",
    },
    {
        "name": "Caseware Verity",
        "categories": ["AI and automation"],
        "tagline": "AI engagement intelligence inside your audit workflow.",
        "summary": (
            "AI assistance grounded in the standards and in the context of your "
            "engagement, helping teams draft, research and complete work such as "
            "disclosure checklists more quickly while keeping the auditor in control."
        ),
        "features": [
            "Answers grounded in standards and engagement context",
            "Disclosure checklist drafting with anchored references",
            "Embedded in the engagement rather than a separate tool",
        ],
        "ideal_for": "Firms adopting AI in audit with appropriate oversight",
    },
]

# Home page product highlights (brief 4.4)
HIGHLIGHT_PRODUCTS = ["Caseware Working Papers", "Caseware Cloud", "Caseware Financials (IFRS)"]

# Five target segments (brief 2, 4.2 and 6). Each becomes a page under "Who it's for".
SEGMENTS = [
    {
        "slug": "audit-firms",
        "nav": "Audit firms",
        "tile": "Run every audit on a risk-based ISA methodology, with one engagement file from planning to opinion.",
        "seo_title": "ISA Audit Software for UAE Audit Firms · Caseware",
        "headline": "Every audit file inspection-ready, by design",
        "sub": (
            "Caseware gives UAE audit firms a risk-based, ISA-aligned methodology inside one "
            "engagement file. Your teams follow the same standard on every job, and your "
            "reviewers see exactly how risk drove the work."
        ),
        "challenges": [
            ("Inconsistent files", "Different teams, different templates, different standards of documentation."),
            ("Inspection pressure", "Reviewers expect a clear link from risk assessment to procedures to evidence."),
            ("Wasted hours", "Spreadsheets re-keyed, lead sheets rebuilt and files re-created every year."),
        ],
        "solves": [
            ("ISA methodology built in", "Programmes adapt to the risks you identify, so teams do the work that matters and document why."),
            ("One engagement file", "Trial balance, lead sheets, working papers, adjustments and financial statements stay linked."),
            ("Review you can see", "Preparer and reviewer sign-offs, review notes and issues tracked to clearance."),
            ("ISQM 1 support", "Standardised files and review evidence support your firm's system of quality management."),
            ("Group audits", "Structure component work and group reporting in line with ISA 600 (Revised)."),
            ("Roll forward in minutes", "Last year's mapping, documents and structure carry over."),
        ],
        "products": ["Caseware Audit International", "Caseware Working Papers", "Caseware Cloud"],
        "faqs": [
            (
                "Is Caseware aligned with International Standards on Auditing?",
                "Yes. Caseware Audit International provides a risk-based audit methodology aligned with the ISAs, "
                "and its content is updated as the standards change.",
            ),
            (
                "Can we add our firm's own templates and UAE-specific procedures?",
                "Yes. Engagement files can be tailored with your firm's templates, and we set up UAE-specific "
                "procedures and disclosures with you as part of onboarding.",
            ),
            (
                "How long does onboarding take for a firm of 20, 50 or 100 staff?",
                "It depends on the number of users, the templates you need and the prior-year files to bring across. "
                "We agree a plan and timetable with you before you start.",
            ),
            (
                "Can we migrate prior-year files from Excel?",
                "Yes. Our migration service brings prior-year balances, mapping and Excel templates into Caseware.",
            ),
            (
                "Where is our client data stored?",
                "Working Papers files are stored on your own computers or network. Caseware Cloud is hosted by "
                "Caseware on Amazon Web Services. See our Trust and data security page for details.",
            ),
        ],
        "cta": "Book an audit-methodology demo",
    },
    {
        "slug": "consolidation",
        "nav": "Group consolidation",
        "tile": "Consolidate entities, eliminate intercompany balances and produce IFRS group statements in one controlled file.",
        "seo_title": "Group Consolidation Software UAE · Caseware",
        "headline": "Close the group faster, with every elimination accounted for",
        "sub": (
            "Consolidate subsidiaries, eliminate intercompany balances and produce IFRS group "
            "financial statements in one controlled file, with a clear trail from each entity's "
            "trial balance to the group numbers."
        ),
        "challenges": [
            ("Fragile workbooks", "Consolidation workbooks that only one person understands."),
            ("Late surprises", "Intercompany differences found late, delaying the close."),
            ("Manual disclosures", "Group disclosures rebuilt by hand every year."),
        ],
        "solves": [
            ("Multi-entity import", "Bring in each entity's trial balance from its own accounting or ERP system."),
            ("Intercompany eliminations", "Record elimination entries in the group file, with a trail back to each entity."),
            ("Foreign currency translation", "Translate entities that report outside the UAE or in other currencies."),
            ("Ownership and NCI", "Reflect ownership percentages and non-controlling interests."),
            ("IFRS group statements", "Produce group financial statements and notes from the consolidated balances."),
        ],
        "products": ["Caseware Working Papers", "Caseware Financials (IFRS)"],
        "faqs": [
            (
                "Can we import trial balances from different accounting systems?",
                "Yes. Each entity's trial balance can be imported from most accounting and ERP systems, "
                "or from Excel and text files.",
            ),
        ],
        "cta": "Book a consolidation demo",
    },
    {
        "slug": "internal-audit",
        "nav": "Internal audit",
        "tile": "Plan, perform and report internal audits with structured working papers and a full review trail.",
        "seo_title": "Internal Audit Software UAE · Caseware",
        "headline": "Internal audit with the rigour of external audit",
        "sub": (
            "Give your internal audit function a risk-based plan, structured working papers and "
            "a review trail your audit committee can rely on."
        ),
        "challenges": [
            ("Plans disconnected from the work", "The annual plan lives in one place and the fieldwork in another."),
            ("Evidence spread everywhere", "Working papers scattered across email and shared drives."),
            ("Findings that drift", "Management responses and follow-up are hard to track to closure."),
        ],
        "solves": [
            ("Risk-based plan", "An annual audit plan linked to each engagement."),
            ("Standard programmes", "Standardised programmes and controls-testing templates."),
            ("Findings tracked to closure", "Findings, management responses and follow-up in one place."),
            ("Committee reporting", "Report to the audit committee from the same file."),
            ("Standards alignment", "Supports alignment with the IIA Global Internal Audit Standards."),
        ],
        "products": ["Caseware Working Papers", "Caseware Cloud"],
        "faqs": [],
        "cta": "Book an internal audit demo",
    },
    {
        "slug": "audit-quality",
        "nav": "Regulators and audit quality",
        "tile": "A common, ISA-aligned methodology that makes audit files consistent and easier to inspect.",
        "seo_title": "Audit Quality & ISA Methodology in the UAE · Caseware",
        "headline": "Raising audit quality across the UAE",
        "sub": (
            "When audit firms work on a consistent, ISA-aligned methodology, files are easier to "
            "inspect, quality issues are easier to find, and standards rise across the profession."
        ),
        "challenges": [],
        "solves": [
            (
                "For audit oversight bodies",
                "What a standardised Caseware file shows an inspector: risk assessment, materiality, "
                "linked procedures, evidence and reviewer sign-off.",
            ),
            (
                "For public sector audit institutions",
                "Manage audits of government entities on a documented, consistent methodology.",
            ),
            (
                "Briefings for regulators",
                "Leeds offers confidential, no-obligation briefings on how methodology software supports "
                "audit quality programmes.",
            ),
        ],
        "products": ["Caseware Audit International", "Caseware Working Papers"],
        "faqs": [],
        "cta": "Request a regulator briefing",
        "disclaimer": (
            "References to UAE authorities describe the regulatory environment only. "
            "No authority endorses or recommends any software product."
        ),
    },
    {
        "slug": "accounting-practices",
        "nav": "Accounting practices",
        "tile": "Produce IFRS and IFRS for SMEs statements straight from the trial balance, ready for Corporate Tax.",
        "seo_title": "IFRS Financial Statements Software UAE · Caseware",
        "headline": "Year-end accounts for every client, done right the first time",
        "sub": (
            "Prepare IFRS and IFRS for SMEs financial statements straight from the trial balance, "
            "including the year-end accounts UAE companies need for shareholders, banks, free zone "
            "authorities and Corporate Tax filing."
        ),
        "challenges": [],
        "solves": [
            (
                "UAE Corporate Tax",
                "Corporate Tax has increased the number of UAE entities that need IFRS financial statements. "
                "Caseware Financials produces them consistently across your client base.",
            ),
            ("Straight from the trial balance", "Statements, notes and schedules stay linked to each client's balances."),
            ("Fewer errors", "Automatic rounding, casting and cross-referencing, with Caseware Validate as a final check."),
            ("Next year in minutes", "Roll each client forward with comparatives in place."),
        ],
        "products": ["Caseware Financials (IFRS)", "Caseware Working Papers", "Caseware Validate"],
        "faqs": [],
        "cta": "Book a demo",
    },
]

# Home page "Why UAE firms choose Caseware" panel (brief 4.3, interim figures until UAE numbers exist)
PROOF_STATS = [
    ("ISA · IFRS · IFRS for SMEs", "standards built into the content"),
    ("Cloud and desktop", "work the way your team prefers"),
    ("Local licensing and support", "from a team based in the UAE"),
    ("Certified trainers", "for every role, from new users to methodology leads"),
]

# Home page "What's changing" cards (brief 4.6): (title, text, link)
CHANGES = [
    (
        "IFRS 18, effective 1 January 2027",
        "New presentation and disclosure requirements for IFRS financial statements, for annual periods "
        "beginning on or after 1 January 2027.",
        "accounting-practices",
    ),
    (
        "ISQM 1 and audit quality inspections",
        "Show your quality system is working, file by file.",
        "audit-firms",
    ),
    (
        "Corporate Tax and audited financial statements",
        "More UAE entities now need IFRS financial statements. Produce them faster and consistently.",
        "accounting-practices",
    ),
]

# Why Caseware comparison table (brief 7.1). Do not name competing vendors.
COMPARISON = [
    ("Audit methodology", "Depends on each team's templates", "Risk-based ISA methodology built into every file"),
    ("Link from risk to evidence", "Manual cross-referencing", "Risks, procedures and evidence linked in one file"),
    ("Trial balance to financial statements", "Re-keyed and re-checked", "Imported once; lead sheets and statements update automatically"),
    ("Review trail", "Comments in emails and margins", "Sign-offs, review notes and issues tracked to clearance"),
    ("Next year's file", "Rebuilt from scratch", "Rolled forward in minutes"),
    ("Inspection readiness", "Varies by engagement", "Consistent structure across every engagement"),
    ("Local support", "None", "Leeds team in the UAE"),
]

SERVICES = [
    ("Licensing & renewals", "New licences, extra users and renewals, quoted and invoiced in AED by a UAE entity."),
    ("Onboarding", "A structured onboarding plan: installation, firm templates, user roles and your first live engagement."),
    ("Training", "Classroom and online training for every role, from first-time users to methodology leads."),
    ("Templates & customisation", "Firm-standard templates, UAE-specific procedures and disclosures tailored to your practice."),
    ("Local support", "Support from a UAE team on working days."),
    ("Product advice", "An independent review of your current process and a recommendation on the right products and licences."),
    ("Migration", "Move prior-year files and Excel templates into Caseware, with balances and mapping carried over."),
    ("Methodology health check", "An annual review of how your teams use the methodology, ahead of quality inspections."),
]

# Insights topics (brief 9.7). Shown as upcoming until each article is published.
INSIGHTS = [
    ("IFRS 18: what changes for UAE financial statements in 2027", "accounting-practices"),
    ("What a well-documented ISA audit file looks like", "audit-firms"),
    ("ISQM 1 in practice for small and mid-sized UAE firms", "audit-firms"),
    ("Consolidation in the UAE: common errors and how to avoid them", "consolidation"),
    ("Corporate Tax and the rising demand for IFRS financial statements", "accounting-practices"),
    ("Internal audit planning against the Global Internal Audit Standards", "internal-audit"),
]

# Customer resources (moved from the old Knowledge hub, brief 7.3)
GUIDES = [
    (
        "Preparing your trial balance for import",
        "Export account number, description and closing balance, and check that the total balances. "
        "Keep account numbers the same from year to year so last year's mapping carries over.",
    ),
    (
        "Map each account once",
        "Assign every account to a group so lead sheets and financial statements fill in automatically. "
        "In later years only new accounts need attention.",
    ),
    (
        "Record adjustments in the file",
        "Post adjusting and reclassifying entries in Working Papers rather than in a separate spreadsheet, "
        "so lead sheets and statements always agree with the adjusted trial balance.",
    ),
    (
        "Review with sign-offs and notes",
        "Use preparer and reviewer sign-offs on each document and raise review notes inside the file, "
        "so open points are visible and cleared before completion.",
    ),
    (
        "Close the file properly",
        "At the end of the engagement, clear outstanding notes, clean up and lock down the file "
        "so the final version is protected.",
    ),
    (
        "Roll forward for next year",
        "Start the new year from the completed file. Closing balances become comparatives and your "
        "documents and mapping are kept, so the team is not rebuilding the file each year.",
    ),
]

FAQS = [
    (
        "What is Caseware Working Papers?",
        "Software for assurance and financial reporting engagements. It brings the trial balance, "
        "working papers and financial statements together in one engagement file.",
    ),
    (
        "Can we import a trial balance from our accounting system?",
        "Yes. Trial balances can be imported from many accounting packages, and from Excel or text files.",
    ),
    (
        "Which reporting frameworks are covered?",
        "The Financials content covers IFRS and IFRS for SMEs. Contact us to confirm the content "
        "available for your requirements.",
    ),
    (
        "Is it desktop or cloud?",
        "Working Papers is installed on your computers. Caseware Cloud is an online platform, and the two "
        "can be connected so teams can share and manage engagement files online.",
    ),
    (
        "Do you provide training?",
        "Yes. We offer training for new and existing users. Contact us to discuss what your team needs.",
    ),
    (
        "How do I get a demo or a quote?",
        "Send us your details through the Contact page and we will get back to you.",
    ),
]

RESOURCE_LINKS = [
    ("Caseware blog", "Articles from Caseware on audit, accounting and technology.", "https://www.caseware.com/resources/blog"),
    ("Caseware support", "Caseware's customer support page.", "https://www.caseware.com/support"),
    ("MyCaseware", "Sign in to your Caseware account.", "https://my.caseware.com/"),
]

# Caseware Cloud security facts, as published at caseware.com/legal/security-certifications
SECURITY_FACTS = [
    ("ISO/IEC 27001:2022", "Caseware Cloud's information security management system is certified to ISO/IEC 27001:2022 by an independent auditor."),
    ("SOC 2 Type 2", "Caseware has obtained a SOC 2 Type 2 report on the controls over Caseware Cloud."),
    ("Hosted on Amazon Web Services", "Caseware Cloud runs on AWS, which holds its own ISO and SOC certifications for its data centres."),
    ("Encrypted in transit", "Data moving to and from the service, including backups, is encrypted (AES-256 over SSL)."),
    ("Separated by design", "Each customer's data is logically separated through database isolation."),
    ("Independently tested", "Regular third-party audits, external penetration testing and internal vulnerability testing."),
]

# Retained for the About page
WHY_US = [
    ("Local presence", "A UAE-based team for sales, onboarding and support."),
    ("Global standard", "Software used by audit and accounting professionals in 130 countries."),
    ("End-to-end", "From trial balance to signed financial statements in one connected workflow."),
    ("Quality & consistency", "Standardised files and methodology that stand up to regulatory review."),
]
