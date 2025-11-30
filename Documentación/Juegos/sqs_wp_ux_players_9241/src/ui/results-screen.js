import { clearChildren, createElement } from '../utils/dom.js';

export function renderResultsScreen(root, { scenario, score, onReset }) {
    clearChildren(root);

    const panel = createElement('section', { className: 'panel' });
    panel.append(
        createElement('h2', { text: 'Lab summary' }),
        createElement('p', {
            text: scenario.completionMessage || 'Review the insights and decide the next classroom action.'
        }),
        createElement('div', {
            className: 'badge',
            text: `Score: ${score.total}%`
        }),
        createElement('p', {
            className: 'subtitle',
            text: `${score.correct} of ${score.totalQuestions} checkpoints validated.`
        })
    );

    const resultsGrid = createElement('div', { className: 'results-grid' });
    score.labs.forEach((lab) => {
        const card = createElement('article', { className: 'result-card' });
        card.append(
            createElement('h3', { text: lab.title }),
            createElement('p', {
                text: lab.total ? `${lab.score}% (${lab.correct}/${lab.total})` : 'No checkpoints in this lab.'
            })
        );
        resultsGrid.appendChild(card);
    });
    panel.appendChild(resultsGrid);

    const resources = createElement('ul', { className: 'task-list' });
    (scenario.resources || []).forEach((resource) => {
        const item = createElement('li', { className: 'task-item' });
        item.append(createElement('p', { text: resource }));
        resources.appendChild(item);
    });
    if (scenario.resources?.length) {
        panel.append(createElement('h3', { text: 'Recommended follow-up' }), resources);
    }

    const restartBtn = createElement('button', {
        className: 'primary',
        text: 'Reset session'
    });
    restartBtn.addEventListener('click', onReset);
    panel.appendChild(restartBtn);

    root.appendChild(panel);
}
