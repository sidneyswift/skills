# Teach-me explainer

Teach the user a domain just well enough that they can prompt with real vocabulary. Use when the user must direct work in a field they cannot name: color grading, typography, audio mixing, SEO, database tuning. The tell is a vague ask like "make the video look nicer" or "make the page feel more premium".

Example trigger prompt:

> I don't know what color grading is but I need to grade the launch video. Teach me color grading well enough that I understand my unknown unknowns and can prompt you with real vocabulary.

## Output shape

A single self-contained HTML explainer with these sections:

1. **The mental model**: the domain's pipeline as 3 to 5 numbered stages, one line each (e.g. ingest, correct, grade, match). This gives the user a skeleton to hang everything else on.
2. **The vocabulary ladder**: 5 to 8 terms, ordered from foundational to advanced. Each entry has:
   - The term plus a two-word gloss ("Exposure · overall brightness")
   - A plain-language definition including the classic gotcha
   - A ready-made note phrased as a real prompt in quotes: "the interview shots look a half-stop underexposed, bring them up"
3. **A live playground** when the domain allows it: sliders, presets, a before/after comparison on a realistic example. Let the user feel the parameters until they become obvious. Skip this only when interactivity genuinely cannot demonstrate the domain.
4. **What good looks like**: a checklist of 4 to 6 quality criteria phrased as judgments the user can now make themselves ("skin tones stay believable", "blacks are rich but not crushed").
5. **The payoff**: 3 or 4 example prompts the user could not have written an hour ago, each one specific, using the new vocabulary, and directly relevant to their actual task.

## Quality bar

- Anchor every example to the user's real asset or project, not a generic one.
- Each vocabulary entry must include the prompt-quote line. The whole point is converting vocabulary into promptability.
- Definitions include the practical failure mode, not just the meaning (saturation turns skin orange; vibrance protects it).
- Keep it to one sitting. This is a working vocabulary, not a course.
