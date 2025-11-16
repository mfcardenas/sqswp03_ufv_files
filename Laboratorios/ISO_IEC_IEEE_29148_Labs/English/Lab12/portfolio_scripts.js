/**
 * Requirements Portfolio Management Dashboard
 * JavaScript Implementation for ISO/IEC/IEEE 29148 Lab
 */

document.addEventListener('DOMContentLoaded', function() {
    initializeDashboard();
    initializeCharts();
    setupEventListeners();
});

/**
 * Initialize the dashboard functionality
 */
function initializeDashboard() {
    console.log("Initializing Requirements Portfolio Dashboard...");
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('portfolioTheme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        document.getElementById('theme-toggle').innerHTML = '<i class="fas fa-sun"></i>';
    }
    
    // Simulate loading data
    setTimeout(() => {
        console.log("Dashboard data loaded successfully");
    }, 500);
}

/**
 * Initialize all charts in the dashboard
 */
function initializeCharts() {
    // Requirements by Status Chart (Pie Chart)
    const reqStatusCtx = document.getElementById('requirements-status-chart').getContext('2d');
    const reqStatusChart = new Chart(reqStatusCtx, {
        type: 'pie',
        data: {
            labels: ['Approved', 'In Progress', 'Under Review', 'Implemented', 'Rejected'],
            datasets: [{
                data: [45, 25, 15, 10, 5],
                backgroundColor: [
                    'rgba(66, 133, 244, 0.8)',
                    'rgba(52, 168, 83, 0.8)',
                    'rgba(251, 188, 5, 0.8)',
                    'rgba(234, 67, 53, 0.8)',
                    'rgba(128, 128, 128, 0.8)'
                ],
                borderColor: [
                    'rgba(66, 133, 244, 1)',
                    'rgba(52, 168, 83, 1)',
                    'rgba(251, 188, 5, 1)',
                    'rgba(234, 67, 53, 1)',
                    'rgba(128, 128, 128, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        boxWidth: 12,
                        padding: 15
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.raw || 0;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = Math.round((value / total) * 100);
                            return `${label}: ${percentage}% (${value})`;
                        }
                    }
                }
            }
        }
    });
    
    // Strategic Alignment Chart (Radar Chart)
    const strategicCtx = document.getElementById('strategic-alignment-chart').getContext('2d');
    const strategicChart = new Chart(strategicCtx, {
        type: 'radar',
        data: {
            labels: [
                'Business Value', 
                'Technical Alignment', 
                'User Experience', 
                'Security Compliance', 
                'Market Fit',
                'Innovation'
            ],
            datasets: [{
                label: 'Current Portfolio',
                data: [85, 72, 90, 65, 78, 60],
                backgroundColor: 'rgba(66, 133, 244, 0.2)',
                borderColor: 'rgba(66, 133, 244, 1)',
                borderWidth: 2,
                pointBackgroundColor: 'rgba(66, 133, 244, 1)',
                pointRadius: 4
            }, {
                label: 'Target Alignment',
                data: [90, 85, 95, 90, 85, 80],
                backgroundColor: 'rgba(234, 67, 53, 0.05)',
                borderColor: 'rgba(234, 67, 53, 1)',
                borderWidth: 1,
                borderDash: [5, 5],
                pointBackgroundColor: 'rgba(234, 67, 53, 1)',
                pointRadius: 3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    angleLines: {
                        display: true,
                        color: 'rgba(0, 0, 0, 0.1)'
                    },
                    suggestedMin: 0,
                    suggestedMax: 100,
                    ticks: {
                        stepSize: 20,
                        backdropColor: 'transparent'
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        boxWidth: 12,
                        padding: 15
                    }
                }
            }
        }
    });
    
    // Portfolio Trend Chart (Line Chart)
    const trendCtx = document.getElementById('portfolio-trend-chart').getContext('2d');
    const trendChart = new Chart(trendCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'Portfolio Performance',
                data: [65, 68, 70, 72, 75, 73, 76, 80, 82, 85, 87, 90],
                backgroundColor: 'rgba(66, 133, 244, 0.1)',
                borderColor: 'rgba(66, 133, 244, 1)',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }, {
                label: 'Resource Utilization',
                data: [70, 72, 76, 80, 82, 85, 83, 78, 75, 78, 80, 83],
                backgroundColor: 'rgba(52, 168, 83, 0.1)',
                borderColor: 'rgba(52, 168, 83, 1)',
                borderWidth: 2,
                tension: 0.4,
                hidden: true
            }, {
                label: 'Risk Level',
                data: [45, 40, 38, 35, 30, 32, 35, 30, 28, 25, 22, 20],
                backgroundColor: 'rgba(234, 67, 53, 0.1)',
                borderColor: 'rgba(234, 67, 53, 1)',
                borderWidth: 2,
                tension: 0.4,
                hidden: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        stepSize: 20
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
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
                    align: 'end',
                    labels: {
                        boxWidth: 12,
                        usePointStyle: true
                    }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                    callbacks: {
                        label: function(context) {
                            let label = context.dataset.label || '';
                            return `${label}: ${context.parsed.y}%`;
                        }
                    }
                }
            },
            interaction: {
                mode: 'nearest',
                axis: 'x',
                intersect: false
            }
        }
    });
    
    // Store charts in global object for later access
    window.portfolioCharts = {
        reqStatusChart,
        strategicChart,
        trendChart
    };
}

