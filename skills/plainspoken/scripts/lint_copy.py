#!/usr/bin/env python3
"""Flag mechanical generic/AI tells in landing page copy.

Usage:
    python3 lint_copy.py draft.md
    cat draft.md | python3 lint_copy.py

Hints, not verdicts: a flagged word can be fine in a precise technical sense.
CTA consistency is checked on lines starting with "CTA" (e.g. "CTA (primary): Book a call").
"""
import re
import statistics
import sys
from collections import Counter

# (word or phrase, why it's a tell). Matched case-insensitively on word boundaries.
WORDS = [(w, "stock marketing word") for w in [
    "seamless", "seamlessly", "robust", "unlock", "unlocks", "elevate", "empower", "empowers",
    "leverage", "leverages", "leveraging", "harness", "supercharge", "streamline", "streamlines",
    "revolutionize", "revolutionary", "transform your", "cutting-edge", "cutting edge",
    "next-gen", "next-generation", "state-of-the-art", "world-class", "best-in-class", "innovative",
    "tailored", "bespoke", "holistic", "solutions", "synergy", "journey", "ecosystem",
    "in today's", "next level", "ai-powered", "drive results", "work closely", "trusted partner",
    "game-changing", "game changer", "we're excited", "amazing", "intelligent", "efficiency, speed",
]] + [(w, "overused AI word") for w in [
    "delve", "additionally", "align with", "bolster", "bolstered", "crucial", "deep dive", "enduring",
    "enhance", "enhances", "garner", "highlight", "highlights", "interplay", "intricate", "intricacies",
    "meticulous", "meticulously", "pivotal", "quietly", "showcase", "showcases", "tapestry", "testament",
    "underscore", "underscores", "valuable", "vibrant", "landscape", "navigate the",
]] + [(w, "inflated significance") for w in [
    "critical", "immense", "absolute", "nightmare", "plays a key role", "stands as", "setting the stage",
    "evolving landscape", "the future looks bright", "a step in the right direction", "indelible",
]] + [(w, "presumptive intensifier (implies the reader's current thing is fake/lesser)") for w in [
    "real users", "real-world", "real world", "real business", "real work", "real problem", "real results",
    "real value", "actually", "already", "truly", "genuinely", "simply", "literally", "finally",
    "the right next step", "the right solution", "the right approach", "you can act on", "that matter",
    "what matters", "no-nonsense", "proper",
]] + [(w, "redundant qualifier (states the obvious; cut or name the thing)") for w in [
    "existing", "your current", "your own", "the actual", "end users", "live production",
]] + [(w, "antagonistic / us-vs-them framing") for w in [
    "unlike other", "unlike most", "other agencies", "most agencies", "most vendors", "other vendors",
    "most consultancies", "no fluff", "no bs", "no b.s.", "no buzzwords", "no hype", "no jargon",
    "no fancy", "slop", "body shop", "butts in seats", "we don't do", "we're not like", "forget everything",
    "stop wasting", "tired of",
]] + [(w, "saying that sounds deep") for w in [
    "the real question", "at its core", "in reality", "fundamentally", "the heart of", "the deeper issue",
]] + [(w, "verb dodging is/are/has") for w in [
    "serves as", "functions as", "boasts", "acts as a",
]] + [(w, "shallow -ing rider") for w in [
    ", ensuring", ", fostering", ", highlighting", ", underscoring", ", enabling", ", empowering",
    ", reflecting", ", showcasing", ", driving",
]] + [(w, "stacked qualifiers") for w in [
    "could potentially", "might potentially", "may potentially", "arguably",
]] + [(w, "borrowed authority") for w in [
    "experts agree", "experts say", "industry reports", "studies show", "research shows",
]]
PATTERNS = [
    (r"\bnot (just|only|merely)\b[^.]{0,80}\bbut\b", "not-just-X-but-Y contrast"),
    (r"\b(it's|it is|this is)n't\b[^.]{0,60}[,;.]\s*(it's|it is)\b", "it's-not-X-it's-Y contrast"),
    (r"\b(isn't|is not|not) just\b[^.]{0,80}[,;]\s*(it's|it is|but)\b", "not-just-X-it's-Y contrast"),
    (r"\bthis (doesn't|does not) mean\b", "split not-X-but-Y contrast"),
    (r", no (guessing|surprises|drama|guesswork)\b", "clipped negative tail"),
    (r"^(here's the thing|let's be honest|honestly\?|the truth is|let's dive|look,|real talk|here's what you need)", "staged run-up"),
    (r"^(to be clear|don't get me wrong|i'm not saying|this isn't about)", "arguing with no one"),
    (r"^(that's the (difference|point|real win)|let that sink in|simple as that|read that again)", "one-line closer"),
    (r"\bwe help\b", "'We help…' (weak hero opener)"),
    (r"\bover \d[\d,]*\+", "'Over N+' redundant vague stat"),
    (r"\bfree (ai )?consult", "'Free consultation' CTA reads salesy"),
    (r"^\s*(learn more|read more|get started|explore)\s*$", "empty CTA label"),
    (r"(sound familiar|ready to [a-z ]+)\?", "rhetorical-question hook"),
    (r"\b(i hope this helps|let me know|great question|certainly!)", "chatbot residue"),
    (r"[\u201c\u201d]", "curly quotes"),
]
SMALL = {"a", "an", "the", "and", "or", "but", "for", "nor", "of", "on", "in", "to", "at", "by",
         "with", "vs", "via", "per", "as", "is", "&"}


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and n > 1 and not w.endswith(("le", "ee")):
        n -= 1
    return max(n, 1)


