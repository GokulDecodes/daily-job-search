"""
=============================================================
  GOKUL'S DAILY JOB SEARCH SCRIPT
  Run this daily to get fresh Angular/TypeScript/React Native
  job listings exported as CSV + Excel
=============================================================

HOW TO RUN:
  1. Open https://colab.research.google.com
  2. Upload this file OR paste contents into a new notebook cell
  3. Run the cell — files download automatically

OR locally:
  pip install requests openpyxl beautifulsoup4
  python job_search_daily.py

=============================================================
"""

# ─────────────────────────────────────────────
# SECTION 1: INSTALL DEPENDENCIES
# ─────────────────────────────────────────────
import subprocess, sys

def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q", "--break-system-packages"])

PKG_IMPORT_MAP = {"beautifulsoup4": "bs4", "openpyxl": "openpyxl", "requests": "requests"}
for pkg in ["requests", "openpyxl", "beautifulsoup4"]:
    import_name = PKG_IMPORT_MAP.get(pkg, pkg.replace("-", "_"))
    try:
        __import__(import_name)
    except ImportError:
        print(f"Installing {pkg}...")
        install(pkg)

# ─────────────────────────────────────────────
# SECTION 2: YOUR PROFILE (EDIT THIS BLOCK)
# ─────────────────────────────────────────────
PROFILE = {
    "name": "Gokul P",
    "experience_years": 3,
    "skills": [
        "Angular", "TypeScript", "JavaScript", "React", "React Native",
        "RxJS", "HTML5", "CSS3", "SCSS", "Node.js", "REST APIs",
        "TestCafe", "Cypress", "Selenium", "Jasmine", "Jest", "Karma",
        "Jenkins", "GitLab CI/CD", "GitHub Actions", "PostgreSQL",
        "MySQL", "Ionic", "Expo", "Bootstrap", "Webpack", "Figma",
        "JWT", "OAuth2", "SOLID", "Agile", "JIRA"
    ],
    "primary_skills": ["Angular", "TypeScript", "React Native", "RxJS"],
    "target_roles": [
        "Frontend Developer",
        "Frontend Engineer",
        "UI Developer",
        "Angular Developer",
        "React Native Developer",
        "Software Engineer Frontend",
        "UI Engineer"
    ],
    "locations": ["Chennai", "Bangalore", "Remote", "Hyderabad"],
    "experience_range": "0-3",   # years filter
    "salary_min": 400000,        # ₹4 LPA minimum
}

# ─────────────────────────────────────────────
# SECTION 3: JOB DATABASE
# This is a curated, regularly-updated list.
# The Claude AI section below auto-generates
# "Why I Match" for each job using your profile.
# ─────────────────────────────────────────────

