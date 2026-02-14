import { createElement } from '../utils/dom.js';

const MODAL_ID = 'resource-preview-modal';
const MODAL_CLASS = 'resource-modal';
let markedLoader;
let markedConfigured = false;

function ensureModal() {
    let modal = document.getElementById(MODAL_ID);
    if (modal) {
        return modal;
    }
    modal = createElement('div', { className: `${MODAL_CLASS} hidden`, attrs: { id: MODAL_ID } });
    const dialog = createElement('div', { className: 'resource-modal__dialog' });
    const closeBtn = createElement('button', {
        className: 'resource-modal__close',
        text: '×'
    });
    closeBtn.setAttribute('type', 'button');
    closeBtn.addEventListener('click', () => hideModal());

    const title = createElement('h3', { className: 'resource-modal__title' });
    const body = createElement('div', { className: 'resource-modal__body' });
    dialog.append(closeBtn, title, body);
    modal.appendChild(dialog);
    modal.addEventListener('click', (event) => {
        if (event.target === modal) {
            hideModal();
        }
    });
    document.body.appendChild(modal);
    return modal;
}

function hideModal() {
    const modal = ensureModal();
    modal.classList.add('hidden');
}

function showModalContent({ title, content }) {
    const modal = ensureModal();
    const titleNode = modal.querySelector('.resource-modal__title');
    const bodyNode = modal.querySelector('.resource-modal__body');
    titleNode.textContent = title || 'Resource preview';
    bodyNode.innerHTML = '';
    bodyNode.appendChild(content);
    modal.classList.remove('hidden');
}

export async function openLocalResource(path, displayName) {
    const name = displayName || deriveName(path);
    const placeholder = createElement('div', { className: 'resource-modal__loading', text: 'Loading resource…' });
    showModalContent({ title: name, content: placeholder });
    try {
        const response = await fetch(path);
        if (!response.ok) {
            throw new Error(`Failed to load resource (${response.status})`);
        }
        const text = await response.text();
        const rendered = await renderMarkdown(text);
        showModalContent({ title: name, content: rendered });
    } catch (error) {
        const message = createElement('p', {
            className: 'resource-modal__error',
            text: `Could not load resource. ${error.message}`
        });
        showModalContent({ title: name, content: message });
    }
}

function deriveName(path) {
    if (typeof path !== 'string') {
        return 'Resource';
    }
    const parts = path.split('/');
    return parts[parts.length - 1] || 'Resource';
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        const modal = document.getElementById(MODAL_ID);
        if (modal && !modal.classList.contains('hidden')) {
            hideModal();
        }
    }
});

async function renderMarkdown(text) {
    const module = await loadMarked();
    if (module?.marked) {
        if (!markedConfigured) {
            module.marked.setOptions({
                mangle: false,
                headerIds: false
            });
            markedConfigured = true;
        }
        const container = createElement('div', { className: 'resource-modal__content' });
        container.innerHTML = module.marked.parse(text);
        return container;
    }
    const fallback = createElement('pre', { className: 'resource-modal__content' });
    fallback.textContent = text;
    return fallback;
}

function loadMarked() {
    if (!markedLoader) {
        markedLoader = import('https://cdn.jsdelivr.net/npm/marked@12.0.2/lib/marked.esm.js').catch(() => null);
    }
    return markedLoader;
}
