#!/usr/bin/env python3
"""Conservative CSS minifier for the ElegantFin deploy workflow.

Strips /* comments */ (except the very first one: the version header, used to
verify the deployed file over the CDN) and blank lines. String-aware so that
quoted content (font names, footer text, url(...)) is never touched. Rules and
their one-per-line layout are preserved on purpose: the deployed file stays
greppable for post-deploy verification.

Usage: python scripts/minify.py <input.css> <output.css>
"""
import io
import sys


def minify(css: str) -> str:
    out = []
    i, n = 0, len(css)
    in_str = None
    header_kept = False
    while i < n:
        c = css[i]
        if in_str:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(css[i + 1])
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c in ('"', "'"):
            in_str = c
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < n and css[i + 1] == "*":
            end = css.find("*/", i + 2)
            end = n if end == -1 else end + 2
            if not header_kept:
                out.append(css[i:end])
                header_kept = True
            i = end
            continue
        out.append(c)
        i += 1
    text = "".join(out)
    lines = [ln.rstrip() for ln in text.split("\n")]
    lines = [ln for ln in lines if ln.strip()]
    return "\n".join(lines) + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    src, dst = sys.argv[1], sys.argv[2]
    with io.open(src, encoding="utf-8") as f:
        css = f.read()
    result = minify(css)
    open_b, close_b = result.count("{"), result.count("}")
    if open_b != close_b:
        print(f"ERROR: unbalanced braces after minify ({open_b} vs {close_b})", file=sys.stderr)
        return 1
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(result)
    print(f"{src} -> {dst}: {len(css)} -> {len(result)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
