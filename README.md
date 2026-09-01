# Okhayo Design
### Southern African Living Heritage — A Design Platform

> *"Umuntu ngumuntu ngabantu — a person is a person through other people."*

![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Built With](https://img.shields.io/badge/Built%20With-HTML%20%7C%20CSS%20%7C%20JS-orange)
![Deployed On](https://img.shields.io/badge/Deployed%20On-Vercel-black)
![CMS](https://img.shields.io/badge/CMS-Decap%20CMS-blue)
![Analytics](https://img.shields.io/badge/Analytics-Google%20Analytics-yellow)

---

## 🌍 Live Site

**[okhayodesign.co.za](https://okhayodesign.co.za)**

Admin CMS: [ubiquitous-toffee-fb1798.netlify.app/admin](https://ubiquitous-toffee-fb1798.netlify.app/admin)

---

## 📖 About This Project

Okhayo Design is my first ever website — built entirely from scratch with no prior
web development experience. I started this project knowing nothing about HTML, CSS,
JavaScript, Git, DNS, or deployment. Everything documented here was learned in real
time, through trial and error, with genuine problems solved along the way.

**Okhayo** means "home" in isiZulu.

The platform is a living archive and editorial destination celebrating Southern
African design heritage — from the carved geometry of the Bantu headrest to the
mathematical precision of Ndebele wall painting, from Nguni plant medicine to the
communal architecture of the rondavel.

The design philosophy is rooted in **Ubuntu**: a person is a person through
other people. Every object our ancestors made was made in community — and so
was this website.

---

## 🎨 Design Inspiration & Visual Language

The site draws its visual identity from two main sources:

**Aesop.com** — for its editorial layout philosophy: generous whitespace,
quiet luxury, long-form content treated with respect, and a restrained
typographic system.

**Southern Ndebele wall painting** — for its colour palette and geometric
vocabulary. The Ndebele geometric tradition is one of Africa's great design
languages — developed over centuries by women, communicating cosmological
belief through triangles, stepped forms, and bold colour fields.

### Colour Palette

| Name | Hex | Inspired By |
|------|-----|-------------|
| Ndebele Red | `#CC2200` | Traditional Ndebele pigment |
| Ochre Gold | `#C8960C` | Raw ochre clay |
| Ndebele Blue | `#003366` | Ndebele wall accent |
| Terracotta | `#C17B3F` | Southern African earth |
| Deep Soil | `#231209` | Limpopo soil |
| Sand | `#E8D5B0` | Kalahari sand |

### Typography

- **Cormorant Garamond** — editorial serif for headings and display text
- **Jost** — clean geometric sans-serif for body copy and UI

---

## 🏗️ What Is On The Site

Six design disciplines are documented:

| # | Discipline | What It Covers |
|---|-----------|----------------|
| 01 | Objects & Furniture | Bantu headrests, ceremonial stools, clay vessels |
| 02 | Weaving & Textiles | Grass mats, ilala palm basketry, Zulu beadwork |
| 03 | Living Architecture | Ndebele murals, rondavel, kraal design |
| 04 | Dance & Rhythm | Umgido, Reed Dance, Isicathamiya |
| 05 | Medicine & Plant Lore | Muthi, Nguni herbalism, sacred plants |
| 06 | Food & Fire | Umngqusho, morogo, umqombothi, three-legged pot |

---

## 🛠️ Technology Stack

This is a **pure frontend static site** — no frameworks, no build tools, no dependencies.

| Technology | Purpose |
|-----------|---------|
| HTML5 | Page structure and content |
| CSS3 | All styling, layout, animations |
| Vanilla JavaScript | Interactivity and scroll behaviour |
| SVG | All illustrations drawn by hand in code |
| Google Fonts | Cormorant Garamond + Jost |
| Git + GitHub | Version control |
| Vercel | Hosting and continuous deployment |
| Decap CMS | Content management system |
| Netlify Identity | CMS authentication |
| Google Analytics (G-XV9VKNQT4K) | Traffic and audience analytics |
| Host Africa | Domain registrar (.co.za) |

---

## 📁 Project Structure

```
okhayo-design/
│
├── index.html              # Main website — all content and structure
├── style.css               # All styling (2000+ lines)
├── script.js               # Interactive behaviour
├── README.md               # This file
├── netlify.toml            # Netlify configuration and redirects
│
├── admin/                  # CMS admin panel
│   ├── index.html          # Decap CMS loader
│   └── config.yml          # CMS configuration — collections, fields
│
├── _posts/                 # All published content (saved by CMS)
│   ├── journal/            # Journal articles (markdown files)
│   └── objects/            # Archive object entries
│
├── images/
│   └── uploads/            # Images uploaded through CMS
│
└── _data/
    └── settings.json       # Site-wide settings
```

---

## ✨ Key Features

- **Opening video overlay** — full-screen brand intro on page load, inspired by Aesop.com, with animated Ndebele pattern backdrop, auto-dismisses after 8 seconds

- **Ndebele geometric patterns** — all patterns are hand-coded SVGs faithful to Southern Ndebele wall-painting traditions, used as section dividers and backgrounds throughout

- **Animated marquee strip** — scrolling text in Ndebele red carrying *Umuntu Ngumuntu Ngabantu* and cultural keywords

- **Six discipline grid** — hover-reveal cards with custom SVG illustrations for each cultural category

- **Horizontal scroll section** — touch and mouse scrollable discipline cards with in-depth cultural descriptions

- **Ubuntu philosophy section** — custom triadic Ubuntu symbol illustration with brand manifesto

- **Stylised origins map** — hand-drawn SVG map of Southern Africa with regional cultural markers

- **Scroll reveal animations** — sections animate in on scroll using IntersectionObserver API

- **Responsive navigation** — nav colour switches automatically from light to dark when scrolling over dark sections

- **Content Management System** — editors can publish journal articles and archive objects through a web interface without touching code

- **Google Analytics** — visitor tracking and audience insights

- **Fully responsive** — works on mobile, tablet, and desktop

---

## 🧠 What I Learned Building This

This project was a complete education in web development from zero.
Here is everything I genuinely learned:

### HTML & CSS
- How HTML structures a web page (elements, nesting, semantic markup)
- CSS custom properties (variables) for consistent design systems
- CSS Grid for complex two-dimensional layouts
- Flexbox for one-dimensional alignment
- CSS animations (@keyframes, transitions, transforms)
- IntersectionObserver for scroll-triggered animations
- Responsive design with media queries
- How to embed and style SVG inline in HTML
- CSS repeating-linear-gradient for geometric patterns
- How the browser renders a page (box model, stacking context)

### JavaScript
- DOM manipulation and event listeners
- IntersectionObserver API for scroll reveals
- setTimeout and animation timing
- classList.add/remove for state management
- How JavaScript files connect to HTML via script tags

### SVG
- How to draw shapes, paths, polygons, and ellipses in SVG
- How to use SVG patterns (defs + pattern) for repeating textures
- How to build complex illustrations entirely in code
- SVG viewBox and coordinate systems
- How to make SVGs responsive

### Git & Version Control
- What Git is and why version control matters
- git init, git add, git commit, git push, git pull
- How merge conflicts happen and how to resolve them
- Why you should NEVER edit files directly on GitHub
- How folder names with spaces need quotes in the terminal (cd "Okhayo Design 2")
- How to navigate the terminal using cd, ls, pwd
- The difference between local machine and remote repository
- What HEAD, origin, and main mean in Git

### Deployment & Hosting
- What static site hosting means
- How Vercel connects to GitHub and auto-deploys on every push
- What a continuous deployment pipeline is
- How preview deployments work for testing
- The difference between development, staging, and production environments

### DNS & Domains
- What DNS (Domain Name System) is and how it works
- A records, CNAME records, NS records, MX records, TXT records
- How to buy a domain from a registrar (Host Africa)
- How to point a domain to a hosting provider
- What DNS propagation is and why it takes time (up to 48 hours)
- How to check propagation globally using whatsmydns.net
- The difference between .com and .co.za domains
- What nameservers are and how to change them
- How HTTPS/SSL certificates work (automatic on Vercel)
- Why www.domain.com and domain.com are technically different

### Content Management & Authentication
- What a headless CMS is and why it is useful
- How Decap CMS works with GitHub as a backend
- How YAML configuration files work
- What Netlify Identity is and how OAuth authentication works
- The difference between git-gateway and github backends in Decap CMS
- How GitHub OAuth Apps work (Client ID, Client Secret, callback URLs)
- What JWT tokens are (JSON Web Tokens)
- How content is saved as markdown files in a git repository
- What frontmatter is (the --- metadata at the top of markdown files)
- The difference between invite-only and open registration

### Terminal & Command Line
- How to navigate the file system (cd, ls, pwd)
- How ~ represents the home directory on Mac
- How folder names with spaces require quotes
- How to use cat to read file contents
- How to use find to search for files
- How to use curl to test URLs
- The difference between relative and absolute file paths

### Analytics
- What Google Analytics measures (sessions, users, pageviews)
- How to create a Google Analytics property and data stream
- What a Measurement ID (G-XXXXXXXX) is and how to add it to a site
- What Realtime reporting shows
- The difference between Google Analytics and Google Search Console

### General Web Concepts
- The difference between frontend and backend
- What a static site is vs a dynamic site
- What an API is
- What environment variables are and why secrets must never go in code
- What HTTP errors mean (404 Not Found, 500 Server Error, 301/302 redirects)
- How browser caching works and why hard refresh (Cmd+Shift+R) exists
- Why browsers block popups and how to allow them
- The importance of never sharing API keys or Client Secrets publicly

---

## 🚀 How to Run This Locally

```bash
# 1. Clone the repository
git clone https://github.com/Kongzar/Okhayo-Design-.git
cd Okhayo-Design-

# 2. Open in VS Code
code .

# 3. Install Live Server extension in VS Code
# Then right-click index.html → Open with Live Server

# No npm install. No build step. No dependencies. Just open and run.
```

---

## 🔄 How to Update the Site

### Update design or content:
```bash
# 1. Edit files in VS Code
# 2. Save (Cmd+S on Mac)
# 3. Push to GitHub
git add .
git commit -m "Describe what you changed"
git push
# Vercel redeploys automatically in ~30 seconds
```

### Publish a new article (no code needed):
```
1. Go to: ubiquitous-toffee-fb1798.netlify.app/admin
2. Log in with Netlify Identity
3. Click Journal Articles → + Journal Article
4. Fill in title, category, image, excerpt, body
5. Click Publish
6. Article saves to GitHub and Vercel redeploys automatically
```

---

## 🔒 Security

### Current measures in place:
- HTTPS enforced via Vercel (automatic SSL certificate)
- CMS is invite-only — no public registration possible
- Netlify Identity handles authentication securely
- Git Gateway controls write access to the repository
- GitHub OAuth app scoped to minimum required permissions
- No API keys or secrets stored in the codebase

### Planned security improvements:
- [ ] Content Security Policy (CSP) headers
- [ ] HTTP Strict Transport Security (HSTS) headers
- [ ] X-Frame-Options header (clickjacking protection)
- [ ] X-Content-Type-Options header (MIME sniffing protection)
- [ ] Referrer-Policy header
- [ ] Permissions-Policy header
- [ ] Rate limiting on the admin panel
- [ ] Regular npm/dependency security audits
- [ ] Subresource Integrity (SRI) for CDN scripts
- [ ] GDPR-compliant cookie consent for analytics
- [ ] Security.txt file
- [ ] Penetration testing

### Cybersecurity learning goals:
- [ ] OWASP Top 10 vulnerabilities study
- [ ] How XSS (Cross-Site Scripting) attacks work and how to prevent them
- [ ] How CSRF (Cross-Site Request Forgery) works
- [ ] How SQL injection works (even on static sites via forms)
- [ ] How to implement proper Content Security Policy headers
- [ ] How to read and interpret security audit reports
- [ ] Bug bounty fundamentals

---

## 🌱 Roadmap

- [ ] Resolve DNS fully — connect okhayodesign.co.za to Vercel
- [ ] Build individual article pages that render markdown content
- [ ] Add Eleventy or Astro for static site generation from markdown
- [ ] Add search functionality to the journal
- [ ] Build searchable objects archive page
- [ ] Google Search Console setup for SEO tracking
- [ ] Implement full security headers suite
- [ ] Add contact/enquiry form via Formspree
- [ ] Newsletter integration with Mailchimp or Beehiiv
- [ ] Explore e-commerce for prints and archive objects (Snipcart)
- [ ] Multilingual support (isiZulu, Sesotho, Setswana)
- [ ] Image optimisation and lazy loading
- [ ] Accessibility audit (WCAG 2.1 compliance)
- [ ] Cybersecurity hardening

---

## 🙏 Cultural Acknowledgement

Okhayo Design draws from the living design traditions of:

- **KwaZulu-Natal** — Zulu beadwork, headrests (izigqiki), umgido dance
- **Mpumalanga** — Southern Ndebele wall murals and beaded jewellery
- **Limpopo Valley** — Venda pottery and domba dance
- **Eswatini** — Swazi reed dance and siswati weaving
- **Lesotho** — Basotho mokorotlo hat and seanamarena blanket
- **Western Cape** — Khoisan material culture and Cape Malay traditions

This project is built with deep respect for these traditions and the
communities that carry them. Design credit belongs to the ancestors and
the living craftspeople who continue this knowledge today.

---

## 👤 About the Developer

**This is my first website.**

I am not a trained developer. I had an idea, I did not know how to build it,
and I built it anyway. Every single skill listed in this README was learned
while making this project — from what HTML even is, to how DNS propagation
works, to what a JWT token is, to why you should never edit files directly
on GitHub.

I made hundreds of mistakes. I got stuck constantly. I kept going.

That is the Ubuntu philosophy in practice — you do not learn alone,
and you do not build alone.

**GitHub:** [@Kongzar](https://github.com/Kongzar)
**Website:** [okhayodesign.co.za](https://okhayodesign.co.za)

---

## 📄 License

The code in this repository is released under the **MIT License** —
free to use, modify, and distribute with attribution.

The cultural content, brand name **Okhayo Design**, and associated
visual identity belong to their respective creators and should not
be reproduced commercially without permission.

---

*Built with intention. Rooted in Southern Africa.*

*Okhayo — welcome home.*
