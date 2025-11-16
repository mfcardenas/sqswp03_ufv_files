// Requirements Validation & Verification Dashboard JavaScript

class ValidationDashboard {
    constructor() {
        this.charts = {};
        this.currentData = null;
        this.refreshInterval = null;
        this.init();
    }

    init() {
        this.bindEvents();
        this.initializeCharts();
        this.loadInitialData();
        this.startAutoRefresh();
    }

    bindEvents() {
        // Header controls
        document.getElementById('refresh-btn').addEventListener('click', () => this.refreshData());
        document.getElementById('export-btn').addEventListener('click', () => this.exportData());

        // Tabs
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchTab(e.target));
        });

        // Review controls
        document.getElementById('create-review-btn').addEventListener('click', () => this.showCreateReviewModal());
        document.getElementById('view-reviews-btn').addEventListener('click', () => this.showReviewDetailsModal());

        // Modal controls
        document.querySelectorAll('.modal-close').forEach(close => {
            close.addEventListener('click', (e) => this.closeModal(e.target.closest('.modal').id));
        });

        // Form submissions
        document.getElementById('create-review-form').addEventListener('submit', (e) => this.handleCreateReview(e));

        // Click outside modal to close
        window.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal')) {
                this.closeModal(e.target.id);
            }
        });
    }

    initializeCharts() {
        // Quality Dimensions Chart
        const qualityCtx = document.getElementById('qualityChart').getContext('2d');
        this.charts.quality = new Chart(qualityCtx, {
            type: 'radar',
            data: {
                labels: ['Completeness', 'Correctness', 'Consistency', 'Clarity', 'Verifiability', 'Traceability'],
                datasets: [{
                    label: 'Quality Score',
                    data: [0, 0, 0, 0, 0, 0],
                    backgroundColor: 'rgba(37, 99, 235, 0.2)',
                    borderColor: 'rgba(37, 99, 235, 1)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgba(37, 99, 235, 1)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgba(37, 99, 235, 1)'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        beginAtZero: true,
                        max: 100,
                        ticks: {
                            stepSize: 20
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });

        // Trends Chart
        const trendsCtx = document.getElementById('trendsChart').getContext('2d');
        this.charts.trends = new Chart(trendsCtx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Overall Quality Score',
                    data: [],
                    borderColor: 'rgba(16, 185, 129, 1)',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    async loadInitialData() {
        try {
            this.showLoading();
            // In a real implementation, this would fetch data from an API
            // For now, we'll use mock data
            const mockData = await this.getMockData();
            this.updateDashboard(mockData);
        } catch (error) {
            console.error('Error loading data:', error);
            this.showError('Failed to load validation data');
        } finally {
            this.hideLoading();
        }
    }

    async refreshData() {
        await this.loadInitialData();
        this.showNotification('Data refreshed successfully', 'success');
    }

    updateDashboard(data) {
        this.currentData = data;

        // Update metrics
        this.updateMetrics(data);

        // Update charts
        this.updateCharts(data);

        // Update results
        this.updateResults(data);

        // Update verification methods
        this.updateVerificationMethods(data);

        // Update activity feed
        this.updateActivityFeed(data);
    }

    updateMetrics(data) {
        const metrics = data.quality_metrics || {};

        // Overall score
        document.getElementById('overall-score').textContent = `${metrics.overall_score || 0}%`;

        // Total requirements
        document.getElementById('total-requirements').textContent = data.summary?.total || 0;

        // Active reviews (mock data)
        document.getElementById('active-reviews').textContent = Math.floor(Math.random() * 5) + 1;

        // Validation accuracy
        document.getElementById('validation-accuracy').textContent = '95%';
    }

    updateCharts(data) {
        const dimensions = data.quality_metrics?.dimensions || {};

        // Update quality chart
        this.charts.quality.data.datasets[0].data = [
            dimensions.completeness || 0,
            dimensions.correctness || 0,
            dimensions.consistency || 0,
            dimensions.clarity || 0,
            dimensions.verifiability || 0,
            dimensions.traceability || 0
        ];
        this.charts.quality.update();

        // Update trends chart (mock historical data)
        const historicalData = this.generateHistoricalData(data.quality_metrics?.overall_score || 0);
        this.charts.trends.data.labels = historicalData.labels;
        this.charts.trends.data.datasets[0].data = historicalData.data;
        this.charts.trends.update();
    }

    updateResults(data) {
        const resultsContent = document.getElementById('results-content');

        // Summary tab
        const summaryHTML = `
            <div class="results-summary">
                <div class="summary-item">
                    <span class="summary-label">Total Requirements:</span>
                    <span class="summary-value">${data.summary?.total || 0}</span>
                </div>
                <div class="summary-item">
                    <span class="summary-label">Passed:</span>
                    <span class="summary-value status-passed">${data.summary?.passed || 0}</span>
                </div>
                <div class="summary-item">
                    <span class="summary-label">Failed:</span>
                    <span class="summary-value status-failed">${data.summary?.failed || 0}</span>
                </div>
                <div class="summary-item">
                    <span class="summary-label">Warnings:</span>
                    <span class="summary-value status-warning">${data.summary?.warnings || 0}</span>
                </div>
            </div>
        `;

        // Details tab
        const detailsHTML = `
            <div class="results-details">
                ${data.details?.map(req => `
                    <div class="requirement-item ${req.status.toLowerCase()}">
                        <div class="requirement-header">
                            <span class="requirement-id">${req.id}</span>
                            <span class="requirement-status status-${req.status.toLowerCase()}">${req.status}</span>
                        </div>
                        <div class="requirement-scores">
                            ${Object.entries(req.scores || {}).map(([key, value]) =>
                                `<span class="score-item">${key}: ${(value * 100).toFixed(1)}%</span>`
                            ).join('')}
                        </div>
                        ${req.issues?.length ? `
                            <div class="requirement-issues">
                                ${req.issues.map(issue =>
                                    `<div class="issue-item ${issue.type}">${issue.message}</div>`
                                ).join('')}
                            </div>
                        ` : ''}
                    </div>
                `).join('') || '<p>No validation results available</p>'}
            </div>
        `;

        // Issues tab
        const issuesHTML = `
            <div class="results-issues">
                ${data.details?.filter(req => req.issues?.length).map(req => `
                    <div class="issue-group">
                        <h4>${req.id}</h4>
                        ${req.issues.map(issue => `
                            <div class="issue-item ${issue.type}">
                                <span class="issue-type">${issue.type.toUpperCase()}</span>
                                ${issue.message}
                            </div>
                        `).join('')}
                    </div>
                `).join('') || '<p>No issues found</p>'}
            </div>
        `;

        // Store content for tab switching
        this.resultsContent = { summary: summaryHTML, details: detailsHTML, issues: issuesHTML };

        // Show current tab
        const activeTab = document.querySelector('.tab-btn.active').dataset.tab;
        resultsContent.innerHTML = this.resultsContent[activeTab];
    }

    updateVerificationMethods(data) {
        // Mock verification method updates
        const methods = ['analysis', 'demonstration', 'testing', 'inspection'];

        methods.forEach(method => {
            const statusEl = document.getElementById(`${method}-status`);
            const confidenceEl = document.getElementById(`${method}-confidence`);

            // Simulate different statuses
            const confidence = Math.floor(Math.random() * 40) + 60; // 60-100%
            confidenceEl.textContent = `${confidence}%`;

            if (confidence > 80) {
                statusEl.textContent = 'Excellent';
                statusEl.className = 'method-status status-passed';
            } else if (confidence > 60) {
                statusEl.textContent = 'Good';
                statusEl.className = 'method-status status-info';
            } else {
                statusEl.textContent = 'Needs Review';
                statusEl.className = 'method-status status-warning';
            }
        });
    }

    updateActivityFeed(data) {
        const activityFeed = document.getElementById('activity-feed');

        const activities = [
            { time: '2 minutes ago', action: 'Validation completed for REQ-001', type: 'validation' },
            { time: '5 minutes ago', action: 'Review started for REQ-002', type: 'review' },
            { time: '10 minutes ago', action: 'Quality metrics updated', type: 'metrics' },
            { time: '15 minutes ago', action: 'New requirement added: REQ-003', type: 'requirement' },
            { time: '1 hour ago', action: 'Verification methods calibrated', type: 'system' }
        ];

        activityFeed.innerHTML = activities.map(activity => `
            <div class="activity-item ${activity.type}">
                <div class="activity-time">${activity.time}</div>
                <div class="activity-action">${activity.action}</div>
            </div>
        `).join('');
    }

    switchTab(target) {
        // Remove active class from all tabs
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));

        // Add active class to clicked tab
        target.classList.add('active');

        // Update content
        const tabName = target.dataset.tab;
        const resultsContent = document.getElementById('results-content');
        resultsContent.innerHTML = this.resultsContent[tabName];
    }

    showCreateReviewModal() {
        document.getElementById('create-review-modal').style.display = 'block';
    }

    showReviewDetailsModal() {
        // Mock review details
        const reviewDetails = `
            <div class="review-details">
                <div class="review-info">
                    <h4>Review ID: REV-001</h4>
                    <p><strong>Requirement:</strong> REQ-001</p>
                    <p><strong>Type:</strong> Functional</p>
                    <p><strong>Status:</strong> In Progress</p>
                    <p><strong>Reviewers:</strong> john@example.com, jane@example.com</p>
                </div>
                <div class="review-findings">
                    <h4>Findings</h4>
                    <div class="finding-item">
                        <span class="finding-severity medium">Medium</span>
                        <p>Requirement lacks specific performance criteria</p>
                        <small>Submitted by: john@example.com</small>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('review-details-content').innerHTML = reviewDetails;
        document.getElementById('review-details-modal').style.display = 'block';
    }

    async handleCreateReview(e) {
        e.preventDefault();

        const formData = new FormData(e.target);
        const reviewData = {
            requirement_id: formData.get('review-requirement-id'),
            type: formData.get('review-type'),
            reviewers: formData.get('review-reviewers').split(',').map(r => r.trim())
        };

        try {
            // In a real implementation, this would send data to an API
            console.log('Creating review:', reviewData);
            this.showNotification('Review created successfully', 'success');
            this.closeModal('create-review-modal');
            e.target.reset();
        } catch (error) {
            this.showNotification('Failed to create review', 'error');
        }
    }

    closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }

    exportData() {
        if (!this.currentData) {
            this.showNotification('No data to export', 'warning');
            return;
        }

        const dataStr = JSON.stringify(this.currentData, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });

        const link = document.createElement('a');
        link.href = URL.createObjectURL(dataBlob);
        link.download = 'validation_results.json';
        link.click();

        this.showNotification('Data exported successfully', 'success');
    }

    showLoading() {
        document.getElementById('loading-overlay').style.display = 'block';
    }

    hideLoading() {
        document.getElementById('loading-overlay').style.display = 'none';
    }

    showNotification(message, type = 'info') {
        // Simple notification system
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;

        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 20px;
            border-radius: 6px;
            color: white;
            font-weight: 500;
            z-index: 10000;
            animation: slideIn 0.3s ease;
        `;

        // Set background color based on type
        const colors = {
            success: '#10b981',
            error: '#ef4444',
            warning: '#f59e0b',
            info: '#3b82f6'
        };
        notification.style.backgroundColor = colors[type] || colors.info;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => document.body.removeChild(notification), 300);
        }, 3000);
    }

    startAutoRefresh() {
        // Auto-refresh every 5 minutes
        this.refreshInterval = setInterval(() => {
            this.refreshData();
        }, 5 * 60 * 1000);
    }

    generateHistoricalData(currentScore) {
        const labels = [];
        const data = [];

        // Generate last 10 data points
        for (let i = 9; i >= 0; i--) {
            const date = new Date();
            date.setDate(date.getDate() - i);
            labels.push(date.toLocaleDateString());

            // Simulate historical scores with some variation
            const variation = (Math.random() - 0.5) * 10;
            const score = Math.max(0, Math.min(100, currentScore + variation));
            data.push(Math.round(score));
        }

        return { labels, data };
    }

    async getMockData() {
        // Simulate API call delay
        await new Promise(resolve => setTimeout(resolve, 1000));

        return {
            summary: {
                total: 8,
                passed: 6,
                failed: 1,
                warnings: 1
            },
            quality_metrics: {
                overall_score: 82.5,
                dimensions: {
                    completeness: 85,
                    correctness: 88,
                    consistency: 78,
                    clarity: 82,
                    verifiability: 80,
                    traceability: 75
                }
            },
            details: [
                {
                    id: 'REQ-001',
                    status: 'PASSED',
                    scores: { syntax: 0.95, semantics: 0.88, consistency: 0.92 },
                    issues: []
                },
                {
                    id: 'REQ-002',
                    status: 'PASSED',
                    scores: { syntax: 0.98, semantics: 0.91, consistency: 0.85 },
                    issues: []
                },
                {
                    id: 'REQ-003',
                    status: 'WARNING',
                    scores: { syntax: 0.88, semantics: 0.75, consistency: 0.82 },
                    issues: [{ type: 'warning', message: 'Ambiguous terms detected' }]
                },
                {
                    id: 'REQ-004',
                    status: 'FAILED',
                    scores: { syntax: 0.65, semantics: 0.72, consistency: 0.78 },
                    issues: [
                        { type: 'error', message: 'Missing required fields' },
                        { type: 'warning', message: 'Inconsistent terminology' }
                    ]
                }
            ]
        };
    }
}

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.validationDashboard = new ValidationDashboard();
});