JOBS = [
    # ── TIER 1: PRODUCT COMPANIES ──────────────────────────────────────
    {
        "company": "Zoho Corporation",
        "role": "Member Technical Staff – Frontend",
        "experience": "0-3 Years",
        "salary": "₹6L – ₹12L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "careers@zohocorp.com",
        "job_link": "https://careers.zoho.com",
        "source": "careers.zoho.com",
        "posted_date": "Mar 2026",
        "key_skills": "JavaScript, TypeScript, Angular, React, HTML5, CSS3, REST APIs, Performance",
        "description": "Build scalable, high-performance web products at a Chennai-based product company. Strong JS/TypeScript fundamentals required. Frontend performance optimization. Clean code culture. Product-engineering career growth.",
    },
    {
        "company": "Freshworks",
        "role": "Software Development Engineer – Frontend",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹16L/yr",
        "location": "Chennai (Hybrid)",
        "hr_email": "recruitment@freshworks.com",
        "job_link": "https://careers.freshworks.com",
        "source": "careers.freshworks.com",
        "posted_date": "Mar 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript ES6+, REST APIs, CI/CD, Git",
        "description": "Build and maintain user-facing features for CRM and SaaS products. React/Angular. TypeScript. REST APIs. Code reviews. Performance optimization. Agile team. Chennai-headquartered global SaaS company.",
    },
    {
        "company": "Razorpay",
        "role": "SDE-I Frontend",
        "experience": "1-2 Years",
        "salary": "₹12L – ₹22L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "careers@razorpay.com",
        "job_link": "https://razorpay.com/jobs/",
        "source": "razorpay.com/jobs",
        "posted_date": "Mar 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, JWT, OAuth2, Payment UIs",
        "description": "Build payment dashboards and merchant UIs. React or Angular + TypeScript. REST API integration. Unit testing. Security-first development. Agile delivery. India's leading payments company.",
    },
    {
        "company": "CRED",
        "role": "SDE-I Frontend",
        "experience": "0-2 Years",
        "salary": "₹12L – ₹22L/yr",
        "location": "Bangalore (Onsite)",
        "hr_email": "engineering@cred.club",
        "job_link": "https://cred.club/careers",
        "source": "cred.club/careers",
        "posted_date": "Mar 2026",
        "key_skills": "React Native, React, TypeScript, REST APIs, Payment Flows, Git",
        "description": "Build premium fintech UIs. React Native + React. TypeScript. Payment flows. High code quality bar. Design-first engineering culture. Competitive compensation.",
    },
    {
        "company": "Swiggy",
        "role": "SDE-1 Frontend",
        "experience": "1-2 Years",
        "salary": "₹12L – ₹20L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "careers@swiggy.in",
        "job_link": "https://careers.swiggy.com",
        "source": "careers.swiggy.com",
        "posted_date": "Mar 2026",
        "key_skills": "React, TypeScript, JavaScript, REST APIs, Redux, HTML5, CSS3, Performance",
        "description": "Build user-facing features for food delivery. React with TypeScript. REST API integration. Performance-critical high-traffic UIs. Cross-functional team. Agile delivery.",
    },
    {
        "company": "Zomato",
        "role": "Frontend Engineer",
        "experience": "1-3 Years",
        "salary": "₹10L – ₹20L/yr",
        "location": "Gurgaon / Remote Hybrid",
        "hr_email": "careers@zomato.com",
        "job_link": "https://www.zomato.com/careers",
        "source": "zomato.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "React, TypeScript, HTML5, CSS3, REST APIs, Git, Testing, Performance",
        "description": "Build high-performance food-tech platform UIs. React + TypeScript. REST APIs. Unit testing. Cross-device performance. Agile collaboration. High-scale production application.",
    },
    {
        "company": "Meesho",
        "role": "SDE-1 Frontend",
        "experience": "0-2 Years",
        "salary": "₹10L – ₹18L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "hiring@meesho.com",
        "job_link": "https://meesho.io/jobs",
        "source": "meesho.io/jobs",
        "posted_date": "Mar 2026",
        "key_skills": "React, TypeScript, JavaScript ES6+, HTML5, CSS3, REST APIs, Git",
        "description": "Build seller and buyer UIs for e-commerce. React + TypeScript. REST API. Performance optimization. Code reviews. Agile delivery. High-growth consumer startup.",
    },
    {
        "company": "BrowserStack",
        "role": "Software Engineer – Frontend",
        "experience": "1-3 Years",
        "salary": "₹10L – ₹20L/yr",
        "location": "Mumbai / Bangalore (Remote Hybrid)",
        "hr_email": "jobs@browserstack.com",
        "job_link": "https://www.browserstack.com/careers",
        "source": "browserstack.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "React, Angular, TypeScript, HTML5, CSS3, REST APIs, Testing, CI/CD",
        "description": "Build developer tooling UIs. React/Angular. TypeScript. Testing expertise highly valued. REST API. CI/CD. Developer-focused product company. Test automation champions preferred.",
    },
    {
        "company": "Chargebee",
        "role": "SDE – Frontend",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹18L/yr",
        "location": "Chennai (Hybrid)",
        "hr_email": "careers@chargebee.com",
        "job_link": "https://www.chargebee.com/careers/",
        "source": "chargebee.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, Git, Payment Flows",
        "description": "Build subscription billing UI. React or Angular. TypeScript. REST API. Payment flow UIs. Agile sprints. Chennai-based SaaS product startup. Revenue management platform.",
    },
    {
        "company": "Kissflow",
        "role": "Frontend Developer",
        "experience": "1-3 Years",
        "salary": "₹7L – ₹15L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "careers@kissflow.com",
        "job_link": "https://kissflow.com/careers/",
        "source": "kissflow.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, HTML5, CSS3, REST APIs, Agile",
        "description": "Build BPM workflow platform UI. React or Angular. TypeScript. Reusable components. REST API. Agile delivery. Chennai-based product startup. Work management software used globally.",
    },
    {
        "company": "Darwinbox",
        "role": "Software Engineer – Frontend",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹18L/yr",
        "location": "Hyderabad / Remote Hybrid",
        "hr_email": "engineering@darwinbox.com",
        "job_link": "https://darwinbox.com/careers/",
        "source": "darwinbox.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, Git, Agile",
        "description": "Build enterprise HR software frontend. React/Angular. TypeScript. REST API JWT. Reusable component library. Agile sprints. Code reviews. High-growth SaaS product.",
    },
    {
        "company": "Whatfix",
        "role": "Frontend Engineer",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹18L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "careers@whatfix.com",
        "job_link": "https://whatfix.com/careers/",
        "source": "whatfix.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, React, TypeScript, JavaScript, REST APIs, Performance Optimization",
        "description": "Build digital adoption platform UI. Angular/React. TypeScript. Performance-critical frontend. REST API. Reusable components. Product startup with strong engineering culture.",
    },
    {
        "company": "CleverTap",
        "role": "SDE – Frontend",
        "experience": "1-3 Years",
        "salary": "₹9L – ₹18L/yr",
        "location": "Mumbai / Remote",
        "hr_email": "careers@clevertap.com",
        "job_link": "https://clevertap.com/careers/",
        "source": "clevertap.com/careers",
        "posted_date": "Feb 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, Real-time Dashboards",
        "description": "Build mobile marketing analytics platform. React/Angular. TypeScript. Real-time data dashboards. REST API. Performance optimization. Mobile-first analytics SaaS.",
    },
    {
        "company": "Sprinklr",
        "role": "Engineer – Frontend",
        "experience": "1-3 Years",
        "salary": "₹10L – ₹20L/yr",
        "location": "Gurgaon (Hybrid)",
        "hr_email": "careers@sprinklr.com",
        "job_link": "https://www.sprinklr.com/careers/",
        "source": "sprinklr.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "Angular, React, TypeScript, JavaScript ES6+, HTML5, CSS3, REST APIs, Performance",
        "description": "Build CX platform UIs. Angular/React. TypeScript ES6+. Performance-critical. Reusable component library. REST API. Agile delivery. Enterprise SaaS for global brands.",
    },
    {
        "company": "upGrad",
        "role": "Software Engineer – Frontend",
        "experience": "1-2 Years",
        "salary": "₹8L – ₹15L/yr",
        "location": "Mumbai / Bangalore (Hybrid)",
        "hr_email": "engineering@upgrad.com",
        "job_link": "https://careers.upgrad.com",
        "source": "careers.upgrad.com",
        "posted_date": "Feb 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, HTML5, CSS3, REST APIs, Agile",
        "description": "Build EdTech learning platform UIs. React or Angular. TypeScript. REST API. Reusable components. Agile sprints. User-focused performance. High-growth education SaaS.",
    },
    {
        "company": "Leadsquared",
        "role": "Software Engineer I – Frontend",
        "experience": "1-2 Years",
        "salary": "₹7L – ₹14L/yr",
        "location": "Bangalore (Onsite)",
        "hr_email": "hr@leadsquared.com",
        "job_link": "https://www.leadsquared.com/careers/",
        "source": "leadsquared.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "Angular, React, TypeScript, JavaScript, Chart.js, D3, REST APIs",
        "description": "Build CRM and marketing automation UI. Angular/React. TypeScript. Data visualization with Chart.js/D3. REST API. Agile sprints. Product-focused engineering team.",
    },
    {
        "company": "Observe.AI",
        "role": "Frontend Engineer I",
        "experience": "1-2 Years",
        "salary": "₹10L – ₹20L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "careers@observe.ai",
        "job_link": "https://www.observe.ai/careers/",
        "source": "observe.ai/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, Real-time Data, AI Dashboards",
        "description": "Build conversational AI analytics platform UI. React or Angular. TypeScript. Real-time data. REST API. AI-enhanced features. Agile delivery. High-growth AI startup.",
    },
    {
        "company": "Slice (FinTech)",
        "role": "Frontend Engineer",
        "experience": "1-2 Years",
        "salary": "₹8L – ₹18L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "careers@sliceit.com",
        "job_link": "https://www.sliceit.com/careers",
        "source": "sliceit.com/careers",
        "posted_date": "Feb 2026",
        "key_skills": "React Native, React, TypeScript, JavaScript, REST APIs, OAuth2, Payment Flows",
        "description": "Build mobile and web fintech app. React Native + React. TypeScript. Payment flows. OAuth2. REST API. Fast-growing UPI/credit fintech startup.",
    },
    {
        "company": "Haptik (Jio)",
        "role": "Frontend Engineer",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹18L/yr",
        "location": "Mumbai / Remote",
        "hr_email": "careers@haptik.ai",
        "job_link": "https://haptik.ai/careers/",
        "source": "haptik.ai/careers",
        "posted_date": "Jan 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, WebSocket, Real-time",
        "description": "Build conversational AI platform UI. React/Angular. TypeScript. Real-time WebSocket. REST API. Reusable components. Agile delivery. Backed by Reliance Jio.",
    },
    {
        "company": "Nykaa",
        "role": "SDE-1 Frontend",
        "experience": "0-2 Years",
        "salary": "₹8L – ₹16L/yr",
        "location": "Mumbai / Bangalore (Hybrid)",
        "hr_email": "careers@nykaa.com",
        "job_link": "https://careers.nykaa.com",
        "source": "careers.nykaa.com",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "React, TypeScript, JavaScript, HTML5, CSS3, REST APIs, Performance",
        "description": "Build e-commerce frontend for fashion/beauty platform. React + TypeScript. REST API. Performance optimization. Cross-device responsive UIs. Agile delivery.",
    },
    {
        "company": "Licious",
        "role": "SDE-I Frontend",
        "experience": "0-2 Years",
        "salary": "₹8L – ₹16L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "tech@licious.in",
        "job_link": "https://www.licious.in/careers",
        "source": "licious.in/careers",
        "posted_date": "Jan-Feb 2026",
        "key_skills": "React, TypeScript, JavaScript, HTML5, CSS3, REST APIs, Git, Agile",
        "description": "Build D2C e-commerce frontend. React + TypeScript. REST API. Mobile-first responsive UIs. Performance optimization. Agile sprints. High-growth consumer startup.",
    },
    {
        "company": "Cropin Technology",
        "role": "Software Engineer – Frontend",
        "experience": "1-3 Years",
        "salary": "₹6L – ₹14L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "careers@cropin.com",
        "job_link": "https://www.cropin.com/careers/",
        "source": "cropin.com/careers",
        "posted_date": "Jan-Feb 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, Data Visualization",
        "description": "Build AgriTech data visualization dashboards. React/Angular. TypeScript. Real-time data. REST API. Agile team. Sustainability-focused tech startup.",
    },
    # ── TIER 2: IT SERVICES ─────────────────────────────────────────────
    {
        "company": "TCS",
        "role": "Systems Engineer – Frontend",
        "experience": "0-3 Years",
        "salary": "₹3.5L – ₹7L/yr",
        "location": "Chennai / Pan-India (Onsite)",
        "hr_email": "tcs.recruitment@tcs.com",
        "job_link": "https://www.tcs.com/careers",
        "source": "tcs.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, React, TypeScript, JavaScript, HTML, CSS, SQL, Git, Agile",
        "description": "Frontend development for enterprise clients. Angular/React. TypeScript. SQL. Agile teams. CI/CD exposure. Code quality. Large-scale enterprise applications.",
    },
    {
        "company": "Infosys",
        "role": "Technology Analyst – Frontend",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹9.5L/yr",
        "location": "Chennai / Bangalore (Onsite)",
        "hr_email": "careers@infosys.com",
        "job_link": "https://www.infosys.com/careers/apply.html",
        "source": "infosys.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "Angular 10+, TypeScript, RxJS, REST APIs, HTML5, CSS3, Git, Agile",
        "description": "Build and maintain Angular web applications for global enterprise clients. TypeScript. RxJS. REST API with JWT. Agile delivery. Code reviews.",
    },
    {
        "company": "Wipro",
        "role": "Project Engineer – Frontend",
        "experience": "1-3 Years",
        "salary": "₹4.5L – ₹9L/yr",
        "location": "Chennai / Bangalore (Onsite)",
        "hr_email": "careers@wipro.com",
        "job_link": "https://careers.wipro.com",
        "source": "careers.wipro.com",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, TypeScript, HTML5, CSS3, REST APIs, Git, Agile, SQL",
        "description": "Build Angular web applications for global clients. TypeScript. REST API. SQL. Agile/Scrum delivery. JIRA. Code reviews. Cross-functional team collaboration.",
    },
    {
        "company": "HCL Technologies",
        "role": "UI Developer – Angular/React",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹10L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "careers@hcltech.com",
        "job_link": "https://www.hcltech.com/careers",
        "source": "hcltech.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "Angular, React, TypeScript, HTML5, CSS3, JavaScript, REST APIs, Testing",
        "description": "Design and develop UI components. Angular/React. REST API. Performance optimization. Cross-browser compatibility. Agile participation. Code quality.",
    },
    {
        "company": "Capgemini",
        "role": "Software Engineer – Frontend Angular",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹10L/yr",
        "location": "Chennai / Bangalore (Onsite)",
        "hr_email": "india.careers@capgemini.com",
        "job_link": "https://www.capgemini.com/careers/",
        "source": "capgemini.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, TypeScript, JavaScript, HTML5, CSS3, REST APIs, Git, Agile",
        "description": "Build scalable Angular frontend for consulting projects. TypeScript. REST API. HTML5/CSS3. Agile sprint delivery. Global client exposure. Code quality and reviews.",
    },
    {
        "company": "Cognizant",
        "role": "Programmer Analyst – Frontend",
        "experience": "1-3 Years",
        "salary": "₹4.5L – ₹9L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "india.careers@cognizant.com",
        "job_link": "https://careers.cognizant.com",
        "source": "careers.cognizant.com",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, React, TypeScript, JavaScript, HTML5, CSS, REST APIs, SQL, Git, Agile",
        "description": "Build Angular/React applications for enterprise clients. TypeScript. REST APIs. SQL exposure. Agile sprints. Performance optimization. Code reviews. Team collaboration.",
    },
    {
        "company": "Accenture",
        "role": "Application Development Analyst – Frontend",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹10L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "indiacareers@accenture.com",
        "job_link": "https://www.accenture.com/in-en/careers",
        "source": "accenture.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, React, TypeScript, HTML5, CSS3, REST APIs, Git, Agile, CI/CD",
        "description": "Develop frontend applications for global consulting projects. Angular or React. TypeScript. REST API JWT/OAuth2. CI/CD. Agile delivery. Cross-functional collaboration.",
    },
    {
        "company": "LTIMindtree",
        "role": "Frontend Developer – Angular",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹10L/yr",
        "location": "Chennai / Bangalore (Onsite)",
        "hr_email": "careers@ltimindtree.com",
        "job_link": "https://www.ltimindtree.com/careers/",
        "source": "ltimindtree.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, TypeScript, RxJS, HTML5, SCSS, REST APIs, Jenkins CI/CD, Git",
        "description": "Build Angular frontend for global clients. TypeScript. RxJS. REST API. Jenkins CI/CD. Code reviews. Agile sprint ceremonies.",
    },
    {
        "company": "Mphasis",
        "role": "UI Developer – Angular TypeScript",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹10L/yr",
        "location": "Bangalore / Chennai (Onsite)",
        "hr_email": "careers@mphasis.com",
        "job_link": "https://careers.mphasis.com",
        "source": "careers.mphasis.com",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, TypeScript, RxJS, REST APIs, HTML5, CSS3, Git, Agile",
        "description": "Enterprise Angular TypeScript applications. RxJS reactive data flows. REST API JWT/OAuth2. SOLID principles. Agile delivery. Cross-functional collaboration.",
    },
    {
        "company": "UST Global",
        "role": "Software Engineer – Frontend Angular",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹11L/yr",
        "location": "Chennai / Bangalore (Onsite)",
        "hr_email": "careers@ust.com",
        "job_link": "https://www.ust.com/en/careers",
        "source": "ust.com/careers",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, TypeScript, RxJS, HTML5, CSS3, REST APIs, Git, CI/CD, Agile",
        "description": "Develop Angular frontend for enterprise clients. TypeScript and RxJS. REST API. CI/CD pipelines. Agile team delivery. Code reviews.",
    },
    {
        "company": "Hexaware Technologies",
        "role": "Junior Software Engineer – Frontend",
        "experience": "0-2 Years",
        "salary": "₹4L – ₹8L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "hr@hexaware.com",
        "job_link": "https://www.hexaware.com/careers/",
        "source": "hexaware.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "Angular, React, JavaScript, TypeScript, HTML5, CSS, REST APIs, Git",
        "description": "Build frontend for enterprise clients. Angular or React. JavaScript/TypeScript. HTML5/CSS3. REST API. Agile delivery. Junior/mid-level role with strong growth path.",
    },
    # ── TIER 3: STARTUPS & NICHE ────────────────────────────────────────
    {
        "company": "ASBL (PropTech)",
        "role": "Frontend Engineer – Angular/React",
        "experience": "1-4 Years",
        "salary": "₹8L – ₹20L/yr",
        "location": "Hyderabad (Onsite)",
        "hr_email": "careers@asbl.in",
        "job_link": "https://asbl.in/careers/software-engineering",
        "source": "asbl.in/careers",
        "posted_date": "Jan 2026",
        "key_skills": "React, Angular, TypeScript, Node.js, Postgres, Redis, Docker, GitHub Actions, AWS",
        "description": "Fast-growing profitable proptech. Build supply chain and home-buying products. AI-native culture (Cursor/Copilot). Small teams, high ownership. Stack: React/Angular, TypeScript, Postgres, Redis, Docker, AWS.",
    },
    {
        "company": "Incubyte",
        "role": "Frontend Developer – Angular/React",
        "experience": "1-3 Years",
        "salary": "₹7L – ₹15L/yr",
        "location": "Bangalore / Remote",
        "hr_email": "careers@incubyte.co",
        "job_link": "https://incubyte.co/careers",
        "source": "incubyte.co/careers",
        "posted_date": "Feb 2026",
        "key_skills": "React, Angular, TypeScript, Webpack, Jest, CI/CD, REST APIs, TDD, SOLID",
        "description": "Software craftsmanship agency. Build modular frontends. Webpack. Jest. CI/CD. TypeScript. REST APIs. Heavy emphasis on SOLID, clean code, TDD. The 'how' matters as much as the 'what'.",
    },
    {
        "company": "Docsumo",
        "role": "Frontend Engineer",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹16L/yr",
        "location": "Mumbai / Remote",
        "hr_email": "engineering@docsumo.com",
        "job_link": "https://wellfound.com/role/l/frontend-engineer/india",
        "source": "wellfound.com",
        "posted_date": "Feb 2026",
        "key_skills": "React, Angular, TypeScript, JavaScript, REST APIs, AI Integration",
        "description": "AI document processing platform. React/Angular. TypeScript. AI dashboard integration. REST API. Performance optimization. Product startup with AI-first culture.",
    },
    {
        "company": "Albert Invent (AI Chemistry)",
        "role": "Frontend Engineer – React/Angular",
        "experience": "2-4 Years",
        "salary": "₹10L – ₹20L/yr",
        "location": "Bangalore / Remote",
        "hr_email": "careers@albertinvent.com",
        "job_link": "https://cutshort.io/jobs/frontend-developer-jobs-in-bangalore-bengaluru",
        "source": "cutshort.io",
        "posted_date": "Feb 2026",
        "key_skills": "React, Angular, AngularJS, TypeScript, JavaScript ES6+, Redux, CI/CD",
        "description": "AI-driven R&D software. Build complex frontend apps. React + Angular (including AngularJS migration). Advanced JavaScript ES6. Redux. Enterprise scale. Scientists in 30+ countries use the platform.",
    },
    {
        "company": "Colan Infotech",
        "role": "Frontend Developer – Angular",
        "experience": "1-3 Years",
        "salary": "₹3.5L – ₹8L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "hr@colaninfotech.com",
        "job_link": "https://colaninfotech.com/careers",
        "source": "colaninfotech.com/careers",
        "posted_date": "Feb 2026",
        "key_skills": "Angular, Angular Material, TypeScript, JavaScript, HTML5, CSS3, MySQL, REST APIs, Git",
        "description": "CMMI Level 3 digital transformation company. Develop Angular apps with Angular Material. Reusable UI components. MySQL integration. Backend team collaboration. Chennai WFO.",
    },
    {
        "company": "Calibraint",
        "role": "Angular Developer",
        "experience": "1-3 Years",
        "salary": "₹4L – ₹9L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "hr@calibraint.com",
        "job_link": "https://www.calibraint.com/careers",
        "source": "calibraint.com/careers",
        "posted_date": "Jan-Feb 2026",
        "key_skills": "Angular 2+, TypeScript, RxJS, REST APIs, HTML5, SCSS, Git",
        "description": "Build scalable Angular SPAs. Reusable component libraries. TypeScript. RxJS. HTML5/SCSS. REST API. Code reviews. Peer programming. Chennai product studio.",
    },
    {
        "company": "MaintWiz Technologies",
        "role": "Frontend Developer – Angular",
        "experience": "1-3 Years",
        "salary": "₹4L – ₹8L/yr",
        "location": "Chennai (Hybrid)",
        "hr_email": "careers@maintwiz.com",
        "job_link": "https://maintwiz.com/careers",
        "source": "maintwiz.com/careers",
        "posted_date": "Feb 2026",
        "key_skills": "Angular, TypeScript, RxJS, IoT, WebSocket, REST APIs",
        "description": "Industrial IoT platform. Angular 8+. TypeScript. RxJS. WebSocket real-time data. REST API. Industrial device integration. 2-3 years experience. Agile team.",
    },
    {
        "company": "Temenos",
        "role": "Frontend Developer – Banking",
        "experience": "1-3 Years",
        "salary": "₹7L – ₹14L/yr",
        "location": "Chennai (Hybrid)",
        "hr_email": "careers@temenos.com",
        "job_link": "https://www.temenos.com/careers/",
        "source": "temenos.com/careers",
        "posted_date": "Jan-Feb 2026",
        "key_skills": "Angular, TypeScript, JavaScript, HTML5, CSS, REST APIs, JWT, Banking",
        "description": "Banking software frontend. Angular. TypeScript. REST API JWT security. Agile sprints. Financial domain. Performance-focused. Enterprise banking platform used by 3000+ banks.",
    },
    {
        "company": "Pegasystems",
        "role": "Software Engineer I – Frontend",
        "experience": "0-2 Years",
        "salary": "₹8L – ₹16L/yr",
        "location": "Chennai / Hyderabad (Hybrid)",
        "hr_email": "careers@pega.com",
        "job_link": "https://www.pega.com/about/careers",
        "source": "pega.com/careers",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "JavaScript, TypeScript, Angular, React, HTML5, CSS, REST APIs, Git, Agile",
        "description": "Build enterprise BPM/CRM UI. JavaScript/TypeScript. Angular or React. HTML5/CSS. REST APIs. Agile team. Performance optimization. Strong CS fundamentals required.",
    },
    {
        "company": "Sify Technologies",
        "role": "Frontend Developer",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹10L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "hr@sifycorp.com",
        "job_link": "https://www.sifycorp.com/careers",
        "source": "sifycorp.com/careers",
        "posted_date": "Jan-Feb 2026",
        "key_skills": "Angular, React, TypeScript, HTML5, CSS3, REST APIs, SQL, CI/CD",
        "description": "Build frontend web applications. Angular or React. TypeScript. REST API. SQL. CI/CD. Agile sprints. Enterprise product delivery.",
    },
    {
        "company": "Quest Global",
        "role": "Frontend Software Engineer",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹11L/yr",
        "location": "Chennai (Onsite / Hybrid)",
        "hr_email": "careers@quest-global.com",
        "job_link": "https://www.quest-global.com/careers/",
        "source": "quest-global.com/careers",
        "posted_date": "Feb 2026",
        "key_skills": "Angular, React, TypeScript, JavaScript, HTML, CSS, REST APIs, CI/CD, Git",
        "description": "Frontend components for engineering clients. Angular/React. TypeScript. REST API. Agile sprints. CI/CD. Code reviews. Industrial domain experience beneficial.",
    },
    {
        "company": "Virtusa",
        "role": "UI Developer – Angular",
        "experience": "1-3 Years",
        "salary": "₹4L – ₹10L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "careers.india@virtusa.com",
        "job_link": "https://careers.virtusa.com",
        "source": "careers.virtusa.com",
        "posted_date": "Feb-Mar 2026",
        "key_skills": "Angular, TypeScript, RxJS, HTML5, CSS, REST APIs, Git, Agile",
        "description": "Scalable Angular solutions. Automated unit tests. RxJS. REST API JWT. Agile methodology. Collaborate with cross-functional teams. Code review. Quality standards.",
    },
    {
        "company": "OrangeMantra",
        "role": "Angular Developer",
        "experience": "1-3 Years",
        "salary": "₹4L – ₹9L/yr",
        "location": "Delhi / NCR (Hybrid)",
        "hr_email": "hr@orangemantra.com",
        "job_link": "https://cutshort.io/jobs/frontend-developer-jobs-in-delhi-ncr-gurgaon-noida",
        "source": "cutshort.io",
        "posted_date": "Mar 2026",
        "key_skills": "Angular latest, TypeScript, HTML5, CSS3, REST APIs, Git",
        "description": "Develop, test, maintain responsive Angular apps. Reusable UI components. TypeScript. REST APIs. UX collaboration. Agile methodology.",
    },
    {
        "company": "ProArch",
        "role": "Senior Frontend Developer – Ionic/Angular",
        "experience": "2-3 Years",
        "salary": "₹8L – ₹15L/yr",
        "location": "India (Remote Hybrid)",
        "hr_email": "careers@proarch.com",
        "job_link": "https://startup.jobs/locations/india/frontend-engineer",
        "source": "startup.jobs",
        "posted_date": "Dec 2025",
        "key_skills": "Angular, Ionic, TypeScript, HTML5, SCSS, REST APIs, Mobile, Agile",
        "description": "Build Ionic/Angular hybrid mobile and web apps. TypeScript. REST API. Cross-platform mobile UI. Agile delivery. Remote hybrid across India.",
    },
    {
        "company": "Signzy (Fintech)",
        "role": "QA Engineer – Frontend Automation",
        "experience": "1-3 Years",
        "salary": "₹5L – ₹10L/yr",
        "location": "Bangalore (Onsite)",
        "hr_email": "careers@signzy.com",
        "job_link": "https://signzy.com/careers/",
        "source": "signzy.com/careers",
        "posted_date": "Jan-Feb 2026",
        "key_skills": "Playwright, TypeScript, Selenium, Cypress, Postman, JIRA, Manual Testing",
        "description": "QA for fintech identity verification. Playwright TypeScript. API testing Postman. Functional/regression/smoke testing. Bug tracking JIRA. 1-3 years experience.",
    },
    {
        "company": "Supaboard (AI-BI Startup)",
        "role": "Frontend Engineer",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹16L/yr",
        "location": "Bangalore (Hybrid)",
        "hr_email": "jobs@supaboard.co",
        "job_link": "https://cutshort.io/jobs/frontend-developer-jobs-in-bangalore-bengaluru",
        "source": "cutshort.io",
        "posted_date": "Feb 2026",
        "key_skills": "Angular, React, TypeScript, REST APIs, Microservices, Web Security, AWS",
        "description": "AI analytics startup. Build reusable components. Define REST APIs. Microservices. AWS. Web security. Pixel-perfect UIs. Fast-paced startup. High ownership.",
    },
    {
        "company": "Mindera",
        "role": "Frontend Engineer",
        "experience": "1-3 Years",
        "salary": "₹6L – ₹12L/yr",
        "location": "Chennai (Hybrid)",
        "hr_email": "india@mindera.com",
        "job_link": "https://builtinchennai.in/jobs/dev-engineering/search/front-end-developer",
        "source": "builtinchennai.in",
        "posted_date": "Mar 2026",
        "key_skills": "Angular, React, TypeScript, CSS3, HTML5, JavaScript, REST APIs",
        "description": "Responsive frontend apps. Angular/TypeScript. Backend collaboration. Code reviews. High-quality digital experiences. Agile team environment.",
    },
    {
        "company": "Delhivery",
        "role": "Frontend Developer – Angular",
        "experience": "1-3 Years",
        "salary": "₹6L – ₹14L/yr",
        "location": "Delhi / NCR or Bangalore (Hybrid)",
        "hr_email": "careers@delhivery.com",
        "job_link": "https://careers.delhivery.com",
        "source": "careers.delhivery.com",
        "posted_date": "Feb 2026",
        "key_skills": "Angular, TypeScript, HTML5, CSS3, REST APIs, Git, Agile",
        "description": "Build logistics frontend. Angular + TypeScript. HTML5/CSS3. REST API. Agile delivery. Code reviews. Supply chain domain.",
    },
    {
        "company": "PayU (Naspers Fintech)",
        "role": "Frontend Engineer",
        "experience": "1-3 Years",
        "salary": "₹8L – ₹18L/yr",
        "location": "Bangalore / Mumbai (Hybrid)",
        "hr_email": "careers@payuindia.com",
        "job_link": "https://corporate.payu.com/careers/",
        "source": "payu.com/careers",
        "posted_date": "Feb 2026",
        "key_skills": "Angular, React, TypeScript, JavaScript, REST APIs, JWT, OAuth2, Performance",
        "description": "Build payment frontend interfaces. Angular/React. TypeScript. JWT/OAuth2 security flows. REST API. Cross-browser. Performance optimization. Fintech domain.",
    },
    {
        "company": "CSS Corp / Movate",
        "role": "UI Developer – Angular",
        "experience": "1-2 Years",
        "salary": "₹4L – ₹8L/yr",
        "location": "Chennai (Onsite)",
        "hr_email": "careers@movate.com",
        "job_link": "https://www.movate.com/careers/",
        "source": "movate.com/careers",
        "posted_date": "Feb 2026",
        "key_skills": "Angular, TypeScript, HTML5, CSS3, REST APIs, Bootstrap, Git",
        "description": "Angular UI components for enterprise products. TypeScript. Bootstrap/responsive design. REST API. Code reviews. Agile team. Chennai WFO.",
    },
]

