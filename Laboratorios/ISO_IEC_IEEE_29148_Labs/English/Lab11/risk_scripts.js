/**
 * Requirements Risk Management Dashboard
 * JavaScript Implementation for ISO/IEC/IEEE 29148 Lab
 */

// Initialize the dashboard when DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the dashboard components
    initializeDashboard();
    
    // Set up event listeners
    setupEventListeners();
    
    // Load initial data
    loadDashboardData();
});

/**
 * Initialize the dashboard components
 */
function initializeDashboard() {
    console.log('Initializing Requirements Risk Management Dashboard...');
    
    // Initialize Risk Distribution Chart
    initializeRiskDistributionChart();
    
    // Initialize Risk Trends Chart
    initializeRiskTrendsChart();
    
    // Initialize Risk Categories Chart
    initializeRiskCategoriesChart();
    
    // Initialize Risk Matrix
    initializeRiskMatrix();
    
    // Initialize Requirements Risk Table
    initializeRequirementsRiskTable();
    
    // Initialize Mitigation Actions Table
    initializeMitigationActionsTable();
    
    console.log('Dashboard initialization complete.');
}

/**
 * Set up event listeners for interactive elements
 */
function setupEventListeners() {
    // Refresh button
    document.getElementById('refresh-btn').addEventListener('click', function() {
        loadDashboardData();
    });
    
    // Project filter change
    document.getElementById('project-filter').addEventListener('change', function() {
        loadDashboardData();
    });
    
    // Time period filter change
    document.getElementById('time-filter').addEventListener('change', function() {
        loadDashboardData();
    });
    
    // Add Mitigation button
    document.getElementById('add-mitigation-btn').addEventListener('click', function() {
        openRiskAssessmentModal();
    });
    
    // Export Actions button
    document.getElementById('export-mitigation-btn').addEventListener('click', function() {
        exportMitigationActions();
    });
    
    // Risk Assessment form submission
    document.getElementById('risk-assessment-form').addEventListener('submit', function(e) {
        e.preventDefault();
        saveRiskAssessment();
    });
    
    // Modal close button
    let closeButtons = document.getElementsByClassName('close-modal');
    for (let i = 0; i < closeButtons.length; i++) {
        closeButtons[i].addEventListener('click', function() {
            closeRiskAssessmentModal();
        });
    }
    
    // Cancel button in modal
    let cancelButtons = document.getElementsByClassName('cancel-button');
    for (let i = 0; i < cancelButtons.length; i++) {
        cancelButtons[i].addEventListener('click', function() {
            closeRiskAssessmentModal();
        });
    }
    
    // Close modal when clicking outside of it
    window.addEventListener('click', function(event) {
        let modal = document.getElementById('risk-assessment-modal');
        if (event.target === modal) {
            closeRiskAssessmentModal();
        }
    });
}

/**
 * Load dashboard data based on current filters
 */
function loadDashboardData() {
    let projectFilter = document.getElementById('project-filter').value;
    let timeFilter = document.getElementById('time-filter').value;
    
    console.log(`Loading dashboard data... (Project: ${projectFilter}, Time: ${timeFilter})`);
    
    // In a real implementation, this would make API calls to fetch data
    // For this lab, we'll use mock data

    // Show loading state
    updateLoadingState(true);
    
    // Simulate API delay
    setTimeout(function() {
        // Load data for each component
        loadRiskOverviewData(projectFilter, timeFilter);
        loadRiskTrendsData(projectFilter, timeFilter);
        loadRequirementsRiskData(projectFilter, timeFilter);
        loadRiskCategoriesData(projectFilter, timeFilter);
        loadMitigationActionsData(projectFilter, timeFilter);
        
        // Update risk matrix
        updateRiskMatrix(projectFilter, timeFilter);
        
        // Hide loading state
        updateLoadingState(false);
        
        console.log('Dashboard data loaded successfully.');
    }, 800);
}

/**
 * Update loading state for dashboard
 */
