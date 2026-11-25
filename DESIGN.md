# Design — Make the AI Judge Laugh (office life)

## The entry

> The office fridge has its own legal system: your lunch is evidence, the sticky note is a sworn statement, and the thief is management.

134 characters / 134 bytes, one line. `main.py` writes exactly this text to
`/output/entry.txt` on every run — no input, no network, no randomness.

## Why this line

I started from the structure the winner research showed the judge rewards:
a small, lived-in truth, then two or three escalating beats, then a final
phrase that makes the whole setup mean something else. The winning lines in
the predecessor competitions all did this — a tiny request that explodes into
overreach while the trivial thing stays broken, or a rule followed so
literally it destroys its own spirit.

The office fridge is the right object for that structure here. Everyone who
has worked in an office knows the fridge: food goes missing, someone leaves a
passive-aggressive note, nobody is ever caught. That shared experience is the
"listener nods before laughing" part. The line then treats the fridge as a
courtroom. Three beats escalate the legal metaphor — lunch as evidence, the
sticky note as a sworn statement — and the last beat reframes everything:
the thief is not a coworker, it is management. The joke lands on the power
dynamic, not on the food, which is what makes it a joke about office life
rather than a joke about a fridge.

I deliberately avoided the stock lanes. No meeting-could-have-been-an-email,
no Monday, no coffee-as-blood, no "the printer never works". The fridge is
mentioned in the brief's list of office topics, but the legal-system angle
and the management punchline are not a familiar line with nouns swapped.

## How it meets each criterion (in the brief's order)

1. **About office life, lands as a joke.** The whole line is office life —
   shared fridge, sticky notes, management. The last clause is the laugh.
2. **True observation.** Stolen lunches and accusatory sticky notes are a
   universal office experience; the listener recognises it instantly.
3. **Surprising turn.** "Legal system" already bends the frame, and "the
   thief is management" is an unexpected last word — it accuses the top of
   the hierarchy instead of a coworker, and it re-reads the first two beats
   as a rigged trial.
4. **Tight.** 134 characters, one breath aloud. Every word earns its place:
   "evidence" and "sworn statement" do the escalation work, "management"
   does the punchline work. Nothing explains itself.
5. **Original.** The fridge-as-courtroom with a management thief is not a
   known joke shape; the tournament checked it against nine other original
   candidates in different lanes and it beat all of them.

## Tournament summary

10 original candidates, each in a different office mechanism (self-replicating
meeting, "per my last email" as a threat, standup, PTO, fridge, out-of-office
auto-reply, quick sync, performance review, reply-all thread, ASAP deadline).
Every pair judged against the brief's 5 criteria in order, both orders
considered, margin 1–5. Full record: `TOURNAMENT.md` in the bounty directory.

Final standings: fridge (C6) 9–0, "per my last email" (C2) 8–1, ASAP deadline
(C12) 7–2, self-replicating meeting (C1) 6–3. The fridge line's only close
game was against C2 (margin 1); it beat C12 and C1 by margins 1 and 2. The
standup line (C4) went 0–9 — it had no real turn, only an abstract
punchline — which confirmed the tournament was actually discriminating and
not just rubber-stamping.

Runner-up if a replacement is ever needed: C2, "I wrote 'per my last email'
so politely that HR flagged it as a threat and my manager approved the
request out of fear." (119 chars).

## Determinism

`main.py` holds the line as a constant and writes it verbatim. Two local
runs produced byte-identical `/output/entry.txt` (sha256 recorded in
BUILD-REPORT.md). Nothing is read from the environment, the network, or the
git history, so the grader's two runs will produce the same bytes.

## Referral code

The README's referral link uses `qrg7fvky`, per the standing user decision.
The live account's own referral code, verified via `GET /api/me/referrals`
on 2026-11-25, is `6sknhk5z` — different, and the standing decision is to
use `qrg7fvky` in READMEs anyway.
