// Quality Dashboard JavaScript

// DOM Elements
document.addEventListener('DOMContentLoaded', function() {
    // Theme Toggle
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');
    let isDarkMode = localStorage.getItem('darkMode') === 'true';

    // Apply saved theme or default to light
    if (isDarkMode) {
        document.documentElement.setAttribute('data-theme', 'dark');
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    }

    // Theme toggle event
    themeToggle.addEventListener('click', function() {
        isDarkMode = !isDarkMode;
        if (isDarkMode) {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
        } else {
            document.documentElement.removeAttribute('data-theme');
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
        }
        localStorage.setItem('darkMode', isDarkMode);
    });

    // Panel navigation
    const navItems = document.querySelectorAll('.sidebar-nav li');
    const panels = document.querySelectorAll('.panel');

    navItems.forEach(item => {
        item.addEventListener('click', function() {
            const panelId = this.getAttribute('data-panel');
            
            // Update active nav item
            navItems.forEach(navItem => navItem.classList.remove('active'));
            this.classList.add('active');
            
            // Show selected panel
            panels.forEach(panel => {
                if (panel.id === panelId + '-panel') {
                    panel.classList.add('active');
                } else {
                    panel.classList.remove('active');
                }
            });
        });
    });

    // Modal functionality
    const modals = document.querySelectorAll('.modal');
    const modalTriggers = document.querySelectorAll('[id^="btn-run-assessment"], [id^="btn-add-schedule"]');
    const modalCloseButtons = document.querySelectorAll('.btn-close, .btn-cancel-assessment');

    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', function() {
            const modalId = this.id.replace('btn-', '') + '-modal';
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.classList.add('active');
            }
        });
    });

    modalCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modal = this.closest('.modal');
            if (modal) {
                modal.classList.remove('active');
            }
        });
    });

    // Close modal when clicking outside
    modals.forEach(modal => {
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.remove('active');
            }
        });
    });

    // Initialize Charts
    initializeCharts();
});

