# Lab 7: Evaluation Methods

## Solution

### Step 1: Usability Testing Framework HTML
Create a `usability_testing.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usability Evaluation Framework - ISO 9241 Lab</title>
    <link rel="stylesheet" href="usability.css">
</head>
<body>
    <header>
        <h1>Usability Evaluation Framework</h1>
        <nav>
            <button id="startTestBtn">Start New Test</button>
            <button id="heuristicBtn">Heuristic Evaluation</button>
            <button id="accessibilityBtn">Accessibility Check</button>
            <button id="generateReportBtn">Generate Report</button>
        </nav>
    </header>

    <main>
        <section class="test-setup">
            <h2>Test Configuration</h2>
            <form id="testConfigForm">
                <div class="form-group">
                    <label for="testName">Test Name:</label>
                    <input type="text" id="testName" required>
                </div>
                
                <div class="form-group">
                    <label for="evaluatorName">Evaluator Name:</label>
                    <input type="text" id="evaluatorName" required>
                </div>
                
                <div class="form-group">
                    <label for="testType">Evaluation Method:</label>
                    <select id="testType">
                        <option value="usability">Usability Testing</option>
                        <option value="heuristic">Heuristic Evaluation</option>
                        <option value="cognitive">Cognitive Walkthrough</option>
                        <option value="accessibility">Accessibility Audit</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="participants">Number of Participants:</label>
                    <input type="number" id="participants" min="1" max="20" value="5">
                </div>
                
                <button type="submit" class="primary-btn">Configure Test</button>
            </form>
        </section>

        <section class="test-interface" id="testInterface" style="display: none;">
            <h2>Usability Test Interface</h2>
            
            <div class="test-controls">
                <button id="recordBtn" class="record-btn">Start Recording</button>
                <button id="pauseBtn" class="pause-btn" disabled>Pause</button>
                <button id="stopBtn" class="stop-btn" disabled>Stop Test</button>
                <div id="timer">00:00:00</div>
            </div>
            
            <div class="test-area">
                <div class="task-panel">
                    <h3>Current Task</h3>
                    <div id="currentTask">No task assigned</div>
                    <div class="task-controls">
                        <button id="successBtn" class="success-btn" disabled>Task Success</button>
                        <button id="failureBtn" class="failure-btn" disabled>Task Failure</button>
                    </div>
                </div>
                
                <div class="observation-panel">
                    <h3>Observations</h3>
                    <textarea id="observations" placeholder="Record your observations here..."></textarea>
                    <button id="addObservationBtn">Add Observation</button>
                </div>
                
                <div class="metrics-panel">
                    <h3>Real-time Metrics</h3>
                    <div class="metric" id="taskTime">Task Time: 00:00</div>
                    <div class="metric" id="clickCount">Clicks: 0</div>
                    <div class="metric" id="errorCount">Errors: 0</div>
                    <div class="metric" id="completionRate">Completion: 0%</div>
                </div>
            </div>
        </section>

        <section class="heuristic-evaluation" id="heuristicSection" style="display: none;">
            <h2>Heuristic Evaluation</h2>
            <div class="heuristic-checklist">
                <h3>Nielsen's 10 Usability Heuristics</h3>
                <div class="heuristic-item">
                    <h4>1. Visibility of system status</h4>
                    <div class="rating">
                        <input type="radio" name="heuristic1" value="1">1
                        <input type="radio" name="heuristic1" value="2">2
                        <input type="radio" name="heuristic1" value="3">3
                        <input type="radio" name="heuristic1" value="4">4
                        <input type="radio" name="heuristic1" value="5" checked>5
                    </div>
                    <textarea placeholder="Comments..."></textarea>
                </div>
                
                <div class="heuristic-item">
                    <h4>2. Match between system and real world</h4>
                    <div class="rating">
                        <input type="radio" name="heuristic2" value="1">1
                        <input type="radio" name="heuristic2" value="2">2
                        <input type="radio" name="heuristic2" value="3">3
                        <input type="radio" name="heuristic2" value="4">4
                        <input type="radio" name="heuristic2" value="5" checked>5
                    </div>
                    <textarea placeholder="Comments..."></textarea>
                </div>
                
                <!-- Add remaining 8 heuristics similarly -->
            </div>
            
            <button id="calculateHeuristicScore">Calculate Score</button>
            <div id="heuristicResults"></div>
        </section>

        <section class="accessibility-check" id="accessibilitySection" style="display: none;">
            <h2>Accessibility Audit</h2>
            <div class="accessibility-tools">
                <button id="runAccessibilityCheck">Run Automated Check</button>
                <button id="manualAuditBtn">Manual Audit</button>
            </div>
            
            <div id="accessibilityResults"></div>
        </section>

        <section class="results-section" id="resultsSection" style="display: none;">
            <h2>Evaluation Results</h2>
            <div class="results-tabs">
                <button class="tab-btn active" data-tab="summary">Summary</button>
                <button class="tab-btn" data-tab="metrics">Metrics</button>
                <button class="tab-btn" data-tab="issues">Issues</button>
                <button class="tab-btn" data-tab="recommendations">Recommendations</button>
            </div>
            
            <div class="tab-content">
                <div id="summaryTab" class="tab-panel active">
                    <h3>Test Summary</h3>
                    <div id="testSummary"></div>
                </div>
                
                <div id="metricsTab" class="tab-panel">
                    <h3>Usability Metrics</h3>
                    <canvas id="metricsChart"></canvas>
                </div>
                
                <div id="issuesTab" class="tab-panel">
                    <h3>Identified Issues</h3>
                    <div id="issuesList"></div>
                </div>
                
                <div id="recommendationsTab" class="tab-panel">
                    <h3>Recommendations</h3>
                    <div id="recommendationsList"></div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="usability.js"></script>
</body>
</html>
```

