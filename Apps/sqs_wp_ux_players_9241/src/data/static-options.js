export const STATIC_SCENARIOS = [
    {
        id: 'iso-9241-usability-quest',
        label: 'ISO 9241 Usability Quest',
        path: './data/iso9241_challenges.json'
    },
    {
        id: 'iso-9241-guided-onboarding',
        label: 'ISO 9241 Guided Onboarding Sprint',
        path: './data/iso9241_guided_onboarding.json'
    },
    {
        id: 'iso-9241-field-validation',
        label: 'ISO 9241 Field Validation Expedition',
        path: './data/iso9241_field_validation.json'
    }
];

export function getStaticScenarioById(id) {
    return STATIC_SCENARIOS.find((scenario) => scenario.id === id) ?? null;
}

export function getDefaultStaticScenario() {
    return STATIC_SCENARIOS[0] ?? null;
}