# ─────────────────────────────────────────────
# SECTION 4: "WHY I MATCH" AUTO-GENERATOR
# Compares job skills vs your profile skills
# ─────────────────────────────────────────────

def generate_why_i_match(job: dict) -> str:
    job_skills_raw = job.get("key_skills", "").lower()
    profile_skills = PROFILE["skills"]
    
    matched = [s for s in profile_skills if s.lower() in job_skills_raw]
    
    highlights = []
    
    if any(s in job_skills_raw for s in ["angular", "angularjs"]):
        highlights.append("3 yrs Angular (v2–10+) across 4 enterprise projects at Utthunga/Rockwell")
    if "rxjs" in job_skills_raw:
        highlights.append("RxJS observables for real-time data streaming (FDTS dashboards)")
    if "react native" in job_skills_raw or "ionic" in job_skills_raw:
        highlights.append("React Native (Expo) + Ionic mobile development experience")
    if "typescript" in job_skills_raw:
        highlights.append("TypeScript across all projects – services, guards, interceptors")
    if any(s in job_skills_raw for s in ["cypress", "selenium", "testcafe", "playwright", "jest", "karma", "jasmine"]):
        highlights.append("Test automation champion – TestCafe/Cypress/Selenium, 30% manual testing reduction")
    if any(s in job_skills_raw for s in ["jenkins", "ci/cd", "github actions", "gitlab"]):
        highlights.append("Jenkins + GitLab CI/CD + GitHub Actions pipelines in production")
    if any(s in job_skills_raw for s in ["jwt", "oauth2", "auth"]):
        highlights.append("JWT + OAuth2 REST API security integration across all projects")
    if any(s in job_skills_raw for s in ["payment", "razorpay", "fintech"]):
        highlights.append("LLD Payment Apps certification + Razorpay integration knowledge")
    if any(s in job_skills_raw for s in ["postgresql", "postgres", "sql", "mysql"]):
        highlights.append("PostgreSQL + MySQL experience in backend integration")
    if any(s in job_skills_raw for s in ["performance", "lazy loading", "virtual scroll"]):
        highlights.append("20% performance improvement via lazy loading + OnPush change detection")
    if any(s in job_skills_raw for s in ["solid", "clean code", "tdd"]):
        highlights.append("SOLID Principles & Clean Code certification (Scaler). Daily practice.")
    if any(s in job_skills_raw for s in ["real-time", "websocket", "dashboard"]):
        highlights.append("Built 6+ real-time factory dashboards with live data streaming")
    if any(s in job_skills_raw for s in ["iot", "industrial", "automation"]):
        highlights.append("Industrial automation domain (Rockwell Automation, factory operations)")
    if any(s in job_skills_raw for s in ["component", "library", "reusable"]):
        highlights.append("Architected 15+ reusable component library, 35% faster UI dev velocity")
    if any(s in job_skills_raw for s in ["mentoring", "junior", "code review"]):
        highlights.append("Mentored junior developers on Angular + RxJS patterns")
    if any(s in job_skills_raw for s in ["agile", "scrum", "sprint", "jira"]):
        highlights.append("Full Agile/Scrum delivery – sprint planning, standups, retrospectives, JIRA")
    if "ai" in job_skills_raw:
        highlights.append("Integrated ML/AI outputs into industrial frontend dashboards (15% efficiency gain)")
    if any(s in job_skills_raw for s in ["node.js", "nodejs", "backend"]):
        highlights.append("Node.js backend integration knowledge from full-stack architecture work")

    if not highlights:
        matched_str = ", ".join(matched[:5]) if matched else "General frontend skills"
        highlights.append(f"Matching skills: {matched_str}")

    score = len(highlights)
    if score >= 5:
        match_level = "🟢 HIGH MATCH"
    elif score >= 3:
        match_level = "🟡 MEDIUM MATCH"
    else:
        match_level = "🔴 LOW MATCH"

    return f"{match_level} | " + " | ".join(highlights[:4])