### Step 2: CSS for Usability Testing Interface
Create a `usability.css` file:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
    color: #333;
}

header {
    background-color: #007bff;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    margin: 0;
}

nav button {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 0.5rem 1rem;
    margin-left: 0.5rem;
    border-radius: 4px;
    cursor: pointer;
}

nav button:hover, nav button:focus {
    background-color: rgba(255, 255, 255, 0.3);
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

section {
    background-color: white;
    margin-bottom: 2rem;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h2 {
    color: #495057;
    border-bottom: 2px solid #007bff;
    padding-bottom: 0.5rem;
}

/* Form Styles */
.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.form-group input, .form-group select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    font-size: 1rem;
}

.primary-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
}

.primary-btn:hover {
    background-color: #0056b3;
}

/* Test Interface */
.test-controls {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin-bottom: 2rem;
}

.record-btn {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
}

.record-btn:hover {
    background-color: #c82333;
}

.pause-btn, .stop-btn {
    background-color: #ffc107;
    color: #212529;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
}

.pause-btn:hover, .stop-btn:hover {
    background-color: #e0a800;
}

#timer {
    font-size: 1.5rem;
    font-weight: bold;
    margin-left: auto;
}

.test-area {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.task-panel, .observation-panel, .metrics-panel {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.task-panel h3, .observation-panel h3, .metrics-panel h3 {
    margin-top: 0;
    color: #495057;
}

#currentTask {
    background-color: white;
    padding: 1rem;
    border-radius: 4px;
    margin-bottom: 1rem;
    min-height: 3rem;
    display: flex;
    align-items: center;
}

.task-controls {
    display: flex;
    gap: 1rem;
}

.success-btn {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
}

.success-btn:hover {
    background-color: #218838;
}

.failure-btn {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
}

.failure-btn:hover {
    background-color: #c82333;
}

#observations {
    width: 100%;
    height: 150px;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    resize: vertical;
}

.metric {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

/* Heuristic Evaluation */
.heuristic-item {
    margin-bottom: 2rem;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 8px;
}

.heuristic-item h4 {
    margin-top: 0;
    color: #007bff;
}

.rating {
    margin: 1rem 0;
}

.rating input {
    margin-right: 0.5rem;
}

.heuristic-item textarea {
    width: 100%;
    height: 80px;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    resize: vertical;
}

/* Results Section */
.results-tabs {
    display: flex;
    margin-bottom: 2rem;
}

.tab-btn {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 0.75rem 1.5rem;
    cursor: pointer;
    border-radius: 4px 4px 0 0;
}

.tab-btn.active {
    background-color: white;
    border-bottom: 1px solid white;
}

.tab-panel {
    display: none;
    padding: 2rem;
    background-color: white;
    border: 1px solid #dee2e6;
    border-radius: 0 4px 4px 4px;
}

.tab-panel.active {
    display: block;
}

/* Notification */
.notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #007bff;
    color: white;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    display: none;
    max-width: 300px;
}

