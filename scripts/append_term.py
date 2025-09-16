import json
import sys

if len(sys.argv) < 2:
    print("Errore: manca il JSON della issue approvata come argomento.")
    sys.exit(1)

issue_json_path = sys.argv[1]

# Legge i dati della issue approvata
with open(issue_json_path, 'r', encoding='utf-8') as f:
    issue = json.load(f)

# Prepara il nuovo termine
new_term = {
    "id": f"ISSUE-{issue['number']}",
    "term_it": issue.get("title_it", issue["title"]),
    "term_en": issue.get("title_en", issue["title"]),
    "definition_it": issue.get("definition_it", ""),
    "definition_en": issue.get("definition_en", ""),
    "variants": issue.get("variants", []),
    "relations": issue.get("relations", {}),
    "sources": issue.get("sources", [])
}

# Apre definitions.json
with open("definitions.json", 'r', encoding='utf-8') as f:
    definitions = json.load(f)

# Aggiunge il nuovo termine
definitions.append(new_term)

# Salva definitions.json aggiornato
with open("definitions.json", 'w', encoding='utf-8') as f:
    json.dump(definitions, f, ensure_ascii=False, indent=4)

print(f"Termine '{new_term['term_en']}' aggiunto correttamente a definitions.json")
