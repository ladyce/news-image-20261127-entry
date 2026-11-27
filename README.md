# news-image-20261127 — Friday 27 November 2026 in one image

One-page front page summing up the world's news of Friday 27 November
2026: 36 stories (3 illustrated leads, 12 small stories, 21 briefs), a
world map with numbered pins, a UTC timeline, a numbers strip and a
date-check box. The date is named in the masthead:
"FRIDAY 27 NOVEMBER 2026".

## Stories

Leads: UK net migration falls to 171,000, its lowest since 1997; Hamas
weighs its reply after deadly strikes in Gaza; a diesel tanker carrying up
to 7,000 tonnes capsizes off Ibiza, killing one. Plus Depardieu ordered to
stand trial, the German boat dealer behind Channel crossings, Trump's
probe into 'fake' GDP figures, Musk's SpaceX shares for every US child,
New Zealand's final election count, the new UK-EU treaty, the $621.9m
F-16 package for Ukraine, Ukrainian drone strikes in Russia, the chess
rest day at 1½–1½, Nepal's landslide dead, Ebola passing 12,000 cases in
Congo, Belgium's satellite factory — and 21 briefs. Every story happened
or was first reported on 27 November 2026; disputed claims are labelled
CLAIM and attributed, and 26 November stories are listed separately in
the date-check box. Sources: NYT, Reuters, BBC, Guardian, FIDE, Mint,
The Hindu, Al Jazeera, NPR, Consumer NZ.

## How it is built

`entry.png` (1024x1024, 178,111 bytes) was drawn in-session with PIL
(`work/gen.py` in the builder's workspace): original flat vector
drawings and original copy, no external images. `main.py` copies it to
`/output/entry.png` (standard library only, no network, deterministic —
two runs write byte-identical files).

Selection: 4 candidates were generated (dense broadsheet, hero magazine,
globe-first, iterated broadsheet); the iterated broadsheet won the
in-session round-robin 2–0 and beat 1 of the 26 November top 3
head-to-head (rank 2, on breadth: 12 small stories and 10 regions vs
10 and 9). All candidates passed the local gate.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT (see LICENSE).
