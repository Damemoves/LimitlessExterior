#!/usr/bin/env python3
"""Builds the static pages for limitlessexterior.ca into ../Website.

Edit the content below, then run:  python3 tools/build_site.py
"""
import json
from datetime import date
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "Website"
SITE = "https://limitlessexterior.ca"
PHONE = "(647) 807-5919"
TEL = "+16478075919"
EMAIL = "info@limitlessexterior.ca"
REVIEW_COUNT = 22
RATING = "5.0"
GOOGLE_LISTING = "https://maps.google.com/?cid=17564325381363111413"
GOOGLE_WRITE_REVIEW = "https://g.page/r/CfWVhuPfBMHzEAE/review"
INSTAGRAM = "https://www.instagram.com/limitless.exterior/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61589252013529"
TIKTOK = "https://www.tiktok.com/@limitlessexterior"
AREAS = ["Etobicoke", "Mississauga", "North York", "Brampton", "Toronto"]
TODAY = date.today().isoformat()

# Real Google reviews (copied from the Google Business Profile, Nov 2026)
REVIEWS = [
    ("Olivera C.", "We had an excellent experience with Limitless Exterior! Their team was professional, punctual, pleasant and incredibly thorough. Our windows are spotless. They paid attention to every detail, worked efficiently, and left everything clean when they were finished. It’s refreshing to work with a company that takes such pride in their work. I highly recommend Limitless Exterior to anyone looking for exceptional window cleaning. We’ll definitely be calling them again!"),
    ("Andrea R.", "I was impressed with the owners and their professionalism. The window cleaning service they provided was thorough and really well done. I’d definitely recommend hiring Limitless Exterior."),
    ("Niam M.", "Hard efficient workers and incredible quality my windows have never looked better! Would seriously recommend."),
]

ICONS = {
    "lights": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 4c4 3 9 4.5 14 4.5S26 7 30 4"/><rect x="13" y="8.5" width="6" height="4" rx="1"/><path d="M16 12.5c-3.6 0-6.2 3.3-6.2 7.6 0 3.9 2.8 7.4 6.2 7.4s6.2-3.5 6.2-7.4c0-4.3-2.6-7.6-6.2-7.6z" fill="currentColor" fill-opacity=".18"/><path d="M13.5 18.5c.4-1.2 1.2-2 2.2-2.4"/></svg>',    "gutter": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 15L16 5l13 10"/><path d="M2 15h28v3a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2z"/><path d="M26 20v9"/><path d="M10 13.5l2-1.5M16 12l1.5 1.5M21 13l1.5-1"/></svg>',
    "window": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="4" width="22" height="24" rx="1.5"/><path d="M16 4v24M5 16h22"/><path d="M9 8.5l3-1M20 20.5l3-1.5"/></svg>',
    "pressure": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 27l9-9"/><path d="M10 16l6 6"/><path d="M13 19l7-7"/><path d="M20 12l2-2"/><path d="M24 4l1.5 3M28 8l-3 1.5M27.5 3.5L25 6.5M29 12l-3.5-.5"/></svg>',
}
SVG = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "sms": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>',
    "tt": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 5.82A4.28 4.28 0 0 1 15.54 3h-3.09v12.4a2.59 2.59 0 0 1-2.59 2.5c-1.42 0-2.6-1.16-2.6-2.6 0-1.72 1.66-3.01 3.37-2.48V9.66c-3.45-.46-6.47 2.22-6.47 5.64 0 3.33 2.76 5.7 5.69 5.7 3.14 0 5.69-2.55 5.69-5.7V9.01a7.35 7.35 0 0 0 4.3 1.38V7.3s-1.88.09-3.24-1.48z"/></svg>',
    "google": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.27-4.74 3.27-8.1z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84A11 11 0 0 0 12 23z"/><path fill="#FBBC05" d="M5.84 14.09a6.6 6.6 0 0 1 0-4.18V7.07H2.18a11 11 0 0 0 0 9.86z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15A11 11 0 0 0 2.18 7.07l3.66 2.84C6.71 7.31 9.14 5.38 12 5.38z"/></svg>',
}

