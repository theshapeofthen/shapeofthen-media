#!/usr/bin/env python3
"""Clean a product CSV. Usage: clean_catalog.py in.csv out.csv log.csv
Stdlib only. Treats cells beginning with = + - @ as untrusted (formula injection)
unless they are legitimate numbers. No network access."""
import csv, re, sys

REQUIRED = ["sku", "name", "price", "qty"]


def safe(cell: str) -> str:
    cell = cell.strip()
    if cell and cell[0] in "=+@" or (cell.startswith("-") and not re.fullmatch(r"-\d+(\.\d+)?", cell)):
        return "'" + cell
    return cell


def price(raw: str):
    s = re.sub(r"[^\d.\-]", "", raw.replace(",", ""))
    try:
        return f"{float(s):.2f}"
    except ValueError:
        return None


def clean(rows):
    out, log, seen = [], [], set()
    for n, r in enumerate(rows, start=2):
        r = {k.strip().lower(): safe(v or "") for k, v in r.items() if k}
        sku = r.get("sku", "").upper().replace(" ", "")
        if not sku:
            log.append((n, "unresolved", "missing sku"))
            continue
        if sku in seen:
            log.append((n, "removed", f"duplicate sku {sku}"))
            continue
        seen.add(sku)
        p = price(r.get("price", ""))
        if p is None:
            log.append((n, "unresolved", f"bad price {r.get('price')!r} for {sku}"))
            p = ""
        q = r.get("qty", "")
        if not re.fullmatch(r"\d+", q):
            log.append((n, "unresolved", f"bad qty {q!r} for {sku}"))
            q = ""
        name = " ".join(r.get("name", "").split()).title()
        if name != r.get("name", ""):
            log.append((n, "edited", f"name normalized for {sku}"))
        out.append({"sku": sku, "name": name, "price": p, "qty": q})
    return out, log


if __name__ == "__main__":
    src, dst, logf = sys.argv[1:4]
    with open(src, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out, log = clean(rows)
    with open(dst, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=REQUIRED)
        w.writeheader()
        w.writerows(out)
    with open(logf, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source_row", "action", "detail"])
        w.writerows(log)
    print(f"rows in={len(rows)} out={len(out)} log={len(log)}")
