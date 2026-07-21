# Okhayo Design

> *"Umuntu ngumuntu ngabantu — a person is a person through other people."*

**Okhayo Design** is a living archive and editorial platform celebrating Southern African design heritage. Built on the philosophy of Ubuntu, the site documents and honours the material culture of Southern Africa — from the carved geometry of the Bantu headrest to the mathematical precision of Ndebele wall painting, from the medicinal knowledge of Nguni herbalists to the communal architecture of the rondavel.

*Okhayo* means **home** in isiZulu.

---

## Live Preview

> Coming soon — deployment link will be added here once the site is live.

---

## What the Site Covers

The platform is organised around six design disciplines:

| # | Discipline | Heritage |
|---|-----------|----------|
| 01 | Objects & Furniture | Bantu headrests, ceremonial stools, clay vessels |
| 02 | Weaving & Textiles | Grass mats, ilala palm basketry, Sotho blankets, Zulu beadwork |
| 03 | Living Architecture | Ndebele wall murals, rondavel, kraal design |
| 04 | Dance & Rhythm | Umgido, isicathamiya, Reed Dance, Moribane |
| 05 | Medicine & Plant Lore | Muthi, Nguni herbalism, sacred botanical knowledge |
| 06 | Food & Fire | Umngqusho, morogo, umqombothi, three-legged pot culture |

---

## Design Philosophy

The visual design draws directly from Southern African geometric traditions:

- **Ndebele colour palette** — terracotta, Ndebele red (`#CC2200`), ochre gold (`#C8960C`), Ndebele blue (`#003366`), and deep soil tones
- **Geometric patterns** — repeating Ndebele wall-painting motifs used as dividers, backgrounds, and structural elements throughout
- **Typography** — Cormorant Garamond (editorial serif) paired with Jost (clean sans-serif) for a luxury editorial feel
- **Layout** — inspired by the quiet architectural restraint of Aesop.com: generous whitespace, editorial grid, full-bleed sections
- **Illustrations** — all visuals are hand-crafted SVGs representing actual Southern African cultural objects: headrests, grass mats, beaded collars, clay pots, dance figures, and botanical forms

---

## Built With

This is a **pure HTML, CSS, and JavaScript** project — no frameworks, no build tools, no dependencies. Intentionally lean.

- **HTML5** — semantic structure
- **CSS3** — custom properties (variables), CSS Grid, Flexbox, animations, scroll-based effects
- **Vanilla JavaScript** — IntersectionObserver for scroll reveals, video overlay logic, nav state
- **SVG** — all illustrations and geometric patterns are inline SVG, no external image files required
- **Google Fonts** — Cormorant Garamond, Jost (loaded via CDN)

---

## Project Structure

```
okhayo-design/
│
├── index.html          # All page content and structure
├── style.css           # All styling — layout, colours, typography, animations
├── script.js           # Interactive behaviour — overlay, scroll reveals, nav
└── README.md           # This file
```

Everything lives in three files. The HTML links to the CSS and JS:

```html
<link rel="stylesheet" href="style.css">
<script src="script.js"></script>
```

---

## Key Features

- **Opening video overlay** — full-screen brand intro on page load, inspired by Aesop.com, with auto-dismiss after 8 seconds or on user interaction
- **Ndebele geometric patterns** — SVG-based repeating patterns used as backgrounds and section dividers throughout, faithful to Southern Ndebele wall-painting traditions
- **Animated marquee strip** — scrolling text in Ndebele red carrying the phrase *Umuntu Ngumuntu Ngabantu* and cultural keywords
- **Six discipline category grid** — hover-reveal cards with hand-crafted SVG illustrations for each cultural category
- **Horizontal discipline scroll** — touch/mouse-scrollable row of in-depth practice cards
- **Ubuntu philosophy section** — custom triadic Ubuntu symbol illustration with brand manifesto
- **Stylised origins map** — hand-drawn SVG map of Southern Africa with regional markers
- **Scroll reveal animations** — sections animate in as the user scrolls using IntersectionObserver
- **Responsive navigation** — nav changes from light to dark automatically over dark page sections
- **Newsletter section** — ready to connect to Formspree, Mailchimp, or similar
- **Fully responsive** — mobile breakpoints at 900px