SERVICES = [
    {
        "slug": "christmas-light-installation", "key": "Christmas Light Installation", "icon": "lights",
        "nav": "Christmas lights", "when": "Book Oct – Dec", "featured": True,
        "short": "Rooflines, trees and shrubs lit up, with no ladder for you. Takedown in the new year.",
        "title": "Christmas Light Installation in Etobicoke & the GTA | Limitless Exterior",
        "desc": "Professional Christmas light installation in Etobicoke, Mississauga and across the GTA. Rooflines, trees and shrubs installed and taken down after the holidays. Free quote today.",
        "h1": "Christmas light installation in Etobicoke & the GTA",
        "lead": "We hang your holiday lights so you don’t spend a cold November afternoon on a ladder. Rooflines, trees, shrubs and railings, installed and working, then taken down after the holidays.",
        "body": [
            "Every install starts with a quick look at your home so we can plan where the lights go, how they’ll be powered, and what the finished house will look like at night. You get one price for the whole job before we start.",
            "Lights go up with clips made for gutters and shingles, not nails or staples, so nothing gets damaged and everything comes down clean in January.",
        ],
        "included": [
            "Roofline and eavestrough lighting",
            "Trees, shrubs, railings and walkways",
            "Every strand tested before it goes up",
            "Takedown in the new year, added to your quote",
            "Use your own lights, or ask us to quote supplying them",
        ],
        "note": "Install dates fill up through November. Book now to get the week you want.",
        "faqs": [
            ("When do you install Christmas lights?", "We install from early November through mid-December. The earlier you book, the more choice you have on dates."),
            ("Do you take the lights down too?", "Yes. Add takedown to your quote and we’ll come back in the new year to take everything down."),
            ("Can you use the lights I already have?", "Yes, as long as they work. We test every strand before hanging it. If some are dead, we’ll tell you and can quote replacements."),
            ("Will the clips damage my roof or gutters?", "No. We use clips designed for shingles and eavestroughs, with no nails, staples or screws."),
            ("Do I need an outdoor outlet?", "Lights need power from an outdoor outlet. When we quote, we’ll check where yours are and plan the layout around them."),
            ("Can you clean my gutters at the same visit?", "Yes. Lots of customers do both. Clean gutters before the lights go up, and you’re set for winter."),
        ],
    },
    {
        "slug": "gutter-cleaning", "key": "Gutter Cleaning", "icon": "gutter",
        "nav": "Gutter cleaning", "when": "Spring & late fall",
        "short": "Eavestroughs cleared by hand and downspouts flushed before the freeze.",
        "title": "Gutter Cleaning in Etobicoke & the GTA | Eavestrough Cleaning | Limitless Exterior",
        "desc": "Gutter and eavestrough cleaning in Etobicoke, Mississauga and across the GTA. Hand clean-out, downspouts flushed, mess cleaned up. Free quote today.",
        "h1": "Gutter cleaning in Etobicoke & the GTA",
        "lead": "Clogged eavestroughs overflow, freeze, and send water toward your foundation. We clear them out by hand, flush the downspouts, and leave your property clean.",
        "body": [
            "Late fall is the most important time to clean gutters. Once the leaves are down, a single clean-out before the freeze helps prevent ice dams and overflow that can damage fascia, siding and basements.",
            "If we notice loose sections, leaks or damage while we’re up there, we’ll show you so you can decide what to do about it.",
        ],
        "included": [
            "Hand clean-out of every eavestrough",
            "Downspouts flushed and checked for blockages",
            "Debris cleaned up from the roof edge, ground and driveway",
            "A heads-up on any damage we spot",
        ],
        "note": "Booking late-fall gutter cleanings now, before the ground freezes.",
        "faqs": [
            ("When should I get my gutters cleaned?", "Late fall, after most leaves have dropped and before the freeze. Homes with lots of trees often need a second clean in spring."),
            ("Do I need to be home?", "No. As long as we can get to the outside of your house, we can do the job while you’re out."),
            ("What happens to the debris?", "We clean up after ourselves. Nothing is left on your lawn, driveway or walkways."),
            ("Can you do gutters and Christmas lights together?", "Yes. We can clean your gutters right before your lights go up, in one visit."),
        ],
    },
    {
        "slug": "window-cleaning", "key": "Window Cleaning", "icon": "window",
        "nav": "Window cleaning", "when": "Book Apr – Nov",
        "short": "Streak-free glass with a pure water, waterfed pole system. No soap, no residue.",
        "title": "Window Cleaning in Etobicoke & the GTA | Pure Water System | Limitless Exterior",
        "desc": "Residential and commercial window cleaning in Etobicoke, Mississauga and across the GTA. Pure water system: no soap, no streaks. Free quote, same-day reply.",
        "h1": "Window cleaning in Etobicoke & the GTA",
        "lead": "Streak-free windows, cleaned with 100% purified water through waterfed poles. No soap, no chemicals, and nothing left behind to attract dirt.",
        "body": [
            "Our waterfed brush system pushes purified water through extension poles, so we clean bungalows and two-storey homes safely from the ground. The brush scrubs the glass and frames, then a pure water rinse carries the dirt away.",
            "Because the water has nothing dissolved in it, it dries with no spots and no film. That means no squeegee marks, no soap residue, and windows that stay clean longer.",
        ],
        "included": [
            "Exterior glass, frames and sills",
            "Bungalows, two-storey homes and townhouses",
            "Storefronts, offices and multi-unit buildings",
            "Satisfaction guaranteed or we come back free",
        ],
        "note": None,
        "faqs": [
            ("Do I need to be home during the cleaning?", "No. As long as we can reach the outside of your windows, you don’t need to be there."),
            ("What if it rains right after you clean?", "Rain doesn’t leave the marks, the dirt and minerals do. With purified water, there’s no residue for rain to spot."),
            ("Do you use soaps or chemicals?", "Never. Our pure water system is chemical-free, so it’s safe for your family, pets and garden."),
            ("How often should I get my windows cleaned?", "For most homes, 2–4 times a year. Homes near busy roads or lots of trees may want it more often."),
            ("Do you clean storefronts?", "Yes. We clean storefronts, offices and multi-unit buildings, and work around your hours."),
        ],
    },
    {
        "slug": "pressure-washing", "key": "Pressure Washing", "icon": "pressure",
        "nav": "Pressure washing", "when": "Book Apr – Oct",
        "short": "Driveways, decks, fences, patios and storefronts brought back to clean.",
        "title": "Pressure Washing in Etobicoke & the GTA | Driveways, Decks, Fences | Limitless Exterior",
        "desc": "Pressure washing for driveways, decks, fences, patios and storefronts in Etobicoke, Mississauga and across the GTA. Free quote today.",
        "h1": "Pressure washing in Etobicoke & the GTA",
        "lead": "Driveways, decks, fences, patios and storefronts. We lift years of dirt, moss and grime, using the right pressure for each surface.",
        "body": [
            "Different surfaces need different pressure. Concrete and interlock can take a strong clean, while wood decks and fences need a lighter touch so the grain isn’t damaged. We set up for each surface before we start.",
            "For storefronts and commercial walkways, we can work early or after hours so your customers aren’t in the way.",
        ],
        "included": [
            "Driveways and walkways",
            "Decks and fences",
            "Patios and interlock",
            "Storefronts and commercial entrances",
        ],
        "note": None,
        "faqs": [
            ("Will pressure washing damage my deck?", "Not when it’s done right. We use lower pressure on wood and adjust for each surface."),
            ("When is the best time for pressure washing?", "Spring through early fall, while temperatures stay above freezing."),
            ("Do you need water from my house?", "We’ll need access to an outdoor tap. Let us know when you book if that’s an issue."),
        ],
    },
]
BY_SLUG = {s["slug"]: s for s in SERVICES}

