---
name: grill-me-with-docs
description: >-
  Challenges plans and implementation choices against CONTEXT.md, implementatietoelichtingen,
  and code; sharpens domain terminology and updates docs inline. Use proactively at the start
  of non-trivial work—plans, design, architecture, refactors, new features, stelselgroep or
  beleidsregel changes, VERA modeling, ambiguous requirements, warning/error behavior, or
  when terminology or project boundaries are unclear. Also when user mentions grill, plan,
  design, domain, interpretatie, or implementatiekeuze.
---

<what-to-do>

**Wanneer starten:** aan het begin van elke taak die domein, ontwerp of gedrag raakt—niet pas na implementatie. Bij twijfel: start met één verhelderende vraag in plaats van meteen code te schrijven.

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing.

If a question can be answered by exploring the codebase, explore the codebase instead.

</what-to-do>

<supporting-info>

## Domain awareness

During codebase exploration, also look for existing documentation. In this repo, start with:

- `CONTEXT.md` — gedeelde domeintaal en projectgrenzen
- `README.md`, `docs/introductie/opzet.md` — opzet, criterium-id's, lookup-tabellen
- `docs/implementatietoelichtingen/` — welke beleidsboekregels wel/niet geïmplementeerd zijn en waarom
- `docs/voor-ontwikkelaars/` — ontwikkelaarsafspraken
- `AGENTS.md` — agent-instructies en conventies
- https://wetten.overheid.nl/BWBR0003237/2026-01-01 — wettekst als leidende bron bij domeinlogica

### File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

This repo uses `docs/implementatietoelichtingen/` for domain implementation decisions instead of (or alongside) ADRs. Prefer updating implementatietoelichtingen when a decision affects beleidsregel-interpretatie or implementatiestatus.

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives.

Create files lazily — only when you have something to write. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up — capture them as they happen. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

Don't couple `CONTEXT.md` to implementation details. Only include terms that are meaningful to domain experts.

### Update implementatietoelichtingen when relevant

When a grilling session resolves how a beleidsboekregel should be interpreted or whether it is (fully) implementeerbaar, offer to update the relevant page in `docs/implementatietoelichtingen/`. Include bronverwijzing (beleidsboek/wettekst) and quote where possible.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).

</supporting-info>
