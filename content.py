"""Site copy: products, solutions and services. Edit freely."""

PRODUCTS = [
    {
        "name": "Caseware Working Papers",
        "category": "Audit & Assurance",
        "tagline": "The engagement file trusted by audit and accounting firms worldwide.",
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
        "ideal_for": "Audit firms, accounting practices and corporate finance teams",
    },
    {
        "name": "Caseware IDEA",
        "category": "Data Analytics",
        "tagline": "Analyse 100% of your data, not just a sample.",
        "summary": (
            "A data analysis tool built for auditors, accountants and finance "
            "professionals. Import data from almost any source, test entire "
            "populations and document every step for your audit file."
        ),
        "features": [
            "Import from ERPs, databases, spreadsheets, PDFs and print reports",
            "Built-in audit tests: duplicates, gaps, Benford's Law, stratification, ageing",
            "Statistical and monetary unit sampling",
            "Read-only source data with a complete history log of every action",
            "Automate repeat tests with IDEAScript, Python and visual workflows",
        ],
        "ideal_for": "External and internal auditors, fraud examiners, tax and compliance teams",
    },
    {
        "name": "Caseware Cloud",
        "category": "Platform",
        "tagline": "One secure hub for your engagements, clients and staff.",
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
        "ideal_for": "Firms that want to work and collaborate from anywhere",
    },
    {
        "name": "Caseware Audit International",
        "category": "Audit & Assurance",
        "tagline": "A risk-based audit methodology aligned to International Standards on Auditing.",
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
        "ideal_for": "Audit firms performing ISA audits of any size",
    },
    {
        "name": "Caseware Financials (IFRS)",
        "category": "Financial Reporting",
        "tagline": "Financial statements prepared faster, with fewer errors.",
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
        "ideal_for": "Accounting firms and finance teams preparing annual accounts",
    },
    {
        "name": "Caseware Extractly",
        "category": "AI & Automation",
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
        "category": "AI & Automation",
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
        "name": "Caseware Verity",
        "category": "AI & Automation",
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

SOLUTIONS = [
    {
        "title": "Audit & assurance firms",
        "text": (
            "Run ISA-compliant audits from planning to completion with a "
            "risk-based methodology, a single engagement file and built-in review."
        ),
        "products": ["Caseware Working Papers", "Caseware Audit International", "Caseware IDEA", "Caseware Cloud"],
    },
    {
        "title": "Accounting & financial reporting",
        "text": (
            "Prepare IFRS and IFRS for SMEs financial statements straight from the "
            "trial balance, including the year-end accounts UAE companies need for "
            "shareholders, banks, free zone authorities and corporate tax filing."
        ),
        "products": ["Caseware Working Papers", "Caseware Financials (IFRS)", "Caseware Validate"],
    },
    {
        "title": "Internal audit & compliance",
        "text": (
            "Test complete populations of transactions, find anomalies and "
            "control failures, and repeat the same tests every period."
        ),
        "products": ["Caseware IDEA", "Caseware Working Papers"],
    },
    {
        "title": "Government & regulators",
        "text": (
            "Give public sector audit and inspection teams a consistent, "
            "documented way to analyse data and manage engagements."
        ),
        "products": ["Caseware IDEA", "Caseware Working Papers", "Caseware Cloud"],
    },
]

SERVICES = [
    ("Licensing & renewals", "New licences, additional users and annual renewals, quoted and invoiced locally."),
    ("Implementation", "Installation, configuration and firm set-up so your team is productive from day one."),
    ("Training", "Hands-on training for Working Papers and IDEA, from first-time users to advanced topics."),
    ("Templates & customisation", "Firm-standard financial statement and working paper templates tailored to your practice."),
    ("Local support", "Help from a team in your time zone that understands UAE reporting requirements."),
    ("Data analytics assistance", "Support in designing and automating IDEA tests for audit and compliance work."),
]

WHY_US = [
    ("Local presence", "A UAE-based team for sales, onboarding and support."),
    ("Global standard", "Software used by audit and accounting professionals in 130 countries."),
    ("End-to-end", "From trial balance to signed financial statements in one connected workflow."),
    ("Quality & consistency", "Standardised files and methodology that stand up to regulatory review."),
]
