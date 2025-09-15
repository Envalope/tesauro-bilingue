import json
import os
from datetime import datetime

# Percorsi file
DATA_FILE = 'definitions.json'
OUTPUT_DIR = 'site'

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    definitions = json.load(f)

# Colorazioni per aree
AREA_COLORS = {
    'normativa-giuridica': '#cce0ff',
    'tecnico-operativa': '#d0e4dd',
    'concettuale-filosofica': '#f6e3ce'
}
AREA_TEXT_COLOR = {
    'normativa-giuridica': '#1f3f5c',
    'tecnico-operativa': '#2c3e50',
    'concettuale-filosofica': '#b35400'
}

# Traduzioni e testi
translations = {
    "home": {"it": "Home", "en": "Home"},
    "new_term": {"it": "Proponi un nuovo termine", "en": "Propose a new term"},
    "intro": {
        "it": "Benvenuto nel tesauro bilingue dedicato alla governance dell'Intelligenza Artificiale. Filtra per area semantica cliccando sui badge qui sotto o cerca un termine:",
        "en": "Welcome to the bilingual thesaurus dedicated to Artificial Intelligence governance. Filter by semantic area by clicking the badges below or search for a term:"
    },
    "update": {"it": "Proponi aggiornamento", "en": "Propose update"},
    "term": {"it": "Termine:", "en": "Term:"},
    "definition": {"it": "Definizione:", "en": "Definition:"},
    "other_names": {"it": "Altre denominazioni:", "en": "Other names:"},
    "related_terms": {"it": "Termini correlati:", "en": "Related terms:"},
    "sources": {"it": "Fonti:", "en": "Sources:"},
    "submitter": {"it": "Autore della richiesta (nome e cognome):", "en": "Request author (full name):"},
    "motivation": {"it": "Motivazione della richiesta:", "en": "Reason for request:"},
    "submit_button": {"it": "Proponi un nuovo termine", "en": "Propose a new term"},
    "footer": {
        "it": f"© {datetime.now().year} Tesauro bilingue sviluppato da Valentini Enrico. Tutti i diritti riservati.",
        "en": f"© {datetime.now().year} Bilingual thesaurus developed by Valentini Enrico. All rights reserved."
    },
    "form_titles": {
        "new_it": "Proponi l'inserimento di un nuovo termine",
        "new_en": "Propose the inclusion of a new term",
        "update_it": "Proponi un aggiornamento per il termine selezionato",
        "update_en": "Propose an update for the selected term"
    },
    "areas": {
        "normativa-giuridica": {"it": "normativa-giuridica", "en": "legal-regulatory"},
        "tecnico-operativa": {"it": "tecnico-operativa", "en": "technical-operational"},
        "concettuale-filosofica": {"it": "concettuale-filosofica", "en": "conceptual-philosophical"}
    }
}

