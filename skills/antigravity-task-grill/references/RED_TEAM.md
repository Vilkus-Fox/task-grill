# Evidence-Based Red-Team Pass

**Purpose:** challenge the favored product/implementation plan before expensive work begins. For a committed owner, do not repeatedly debate the decision to build; expose actual blockers and offer a testable route to the intended outcome. Red-team is a falsification pass, not an aggressive persona and not a license to invent hypothetical disasters.

## When to run

Run for new architectural decisions, expensive or cross-cutting features, difficult data semantics, new game loops, uncertain platforms/asset pipelines, security/privacy concerns, parallel-agent plans, or when the owner expressly requests red-team. For a verified small reversible fix, skip or compress it to one sentence.

## Test the hypothesis, not the owner

1. State the intended outcome and recommended approach in a falsifiable sentence.
2. Enumerate the few credible assumptions that must hold. Seek counterevidence in the repo, prior decisions, platform documentation, tests or a bounded investigation.
3. Attack the recommended solution just as seriously as alternatives. Look for cases where local component success would not produce the user's actual goal.
4. Consider a failure story from: product usefulness, user journey, data/source truth, authorization, integration, platform performance, game mechanic or content/asset rights, delivery limitations. Only applicable categories count.
5. For each material finding provide: `ID`, assumption, counterexample/failure path, expected impact, likelihood/evidence confidence, severity, cheapest discriminating test, fallback/mitigation, and whether it requires an owner choice.
6. Suggest a cheaper feasible alternative when a failure can be avoided by a smaller vertical slice, reused component, early prototype, or reduced concurrency.
7. Reassess after a material decision or test changes the situation, not after every answer.

## Risk classifications

- `P0`: an unauthorized, unsafe or fundamentally infeasible plan, or a demonstrated conflict that invalidates the end goal. Blocking even if all other aspects look ready.
- `P1`: a credible failure likely to cause major rework, wrong product semantics, critical-path derailment, material budget/performance damage or loss of a must-have capability. Resolve or run a decisive feasibility check before handoff.
- `P2`: low-impact, easily reversible or nonblocking concerns. Document with owner and decision point; do not prolong an interview.

Assess **impact** and **likelihood/evidence confidence** separately. If probabilities are unknown, say "likelihood unknown" rather than fabricating scores. Prioritize high-impact, high-dependency uncertainties. Missing evidence is not proof of failure, but is not proof of safety either.

## Mandatory red-team self-check

- Did I challenge my own favorite plan rather than merely defend it?
- Is each objection linked to observable failure of a stated requirement or goal?
- Did I distinguish testable facts from owner's value judgments?
- Would the proposed question, test or mitigation actually alter a decision?
- Am I inventing cloud/agent capabilities, quotas, timelines or performance without evidence?
- Has a "No" already removed this feature from scope?
- Would one early spike be more useful than more dialogue?

## Red-team stop condition

Stop when no new **material, evidence-supported** failure mode has emerged, or when the next uncertainty requires a bounded external test. Return the top findings and a decision/action. Do not keep adding hypothetical risks to simulate diligence.

## Example

A website compares movie views on flights. The favored UI shows raw counts. Challenge: flight A has 180 connected passengers and flight B has 40; raw counts may give the wrong operational conclusion. Evidence needed: documented event and audience definitions. Cheapest test: inspect data schema and run a small aggregation on permitted fixtures. Owner decision: whether to emphasize absolute reach, normalized engagement, or both, **after** technical feasibility is checked.
