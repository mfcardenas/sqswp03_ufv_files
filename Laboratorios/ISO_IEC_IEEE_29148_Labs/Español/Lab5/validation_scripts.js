// validation_scripts.js - Scripts para Dashboard de Validación

class ValidationDashboard {
    constructor() {
        this.validationEngine = null;
        this.currentResults = null;
        this.scoreChart = null;
        this.init();
    }

    init() {
        this.bindEvents();
        this.initializeCharts();
        this.showNotification('Dashboard de Validación inicializado', 'info');
    }

    bindEvents() {
        // Navegación por pestañas
        document.querySelectorAll('.nav-tab').forEach(tab => {
            tab.addEventListener('click', (e) => this.switchTab(e.target));
        });

        // Botones principales
        document.getElementById('loadReqBtn').addEventListener('click', () => this.loadRequirements());
        document.getElementById('validateBtn').addEventListener('click', () => this.runValidation());
        document.getElementById('generateTestsBtn').addEventListener('click', () => this.generateTestCases());
        document.getElementById('runAcceptanceBtn').addEventListener('click', () => this.runAcceptanceTesting());

        // Controles de secciones
        document.getElementById('generateTestCasesBtn').addEventListener('click', () => this.generateTestCases());
        document.getElementById('runAcceptanceTestsBtn').addEventListener('click', () => this.runAcceptanceTesting());
        document.getElementById('checkComplianceBtn').addEventListener('click', () => this.checkCompliance());
        document.getElementById('generateReportBtn').addEventListener('click', () => this.generateReport());

        // Filtros
        document.getElementById('validationFilter').addEventListener('change', (e) => this.filterValidationResults(e.target.value));
    }