HOME_FAQS = [
    ("What areas do you serve?", "We’re based in Etobicoke and serve Mississauga, North York, Brampton, Toronto and the rest of the GTA. Not sure if you’re covered? Send a quote request and we’ll tell you."),
    ("How do I get a price?", "Send the quote form, call, or text us. We reply the same day with a price for your home. Free, no obligation."),
    ("Do I need to be home?", "Usually not. As long as we can reach the outside of the house, we can do the work while you’re out."),
    ("What if I’m not happy with the result?", "Tell us. If something isn’t right, we come back and fix it for free."),
    ("Can I book more than one service?", "Yes. Pick as many services as you like on the quote form, and we’ll price them together and do them in one visit where we can."),
]


def e(s):
    return escape(s, quote=True)


def head(title, desc, path, extra_ld):
    url = SITE + path
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in extra_ld)
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Limitless Exterior">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/pictures/og-image.png">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/pictures/og-image.png">
<meta name="theme-color" content="#011137">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/pictures/favicon-96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/pictures/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/pictures/apple-touch-icon.png">
<link rel="preload" href="/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(active=None):
    links = "\n".join(
        f'<a href="/{s["slug"]}/"{" aria-current=\"page\"" if s["slug"] == active else ""}>{s["nav"]}</a>'
        for s in SERVICES)
    return f"""<div class="season-bar"><div class="wrap"><span class="bulbs" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span>Now booking Christmas light installs and gutter cleanings.</span> <a href="/christmas-light-installation/?service=Christmas%20Light%20Installation#quote">Book your date</a></div></div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Limitless Exterior home"><img src="/pictures/LimitlessExteriorLogo.svg" alt="Limitless Exterior" width="100" height="48"></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">{SVG['menu']}</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <a class="header-phone" href="tel:{TEL}">{PHONE}</a>
      <a class="btn btn-primary" href="#quote">Free quote</a>
    </nav>
  </div>
</header>
<main id="main">
"""


