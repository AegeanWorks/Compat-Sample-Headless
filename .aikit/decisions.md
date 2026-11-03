# Decisions

Why this project is built the way it is, oldest first. One entry per decision that changes a
contract, a dependency, a data format or the architecture; IDs are consecutive and never reused.

<!-- Entry format:
### ADR-NNN: <decision in one line>
- **Date**: YYYY-MM-DD
- **Status**: Accepted
- **Context**: <what forced the decision>
- **Decision**: <what was decided>
- **Consequences**: <what follows, including what it costs>
-->

### ADR-001: Adopt canonical seeded-replay scaffold for headless compat proof
- **Date**: 2026-11-03
- **Status**: Accepted
- **Context**: Audit of wave0 + 2 commits found demo.py ignoring --seed and compat.json missing seed/bench/evidence blocks plus .aikit/bench-*.json and evidence.json, diverging from scripts/project_compat.py scaffold; verify passed only because absent sections are skipped.
- **Decision**: Add --seed N determinism with SEED line to demo.py, add seed/bench/evidence to compat.json with replay/bench/evidence files, and pin with a seeded-replay regression test.
- **Consequences**: Seeded runs are deterministic and the compat proof covers replay identity; demo output gains a SEED line which seeded callers must accept.
