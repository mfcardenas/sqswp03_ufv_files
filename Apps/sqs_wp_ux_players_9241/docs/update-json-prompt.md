# Refreshing `iso9241_challenges.json`

This application can run entirely offline using `data/iso9241_challenges.json`. Follow the workflow below to regenerate the content pack when you want new labs or themes.

## 1. Prepare your authoring environment

- Open a tool capable of running prompts against **Ollama gpt-oss**, GPT-4 class models, or any model that can return structured JSON.
- Copy the latest version of `data/iso9241_challenges.json` so you can compare formats.

## 2. Use the structured prompt

Paste the following prompt (replace the theme and context as needed). The model must return **raw JSON only**, matching the schema described in the comments.

```
You are an instructional designer. Return ONLY valid JSON (no markdown fences) with this structure:
{
  "id": "kebab-case identifier",
  "title": "Scenario title",
  "theme": "<Your theme>",
  "overview": "Two paragraphs max",
  "labs": [
    {"id":"lab-a","title":"Lab A · Discovery Workshop","summary":"...","challengeIds":["challenge-1","challenge-2"]},
    {"id":"lab-b","title":"Lab B · Interaction Audit","summary":"...","challengeIds":["challenge-3"]},
    {"id":"lab-c","title":"Lab C · Validation Sprint","summary":"...","challengeIds":["challenge-4","challenge-5"]}
  ],
  "resources": ["ISO references or links"],
  "scoring": {"perCorrect": number, "max": number},
  "completionMessage": "Wrap-up text",
  "challenges": [
    {
      "id": "challenge-1",
      "title": "Student-facing title",
      "labId": "lab-a",
      "narrative": "Immersive context",
      "objectives": ["Learning outcomes"],
      "tasks": [
        {
          "type":"context",
          "content":"Ambient text",
          "instruction":"Optional instruction",
          "tip":"Short reminder",
          "example":"Concrete illustration",
          "helper":"Extra advice",
          "checklistTitle":"Optional heading",
          "checklist":["Step 1","Step 2"],
          "resources":[
            "Plain text reminder",
            {"label":"Link caption","url":"https://example.com","note":"How to use it"}
          ]
        },
        {"type":"action","instruction":"Hands-on step"},
        {"type":"prompt","instruction":"Ask students to consult ISO"},
        {"type":"research","instruction":"Have them ask the instructor or look online"},
        {"type":"deliverable","instruction":"Expected artefact"}
      ],
      "quizzes": [
        {"id":"c1-q1","type":"single-select","question":"?","choices":["..."],"answer":0,"rationale":"Explain the correct choice"}
      ],
      "nextStepCue": "Instruction for students before advancing"
    }
  ]
}
The JSON must include five challenges (two in Lab A, one in Lab B, two in Lab C). Each challenge needs at least two quiz questions. At least two tasks per challenge should include examples, hints, checklists, or resource links so the student clearly sees how to proceed.
```

## 3. Validate before publishing

1. Use an online JSON validator or `jq` to confirm syntax.
2. Ensure `labs[].challengeIds` reference valid `challenges[].id` values.
3. Replace the file at `data/iso9241_challenges.json` and reload the browser.

## 4. Document classroom tweaks

When you customize the content, note the theme, date, and instructor guidance so future sessions understand the intent. A lightweight changelog in `Documentación/` is enough.