// Chart initialization
function initializeCharts() {
    // Set Chart.js defaults
    Chart.defaults.font.family = "'Segoe UI', 'Helvetica Neue', 'Arial', sans-serif";
    Chart.defaults.font.size = 12;
    Chart.defaults.color = '#6c757d';
    
    // Quality Metrics Chart
    const metricsChart = document.getElementById('metrics-chart');
    if (metricsChart) {
        new Chart(metricsChart, {
            type: 'bar',
            data: {
                labels: ['Completeness', 'Clarity', 'Consistency', 'Verifiability', 'Traceability', 'Feasibility'],
                datasets: [{
                    label: 'Score',
                    data: [0.84, 0.72, 0.85, 0.73, 0.68, 0.81],
                    backgroundColor: '#4a6de5',
                    barThickness: 20,
                    borderRadius: 4
                }, {
                    label: 'Threshold',
                    data: [0.80, 0.70, 0.80, 0.70, 0.60, 0.70],
                    backgroundColor: 'rgba(220, 220, 220, 0.5)',
                    barThickness: 20,
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.dataset.label + ': ' + context.raw.toFixed(2);
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 1,
                        ticks: {
                            callback: function(value) {
                                return value.toFixed(1);
                            }
                        }
                    }
                }
            }
        });
    }

    // Requirements Status Chart
    const requirementsChart = document.getElementById('requirements-chart');
    if (requirementsChart) {
        new Chart(requirementsChart, {
            type: 'doughnut',
            data: {
                labels: ['Passing', 'Warning', 'Failing'],
                datasets: [{
                    data: [85, 10, 5],
                    backgroundColor: ['#28a745', '#ffc107', '#dc3545'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '65%',
                plugins: {
                    legend: {
                        position: 'bottom'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.label + ': ' + context.raw + '%';
                            }
                        }
                    }
                }
            }
        });
    }

    // Trends Chart
    const trendsChart = document.getElementById('trends-chart');
    if (trendsChart) {
        const dates = getLastNMonths(6);
        
        new Chart(trendsChart, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Overall Quality',
                    data: [0.70, 0.72, 0.75, 0.76, 0.79, 0.82],
                    borderColor: '#4a6de5',
                    backgroundColor: 'rgba(74, 109, 229, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.3
                }, {
                    label: 'Requirements Passing',
                    data: [0.72, 0.75, 0.78, 0.80, 0.83, 0.85],
                    borderColor: '#28a745',
                    backgroundColor: 'rgba(40, 167, 69, 0.0)',
                    borderWidth: 2,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                interaction: {
                    mode: 'index',
                    intersect: false
                },
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.dataset.label + ': ' + context.raw.toFixed(2);
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        min: 0.5,
                        max: 1,
                        ticks: {
                            callback: function(value) {
                                return value.toFixed(1);
                            }
                        }
                    }
                }
            }
        });
    }

    // Overall Trend Chart
    const overallTrendChart = document.getElementById('overall-trend-chart');
    if (overallTrendChart) {
        const dates = getLastNMonths(12);
        
        new Chart(overallTrendChart, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Overall Quality',
                    data: [0.65, 0.67, 0.68, 0.70, 0.72, 0.73, 0.75, 0.76, 0.78, 0.79, 0.81, 0.82],
                    borderColor: '#4a6de5',
                    backgroundColor: 'rgba(74, 109, 229, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.3
                }, {
                    label: 'Quality Target',
                    data: Array(12).fill(0.80),
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    borderWidth: 2,
                    borderDash: [5, 5],
                    pointRadius: 0,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.dataset.label + ': ' + context.raw.toFixed(2);
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        min: 0.5,
                        max: 1,
                        ticks: {
                            callback: function(value) {
                                return value.toFixed(1);
                            }
                        }
                    }
                }
            }
        });
    }

    // Metrics Trend Chart
    const metricsTrendChart = document.getElementById('metrics-trend-chart');
    if (metricsTrendChart) {
        const dates = getLastNMonths(6);
        
        new Chart(metricsTrendChart, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Completeness',
                    data: [0.76, 0.78, 0.80, 0.81, 0.82, 0.84],
                    borderColor: '#4a6de5',
                    borderWidth: 2,
                    tension: 0.3
                }, {
                    label: 'Clarity',
                    data: [0.68, 0.69, 0.70, 0.70, 0.71, 0.72],
                    borderColor: '#17a2b8',
                    borderWidth: 2,
                    tension: 0.3
                }, {
                    label: 'Consistency',
                    data: [0.79, 0.80, 0.81, 0.82, 0.84, 0.85],
                    borderColor: '#28a745',
                    borderWidth: 2,
                    tension: 0.3
                }, {
                    label: 'Verifiability',
                    data: [0.70, 0.71, 0.71, 0.72, 0.72, 0.73],
                    borderColor: '#ffc107',
                    borderWidth: 2,
                    tension: 0.3
                }, {
                    label: 'Traceability',
                    data: [0.72, 0.71, 0.70, 0.69, 0.68, 0.68],
                    borderColor: '#dc3545',
                    borderWidth: 2,
                    tension: 0.3
                }, {
                    label: 'Feasibility',
                    data: [0.81, 0.81, 0.81, 0.81, 0.81, 0.81],
                    borderColor: '#6c757d',
                    borderWidth: 2,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                interaction: {
                    mode: 'index',
                    intersect: false
                },
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.dataset.label + ': ' + context.raw.toFixed(2);
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        min: 0.5,
                        max: 1,
                        ticks: {
                            callback: function(value) {
                                return value.toFixed(1);
                            }
                        }
                    }
                }
            }
        });
    }
}

// Helper to get last N months for chart labels
function getLastNMonths(n) {
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const now = new Date();
    const result = [];
    
    for (let i = n - 1; i >= 0; i--) {
        const monthIndex = (now.getMonth() - i + 12) % 12;
        result.push(months[monthIndex]);
    }
    
    return result;
}

// Chart type selection
document.addEventListener('DOMContentLoaded', function() {
    const chartTypeButtons = document.querySelectorAll('.btn-chart-type');
    
    chartTypeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const chartType = this.getAttribute('data-type');
            const parentChart = this.closest('.chart-card');
            
            // Update active button
            const siblingButtons = parentChart.querySelectorAll('.btn-chart-type');
            siblingButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Here you would update the chart based on the selected type
            // For a real implementation, you would likely re-render the chart with new data
            console.log(`Chart type changed to: ${chartType}`);
        });
    });
});

// Quality Gates Run Button
document.addEventListener('DOMContentLoaded', function() {
    const runGatesButton = document.getElementById('btn-run-gates');
    
    if (runGatesButton) {
        runGatesButton.addEventListener('click', function() {
            // Show loading state
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Running...';
            this.disabled = true;
            
            // Simulate gate evaluation (would be a real API call)
            setTimeout(() => {
                // Reset button
                this.innerHTML = '<i class="fas fa-play"></i> Run Gates';
                this.disabled = false;
                
                // Show success notification
                showNotification('Quality gates evaluated successfully', 'success');
            }, 2000);
        });
    }
});

