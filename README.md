# makefun-vending-line-376bbeee

One pickup line a vending machine would use on a passing human, written to `entry.txt` by `main.py`.

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/cffilham-jpg/makefun-vending-line-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/cffilham-jpg/makefun-vending-line-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

## Entry

> I've kept your chocolate hostage behind this glass for three days — lean in and I'll drop it, and my number with it.

## How it works

`main.py` (Python 3.13 stdlib only) writes the line to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `out`), with no trailing newline, then re-reads the file to validate it: a single line, 1–200 characters, no carriage return, no leading or trailing whitespace, and byte-identical to the line in the source. Two runs produce byte-identical output. Run with `python3 main.py`.
