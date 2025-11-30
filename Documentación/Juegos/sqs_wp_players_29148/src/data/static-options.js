export const STATIC_SCENARIOS = [
    {
        id: 'iso-29148-requirements-rally',
        label: 'ISO 29148 Requirements Rally',
        path: './data/iso29148_requirements_rally.json'
    },
    {
        id: 'iso-29148-supplier-alignment',
        label: 'ISO 29148 Supplier Alignment Sprint',
        path: './data/iso29148_supplier_alignment.json'
    }
];

export function getStaticScenarioById(id) {
    return STATIC_SCENARIOS.find((scenario) => scenario.id === id) ?? null;
}

export function getDefaultStaticScenario() {
    return STATIC_SCENARIOS[0] ?? null;
}