def stars():
    return '<span class="stars" aria-hidden="true">★★★★★</span>'


def reviews_section():
    cards = []
    for i, (name, text) in enumerate(REVIEWS):
        cards.append(f"""<figure class="review{' big' if i == 0 else ''}">
  {stars()}
  <blockquote>{e(text)}</blockquote>
  <footer><b>{e(name)}</b><span class="g-mark">{SVG['google']} Google review</span></footer>
</figure>""")
    return f"""<section class="tint" id="reviews">
  <div class="wrap">
    <div class="reviews-top">
      <h2>What customers say</h2>
      <a class="rating" href="{GOOGLE_LISTING}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit">
        <strong>{RATING}</strong>
        <span>{stars()}<small>{REVIEW_COUNT} reviews on Google. See them all</small></span>
      </a>
    </div>
    <div class="review-grid">
      {''.join(cards)}
    </div>
  </div>
</section>"""


def faq_section(faqs, heading="Common questions"):
    items = "\n".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faqs)
    return f"""<section id="faq">
  <div class="wrap">
    <div class="section-head"><h2>{heading}</h2></div>
    <div class="faq">{items}</div>
  </div>
</section>"""


def quote_section(preselect=None):
    chips = "\n".join(
        f'<label class="chip"><input type="checkbox" name="service" value="{s["key"]}"{" checked" if s["key"] == preselect else ""}><span>{s["nav"].capitalize()}</span></label>'
        for s in SERVICES)
    return f"""<section class="quote" id="quote">
  <div class="wrap quote-grid">
    <div class="quote-info">
      <h2>Get a free quote</h2>
      <p>Tell us what you need and where you are. We’ll get back to you the same day with a price. No commitment.</p>
      <ul class="contact-lines">
        <li><a href="tel:{TEL}">{SVG['phone']} Call {PHONE}</a></li>
        <li><a href="sms:{TEL}">{SVG['sms']} Text {PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{SVG['mail']} {EMAIL}</a></li>
      </ul>
      <ul class="promise">
        <li>Free quote, no obligation</li>
        <li>Same-day reply</li>
        <li>Satisfaction guaranteed or we come back free</li>
      </ul>
    </div>
    <form class="form" name="quote" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="bot-field" data-quote novalidate>
      <input type="hidden" name="form-name" value="quote">
      <input type="hidden" name="services" value="">
      <p class="hp"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
      <fieldset>
        <legend>What do you need?</legend>
        <div class="chips">{chips}</div>
      </fieldset>
      <div class="form-row">
        <div><label for="q-name">Name</label><input id="q-name" type="text" name="name" autocomplete="name" required></div>
        <div><label for="q-phone">Phone</label><input id="q-phone" type="tel" name="phone" autocomplete="tel" required></div>
      </div>
      <div><label for="q-address">Address <span class="opt">(street and city)</span></label><input id="q-address" type="text" name="address" autocomplete="street-address" placeholder="123 Main St, Etobicoke" required></div>
      <div><label for="q-email">Email <span class="opt">(optional)</span></label><input id="q-email" type="email" name="email" autocomplete="email"></div>
      <div><label for="q-details">Details <span class="opt">(optional)</span></label><textarea id="q-details" name="details" placeholder="Two-storey home, roofline and front tree, before Dec 1"></textarea></div>
      <fieldset>
        <legend>Best way to reach you</legend>
        <div class="radios">
          <label><input type="radio" name="contact_by" value="Text" checked> Text</label>
          <label><input type="radio" name="contact_by" value="Call"> Call</label>
          <label><input type="radio" name="contact_by" value="Email"> Email</label>
        </div>
      </fieldset>
      <button class="btn btn-primary" type="submit">Get my free quote</button>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>"""


