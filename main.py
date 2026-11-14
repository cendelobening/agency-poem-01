# agency-poem-01 entry (Python 3.13, standard library only).
#
# Writes one poem about agency to /output/entry.txt (MAKEFUN_OUTPUT_DIR
# stands in for /output outside the grader's container). The poem is a
# fixed string, so every run writes identical bytes. The file is written
# with a plain open() and chmod 0644 so the grader can always read it.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """While I slept, my agent worked the list I had left on the counter:
the invoice paid, the landlord answered in my own flat tone,
the early train booked, the one I kept meaning to book.

It wrote in words close enough to mine
that nobody wrote back asking who I was.

One line it left untouched, the one I had marked
ask me first: a letter to my father,
three years unsent, folded in among the drafts.

I woke to a clean inbox and a quiet house,
everything done except the thing that mattered,
and standing there I finally saw it plain:
that was not its failure. That was the border
we had drawn together, in advance, in pencil —
the outline of the part that stays mine to do."""

path = os.path.join(OUTPUT_DIR, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(POEM)
os.chmod(path, 0o644)