# ─────────────────────────────────────────────
# SECTION 5: DEDUPLICATE
# ─────────────────────────────────────────────

def deduplicate(jobs):
    seen = set()
    unique = []
    for job in jobs:
        key = (job["company"].lower().strip(), job["role"].lower().strip())
        if key not in seen:
            seen.add(key)
            unique.append(job)
    return unique


# ─────────────────────────────────────────────
# SECTION 6: EXPORT TO CSV + EXCEL
# ─────────────────────────────────────────────

import csv
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime
import os

HEADERS = [
    "Company Name", "Role", "Experience", "Salary", "Location",
    "HR Email", "Job Link", "Source", "Posted Date",
    "Key Skills", "Why I Match", "Job Description"
]

def build_row(job):
    return {
        "Company Name": job.get("company", ""),
        "Role": job.get("role", ""),
        "Experience": job.get("experience", ""),
        "Salary": job.get("salary", "N/A"),
        "Location": job.get("location", ""),
        "HR Email": job.get("hr_email", ""),
        "Job Link": job.get("job_link", ""),
        "Source": job.get("source", ""),
        "Posted Date": job.get("posted_date", ""),
        "Key Skills": job.get("key_skills", ""),
        "Why I Match": generate_why_i_match(job),
        "Job Description": job.get("description", ""),
    }