// Add notification animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }

    .notification {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .activity-item {
        padding: 12px;
        border-bottom: 1px solid #e2e8f0;
        transition: background-color 0.2s ease;
    }

    .activity-item:hover {
        background-color: #f8fafc;
    }

    .activity-time {
        font-size: 0.8rem;
        color: #64748b;
        margin-bottom: 4px;
    }

    .activity-action {
        font-size: 0.9rem;
        color: #1e293b;
    }

    .results-summary {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 16px;
        margin-bottom: 20px;
    }

    .summary-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px;
        background: #f8fafc;
        border-radius: 6px;
    }

    .summary-label {
        font-weight: 500;
        color: #64748b;
    }

    .summary-value {
        font-weight: 600;
        font-size: 1.2rem;
    }

    .requirement-item {
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 12px;
    }

    .requirement-item.passed {
        border-color: #10b981;
        background: rgba(16, 185, 129, 0.05);
    }

    .requirement-item.failed {
        border-color: #ef4444;
        background: rgba(239, 68, 68, 0.05);
    }

    .requirement-item.warning {
        border-color: #f59e0b;
        background: rgba(245, 158, 11, 0.05);
    }

    .requirement-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }

    .requirement-id {
        font-weight: 600;
        color: #1e293b;
    }

    .requirement-scores {
        display: flex;
        gap: 12px;
        margin-bottom: 8px;
        flex-wrap: wrap;
    }

    .score-item {
        font-size: 0.8rem;
        color: #64748b;
    }

    .requirement-issues {
        margin-top: 8px;
    }

    .issue-item {
        font-size: 0.8rem;
        padding: 4px 8px;
        border-radius: 4px;
        margin-bottom: 4px;
    }

    .issue-item.error {
        background: rgba(239, 68, 68, 0.1);
        color: #ef4444;
    }

    .issue-item.warning {
        background: rgba(245, 158, 11, 0.1);
        color: #f59e0b;
    }

    .issue-item.info {
        background: rgba(59, 130, 246, 0.1);
        color: #3b82f6;
    }
`;
document.head.appendChild(style);
