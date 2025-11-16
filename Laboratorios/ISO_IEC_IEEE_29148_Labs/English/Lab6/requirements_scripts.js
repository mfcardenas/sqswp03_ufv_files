// requirements_scripts.js - Interactive Dashboard for Requirements Management

class RequirementsDashboard {
    constructor() {
        this.currentUser = 'admin';
        this.currentSection = 'dashboard';
        this.requirements = [];
        this.changes = [];
        this.selectedRequirement = null;
        this.charts = {};
        this.init();
    }

    init() {
        this.bindEvents();
        this.initializeCharts();
        this.loadDashboardData();
        this.showNotification('Requirements Management System loaded', 'success');
    }

    bindEvents() {
        // Navigation tabs
        document.querySelectorAll('.nav-tab').forEach(tab => {
            tab.addEventListener('click', (e) => this.switchSection(e.target));
        });

        // Dashboard buttons
        document.getElementById('createReqBtn').addEventListener('click', () => this.showCreateRequirementModal());
        document.getElementById('createChangeBtn').addEventListener('click', () => this.showCreateChangeModal());
        document.getElementById('createLinkBtn').addEventListener('click', () => this.showCreateLinkModal());
        document.getElementById('generateReportBtn').addEventListener('click', () => this.generateReports());

        // Filter and search
        document.getElementById('applyFiltersBtn').addEventListener('click', () => this.applyFilters());

        // Modal events
        document.querySelectorAll('.close-modal').forEach(btn => {
            btn.addEventListener('click', () => this.closeModal());
        });

        // Form submissions
        document.getElementById('requirementForm').addEventListener('submit', (e) => this.handleRequirementSubmit(e));
        document.getElementById('changeForm').addEventListener('submit', (e) => this.handleChangeSubmit(e));
        document.getElementById('linkForm').addEventListener('submit', (e) => this.handleLinkSubmit(e));

        // Logout
        document.getElementById('logoutBtn').addEventListener('click', () => this.logout());
    }

    switchSection(targetTab) {
        const sectionId = targetTab.id.replace('Tab', 'Section');

        // Update navigation
        document.querySelectorAll('.nav-tab').forEach(tab => {
            tab.classList.remove('active');
        });
        targetTab.classList.add('active');

        // Update content
        document.querySelectorAll('.content-section').forEach(section => {
            section.classList.remove('active');
        });
        document.getElementById(sectionId).classList.add('active');

        this.currentSection = sectionId.replace('Section', '').toLowerCase();

        // Load section data
        this.loadSectionData();
    }

    loadDashboardData() {
        // Simulate loading dashboard metrics
        this.updateDashboardMetrics();
        this.loadRecentActivity();
    }

    updateDashboardMetrics() {
        // Mock data - in real implementation, this would come from API
        const metrics = {
            totalReqs: 47,
            pendingChanges: 8,
            approvedReqs: 32,
            traceabilityLinks: 156
        };

        document.getElementById('totalReqs').textContent = metrics.totalReqs;
        document.getElementById('pendingChanges').textContent = metrics.pendingChanges;
        document.getElementById('approvedReqs').textContent = metrics.approvedReqs;
        document.getElementById('traceabilityLinks').textContent = metrics.traceabilityLinks;
    }

    loadRecentActivity() {
        const activityFeed = document.getElementById('activityFeed');
        const activities = [
            {
                type: 'create',
                title: 'New requirement created',
                description: 'REQ-047: User Authentication System',
                time: '2 minutes ago',
                icon: 'fas fa-plus'
            },
            {
                type: 'update',
                title: 'Requirement updated',
                description: 'REQ-023: Database Schema',
                time: '15 minutes ago',
                icon: 'fas fa-edit'
            },
            {
                type: 'approve',
                title: 'Change approved',
                description: 'CHG-012: Security Enhancement',
                time: '1 hour ago',
                icon: 'fas fa-check'
            },
            {
                type: 'link',
                title: 'Traceability link created',
                description: 'REQ-015 → REQ-034',
                time: '2 hours ago',
                icon: 'fas fa-link'
            }
        ];

        activityFeed.innerHTML = activities.map(activity => `
            <div class="activity-item">
                <div class="activity-icon">
                    <i class="${activity.icon}"></i>
                </div>
                <div class="activity-content">
                    <div class="title">${activity.title}</div>
                    <div class="description">${activity.description}</div>
                    <div class="meta">${activity.time}</div>
                </div>
            </div>
        `).join('');
    }

    loadSectionData() {
        switch (this.currentSection) {
            case 'requirements':
                this.loadRequirements();
                break;
            case 'changes':
                this.loadChanges();
                break;
            case 'traceability':
                this.loadTraceability();
                break;
            case 'reports':
                this.loadReports();
                break;
        }
    }