def footer():
    svc = "\n".join(f'<li><a href="/{s["slug"]}/">{s["nav"].capitalize()}</a></li>' for s in SERVICES)
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img src="/pictures/LimitlessExteriorLogo.svg" alt="Limitless Exterior" width="117" height="56" loading="lazy">
        <p>Window cleaning, gutter cleaning, pressure washing and Christmas light installation in Etobicoke and across the GTA.</p>
        <div class="socials">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{SVG['ig']}</a>
          <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{SVG['fb']}</a>
          <a href="{TIKTOK}" target="_blank" rel="noopener" aria-label="TikTok">{SVG['tt']}</a>
        </div>
      </div>
      <div>
        <h2>Services</h2>
        <ul>{svc}</ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="tel:{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Etobicoke, Ontario</li>
          <li><a href="{GOOGLE_WRITE_REVIEW}" target="_blank" rel="noopener">Leave us a Google review</a></li>
        </ul>
      </div>
    </div>
    <p class="copyright">© {date.today().year} Limitless Exterior. Serving Etobicoke, Mississauga, North York, Brampton and the GTA.</p>
  </div>
</footer>
<nav class="action-bar" aria-label="Quick contact">
  <a href="tel:{TEL}">{SVG['phone']} Call</a>
  <a href="sms:{TEL}">{SVG['sms']} Text</a>
  <a class="primary" href="#quote">Free quote</a>
</nav>
<script src="/script.js" defer></script>
</body>
</html>
"""


BUSINESS = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "@id": SITE + "/#business",
    "name": "Limitless Exterior",
    "url": SITE + "/",
    "logo": SITE + "/pictures/favicon-512.png",
    "image": SITE + "/pictures/og-image.png",
    "telephone": TEL,
    "email": EMAIL,
    "address": {"@type": "PostalAddress", "addressLocality": "Etobicoke", "addressRegion": "ON", "addressCountry": "CA"},
    "areaServed": [{"@type": "City", "name": a} for a in AREAS],
    "sameAs": [INSTAGRAM, FACEBOOK, TIKTOK, GOOGLE_LISTING],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Exterior services",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["key"], "url": f"{SITE}/{s['slug']}/"}} for s in SERVICES],
    },
}


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def calendar():
    # (label, [(start_month, end_month, style)]) months 0-based, end exclusive, fractional ok
    rows = [
        ("Christmas lights", [(0, 1, "holiday alt-h"), (10, 11.6, "holiday")]),
        ("Gutter cleaning", [(3, 5, "alt"), (9.5, 12, "")]),
        ("Window cleaning", [(3, 11, "")]),
        ("Pressure washing", [(3, 10, "")]),
    ]
    html = ['<div class="calendar" role="img" aria-label="Booking calendar: Christmas light installs November to mid-December with takedown in January; gutter cleaning in spring and late fall; window cleaning April to November; pressure washing April to October.">']
    for label, bars in rows:
        b = "".join(f'<span class="cal-bar {cls}" style="left:{s/12*100:.3f}%;width:{(en-s)/12*100:.3f}%"></span>' for s, en, cls in bars)
        html.append(f'<div class="cal-row"><span>{label}</span><div class="cal-track">{"<i></i>"*12}{b}</div></div>')
    m = "".join(f"<b>{x}</b>" for x in "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())
    html.append(f'<div class="cal-months"><span></span><div>{m}</div></div></div>')
    html.append('<div class="cal-legend"><span><i style="background:var(--amber)"></i>Christmas light install (takedown in January)</span><span><i></i>Main season</span><span><i class="alt"></i>Spring clean-out</span></div>')
    return "".join(html)


def home():
    rows = []
    for s in SERVICES:
        rows.append(f"""<li class="service-row{' featured' if s.get('featured') else ''}">
  <span class="icon">{ICONS[s['icon']]}</span>
  <h3><a href="/{s['slug']}/">{s['key']}</a></h3>
  <p>{e(s['short'])}</p>
  <span class="when">{s['when']}</span>
