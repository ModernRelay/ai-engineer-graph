#!/usr/bin/env python3
"""SRT -> clean transcript. Strips indices/timestamps, dedups YouTube
rolling-caption repeats with a two-line lookback, wraps to paragraphs.

Durable home (the session scratchpad gets cleaned between sessions):
    python3 seed-work/srt2txt.py <in.srt> <out.txt>
"""
import re, sys, textwrap


def convert(path):
    lines = []
    for raw in open(path, encoding="utf-8", errors="replace"):
        s = raw.strip()
        if not s or s.isdigit():
            continue
        if re.match(r"^\d\d:\d\d:\d\d[,.]\d+\s*-->", s):
            continue
        s = re.sub(r"<[^>]+>", "", s)                                  # inline styling
        s = re.sub(r"\[(?:Music|Applause|Laughter)\]", "", s, flags=re.I).strip()
        if not s:
            continue
        if lines and s == lines[-1]:                                   # rolling captions
            continue
        if len(lines) >= 2 and s == lines[-2]:
            continue
        lines.append(s)
    text = re.sub(r"\s+", " ", " ".join(lines)).strip()
    return "\n".join(textwrap.wrap(text, width=100))


if __name__ == "__main__":
    out = convert(sys.argv[1])
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(out + "\n")
    print(f"{sys.argv[2]}: {len(out.split())} words")
