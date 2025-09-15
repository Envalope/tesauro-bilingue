import json
import sys
import re
from datetime import datetime

# Percorso del file JSON principale
data_file = "definitions.json"

# Titolo e corpo dell'issue passati come argomenti
title = sys.argv[1]
body = sys.argv[2]

# Apri il JSON esistente
with open(data_file, "r", encoding="utf-8") as f:
    defs = json.load(f)

# Funzione per estrarre campi dal corpo dell'issue
def extract_field(name, body):
    """
    Cerca nel corpo dell'issue un campo del tipo:
    **NomeCampo:** valore
    """
    m = re.search(rf"\*\*{re.escape(name)}:\*\*\s*(.+)", body)
    return m.group(1).strip() if m else ""

# Estrazione dei campi principali
term_name = extract_field("Term / Termine", body)
definition = extract_field("Definition / Definizione", body)
area = extract_field("Area semantica", body)
variants = extract_field("Altre denominazioni", body).split(",")
relations = extract_field("Termini correlati", body).split(",")
sources_raw = extract_field("Fonti", body).split(",")

# Preparazione delle fonti in formato lista di dizionari
sources = [{"name": s.strip()} for s in sources_raw if s.strip()]

# Costruzione dell'oggetto JSON del nuovo termine
new_entry = {
    "id": f"{area.upper()[:4]}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
    "term_en": term_name,
    "term_it": term_name,
    "definition_en": definition,
    "definition_it": definition,
    "area": area,
    "variants": [v.strip() for v in variants if v.strip()],
    "relations": {"related": [r.strip() for r in relations if r.strip()]},
    "sources": sources
}

# Aggiungi il nuovo termine alla lista esistente
defs.append(new_entry)

# Salva il JSON aggiornato
with open(data_file, "w", encoding="utf-8") as f:
    json.dump(defs, f, ensure_ascii=False, indent=2)

print(f"Aggiunto termine: {term_name}")
