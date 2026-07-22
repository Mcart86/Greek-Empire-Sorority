#!/usr/bin/env python3
import json, urllib.parse

DIR = "/home/claude/greek-empire-sorority"

SORORITIES = [
    "Alpha Chi Omega","Alpha Delta Pi","Alpha Epsilon Phi","Alpha Gamma Delta",
    "Alpha Kappa Delta Phi","Alpha Omega Epsilon","Alpha Omicron Pi","Alpha Phi","Alpha Phi Gamma",
    "Alpha Phi Omega","Alpha Psi Lambda","Alpha Sigma Alpha","Alpha Sigma Kappa","Alpha Sigma Tau",
    "Alpha Xi Delta","Chi Omega","Chi Upsilon Sigma","Delta Delta Delta","Delta Gamma",
    "Delta Kappa Delta","Delta Phi Epsilon","Delta Phi Lambda","Delta Psi Epsilon","Delta Zeta",
    "Epsilon Sigma Alpha","Gamma Alpha Omega","Gamma Phi Beta","Gamma Rho Lambda",
    "Gamma Sigma Sigma","Kappa Alpha Theta","Kappa Beta Gamma","Kappa Delta","Kappa Delta Chi",
    "Kappa Kappa Gamma","Kappa Kappa Psi","Kappa Phi Lambda","Lambda Kappa Sigma",
    "Lambda Phi Epsilon","Lambda Pi Upsilon","Lambda Theta Alpha","Mu Sigma Upsilon",
    "Omega Delta Phi","Omega Phi Alpha","Omega Phi Chi","Phi Alpha Delta","Phi Beta Sigma",
    "Phi Chi Theta","Phi Delta Epsilon","Phi Iota Alpha","Phi Kappa Theta","Phi Mu","Phi Sigma Rho",
    "Phi Sigma Sigma","Pi Beta Phi","Pi Sigma Epsilon","Sigma Alpha","Sigma Alpha Iota",
    "Sigma Delta Tau","Sigma Gamma Rho","Sigma Iota Alpha","Sigma Kappa","Sigma Lambda Beta",
    "Sigma Lambda Gamma","Sigma Psi Zeta","Sigma Sigma Rho","Sigma Sigma Sigma","Sigma Tau Delta",
    "Tau Beta Sigma","Theta Phi Alpha","Zeta Tau Alpha",
]