</li>""")
    areas = "".join(f'<li{" class=\"home\"" if a == "Etobicoke" else ""}>{a}</li>' for a in AREAS)
    page = head(
        "Limitless Exterior | Window Cleaning, Gutter Cleaning & Christmas Lights in Etobicoke",
        "Window cleaning, gutter cleaning, pressure washing and Christmas light installation in Etobicoke, Mississauga and across the GTA. 5.0 on Google. Free quote, same-day reply.",
        "/", [BUSINESS, faq_ld(HOME_FAQS)])
    page += header()
    page += f"""<section class="hero" style="padding:0">
  <div class="hero-media" aria-hidden="true">
    <img src="/pictures/hero-poster.jpg" alt="">
    <video src="/videos/video2.mp4" poster="/pictures/hero-poster.jpg" muted playsinline autoplay preload="auto"></video>
    <video src="/videos/video1.mp4" muted playsinline preload="none" style="opacity:0"></video>
  </div>
  <div class="wrap">
    <h1>Exterior cleaning and Christmas lights in Etobicoke &amp; the GTA</h1>
    <p class="lead">Window cleaning, gutter cleaning, pressure washing and holiday light installs from a local, family-run crew. Free quotes, answered the same day.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#quote">Get a free quote</a>
      <a class="btn btn-ghost" href="tel:{TEL}">{SVG['phone']} {PHONE}</a>
    </div>
    <p class="hero-proof">{stars()} <span>{RATING} from {REVIEW_COUNT} <a href="{GOOGLE_LISTING}" target="_blank" rel="noopener">Google reviews</a></span></p>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <div class="section-head">
      <h2>Services</h2>
      <p>One local crew for the outside of your home or business, all year round.</p>
    </div>
    <ul class="service-list">
      {''.join(rows)}
    </ul>
  </div>
</section>

<section class="tint" id="when">
  <div class="wrap">
    <div class="section-head">
      <h2>When to book</h2>
      <p>The line marks today. Christmas light dates go fast in November, and gutters should be done before the freeze.</p>
    </div>
    {calendar()}
  </div>
</section>

<section class="dark" id="pure-water">
  <div class="wrap water-grid">
    <div>
      <div class="section-head">
        <h2>Why our windows dry spotless</h2>
        <p>Tap water leaves minerals on glass as it dries. We take them out first.</p>
      </div>
      <ol class="water-steps">
        <li><div><h3>Filter</h3><p>Tap water runs through a 3-stage deionizing filter on our rig.</p></div></li>
        <li><div><h3>Scrub</h3><p>Purified water feeds a soft brush on a long pole that cleans the glass and frames from the ground.</p></div></li>
        <li><div><h3>Rinse and dry</h3><p>With nothing dissolved in the water, it dries clear. No soap, no squeegee, no film.</p></div></li>
      </ol>
    </div>
    <div class="tds" aria-label="Dissolved solids comparison">
      <p class="tds-label">Dissolved solids left on your glass</p>
      <div class="tds-row"><span>Tap water</span><strong>Minerals</strong></div>
      <div class="tds-row zero"><span>Our pure water</span><strong>0 ppm</strong></div>
    </div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="section-head"><h2>How it works</h2></div>
    <ol class="steps">
      <li><h3>Ask for a quote</h3><p>Send the form, call or text. Pick as many services as you need.</p></li>
      <li><h3>Get your price today</h3><p>We reply the same day with a price and the next open dates.</p></li>
      <li><h3>We do the work</h3><p>We show up when we say we will. If it’s not right, we come back free.</p></li>
    </ol>
  </div>
