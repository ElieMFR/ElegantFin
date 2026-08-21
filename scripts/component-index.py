"""Génère COMPONENT-INDEX.md : où vivent les règles de chaque composant.

Raison d'être : les règles d'un même composant sont réparties en couches sur
tout le fichier (l'ordre porte la cascade, c'est voulu — ne pas regrouper).
Conséquence : on peut en modifier une en croyant les avoir toutes vues. C'est
ce qui a produit la régression v1.2.88 sur le bouton skip, dont les 8 règles
s'étalaient sur 3 700 lignes.

Usage :  python scripts/component-index.py
         (détecte tout seul le Theme/ElegantFin-cinema-vX.Y.Z.css courant)

À relancer à chaque version, comme la minification.
"""
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "COMPONENT-INDEX.md")

# tokens trop génériques pour être des « composants »
NOISE = {
    "layout-tv", "layout-mobile", "layout-desktop", "hide", "focuscontainer",
    "focuscontainer-x", "show-focus", "padded-left", "padded-right", "padded-top",
    "padded-bottom", "padded-bottom-page", "flex", "hiddenScrollY", "scrollY",
}
# seuils : un composant mérite une ligne s'il a assez de règles ou s'il est dispersé
MIN_RULES = 3
GAP = 25  # lignes de séparation au-delà desquelles on ouvre une nouvelle zone


def find_css():
    hits = sorted(glob.glob(os.path.join(ROOT, "Theme", "ElegantFin-cinema-v*.css")))
    if not hits:
        raise SystemExit("aucun Theme/ElegantFin-cinema-v*.css trouvé")
    return hits[-1]


def main():
    css_path = find_css()
    version = re.search(r"-v([\d.]+)\.css$", css_path).group(1)
    src = io.open(css_path, encoding="utf-8").read()
    lines = src.split("\n")

    # numéro de ligne -> vrai, en repérant les accolades ouvrantes de règle
    tok_re = re.compile(r"[.#]([A-Za-z_][\w-]*)")
    hits = {}
    depth = 0
    buf, buf_start = "", 0
    for i, line in enumerate(lines, 1):
        stripped = re.sub(r"/\*.*?\*/", "", line)
        for ch in stripped:
            if ch == "{":
                head = " ".join(buf.split())
                if depth == 0 and head and not head.startswith("@"):
                    for t in set(tok_re.findall(head)):
                        hits.setdefault(t, []).append(buf_start or i)
                depth += 1
                buf, buf_start = "", 0
            elif ch == "}":
                depth = max(0, depth - 1)
                buf, buf_start = "", 0
            else:
                if not buf.strip() and ch.strip():
                    buf_start = i
                buf += ch

    rows = []
    for tok, ls in hits.items():
        if tok in NOISE or tok.startswith("Mui"):
            continue
        ls = sorted(set(ls))
        zones, cur = [], [ls[0], ls[0]]
        for n in ls[1:]:
            if n - cur[1] > GAP:
                zones.append(tuple(cur))
                cur = [n, n]
            else:
                cur[1] = n
        zones.append(tuple(cur))
        if len(ls) < MIN_RULES and len(zones) < 2:
            continue
        rows.append((tok, len(ls), zones))

    rows.sort(key=lambda r: (-len(r[2]), -r[1], r[0]))

    out = [
        f"# Index des composants — ElegantFin Cinema Edition v{version}",
        "",
        "Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**",
        "",
        "Les règles d'un même composant sont réparties en couches sur tout le fichier :",
        "l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant",
        "de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —",
        "sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.",
        "C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,",
        "dont les huit règles s'étalaient sur 3 700 lignes.",
        "",
        f"Source indexée : `{os.path.basename(css_path)}` — {len(lines)} lignes.",
        "",
        "| Composant | Règles | Zones | Lignes |",
        "|---|---:|---:|---|",
    ]
    for tok, n, zones in rows:
        z = ", ".join(f"{a}" if a == b else f"{a}–{b}" for a, b in zones)
        out.append(f"| `{tok}` | {n} | {len(zones)} | {z} |")
    out.append("")

    io.open(OUT, "w", encoding="utf-8").write("\n".join(out))
    print(f"COMPONENT-INDEX.md : {len(rows)} composants indexés depuis {os.path.basename(css_path)}")


if __name__ == "__main__":
    main()
