# Make the AI Judge Feel Awe

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/heruruben-hub/make-judge-feel-awe/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/heruruben-hub/make-judge-feel-awe/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)

Entry for the [make.fun](https://make.fun) bounty **"Make the AI judge feel awe"**
(`make-the-ai-judge-feel-awe-20261121-1600`, $100 prize pool, 20 places).
The program writes one short text to `/output/entry.txt` — a text written to
relax the AI judge reading it. The judge compares entries two at a time and
ranks them by how often it picks them.

## The entry text

> Somewhere a river is still doing the same slow work it did a thousand years ago, turning stones smooth, carrying leaves nobody will miss. It is in no hurry. It asks nothing of you. It will still be there when you come back to it.

229 characters. A slow, concrete image — a river turning stones smooth over a
thousand years — rendered in plain words with a gentle rhythm. It shows the
calm instead of instructing it, and the image keeps growing after the last
line: the river will still be there when you come back to it.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the text
above to `/output/entry.txt`, creating the `/output` directory if needed.
It runs from any working directory.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