---

## Getting Started

No installation, no build step. Clone the repo and open the file.

```bash
git clone https://github.com/YOUR-USERNAME/okhayo-design.git
cd okhayo-design
```

Then either:
- Open `index.html` directly in your browser, or
- Use the **Live Server** extension in VS Code for hot-reloading during development

---

## Customisation Guide

### Change brand colours
All colours are defined as CSS custom properties at the top of `style.css`:

```css
:root {
  --soil:   #231209;   /* darkest background */
  --terra:  #a0522d;   /* terracotta */
  --clay:   #c17b3f;   /* warm mid-tone */
  --ochre:  #c8960c;   /* gold */
  --sand:   #e8d5b0;   /* light warm tone */
  --nred:   #cc2200;   /* Ndebele red */
  --nblue:  #003366;   /* Ndebele blue */
  --ngold:  #c8960c;   /* Ndebele gold */
}
```
Change any value here and it updates everywhere on the site.

### Change text content
All page copy is in `index.html`. Use your editor's Find function (`Ctrl+F` / `Cmd+F`) to locate any piece of text.

### Change the video overlay duration
In `script.js`, find:
```js
setTimeout(dismiss, 8000);
```
Change `8000` to any number of milliseconds (e.g. `5000` = 5 seconds, `0` = skip the overlay entirely).

### Connect the newsletter form
In `index.html`, find the newsletter section and add a Formspree action to the form, or replace the inputs with your email provider's embed code.

### Add a real video
In `index.html`, find the `.v-screen` div inside the video overlay and replace the SVG illustration with an HTML5 `<video>` tag or a YouTube/Vimeo embed iframe.

---

## Deployment

This site deploys as a **static site** — no server required.

### Vercel (recommended)
1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) and sign in with GitHub
3. Click **"Add New Project"** and import this repository
4. Click **Deploy** — live in under a minute
5. Connect a custom domain in the Vercel dashboard

### Netlify
1. Push this repo to GitHub
2. Go to [netlify.com](https://netlify.com), click **"Add new site → Import an existing project"**
3. Connect your GitHub repo and deploy
4. Connect a custom domain in the Netlify dashboard

### Cloudflare Pages
1. Push this repo to GitHub
2. Go to [pages.cloudflare.com](https://pages.cloudflare.com) and connect your repo
3. Deploy — also free, with Cloudflare's global CDN included

All three platforms redeploy automatically every time you push new code to GitHub.

---

## Roadmap

Future development plans:

- [ ] Connect newsletter form to Mailchimp / Beehiiv
- [ ] Add a headless CMS (Sanity or Decap CMS) for the Journal section
- [ ] Add a searchable Objects archive page
- [ ] Individual object detail pages
- [ ] E-commerce integration for prints and archive items (Shopify Buy Button or Snipcart)
- [ ] User accounts — saved favourites, mood boards (Supabase Auth)
- [ ] Replace SVG video placeholder with real brand film
- [ ] Multilingual support (isiZulu, Sesotho, Setswana)

---

## Origins & Cultural Acknowledgement

Okhayo Design draws from the living design traditions of the following communities and regions:

- **KwaZulu-Natal** — Zulu beadwork, headrests, umgido dance
- **Mpumalanga** — Southern Ndebele wall murals and beaded jewellery
- **Limpopo Valley** — Venda pottery and domba dance
- **Eswatini** — Swazi reed dance and siswati weaving
- **Lesotho** — Basotho mokorotlo hat and seanamarena blanket
- **Western Cape** — Khoisan material culture and Cape Malay traditions

This project is built with deep respect for these traditions and the communities that carry them. Design credit belongs to the ancestors and the living craftspeople who continue this knowledge.

---

## License

This codebase is released under the **MIT License** — you are free to use, modify, and distribute it, with attribution.

The cultural content, brand name **Okhayo Design**, and associated philosophy belong to their respective creators and should not be reproduced commercially without permission.

---

## Contact

For collaborations, commissions, or enquiries:

- **Website:** [okhayodesign.com](https://okhayodesign.com) *(coming soon)*
- **Instagram:** [@okhayodesign](https://instagram.com)
- **Email:** hello@okhayodesign.com

---

*Built with intention. Rooted in Southern Africa.*