/**
 * Set up all event listeners for the dashboard
 */
function setupEventListeners() {
    // Navigation tabs
    const navItems = document.querySelectorAll('.sidebar-nav li');
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all items
            navItems.forEach(nav => nav.classList.remove('active'));
            
            // Add active class to clicked item
            this.classList.add('active');
            
            // Show corresponding panel
            const panelId = this.getAttribute('data-panel');
            showPanel(panelId);
        });
    });
    
    // Theme toggle
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.addEventListener('click', toggleTheme);
    
    // Chart type buttons
    const chartTypeButtons = document.querySelectorAll('.btn-chart-type');
    chartTypeButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            chartTypeButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Change visible dataset in the trend chart
            const chartType = this.getAttribute('data-type');
            updateTrendChart(chartType);
        });
    });
    
    // Notification button
    const notificationBtn = document.querySelector('.action-button:first-child');
    const notificationPanel = document.getElementById('notification-panel');
    
    notificationBtn.addEventListener('click', function() {
        // Toggle notification panel
        if (notificationPanel.style.display === 'none' || notificationPanel.style.display === '') {
            notificationPanel.style.display = 'block';
        } else {
            notificationPanel.style.display = 'none';
        }
    });
    
    // Close notification panel button
    const closeNotificationBtn = document.querySelector('.btn-close-notifications');
    closeNotificationBtn.addEventListener('click', function() {
        notificationPanel.style.display = 'none';
    });
    
    // Mark notifications as read
    const markReadBtn = document.querySelector('.btn-mark-read');
    markReadBtn.addEventListener('click', function() {
        const unreadNotifications = document.querySelectorAll('.notification-item.unread');
        unreadNotifications.forEach(notification => {
            notification.classList.remove('unread');
        });
        
        // Update notification count
        document.querySelector('.notification-count').textContent = '0';
    });
    
    // Time range selector
    const timeRange = document.getElementById('time-range');
    timeRange.addEventListener('change', function() {
        updateDashboardData(this.value);
    });
    
    // Export button
    const exportBtn = document.querySelector('.btn-export');
    exportBtn.addEventListener('click', exportDashboardData);
    
    // Click outside notification panel to close
    document.addEventListener('click', function(event) {
        if (!notificationPanel.contains(event.target) && 
            !notificationBtn.contains(event.target) && 
            notificationPanel.style.display === 'block') {
            notificationPanel.style.display = 'none';
        }
    });
}

/**
 * Show the specified panel and hide others
 * @param {string} panelId - The ID of the panel to show
 */
function showPanel(panelId) {
    // Hide all panels
    const panels = document.querySelectorAll('.panel');
    panels.forEach(panel => {
        panel.classList.remove('active');
    });
    
    // Show the selected panel
    const selectedPanel = document.getElementById(`${panelId}-panel`);
    if (selectedPanel) {
        selectedPanel.classList.add('active');
    }
}

/**
 * Toggle between light and dark theme
 */
function toggleTheme() {
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');
    
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
        localStorage.setItem('portfolioTheme', 'light');
        updateChartsTheme('light');
    } else {
        body.classList.add('dark-mode');
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        localStorage.setItem('portfolioTheme', 'dark');
        updateChartsTheme('dark');
    }
}

/**
 * Update chart colors based on theme
 * @param {string} theme - The theme to apply ('light' or 'dark')
 */
