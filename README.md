# ai-journey

A 10-month transition from web developer to applied AI engineer, built in public.

## The goal

In 10 months (Oct 2026 – Jul 2027), become an **Applied AI Engineer** who can design, build, evaluate and ship production LLM systems, and who has the research habits to publish original work (Paper 1 starts as a pilot in Month 1).

By the end I want:
- A portfolio of public, working AI projects, each with a README, tests, evals and a demo
- A solid grasp of how LLMs work, from the API inward to the math
- A regular research habit: reading papers, running small experiments, writing them up
- A public record of the journey: posts, write-ups and open-source code

## Month 1: Foundations (Oct 3 – Nov 1, 2026)

Python for AI, how LLMs work from the API inward, the math I actually need, and my first research habit. About 40 hours a week.

| Week | Theme |
|------|-------|
| 0 | Setup: tools, accounts, logs |
| 1 | Python for AI engineers + `llm-cli` |
| 2 | Inside the API: tokens, sampling, structured outputs |
| 3 | Embeddings, retrieval, tools and evals |
| 4 | Ship it: typed-judge capstone + Paper 1 pilot |

**Deliverables by Nov 1:** four public repos and a Paper 1 one-pager.

## Layout

- `LEARNING.md`: daily log
- `research/log.md`: paper notes
- project folders get added as they're built (`llm-cli`, `token-explorer`, `doc-qa`, `typed-judge`, ...)

## Setup

Python 3.12 with [uv](https://docs.astral.sh/uv/). Secrets live in `.env` (git-ignored).