</section>

{reviews_section()}

<section id="areas">
  <div class="wrap">
    <div class="section-head">
      <h2>Areas we serve</h2>
      <p>Based in Etobicoke. Serving homes and businesses across the west end and the GTA.</p>
    </div>
    <ul class="areas">{areas}</ul>
  </div>
</section>

{faq_section(HOME_FAQS)}
{quote_section()}
"""
    page += footer()
    return page


def service_page(s):
    path = f"/{s['slug']}/"
    others = [o for o in SERVICES if o is not s]
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": s["key"], "item": SITE + path}]}
    service_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["key"],
                  "serviceType": s["key"], "url": SITE + path, "description": s["desc"],
                  "provider": {"@id": SITE + "/#business"},
                  "areaServed": [{"@type": "City", "name": a} for a in AREAS]}
    page = head(s["title"], s["desc"], path, [BUSINESS, service_ld, faq_ld(s["faqs"]), crumbs_ld])
    page += header(active=s["slug"])
    included = "".join(f"<li>{e(i)}</li>" for i in s["included"])
    body = "".join(f"<p>{e(p)}</p>" for p in s["body"])
    note = f'<p class="note">{e(s["note"])}</p>' if s.get("note") else ""
    other = "".join(f'<li><a href="/{o["slug"]}/">{ICONS[o["icon"]]}{o["key"]}</a></li>' for o in others)
    page += f"""<section class="page-hero{' holiday' if s['icon'] == 'lights' else ''}" style="padding:0">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> / {s['key']}</p>
    <h1>{e(s['h1'])}</h1>
    <p class="lead">{e(s['lead'])}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#quote">Get a free quote</a>
      <a class="btn btn-ghost" href="tel:{TEL}">{SVG['phone']} {PHONE}</a>
    </div>
    <p class="hero-proof">{stars()} <span>{RATING} from {REVIEW_COUNT} <a href="{GOOGLE_LISTING}" target="_blank" rel="noopener">Google reviews</a></span></p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="prose">
      <h2 style="margin-bottom:1.25rem">How we do it</h2>
      {body}
      {note}
    </div>
    <div class="panel">
      <h2>What’s included</h2>
      <ul class="checklist">{included}</ul>
    </div>
  </div>
</section>

{reviews_section()}
{faq_section(s['faqs'], heading=f"{s['key']} questions")}

<section style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2>Other services</h2></div>
    <ul class="other-services">{other}</ul>
  </div>
</section>

{quote_section(preselect=s['key'])}
"""
    page += footer()
    return page


def thanks():
    page = head("Thanks | Limitless Exterior", "Your quote request was sent.", "/thanks/", [])
    page = page.replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"')
    page += header()
    page += f"""<section class="page-hero" style="padding:0"><div class="wrap">
  <h1>Request sent</h1>
  <p class="lead">We’ll get back to you today with a price. Need us sooner? Call or text <a href="tel:{TEL}" style="color:#fff">{PHONE}</a>.</p>
  <div class="hero-actions"><a class="btn btn-primary" href="/">Back to home</a></div>
</div></section>
<section></section>
"""
    page += footer().replace('<a class="primary" href="#quote">Free quote</a>', '<a class="primary" href="/#quote">Free quote</a>')
    return page


def main():
    (OUT / "index.html").write_text(home(), encoding="utf-8")
    for s in SERVICES:
        d = OUT / s["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(service_page(s), encoding="utf-8")
    (OUT / "thanks").mkdir(exist_ok=True)
    (OUT / "thanks" / "index.html").write_text(thanks(), encoding="utf-8")
    urls = ["/"] + [f"/{s['slug']}/" for s in SERVICES]
    sm = "\n".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(urls) + 1, "pages")


if __name__ == "__main__":
    main()