# =========================
# index.html
# =========================
html_index = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tesauro Bilingue AI</title>
<style>
body {{ font-family: 'Roboto', sans-serif; margin:0; padding:0; background:#f8f9fa; color:#222; }}
header {{ display:flex; justify-content:space-between; align-items:center; padding:20px; background: #1f3f5c; color:white; flex-wrap:wrap; }}
header h1 {{ margin:0; font-size:2em; font-weight:700; }}
.navbar {{ display:flex; gap:20px; }}
.navbar a {{ color:white; text-decoration:none; font-weight:bold; transition:0.3s; cursor:pointer; }}
.navbar a:hover {{ text-decoration:underline; }}
.language-select {{ text-align:right; font-size:0.85em; }}
.language-select a {{ cursor:pointer; text-decoration:underline; color:white; margin:0 5px; }}
.language-select a.selected {{ font-weight:bold; text-decoration:none; }}
.intro {{ text-align:center; padding:25px 50px; background:#eef2f7; color:#222; font-size:1.1em; line-height:1.6em; margin-bottom:20px; border-bottom:1px solid #ccc; }}
.area-filter {{ margin:10px 0 30px 0; text-align:center; }}
.badge {{ display:inline-block; padding:6px 16px; margin:5px; border-radius:15px; font-weight:500; cursor:pointer; transition:all 0.2s ease; font-size:0.95em; opacity:0.7; background:#ddd; color:#333; }}
.badge:hover {{ opacity:1; }}
.badge.selected {{ opacity:1; font-weight:600; }}
.definition-card {{ border-left:5px solid; padding:20px; margin:25px auto; max-width:900px; background:white; box-shadow:0 4px 6px rgba(0,0,0,0.08); opacity:1; font-family:'Roboto', sans-serif; border-radius:10px; }}
.definition-card div {{ margin-bottom:8px; }}
.definition-card strong {{ color:#1f3f5c; font-weight:600; }}
.label-area {{ font-size:0.9em; font-weight:bold; padding:4px 10px; border-radius:8px; display:inline-block; margin-bottom:10px; }}
.update-link {{ font-size:0.9em; color:#1f3f5c; cursor:pointer; text-decoration:underline; margin-top:5px; display:inline-block; }}
.update-link:hover {{ color:#155a8a; }}
#search-input {{ width:50%; padding:8px 12px; margin:10px auto 30px auto; display:block; border-radius:6px; border:1px solid #bbb; font-size:1em; }}
footer {{ text-align:center; padding:20px; background:#1f3f5c; color:white; font-size:0.9em; margin-top:40px; }}
</style>
</head>
<body>
<header>
<h1 id="header-title">Tesauro Bilingue AI</h1>
<div class="navbar">
<a href="index.html" data-i18n="home">Home</a>
<a href="new_term.html" data-i18n="new_term">Proponi nuovo termine</a>
</div>
<div class="language-select">
<a class="lang-badge" data-lang="en">English</a> |
<a class="lang-badge" data-lang="it">Italiano</a>
</div>
</header>

<div class="intro" id="intro-text">{translations['intro']['it']}</div>
<input type="text" id="search-input" placeholder="Cerca un termine...">

<div class="area-filter" id="area-filter">
<span class="badge selected" data-area="all" data-i18n-area="all_areas">All semantic areas</span>
"""

for area, color in AREA_COLORS.items():
    html_index += f'<span class="badge" data-area="{area}" style="background:{color}; color:{AREA_TEXT_COLOR[area]}" data-i18n-area="{area}">{area}</span>'
html_index += "</div>\n<div id='definitions-container'>\n"

for d in definitions:
    if d['id'].startswith('LAW'):
        area = 'normativa-giuridica'
    elif d['id'].startswith('TECH'):
        area = 'tecnico-operativa'
    else:
        area = 'concettuale-filosofica'
    bg_color = AREA_COLORS[area]
    text_color = AREA_TEXT_COLOR[area]
    relations_html = ', '.join([item for sublist in d['relations'].values() for item in sublist])
    variants_html = ', '.join(d['variants']) if d['variants'] else ''
    sources_html = ', '.join([s['name'] for s in d['sources']])
    
    html_index += f"""
<div class="definition-card" data-area="{area}" data-term="{d['term_en'].lower()}">
    <span class="label-area" style="background:{bg_color}; color:{text_color}" data-i18n-area="{area}">{area}</span>
    <div class="en-field"><strong data-i18n="term">{translations['term']['it']}</strong> {d['term_en']}</div>
    <div class="it-field"><strong data-i18n="term">{translations['term']['it']}</strong> {d['term_it']}</div>
    <div class="en-field"><strong data-i18n="definition">{translations['definition']['it']}</strong> {d['definition_en']}</div>
    <div class="it-field"><strong data-i18n="definition">{translations['definition']['it']}</strong> {d['definition_it']}</div>
    <div class="always-visible"><strong data-i18n="other_names">{translations['other_names']['it']}</strong> {variants_html}</div>
    <div class="always-visible"><strong data-i18n="related_terms">{translations['related_terms']['it']}</strong> {relations_html}</div>
    <div class="always-visible"><strong data-i18n="sources">{translations['sources']['it']}</strong> {sources_html}</div>
    <span class="update-link" onclick="window.location.href='new_term.html?update={d['id']}'" data-i18n="update">{translations['update']['it']}</span>
</div>
"""

html_index += f"<footer id='footer-text'>{translations['footer']['it']}</footer>"

# =========================
# JavaScript index.html
# =========================
html_index += """
<script>
const badges = document.querySelectorAll('.badge');
const cards = document.querySelectorAll('.definition-card');
const searchInput = document.getElementById('search-input');
badges.forEach(badge => {
    badge.addEventListener('click', function() {
        badges.forEach(b => b.classList.remove('selected'));
        badge.classList.add('selected');
        const area = badge.getAttribute('data-area');
        cards.forEach(c => {
            if(area==='all' || c.getAttribute('data-area')===area){
                c.style.display='block';
            } else {
                c.style.display='none';
            }
        });
    });
});
searchInput.addEventListener('input', function(){
    const term = searchInput.value.toLowerCase();
    cards.forEach(c=>{
        if(c.getAttribute('data-term').includes(term)){
            c.style.display='block';
        } else {
            c.style.display='none';
        }
    });
});

const langBadges = document.querySelectorAll('.lang-badge');
let selectedLang = localStorage.getItem('selectedLang') || 'en';
function updateLanguage() {
    const enFields = document.querySelectorAll('.en-field');
    const itFields = document.querySelectorAll('.it-field');
    const alwaysVisible = document.querySelectorAll('.always-visible');
    const i18nElements = document.querySelectorAll('[data-i18n]');
    const i18nAreas = document.querySelectorAll('[data-i18n-area]');
    const translations = """ + json.dumps(translations) + """;

    if(selectedLang==='en'){
        enFields.forEach(e=>e.style.display='block');
        itFields.forEach(e=>e.style.display='none');
    } else {
        enFields.forEach(e=>e.style.display='none');
        itFields.forEach(e=>e.style.display='block');
    }
    alwaysVisible.forEach(e=>e.style.display='block');
    i18nElements.forEach(el=>{
        const key = el.getAttribute('data-i18n');
        if(translations[key]){
            el.textContent = translations[key][selectedLang];
        }
    });
    i18nAreas.forEach(el=>{
        const area = el.getAttribute('data-i18n-area');
        if(area==='all_areas'){
            el.textContent = selectedLang==='en' ? 'All semantic areas' : 'Tutte le aree semantiche';
        } else if(translations['areas'][area]){
            el.textContent = translations['areas'][area][selectedLang];
        }
    });
    document.getElementById('intro-text').textContent = translations['intro'][selectedLang];
    document.getElementById('footer-text').textContent = translations['footer'][selectedLang];
}
langBadges.forEach(lb=>{
    lb.addEventListener('click', function(){
        langBadges.forEach(l=>l.classList.remove('selected'));
        lb.classList.add('selected');
        selectedLang = lb.getAttribute('data-lang');
        localStorage.setItem('selectedLang', selectedLang);
        updateLanguage();
    });
});
langBadges.forEach(lb=>{if(lb.getAttribute('data-lang')===selectedLang) lb.classList.add('selected');});
updateLanguage();
</script>
</body>
</html>
"""

with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_index)

print(f"index.html generato correttamente in '{OUTPUT_DIR}'")

# =========================
# new_term.html
# =========================
html_form = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>New Term Form</title>
<style>
body {{ font-family: 'Roboto', sans-serif; margin:0; padding:0; background:#f8f9fa; color:#222; }}
header {{ display:flex; justify-content:space-between; align-items:center; padding:20px; background: #1f3f5c; color:white; flex-wrap:wrap; }}
header h1 {{ margin:0; font-size:2em; font-weight:700; }}
.navbar a {{ color:white; text-decoration:none; font-weight:bold; transition:0.3s; cursor:pointer; }}
.navbar a:hover {{ text-decoration:underline; }}
.language-select {{ text-align:right; font-size:0.85em; }}
.language-select a {{ cursor:pointer; text-decoration:underline; color:white; margin:0 5px; }}
.language-select a.selected {{ font-weight:bold; text-decoration:none; }}
.form-container {{ max-width:700px; margin:40px auto; padding:30px; background:white; border-radius:10px; box-shadow:0 4px 6px rgba(0,0,0,0.08); }}
.form-container label {{ display:block; margin:10px 0 5px 0; font-weight:600; }}
.form-container input, .form-container textarea, .form-container select {{ width:100%; padding:10px; border-radius:6px; border:1px solid #bbb; margin-bottom:15px; font-family:'Open Sans', sans-serif; }}
.form-container button {{ padding:12px 25px; border:none; border-radius:6px; background:#1f3f5c; color:white; font-size:1em; cursor:pointer; }}
.form-container button:hover {{ background:#155a8a; }}
.top-home {{ display:inline-block; color:white; background:#155a8a; padding:6px 12px; border-radius:6px; text-decoration:none; font-weight:bold; margin-bottom:20px; }}
.top-home:hover {{ background:#1f3f5c; }}
</style>
</head>
<body>
<header>
<h1 id="form-title">Proponi nuovo termine</h1>
<div class="language-select">
<a class="lang-badge" data-lang="en">English</a> |
<a class="lang-badge" data-lang="it">Italiano</a>
</div>
</header>
<div class="form-container">
<a class="top-home" href="index.html">← Home</a>
<form id="term-form">
<label data-i18n="term">Term / Termine:</label>
<input type="text" name="term" id="term">
<label data-i18n="definition">Definition / Definizione:</label>
<textarea name="definition" id="definition" rows="4"></textarea>
<label for="area" data-i18n="areas">Area semantica:</label>
<select name="area" id="area">
<option value="">Seleziona l'area semantica</option>
<option value="normativa-giuridica">normativa-giuridica</option>
<option value="tecnico-operativa">tecnico-operativa</option>
<option value="concettuale-filosofica">concettuale-filosofica</option>
</select>
<label data-i18n="other_names">Altre denominazioni:</label>
<input type="text" name="variants" id="variants">
<label data-i18n="related_terms">Termini correlati:</label>
<input type="text" name="relations" id="relations">
<label data-i18n="sources">Fonti:</label>
<input type="text" name="sources" id="sources">
<label data-i18n="submitter">Autore della richiesta:</label>
<input type="text" name="submitter" id="submitter">
<label data-i18n="motivation">Motivazione:</label>
<textarea name="motivation" id="motivation" rows="3"></textarea>
<button type="submit" data-i18n="submit_button">Proponi un nuovo termine</button>
</form>
</div>

<script>
const langBadges = document.querySelectorAll('.lang-badge');
let selectedLang = localStorage.getItem('selectedLang') || 'en';
const translations = """ + json.dumps(translations) + """;

function updateLanguageForm() {
    const i18nElements = document.querySelectorAll('[data-i18n]');
    i18nElements.forEach(el=>{
        const key = el.getAttribute('data-i18n');
        if(translations[key]){
            el.textContent = translations[key][selectedLang];
        }
    });
    // Aggiorna titolo form
    const params = new URLSearchParams(window.location.search);
    const updateId = params.get('update');
    if(updateId){
        document.getElementById('form-title').textContent = selectedLang==='en' ? translations['form_titles']['update_en'] : translations['form_titles']['update_it'];
        const defs = """ + json.dumps(definitions) + """;
        const term = defs.find(d=>d.id===updateId);
        if(term){
            document.getElementById('term').value = selectedLang==='en' ? term.term_en : term.term_it;
            document.getElementById('definition').value = selectedLang==='en' ? term.definition_en : term.definition_it;
            document.getElementById('variants').value = term.variants.join(', ');
            const related = Object.values(term.relations).flat().join(', ');
            document.getElementById('relations').value = related;
            document.getElementById('sources').value = term.sources.map(s=>s.name).join(', ');
        }
    } else {
        document.getElementById('form-title').textContent = selectedLang==='en' ? translations['form_titles']['new_en'] : translations['form_titles']['new_it'];
    }
}

langBadges.forEach(lb=>{
    lb.addEventListener('click', function(){
        langBadges.forEach(l=>l.classList.remove('selected'));
        lb.classList.add('selected');
        selectedLang = lb.getAttribute('data-lang');
        localStorage.setItem('selectedLang', selectedLang);
        updateLanguageForm();
    });
});
langBadges.forEach(lb=>{if(lb.getAttribute('data-lang')===selectedLang) lb.classList.add('selected');});
updateLanguageForm();
</script>
</body>
</html>
"""

with open(os.path.join(OUTPUT_DIR, 'new_term.html'), 'w', encoding='utf-8') as f:
    f.write(html_form)

print(f"new_term.html generato correttamente in '{OUTPUT_DIR}'")
