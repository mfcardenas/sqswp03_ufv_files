import { clearChildren, createElement } from '../utils/dom.js';
import { openLocalResource } from './resource-preview.js';

const TASK_LABELS = {
    context: 'Context',
    action: 'Action',
    prompt: 'Prompt',
    research: 'Research',
    deliverable: 'Deliverable'
};

export function renderLabRunner(root, { scenario, state, onRecordAnswer, onAdvance }) {
    clearChildren(root);

    const { activeChallengeIndex } = state;
    const challenge = scenario.challenges[activeChallengeIndex];

    if (!challenge) {
        root.appendChild(
            createElement('section', {
                className: 'panel',
                text: 'No more challenges available. Review the summary to continue.'
            })
        );
        return;
    }

    const panel = createElement('section', { className: 'panel' });
    const meta = createElement('div', { className: 'challenge-meta' });
    meta.append(
        createElement('span', {
            className: 'badge',
            text: `Lab: ${challenge.labId.toUpperCase()}`
        }),
        createElement('span', { text: `Challenge ${activeChallengeIndex + 1} of ${scenario.challenges.length}` })
    );

    panel.append(
        meta,
        createElement('h2', { text: challenge.title }),
        createElement('p', { text: challenge.narrative })
    );

    const objectivesList = createElement('ul', { className: 'task-list' });
    challenge.objectives.forEach((objective) => {
        const item = createElement('li', { className: 'task-item' });
        item.append(
            createElement('strong', { text: 'Objective' }),
            createElement('p', { text: objective })
        );
        objectivesList.appendChild(item);
    });

    panel.append(
        createElement('h3', { text: 'Objectives' }),
        objectivesList,
        createElement('h3', { text: 'Activities' })
    );

    const taskList = createElement('ol', { className: 'task-list' });
    challenge.tasks.forEach((task) => {
        const item = createElement('li', { className: 'task-item' });
        item.append(
            createElement('strong', { text: TASK_LABELS[task.type] ?? 'Task' }),
            createElement('p', { text: task.instruction || task.content })
        );
        if (task.tip) {
            item.append(
                createElement('p', {
                    className: 'subtitle',
                    text: task.tip
                })
            );
        }

        if (task.example) {
            item.append(
                createElement('p', {
                    className: 'task-example',
                    text: `Example · ${task.example}`
                })
            );
        }

        if (task.helper) {
            item.append(
                createElement('p', {
                    className: 'task-helper',
                    text: `Hint · ${task.helper}`
                })
            );
        }

        if (Array.isArray(task.checklist) && task.checklist.length) {
            const details = createElement('details', { className: 'task-checklist' });
            details.append(
                createElement('summary', {
                    text: task.checklistTitle || 'Suggested steps'
                })
            );
            const list = createElement('ul');
            task.checklist.forEach((step) => {
                list.appendChild(createElement('li', { text: step }));
            });
            details.appendChild(list);
            item.appendChild(details);
        }

        if (Array.isArray(task.resources) && task.resources.length) {
            item.append(
                createElement('p', {
                    className: 'task-meta-heading',
                    text: 'Helpful references'
                })
            );
            const resList = createElement('ul', { className: 'task-resources' });
            task.resources.forEach((resource) => {
                const entry = createElement('li');
                if (typeof resource === 'string') {
                    if (isLocalDoc(resource)) {
                        entry.classList.add('task-resource-entry');
                        const label = createElement('span', { text: formatResourceLabel(resource) });
                        const button = createElement('button', {
                            className: 'resource-button',
                            text: 'Open resource'
                        });
                        button.addEventListener('click', () => openLocalResource(resource, formatResourceLabel(resource)));
                        entry.append(label, button);
                    } else {
                        entry.textContent = resource;
                    }
                } else if (resource?.url) {
                    const link = createElement('a', {
                        text: resource.label || resource.url,
                        attrs: {
                            href: resource.url,
                            target: '_blank',
                            rel: 'noopener noreferrer'
                        }
                    });
                    entry.appendChild(link);
                    if (resource.note) {
                        entry.appendChild(document.createTextNode(` – ${resource.note}`));
                    }
                }
                resList.appendChild(entry);
            });
            item.appendChild(resList);
        }
        taskList.appendChild(item);
    });
    panel.appendChild(taskList);

    if (challenge.quizzes?.length) {
        const quizWrapper = createElement('div', { className: 'quiz-block' });
        quizWrapper.appendChild(createElement('h3', { text: 'Checkpoints' }));
        challenge.quizzes.forEach((quiz) => {
            const fieldset = createElement('fieldset');
            const legend = createElement('legend', { text: quiz.question });
            fieldset.appendChild(legend);
            quiz.choices.forEach((choice, index) => {
                const optionId = `${quiz.id}-${index}`;
                const label = createElement('label', { className: 'quiz-option', attrs: { for: optionId } });
                const input = createElement('input', {
                    attrs: {
                        type: quiz.type === 'single-select' ? 'radio' : 'checkbox',
                        name: quiz.id,
                        id: optionId,
                        value: index
                    }
                });
                const savedValue = state.answers?.[challenge.id]?.[quiz.id];
                if (quiz.type === 'single-select' && savedValue === index) {
                    input.checked = true;
                }
                input.addEventListener('change', () => onRecordAnswer(challenge.id, quiz.id, index));
                label.append(input, createElement('span', { text: choice }));
                fieldset.appendChild(label);
            });
            quizWrapper.appendChild(fieldset);
        });
        panel.appendChild(quizWrapper);
    }

    const footer = createElement('div', { className: 'challenge-block' });
    footer.append(
        createElement('p', {
            className: 'subtitle',
            text: challenge.nextStepCue
        }),
        createElement('button', {
            className: 'primary',
            text: activeChallengeIndex === scenario.challenges.length - 1 ? 'Show final results' : 'Continue to next challenge'
        })
    );

    footer.querySelector('button').addEventListener('click', onAdvance);
    panel.appendChild(footer);

    root.appendChild(panel);
}

function isLocalDoc(resource) {
    return typeof resource === 'string' && resource.startsWith('./docs/');
}

function formatResourceLabel(path) {
    if (typeof path !== 'string') {
        return 'Resource';
    }
    const file = path.split('/').pop() || 'Resource';
    return file.replace(/[-_]/g, ' ');
}
