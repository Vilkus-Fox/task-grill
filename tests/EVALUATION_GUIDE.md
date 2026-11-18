# Model behavior evaluation / Испытания поведения моделей

**EN:** This document is a test plan, **not** evidence of a passed model test.

1. Load the intended Skill in a fresh target runtime with the same prerequisites for each comparison.
2. Run the scenarios from [SCENARIO_TESTS.md](../shared/references/SCENARIO_TESTS.md) and retain reproducible evidence.
3. For each case, record `PASS`, `FAIL`, or `NOT RUN`, tool access, model/runtime, input and a short relevant result excerpt.
4. Compare baseline 1.6, candidate 1.6.1 and, where useful, no Skill / upstream Grill Me under comparable conditions.
5. Measure unnecessary questions, false claims of execution, wrong executor assumptions, premature handoff, unauthorized tool launches, context overhead, verification accuracy and owner corrections.
6. In the BFDO/Antigravity pilot, include T50–T57: chosen executor, blind-first brief, prototype approval gate, evidence/SHA continuity and no duplicated issues.

**RU:** Это план проверки, **а не подтверждение успешного тестирования моделей**.

1. Загружайте нужный Skill в новую сессию с одинаковыми исходными условиями.
2. Выполняйте сценарии из [SCENARIO_TESTS.md](../shared/references/SCENARIO_TESTS.md), сохраняйте воспроизводимые доказательства.
3. Для каждого теста фиксируйте `PASS`, `FAIL` или `NOT RUN`, среду, доступ к инструментам, ввод и короткую выдержку результата.
4. Сравнивайте версию 1.6, кандидат 1.6.1 и, где полезно, режим без Skill / исходный Grill Me в сопоставимых условиях.
5. Измеряйте количество лишних вопросов, ложных заявлений о выполнении, ошибочный выбор исполнителя, преждевременный handoff, неразрешённые запуски инструментов, стоимость контекста и количество поправок владельца.
6. В пилоте BFDO/Antigravity особое внимание сценариям T50–T57: исполнитель, независимый бриф, контроль прототипа, передача доказательств/SHA и отсутствие дублей Issue/PR.

**Current status / Текущий статус:** structural checks PASS; live-model behavioral tests NOT RUN.