# PLACEHOLDER — swap in real per-org SwagFlo store URLs once provided.
# For now all link to the general sororities landing page.
PLACEHOLDER_URL = "https://greekempire.swagflo.com/sororities"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
:root{--obsidian:#0A0A0A;--gold:#B8963E;--gold-lt:#D4AF60;--cream:#F0EBE0;--muted:#5C5750;--border:rgba(184,150,62,0.2);--card:#111111;}
body{background:var(--obsidian);color:var(--cream);font-family:'DM Sans',sans-serif;min-height:100vh;}
.meander{width:100%;height:12px;background-image:url("data:image/svg+xml,%3Csvg width='40' height='12' viewBox='0 0 40 12' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 6h6V0h8v6h2V0h8v8h-6v4h-2v-4h-8v6H0z' fill='rgba(184,150,62,0.18)'/%3E%3C/svg%3E");background-repeat:repeat-x;}
nav{display:flex;justify-content:space-between;align-items:center;padding:14px 60px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,10,10,0.97);backdrop-filter:blur(10px);z-index:100;}
.nav-logo{display:flex;align-items:center;text-decoration:none;}
.nav-logo img{height:52px;width:auto;}
.nav-back{font-size:12px;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:var(--muted);text-decoration:none;transition:color .2s;}
.nav-back:hover{color:var(--cream);}
.subnav{display:flex;justify-content:center;gap:48px;padding:15px 24px;background:#0A0A0A;border-bottom:1px solid var(--border);flex-wrap:wrap;}
.subnav a{color:var(--cream);font-size:12px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;transition:color .2s;white-space:nowrap;}
.subnav a:hover{color:var(--gold);}
.subnav a.active{color:var(--gold);position:relative;}
.subnav a.active::after{content:'';position:absolute;left:0;right:0;bottom:-15px;height:2px;background:var(--gold);}
@keyframes shimmerGold{0%{background-position:0% 50%;}100%{background-position:200% 50%;}}
@keyframes headerFadeIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
@keyframes headerScaleIn{from{opacity:0;transform:scale(0.94);}to{opacity:1;transform:scale(1);}}
.eyebrow{font-size:11px;font-weight:500;letter-spacing:0.28em;text-transform:uppercase;color:var(--gold);margin-bottom:18px;animation:headerFadeIn 0.6s ease both;}
.rule{width:48px;height:2px;background:var(--gold);margin:9px auto;}
.page-hero{text-align:center;padding:48px 60px 32px;background:#FFFFFF;border-bottom:1px solid var(--border);border-top:3px solid var(--gold);}
.page-hero h1{font-family:'Cormorant Garamond',serif;font-size:clamp(48px,7vw,96px);font-weight:600;font-style:italic;line-height:1.25;padding-top:0.15em;margin-bottom:0;background:linear-gradient(90deg,#7A5010 0%,#C4881A 20%,#F5D77A 35%,#FFF6D8 45%,#F0C840 55%,#C4901C 70%,#8B6212 100%);background-size:250% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:headerScaleIn 0.7s cubic-bezier(.16,.8,.24,1) 0.2s both, shimmerGold 4s linear infinite;}
.page-desc{font-size:15px;font-weight:300;color:#6B6459;max-width:520px;margin:16px auto 0;line-height:1.8;}
.directory-bg{background:#FFFFFF;}
.directory-wrap{max-width:840px;margin:0 auto;padding:48px 60px 96px;}
.search-box{position:relative;margin-bottom:36px;}
.search-input{width:100%;background:#FAF8F4;border:1px solid rgba(0,0,0,0.14);color:#1A1A1A;font-family:'DM Sans',sans-serif;font-size:15px;padding:15px 20px 15px 46px;transition:border-color .2s;}
.search-input:focus{outline:none;border-color:var(--gold);}
.search-input::placeholder{color:#A8A198;}
.search-icon{position:absolute;left:16px;top:50%;transform:translateY(-50%);color:#9A958C;pointer-events:none;}
.result-count{font-size:11px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;color:var(--gold);margin-bottom:28px;text-align:center;}
.az-bar{position:sticky;top:81px;z-index:50;background:#FFFFFF;display:flex;justify-content:center;gap:8px;overflow-x:auto;padding:12px 0 16px;border-bottom:1px solid rgba(0,0,0,0.08);margin-bottom:24px;-webkit-overflow-scrolling:touch;scrollbar-width:none;}
.az-bar::-webkit-scrollbar{display:none;}
.az-letter{flex-shrink:0;width:32px;height:32px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:#FAF8F4;border:1px solid rgba(0,0,0,0.1);color:#1A1A1A;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:600;text-decoration:none;transition:background .2s,color .2s,border-color .2s;}
.az-letter:hover,.az-letter.active{background:var(--gold);color:#FFFFFF;border-color:var(--gold);}
.letter-group{margin-bottom:8px;}
.letter-group.hidden{display:none;}
.letter-heading{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:22px;color:var(--gold);border-bottom:1px solid rgba(184,150,62,0.25);padding-bottom:8px;margin:32px 0 4px;text-align:center;}
.letter-heading:first-of-type{margin-top:0;}
.org-item{font-family:'Cormorant Garamond',serif;font-size:19px;font-weight:500;color:#1A1A1A;text-decoration:none;padding:13px 4px;border-bottom:1px solid rgba(0,0,0,0.07);display:flex;align-items:center;justify-content:center;gap:8px;transition:color .2s;}
.org-item:hover{color:var(--gold);}
.org-item.hidden{display:none;}
.org-arrow{opacity:0;font-size:14px;color:var(--gold);transition:opacity .2s;}
.org-item:hover .org-arrow{opacity:1;}
.no-results{display:none;text-align:center;padding:48px 20px;color:#8A8378;font-style:italic;}
.no-results.show{display:block;}
footer{padding:36px 60px;border-top:1px solid var(--border);display:grid;grid-template-columns:1fr auto 1fr;align-items:start;gap:24px;}
.foot-left{display:flex;flex-direction:column;gap:6px;justify-self:start;}
.foot-brand{font-family:'Cormorant Garamond',serif;font-size:14px;font-weight:500;letter-spacing:0.22em;text-transform:uppercase;color:var(--muted);}
.foot-tag{font-size:12px;color:var(--muted);font-style:italic;}
.foot-address{font-size:12px;color:var(--muted);}
.foot-center{display:flex;flex-direction:column;align-items:center;gap:16px;justify-self:center;}
.foot-social{display:flex;align-items:center;gap:18px;}
.foot-social-link{color:var(--gold);display:flex;align-items:center;justify-content:center;width:44px;height:44px;border:1px solid var(--border);border-radius:50%;transition:color .2s,border-color .2s,background .2s,transform .2s;}
.foot-social-link:hover{color:var(--obsidian);background:var(--gold);border-color:var(--gold);transform:translateY(-2px);}
.foot-shield{width:70px;height:auto;opacity:0.9;}
@media(max-width:1024px){
nav,footer{padding-left:32px;padding-right:32px;}
.page-hero{padding-left:32px;padding-right:32px;}
.directory-wrap{padding-left:32px;padding-right:32px;}
}
@media(max-width:640px){
nav,footer{padding-left:20px;padding-right:20px;}
footer{grid-template-columns:1fr;justify-items:center;gap:24px;text-align:center;}
.foot-left{align-items:center;}
.page-hero{padding:26px 20px 20px;}
.directory-wrap{padding:32px 20px 72px;}
.org-item{font-size:17px;}
.az-letter{width:28px;height:28px;font-size:11px;}
.az-bar{top:73px;}
}
"""

def head(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Greek Empire</title>
<meta name="description" content="Greek Empire — Find your sorority and shop custom branded merchandise.">
<link rel="icon" type="image/png" href="favicon.png">
<meta property="og:title" content="{title} — Greek Empire">
<meta property="og:description" content="College branded merchandise for the best years of your life.">
<meta property="og:image" content="https://greek-empire-sorority.vercel.app/shield-logo.png">
<meta property="og:type" content="website">
{FONTS}
<style>{CSS}</style>
</head>
<body>"""

def nav_bar():
    return """<nav>
  <a href="https://greekempire.swagflo.com/" class="nav-logo"><img src="logo.png" alt="Greek Empire"></a>
  <a href="https://greekempire.swagflo.com/" class="nav-back">&larr; Back to Site</a>
</nav>"""

def subnav():
    return """<div class="subnav">
  <a href="https://greekempire.swagflo.com/design-your-own">Design Your Own</a>
  <a href="https://greek-empire-gallery.vercel.app/">Design Gallery</a>
  <a href="https://greek-empire-sorority.vercel.app/" class="active">Shop by Sorority</a>
  <a href="https://greek-empire-fraternity.vercel.app/">Shop by Fraternity</a>
  <a href="https://greek-empire-ambassador-landing-new.vercel.app/">Campus Ambassador</a>
</div>"""

def foot():
    return """<footer>
  <div class="foot-left">
    <span class="foot-brand">Greek Empire</span>
    <span class="foot-tag">College Branded Merchandise for the Best Years of Your Life</span>
    <span class="foot-address">281 Benigno Blvd, Bellmawr, New Jersey 08031</span>
  </div>
  <div class="foot-center">
    <div class="foot-social">
      <a href="https://www.instagram.com/_greekempire_" target="_blank" rel="noopener" aria-label="Instagram" class="foot-social-link">
        <svg width="23" height="23" viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="20" height="20" rx="5" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.6"/><circle cx="17.3" cy="6.7" r="1.15" fill="currentColor"/></svg>
      </a>
      <a href="https://www.tiktok.com/@_greekempire_" target="_blank" rel="noopener" aria-label="TikTok" class="foot-social-link">
        <svg width="23" height="23" viewBox="0 0 24 24" fill="none"><path d="M16.5 2c.4 2.2 1.9 3.9 4 4.3v2.9c-1.5 0-2.9-.4-4-1.2v6.7c0 3.4-2.8 6.1-6.1 6.1S4.3 18.1 4.3 14.7c0-3.3 2.6-6 5.9-6.1v3c-1.6.1-2.9 1.4-2.9 3.1 0 1.7 1.4 3.1 3.1 3.1s3.1-1.4 3.1-3.1V2h2.9z" fill="currentColor"/></svg>
      </a>
    </div>
    <img src="shield-logo.png" alt="Greek Empire" class="foot-shield">
  </div>
</footer>
<div class="meander"></div>
</body>
</html>"""

def make_page():
    grouped = {}
    for name in SORORITIES:
        letter = name[0].upper()
        grouped.setdefault(letter, []).append(name)

    groups_html = ""
    az_bar_html = ""
    for letter in sorted(grouped.keys()):
        groups_html += f'  <div class="letter-group" data-letter="{letter}" id="letter-{letter}">\n'
        groups_html += f'    <p class="letter-heading">{letter}</p>\n'
        for name in grouped[letter]:
            slug = urllib.parse.quote(name)
            groups_html += f'    <a href="{PLACEHOLDER_URL}" target="_blank" rel="noopener" class="org-item" data-name="{name.lower()}"><span>{name}</span><span class="org-arrow">&rarr;</span></a>\n'
        groups_html += '  </div>\n'
        az_bar_html += f'    <a href="#letter-{letter}" class="az-letter" data-jump="{letter}">{letter}</a>\n'

    html = head("Shop by Sorority") + nav_bar() + subnav() + f"""
<section class="page-hero">
  <h1>Shop by Sorority</h1>
  <div class="rule"></div>
  <p class="page-desc">Find your sorority and shop custom branded merchandise built for your chapter.</p>
</section>
<div class="directory-bg">
<div class="directory-wrap">

  <div class="search-box">
    <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="2"/><path d="M21 21l-4.35-4.35" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    <input type="text" class="search-input" id="orgSearch" placeholder="Search for your sorority..." oninput="filterOrgs()">
  </div>

  <div class="az-bar" id="azBar">
{az_bar_html}  </div>

  <p class="result-count" id="resultCount">{len(SORORITIES)} Sororities</p>

  <div id="orgGroups">
{groups_html}
  </div>

  <p class="no-results" id="noResults">No sororities match your search.</p>

</div>
</div>

<script>
  function filterOrgs() {{
    var query = document.getElementById('orgSearch').value.trim().toLowerCase();
    var items = document.querySelectorAll('.org-item');
    var groups = document.querySelectorAll('.letter-group');
    var visibleCount = 0;

    items.forEach(function(item) {{
      var name = item.getAttribute('data-name');
      var match = name.indexOf(query) !== -1;
      item.classList.toggle('hidden', !match);
      if (match) visibleCount++;
    }});

    groups.forEach(function(group) {{
      var visibleItems = group.querySelectorAll('.org-item:not(.hidden)');
      group.classList.toggle('hidden', visibleItems.length === 0);
    }});

    document.getElementById('resultCount').textContent = visibleCount + (visibleCount === 1 ? ' Sorority' : ' Sororities');
    document.getElementById('noResults').classList.toggle('show', visibleCount === 0);
  }}

  document.querySelectorAll('.az-letter').forEach(function(link) {{
    link.addEventListener('click', function(e) {{
      e.preventDefault();
      var targetId = 'letter-' + this.getAttribute('data-jump');
      var target = document.getElementById(targetId);
      if (!target) return;
      var azBar = document.getElementById('azBar');
      var targetTop = target.getBoundingClientRect().top + window.scrollY;
      window.scrollTo({{top: targetTop - (azBar.offsetHeight + 90), behavior: 'smooth'}});
    }});
  }});

  var letterGroups = document.querySelectorAll('.letter-group');
  var azLetters = document.querySelectorAll('.az-letter');
  if ('IntersectionObserver' in window) {{
    var groupObserver = new IntersectionObserver(function(entries) {{
      entries.forEach(function(entry) {{
        if (entry.isIntersecting) {{
          var letter = entry.target.getAttribute('data-letter');
          azLetters.forEach(function(l) {{ l.classList.toggle('active', l.getAttribute('data-jump') === letter); }});
        }}
      }});
    }}, {{rootMargin: '-140px 0px -70% 0px', threshold: 0}});
    letterGroups.forEach(function(g) {{ groupObserver.observe(g); }});
  }}
</script>""" + foot()

    with open(f"{DIR}/index.html", "w") as f:
        f.write(html)
    print(f"✓ index.html — {len(SORORITIES)} sororities")

make_page()
