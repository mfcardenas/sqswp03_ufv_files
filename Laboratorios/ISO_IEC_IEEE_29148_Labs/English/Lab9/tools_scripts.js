// Requirements Tools & Automation Dashboard Scripts

class ToolsDashboard {
    constructor() {
        this.connectors = [];
        this.workflows = [];
        this.apiLogs = [];
        this.syncLogs = [];
        this.charts = {};
        this.initialize();
    }

    initialize() {
        this.loadData();
        this.setupEventListeners();
        this.initializeCharts();
        this.startRealTimeUpdates();
    }

    loadData() {
        // Load initial data from local storage or API
        this.loadConnectors();
        this.loadWorkflows();
        this.loadApiLogs();
        this.loadSyncLogs();
        this.updateMetrics();
    }

    setupEventListeners() {
        // Form submissions
        document.getElementById('connector-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.addConnector();
        });

        document.getElementById('workflow-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.addWorkflow();
        });

        // Modal controls
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeAllModals();
            }
        });
    }

    initializeCharts() {
        // Integration Status Chart
        const integrationCtx = document.getElementById('integrationChart').getContext('2d');
        this.charts.integration = new Chart(integrationCtx, {
            type: 'doughnut',
            data: {
                labels: ['Connected', 'Disconnected', 'Configuring'],
                datasets: [{
                    data: [0, 0, 0],
                    backgroundColor: ['#10b981', '#ef4444', '#f59e0b'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });

        // Automation Performance Chart
        const automationCtx = document.getElementById('automationChart').getContext('2d');
        this.charts.automation = new Chart(automationCtx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Workflow Executions',
                    data: [],
                    borderColor: '#2563eb',
                    backgroundColor: 'rgba(37, 99, 235, 0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    startRealTimeUpdates() {
        // Update metrics every 30 seconds
        setInterval(() => {
            this.updateMetrics();
            this.updateCharts();
        }, 30000);

        // Update sync status every 10 seconds
        setInterval(() => {
            this.updateSyncStatus();
        }, 10000);
    }

    // Data Management
    loadConnectors() {
        // Simulate loading connectors from API
        this.connectors = [
            { id: 1, name: 'Jira', type: 'requirements', status: 'connected', url: 'https://company.atlassian.net' },
            { id: 2, name: 'Confluence', type: 'documentation', status: 'connected', url: 'https://company.atlassian.net' },
            { id: 3, name: 'GitHub', type: 'version-control', status: 'configuring', url: 'https://github.com/company' },
            { id: 4, name: 'TestRail', type: 'testing', status: 'disconnected', url: 'https://company.testrail.com' }
        ];
        this.renderConnectors();
    }

    loadWorkflows() {
        this.workflows = [
            {
                id: 1,
                name: 'Auto Review Assignment',
                trigger: 'requirement-created',
                actions: 'Assign reviewers based on requirement type and priority',
                status: 'active'
            },
            {
                id: 2,
                name: 'Deadline Notifications',
                trigger: 'deadline-approaching',
                actions: 'Send email notifications 3 days before deadline',
                status: 'active'
            }
        ];
        this.renderWorkflows();
    }

    loadApiLogs() {
        this.apiLogs = [
            { timestamp: '2024-01-15 10:30:00', method: 'GET', endpoint: '/api/requirements', status: 200 },
            { timestamp: '2024-01-15 10:29:45', method: 'POST', endpoint: '/api/workflows', status: 201 },
            { timestamp: '2024-01-15 10:29:30', method: 'PUT', endpoint: '/api/connectors/1', status: 200 },
            { timestamp: '2024-01-15 10:29:15', method: 'GET', endpoint: '/api/sync/status', status: 200 }
        ];
        this.renderApiLogs();
    }

    loadSyncLogs() {
        this.syncLogs = [
            { timestamp: '2024-01-15 10:30:00', action: 'Sync completed', status: 'success', records: 150 },
            { timestamp: '2024-01-15 10:25:00', action: 'Sync started', status: 'info', records: 0 },
            { timestamp: '2024-01-15 10:20:00', action: 'Sync completed', status: 'success', records: 145 }
        ];
        this.renderSyncLogs();
    }

    // Rendering Methods
    renderConnectors() {
        const container = document.getElementById('connectors-grid');
        container.innerHTML = '';

        this.connectors.forEach(connector => {
            const card = document.createElement('div');
            card.className = 'connector-card';
            card.innerHTML = `
                <div class="connector-header">
                    <div class="connector-name">${connector.name}</div>
                    <div class="connector-status status-${connector.status}">
                        ${connector.status.charAt(0).toUpperCase() + connector.status.slice(1)}
                    </div>
                </div>
                <div class="connector-details">
                    <p><strong>Type:</strong> ${connector.type.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}</p>
                    <p><strong>URL:</strong> ${connector.url}</p>
                    <div class="connector-actions">
                        <button class="btn-secondary" onclick="dashboard.testConnection(${connector.id})">Test</button>
                        <button class="btn-secondary" onclick="dashboard.configureConnector(${connector.id})">Configure</button>
                    </div>
                </div>
            `;
            container.appendChild(card);
        });
    }

    renderWorkflows() {
        const container = document.getElementById('workflows-container');
        container.innerHTML = '';

        this.workflows.forEach(workflow => {
            const card = document.createElement('div');
            card.className = 'workflow-card';
            card.innerHTML = `
                <div class="workflow-header">
                    <div class="workflow-name">${workflow.name}</div>
                    <div class="workflow-trigger">${workflow.trigger.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}</div>
                </div>
                <div class="workflow-details">
                    <p><strong>Actions:</strong> ${workflow.actions}</p>
                    <p><strong>Status:</strong> ${workflow.status.charAt(0).toUpperCase() + workflow.status.slice(1)}</p>
                    <div class="workflow-actions">
                        <button class="btn-secondary" onclick="dashboard.editWorkflow(${workflow.id})">Edit</button>
                        <button class="btn-secondary" onclick="dashboard.runWorkflow(${workflow.id})">Run</button>
                    </div>
                </div>
            `;
            container.appendChild(card);
        });
    }

    renderApiLogs() {
        const container = document.getElementById('api-logs-list');
        container.innerHTML = '';

        // API Endpoints
        const endpoints = [
            { method: 'GET', path: '/api/requirements', description: 'List requirements' },
            { method: 'POST', path: '/api/requirements', description: 'Create requirement' },
            { method: 'GET', path: '/api/workflows', description: 'List workflows' },
            { method: 'POST', path: '/api/workflows', description: 'Create workflow' },
            { method: 'GET', path: '/api/connectors', description: 'List connectors' },
            { method: 'POST', path: '/api/connectors', description: 'Add connector' }
        ];

        const endpointsContainer = document.getElementById('api-endpoints-list');
        endpointsContainer.innerHTML = '';

        endpoints.forEach(endpoint => {
            const item = document.createElement('div');
            item.className = 'endpoint-item';
            item.innerHTML = `
                <div>
                    <span class="endpoint-method">${endpoint.method}</span>
                    <span class="endpoint-path">${endpoint.path}</span>
                </div>
                <div>${endpoint.description}</div>
            `;
            endpointsContainer.appendChild(item);
        });

        // API Logs
        this.apiLogs.forEach(log => {
            const item = document.createElement('div');
            item.className = 'log-item';
            item.innerHTML = `
                <span class="log-timestamp">${log.timestamp}</span>
                <span class="log-method">${log.method}</span>
                <span class="log-endpoint">${log.endpoint}</span>
                <span class="log-status status-${log.status < 300 ? 'success' : 'error'}">${log.status}</span>
            `;
            container.appendChild(item);
        });
    }

    renderSyncLogs() {
        const container = document.getElementById('sync-logs');
        container.innerHTML = '';

        this.syncLogs.forEach(log => {
            const item = document.createElement('div');
            item.className = 'log-item';
            item.innerHTML = `
                <span class="log-timestamp">${log.timestamp}</span>
                <span class="log-action">${log.action}</span>
                <span class="log-records">${log.records} records</span>
                <span class="log-status status-${log.status}">${log.status}</span>
            `;
            container.appendChild(item);
        });
    }

    // Action Methods
    addConnector() {
        const formData = new FormData(document.getElementById('connector-form'));
        const connector = {
            id: Date.now(),
            name: formData.get('tool-name'),
            type: formData.get('tool-type'),
            url: formData.get('api-url'),
            apiKey: formData.get('api-key'),
            status: 'configuring'
        };

        this.connectors.push(connector);
        this.renderConnectors();
        this.updateMetrics();
        this.closeModal('connector-modal');
        document.getElementById('connector-form').reset();

        this.showNotification('Connector added successfully!', 'success');
    }

    addWorkflow() {
        const formData = new FormData(document.getElementById('workflow-form'));
        const workflow = {
            id: Date.now(),
            name: formData.get('workflow-name'),
            trigger: formData.get('trigger-type'),
            actions: formData.get('actions'),
            status: 'active'
        };

        this.workflows.push(workflow);
        this.renderWorkflows();
        this.updateMetrics();
        this.closeModal('workflow-modal');
        document.getElementById('workflow-form').reset();

        this.showNotification('Workflow created successfully!', 'success');
    }

    testConnection(connectorId) {
        const connector = this.connectors.find(c => c.id === connectorId);
        if (!connector) return;

        // Simulate connection test
        connector.status = 'configuring';
        this.renderConnectors();

        setTimeout(() => {
            connector.status = Math.random() > 0.3 ? 'connected' : 'disconnected';
            this.renderConnectors();
            this.updateMetrics();
            this.showNotification(
                `Connection test ${connector.status === 'connected' ? 'successful' : 'failed'}!`,
                connector.status === 'connected' ? 'success' : 'error'
            );
        }, 2000);
    }

    configureConnector(connectorId) {
        const connector = this.connectors.find(c => c.id === connectorId);
        if (!connector) return;

        // Open configuration modal (simplified)
        alert(`Configuration for ${connector.name} would open here`);
    }

    editWorkflow(workflowId) {
        const workflow = this.workflows.find(w => w.id === workflowId);
        if (!workflow) return;

        // Open edit modal (simplified)
        alert(`Edit workflow ${workflow.name} would open here`);
    }

    runWorkflow(workflowId) {
        const workflow = this.workflows.find(w => w.id === workflowId);
        if (!workflow) return;

        this.showNotification(`Running workflow: ${workflow.name}`, 'info');

        // Simulate workflow execution
        setTimeout(() => {
            this.showNotification(`Workflow ${workflow.name} completed successfully!`, 'success');
        }, 3000);
    }

    triggerSync() {
        document.getElementById('sync-status').textContent = 'Running';
        document.getElementById('sync-progress').style.width = '0%';
        document.getElementById('sync-progress-text').textContent = '0%';

        // Simulate sync process
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 15;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);
                document.getElementById('sync-status').textContent = 'Completed';
                document.getElementById('last-sync-time').textContent = new Date().toLocaleString();
                this.addSyncLog('Sync completed', 'success', Math.floor(Math.random() * 200) + 100);
                this.showNotification('Data synchronization completed!', 'success');
            }

            document.getElementById('sync-progress').style.width = progress + '%';
            document.getElementById('sync-progress-text').textContent = Math.round(progress) + '%';
        }, 500);
    }

    // Update Methods
    updateMetrics() {
        const connectedCount = this.connectors.filter(c => c.status === 'connected').length;
        const activeWorkflows = this.workflows.filter(w => w.status === 'active').length;
        const apiRequests = this.apiLogs.length;
        const syncSuccessRate = 95; // Mock value

        document.getElementById('connected-tools').textContent = connectedCount;
        document.getElementById('active-workflows').textContent = activeWorkflows;
        document.getElementById('api-requests').textContent = apiRequests;
        document.getElementById('sync-rate').textContent = syncSuccessRate + '%';
    }

    updateCharts() {
        // Update integration chart
        const connected = this.connectors.filter(c => c.status === 'connected').length;
        const disconnected = this.connectors.filter(c => c.status === 'disconnected').length;
        const configuring = this.connectors.filter(c => c.status === 'configuring').length;

        this.charts.integration.data.datasets[0].data = [connected, disconnected, configuring];
        this.charts.integration.update();

        // Update automation chart with mock data
        const now = new Date();
        const labels = [];
        const data = [];

        for (let i = 6; i >= 0; i--) {
            const date = new Date(now);
            date.setHours(date.getHours() - i);
            labels.push(date.toLocaleTimeString());
            data.push(Math.floor(Math.random() * 50) + 10);
        }

        this.charts.automation.data.labels = labels;
        this.charts.automation.data.datasets[0].data = data;
        this.charts.automation.update();
    }

    updateSyncStatus() {
        // Mock sync status updates
        const isRunning = Math.random() > 0.8;
        if (isRunning) {
            document.getElementById('sync-status').textContent = 'Running';
        } else {
            document.getElementById('sync-status').textContent = 'Idle';
        }
    }

    addSyncLog(action, status, records) {
        const log = {
            timestamp: new Date().toLocaleString(),
            action,
            status,
            records
        };
        this.syncLogs.unshift(log);
        this.syncLogs = this.syncLogs.slice(0, 10); // Keep only last 10 logs
        this.renderSyncLogs();
    }

    // Modal Methods
    closeAllModals() {
        document.querySelectorAll('.modal').forEach(modal => {
            modal.style.display = 'none';
        });
    }

    closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }

    // Utility Methods
    showNotification(message, type = 'info') {
        // Simple notification (could be enhanced with a proper notification system)
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#2563eb'};
            color: white;
            border-radius: 6px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            z-index: 1001;
            animation: slideIn 0.3s ease;
        `;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }
}

// Global functions for HTML onclick handlers
function showSection(sectionId) {
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('active');
    });
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    document.getElementById(sectionId).classList.add('active');
    event.target.classList.add('active');
}

function openConnectorModal() {
    document.getElementById('connector-modal').style.display = 'block';
}

function openWorkflowModal() {
    document.getElementById('workflow-modal').style.display = 'block';
}

function closeModal(modalId) {
    dashboard.closeModal(modalId);
}

function refreshApiLogs() {
    dashboard.loadApiLogs();
    dashboard.showNotification('API logs refreshed!', 'info');
}

// Initialize dashboard when page loads
let dashboard;
document.addEventListener('DOMContentLoaded', () => {
    dashboard = new ToolsDashboard();
});
