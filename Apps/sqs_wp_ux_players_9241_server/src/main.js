import { loadScenario } from './data/content-provider.js';
import { sessionStore } from './state/session-store.js';
import { calculateScore } from './state/scoring.js';
import { renderIntroScreen } from './ui/intro-screen.js';
import { renderLabRunner } from './ui/lab-runner.js';
import { renderResultsScreen } from './ui/results-screen.js';
import { clearChildren, createElement } from './utils/dom.js';
import { STATIC_SCENARIOS, getDefaultStaticScenario } from './data/static-options.js';

const persist = window.persistenceAPI || null;
let currentAttemptId = null;
let attemptStartedAt = null;
let currentChallengeIndex = -1;

const appRoot = document.getElementById('app');
const loadButton = document.getElementById('load-scenario');
const sourceSelect = document.getElementById('content-source');
const themeInput = document.getElementById('theme-input');
const themeLabel = document.querySelector('label[for="theme-input"]');
const staticScenarioSelect = document.getElementById('static-scenario');
const staticScenarioLabel = document.getElementById('static-scenario-label');

let isLoading = false;

initializeStaticOptions();
handleSourceChange();

loadButton?.addEventListener('click', handleScenarioLoad);
sourceSelect?.addEventListener('change', handleSourceChange);
sessionStore.subscribe(render);
render(sessionStore.getState());

async function handleScenarioLoad() {
    if (isLoading) return;
    isLoading = true;
    loadButton.disabled = true;
    showLoadingState(sourceSelect.value);

    try {
        const { scenario, mode } = await loadScenario({
            mode: sourceSelect.value,
            theme: themeInput.value.trim(),
            staticScenarioId: staticScenarioSelect.value
        });
        sessionStore.loadScenario(scenario, mode);

        // ── Persistence: create attempt ──
        if (persist) {
            currentAttemptId = await persist.createAttempt(scenario.id, scenario.title);
            attemptStartedAt = Date.now();
        }
    } catch (error) {
        showErrorState(error.message);
    } finally {
        isLoading = false;
        loadButton.disabled = false;
    }
}

function render(state) {
    if (!state.scenario) {
        showDefaultPlaceholder();
        return;
    }

    if (state.stage === 'intro') {
        renderIntroScreen(appRoot, {
            scenario: state.scenario,
            onStartLabs: () => sessionStore.setStage('labs'),
            onJumpToLab: (labId) => {
                const index = state.scenario.challenges.findIndex(c => c.labId === labId);
                if (index !== -1) {
                    sessionStore.jumpToChallenge(index, labId);
                }
            }
        });
        return;
    }

    if (state.stage === 'labs') {
        // Scroll to top only if challenge changed
        if (currentChallengeIndex !== state.activeChallengeIndex) {
            window.scrollTo({ top: 0, behavior: 'smooth' });
            currentChallengeIndex = state.activeChallengeIndex;
        }

        renderLabRunner(appRoot, {
            scenario: state.scenario,
            state,
            onRecordAnswer: (challengeId, quizId, value) =>
                sessionStore.recordAnswer(challengeId, quizId, value),
            onAdvance: () => sessionStore.advanceChallenge()
        });
        return;
    }

    if (state.stage === 'results') {
        const score = calculateScore(state.scenario, state.answers);
        renderResultsScreen(appRoot, {
            scenario: state.scenario,
            score,
            onReset: () => {
                currentAttemptId = null;
                attemptStartedAt = null;
                sessionStore.reset();
            }
        });

        // ── Persistence: complete attempt ──
        if (persist && currentAttemptId) {
            const enrichedMetadata = buildEnrichedMetadata(state, score);
            const durationMs = attemptStartedAt ? Date.now() - attemptStartedAt : 0;
            persist.completeAttempt(currentAttemptId, {
                score: score.total,
                correctCount: score.correct,
                incorrectCount: score.totalQuestions - score.correct,
                maxScore: 100,
                durationMs,
                metadata: enrichedMetadata
            });
            currentAttemptId = null;
        }
    }
}