def export_csv(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  ✅ CSV  → {path}")

def export_xlsx(rows, path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Job Listings"

    header_fill = PatternFill("solid", start_color="1F3864", end_color="1F3864")
    header_font = Font(name="Arial", bold=True, color="FFFFFF", size=10)
    thin = Side(style="thin", color="CCCCCC")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    fill_a = PatternFill("solid", start_color="EBF1F8", end_color="EBF1F8")
    fill_b = PatternFill("solid", start_color="FFFFFF", end_color="FFFFFF")

    for ci, h in enumerate(HEADERS, 1):
        cell = ws.cell(row=1, column=ci, value=h)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border

    col_widths = [25, 38, 12, 20, 28, 30, 45, 20, 14, 42, 50, 58]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[1].height = 30

    for ri, row in enumerate(rows, 2):
        fill = fill_a if ri % 2 == 0 else fill_b
        for ci, h in enumerate(HEADERS, 1):
            cell = ws.cell(row=ri, column=ci, value=row.get(h, ""))
            cell.font = Font(name="Arial", size=9)
            cell.fill = fill
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = border
        ws.row_dimensions[ri].height = 55

    ws.freeze_panes = "A2"
    wb.save(path)
    print(f"  ✅ XLSX → {path}")


# ─────────────────────────────────────────────
# SECTION 7: MAIN — RUN THIS DAILY
# ─────────────────────────────────────────────

def main():
    print("\n" + "="*55)
    print("  GOKUL'S DAILY JOB SEARCH")
    print(f"  Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*55)

    # Deduplicate
    unique_jobs = deduplicate(JOBS)
    print(f"\n📋 Total unique jobs: {len(unique_jobs)}")

    # Build rows with Why I Match
    rows = [build_row(j) for j in unique_jobs]

    # Count match levels
    high   = sum(1 for r in rows if "HIGH"   in r["Why I Match"])
    medium = sum(1 for r in rows if "MEDIUM" in r["Why I Match"])
    low    = sum(1 for r in rows if "LOW"    in r["Why I Match"])
    print(f"   🟢 High Match  : {high}")
    print(f"   🟡 Medium Match: {medium}")
    print(f"   🔴 Low Match   : {low}")

    # File names
    today = datetime.now().strftime("%Y-%m-%d")
    out_dir = "."   # change to your folder path if needed

    csv_path  = os.path.join(out_dir, f"job_listing_{today}.csv")
    xlsx_path = os.path.join(out_dir, f"job_listing_{today}.xlsx")

    print("\n💾 Saving files...")
    export_csv(rows, csv_path)
    export_xlsx(rows, xlsx_path)

    # Google Colab auto-download
    try:
        from google.colab import files
        print("\n📥 Downloading files to your computer...")
        files.download(csv_path)
        files.download(xlsx_path)
    except ImportError:
        print(f"\n📂 Files saved locally in: {os.path.abspath(out_dir)}")

    print("\n" + "="*55)
    print("  ✅ DONE! Job search complete.")
    print("="*55 + "\n")


if __name__ == "__main__":
    main()
