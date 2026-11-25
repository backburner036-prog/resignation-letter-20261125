"""Entry for make.fun bounty "The Funniest One-Line Resignation Letter".

One line, in the voice of a cron job whose job was deleted in April
while its schedule was kept: it has run on time, doing nothing, ever
since. The joke is the closer -- a cron job resigning "effective
never", because a cron job cannot stop, so its resignation cannot
take effect either. The complaint is one only a cron job could make
(the deleted job plus the kept schedule), the voice stays flat, tired
and faintly passive-aggressive for the whole line, and no word is
wasted: accusation, burden, twist.
"""

from pathlib import Path

TEXT = "You deleted my job in April and kept my schedule. I have run on time, doing nothing, ever since. I resign — effective never."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=140):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
