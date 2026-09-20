# End-to-end fictional example

> All organizations, people, products, dates, and results below are fictional.

## Scenario

A small education studio wants to launch a weekend workshop. Information is scattered across a meeting, a survey, public competitor pages, and a chat with the instructor.

## 1. Log: capture real inputs

The system records:

- the meeting note and date;
- 28 survey responses with the response window;
- three public competitor pages and access dates;
- the instructor's unconfirmed capacity estimate;
- missing data: historical attendance and refund rate.

The summary does not convert “the instructor thinks 30 seats are fine” into a confirmed capacity.

## 2. Route: give each object one job

```text
20_Evidence/Meetings/Workshop kickoff.md
20_Evidence/Research/Survey summary.md
30_Research/Weekend workshop comparison.md
10_Projects/Weekend workshop.md
50_Knowledge/Event launch validation.md
```

The project document is the only active source of current status. Evidence files preserve original context. The knowledge note receives only cross-project learning after validation.

## 3. Orient: form and challenge a judgment

Initial judgment:

> A beginner workshop on Saturday afternoon is likely to attract at least 20 paid participants.

Adversarial review:

| Type | Finding | Effect |
|---|---|---|
| Failure path | Survey interest may not convert at the proposed price | Add a paid reservation test |
| User counterexample | Parents interested in the topic may be unavailable on Saturday | Test two time windows |
| Data gap | No historical no-show or refund baseline | Do not buy supplies for 30 seats yet |

Updated judgment: supported only as a demand hypothesis, not as a launch forecast.

## 4. Operate: convert judgment into work

| Task | Next actor | Acceptance evidence |
|---|---|---|
| Draft two landing-page variants | AI | Both include price, time, audience, and refund terms |
| Choose the final promise | Human | One approved claim with no unsupported outcome guarantee |
| Run a 48-hour paid reservation test | Human | Reservation count and source breakdown |
| Confirm room capacity | Collaborator | Written venue confirmation |
| Wait for results | Waiting | Wake after 48 hours or 20 reservations |

## 5. Validate: close only with evidence

After 48 hours:

- 12 paid reservations;
- 7 chose Sunday, 5 chose Saturday;
- venue confirmed 24 seats;
- two refund questions exposed unclear terms.

The task is marked `partial`, not `done`: the demand test ran, but the launch threshold was not met.

## 6. Preserve: write back reusable learning

The project document is updated with the result. The long-term knowledge note receives one bounded rule:

> For a new paid event, stated interest is a discovery signal. Use a small paid reservation test before committing full capacity, and test time-slot constraints separately from topic interest.

Source reliability is B because the result is first-hand but limited to one small event. Conclusion confidence is C until repeated in another context.

## What this example demonstrates

- Evidence, project state, and reusable knowledge have different homes.
- AI can prepare analysis and drafts without upgrading assumptions to facts.
- Counterexamples change the experiment instead of merely adding a risk list.
- Completion follows acceptance evidence.
- Reuse preserves a bounded judgment, not the entire project diary.
