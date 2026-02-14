import { getDefaultStaticScenario, getStaticScenarioById } from './static-options.js';

const OLLAMA_URL = 'http://localhost:11434/api/generate';
const MODEL = 'gpt-oss';

/**
 * Loads the scenario definition from the selected source.
 * @param {Object} options
 * @param {'json'|'ollama'} options.mode
 * @param {string} options.theme
 */
export async function loadScenario({ mode, theme, staticScenarioId }) {
    if (mode === 'ollama') {
        try {
            const scenario = await loadFromOllama(theme);
            return { scenario, mode };
        } catch (error) {
            console.warn('Falling back to JSON content. Reason:', error.message);
        }
    }

    const scenario = await loadFromJson(staticScenarioId);
    return { scenario, mode: 'json' };
}

async function loadFromJson(scenarioId) {
    const scenarioMeta = getStaticScenarioById(scenarioId) ?? getDefaultStaticScenario();
    if (!scenarioMeta) {
        throw new Error('No static scenarios are configured.');
    }
    const response = await fetch(scenarioMeta.path, { cache: 'no-store' });
    if (!response.ok) {
        throw new Error('Unable to load static scenario content.');
    }
    return response.json();
}

async function loadFromOllama(theme) {
    const payload = {
        model: MODEL,
        stream: false,
        prompt: buildScenarioPrompt(theme)
    };

    const response = await fetch(OLLAMA_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    if (!response.ok) {
        throw new Error('Ollama endpoint is not reachable.');
    }

    const data = await response.json();
    if (!data?.response) {
        throw new Error('Ollama response is empty.');
    }

    return parseScenarioText(data.response);
}

function buildScenarioPrompt(theme) {
    return `You are an instructional designer. Build a JSON document with the following shape:
{
  "id": "kebab-case identifier",
  "title": "Scenario title",
  "theme": "${theme}",
  "overview": "2 paragraph description",
  "labs": [
    {"id":"lab-a","title":"Discovery Workshop","summary":"...","challengeIds":["challenge-1","challenge-2"]},
    {"id":"lab-b","title":"Interaction Audit","summary":"...","challengeIds":["challenge-3"]},
    {"id":"lab-c","title":"Validation Sprint","summary":"...","challengeIds":["challenge-4","challenge-5"]}
  ],
  "challenges": [
    {
      "id": "challenge-1",
      "title": "...",
      "labId": "lab-a",
      "narrative": "Rich context for students",
      "objectives": ["Learning outcomes"],
      "tasks": [
                {
                    "type":"context",
                    "content":"Ambient text",
                    "instruction":"Optional instruction field",
                    "tip":"Short reminder",
                    "example":"Concrete illustration",
                    "helper":"Extra advice",
                    "checklistTitle":"Optional title for checklist",
                    "checklist":["Step 1","Step 2"],
                    "resources":[
                        "Plain text reminder",
                        {"label":"Link caption","url":"https://example.com","note":"How to use it"}
                    ]
                }
      ],
      "quizzes": [
        {"id":"c1-q1","type":"single-select","question":"?","choices":["..."],"answer":0,"rationale":"why"}
      ],
            "nextStepCue": "Guidance for students before they advance"
    }
  ],
  "scoring": {"perCorrect": 20, "max": 100},
  "resources": ["ISO references or links"],
  "completionMessage": "Wrap-up copy"
}
Rules:
- Provide exactly three labs (lab-a, lab-b, lab-c) and five challenges (challenge-1..5) mapped to those labs as in the shape above.
- Each challenge needs 3-5 objectives, 4-6 tasks, at least 2 quizzes, and a "nextStepCue".
- Every task must include its "type" plus either "content" or "instruction" AND at least one of these supportive fields: "example", "helper", "checklist", "resources".
- When a task uses "resources", each entry must be either plain text guidance or an HTTPS link object ({"label","url","note"}). Do not reference local files or markdown fences.
- Keep scoring {"perCorrect":20,"max":100} and add a short "completionMessage".
Every task must feel supportive so students understand how to act, not just what to deliver.
Return ONLY valid JSON with no extra narration or markdown fences.`;
}

function parseScenarioText(rawText) {
    const trimmed = rawText.trim();
    const jsonPayload = extractJson(trimmed);
    return normalizeScenario(JSON.parse(jsonPayload));
}

function extractJson(text) {
    const fenced = text.match(/```json([\s\S]*?)```/i);
    if (fenced) {
        return fenced[1].trim();
    }
    const altFence = text.match(/```([\s\S]*?)```/);
    if (altFence) {
        return altFence[1].trim();
    }
    return text;
}

function normalizeScenario(scenario) {
    if (!scenario || typeof scenario !== 'object') {
        throw new Error('Generated scenario does not contain a valid object.');
    }

    scenario.labs = Array.isArray(scenario.labs) ? scenario.labs : [];
    scenario.resources = Array.isArray(scenario.resources) ? scenario.resources : [];
    scenario.challenges = Array.isArray(scenario.challenges) ? scenario.challenges : [];

    scenario.challenges.forEach((challenge) => {
        if (!challenge || typeof challenge !== 'object') {
            return;
        }

        challenge.objectives = Array.isArray(challenge.objectives) ? challenge.objectives : [];
        challenge.tasks = Array.isArray(challenge.tasks) ? challenge.tasks : [];
        challenge.quizzes = Array.isArray(challenge.quizzes) ? challenge.quizzes : [];
        challenge.nextStepCue = challenge.nextStepCue || 'Before moving on, align next steps with your team.';

        challenge.tasks.forEach((task) => {
            if (!task || typeof task !== 'object') {
                return;
            }

            if (!task.content && task.instruction) {
                task.content = task.instruction;
            }

            task.checklist = Array.isArray(task.checklist) ? task.checklist : [];
            task.resources = normalizeResources(task.resources);

            const hasSupport = Boolean(
                task.example ||
                task.helper ||
                task.checklist.length ||
                task.resources.length
            );

            if (!hasSupport) {
                task.helper = 'Add concrete examples or metrics so the team knows how to carry out this activity.';
            }
        });
    });

    return scenario;
}

function normalizeResources(resources) {
    if (!Array.isArray(resources)) {
        return [];
    }

    return resources
        .filter(Boolean)
        .map((resource) => {
            if (typeof resource === 'string') {
                return resource.trim();
            }

            if (resource && typeof resource === 'object') {
                const cleaned = { ...resource };
                if (cleaned.url && !/^https?:/i.test(cleaned.url)) {
                    delete cleaned.url;
                }
                return cleaned;
            }

            return null;
        })
        .filter((resource) => resource && (typeof resource === 'string' || resource.url));
}
