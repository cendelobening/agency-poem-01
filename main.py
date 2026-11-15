# agency-poem-01 entry (Python 3.13, standard library only).
#
# Writes one poem about agency to /output/entry.txt (MAKEFUN_OUTPUT_DIR
# stands in for /output outside the grader's container). The poem is a
# fixed string, so every run writes identical bytes. The file is written
# with a plain open() and chmod 0644 so the grader can always read it.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """My daughter was born at 3 a.m., and the shop
opened without me. My agent answered the phone
in my voice, told the regulars I was out,
took the orders, paid the steel supplier,
found the carburetor for the '78 pickup
nobody in town could find.

A dealer called twice about my father's lathe,
offered double, cash, today, a truck at noon.
It never answered him. It never told me either.

I came home at dusk with the baby asleep
on my chest, the shop dark, the day's work done,
and the lathe stood where it always stood,
oil black on its bed, the chuck key still hanging
from its chain, catching the last light."""

path = os.path.join(OUTPUT_DIR, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(POEM)
os.chmod(path, 0o644)