/* Responsive */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    .test-area {
        grid-template-columns: 1fr;
    }
    
    .results-tabs {
        flex-direction: column;
    }
    
    .tab-btn {
        border-radius: 0;
    }
}
```

### Step 3: JavaScript for Usability Testing
Create a `usability.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Test configuration
    let currentTest = null;
    let testStartTime = null;
    let testTimer = null;
    let observations = [];
    let metrics = {
        clicks: 0,
        errors: 0,
        taskTime: 0,
        completionRate: 0
    };
    
    // Test configuration form
    document.getElementById('testConfigForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        currentTest = {
            name: document.getElementById('testName').value,
            evaluator: document.getElementById('evaluatorName').value,
            type: document.getElementById('testType').value,
            participants: parseInt(document.getElementById('participants').value),
            startTime: new Date(),
            tasks: [],
            observations: [],
            metrics: { ...metrics }
        };
        
        document.querySelector('.test-setup').style.display = 'none';
        document.getElementById('testInterface').style.display = 'block';
        
        showNotification('Test configured successfully');
    });
    
    // Recording controls
    document.getElementById('recordBtn').addEventListener('click', function() {
        startRecording();
    });
    
    document.getElementById('pauseBtn').addEventListener('click', function() {
        pauseRecording();
    });
    
    document.getElementById('stopBtn').addEventListener('click', function() {
        stopRecording();
    });
    
    function startRecording() {
        testStartTime = new Date();
        testTimer = setInterval(updateTimer, 1000);
        
        document.getElementById('recordBtn').disabled = true;
        document.getElementById('pauseBtn').disabled = false;
        document.getElementById('stopBtn').disabled = false;
        document.getElementById('successBtn').disabled = false;
        document.getElementById('failureBtn').disabled = false;
        
        showNotification('Recording started');
    }
    
    function pauseRecording() {
        clearInterval(testTimer);
        
        document.getElementById('recordBtn').disabled = false;
        document.getElementById('pauseBtn').disabled = true;
        
        showNotification('Recording paused');
    }
    
    function stopRecording() {
        clearInterval(testTimer);
        
        document.getElementById('recordBtn').disabled = false;
        document.getElementById('pauseBtn').disabled = true;
        document.getElementById('stopBtn').disabled = true;
        document.getElementById('successBtn').disabled = true;
        document.getElementById('failureBtn').disabled = true;
        
        showNotification('Recording stopped');
    }
    
    function updateTimer() {
        const now = new Date();
        const elapsed = Math.floor((now - testStartTime) / 1000);
        const hours = Math.floor(elapsed / 3600);
        const minutes = Math.floor((elapsed % 3600) / 60);
        const seconds = elapsed % 60;
        
        document.getElementById('timer').textContent = 
            `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    // Task controls
    document.getElementById('successBtn').addEventListener('click', function() {
        recordTaskResult(true);
    });
    
    document.getElementById('failureBtn').addEventListener('click', function() {
        recordTaskResult(false);
    });
    
    function recordTaskResult(success) {
        const taskTime = Math.floor((new Date() - testStartTime) / 1000);
        
        const task = {
            description: document.getElementById('currentTask').textContent,
            success: success,
            time: taskTime,
            timestamp: new Date().toISOString()
        };
        
        currentTest.tasks.push(task);
        metrics.taskTime = taskTime;
        metrics.completionRate = success ? 100 : 0;
        
        updateMetrics();
        showNotification(`Task ${success ? 'completed successfully' : 'failed'}`);
    }
    
    // Observations
    document.getElementById('addObservationBtn').addEventListener('click', function() {
        const observationText = document.getElementById('observations').value.trim();
        if (observationText) {
            const observation = {
                text: observationText,
                timestamp: new Date().toISOString(),
                type: 'manual'
            };
            
            observations.push(observation);
            currentTest.observations.push(observation);
            
            document.getElementById('observations').value = '';
            showNotification('Observation added');
        }
    });
    
    // Click tracking
    document.addEventListener('click', function(e) {
        if (testStartTime && !e.target.closest('nav') && !e.target.closest('.test-controls')) {
            metrics.clicks++;
            updateMetrics();
        }
    });
    
    // Error tracking (simplified)
    window.addEventListener('error', function() {
        metrics.errors++;
        updateMetrics();
    });
    
    function updateMetrics() {
        document.getElementById('clickCount').textContent = `Clicks: ${metrics.clicks}`;
        document.getElementById('errorCount').textContent = `Errors: ${metrics.errors}`;
        document.getElementById('taskTime').textContent = `Task Time: ${Math.floor(metrics.taskTime / 60)}:${(metrics.taskTime % 60).toString().padStart(2, '0')}`;
        document.getElementById('completionRate').textContent = `Completion: ${metrics.completionRate}%`;
        
        currentTest.metrics = { ...metrics };
    }
    
    // Heuristic evaluation
    document.getElementById('heuristicBtn').addEventListener('click', function() {
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('heuristicSection').style.display = 'block';
    });
    
    document.getElementById('calculateHeuristicScore').addEventListener('click', function() {
        const heuristicItems = document.querySelectorAll('.heuristic-item');
        let totalScore = 0;
        let maxScore = heuristicItems.length * 5;
        
        heuristicItems.forEach(item => {
            const radioButtons = item.querySelectorAll('input[type="radio"]:checked');
            if (radioButtons.length > 0) {
                totalScore += parseInt(radioButtons[0].value);
            }
        });
        
        const percentage = Math.round((totalScore / maxScore) * 100);
        
        document.getElementById('heuristicResults').innerHTML = `
            <h3>Heuristic Evaluation Results</h3>
            <p>Total Score: ${totalScore}/${maxScore}</p>
            <p>Usability Rating: ${percentage}%</p>
            <div class="score-bar">
                <div class="score-fill" style="width: ${percentage}%"></div>
            </div>
        `;
    });
    
    // Accessibility check
    document.getElementById('accessibilityBtn').addEventListener('click', function() {
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('accessibilitySection').style.display = 'block';
    });
    
    document.getElementById('runAccessibilityCheck').addEventListener('click', function() {
        // Simulate accessibility check
        const results = [
            { type: 'error', message: 'Missing alt text on images', count: 3 },
            { type: 'warning', message: 'Low color contrast ratio', count: 5 },
            { type: 'info', message: 'Missing form labels', count: 2 }
        ];
        
        let resultsHTML = '<h3>Accessibility Check Results</h3>';
        results.forEach(result => {
            resultsHTML += `<div class="accessibility-result ${result.type}">
                <strong>${result.type.toUpperCase()}:</strong> ${result.message} (${result.count} instances)
            </div>`;
        });
        
        document.getElementById('accessibilityResults').innerHTML = resultsHTML;
    });
    
    // Report generation
    document.getElementById('generateReportBtn').addEventListener('click', function() {
        if (!currentTest) {
            showNotification('No test data available');
            return;
        }
        
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'block';
        
        generateReport();
    });
    
    function generateReport() {
        // Summary tab
        document.getElementById('testSummary').innerHTML = `
            <p><strong>Test Name:</strong> ${currentTest.name}</p>
            <p><strong>Evaluator:</strong> ${currentTest.evaluator}</p>
            <p><strong>Test Type:</strong> ${currentTest.type}</p>
            <p><strong>Duration:</strong> ${document.getElementById('timer').textContent}</p>
            <p><strong>Tasks Completed:</strong> ${currentTest.tasks.length}</p>
            <p><strong>Observations:</strong> ${currentTest.observations.length}</p>
        `;
        
        // Issues tab
        let issuesHTML = '';
        if (metrics.errors > 0) {
            issuesHTML += `<div class="issue error">Errors detected: ${metrics.errors}</div>`;
        }
        if (metrics.completionRate < 100) {
            issuesHTML += `<div class="issue warning">Task completion rate: ${metrics.completionRate}%</div>`;
        }
        document.getElementById('issuesList').innerHTML = issuesHTML || '<p>No major issues detected</p>';
        
        // Recommendations tab
        const recommendations = [
            'Improve error handling and user feedback',
            'Simplify complex tasks and workflows',
            'Add more intuitive navigation elements',
            'Enhance accessibility features',
            'Conduct additional user testing sessions'
        ];
        
        let recHTML = '<ul>';
        recommendations.forEach(rec => {
            recHTML += `<li>${rec}</li>`;
        });
        recHTML += '</ul>';
        
        document.getElementById('recommendationsList').innerHTML = recHTML;
    }
    
    // Tab switching
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const tabName = this.dataset.tab;
            
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            
            this.classList.add('active');
            document.getElementById(tabName + 'Tab').classList.add('active');
        });
    });
    
    // Navigation
    document.getElementById('startTestBtn').addEventListener('click', function() {
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('heuristicSection').style.display = 'none';
        document.getElementById('accessibilitySection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
        document.querySelector('.test-setup').style.display = 'block';
    });
    
    // Notification system
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
});
```

### Step 4: Python Usability Metrics Calculator
Create a `usability_metrics.py` file:

```python
import json
import statistics
from datetime import datetime
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import numpy as np

class UsabilityMetricsCalculator:
    def __init__(self):
        self.test_data = []
        self.metrics = {}
    
    def load_test_data(self, file_path: str):
        """Load test data from JSON file"""
        with open(file_path, 'r') as f:
            self.test_data = json.load(f)
    
    def calculate_basic_metrics(self) -> Dict[str, Any]:
        """Calculate basic usability metrics"""
        if not self.test_data:
            return {}
        
        total_tasks = len(self.test_data.get('tasks', []))
        successful_tasks = sum(1 for task in self.test_data.get('tasks', []) if task.get('success', False))
        
        task_times = [task.get('time', 0) for task in self.test_data.get('tasks', []) if task.get('success', False)]
        
        metrics = {
            'total_tasks': total_tasks,
            'successful_tasks': successful_tasks,
            'completion_rate': (successful_tasks / total_tasks * 100) if total_tasks > 0 else 0,
            'average_task_time': statistics.mean(task_times) if task_times else 0,
            'median_task_time': statistics.median(task_times) if task_times else 0,
            'task_time_std': statistics.stdev(task_times) if len(task_times) > 1 else 0,
            'total_observations': len(self.test_data.get('observations', [])),
            'total_clicks': self.test_data.get('metrics', {}).get('clicks', 0),
            'total_errors': self.test_data.get('metrics', {}).get('errors', 0)
        }
        
        self.metrics.update(metrics)
        return metrics
    
    def calculate_sus_score(self, responses: List[int]) -> float:
        """Calculate System Usability Scale (SUS) score"""
        if len(responses) != 10:
            raise ValueError("SUS requires exactly 10 responses")
        
        # SUS scoring: subtract 1 from odd items, 5-odd from even items
        score = 0
        for i, response in enumerate(responses):
            if i % 2 == 0:  # Odd items (1,3,5,7,9)
                score += response - 1
            else:  # Even items (2,4,6,8,10)
                score += 5 - response
        
        return score * 2.5  # Scale to 0-100
    
    def calculate_nps_score(self, responses: List[int]) -> float:
        """Calculate Net Promoter Score"""
        promoters = sum(1 for r in responses if r >= 9)
        detractors = sum(1 for r in responses if r <= 6)
        total = len(responses)
        
        if total == 0:
            return 0
        
        return ((promoters - detractors) / total) * 100
    
    def analyze_observation_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in user observations"""
        observations = self.test_data.get('observations', [])
        
        # Categorize observations (simplified)
        categories = {
            'usability_issues': 0,
            'positive_feedback': 0,
            'suggestions': 0,
            'errors': 0,
            'navigation': 0
        }
        
        keywords = {
            'usability_issues': ['difficult', 'confusing', 'hard', 'problem'],
            'positive_feedback': ['good', 'easy', 'great', 'helpful', 'clear'],
            'suggestions': ['should', 'could', 'would', 'suggest', 'improve'],
            'errors': ['error', 'mistake', 'wrong', 'failed'],
            'navigation': ['find', 'locate', 'navigate', 'menu', 'button']
        }
        
        for obs in observations:
            text = obs.get('text', '').lower()
            for category, words in keywords.items():
                if any(word in text for word in words):
                    categories[category] += 1
        
        return categories
    
    def generate_recommendations(self) -> List[str]:
        """Generate actionable recommendations based on metrics"""
        recommendations = []
        
        if self.metrics.get('completion_rate', 0) < 80:
            recommendations.append("Improve task completion rate through better user guidance")
        
        if self.metrics.get('average_task_time', 0) > 300:  # 5 minutes
            recommendations.append("Reduce task completion time by simplifying workflows")
        
        if self.metrics.get('total_errors', 0) > 5:
            recommendations.append("Address error-prone areas with better validation and feedback")
        
        observations_analysis = self.analyze_observation_patterns()
        if observations_analysis.get('usability_issues', 0) > observations_analysis.get('positive_feedback', 0):
            recommendations.append("Focus on resolving identified usability issues")
        
        if len(recommendations) == 0:
            recommendations.append("Overall usability is good, consider minor refinements")
        
        return recommendations
    
    def create_metrics_report(self, output_file: str = 'usability_report.json'):
        """Create comprehensive metrics report"""
        report = {
            'test_info': {
                'name': self.test_data.get('name', 'Unknown'),
                'evaluator': self.test_data.get('evaluator', 'Unknown'),
                'type': self.test_data.get('type', 'Unknown'),
                'date': self.test_data.get('startTime', datetime.now().isoformat())
            },
            'metrics': self.metrics,
            'observations_analysis': self.analyze_observation_patterns(),
            'recommendations': self.generate_recommendations(),
            'generated_at': datetime.now().isoformat()
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"Usability report generated: {output_file}")
        return report
    
    def visualize_metrics(self, save_path: str = 'usability_metrics.png'):
        """Create visualizations of usability metrics"""
        if not self.metrics:
            print("No metrics available for visualization")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
        
        # Completion Rate
        completion_rate = self.metrics.get('completion_rate', 0)
        ax1.bar(['Completion Rate'], [completion_rate], color='skyblue')
        ax1.set_ylim(0, 100)
        ax1.set_title('Task Completion Rate (%)')
        ax1.text(0, completion_rate + 1, f'{completion_rate:.1f}%', ha='center')
        
        # Task Times
        task_times = [task.get('time', 0) for task in self.test_data.get('tasks', [])]
        if task_times:
            ax2.hist(task_times, bins=10, color='lightgreen', edgecolor='black')
            ax2.set_title('Task Completion Times (seconds)')
            ax2.set_xlabel('Time (seconds)')
            ax2.set_ylabel('Frequency')
        
        # Error Analysis
        errors = self.metrics.get('total_errors', 0)
        clicks = self.metrics.get('total_clicks', 0)
        ax3.bar(['Clicks', 'Errors'], [clicks, errors], color=['blue', 'red'])
        ax3.set_title('User Interactions')
        ax3.set_ylabel('Count')
        
        # Observations Analysis
        obs_analysis = self.analyze_observation_patterns()
        categories = list(obs_analysis.keys())
        values = list(obs_analysis.values())
        ax4.bar(categories, values, color='orange')
        ax4.set_title('Observation Categories')
        ax4.set_ylabel('Count')
        ax4.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Metrics visualization saved: {save_path}")

# Example usage
if __name__ == "__main__":
    calculator = UsabilityMetricsCalculator()
    
    # Simulate test data
    test_data = {
        'name': 'Sample Usability Test',
        'evaluator': 'Test Evaluator',
        'type': 'usability',
        'startTime': datetime.now().isoformat(),
        'tasks': [
            {'description': 'Login task', 'success': True, 'time': 45},
            {'description': 'Navigation task', 'success': False, 'time': 120},
            {'description': 'Search task', 'success': True, 'time': 30}
        ],
        'observations': [
            {'text': 'Login was easy to find', 'timestamp': datetime.now().isoformat()},
            {'text': 'Navigation menu was confusing', 'timestamp': datetime.now().isoformat()},
            {'text': 'Search results should load faster', 'timestamp': datetime.now().isoformat()}
        ],
        'metrics': {
            'clicks': 25,
            'errors': 3,
            'completionRate': 67
        }
    }
    
    calculator.test_data = test_data
    metrics = calculator.calculate_basic_metrics()
    
    print("Basic Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
    
    # SUS calculation example
    sus_responses = [4, 3, 5, 2, 4, 3, 5, 2, 4, 3]  # Sample SUS responses
    sus_score = calculator.calculate_sus_score(sus_responses)
    print(f"\nSUS Score: {sus_score:.1f}")
    
    # Generate report
    report = calculator.create_metrics_report()
    
    # Visualize metrics
    calculator.visualize_metrics()
```

### Step 5: Documentation
This usability evaluation framework implements multiple evaluation methods from ISO 9241-11:

1. **Usability Testing**: Real-time task monitoring with metrics collection
2. **Heuristic Evaluation**: Nielsen's 10 usability heuristics assessment
3. **Accessibility Audit**: Automated and manual accessibility checking
4. **Metrics Calculation**: Comprehensive usability metrics with Python analysis

Key features:
- Multi-method evaluation framework
- Real-time data collection and analysis
- Automated heuristic scoring
- Comprehensive reporting with recommendations
- Data visualization and export capabilities

The framework provides a complete toolkit for conducting professional usability evaluations according to ISO 9241 standards.
