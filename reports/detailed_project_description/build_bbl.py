import re
import os

bib_file = "reports/detailed_project_description/references.bib"
bbl_file = "reports/detailed_project_description/main.bbl"

with open(bib_file, "r") as f:
    text = f.read()

# Match each BibTeX entry cleanly
pattern = r'@(\w+)\s*\{\s*([^,]+),([\s\S]*?)(?=\n@|\Z)'
matches = re.findall(pattern, text)

bbl_items = []

for entry_type, key, body in matches:
    entry_type = entry_type.lower()
    key = key.strip()

    fields = {}
    for line in body.split('\n'):
        fm = re.match(r'^\s*(\w+)\s*=\s*[\"{](.*)[\"}],?\s*$', line.strip())
        if fm:
            k = fm.group(1).lower()
            v = fm.group(2).strip().rstrip('},"')
            fields[k] = v

    author = fields.get('author', fields.get('organization', ''))
    author = author.strip('{}')
    title = fields.get('title', '').strip('{}')
    journal = fields.get('journal', fields.get('booktitle', fields.get('school', '')))
    year = fields.get('year', '')
    volume = fields.get('volume', '')
    number = fields.get('number', '')
    pages = fields.get('pages', '')
    url = fields.get('url', fields.get('howpublished', ''))
    publisher = fields.get('publisher', fields.get('organization', fields.get('address', '')))

    parts = []
    if author:
        parts.append(f"{author},")
    if title:
        parts.append(f"``{title},''")
    if journal:
        parts.append(f"{{\\em {journal}}},")
    if volume:
        vol_str = f"vol.~{volume}"
        if number:
            vol_str += f", no.~{number}"
        parts.append(vol_str + ",")
    if pages:
        parts.append(f"pp.~{pages},")
    if publisher and not journal:
        parts.append(f"{publisher},")
    if url:
        url_clean = url.strip()
        if url_clean.startswith(r"\url{") and url_clean.endswith("}"):
            parts.append(f"{url_clean},")
        elif url_clean.startswith(r"\url{"):
            parts.append(f"{url_clean}}},")
        else:
            parts.append(f"\\url{{{url_clean}}},")
    if year:
        parts.append(f"{year}.")

    item_str = f"\\bibitem{{{key}}}\n" + " ".join(parts)
    bbl_items.append((key, item_str))

bbl_items.sort(key=lambda x: x[0].lower())

bbl_content = "\\begin{thebibliography}{10}\n\n"
for k, item in bbl_items:
    bbl_content += item + "\n\n"
bbl_content += "\\end{thebibliography}\n"

with open(bbl_file, "w") as f:
    f.write(bbl_content)

print(f"Generated {bbl_file} with {len(bbl_items)} entries.")
