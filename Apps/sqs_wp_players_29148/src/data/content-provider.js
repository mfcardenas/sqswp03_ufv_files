import { getDefaultStaticScenario, getStaticScenarioById, STATIC_SCENARIOS } from './static-options.js';

const OLLAMA_URL = 'http://localhost:11434/api/generate';
const MODEL = 'gpt-oss';

/**
 * Loads the scenario definition from the selected source.
 * @param {Object} options
 * @param {'json'|'ollama'} options.mode
 * @param {string} options.theme
 * @param {string} options.staticScenarioId
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
    const staticLabels = STATIC_SCENARIOS.map((scenario) => `- ${scenario.label}`).join('\n');
    return `You are an instructional designer specialized in ISO/IEC/IEEE 29148 requirement engineering workshops. Build a JSON document with the following shape:
{
  "id": "kebab-case identifier",
  "title": "Scenario title",
  "theme": "${theme}",
  "overview": "2 paragraph description",
  "labs": [
    {"id":"lab-a","title":"Stakeholder Discovery Studio","summary":"Discovery focus","challengeIds":["challenge-1","challenge-2"]},
    {"id":"lab-b","title":"Specification Architecture Workshop","summary":"Specification focus","challengeIds":["challenge-3","challenge-4"]},
    {"id":"lab-c","title":"Validation & Traceability Sprint","summary":"Verification/validation focus","challengeIds":["challenge-5"]}
  ],
  "challenges": [
    {
      "id": "challenge-1",
      "title": "...",
      "labId": "lab-a",
      "narrative": "Explain the ISO 29148 context",
      "objectives": ["Learning outcomes"],
      "tasks": [
        {
          "type":"context",
          "content":"Ambient text or instructions",
          "instruction":"Optional instruction field",
          "tip":"Short reminder",
          "example":"Concrete illustration",
          "helper":"Extra advice",
          "checklistTitle":"Optional checklist title",
          "checklist":["Step 1","Step 2"],
          "resources":[
            "Plain text reminder",
            {"label":"Link caption","url":"https://example.com","note":"How to use it"},
            "./docs/templates/<existing-markdown>.md"
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
- Keep the three labs above. Always map challenge-1..5 to lab-a..c like the template shows.
- Every challenge must reflect ISO 29148 clauses 5-11 (needs, analysis, specification, verification/validation).
- Each challenge needs 3-5 objectives, 4-6 tasks, at least 2 quizzes, and a "nextStepCue".
- Every task must include its "type" plus either "content" or "instruction" AND at least one supportive field ("example", "helper", "checklist", or "resources").
- When a task uses "resources", each entry must be plain text guidance, an HTTPS link object, or reference one of the local markdown templates mentioned earlier.
- Keep scoring {"perCorrect":20,"max":100} and add a concise "completionMessage".
- Return ONLY valid JSON with no markdown fences.
Reference scenarios already available offline:\n${staticLabels}`;
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
        challenge.nextStepCue = challenge.nextStepCue || 'Align the decision log before moving to the next clause.';

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
                task.helper = 'Add tangible acceptance data or ISO clause references so the activity guides requirement quality.';
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