function updateChartsTheme(theme) {
    if (!window.portfolioCharts) return;
    
    const textColor = theme === 'dark' ? '#ecf0f1' : '#333333';
    const gridColor = theme === 'dark' ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.05)';
    
    // Update all charts with theme colors
    Object.values(window.portfolioCharts).forEach(chart => {
        // Update scale colors
        if (chart.options.scales) {
            Object.values(chart.options.scales).forEach(scale => {
                if (scale.ticks) {
                    scale.ticks.color = textColor;
                }
                if (scale.grid) {
                    scale.grid.color = gridColor;
                }
            });
        }
        
        // Update legend colors
        if (chart.options.plugins && chart.options.plugins.legend) {
            chart.options.plugins.legend.labels.color = textColor;
        }
        
        chart.update();
    });
}

/**
 * Update the trend chart based on selected type
 * @param {string} chartType - The type of data to display
 */
function updateTrendChart(chartType) {
    const trendChart = window.portfolioCharts.trendChart;
    
    // Hide all datasets
    trendChart.data.datasets.forEach(dataset => {
        dataset.hidden = true;
    });
    
    // Show the selected dataset
    switch(chartType) {
        case 'performance':
            trendChart.data.datasets[0].hidden = false;
            break;
        case 'resources':
            trendChart.data.datasets[1].hidden = false;
            break;
        case 'risks':
            trendChart.data.datasets[2].hidden = false;
            break;
    }
    
    trendChart.update();
}

/**
 * Update dashboard data based on time range
 * @param {string} timeRange - The selected time range
 */
function updateDashboardData(timeRange) {
    console.log(`Updating dashboard data for time range: ${timeRange}`);
    
    // Simulate loading state
    const panelHeader = document.querySelector('.panel-header h2');
    const originalText = panelHeader.textContent;
    panelHeader.textContent = 'Loading data...';
    
    // Simulate API call delay
    setTimeout(() => {
        // Update KPI values based on selected time range
        updateKPIValues(timeRange);
        
        // Update charts based on selected time range
        updateChartsData(timeRange);
        
        // Reset header text
        panelHeader.textContent = originalText;
        
        console.log(`Dashboard data updated for ${timeRange}`);
    }, 500);
}

/**
 * Update KPI values based on time range
 * @param {string} timeRange - The selected time range
 */
function updateKPIValues(timeRange) {
    // Sample data for different time ranges
    const kpiData = {
        'day': {
            totalRequirements: '2,105',
            activeProjects: '29',
            riskLevel: 'Low',
            resourceUtilization: '65%'
        },
        'week': {
            totalRequirements: '2,254',
            activeProjects: '31',
            riskLevel: 'Medium',
            resourceUtilization: '72%'
        },
        'month': {
            totalRequirements: '2,458',
            activeProjects: '34',
            riskLevel: 'Medium',
            resourceUtilization: '78%'
        },
        'quarter': {
            totalRequirements: '2,890',
            activeProjects: '38',
            riskLevel: 'Medium',
            resourceUtilization: '85%'
        },
        'year': {
            totalRequirements: '3,256',
            activeProjects: '42',
            riskLevel: 'High',
            resourceUtilization: '90%'
        }
    };
    
    // Get data for selected time range
    const data = kpiData[timeRange];
    if (!data) return;
    
    // Update KPI values
    const kpiValues = document.querySelectorAll('.kpi-value');
    kpiValues[0].textContent = data.totalRequirements;
    kpiValues[1].textContent = data.activeProjects;
    kpiValues[2].textContent = data.riskLevel;
    kpiValues[3].textContent = data.resourceUtilization;
    
    // Update trends randomly
    updateRandomTrends();
}

/**
 * Update chart data based on time range
 * @param {string} timeRange - The selected time range
 */
