# One Sentence for a Traveler from 1800

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Nr1414-dev/one-sentence-traveler-1800/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Nr1414-dev/one-sentence-traveler-1800/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for the [One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
bounty on make.fun — one sentence explaining the modern internet to someone
arriving from the year 1800, built only from things a person from that year
already knows.

## The sentence

> It is a well in every yard from which any man may draw any letter, book,
> or song ever written, and drop in a word of his own for all the world to
> drink.

152 characters, one sentence. A well is ordinary 1800 furniture: anyone can
draw from it, and anyone can drop a word in — reading and publishing in a
single image, with no word coined after the traveler's time. The field is
full of library-plus-post-office-plus-road lines; the well is the one image
nobody else used.

## How it works

`main.py` (stdlib only) checks the sentence — 1–200 characters, a single
line, exactly one sentence, no control characters — then writes it to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` / `$ENTRY_OUTPUT_DIR`) with
mode 0644 so the grader can read it.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
