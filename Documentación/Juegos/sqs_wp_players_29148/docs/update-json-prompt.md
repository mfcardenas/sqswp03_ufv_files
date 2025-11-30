# Updating static ISO 29148 scenarios

The UI expects every scenario JSON to follow this schema:

```jsonc
{
  "id": "kebab-case",
  "title": "Scenario title",
  "theme": "Short tagline",
  "overview": "Paragraphs",
  "labs": [
    {"id":"lab-a","title":"...","summary":"...","challengeIds":["challenge-1","challenge-2"]},
    {"id":"lab-b",...},
    {"id":"lab-c",...}
  ],
  "challenges": [
    {
      "id": "challenge-1",
      "title": "...",
      "labId": "lab-a",
      "narrative": "Context",
      "objectives": ["..."],
      "tasks": [
        {
          "type": "context|action|prompt|research|deliverable",
          "content" or "instruction": "...",
          "example/helper/checklist/resources": "Provide at least one support element"
        }
      ],
      "quizzes": [
        {
          "id": "c1-q1",
          "type": "single-select",
          "question": "...",
          "choices": ["A","B","C","D"],
          "answer": 0,
          "rationale": "..."
        }
      ],
      "nextStepCue": "Transition text"
    }
  ],
  "resources": ["General references"],
  "scoring": {"perCorrect": 20, "max": 100},
  "completionMessage": "Wrap-up"
}
```

## Prompt snippet for Ollama

When you want the dynamic mode to output new data, use this snippet as part of your prompt:

```
You are an ISO/IEC/IEEE 29148 facilitator. Produce JSON with:
- labs: lab-a (Elicitation Studio), lab-b (Specification Workshop), lab-c (Validation Sprint)
- exactly five challenges (challenge-1..challenge-5) mapped to those labs
- each challenge has 3-5 objectives, 4-6 tasks, ≥2 multiple-choice quizzes, and "nextStepCue"
- every task must include helper material (example, helper, checklist, or resources)
- resources must be plain text or HTTPS links (no local paths)
- scoring stays {"perCorrect":20,"max":100}
Return only valid JSON, no markdown fences.
```

## Tips

- Keep tasks actionable: reference the templates in `docs/templates/` so the resource viewer can open them.
- Quizzes should reinforce ISO 29148 concepts (stakeholder needs, requirement quality, traceability, validation).
- Double-check arrays: empty arrays are allowed but never omit the property.
