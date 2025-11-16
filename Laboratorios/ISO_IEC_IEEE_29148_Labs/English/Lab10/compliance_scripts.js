// Requirements Compliance & Audit Dashboard Scripts

class ComplianceDashboard {
    constructor() {
        this.complianceRules = [];
        this.auditLogs = [];
        this.reports = [];
        this.alerts = [];
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
        this.loadComplianceRules();
        this.loadAuditLogs();
        this.loadReports();
        this.loadAlerts();
        this.loadTemplates();
        this.updateMetrics();
    }

    setupEventListeners() {
        // Form submissions
        document.getElementById('rule-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.addComplianceRule();
        });

        document.getElementById('report-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.generateReport();
        });

        // Set current date for date pickers
        const today = new Date().toISOString().split('T')[0];
        const lastMonth = new Date();
        lastMonth.setMonth(lastMonth.getMonth() - 1);
        const lastMonthStr = lastMonth.toISOString().split('T')[0];

        document.getElementById('date-from').value = lastMonthStr;
        document.getElementById('date-to').value = today;
        document.getElementById('report-date-from').value = lastMonthStr;
        document.getElementById('report-date-to').value = today;

        // Modal controls
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeAllModals();
            }
        });
    }

    initializeCharts() {
        // Compliance Trend Chart
        const complianceCtx = document.getElementById('complianceChart').getContext('2d');
        this.charts.compliance = new Chart(complianceCtx, {
            type: 'line',
            data: {
                labels: this.getLast30Days(),
                datasets: [{
                    label: 'Compliance Score (%)',
                    data: this.generateRandomTrendData(30, 70, 95),
                    borderColor: '#3b82f6',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    tooltip: {
                        mode: 'index',
                        intersect: false,
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        min: 60,
                        max: 100,
                        title: {
                            display: true,
                            text: 'Compliance Score (%)'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Date'
                        }
                    }
                }
            }
        });

        // Audit Activity Chart
        const auditCtx = document.getElementById('auditChart').getContext('2d');
        this.charts.audit = new Chart(auditCtx, {
            type: 'bar',
            data: {
                labels: ['Create', 'Update', 'Delete', 'View', 'Export'],
                datasets: [{
                    label: 'Audit Activity Count',
                    data: [65, 78, 12, 98, 32],
                    backgroundColor: [
                        'rgba(59, 130, 246, 0.7)',
                        'rgba(16, 185, 129, 0.7)',
                        'rgba(239, 68, 68, 0.7)',
                        'rgba(245, 158, 11, 0.7)',
                        'rgba(14, 165, 233, 0.7)'
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false,
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Count'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Action Type'
                        }
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

        // Add random audit logs every 5-10 seconds
        setInterval(() => {
            if (Math.random() > 0.7) {
                this.addRandomAuditLog();
                this.renderAuditLogs();
            }
        }, 7000);

        // Add random alerts every 20-30 seconds
        setInterval(() => {
            if (Math.random() > 0.8) {
                this.addRandomAlert();
                this.renderAlerts();
            }
        }, 25000);
    }

    // Data Management
    loadComplianceRules() {
        // Simulate loading compliance rules from API
        this.complianceRules = [
            { id: 'CR-001', standard: 'iso29148', description: 'Requirements must have unique identifiers', status: 'compliant', severity: 'high', lastCheck: '2025-09-05 14:30:00' },
            { id: 'CR-002', standard: 'iso29148', description: 'Requirements must be atomic', status: 'non-compliant', severity: 'critical', lastCheck: '2025-09-05 14:30:00' },
            { id: 'CR-003', standard: 'iso29148', description: 'Requirements must be verifiable', status: 'compliant', severity: 'high', lastCheck: '2025-09-05 14:30:00' },
            { id: 'CR-004', standard: 'gdpr', description: 'Data privacy requirements must be defined', status: 'pending', severity: 'critical', lastCheck: '2025-09-05 14:30:00' },
            { id: 'CR-005', standard: 'sox', description: 'Audit trail must be maintained', status: 'compliant', severity: 'critical', lastCheck: '2025-09-05 14:30:00' },
            { id: 'CR-006', standard: 'iso27001', description: 'Security requirements must be specified', status: 'compliant', severity: 'high', lastCheck: '2025-09-05 14:30:00' },
            { id: 'CR-007', standard: 'iso29148', description: 'Requirements must be traceable', status: 'non-compliant', severity: 'medium', lastCheck: '2025-09-05 14:30:00' },
            { id: 'CR-008', standard: 'gdpr', description: 'Data retention periods must be specified', status: 'pending', severity: 'medium', lastCheck: '2025-09-05 14:30:00' }
        ];
        this.renderComplianceRules();
    }

    loadAuditLogs() {
        // Simulate loading audit logs from API
        const currentDate = new Date();
        this.auditLogs = [
            { timestamp: new Date(currentDate - 2 * 60000).toLocaleString(), user: 'admin', action: 'Create', objectType: 'Requirement', objectId: 'REQ-123', details: 'Created new requirement "User Authentication"' },
            { timestamp: new Date(currentDate - 5 * 60000).toLocaleString(), user: 'analyst', action: 'Update', objectType: 'Requirement', objectId: 'REQ-120', details: 'Updated requirement description' },
            { timestamp: new Date(currentDate - 15 * 60000).toLocaleString(), user: 'manager', action: 'View', objectType: 'Compliance Report', objectId: 'RPT-456', details: 'Viewed ISO 29148 compliance report' },
            { timestamp: new Date(currentDate - 30 * 60000).toLocaleString(), user: 'reviewer', action: 'Update', objectType: 'Compliance Rule', objectId: 'CR-002', details: 'Updated rule severity to Critical' },
            { timestamp: new Date(currentDate - 60 * 60000).toLocaleString(), user: 'admin', action: 'Delete', objectType: 'Requirement', objectId: 'REQ-119', details: 'Deleted obsolete requirement' },
            { timestamp: new Date(currentDate - 120 * 60000).toLocaleString(), user: 'analyst', action: 'Export', objectType: 'Audit Log', objectId: 'AUD-789', details: 'Exported audit log for the past month' }
        ];
        this.renderAuditLogs();
    }

    loadReports() {
        // Simulate loading reports from API
        this.reports = [
            { id: 'RPT-001', standard: 'iso29148', type: 'compliance-summary', date: '2025-09-01 09:15:00', status: 'Completed' },
            { id: 'RPT-002', standard: 'gdpr', type: 'detailed-compliance', date: '2025-08-15 14:30:00', status: 'Completed' },
            { id: 'RPT-003', standard: 'sox', type: 'non-compliance', date: '2025-08-10 11:45:00', status: 'Completed' },
            { id: 'RPT-004', standard: 'iso27001', type: 'audit-trail', date: '2025-08-05 16:20:00', status: 'Completed' }
        ];
        this.renderReports();
    }

    loadAlerts() {
        // Simulate loading alerts from API
        const currentDate = new Date();
        this.alerts = [
            { message: 'Non-compliance detected: Requirements must be atomic', severity: 'critical', timestamp: new Date(currentDate - 15 * 60000).toLocaleString() },
            { message: 'New compliance rule added: Data retention periods', severity: 'medium', timestamp: new Date(currentDate - 45 * 60000).toLocaleString() },
            { message: 'Requirements without unique identifiers detected', severity: 'high', timestamp: new Date(currentDate - 120 * 60000).toLocaleString() },
            { message: 'Automated compliance check completed successfully', severity: 'low', timestamp: new Date(currentDate - 360 * 60000).toLocaleString() }
        ];
        this.renderAlerts();
    }

    loadTemplates() {
        // Load report templates
        const templates = [
            { id: 1, title: 'Compliance Summary', standard: 'iso29148', description: 'Overview of compliance status for all requirements' },
            { id: 2, title: 'Detailed Compliance', standard: 'gdpr', description: 'Detailed analysis of compliance with specific focus on data privacy' },
            { id: 3, title: 'Non-Compliance Report', standard: 'sox', description: 'List of all non-compliant items with remediation suggestions' },
            { id: 4, title: 'Audit Trail Report', standard: 'iso27001', description: 'Comprehensive audit log with security focus' }
        ];

        const container = document.getElementById('templates-grid');
        container.innerHTML = '';

        templates.forEach(template => {
            const card = document.createElement('div');
            card.className = 'template-card';
            card.setAttribute('data-id', template.id);
            card.innerHTML = `
                <div class="template-header">
                    <div class="template-title">${template.title}</div>
                    <div class="template-standard">${this.formatStandard(template.standard)}</div>
                </div>
                <div class="template-description">${template.description}</div>
                <button class="btn-secondary" onclick="dashboard.useTemplate(${template.id})">Use Template</button>
            `;
            container.appendChild(card);
        });
    }

    // Rendering Methods
    renderComplianceRules() {
        const container = document.getElementById('compliance-rules');
        container.innerHTML = '';

        this.complianceRules.forEach(rule => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${rule.id}</td>
                <td>${this.formatStandard(rule.standard)}</td>
                <td>${rule.description}</td>
                <td><span class="status-badge status-${rule.status}">${this.formatStatus(rule.status)}</span></td>
                <td>${rule.severity.charAt(0).toUpperCase() + rule.severity.slice(1)}</td>
                <td>${rule.lastCheck}</td>
                <td>
                    <button class="btn-secondary" onclick="dashboard.checkComplianceRule('${rule.id}')">Check</button>
                    <button class="btn-secondary" onclick="dashboard.editComplianceRule('${rule.id}')">Edit</button>
                </td>
            `;
            container.appendChild(row);
        });
    }

    renderAuditLogs() {
        const container = document.getElementById('audit-log');
        container.innerHTML = '';

        this.auditLogs.forEach(log => {
            const entry = document.createElement('div');
            entry.className = 'log-entry';
            entry.innerHTML = `
                <div class="log-entry-metadata">
                    <div>${log.timestamp}</div>
                    <div>User: ${log.user}</div>
                </div>
                <div class="log-entry-content">
                    <div class="log-entry-action">${log.action} ${log.objectType} (${log.objectId})</div>
                    <div class="log-entry-details">${log.details}</div>
                </div>
            `;
            container.appendChild(entry);
        });
    }

    renderReports() {
        const container = document.getElementById('reports-list');
        container.innerHTML = '';

        this.reports.forEach(report => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${report.id}</td>
                <td>${this.formatStandard(report.standard)}</td>
                <td>${this.formatReportType(report.type)}</td>
                <td>${report.date}</td>
                <td>${report.status}</td>
                <td>
                    <button class="btn-secondary" onclick="dashboard.viewReport('${report.id}')">View</button>
                    <button class="btn-secondary" onclick="dashboard.downloadReport('${report.id}')">Download</button>
                </td>
            `;
            container.appendChild(row);
        });
    }

    renderAlerts() {
        const container = document.getElementById('alerts-list');
        container.innerHTML = '';

        this.alerts.forEach(alert => {
            const item = document.createElement('div');
            item.className = `alert-item alert-${alert.severity}`;
            item.innerHTML = `
                <div class="alert-message">${alert.message}</div>
                <div class="alert-time">${alert.timestamp}</div>
            `;
            container.appendChild(item);
        });
    }

    // Action Methods
    addComplianceRule() {
        const standard = document.getElementById('rule-standard').value;
        const description = document.getElementById('rule-description').value;
        const severity = document.getElementById('rule-severity').value;
        const validation = document.getElementById('rule-validation').value;

        const newRule = {
            id: `CR-${String(this.complianceRules.length + 1).padStart(3, '0')}`,
            standard,
            description,
            status: 'pending',
            severity,
            lastCheck: new Date().toLocaleString(),
            validation
        };

        this.complianceRules.push(newRule);
        this.renderComplianceRules();
        this.updateMetrics();
        this.closeModal('rule-modal');
        document.getElementById('rule-form').reset();

        this.showNotification('Compliance rule added successfully!', 'success');
        
        // Add audit log for this action
        this.addAuditLog('Create', 'Compliance Rule', newRule.id, `Added new compliance rule: ${description}`);
    }

    generateReport() {
        const standard = document.getElementById('report-standard').value;
        const type = document.getElementById('report-type').value;
        const dateFrom = document.getElementById('report-date-from').value;
        const dateTo = document.getElementById('report-date-to').value;
        const format = document.getElementById('report-format-select').value;

        const newReport = {
            id: `RPT-${String(this.reports.length + 1).padStart(3, '0')}`,
            standard,
            type,
            date: new Date().toLocaleString(),
            status: 'Generating',
            format
        };

        this.reports.unshift(newReport);
        this.renderReports();
        this.closeModal('report-modal');
        document.getElementById('report-form').reset();

        this.showNotification('Report generation started. This may take a few moments.', 'info');

        // Simulate report generation
        setTimeout(() => {
            newReport.status = 'Completed';
            this.renderReports();
            this.updateMetrics();
            this.showNotification(`Report ${newReport.id} has been generated successfully!`, 'success');
            
            // Add audit log for this action
            this.addAuditLog('Create', 'Regulatory Report', newReport.id, `Generated ${this.formatReportType(type)} report for ${this.formatStandard(standard)}`);
        }, 3000);
    }

    runCompliance() {
        this.showNotification('Running compliance check on all rules...', 'info');

        // Simulate compliance check
        setTimeout(() => {
            // Update some rules randomly
            this.complianceRules.forEach(rule => {
                if (Math.random() > 0.7) {
                    rule.status = ['compliant', 'non-compliant', 'pending'][Math.floor(Math.random() * 3)];
                    rule.lastCheck = new Date().toLocaleString();
                }
            });

            this.renderComplianceRules();
            this.updateMetrics();
            this.showNotification('Compliance check completed!', 'success');
            
            // Add audit log for this action
            this.addAuditLog('Update', 'Compliance Check', 'CHK-' + Date.now(), 'Ran compliance check on all rules');
        }, 2000);
    }

    checkComplianceRule(ruleId) {
        const rule = this.complianceRules.find(r => r.id === ruleId);
        if (!rule) return;

        this.showNotification(`Checking compliance rule: ${rule.description}`, 'info');

        // Simulate rule check
        setTimeout(() => {
            rule.status = ['compliant', 'non-compliant'][Math.floor(Math.random() * 2)];
            rule.lastCheck = new Date().toLocaleString();
            this.renderComplianceRules();
            this.updateMetrics();
            this.showNotification(`Compliance check completed for rule ${rule.id}!`, 'success');
            
            // Add audit log for this action
            this.addAuditLog('Update', 'Compliance Rule', rule.id, `Checked compliance for rule: ${rule.description}`);
        }, 1500);
    }

    editComplianceRule(ruleId) {
        const rule = this.complianceRules.find(r => r.id === ruleId);
        if (!rule) return;

        // In a real app, you would populate and open an edit modal
        this.showNotification(`Editing rule ${rule.id} would open a modal here`, 'info');
    }

    viewReport(reportId) {
        const report = this.reports.find(r => r.id === reportId);
        if (!report) return;

        // In a real app, you would open the report in a viewer
        this.showNotification(`Viewing report ${report.id} would open a viewer here`, 'info');
        
        // Add audit log for this action
        this.addAuditLog('View', 'Regulatory Report', report.id, `Viewed ${this.formatReportType(report.type)} report`);
    }

    downloadReport(reportId) {
        const report = this.reports.find(r => r.id === reportId);
        if (!report) return;

        // In a real app, you would download the report
        this.showNotification(`Downloading report ${report.id}...`, 'info');
        
        // Add audit log for this action
        this.addAuditLog('Export', 'Regulatory Report', report.id, `Downloaded ${this.formatReportType(report.type)} report`);
    }

    exportAudit() {
        this.showNotification('Exporting audit log...', 'info');
        
        // Simulate export
        setTimeout(() => {
            this.showNotification('Audit log exported successfully!', 'success');
            
            // Add audit log for this action
            this.addAuditLog('Export', 'Audit Log', 'AUD-' + Date.now(), 'Exported audit log');
        }, 1500);
    }

    refreshAudit() {
        this.showNotification('Refreshing audit log...', 'info');
        
        // Add some random logs
        for (let i = 0; i < 3; i++) {
            this.addRandomAuditLog();
        }
        
        this.renderAuditLogs();
        this.showNotification('Audit log refreshed!', 'success');
    }

    useTemplate(templateId) {
        // In a real app, you would load the template data
        this.showNotification(`Template ${templateId} selected. Opening report generator...`, 'info');
        this.openModal('report-modal');
    }

    saveSettings() {
        this.showNotification('Saving compliance settings...', 'info');
        
        // Simulate saving
        setTimeout(() => {
            this.showNotification('Settings saved successfully!', 'success');
            
            // Add audit log for this action
            this.addAuditLog('Update', 'Compliance Settings', 'SET-' + Date.now(), 'Updated compliance settings');
        }, 1500);
    }

    filterCompliance() {
        // In a real app, you would filter the compliance rules
        this.showNotification('Filtering compliance rules...', 'info');
        
        // For demo, just refresh the view
        this.renderComplianceRules();
    }

    filterAudit() {
        // In a real app, you would filter the audit logs
        this.showNotification('Filtering audit logs...', 'info');
        
        // For demo, just refresh the view
        this.renderAuditLogs();
    }

    // Helper Methods
    addAuditLog(action, objectType, objectId, details) {
        const log = {
            timestamp: new Date().toLocaleString(),
            user: ['admin', 'analyst', 'reviewer', 'manager'][Math.floor(Math.random() * 4)],
            action,
            objectType,
            objectId,
            details
        };
        
        this.auditLogs.unshift(log);
        // Keep only the latest 100 logs
        if (this.auditLogs.length > 100) {
            this.auditLogs = this.auditLogs.slice(0, 100);
        }
        
        this.renderAuditLogs();
        this.updateMetrics();
    }

    addRandomAuditLog() {
        const actions = ['Create', 'Update', 'View', 'Delete', 'Export'];
        const objectTypes = ['Requirement', 'Compliance Rule', 'Regulatory Report', 'Audit Log'];
        const users = ['admin', 'analyst', 'reviewer', 'manager'];
        
        const action = actions[Math.floor(Math.random() * actions.length)];
        const objectType = objectTypes[Math.floor(Math.random() * objectTypes.length)];
        const objectId = objectType.substring(0, 3).toUpperCase() + '-' + Math.floor(Math.random() * 1000);
        const user = users[Math.floor(Math.random() * users.length)];
        
        let details = '';
        switch (action) {
            case 'Create':
                details = `Created new ${objectType.toLowerCase()}`;
                break;
            case 'Update':
                details = `Updated ${objectType.toLowerCase()} information`;
                break;
            case 'View':
                details = `Viewed ${objectType.toLowerCase()} details`;
                break;
            case 'Delete':
                details = `Deleted ${objectType.toLowerCase()}`;
                break;
            case 'Export':
                details = `Exported ${objectType.toLowerCase()} data`;
                break;
        }
        
        const log = {
            timestamp: new Date().toLocaleString(),
            user,
            action,
            objectType,
            objectId,
            details
        };
        
        this.auditLogs.unshift(log);
        // Keep only the latest 100 logs
        if (this.auditLogs.length > 100) {
            this.auditLogs = this.auditLogs.slice(0, 100);
        }
    }

    addRandomAlert() {
        const messages = [
            'Non-compliance detected in requirements structure',
            'New compliance standard published: ISO/IEC/IEEE 29148:2025',
            'Compliance check scheduled for tomorrow at 9:00 AM',
            'Audit log export completed successfully',
            'Requirements without traceability detected'
        ];
        
        const severities = ['critical', 'high', 'medium', 'low'];
        
        const alert = {
            message: messages[Math.floor(Math.random() * messages.length)],
            severity: severities[Math.floor(Math.random() * severities.length)],
            timestamp: new Date().toLocaleString()
        };
        
        this.alerts.unshift(alert);
        // Keep only the latest 10 alerts
        if (this.alerts.length > 10) {
            this.alerts = this.alerts.slice(0, 10);
        }
    }

    updateMetrics() {
        // Calculate compliance score
        const compliantRules = this.complianceRules.filter(rule => rule.status === 'compliant').length;
        const totalRules = this.complianceRules.length;
        const complianceScore = totalRules > 0 ? Math.round((compliantRules / totalRules) * 100) : 0;
        
        // Update metrics
        document.getElementById('compliance-score').textContent = complianceScore + '%';
        document.getElementById('audit-entries').textContent = this.auditLogs.length;
        document.getElementById('violations').textContent = this.complianceRules.filter(rule => rule.status === 'non-compliant').length;
        document.getElementById('reports').textContent = this.reports.length;
    }

    updateCharts() {
        // Update compliance trend chart
        this.charts.compliance.data.datasets[0].data = this.generateRandomTrendData(30, 70, 95);
        this.charts.compliance.update();
        
        // Update audit activity chart
        const actionCounts = {
            'Create': this.auditLogs.filter(log => log.action === 'Create').length,
            'Update': this.auditLogs.filter(log => log.action === 'Update').length,
            'Delete': this.auditLogs.filter(log => log.action === 'Delete').length,
            'View': this.auditLogs.filter(log => log.action === 'View').length,
            'Export': this.auditLogs.filter(log => log.action === 'Export').length
        };
        
        this.charts.audit.data.datasets[0].data = [
            actionCounts['Create'] || Math.floor(Math.random() * 50) + 30,
            actionCounts['Update'] || Math.floor(Math.random() * 50) + 30,
            actionCounts['Delete'] || Math.floor(Math.random() * 20) + 10,
            actionCounts['View'] || Math.floor(Math.random() * 50) + 40,
            actionCounts['Export'] || Math.floor(Math.random() * 30) + 20
        ];
        this.charts.audit.update();
    }

    getLast30Days() {
        const dates = [];
        const today = new Date();
        
        for (let i = 29; i >= 0; i--) {
            const date = new Date();
            date.setDate(today.getDate() - i);
            dates.push(date.toLocaleDateString());
        }
        
        return dates;
    }

    generateRandomTrendData(days, min, max) {
        const data = [];
        let value = Math.floor(Math.random() * (max - min)) + min;
        
        for (let i = 0; i < days; i++) {
            // Add some random variation
            const change = Math.floor(Math.random() * 5) - 2;
            value += change;
            
            // Keep within bounds
            value = Math.max(min, Math.min(max, value));
            
            data.push(value);
        }
        
        return data;
    }

    formatStandard(standard) {
        switch (standard) {
            case 'iso29148':
                return 'ISO/IEC/IEEE 29148';
            case 'gdpr':
                return 'GDPR';
            case 'sox':
                return 'SOX';
            case 'iso27001':
                return 'ISO 27001';
            default:
                return standard;
        }
    }

    formatStatus(status) {
        switch (status) {
            case 'compliant':
                return 'Compliant';
            case 'non-compliant':
                return 'Non-Compliant';
            case 'pending':
                return 'Pending Review';
            default:
                return status;
        }
    }

    formatReportType(type) {
        switch (type) {
            case 'compliance-summary':
                return 'Compliance Summary';
            case 'detailed-compliance':
                return 'Detailed Compliance';
            case 'non-compliance':
                return 'Non-Compliance Report';
            case 'audit-trail':
                return 'Audit Trail';
            default:
                return type;
        }
    }

    // Modal Methods
    openModal(modalId) {
        document.getElementById(modalId).style.display = 'block';
    }

    closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }

    closeAllModals() {
        document.querySelectorAll('.modal').forEach(modal => {
            modal.style.display = 'none';
        });
    }

    // Utility Methods
    showNotification(message, type = 'info') {
        // Simple notification system
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : type === 'warning' ? '#f59e0b' : '#3b82f6'};
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

function openRuleModal() {
    dashboard.openModal('rule-modal');
}

function openReportModal() {
    dashboard.openModal('report-modal');
}

function closeModal(modalId) {
    dashboard.closeModal(modalId);
}

function runCompliance() {
    dashboard.runCompliance();
}

function exportAudit() {
    dashboard.exportAudit();
}

function refreshAudit() {
    dashboard.refreshAudit();
}

function filterCompliance() {
    dashboard.filterCompliance();
}

function filterAudit() {
    dashboard.filterAudit();
}

function saveSettings() {
    dashboard.saveSettings();
}

// Initialize dashboard when page loads
let dashboard;
document.addEventListener('DOMContentLoaded', () => {
    dashboard = new ComplianceDashboard();
});
