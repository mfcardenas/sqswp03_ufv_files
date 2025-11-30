const STORAGE_KEY = 'iso9241-session-v1';

const defaultState = {
    stage: 'idle', // idle | intro | labs | results
    scenario: null,
    mode: 'json',
    activeChallengeIndex: 0,
    answers: {}, // { challengeId: { quizId: value } }
    completedChallenges: []
};

let state = restoreState();
const subscribers = new Set();

export const sessionStore = {
    getState,
    subscribe,
    loadScenario,
    setStage,
    recordAnswer,
    advanceChallenge,
    reset
};

function getState() {
    return clone(state);
}

function subscribe(listener) {
    subscribers.add(listener);
    return () => subscribers.delete(listener);
}

function loadScenario(scenario, mode) {
    state = {
        ...defaultState,
        stage: 'intro',
        scenario,
        mode,
        activeChallengeIndex: 0
    };
    persistState();
    notify();
}

function setStage(stage) {
    state = { ...state, stage };
    persistState();
    notify();
}

function recordAnswer(challengeId, quizId, value) {
    const existing = state.answers[challengeId] ?? {};
    const updated = {
        ...state.answers,
        [challengeId]: { ...existing, [quizId]: value }
    };
    state = { ...state, answers: updated };
    persistState();
    notify();
}

function advanceChallenge() {
    if (!state.scenario) return;
    const total = state.scenario.challenges.length;
    const nextIndex = Math.min(state.activeChallengeIndex + 1, total);
    const completedSet = new Set(state.completedChallenges);
    const currentChallenge = state.scenario.challenges[state.activeChallengeIndex];
    if (currentChallenge) {
        completedSet.add(currentChallenge.id);
    }

    const nextStage = nextIndex >= total ? 'results' : 'labs';
    state = {
        ...state,
        activeChallengeIndex: nextIndex,
        completedChallenges: Array.from(completedSet),
        stage: nextStage
    };
    persistState();
    notify();
}

function reset() {
    state = { ...defaultState };
    persistState();
    notify();
}

function notify() {
    subscribers.forEach((fn) => fn(getState()));
}

function persistState() {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (error) {
        console.warn('Unable to persist session state', error);
    }
}

function restoreState() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) {
            return { ...defaultState };
        }
        const restored = JSON.parse(raw);
        return { ...defaultState, ...restored };
    } catch (error) {
        console.warn('Unable to restore session state', error);
        return { ...defaultState };
    }
}

function clone(value) {
    if (typeof structuredClone === 'function') {
        return structuredClone(value);
    }
    return JSON.parse(JSON.stringify(value));
}