function updateChartsData(timeRange) {
    if (!window.portfolioCharts) return;
    
    // Sample data for requirements status chart
    const reqStatusData = {
        'day': [40, 30, 15, 10, 5],
        'week': [42, 28, 15, 10, 5],
        'month': [45, 25, 15, 10, 5],
        'quarter': [50, 20, 15, 10, 5],
        'year': [55, 15, 15, 10, 5]
    };
    
    // Sample data for strategic alignment chart
    const strategicData = {
        'day': {
            current: [80, 70, 85, 60, 75, 55],
            target: [90, 85, 95, 90, 85, 80]
        },
        'week': {
            current: [82, 71, 87, 62, 76, 57],
            target: [90, 85, 95, 90, 85, 80]
        },
        'month': {
            current: [85, 72, 90, 65, 78, 60],
            target: [90, 85, 95, 90, 85, 80]
        },
        'quarter': {
            current: [87, 75, 92, 70, 80, 65],
            target: [90, 85, 95, 90, 85, 80]
        },
        'year': {
            current: [88, 78, 94, 75, 82, 70],
            target: [95, 90, 95, 95, 90, 85]
        }
    };
    
    // Update requirements status chart
    const reqStatusChart = window.portfolioCharts.reqStatusChart;
    reqStatusChart.data.datasets[0].data = reqStatusData[timeRange] || reqStatusData['month'];
    reqStatusChart.update();
    
    // Update strategic alignment chart
    const strategicChart = window.portfolioCharts.strategicChart;
    const stratData = strategicData[timeRange] || strategicData['month'];
    strategicChart.data.datasets[0].data = stratData.current;
    strategicChart.data.datasets[1].data = stratData.target;
    strategicChart.update();
    
    // Update trend chart with randomized data
    updateTrendChartWithRandomData(timeRange);
}

/**
 * Update trend chart with randomized data based on time range
 * @param {string} timeRange - The selected time range
 */
function updateTrendChartWithRandomData(timeRange) {
    const trendChart = window.portfolioCharts.trendChart;
    
    // Generate different labels based on time range
    let labels = [];
    switch(timeRange) {
        case 'day':
            labels = ['9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM'];
            break;
        case 'week':
            labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
            break;
        case 'month':
            labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            break;
        case 'quarter':
            labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12'];
            break;
        case 'year':
            labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            break;
        default:
            labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    }
    
    // Update labels
    trendChart.data.labels = labels;
    
    // Generate random but trending data
    const performanceData = generateTrendingData(65, 90, labels.length);
    const resourceData = generateTrendingData(70, 85, labels.length);
    const riskData = generateTrendingData(45, 20, labels.length, true); // Decreasing trend for risks
    
    // Update datasets
    trendChart.data.datasets[0].data = performanceData;
    trendChart.data.datasets[1].data = resourceData;
    trendChart.data.datasets[2].data = riskData;
    
    // Update chart
    trendChart.update();
}

/**
 * Generate random but trending data
 * @param {number} start - Starting value
 * @param {number} end - Target end value
 * @param {number} count - Number of data points
 * @param {boolean} inverse - Whether trend should go down (true) or up (false)
 * @returns {Array} Array of data points
 */
function generateTrendingData(start, end, count, inverse = false) {
    const result = [];
    const trend = (end - start) / (count - 1);
    
    for (let i = 0; i < count; i++) {
        // Base value following the trend
        const baseValue = start + (trend * i);
        
        // Add some randomness (±5%)
        const randomFactor = (Math.random() * 10 - 5) / 100;
        const value = baseValue * (1 + randomFactor);
        
        // Ensure value is within reasonable bounds
        const boundedValue = Math.min(Math.max(value, 0), 100);
        
        result.push(Math.round(boundedValue));
    }
    
    return result;
}

/**
 * Update KPI trends with random values
 */
function updateRandomTrends() {
    const trends = document.querySelectorAll('.kpi-trend');
    
    trends.forEach(trend => {
        // Generate random percentage between -15% and +15%
        const randomPercent = (Math.random() * 30 - 15).toFixed(1);
        
        // Clear existing classes
        trend.classList.remove('positive', 'negative', 'neutral');
        
        // Set icon and class based on value
        if (randomPercent > 0) {
            trend.innerHTML = `<i class="fas fa-arrow-up"></i> ${randomPercent}%`;
            trend.classList.add('positive');
        } else if (randomPercent < 0) {
            trend.innerHTML = `<i class="fas fa-arrow-down"></i> ${Math.abs(randomPercent)}%`;
            trend.classList.add('negative');
        } else {
            trend.innerHTML = `<i class="fas fa-minus"></i> Stable`;
            trend.classList.add('neutral');
        }
    });
}

/**
 * Export dashboard data
 */
function exportDashboardData() {
    console.log("Exporting dashboard data...");
    
    // Create a fake download link
    const link = document.createElement('a');
    link.href = 'javascript:void(0)';
    link.download = 'portfolio_dashboard_export.csv';
    
    // Alert user
    alert('Dashboard data export initiated. The file would be downloaded in a real implementation.');
    
    // In a real implementation, this would create and download a file
    console.log("Export complete (simulated).");
}