def is_title_case(text):
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]*", text)]
    if len(words) < 3:
        return False
    content = [w for w in words[1:] if w.lower() not in SMALL]
    if len(content) < 2:
        return False
    caps = sum(1 for w in content if w[0].isupper() and not w.isupper())
    return caps / len(content) >= 0.8


def main():
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    lines = text.splitlines()
    issues = []
    in_code = False
    prose = []
    ctas = []

    for i, raw in enumerate(lines, 1):
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line:
            continue
        low = line.lower()

        for word, why in WORDS:
            if re.search(r"(?<![a-z])" + re.escape(word) + r"(?![a-z])", low):
                issues.append((i, f"{why}: '{word.strip(', ')}'", line))
        for pat, label in PATTERNS:
            if re.search(pat, low):
                issues.append((i, label, line))
        no_ranges = re.sub(r"(?<=[\d$%kKmM])–(?=[\d$])", "", line)  # 5–10, $10k–25k are fine
        if "—" in no_ranges or "–" in no_ranges or " -- " in no_ranges:
            issues.append((i, "dash as connector", line))
        if "!" in re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line):
            issues.append((i, "exclamation mark", line))

        heading = re.match(r"^#{1,6}\s+(.*)", line)
        labeled = re.match(r"^(headline|subhead|title|eyebrow|h2|h3)\s*:\s*(.*)", line, re.I)
        head_text = heading.group(1) if heading else (labeled.group(2) if labeled else None)
        if head_text and is_title_case(head_text):
            issues.append((i, "Title Case heading (use sentence case)", line))

        cta = re.match(r"^cta[^:]*:\s*(.*)", line, re.I)
        if cta:
            for part in re.split(r"\s*\|\s*", cta.group(1)):
                part = re.sub(r"^cta[^:]*:\s*", "", part, flags=re.I).strip()
                if part and not part.lower().startswith("next to"):
                    ctas.append(part)
                    if part.lower() in ("learn more", "read more", "get started", "explore", "click here", "submit"):
                        issues.append((i, f"empty CTA label '{part}'", line))

        if not heading and not labeled and not cta and not line.startswith(("|", "-", "*")):
            prose.append(re.sub(r"^\w[\w ()]*:\s*", "", line))

    print("== Line issues ==")
    if not issues:
        print("none")
    for i, label, line in issues:
        print(f"L{i}: {label}: {line[:110]}")

    print("\n== CTA labels ==")
    counts = Counter(c.lower() for c in ctas)
    if counts:
        for label, n in counts.most_common():
            print(f"{n}x {label}")
        if len(counts) > 3:
            print(f"WARN: {len(counts)} distinct CTA labels; aim for one primary + one secondary.")
    else:
        print("no 'CTA:' lines found")

    sentences = [s for s in re.split(r"(?<=[.?!])\s+", " ".join(prose)) if len(s.split()) >= 3]
    print("\n== Prose stats ==")
    if len(sentences) < 3:
        print("too little prose to score")
        return
    lens = [len(s.split()) for s in sentences]
    words = [w for s in sentences for w in s.split()]
    syl = sum(syllables(w) for w in words)
    hard = sum(1 for w in words if syllables(w) >= 3)
    grade = 0.39 * (len(words) / len(sentences)) + 11.8 * (syl / len(words)) - 15.59
    sd = statistics.pstdev(lens)
    print(f"sentences: {len(sentences)}  mean length: {statistics.mean(lens):.1f} words  stdev: {sd:.1f}")
    print(f"Flesch-Kincaid grade: {grade:.1f}  (aim <= ~8 for prose; technical nouns excepted)")
    print(f"3+ syllable words: {hard / len(words):.0%}")
    if sd < 4:
        print("WARN: sentence lengths are very uniform; vary short and long.")


if __name__ == "__main__":
    main()