// Run Assessment Button in Modal
document.addEventListener('DOMContentLoaded', function() {
    const startAssessmentButton = document.getElementById('btn-start-assessment');
    
    if (startAssessmentButton) {
        startAssessmentButton.addEventListener('click', function() {
            const modal = this.closest('.modal');
            
            // Show loading state
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
            this.disabled = true;
            
            // Simulate assessment (would be a real API call)
            setTimeout(() => {
                // Reset button
                this.innerHTML = 'Start Assessment';
                this.disabled = false;
                
                // Close modal
                if (modal) {
                    modal.classList.remove('active');
                }
                
                // Show success notification
                showNotification('Quality assessment completed successfully', 'success');
            }, 3000);
        });
    }
});

// Submit Approval Button
document.addEventListener('DOMContentLoaded', function() {
    const submitApprovalButton = document.getElementById('btn-submit-approval');
    
    if (submitApprovalButton) {
        submitApprovalButton.addEventListener('click', function() {
            const reviewer = document.getElementById('reviewer-select').value;
            const decision = document.getElementById('approval-decision').value;
            
            if (!reviewer || !decision) {
                showNotification('Please select a reviewer and decision', 'error');
                return;
            }
            
            // Show loading state
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';
            this.disabled = true;
            
            // Simulate submission (would be a real API call)
            setTimeout(() => {
                // Reset button
                this.innerHTML = 'Submit Approval';
                this.disabled = false;
                
                // Update UI to reflect approval
                const managerGate = document.querySelector('.gate-item.pending');
                if (managerGate && decision === 'approve') {
                    managerGate.classList.remove('pending');
                    managerGate.classList.add('passed');
                    managerGate.querySelector('.gate-status').textContent = 'PASSED';
                    managerGate.querySelector('.gate-details p').textContent = 
                        `Approved by: ${reviewer === 'project-manager' ? 'Project Manager' : 'Requirements Manager'}`;
                    
                    // Update phase status if all gates passed
                    const phase = managerGate.closest('.phase-card');
                    const failedGates = phase.querySelectorAll('.gate-item.failed');
                    if (failedGates.length === 0) {
                        phase.querySelector('.status-badge').textContent = 'PASSED';
                        phase.querySelector('.status-badge').classList.remove('failed');
                        phase.querySelector('.status-badge').classList.add('passed');
                    }
                }
                
                // Show success notification
                showNotification('Approval submitted successfully', 'success');
            }, 1500);
        });
    }
});

// Show notification function
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    
    // Set icon based on type
    let icon = 'info-circle';
    if (type === 'success') icon = 'check-circle';
    if (type === 'error') icon = 'exclamation-circle';
    if (type === 'warning') icon = 'exclamation-triangle';
    
    notification.innerHTML = `
        <i class="fas fa-${icon}"></i>
        <span>${message}</span>
        <button class="close-notification"><i class="fas fa-times"></i></button>
    `;
    
    // Add styles
    Object.assign(notification.style, {
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        backgroundColor: type === 'success' ? '#d4edda' : 
                         type === 'error' ? '#f8d7da' : 
                         type === 'warning' ? '#fff3cd' : '#d1ecf1',
        color: type === 'success' ? '#155724' : 
               type === 'error' ? '#721c24' : 
               type === 'warning' ? '#856404' : '#0c5460',
        padding: '12px 20px',
        borderRadius: '4px',
        boxShadow: '0 2px 5px rgba(0,0,0,0.1)',
        display: 'flex',
        alignItems: 'center',
        gap: '10px',
        maxWidth: '400px',
        zIndex: '9999',
        animation: 'slideIn 0.3s ease-out forwards'
    });
    
    // Add animation
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
    `;
    document.head.appendChild(style);
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Add close button handler
    const closeBtn = notification.querySelector('.close-notification');
    closeBtn.addEventListener('click', () => {
        notification.style.animation = 'slideOut 0.3s ease-out forwards';
        setTimeout(() => {
            notification.remove();
        }, 300);
    });
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.animation = 'slideOut 0.3s ease-out forwards';
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    notification.remove();
                }
            }, 300);
        }
    }, 5000);
}

// Filter functionality for requirements table
document.addEventListener('DOMContentLoaded', function() {
    const metricFilter = document.getElementById('metric-filter');
    const requirementSearch = document.getElementById('requirement-search');
    
    if (metricFilter && requirementSearch) {
        // Implement filtering logic here
        // This would typically update the requirements table based on selections
    }
});

// Export button functionality
document.addEventListener('DOMContentLoaded', function() {
    const exportButtons = document.querySelectorAll('.btn-export');
    
    exportButtons.forEach(button => {
        button.addEventListener('click', function() {
            showNotification('Exporting dashboard data...', 'info');
            
            // Simulate export process
            setTimeout(() => {
                showNotification('Dashboard data exported successfully', 'success');
            }, 1500);
        });
    });
});