    loadRequirements() {
        const container = document.getElementById('requirementsList');

        // Mock requirements data
        const requirements = [
            {
                id: 'REQ-001',
                title: 'User Authentication System',
                type: 'security',
                priority: 'high',
                status: 'approved',
                created_by: 'admin',
                created_date: '2024-01-15'
            },
            {
                id: 'REQ-002',
                title: 'Database Schema Design',
                type: 'technical',
                priority: 'medium',
                status: 'review',
                created_by: 'admin',
                created_date: '2024-01-14'
            },
            {
                id: 'REQ-003',
                title: 'API Documentation',
                type: 'documentation',
                priority: 'low',
                status: 'draft',
                created_by: 'developer',
                created_date: '2024-01-13'
            }
        ];

        container.innerHTML = requirements.map(req => `
            <div class="requirement-item">
                <div class="requirement-info">
                    <div class="requirement-title">${req.title}</div>
                    <div class="requirement-meta">
                        <span><strong>ID:</strong> ${req.id}</span>
                        <span><strong>Type:</strong> ${req.type}</span>
                        <span><strong>Priority:</strong> ${req.priority}</span>
                        <span><strong>Created:</strong> ${req.created_date}</span>
                    </div>
                </div>
                <span class="requirement-status status-${req.status}">${req.status}</span>
                <div class="requirement-actions">
                    <button class="btn-icon btn-view" onclick="dashboard.viewRequirement('${req.id}')">
                        <i class="fas fa-eye"></i>
                    </button>
                    <button class="btn-icon btn-edit" onclick="dashboard.editRequirement('${req.id}')">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button class="btn-icon btn-delete" onclick="dashboard.deleteRequirement('${req.id}')">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            </div>
        `).join('');
    }

    loadChanges() {
        const container = document.getElementById('changesList');

        const changes = [
            {
                id: 'CHG-001',
                title: 'Add Two-Factor Authentication',
                requirement_id: 'REQ-001',
                status: 'pending',
                requested_by: 'security_team',
                created_date: '2024-01-15'
            },
            {
                id: 'CHG-002',
                title: 'Update Database Schema',
                requirement_id: 'REQ-002',
                status: 'approved',
                requested_by: 'admin',
                created_date: '2024-01-14'
            }
        ];

        container.innerHTML = changes.map(change => `
            <div class="change-item">
                <div class="change-header">
                    <div class="change-title">${change.title}</div>
                    <span class="change-status status-${change.status}">${change.status}</span>
                </div>
                <div class="change-meta">
                    <span><strong>ID:</strong> ${change.id}</span>
                    <span><strong>Requirement:</strong> ${change.requirement_id}</span>
                    <span><strong>Requested by:</strong> ${change.requested_by}</span>
                    <span><strong>Created:</strong> ${change.created_date}</span>
                </div>
                <div class="change-actions">
                    ${change.status === 'pending' ? `
                        <button class="btn-success" onclick="dashboard.approveChange('${change.id}')">
                            <i class="fas fa-check"></i> Approve
                        </button>
                        <button class="btn-danger" onclick="dashboard.rejectChange('${change.id}')">
                            <i class="fas fa-times"></i> Reject
                        </button>
                    ` : ''}
                    <button class="btn-secondary" onclick="dashboard.viewChange('${change.id}')">
                        <i class="fas fa-eye"></i> View Details
                    </button>
                </div>
            </div>
        `).join('');
    }

