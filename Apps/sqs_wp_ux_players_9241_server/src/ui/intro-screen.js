import { clearChildren, createElement } from '../utils/dom.js';

export function renderIntroScreen(root, { scenario, onStartLabs, onJumpToLab }) {
    clearChildren(root);

    const introPanel = createElement('section', { className: 'panel' });
    introPanel.append(
        createElement('div', {
            className: 'badge',
            text: scenario.theme
        }),
        createElement('h2', { text: scenario.title }),
        createElement('p', { text: scenario.overview })
    );

    const labsGrid = createElement('div', { className: 'labs-grid' });
    scenario.labs.forEach((lab) => {
        const card = createElement('article', { className: 'lab-card' });

        const jumpBtn = createElement('button', {
            className: 'secondary',
            text: 'Start this Lab',
            attrs: { style: 'margin-top:auto;width:100%;font-size:0.9rem;padding:0.5rem;' }
        });
        jumpBtn.addEventListener('click', () => onJumpToLab(lab.id));

        card.append(
            createElement('h3', { text: lab.title }),
            createElement('p', { text: lab.summary }),
            createElement('p', {
                className: 'lab-meta',
                text: `${lab.challengeIds.length} Challenges • ${countQuizzes(scenario, lab)} Checkpoints`
            }),
            jumpBtn
        );
        labsGrid.appendChild(card);
    });

    const cta = createElement('button', {
        className: 'primary',
        text: 'Start lab flow'
    });
    cta.addEventListener('click', onStartLabs);

    introPanel.append(
        createElement('h3', { text: 'Workshop structure' }),
        labsGrid,
        createElement('p', {
            className: 'subtitle',
            text: 'Discuss the overview before the first challenge appears to students.'
        }),
        cta
    );

    root.appendChild(introPanel);
}

function countQuizzes(scenario, lab) {
    let count = 0;
    const labChallengeIds = new Set(lab.challengeIds);
    (scenario.challenges || []).forEach((c) => {
        if (labChallengeIds.has(c.id) && c.quizzes) {
            count += c.quizzes.length;
        }
    });
    return count;
}