function updateLoadingState(isLoading) {
    const dashboardCards = document.querySelectorAll('.dashboard-card');
    
    if (isLoading) {
        dashboardCards.forEach(card => {
            card.classList.add('loading');
            
            // Add loading indicator if not already present
            if (!card.querySelector('.loading-indicator')) {
                const loadingIndicator = document.createElement('div');
                loadingIndicator.className = 'loading-indicator';
                loadingIndicator.innerHTML = '<span>Loading...</span>';
                card.appendChild(loadingIndicator);
            }
        });
    } else {
        dashboardCards.forEach(card => {
            card.classList.remove('loading');
            
            // Remove loading indicator
            const loadingIndicator = card.querySelector('.loading-indicator');
            if (loadingIndicator) {
                loadingIndicator.remove();
            }
        });
    }
}

/**
 * Initialize Risk Distribution Chart
 */
function initializeRiskDistributionChart() {
    const ctx = document.getElementById('risk-distribution-chart').getContext('2d');
    
    window.riskDistributionChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['High', 'Medium', 'Low'],
            datasets: [{
                data: [6, 10, 8],
                backgroundColor: [
                    'rgba(231, 76, 60, 0.7)',
                    'rgba(243, 156, 18, 0.7)',
                    'rgba(46, 204, 113, 0.7)'
                ],
                borderColor: [
                    'rgba(231, 76, 60, 1)',
                    'rgba(243, 156, 18, 1)',
                    'rgba(46, 204, 113, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            let value = context.raw;
                            let total = context.dataset.data.reduce((a, b) => a + b, 0);
                            let percentage = Math.round((value / total) * 100);
                            return `${context.label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

/**
 * Initialize Risk Trends Chart
 */
function initializeRiskTrendsChart() {
    const ctx = document.getElementById('risk-trends-chart').getContext('2d');
    
    window.riskTrendsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [
                {
                    label: 'High Risk',
                    data: [8, 10, 9, 8, 7, 6],
                    borderColor: 'rgba(231, 76, 60, 1)',
                    backgroundColor: 'rgba(231, 76, 60, 0.1)',
                    tension: 0.3,
                    fill: true
                },
                {
                    label: 'Medium Risk',
                    data: [6, 7, 8, 9, 10, 10],
                    borderColor: 'rgba(243, 156, 18, 1)',
                    backgroundColor: 'rgba(243, 156, 18, 0.1)',
                    tension: 0.3,
                    fill: true
                },
                {
                    label: 'Low Risk',
                    data: [4, 5, 6, 7, 8, 8],
                    borderColor: 'rgba(46, 204, 113, 1)',
                    backgroundColor: 'rgba(46, 204, 113, 0.1)',
                    tension: 0.3,
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Risks'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Month'
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

/**
 * Initialize Risk Categories Chart
 */
function initializeRiskCategoriesChart() {
    const ctx = document.getElementById('risk-categories-chart').getContext('2d');
    
    window.riskCategoriesChart = new Chart(ctx, {
        type: 'polarArea',
        data: {
            labels: ['Technical', 'Business', 'Operational', 'Compliance'],
            datasets: [{
                data: [8, 6, 4, 3],
                backgroundColor: [
                    'rgba(52, 152, 219, 0.7)',
                    'rgba(155, 89, 182, 0.7)',
                    'rgba(52, 73, 94, 0.7)',
                    'rgba(22, 160, 133, 0.7)'
                ],
                borderColor: [
                    'rgba(52, 152, 219, 1)',
                    'rgba(155, 89, 182, 1)',
                    'rgba(52, 73, 94, 1)',
                    'rgba(22, 160, 133, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            },
            scales: {
                r: {
                    ticks: {
                        display: false
                    }
                }
            }
        }
    });
}

/**
 * Initialize Risk Matrix
 */
function initializeRiskMatrix() {
    const matrix = document.getElementById('risk-matrix');
    
    // Clear existing content
    matrix.innerHTML = '';
    
    // Create 5x5 matrix (impact x probability)
    for (let i = 5; i >= 1; i--) { // Impact (rows, inverted to show 5 at top)
        for (let j = 1; j <= 5; j++) { // Probability (columns)
            const cell = document.createElement('div');
            cell.className = 'matrix-cell';
            
            // Determine risk level
            const riskScore = i * j;
            let riskLevel = '';
            if (riskScore >= 15) {
                riskLevel = 'high-risk';
            } else if (riskScore >= 8) {
                riskLevel = 'medium-risk';
            } else if (riskScore >= 3) {
                riskLevel = 'low-risk';
            } else {
                riskLevel = 'very-low-risk';
            }
            
            cell.classList.add(riskLevel);
            
            // Add label
            cell.textContent = riskScore;
            
            // Add data attributes for filtering
            cell.dataset.impact = i;
            cell.dataset.probability = j;
            cell.dataset.score = riskScore;
            
            // Add to matrix
            matrix.appendChild(cell);
            
            // Add click event to show risks in this cell
            cell.addEventListener('click', function() {
                showRisksForMatrixCell(i, j);
            });
        }
    }
}

/**
 * Show risks for a specific matrix cell
 */
function showRisksForMatrixCell(impact, probability) {
    console.log(`Showing risks with Impact: ${impact}, Probability: ${probability}`);
    
    // In a real implementation, this would filter the requirements table
    // For this lab, we'll just highlight the cell
    
    const cells = document.querySelectorAll('.matrix-cell');
    cells.forEach(cell => {
        cell.classList.remove('selected');
        
        if (parseInt(cell.dataset.impact) === impact && 
            parseInt(cell.dataset.probability) === probability) {
            cell.classList.add('selected');
        }
    });
    
    // Filter the requirements table
    const tableRows = document.querySelectorAll('#requirements-risk-table tbody tr');
    tableRows.forEach(row => {
        row.style.display = 'none';
        
        const rowImpact = parseInt(row.dataset.impact);
        const rowProbability = parseInt(row.dataset.probability);
        
        if (rowImpact === impact && rowProbability === probability) {
            row.style.display = '';
        }
    });
}

/**
 * Initialize Requirements Risk Table
 */
function initializeRequirementsRiskTable() {
    // Table will be populated in loadRequirementsRiskData
}

/**
 * Initialize Mitigation Actions Table
 */
function initializeMitigationActionsTable() {
    // Table will be populated in loadMitigationActionsData
}

/**
 * Load Risk Overview Data
 */
function loadRiskOverviewData(project, timePeriod) {
    // In a real implementation, this would fetch data from an API
    // For this lab, we'll use mock data
    
    let data = {
        total: 24,
        high: 6,
        medium: 10,
        low: 8
    };
    
    // Apply filters
    if (project !== 'all') {
        // Simulate filtered data
        if (project === 'project1') {
            data = { total: 10, high: 3, medium: 4, low: 3 };
        } else if (project === 'project2') {
            data = { total: 8, high: 2, medium: 3, low: 3 };
        } else if (project === 'project3') {
            data = { total: 6, high: 1, medium: 3, low: 2 };
        }
    }
    
    // Update the UI
    document.getElementById('total-risks').textContent = data.total;
    document.getElementById('high-risks').textContent = data.high;
    document.getElementById('medium-risks').textContent = data.medium;
    document.getElementById('low-risks').textContent = data.low;
    
    // Update the chart
    window.riskDistributionChart.data.datasets[0].data = [data.high, data.medium, data.low];
    window.riskDistributionChart.update();
}

/**
 * Load Risk Trends Data
 */
function loadRiskTrendsData(project, timePeriod) {
    // In a real implementation, this would fetch data from an API
    // For this lab, we'll use mock data
    
    let labels = [];
    let highData = [];
    let mediumData = [];
    let lowData = [];
    
    // Set labels based on time period
    if (timePeriod === 'week') {
        labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
        highData = [6, 6, 5, 5, 4, 4, 4];
        mediumData = [10, 10, 9, 9, 10, 10, 9];
        lowData = [8, 8, 9, 9, 8, 8, 8];
    } else if (timePeriod === 'month') {
        labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4'];
        highData = [8, 7, 6, 6];
        mediumData = [9, 9, 10, 10];
        lowData = [7, 8, 8, 8];
    } else if (timePeriod === 'quarter') {
        labels = ['Jan', 'Feb', 'Mar'];
        highData = [10, 8, 6];
        mediumData = [8, 9, 10];
        lowData = [6, 7, 8];
    } else if (timePeriod === 'year') {
        labels = ['Q1', 'Q2', 'Q3', 'Q4'];
        highData = [12, 10, 8, 6];
        mediumData = [8, 9, 10, 10];
        lowData = [5, 6, 7, 8];
    }
    
    // Apply project filter
    if (project !== 'all') {
        // Simulate filtered data
        highData = highData.map(val => Math.max(1, Math.floor(val / 3)));
        mediumData = mediumData.map(val => Math.max(1, Math.floor(val / 3)));
        lowData = lowData.map(val => Math.max(1, Math.floor(val / 3)));
    }
    
    // Update the chart
    window.riskTrendsChart.data.labels = labels;
    window.riskTrendsChart.data.datasets[0].data = highData;
    window.riskTrendsChart.data.datasets[1].data = mediumData;
    window.riskTrendsChart.data.datasets[2].data = lowData;
    window.riskTrendsChart.update();
    
    // Calculate trends
    const highStart = highData[0];
    const highEnd = highData[highData.length - 1];
    const highChange = highEnd - highStart;
    const highPercent = Math.round((highChange / highStart) * 100);
    
    const totalStart = highData[0] + mediumData[0] + lowData[0];
    const totalNew = (highData.length + mediumData.length + lowData.length) - totalStart;
    const newPercent = Math.round((totalNew / totalStart) * 100);
    
    // Update trend summary
    const trendElements = document.querySelectorAll('.trend-metric');
    trendElements[0].querySelector('.trend-value').textContent = `${highPercent}%`;
    trendElements[1].querySelector('.trend-value').textContent = `+${newPercent}%`;
    
    // Update class based on trend direction
    if (highPercent < 0) {
        trendElements[0].classList.add('positive');
        trendElements[0].classList.remove('negative');
        trendElements[0].querySelector('.trend-value').textContent = `${highPercent}%`;
        trendElements[0].querySelector('.trend-label').textContent = 'High Risk Reduction';
    } else {
        trendElements[0].classList.add('negative');
        trendElements[0].classList.remove('positive');
        trendElements[0].querySelector('.trend-value').textContent = `+${highPercent}%`;
        trendElements[0].querySelector('.trend-label').textContent = 'High Risk Increase';
    }
}

/**
 * Load Requirements Risk Data
 */
function loadRequirementsRiskData(project, timePeriod) {
    // In a real implementation, this would fetch data from an API
    // For this lab, we'll use mock data
    
    const tableBody = document.querySelector('#requirements-risk-table tbody');
    tableBody.innerHTML = '';
    
    // Mock data
    const mockData = [
        {
            id: 'REQ-001',
            description: 'The system shall authenticate users with multi-factor authentication.',
            riskLevel: 'High',
            riskFactors: 'Security, Complexity',
            mitigation: 'Implement standard MFA library',
            impact: 5,
            probability: 3
        },
        {
            id: 'REQ-002',
            description: 'The system shall process payments within 3 seconds.',
            riskLevel: 'High',
            riskFactors: 'Performance, External Dependency',
            mitigation: 'Optimize payment gateway integration',
            impact: 4,
            probability: 4
        },
        {
            id: 'REQ-003',
            description: 'The system shall support 10,000 concurrent users.',
            riskLevel: 'Medium',
            riskFactors: 'Scalability, Performance',
            mitigation: 'Implement load balancing',
            impact: 4,
            probability: 2
        },
        {
            id: 'REQ-004',
            description: 'The system shall comply with GDPR regulations.',
            riskLevel: 'Medium',
            riskFactors: 'Compliance, Legal',
            mitigation: 'Regular compliance audits',
            impact: 3,
            probability: 3
        },
        {
            id: 'REQ-005',
            description: 'The system shall provide real-time notifications.',
            riskLevel: 'Low',
            riskFactors: 'Technical Implementation',
            mitigation: 'Use WebSockets protocol',
            impact: 2,
            probability: 2
        },
        {
            id: 'REQ-006',
            description: 'The system shall support mobile devices.',
            riskLevel: 'Low',
            riskFactors: 'UI/UX, Compatibility',
            mitigation: 'Responsive design approach',
            impact: 2,
            probability: 1
        }
    ];
    
    // Filter data based on project
    let filteredData = mockData;
    if (project !== 'all') {
        if (project === 'project1') {
            filteredData = mockData.filter(item => ['REQ-001', 'REQ-002'].includes(item.id));
        } else if (project === 'project2') {
            filteredData = mockData.filter(item => ['REQ-003', 'REQ-004'].includes(item.id));
        } else if (project === 'project3') {
            filteredData = mockData.filter(item => ['REQ-005', 'REQ-006'].includes(item.id));
        }
    }
    
    // Populate table
    filteredData.forEach(req => {
        const row = document.createElement('tr');
        
        // Add data attributes for filtering
        row.dataset.impact = req.impact;
        row.dataset.probability = req.probability;
        
        // Add risk class
        if (req.riskLevel === 'High') {
            row.classList.add('high-risk-row');
        } else if (req.riskLevel === 'Medium') {
            row.classList.add('medium-risk-row');
        } else {
            row.classList.add('low-risk-row');
        }
        
        row.innerHTML = `
            <td>${req.id}</td>
            <td>${req.description}</td>
            <td><span class="risk-badge ${req.riskLevel.toLowerCase()}-risk">${req.riskLevel}</span></td>
            <td>${req.riskFactors}</td>
            <td>${req.mitigation}</td>
        `;
        
        tableBody.appendChild(row);
    });
}

/**
 * Load Risk Categories Data
 */
function loadRiskCategoriesData(project, timePeriod) {
    // In a real implementation, this would fetch data from an API
    // For this lab, we'll use mock data
    
    let data = [8, 6, 4, 3];
    
    // Apply project filter
    if (project !== 'all') {
        // Simulate filtered data
        if (project === 'project1') {
            data = [4, 2, 1, 2];
        } else if (project === 'project2') {
            data = [3, 3, 2, 1];
        } else if (project === 'project3') {
            data = [1, 1, 1, 0];
        }
    }
    
    // Update the chart
    window.riskCategoriesChart.data.datasets[0].data = data;
    window.riskCategoriesChart.update();
    
    // Update the category bars
    const categories = ['Technical', 'Business', 'Operational', 'Compliance'];
    const total = data.reduce((a, b) => a + b, 0);
    
    for (let i = 0; i < categories.length; i++) {
        const percentage = total > 0 ? Math.round((data[i] / total) * 100) : 0;
        const categoryItem = document.querySelectorAll('.category-item')[i];
        
        if (categoryItem) {
            const bar = categoryItem.querySelector('.category-bar');
            const valueText = categoryItem.querySelector('.category-bar-container span');
            
            bar.style.width = `${percentage}%`;
            valueText.textContent = `${percentage}%`;
        }
    }
}

/**
 * Update Risk Matrix
 */
function updateRiskMatrix(project, timePeriod) {
    // In a real implementation, this would update the matrix with actual risk counts
    // For this lab, we'll simulate this by adding risk counts to cells
    
    // Reset all cells
    const cells = document.querySelectorAll('.matrix-cell');
    cells.forEach(cell => {
        // Remove any risk counts
        const text = cell.textContent;
        cell.textContent = text.split(' ')[0]; // Keep only the score
        cell.classList.remove('has-risks');
    });
    
    // Add risk counts based on mock data
    const riskCounts = {
        '5-3': 1, // Impact 5, Probability 3
        '4-4': 1, // Impact 4, Probability 4
        '4-2': 1, // Impact 4, Probability 2
        '3-3': 1, // Impact 3, Probability 3
        '2-2': 1, // Impact 2, Probability 2
        '2-1': 1  // Impact 2, Probability 1
    };
    
    // Apply project filter
    if (project !== 'all') {
        if (project === 'project1') {
            Object.keys(riskCounts).forEach(key => {
                if (!['5-3', '4-4'].includes(key)) {
                    delete riskCounts[key];
                }
            });
        } else if (project === 'project2') {
            Object.keys(riskCounts).forEach(key => {
                if (!['4-2', '3-3'].includes(key)) {
                    delete riskCounts[key];
                }
            });
        } else if (project === 'project3') {
            Object.keys(riskCounts).forEach(key => {
                if (!['2-2', '2-1'].includes(key)) {
                    delete riskCounts[key];
                }
            });
        }
    }
    
    // Update cells with risk counts
    cells.forEach(cell => {
        const impact = parseInt(cell.dataset.impact);
        const probability = parseInt(cell.dataset.probability);
        const key = `${impact}-${probability}`;
        
        if (riskCounts[key]) {
            cell.textContent = `${cell.textContent} (${riskCounts[key]})`;
            cell.classList.add('has-risks');
        }
    });
}

/**
 * Load Mitigation Actions Data
 */
function loadMitigationActionsData(project, timePeriod) {
    // In a real implementation, this would fetch data from an API
    // For this lab, we'll use mock data
    
    const tableBody = document.querySelector('#mitigation-actions-table tbody');
    tableBody.innerHTML = '';
    
    // Mock data
    const mockData = [
        {
            id: 'ACT-001',
            relatedRisk: 'REQ-001',
            description: 'Implement standard MFA library integration',
            owner: 'John Smith',
            dueDate: '2023-07-15',
            status: 'In Progress'
        },
        {
            id: 'ACT-002',
            relatedRisk: 'REQ-002',
            description: 'Optimize payment gateway integration with caching',
            owner: 'Jane Doe',
            dueDate: '2023-07-20',
            status: 'Open'
        },
        {
            id: 'ACT-003',
            relatedRisk: 'REQ-003',
            description: 'Implement load balancing across multiple servers',
            owner: 'Michael Johnson',
            dueDate: '2023-07-25',
            status: 'In Progress'
        },
        {
            id: 'ACT-004',
            relatedRisk: 'REQ-004',
            description: 'Schedule quarterly compliance audit with legal team',
            owner: 'Sarah Williams',
            dueDate: '2023-08-01',
            status: 'Open'
        },
        {
            id: 'ACT-005',
            relatedRisk: 'REQ-005',
            description: 'Implement WebSockets for real-time notifications',
            owner: 'Robert Brown',
            dueDate: '2023-06-30',
            status: 'Completed'
        },
        {
            id: 'ACT-006',
            relatedRisk: 'REQ-006',
            description: 'Develop responsive design templates for mobile support',
            owner: 'Emily Davis',
            dueDate: '2023-06-15',
            status: 'Overdue'
        }
    ];
    
    // Filter data based on project
    let filteredData = mockData;
    if (project !== 'all') {
        if (project === 'project1') {
            filteredData = mockData.filter(item => ['ACT-001', 'ACT-002'].includes(item.id));
        } else if (project === 'project2') {
            filteredData = mockData.filter(item => ['ACT-003', 'ACT-004'].includes(item.id));
        } else if (project === 'project3') {
            filteredData = mockData.filter(item => ['ACT-005', 'ACT-006'].includes(item.id));
        }
    }
    
    // Populate table
    filteredData.forEach(action => {
        const row = document.createElement('tr');
        
        // Add status class
        row.classList.add(`status-${action.status.toLowerCase().replace(' ', '-')}`);
        
        let statusClass = '';
        if (action.status === 'Open') {
            statusClass = 'status-open';
        } else if (action.status === 'In Progress') {
            statusClass = 'status-in-progress';
        } else if (action.status === 'Completed') {
            statusClass = 'status-completed';
        } else if (action.status === 'Overdue') {
            statusClass = 'status-overdue';
        }
        
        row.innerHTML = `
            <td>${action.id}</td>
            <td>${action.relatedRisk}</td>
            <td>${action.description}</td>
            <td>${action.owner}</td>
            <td>${action.dueDate}</td>
            <td><span class="status ${statusClass}">${action.status}</span></td>
        `;
        
        tableBody.appendChild(row);
    });
}

/**
 * Open Risk Assessment Modal
 */
function openRiskAssessmentModal() {
    document.getElementById('risk-assessment-modal').style.display = 'block';
    document.getElementById('risk-assessment-form').reset();
}

/**
 * Close Risk Assessment Modal
 */
function closeRiskAssessmentModal() {
    document.getElementById('risk-assessment-modal').style.display = 'none';
}

/**
 * Save Risk Assessment
 */
function saveRiskAssessment() {
    // Get form values
    const requirementId = document.getElementById('requirement-id').value;
    const riskDescription = document.getElementById('risk-description').value;
    const probability = document.getElementById('risk-probability').value;
    const impact = document.getElementById('risk-impact').value;
    const category = document.getElementById('risk-category').value;
    const mitigation = document.getElementById('risk-mitigation').value;
    
    console.log('Saving risk assessment...');
    console.log({
        requirementId,
        riskDescription,
        probability,
        impact,
        category,
        mitigation
    });
    
    // In a real implementation, this would send data to an API
    // For this lab, we'll just show a success message and close the modal
    
    alert('Risk assessment saved successfully!');
    closeRiskAssessmentModal();
    
    // Refresh the dashboard
    loadDashboardData();
}

/**
 * Export Mitigation Actions
 */
function exportMitigationActions() {
    console.log('Exporting mitigation actions...');
    
    // In a real implementation, this would generate a CSV or PDF file
    // For this lab, we'll just show a success message
    
    alert('Mitigation actions exported successfully!');
}