function showLoadingState(mode) {
    clearChildren(appRoot);
    const placeholder = createElement('section', { className: 'placeholder' });
    const loader = createElement('div', { className: 'loader' });
    const headingText = mode === 'ollama' ? 'Consulting gpt-oss…' : 'Loading static scenario…';
    const bodyText =
        mode === 'ollama'
            ? 'Talking to the local Ollama instance. This may take a few seconds while the model drafts new labs.'
            : 'Retrieving the curated classroom pack from the JSON bundle.';
    placeholder.append(
        loader,
        createElement('h2', { text: headingText }),
        createElement('p', { text: bodyText })
    );
    appRoot.appendChild(placeholder);
}

function showErrorState(message) {
    clearChildren(appRoot);
    const panel = createElement('section', { className: 'panel' });
    const isOllamaError = sourceSelect?.value === 'ollama';
    const friendlyMessage = isOllamaError
        ? 'The local AI (gpt-oss/Ollama) did not respond. Make sure the model is running or switch to a static scenario.'
        : 'Unable to build the scenario.';
    panel.append(
        createElement('h2', { text: 'Something went wrong' }),
        createElement('p', { text: message || friendlyMessage }),
        createElement('p', {
            className: 'subtitle',
            text: 'You can try again or switch to the static JSON source.'
        })
    );
    appRoot.appendChild(panel);
}

function showDefaultPlaceholder() {
    clearChildren(appRoot);
    const placeholder = createElement('section', { className: 'placeholder' });
    placeholder.append(
        createElement('h2', { text: 'Ready when you are' }),
        createElement('p', { text: 'Pick the content source and load the scenario to begin the classroom experience.' })
    );
    appRoot.appendChild(placeholder);
}

function initializeStaticOptions() {
    if (!staticScenarioSelect) {
        return;
    }
    STATIC_SCENARIOS.forEach((scenario) => {
        const option = document.createElement('option');
        option.value = scenario.id;
        option.textContent = scenario.label;
        staticScenarioSelect.appendChild(option);
    });
    const defaultScenario = getDefaultStaticScenario();
    if (defaultScenario) {
        staticScenarioSelect.value = defaultScenario.id;
    }
}

function handleSourceChange() {
    const isJson = sourceSelect.value === 'json';
    toggleStaticScenarioControl(!isJson);
    toggleThemeControl(isJson);
}

function toggleStaticScenarioControl(hidden) {
    [staticScenarioLabel, staticScenarioSelect].forEach((node) => {
        if (!node) return;
        node.classList.toggle('is-hidden', hidden);
        node.toggleAttribute('aria-hidden', hidden);
        if (node === staticScenarioSelect) {
            node.disabled = hidden;
        }
    });
}

function toggleThemeControl(hidden) {
    [themeLabel, themeInput].forEach((node) => {
        if (!node) return;
        node.classList.toggle('is-hidden', hidden);
        node.toggleAttribute('aria-hidden', hidden);
    });
    if (themeInput) {
        themeInput.disabled = hidden;
    }
}

// ── Persistence: build enriched metadata ────────────────

function buildEnrichedMetadata(state, score) {
    const { scenario, answers, mode } = state;

    // Flat list of every quiz with full context
    const enrichedAnswers = [];
    (scenario.challenges || []).forEach((challenge) => {
        (challenge.quizzes || []).forEach((quiz) => {
            const playerChoice = answers?.[challenge.id]?.[quiz.id];
            enrichedAnswers.push({
                challenge_id: challenge.id,
                challenge_title: challenge.title,
                lab_id: challenge.labId,
                quiz_id: quiz.id,
                question: quiz.question,
                choices: quiz.choices,
                correct_index: quiz.answer,
                player_choice: playerChoice ?? null,
                correct: playerChoice !== undefined && playerChoice === quiz.answer,
                rationale: quiz.rationale || ""
            });
        });
    });

    return {
        scenario_id: scenario.id,
        scenario_title: scenario.title,
        scenario_theme: scenario.theme || "",
        content_source: mode || "json",
        target_lab_id: state.targetLabId || null,
        completion_mode: state.targetLabId ? "SPECIFIC_LAB" : "FULL_RUN",
        total_challenges: scenario.challenges?.length || 0,
        total_quizzes: score.totalQuestions,
        score_percentage: score.total,
        correct_count: score.correct,
        labs: score.labs.map((lab) => ({
            lab_id: lab.labId,
            title: lab.title,
            score: lab.score,
            correct: lab.correct,
            total: lab.total
        })),
        answers: enrichedAnswers
    };
}