    initializeCharts() {
        const ctx = document.getElementById('scoreChart').getContext('2d');
        this.scoreChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Aprobado', 'Fallido'],
                datasets: [{
                    data: [0, 100],
                    backgroundColor: ['#10b981', '#ef4444'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }

    switchTab(targetTab) {
        // Remover clase active de todas las pestañas
        document.querySelectorAll('.nav-tab').forEach(tab => {
            tab.classList.remove('active');
        });

        // Agregar clase active a la pestaña seleccionada
        targetTab.classList.add('active');

        // Ocultar todas las secciones
        document.querySelectorAll('.content-section').forEach(section => {
            section.classList.remove('active');
        });

        // Mostrar sección correspondiente
        const sectionId = targetTab.id.replace('Tab', 'Section');
        document.getElementById(sectionId).classList.add('active');
    }

    async loadRequirements() {
        try {
            this.showNotification('Cargando requisitos...', 'info');

            // Simular carga de requisitos (en implementación real, esto haría una petición)
            const response = await fetch('validation_requirements.json');
            const data = await response.json();

            this.validationEngine = new ValidationEngine();
            const loaded = this.validationEngine.load_requirements(data);

            if (loaded) {
                this.updateOverviewMetrics();
                this.showNotification('Requisitos cargados exitosamente', 'success');
            } else {
                this.showNotification('Error al cargar requisitos', 'error');
            }
        } catch (error) {
            console.error('Error loading requirements:', error);
            this.showNotification('Error al cargar requisitos', 'error');
        }
    }

    async runValidation() {
        if (!this.validationEngine) {
            this.showNotification('Primero carga los requisitos', 'warning');
            return;
        }

        try {
            this.showNotification('Ejecutando validación...', 'info');

            // Ejecutar validación
            this.currentResults = this.validationEngine.validate_requirements();

            // Actualizar UI
            this.updateOverviewMetrics();
            this.updateValidationResults();
            this.updateScoreChart();

            this.showNotification('Validación completada', 'success');
        } catch (error) {
            console.error('Error running validation:', error);
            this.showNotification('Error en validación', 'error');
        }
    }

    async generateTestCases() {
        if (!this.validationEngine) {
            this.showNotification('Primero carga los requisitos', 'warning');
            return;
        }

        try {
            this.showNotification('Generando casos de prueba...', 'info');

            const testCases = this.validationEngine.generate_test_cases();
            this.displayTestCases(testCases);

            this.showNotification(`${testCases.length} casos de prueba generados`, 'success');
        } catch (error) {
            console.error('Error generating test cases:', error);
            this.showNotification('Error generando casos de prueba', 'error');
        }
    }

    async runAcceptanceTesting() {
        if (!this.validationEngine) {
            this.showNotification('Primero carga los requisitos', 'warning');
            return;
        }

        try {
            this.showNotification('Ejecutando testing de aceptación...', 'info');

            const acceptanceResults = this.validationEngine.perform_acceptance_testing();
            this.displayAcceptanceResults(acceptanceResults);

            this.showNotification('Testing de aceptación completado', 'success');
        } catch (error) {
            console.error('Error running acceptance testing:', error);
            this.showNotification('Error en testing de aceptación', 'error');
        }
    }

    async checkCompliance() {
        if (!this.validationEngine) {
            this.showNotification('Primero carga los requisitos', 'warning');
            return;
        }

        try {
            this.showNotification('Verificando cumplimiento...', 'info');

            const complianceResults = this.validationEngine.validate_against_standards();
            this.displayComplianceResults(complianceResults);

            this.showNotification('Verificación de cumplimiento completada', 'success');
        } catch (error) {
            console.error('Error checking compliance:', error);
            this.showNotification('Error verificando cumplimiento', 'error');
        }
    }

    async generateReport() {
        if (!this.currentResults) {
            this.showNotification('Primero ejecuta la validación', 'warning');
            return;
        }

        try {
            this.showNotification('Generando reporte...', 'info');

            const report = this.validationEngine.generate_validation_report();
            this.displayReport(report);

            this.showNotification('Reporte generado', 'success');
        } catch (error) {
            console.error('Error generating report:', error);
            this.showNotification('Error generando reporte', 'error');
        }
    }

    updateOverviewMetrics() {
        if (!this.validationEngine || !this.currentResults) return;

        const results = this.currentResults;
        const totalReqs = results.total_requirements || 0;
        const passedReqs = results.passed_requirements?.length || 0;
        const failedReqs = results.failed_requirements?.length || 0;
        const issuesCount = results.issues?.length || 0;

        document.getElementById('totalReqs').textContent = totalReqs;
        document.getElementById('passedReqs').textContent = passedReqs;
        document.getElementById('failedReqs').textContent = failedReqs;
        document.getElementById('issuesCount').textContent = issuesCount;

        // Actualizar colores de las tarjetas métricas
        this.updateMetricCardColors(passedReqs, failedReqs);
    }

    updateMetricCardColors(passed, failed) {
        const cards = document.querySelectorAll('.metric-card');
        cards.forEach((card, index) => {
            if (index === 1) { // Aprobados
                card.style.borderLeftColor = passed > failed ? '#10b981' : '#ef4444';
            } else if (index === 2) { // Fallidos
                card.style.borderLeftColor = failed > 0 ? '#ef4444' : '#10b981';
            }
        });
    }

    updateScoreChart() {
        if (!this.currentResults) return;

        const passed = this.currentResults.passed_requirements?.length || 0;
        const failed = this.currentResults.failed_requirements?.length || 0;
        const total = passed + failed;

        if (total > 0) {
            const passedPercent = (passed / total) * 100;
            const failedPercent = (failed / total) * 100;

            this.scoreChart.data.datasets[0].data = [passedPercent, failedPercent];
            this.scoreChart.update();
        }
    }

    updateValidationResults() {
        if (!this.currentResults) return;

        const container = document.getElementById('validationResults');
        container.innerHTML = '';

        const validationTypes = this.currentResults.validation_types || {};

        for (const [type, results] of Object.entries(validationTypes)) {
            const section = this.createValidationSection(type, results);
            container.appendChild(section);
        }
    }

    createValidationSection(type, results) {
        const section = document.createElement('div');
        section.className = 'validation-type';

        const score = results.score || 0;
        const scorePercent = Math.round(score);
        const issues = results.issues || [];

        section.innerHTML = `
            <h4>${this.capitalizeFirst(type)}</h4>
            <div class="validation-score">
                <div class="score-bar">
                    <div class="score-fill" style="width: ${scorePercent}%"></div>
                </div>
                <span class="score-value">${scorePercent}/100</span>
            </div>
            ${issues.length > 0 ? `
                <ul class="issues-list">
                    ${issues.slice(0, 5).map(issue =>
                        `<li>${issue.description || issue}</li>`
                    ).join('')}
                </ul>
            ` : '<p>No se encontraron problemas</p>'}
        `;

        return section;
    }

    displayTestCases(testCases) {
        const container = document.getElementById('testCasesContent');
        container.innerHTML = '';

        if (testCases.length === 0) {
            container.innerHTML = '<div class="loading">No se generaron casos de prueba</div>';
            return;
        }

        testCases.forEach(testCase => {
            const testElement = this.createTestCaseElement(testCase);
            container.appendChild(testElement);
        });
    }

    createTestCaseElement(testCase) {
        const element = document.createElement('div');
        element.className = 'test-case';

        const steps = testCase.test_steps || [];
        const acceptanceCriteria = testCase.acceptance_criteria || [];

        element.innerHTML = `
            <h5>${testCase.title || testCase.id}</h5>
            <div class="test-case-meta">
                <span><strong>ID:</strong> ${testCase.id}</span>
                <span><strong>Prioridad:</strong> ${testCase.priority || 'N/A'}</span>
                <span><strong>Automatizado:</strong> ${testCase.automated ? 'Sí' : 'No'}</span>
            </div>
            ${testCase.description ? `<p><strong>Descripción:</strong> ${testCase.description}</p>` : ''}
            ${steps.length > 0 ? `
                <div class="test-case-steps">
                    <strong>Pasos:</strong>
                    <ol>
                        ${steps.map(step => `<li>${step}</li>`).join('')}
                    </ol>
                </div>
            ` : ''}
            ${acceptanceCriteria.length > 0 ? `
                <div class="test-case-steps">
                    <strong>Criterios de Aceptación:</strong>
                    <ul>
                        ${acceptanceCriteria.map(criterion => `<li>${criterion}</li>`).join('')}
                    </ul>
                </div>
            ` : ''}
        `;

        return element;
    }

    displayAcceptanceResults(results) {
        // Actualizar métricas
        document.getElementById('acceptanceStatus').textContent = results.acceptance_status || 'N/A';
        document.getElementById('acceptancePassRate').textContent = `${Math.round((results.passed_tests / results.executed_tests) * 100) || 0}%`;
        document.getElementById('acceptanceCoverage').textContent = `${results.coverage_metrics?.requirement_coverage || 0}%`;

        // Mostrar resultados detallados
        const container = document.getElementById('acceptanceDetails');
        container.innerHTML = '';

        if (!results.test_results || results.test_results.length === 0) {
            container.innerHTML = '<div class="loading">No hay resultados de pruebas</div>';
            return;
        }

        results.test_results.forEach(result => {
            const resultElement = this.createTestResultElement(result);
            container.appendChild(resultElement);
        });
    }

    createTestResultElement(result) {
        const element = document.createElement('div');
        element.className = `test-result ${result.status}`;

        element.innerHTML = `
            <div>
                <strong>${result.test_case_id}</strong>
                <span class="test-status ${result.status}">${result.status}</span>
            </div>
            <div>
                <small>${result.notes || 'Sin notas'}</small>
            </div>
        `;

        return element;
    }

    displayComplianceResults(results) {
        document.getElementById('complianceScore').textContent = Math.round(results.overall_compliance) || 0;

        const container = document.getElementById('complianceDetails');
        container.innerHTML = '';

        const sections = results.sections_compliance || {};

        for (const [section, sectionResults] of Object.entries(sections)) {
            const sectionElement = this.createComplianceSection(section, sectionResults);
            container.appendChild(sectionElement);
        }
    }

    createComplianceSection(sectionName, results) {
        const element = document.createElement('div');
        element.className = 'compliance-section';

        const score = results.score || 0;
        const issues = results.issues || [];

        element.innerHTML = `
            <h5>${this.capitalizeFirst(sectionName)}</h5>
            <div class="validation-score">
                <div class="score-bar">
                    <div class="score-fill" style="width: ${score}%"></div>
                </div>
                <span class="score-value">${Math.round(score)}/100</span>
            </div>
            ${issues.length > 0 ? `
                <ul class="issues-list">
                    ${issues.map(issue => `<li>${issue.description || issue}</li>`).join('')}
                </ul>
            ` : '<p>Cumple con los estándares</p>'}
        `;

        return element;
    }

    displayReport(report) {
        const container = document.querySelector('.report-content');
        container.textContent = report;
    }

    filterValidationResults(filter) {
        const sections = document.querySelectorAll('.validation-type');

        sections.forEach(section => {
            if (filter === 'all' || section.querySelector('h4').textContent.toLowerCase().includes(filter)) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        });
    }

    showNotification(message, type = 'info') {
        const notification = document.getElementById('notification');
        const iconMap = {
            'info': 'fa-info-circle',
            'success': 'fa-check-circle',
            'warning': 'fa-exclamation-triangle',
            'error': 'fa-times-circle'
        };

        notification.innerHTML = `
            <i class="fas ${iconMap[type] || 'fa-info-circle'}"></i>
            <span id="notificationText">${message}</span>
        `;

        notification.style.display = 'flex';

        // Ocultar automáticamente después de 3 segundos
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }

    capitalizeFirst(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
}

// Clase ValidationEngine simplificada para el navegador
class ValidationEngine {
    constructor() {
        this.requirements = [];
        this.validation_results = {};
        this.test_cases = [];
    }

    load_requirements(data) {
        try {
            this.requirements = data.requirements || [];
            console.log(`Requisitos cargados: ${this.requirements.length}`);
            return true;
        } catch (error) {
            console.error('Error loading requirements:', error);
            return false;
        }
    }

    validate_requirements() {
        // Simulación de validación
        const results = {
            total_requirements: this.requirements.length,
            passed_requirements: [],
            failed_requirements: [],
            issues: [],
            validation_types: {
                completeness: { score: 85, issues: [] },
                consistency: { score: 90, issues: [] },
                feasibility: { score: 75, issues: [] },
                testability: { score: 80, issues: [] },
                standards_compliance: { score: 88, issues: [] }
            }
        };

        // Simular validación básica
        this.requirements.forEach((req, index) => {
            if (Math.random() > 0.7) {
                results.failed_requirements.push({ id: req.id, issues: ['Problema simulado'] });
            } else {
                results.passed_requirements.push(req.id);
            }
        });

        results.overall_score = 82;
        this.validation_results = results;
        return results;
    }

    generate_test_cases() {
        const testCases = [];

        this.requirements.forEach(req => {
            testCases.push({
                id: `TC_${req.id}`,
                title: `Probar ${req.id}: ${req.text.substring(0, 50)}...`,
                description: `Verificar que ${req.text}`,
                priority: req.priority || 'medium',
                test_steps: [
                    'Configurar entorno de prueba',
                    `Ejecutar ${req.text}`,
                    'Verificar resultado esperado'
                ],
                expected_result: req.acceptance_criteria?.[0] || 'Comportamiento correcto',
                acceptance_criteria: req.acceptance_criteria || [],
                automated: Math.random() > 0.5
            });
        });

        this.test_cases = testCases;
        return testCases;
    }

    perform_acceptance_testing() {
        const results = {
            session_id: 'test-session',
            timestamp: new Date().toISOString(),
            total_test_cases: this.test_cases.length,
            executed_tests: this.test_cases.length,
            passed_tests: 0,
            failed_tests: 0,
            blocked_tests: 0,
            test_results: [],
            acceptance_status: 'pending',
            coverage_metrics: {
                requirement_coverage: 95.5,
                code_coverage: 87.3,
                functional_coverage: 92.1
            }
        };

        this.test_cases.forEach(testCase => {
            const status = Math.random() > 0.8 ? 'failed' : 'passed';
            if (status === 'passed') results.passed_tests++;
            else results.failed_tests++;

            results.test_results.push({
                test_case_id: testCase.id,
                status: status,
                execution_time: Math.random() * 5,
                notes: status === 'passed' ? 'Prueba aprobada' : 'Error simulado'
            });
        });

        results.acceptance_status = results.passed_tests > results.failed_tests ? 'accepted' : 'rejected';
        return results;
    }

    validate_against_standards() {
        return {
            standard: 'ISO/IEC/IEEE 29148:2018',
            validation_date: new Date().toISOString(),
            overall_compliance: 87,
            sections_compliance: {
                structure: { score: 90, issues: [] },
                content: { score: 85, issues: [] },
                attributes: { score: 88, issues: [] },
                traceability: { score: 86, issues: [] }
            },
            issues: [],
            recommendations: [
                'Seguir estructura estándar ISO/IEC/IEEE 29148',
                'Incluir atributos obligatorios',
                'Establecer trazabilidad clara'
            ]
        };
    }

    generate_validation_report() {
        return `# Reporte de Validación de Requisitos
Generado: ${new Date().toLocaleString()}

## Resumen Ejecutivo
- **Total de Requisitos**: ${this.requirements.length}
- **Puntuación General**: ${this.validation_results.overall_score || 0}/100
- **Requisitos Aprobados**: ${this.validation_results.passed_requirements?.length || 0}
- **Problemas Encontrados**: ${this.validation_results.issues?.length || 0}

## Recomendaciones
1. Revisar requisitos fallidos
2. Mejorar criterios de aceptación
3. Verificar consistencia terminológica
4. Asegurar testeabilidad de requisitos

---
*Reporte generado automáticamente por Validation Dashboard*`;
    }
}

// Inicializar dashboard cuando se carga la página
document.addEventListener('DOMContentLoaded', () => {
    window.validationDashboard = new ValidationDashboard();
});
