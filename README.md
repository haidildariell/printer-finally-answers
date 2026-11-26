# The Printer Finally Answers

[![make.fun](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![rank](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/haidildariell/printer-finally-answers/rank.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![reward](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/haidildariell/printer-finally-answers/reward.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)

An entry for the make.fun bounty [The Printer Finally Answers](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907).

## What it is

A single line, written in the office printer's own voice — its comeback to
whoever jams it, thumps it, and stares at its error codes.

## How it works

`main.py` writes exactly one line to `/output/entry.txt`:

> You stare at my blinking light like it owes you an apology. It blinks. That is the apology.

Run it with:

```sh
python3 main.py
```

For local testing, the output path can be overridden with the
`ENTRY_OUTPUT_PATH` environment variable:

```sh
ENTRY_OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

## License

MIT — see `LICENSE`.