    loadTraceability() {
        const container = document.getElementById('traceabilityContent');

        const traceabilityData = {
            outgoing: [
                { target: 'REQ-005', type: 'implements', description: 'Implementation requirement' },
                { target: 'REQ-008', type: 'verifies', description: 'Test requirement' }
            ],
            incoming: [
                { source: 'REQ-002', type: 'derives', description: 'Derived from business requirement' }
            ]
        };

        container.innerHTML = `
            <div class="traceability-matrix">
                <div class="matrix-section">
                    <h4>Outgoing Links</h4>
                    ${traceabilityData.outgoing.map(link => `
                        <div class="trace-link">
                            <div class="trace-icon">
                                <i class="fas fa-arrow-right"></i>
                            </div>
                            <div class="trace-info">
                                <div class="title">${link.target}</div>
                                <div class="type">${link.type} - ${link.description}</div>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <div class="matrix-section">
                    <h4>Incoming Links</h4>
                    ${traceabilityData.incoming.map(link => `
                        <div class="trace-link">
                            <div class="trace-icon">
                                <i class="fas fa-arrow-left"></i>
                            </div>
                            <div class="trace-info">
                                <div class="title">${link.source}</div>
                                <div class="type">${link.type} - ${link.description}</div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    initializeCharts() {
        // Status Chart
        const statusCtx = document.getElementById('statusChart').getContext('2d');
        this.charts.status = new Chart(statusCtx, {
            type: 'doughnut',
            data: {
                labels: ['Draft', 'Review', 'Approved', 'Implemented'],
                datasets: [{
                    data: [12, 8, 20, 7],
                    backgroundColor: ['#64748b', '#f59e0b', '#10b981', '#06b6d4']
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

        // Changes Chart
        const changesCtx = document.getElementById('changesChart').getContext('2d');
        this.charts.changes = new Chart(changesCtx, {
            type: 'bar',
            data: {
                labels: ['Pending', 'Approved', 'Rejected', 'Implemented'],
                datasets: [{
                    label: 'Change Requests',
                    data: [8, 15, 3, 12],
                    backgroundColor: ['#f59e0b', '#10b981', '#ef4444', '#06b6d4']
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

        // Traceability Chart
        const traceCtx = document.getElementById('traceabilityChart').getContext('2d');
        this.charts.traceability = new Chart(traceCtx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Traceability Links Created',
                    data: [45, 52, 48, 61, 55, 67],
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

    loadReports() {
        // Charts are already initialized, just refresh data if needed
        this.updateChartData();
    }

    updateChartData() {
        // Update charts with latest data
        this.charts.status.update();
        this.charts.changes.update();
        this.charts.traceability.update();
    }

    showCreateRequirementModal() {
        document.getElementById('modalTitle').textContent = 'Create Requirement';
        document.getElementById('requirementForm').reset();
        document.getElementById('requirementModal').classList.add('show');
    }

    showCreateChangeModal() {
        document.getElementById('changeModalTitle').textContent = 'Create Change Request';
        document.getElementById('changeForm').reset();
        document.getElementById('changeModal').classList.add('show');
    }

    showCreateLinkModal() {
        document.getElementById('linkModalTitle').textContent = 'Create Traceability Link';
        document.getElementById('linkForm').reset();
        document.getElementById('linkModal').classList.add('show');
    }

    closeModal() {
        document.querySelectorAll('.modal').forEach(modal => {
            modal.classList.remove('show');
        });
    }

    handleRequirementSubmit(e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const requirementData = Object.fromEntries(formData);

        // Mock API call
        console.log('Creating requirement:', requirementData);
        this.showNotification('Requirement created successfully', 'success');
        this.closeModal();
        this.loadRequirements();
    }

    handleChangeSubmit(e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const changeData = Object.fromEntries(formData);

        console.log('Creating change request:', changeData);
        this.showNotification('Change request created successfully', 'success');
        this.closeModal();
        this.loadChanges();
    }

    handleLinkSubmit(e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const linkData = Object.fromEntries(formData);

        console.log('Creating traceability link:', linkData);
        this.showNotification('Traceability link created successfully', 'success');
        this.closeModal();
        this.loadTraceability();
    }

    viewRequirement(reqId) {
        console.log('Viewing requirement:', reqId);
        this.showNotification(`Viewing requirement ${reqId}`, 'info');
    }

    editRequirement(reqId) {
        console.log('Editing requirement:', reqId);
        this.selectedRequirement = reqId;
        document.getElementById('modalTitle').textContent = 'Edit Requirement';
        // Load existing data into form
        document.getElementById('requirementModal').classList.add('show');
    }

    deleteRequirement(reqId) {
        if (confirm(`Are you sure you want to delete requirement ${reqId}?`)) {
            console.log('Deleting requirement:', reqId);
            this.showNotification('Requirement deleted successfully', 'success');
            this.loadRequirements();
        }
    }

    approveChange(changeId) {
        console.log('Approving change:', changeId);
        this.showNotification('Change approved successfully', 'success');
        this.loadChanges();
    }

    rejectChange(changeId) {
        const reason = prompt('Enter rejection reason:');
        if (reason) {
            console.log('Rejecting change:', changeId, 'Reason:', reason);
            this.showNotification('Change rejected', 'warning');
            this.loadChanges();
        }
    }

    viewChange(changeId) {
        console.log('Viewing change:', changeId);
        this.showNotification(`Viewing change ${changeId}`, 'info');
    }

    applyFilters() {
        const statusFilter = document.getElementById('statusFilter').value;
        const typeFilter = document.getElementById('typeFilter').value;
        const priorityFilter = document.getElementById('priorityFilter').value;
        const searchTerm = document.getElementById('searchInput').value;

        console.log('Applying filters:', { statusFilter, typeFilter, priorityFilter, searchTerm });
        this.showNotification('Filters applied', 'info');
        this.loadRequirements();
    }

    generateReports() {
        console.log('Generating reports...');
        this.showNotification('Reports generated successfully', 'success');
        this.updateChartData();
    }

    logout() {
        if (confirm('Are you sure you want to logout?')) {
            console.log('Logging out...');
            this.showNotification('Logged out successfully', 'info');
            // In real implementation, redirect to login page
        }
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

        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
}

// Initialize dashboard when page loads
document.addEventListener('DOMContentLoaded', () => {
    window.dashboard = new RequirementsDashboard();
});
