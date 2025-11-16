/**
 * Requirements Change Management Dashboard
 * JavaScript for ISO/IEC/IEEE 29148:2011 Lab13
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the dashboard components
    initNavigation();
    initCharts();
    initModals();
    initThemeToggle();
    initTagInputs();
});

/**
 * Initialize sidebar navigation and panel switching
 */
function initNavigation() {
    const navItems = document.querySelectorAll('.sidebar-nav li');
    const panels = document.querySelectorAll('.panel');
    
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove active class from all nav items
            navItems.forEach(nav => nav.classList.remove('active'));
            
            // Add active class to clicked nav item
            item.classList.add('active');
            
            // Hide all panels
            panels.forEach(panel => panel.classList.remove('active'));
            
            // Show the corresponding panel
            const panelId = `${item.dataset.panel}-panel`;
            document.getElementById(panelId).classList.add('active');
        });
    });

    // Initialize tabs in approval panel
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all tab buttons
            tabButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked tab button
            button.classList.add('active');
            
            // Here you would toggle content visibility based on the selected tab
            // For demo purposes, we'll just log the selected tab
            console.log(`Selected tab: ${button.dataset.tab}`);
        });
    });
}

/**
 * Initialize all charts using Chart.js
 */
function initCharts() {
    // Status distribution chart (doughnut)
    const statusCtx = document.getElementById('status-chart').getContext('2d');
    const statusChart = new Chart(statusCtx, {
        type: 'doughnut',
        data: {
            labels: ['Submitted', 'In Review', 'Approved', 'Rejected', 'Implemented'],
            datasets: [{
                data: [24, 18, 82, 22, 32],
                backgroundColor: [
                    '#17a2b8', // submitted
                    '#ffc107', // in review
                    '#28a745', // approved
                    '#dc3545', // rejected
                    '#6610f2'  // implemented
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        usePointStyle: true,
                        pointStyle: 'circle'
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.formattedValue;
                            const total = context.dataset.data.reduce((acc, data) => acc + data, 0);
                            const percentage = Math.round((context.raw / total) * 100);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });

    // Priority distribution chart (doughnut)
    const priorityCtx = document.getElementById('priority-chart').getContext('2d');
    const priorityChart = new Chart(priorityCtx, {
        type: 'doughnut',
        data: {
            labels: ['High', 'Medium', 'Low'],
            datasets: [{
                data: [42, 65, 21],
                backgroundColor: [
                    '#dc3545', // high
                    '#fd7e14', // medium
                    '#20c997'  // low
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        usePointStyle: true,
                        pointStyle: 'circle'
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.formattedValue;
                            const total = context.dataset.data.reduce((acc, data) => acc + data, 0);
                            const percentage = Math.round((context.raw / total) * 100);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });

    // Impact analysis trends chart (line)
    const impactCtx = document.getElementById('impact-chart').getContext('2d');
    const impactChart = new Chart(impactCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
            datasets: [
                {
                    label: 'High Impact',
                    data: [12, 15, 18, 14, 22, 19, 23, 25, 28],
                    borderColor: '#dc3545',
                    backgroundColor: 'rgba(220, 53, 69, 0.1)',
                    borderWidth: 2,
                    tension: 0.4,
                    fill: true
                },
                {
                    label: 'Medium Impact',
                    data: [24, 27, 32, 36, 29, 34, 38, 35, 39],
                    borderColor: '#fd7e14',
                    backgroundColor: 'rgba(253, 126, 20, 0.1)',
                    borderWidth: 2,
                    tension: 0.4,
                    fill: true
                },
                {
                    label: 'Low Impact',
                    data: [18, 15, 12, 14, 10, 15, 12, 8, 7],
                    borderColor: '#20c997',
                    backgroundColor: 'rgba(32, 201, 151, 0.1)',
                    borderWidth: 2,
                    tension: 0.4,
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
                    grid: {
                        drawBorder: false
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                    align: 'end'
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                }
            },
            interaction: {
                mode: 'nearest',
                axis: 'x',
                intersect: false
            }
        }
    });

    // Chart type toggle buttons
    const chartTypeButtons = document.querySelectorAll('.btn-chart-type');
    chartTypeButtons.forEach(button => {
        button.addEventListener('click', () => {
            chartTypeButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            // Demo data for different chart types
            const chartData = {
                requirements: [
                    [12, 15, 18, 14, 22, 19, 23, 25, 28],
                    [24, 27, 32, 36, 29, 34, 38, 35, 39],
                    [18, 15, 12, 14, 10, 15, 12, 8, 7]
                ],
                risk: [
                    [8, 12, 15, 18, 20, 17, 15, 19, 22],
                    [18, 22, 25, 28, 24, 26, 30, 28, 32],
                    [30, 27, 25, 22, 20, 18, 15, 12, 10]
                ],
                complexity: [
                    [5, 8, 12, 15, 18, 22, 25, 28, 30],
                    [20, 22, 25, 28, 30, 32, 35, 38, 40],
                    [12, 10, 8, 7, 6, 8, 10, 12, 15]
                ]
            };
            
            const chartType = button.dataset.type;
            
            // Update chart data
            impactChart.data.datasets.forEach((dataset, index) => {
                dataset.data = chartData[chartType][index];
            });
            
            impactChart.update();
        });
    });
}

/**
 * Initialize modal windows
 */
function initModals() {
    // New change request modal
    const newChangeModal = document.getElementById('new-change-modal');
    const newChangeButtons = document.querySelectorAll('#btn-new-change, #btn-new-change-2');
    const closeModalButton = document.querySelector('.btn-close');
    const cancelButton = document.getElementById('btn-cancel-change');
    const submitButton = document.getElementById('btn-submit-change');
    
    // Open modal
    newChangeButtons.forEach(button => {
        button.addEventListener('click', () => {
            newChangeModal.style.display = 'flex';
        });
    });
    
    // Close modal
    function closeModal() {
        newChangeModal.style.display = 'none';
    }
    
    closeModalButton.addEventListener('click', closeModal);
    cancelButton.addEventListener('click', closeModal);
    
    // Close modal when clicking outside of it
    window.addEventListener('click', (event) => {
        if (event.target === newChangeModal) {
            closeModal();
        }
    });
    
    // Submit change request (demo)
    submitButton.addEventListener('click', () => {
        // Get form values
        const title = document.getElementById('change-title').value;
        const description = document.getElementById('change-description').value;
        const type = document.getElementById('change-type').value;
        const priority = document.getElementById('change-priority').value;
        
        // Validate form (simple validation)
        if (!title || !description) {
            alert('Please fill in all required fields.');
            return;
        }
        
        // Here you would normally send the data to the server
        console.log('Submitting change request:', {
            title,
            description,
            type,
            priority
        });
        
        // For demo, just close the modal and show success message
        closeModal();
        alert('Change request submitted successfully!');
    });
}

/**
 * Initialize theme toggle (dark/light mode)
 */
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');
    const darkModeToggle = document.getElementById('dark-mode');
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
        if (darkModeToggle) darkModeToggle.checked = true;
    }
    
    // Toggle theme on button click
    themeToggle.addEventListener('click', toggleTheme);
    
    // Toggle theme on settings switch change
    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', () => {
            if (darkModeToggle.checked) {
                document.body.classList.add('dark-mode');
                themeIcon.classList.replace('fa-moon', 'fa-sun');
                localStorage.setItem('theme', 'dark');
            } else {
                document.body.classList.remove('dark-mode');
                themeIcon.classList.replace('fa-sun', 'fa-moon');
                localStorage.setItem('theme', 'light');
            }
        });
    }
    
    function toggleTheme() {
        if (document.body.classList.contains('dark-mode')) {
            document.body.classList.remove('dark-mode');
            themeIcon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('theme', 'light');
            if (darkModeToggle) darkModeToggle.checked = false;
        } else {
            document.body.classList.add('dark-mode');
            themeIcon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('theme', 'dark');
            if (darkModeToggle) darkModeToggle.checked = true;
        }
    }
}

/**
 * Initialize tag input fields
 */
function initTagInputs() {
    const tagInputs = document.querySelectorAll('#requirement-input, #affected-requirements');
    
    tagInputs.forEach(input => {
        const tagsContainer = input.nextElementSibling;
        
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && input.value.trim() !== '') {
                e.preventDefault();
                
                // Create new tag
                const tag = document.createElement('div');
                tag.className = 'tag';
                
                // Format tag text (e.g., REQ-123)
                let tagText = input.value.trim();
                if (!tagText.startsWith('REQ-') && !isNaN(tagText)) {
                    tagText = `REQ-${tagText.padStart(3, '0')}`;
                }
                
                tag.innerHTML = `
                    ${tagText}
                    <button type="button">
                        <i class="fas fa-times"></i>
                    </button>
                `;
                
                // Add delete event to tag
                const deleteButton = tag.querySelector('button');
                deleteButton.addEventListener('click', () => {
                    tag.remove();
                });
                
                // Add tag to container
                tagsContainer.appendChild(tag);
                
                // Clear input
                input.value = '';
            }
        });
    });
    
    // Initialize impact analysis button
    const analyzeButton = document.getElementById('btn-analyze-impact');
    if (analyzeButton) {
        analyzeButton.addEventListener('click', () => {
            const changeRequest = document.getElementById('change-request-select').value;
            const requirementTags = document.querySelectorAll('#selected-requirements .tag');
            
            if (!changeRequest && requirementTags.length === 0) {
                alert('Please select a change request or add requirements to analyze.');
                return;
            }
            
            // Show loading state
            analyzeButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
            analyzeButton.disabled = true;
            
            // Simulate analysis (would be a server call in a real app)
            setTimeout(() => {
                // Reset button
                analyzeButton.innerHTML = '<i class="fas fa-project-diagram"></i> Analyze Impact';
                analyzeButton.disabled = false;
                
                // Show results
                const resultsDiv = document.querySelector('.impact-analysis-results');
                resultsDiv.style.display = 'block';
                
                // Demo result content
                resultsDiv.innerHTML = `
                    <h3>Impact Analysis Results</h3>
                    <p>Analysis completed for ${changeRequest || 'selected requirements'}.</p>
                    
                    <div class="impact-summary">
                        <div class="impact-metrics">
                            <div class="impact-metric">
                                <span class="metric-value">8</span>
                                <span class="metric-label">Directly Affected Requirements</span>
                            </div>
                            <div class="impact-metric">
                                <span class="metric-value">15</span>
                                <span class="metric-label">Indirectly Affected Requirements</span>
                            </div>
                            <div class="impact-metric">
                                <span class="metric-value">High</span>
                                <span class="metric-label">Overall Impact Level</span>
                            </div>
                            <div class="impact-metric">
                                <span class="metric-value">Medium</span>
                                <span class="metric-label">Risk Level</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="impact-visualization">
                        <p class="placeholder-text">Dependency graph visualization would appear here.</p>
                        <p class="placeholder-text">In a real application, this would be rendered using NetworkX data from the backend.</p>
                    </div>
                    
                    <h4>Affected Requirements</h4>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Requirement ID</th>
                                <th>Title</th>
                                <th>Impact Type</th>
                                <th>Impact Level</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>REQ-001</td>
                                <td>User Authentication</td>
                                <td>Direct</td>
                                <td><span class="badge high">High</span></td>
                            </tr>
                            <tr>
                                <td>REQ-002</td>
                                <td>Session Management</td>
                                <td>Direct</td>
                                <td><span class="badge high">High</span></td>
                            </tr>
                            <tr>
                                <td>REQ-015</td>
                                <td>User Permissions</td>
                                <td>Direct</td>
                                <td><span class="badge medium">Medium</span></td>
                            </tr>
                            <tr>
                                <td>REQ-023</td>
                                <td>Security Logging</td>
                                <td>Indirect</td>
                                <td><span class="badge medium">Medium</span></td>
                            </tr>
                            <tr>
                                <td>REQ-045</td>
                                <td>Audit Trail</td>
                                <td>Indirect</td>
                                <td><span class="badge low">Low</span></td>
                            </tr>
                        </tbody>
                    </table>
                    
                    <div class="impact-actions">
                        <button class="btn btn-secondary">Export Results</button>
                        <button class="btn btn-primary">Create Change Request</button>
                    </div>
                `;
                
                // Add some style for the impact analysis results
                const style = document.createElement('style');
                style.textContent = `
                    .impact-summary {
                        margin: 20px 0;
                    }
                    
                    .impact-metrics {
                        display: grid;
                        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                        gap: 15px;
                        margin-bottom: 20px;
                    }
                    
                    .impact-metric {
                        background-color: var(--bg-secondary);
                        padding: 15px;
                        border-radius: 8px;
                        text-align: center;
                    }
                    
                    .metric-value {
                        display: block;
                        font-size: 24px;
                        font-weight: bold;
                        margin-bottom: 5px;
                    }
                    
                    .metric-label {
                        color: var(--text-secondary);
                        font-size: 14px;
                    }
                    
                    .impact-visualization {
                        background-color: var(--bg-secondary);
                        border: 1px dashed var(--border-color);
                        border-radius: 8px;
                        padding: 40px;
                        margin-bottom: 20px;
                        text-align: center;
                    }
                    
                    .placeholder-text {
                        color: var(--text-secondary);
                        margin-bottom: 10px;
                    }
                    
                    .impact-actions {
                        display: flex;
                        justify-content: flex-end;
                        gap: 10px;
                        margin-top: 20px;
                    }
                    
                    h4 {
                        margin: 20px 0 15px;
                    }
                `;
                
                document.head.appendChild(style);
            }, 2000);
        });
    }
}

/**
 * Filter change requests based on selected filters
 * This would connect to the backend in a real app
 */
function filterChangeRequests() {
    const statusFilter = document.getElementById('status-filter').value;
    const priorityFilter = document.getElementById('priority-filter').value;
    const typeFilter = document.getElementById('type-filter').value;
    
    console.log('Filtering change requests with:', {
        status: statusFilter,
        priority: priorityFilter,
        type: typeFilter
    });
    
    // In a real app, you would fetch filtered data from the server
    // and update the UI with the results
}

/**
 * Time range selector for dashboard charts
 */
document.addEventListener('DOMContentLoaded', function() {
    const timeRangeSelect = document.getElementById('time-range');
    
    if (timeRangeSelect) {
        timeRangeSelect.addEventListener('change', () => {
            const selectedRange = timeRangeSelect.value;
            console.log(`Time range changed to: ${selectedRange}`);
            
            // In a real app, you would update all charts with new data based on the selected time range
            // This would typically involve API calls to get new data
        });
    }
});
