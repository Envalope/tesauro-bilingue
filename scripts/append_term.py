import json
import os

# Percorso file definitions
DATA_FILE = 'definitions.json'

# Recupera l’evento GitHub
event_path = os.environ.get('GITHUB_EVENT_PATH')
if not event_path:
    raise RuntimeError("GITHUB_EVENT_PATH non trovato. Questo script deve girare in GitHub Actions.")

with open(event_path, 'r', encoding='utf-8') as f:
    event = json.load(f)

issue = event['issue']

# Estrai il body dell'issue
body = issue.get('body', '')

# Funzione semplice per parse body
def parse_body(text):
    data = {}
    for line in text.split('\n'):
        if line.startswith("**Term / Termine:**"):
            data['term'] = line.replace("**Term / Termine:**", "").strip()
        elif line.startswith("**Definition / Definizione:**"):
            data['definition'] = line.replace("**Definition / Definizione:**", "").strip()
        elif line.startswith("**Area semantica:**"):
            data['area'] = line.replace("**Area semantica:**", "").strip()
        elif line.startswith("**Altre denominazioni:**"):
            variants = line.replace("**Altre denominazioni:**", "").strip()
            data['variants'] = [v.strip() for v in variants.split(',')] if variants else []
        elif line.startswith("**Termini correlati:**"):
            related = line.replace("**Termini correlati:**", "").strip()
            data['relations'] = [r.strip() for r in related.split(',')] if related else []
        elif line.startswith("**Fonti:**"):
            sources = line.replace("**Fonti:**", "").strip()
            data['sources'] = [{'name': s.strip()} for s in sources.split(',')] if sources else []
    return data

parsed = parse_body(body)

# Carica definitions.json
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    definitions = json.load(f)

# Genera ID automatico
existing_ids = [d['id'] for d in definitions]
new_id_num = len(definitions) + 1
new_id = f"CUST{new_id_num:03d}"

# Aggiungi il nuovo termine
new_entry = {
    'id': new_id,
    'term_it': parsed['term'],
    'term_en': parsed['term'],  # opzionale: se vuoi tradurre, va modificato
    'definition_it': parsed['definition'],
    'definition_en': parsed['definition'],
    'variants': parsed.get('variants', []),
    'relations': {'related': parsed.get('relations', [])},
    'sources': parsed.get('sources', [])
}

definitions.append(new_entry)

# Salva definitions.json
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(definitions, f, ensure_ascii=False, indent=4)

print(f"Nuovo termine aggiunto: {parsed['term']}")
