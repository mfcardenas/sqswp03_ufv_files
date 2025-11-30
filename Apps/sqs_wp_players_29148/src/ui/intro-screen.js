import { clearChildren, createElement } from '../utils/dom.js';

export function renderIntroScreen(root, { scenario, onStartLabs }) {
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
        card.append(
            createElement('h3', { text: lab.title }),
            createElement('p', { text: lab.summary }),
            createElement('p', {
                className: 'lab-meta',
                text: `${lab.challengeIds.length} challenges`
            })
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
