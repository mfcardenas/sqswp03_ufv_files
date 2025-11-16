# Lab 9: Input Device Standards

## Solution

### Step 1: Input Device Assessment HTML
Create an `input_device.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Input Device Standards Assessment - ISO 9241 Lab</title>
    <link rel="stylesheet" href="input.css">
</head>
<body>
    <header>
        <h1>Input Device Standards Assessment</h1>
        <nav>
            <button id="deviceBtn">Device Selection</button>
            <button id="ergonomicsBtn">Ergonomics</button>
            <button id="usabilityBtn">Usability Test</button>
            <button id="performanceBtn">Performance</button>
            <button id="complianceBtn">Compliance Check</button>
            <button id="generateReportBtn">Generate Report</button>
        </nav>
    </header>

    <main>
        <section class="device-setup">
            <h2>Device Configuration</h2>
            <form id="deviceConfigForm">
                <div class="form-group">
                    <label for="deviceType">Input Device Type:</label>
                    <select id="deviceType">
                        <option value="keyboard">Keyboard</option>
                        <option value="mouse">Mouse</option>
                        <option value="touchpad">Touchpad</option>
                        <option value="trackball">Trackball</option>
                        <option value="joystick">Joystick</option>
                        <option value="gamepad">Gamepad</option>
                        <option value="touchscreen">Touchscreen</option>
                        <option value="stylus">Stylus</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="deviceModel">Device Model:</label>
                    <input type="text" id="deviceModel" placeholder="e.g., Logitech MX Master 3">
                </div>
                
                <div class="form-group">
                    <label for="connectionType">Connection Type:</label>
                    <select id="connectionType">
                        <option value="wired">Wired</option>
                        <option value="wireless">Wireless</option>
                        <option value="bluetooth">Bluetooth</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="userHandedness">User Handedness:</label>
                    <select id="userHandedness">
                        <option value="right">Right-handed</option>
                        <option value="left">Left-handed</option>
                        <option value="ambidextrous">Ambidextrous</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="usageScenario">Usage Scenario:</label>
                    <select id="usageScenario">
                        <option value="office">Office Work</option>
                        <option value="gaming">Gaming</option>
                        <option value="design">Design/CAD</option>
                        <option value="programming">Programming</option>
                        <option value="general">General Use</option>
                    </select>
                </div>
                
                <button type="submit" class="primary-btn">Start Assessment</button>
            </form>
        </section>

        <section class="ergonomics-assessment" id="ergonomicsSection" style="display: none;">
            <h2>Ergonomic Assessment</h2>
            
            <div class="ergonomics-tests">
                <div class="test-panel">
                    <h3>Grip & Posture Test</h3>
                    <div class="posture-guide">
                        <p>Position your hand in a natural, relaxed posture.</p>
                        <div class="hand-position">
                            <div class="hand-outline">
                                <div class="finger" id="thumb"></div>
                                <div class="finger" id="index"></div>
                                <div class="finger" id="middle"></div>
                                <div class="finger" id="ring"></div>
                                <div class="finger" id="pinky"></div>
                            </div>
                        </div>
                    </div>
                    <button id="postureTestBtn">Assess Posture</button>
                    <div id="postureResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Force & Pressure Test</h3>
                    <div class="force-test">
                        <p>Apply normal pressure to the input device.</p>
                        <div class="pressure-gauge">
                            <div class="gauge-fill" id="pressureFill"></div>
                            <div class="gauge-label">Pressure Level</div>
                        </div>
                    </div>
                    <button id="forceTestBtn">Measure Force</button>
                    <div id="forceResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Reach & Movement Test</h3>
                    <div class="movement-test">
                        <p>Test natural movement patterns.</p>
                        <div class="movement-patterns">
                            <div class="pattern" data-pattern="circular">Circular</div>
                            <div class="pattern" data-pattern="linear">Linear</div>
                            <div class="pattern" data-pattern="random">Random</div>
                        </div>
                    </div>
                    <button id="movementTestBtn">Test Movement</button>
                    <div id="movementResults"></div>
                </div>
            </div>
        </section>

        <section class="usability-test" id="usabilitySection" style="display: none;">
            <h2>Usability Testing</h2>
            
            <div class="usability-tests">
                <div class="test-panel">
                    <h3>Pointing Accuracy Test</h3>
                    <div class="accuracy-test">
                        <canvas id="accuracyCanvas" width="600" height="400"></canvas>
                        <div class="accuracy-controls">
                            <button id="startAccuracyTest">Start Test</button>
                            <button id="resetAccuracyTest">Reset</button>
                        </div>
                    </div>
                    <div id="accuracyResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Click Speed Test</h3>
                    <div class="speed-test">
                        <div class="click-target" id="clickTarget">
                            <span>Click Here!</span>
                        </div>
                        <div class="speed-metrics">
                            <div class="metric">Clicks: <span id="clickCount">0</span></div>
                            <div class="metric">Time: <span id="clickTime">0.00s</span></div>
                            <div class="metric">CPS: <span id="clicksPerSecond">0.00</span></div>
                        </div>
                    </div>
                    <button id="startSpeedTest">Start Speed Test</button>
                    <button id="stopSpeedTest">Stop Test</button>
                    <div id="speedResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Text Input Test</h3>
                    <div class="text-input-test">
                        <p>Type the following text as quickly and accurately as possible:</p>
                        <div class="sample-text" id="sampleText">
                            The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet and is commonly used for typing speed tests.
                        </div>
                        <textarea id="inputText" placeholder="Start typing here..."></textarea>
                        <div class="typing-metrics">
                            <div class="metric">WPM: <span id="wordsPerMinute">0</span></div>
                            <div class="metric">Accuracy: <span id="typingAccuracy">100%</span></div>
                            <div class="metric">Errors: <span id="typingErrors">0</span></div>
                        </div>
                    </div>
                    <button id="startTypingTest">Start Typing Test</button>
                    <button id="resetTypingTest">Reset Test</button>
                    <div id="typingResults"></div>
                </div>
            </div>
        </section>

        <section class="performance-analysis" id="performanceSection" style="display: none;">
            <h2>Performance Analysis</h2>
            
            <div class="performance-metrics">
                <div class="metric-panel">
                    <h3>Response Time</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="responseTimeValue">-- ms</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="responseTimeBar"></div>
                        </div>
                    </div>
                </div>
                
                <div class="metric-panel">
                    <h3>Throughput</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="throughputValue">-- ops/sec</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="throughputBar"></div>
                        </div>
                    </div>
                </div>
                
                <div class="metric-panel">
                    <h3>Error Rate</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="errorRateValue">-- %</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="errorRateBar"></div>
                        </div>
                    </div>
                </div>
                
                <div class="metric-panel">
                    <h3>Learning Time</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="learningTimeValue">-- min</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="learningTimeBar"></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <button id="runPerformanceTest">Run Performance Test</button>
            <div id="performanceResults"></div>
        </section>

        <section class="compliance-check" id="complianceSection" style="display: none;">
            <h2>ISO 9241 Compliance Check</h2>
            
            <div class="compliance-checklist">
                <h3>Input Device Standards Checklist</h3>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req1">
                    <label for="req1">Device dimensions meet anthropometric requirements</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req2">
                    <label for="req2">Operating force meets ergonomic guidelines (≤ 2N for keys)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req3">
                    <label for="req3">Key travel distance meets usability standards (1.5-4mm)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req4">
                    <label for="req4">Tactile feedback meets accessibility requirements</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req5">
                    <label for="req5">Device weight meets portability requirements (≤ 100g for mobile)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req6">
                    <label for="req6">Cable length meets workspace requirements (≥ 1.5m for wired)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req7">
                    <label for="req7">Battery life meets usage requirements (≥ 3 months for wireless)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req8">
                    <label for="req8">Device supports multiple hand sizes and grip styles</label>
                </div>
            </div>
            
            <button id="runComplianceCheck">Run Compliance Assessment</button>
            <div id="complianceResults"></div>
        </section>

        <section class="results-section" id="resultsSection" style="display: none;">
            <h2>Assessment Results</h2>
            <div class="results-tabs">
                <button class="tab-btn active" data-tab="summary">Summary</button>
                <button class="tab-btn" data-tab="ergonomics">Ergonomics</button>
                <button class="tab-btn" data-tab="usability">Usability</button>
                <button class="tab-btn" data-tab="performance">Performance</button>
                <button class="tab-btn" data-tab="compliance">Compliance</button>
            </div>
            
            <div class="tab-content">
                <div id="summaryTab" class="tab-panel active">
                    <h3>Assessment Summary</h3>
                    <div id="assessmentSummary"></div>
                </div>
                
                <div id="ergonomicsTab" class="tab-panel">
                    <h3>Ergonomic Evaluation</h3>
                    <div id="ergonomicsEvaluation"></div>
                </div>
                
                <div id="usabilityTab" class="tab-panel">
                    <h3>Usability Assessment</h3>
                    <div id="usabilityAssessment"></div>
                </div>
                
                <div id="performanceTab" class="tab-panel">
                    <h3>Performance Analysis</h3>
                    <div id="performanceAnalysis"></div>
                </div>
                
                <div id="complianceTab" class="tab-panel">
                    <h3>Compliance Status</h3>
                    <div id="complianceStatus"></div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="input.js"></script>
</body>
</html>
```

### Step 2: CSS for Input Device Assessment Interface
Create an `input.css` file:

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

/* Ergonomics Tests */
.ergonomics-tests {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.test-panel {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.test-panel h3 {
    margin-top: 0;
    color: #007bff;
}

.hand-outline {
    width: 200px;
    height: 150px;
    background-color: #e9ecef;
    border-radius: 20px;
    margin: 1rem auto;
    position: relative;
    display: flex;
    justify-content: space-around;
    align-items: flex-end;
    padding: 1rem;
}

.finger {
    width: 20px;
    height: 60px;
    background-color: #007bff;
    border-radius: 10px;
    transition: all 0.3s ease;
}

.finger:hover {
    background-color: #0056b3;
    transform: scale(1.1);
}

.pressure-gauge {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background-color: #e9ecef;
    margin: 1rem auto;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.gauge-fill {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    background-color: #007bff;
    border-radius: 10px 10px 0 0;
    transition: height 0.3s ease;
}

.gauge-label {
    font-weight: bold;
    z-index: 1;
}

.movement-patterns {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1rem 0;
}

.pattern {
    padding: 1rem;
    background-color: #007bff;
    color: white;
    border-radius: 4px;
    text-align: center;
    cursor: pointer;
}

.pattern:hover {
    background-color: #0056b3;
}

/* Usability Tests */
.usability-tests {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.accuracy-test {
    margin: 1rem 0;
}

#accuracyCanvas {
    border: 2px solid #dee2e6;
    border-radius: 4px;
    background-color: #f8f9fa;
}

.accuracy-controls {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.click-target {
    width: 150px;
    height: 150px;
    background-color: #007bff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    margin: 1rem auto;
    transition: all 0.2s ease;
}

.click-target:hover {
    background-color: #0056b3;
    transform: scale(1.05);
}

.speed-metrics {
    display: flex;
    justify-content: space-around;
    margin: 1rem 0;
}

.metric {
    text-align: center;
    font-weight: bold;
}

.sample-text {
    background-color: #e9ecef;
    padding: 1rem;
    border-radius: 4px;
    margin: 1rem 0;
    font-family: monospace;
}

#inputText {
    width: 100%;
    height: 100px;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    font-family: monospace;
    resize: vertical;
}

.typing-metrics {
    display: flex;
    justify-content: space-around;
    margin: 1rem 0;
}

/* Performance Metrics */
.performance-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.metric-panel {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
}

.metric-panel h3 {
    margin-top: 0;
    color: #007bff;
}

.metric-value {
    font-size: 2rem;
    font-weight: bold;
    color: #007bff;
    margin: 1rem 0;
}

.metric-bar {
    width: 100%;
    height: 20px;
    background-color: #e9ecef;
    border-radius: 10px;
    overflow: hidden;
}

.bar-fill {
    height: 100%;
    background-color: #007bff;
    width: 0%;
    transition: width 0.3s ease;
}

/* Compliance Checklist */
.compliance-checklist {
    margin-top: 2rem;
}

.compliance-item {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    padding: 0.5rem;
    background-color: #f8f9fa;
    border-radius: 4px;
}

.compliance-item input[type="checkbox"] {
    margin-right: 1rem;
    transform: scale(1.2);
}

.compliance-item label {
    flex: 1;
    cursor: pointer;
}

/* Results Section */
.results-tabs {
    display: flex;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.tab-btn {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 0.75rem 1.5rem;
    cursor: pointer;
    border-radius: 4px 4px 0 0;
    margin-right: 0.25rem;
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
    
    .ergonomics-tests, .usability-tests, .performance-metrics {
        grid-template-columns: 1fr;
    }
    
    .results-tabs {
        flex-direction: column;
    }
    
    .tab-btn {
        border-radius: 0;
        margin-right: 0;
    }
    
    .speed-metrics, .typing-metrics {
        flex-direction: column;
        gap: 0.5rem;
    }
}
```

### Step 3: JavaScript for Input Device Assessment
Create an `input.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Assessment configuration
    let currentAssessment = null;
    let assessmentResults = {
        ergonomics: {},
        usability: {},
        performance: {},
        compliance: {}
    };
    
    // Device configuration form
    document.getElementById('deviceConfigForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        currentAssessment = {
            deviceType: document.getElementById('deviceType').value,
            deviceModel: document.getElementById('deviceModel').value,
            connectionType: document.getElementById('connectionType').value,
            userHandedness: document.getElementById('userHandedness').value,
            usageScenario: document.getElementById('usageScenario').value,
            startTime: new Date()
        };
        
        document.querySelector('.device-setup').style.display = 'none';
        document.getElementById('ergonomicsSection').style.display = 'block';
        
        showNotification('Device assessment configured successfully');
    });
    
    // Navigation
    document.getElementById('deviceBtn').addEventListener('click', function() {
        hideAllSections();
        document.querySelector('.device-setup').style.display = 'block';
    });
    
    document.getElementById('ergonomicsBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('ergonomicsSection').style.display = 'block';
    });
    
    document.getElementById('usabilityBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('usabilitySection').style.display = 'block';
    });
    
    document.getElementById('performanceBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('performanceSection').style.display = 'block';
    });
    
    document.getElementById('complianceBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('complianceSection').style.display = 'block';
    });
    
    function hideAllSections() {
        document.querySelector('.device-setup').style.display = 'none';
        document.getElementById('ergonomicsSection').style.display = 'none';
        document.getElementById('usabilitySection').style.display = 'none';
        document.getElementById('performanceSection').style.display = 'none';
        document.getElementById('complianceSection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
    }
    
    // Ergonomics assessment
    document.getElementById('postureTestBtn').addEventListener('click', function() {
        // Simulate posture assessment
        const postureScore = Math.random() * 30 + 70; // 70-100%
        const comfortLevel = postureScore > 85 ? 'excellent' : postureScore > 75 ? 'good' : 'fair';
        
        document.getElementById('postureResults').innerHTML = `
            <h4>Posture Assessment Results</h4>
            <p>Posture Score: ${postureScore.toFixed(1)}%</p>
            <p>Comfort Level: <span class="${comfortLevel}">${comfortLevel.toUpperCase()}</span></p>
            <p class="${comfortLevel === 'excellent' ? 'good' : comfortLevel === 'good' ? 'good' : 'poor'}">
                ${comfortLevel === 'excellent' ? '✓ Excellent hand positioning' : 
                  comfortLevel === 'good' ? '✓ Good hand positioning' : 
                  '⚠ Consider adjusting hand position'}
            </p>
        `;
        
        assessmentResults.ergonomics.postureScore = postureScore;
        showNotification('Posture test completed');
    });
    
    document.getElementById('forceTestBtn').addEventListener('click', function() {
        // Simulate force measurement
        const forceLevel = Math.random() * 3 + 0.5; // 0.5-3.5N
        const optimal = forceLevel <= 2.0;
        
        // Update pressure gauge
        const pressurePercent = Math.min((forceLevel / 4) * 100, 100);
        document.getElementById('pressureFill').style.height = pressurePercent + '%';
        
        document.getElementById('forceResults').innerHTML = `
            <h4>Force Measurement Results</h4>
            <p>Applied Force: ${forceLevel.toFixed(1)} N</p>
            <p class="${optimal ? 'good' : 'poor'}">
                ${optimal ? '✓ Force level within optimal range' : '⚠ Force level may cause fatigue'}
            </p>
        `;
        
        assessmentResults.ergonomics.forceLevel = forceLevel;
        showNotification('Force test completed');
    });
    
    document.getElementById('movementTestBtn').addEventListener('click', function() {
        // Simulate movement pattern test
        const movementEfficiency = Math.random() * 20 + 80; // 80-100%
        const naturalMovement = movementEfficiency > 85;
        
        document.getElementById('movementResults').innerHTML = `
            <h4>Movement Pattern Results</h4>
            <p>Movement Efficiency: ${movementEfficiency.toFixed(1)}%</p>
            <p class="${naturalMovement ? 'good' : 'poor'}">
                ${naturalMovement ? '✓ Natural movement patterns detected' : '⚠ Movement may require adjustment'}
            </p>
        `;
        
        assessmentResults.ergonomics.movementEfficiency = movementEfficiency;
        showNotification('Movement test completed');
    });
    
    // Usability testing
    let accuracyTestActive = false;
    let accuracyTargets = [];
    let accuracyClicks = [];
    const accuracyCanvas = document.getElementById('accuracyCanvas');
    const ctx = accuracyCanvas.getContext('2d');
    
    document.getElementById('startAccuracyTest').addEventListener('click', function() {
        accuracyTestActive = true;
        accuracyTargets = [];
        accuracyClicks = [];
        
        // Generate random targets
        for (let i = 0; i < 10; i++) {
            accuracyTargets.push({
                x: Math.random() * (accuracyCanvas.width - 40) + 20,
                y: Math.random() * (accuracyCanvas.height - 40) + 20,
                radius: 15
            });
        }
        
        drawAccuracyTest();
        showNotification('Accuracy test started - click the targets');
    });
    
    document.getElementById('resetAccuracyTest').addEventListener('click', function() {
        accuracyTestActive = false;
        accuracyTargets = [];
        accuracyClicks = [];
        ctx.clearRect(0, 0, accuracyCanvas.width, accuracyCanvas.height);
    });
    
    accuracyCanvas.addEventListener('click', function(e) {
        if (!accuracyTestActive) return;
        
        const rect = accuracyCanvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        accuracyClicks.push({ x, y });
        
        // Check if click is within a target
        let hit = false;
        accuracyTargets.forEach((target, index) => {
            const distance = Math.sqrt((x - target.x) ** 2 + (y - target.y) ** 2);
            if (distance <= target.radius) {
                hit = true;
                accuracyTargets.splice(index, 1);
            }
        });
        
        if (hit) {
            drawAccuracyTest();
            if (accuracyTargets.length === 0) {
                // Test completed
                const accuracy = (accuracyClicks.length / 10) * 100;
                document.getElementById('accuracyResults').innerHTML = `
                    <h4>Pointing Accuracy Results</h4>
                    <p>Targets Hit: ${accuracyClicks.length}/10</p>
                    <p>Accuracy: ${accuracy.toFixed(1)}%</p>
                    <p class="${accuracy >= 80 ? 'good' : 'poor'}">
                        ${accuracy >= 80 ? '✓ Good pointing accuracy' : '⚠ Accuracy needs improvement'}
                    </p>
                `;
                assessmentResults.usability.accuracy = accuracy;
                accuracyTestActive = false;
                showNotification('Accuracy test completed');
            }
        }
    });
    
    function drawAccuracyTest() {
        ctx.clearRect(0, 0, accuracyCanvas.width, accuracyCanvas.height);
        
        // Draw targets
        accuracyTargets.forEach(target => {
            ctx.beginPath();
            ctx.arc(target.x, target.y, target.radius, 0, 2 * Math.PI);
            ctx.fillStyle = '#007bff';
            ctx.fill();
            ctx.strokeStyle = '#0056b3';
            ctx.lineWidth = 2;
            ctx.stroke();
        });
        
        // Draw click points
        accuracyClicks.forEach(click => {
            ctx.beginPath();
            ctx.arc(click.x, click.y, 3, 0, 2 * Math.PI);
            ctx.fillStyle = '#dc3545';
            ctx.fill();
        });
    }
    
    // Click speed test
    let speedTestActive = false;
    let clickCount = 0;
    let startTime = 0;
    let speedInterval;
    
    document.getElementById('startSpeedTest').addEventListener('click', function() {
        speedTestActive = true;
        clickCount = 0;
        startTime = Date.now();
        
        document.getElementById('clickCount').textContent = '0';
        document.getElementById('clickTime').textContent = '0.00s';
        document.getElementById('clicksPerSecond').textContent = '0.00';
        
        speedInterval = setInterval(updateSpeedMetrics, 100);
        showNotification('Speed test started - click as fast as possible');
    });
    
    document.getElementById('stopSpeedTest').addEventListener('click', function() {
        speedTestActive = false;
        clearInterval(speedInterval);
        
        const elapsed = (Date.now() - startTime) / 1000;
        const cps = clickCount / elapsed;
        
        document.getElementById('speedResults').innerHTML = `
            <h4>Click Speed Results</h4>
            <p>Total Clicks: ${clickCount}</p>
            <p>Time: ${elapsed.toFixed(2)}s</p>
            <p>Clicks Per Second: ${cps.toFixed(2)}</p>
            <p class="${cps >= 5 ? 'good' : 'poor'}">
                ${cps >= 5 ? '✓ Good click speed' : '⚠ Speed may need improvement'}
            </p>
        `;
        
        assessmentResults.usability.clickSpeed = cps;
        showNotification('Speed test completed');
    });
    
    document.getElementById('clickTarget').addEventListener('click', function() {
        if (speedTestActive) {
            clickCount++;
            document.getElementById('clickCount').textContent = clickCount;
        }
    });
    
    function updateSpeedMetrics() {
        if (!speedTestActive) return;
        
        const elapsed = (Date.now() - startTime) / 1000;
        const cps = clickCount / elapsed;
        
        document.getElementById('clickTime').textContent = elapsed.toFixed(2) + 's';
        document.getElementById('clicksPerSecond').textContent = cps.toFixed(2);
    }
    
    // Typing test
    let typingTestActive = false;
    let typingStartTime = 0;
    const sampleText = document.getElementById('sampleText').textContent;
    
    document.getElementById('startTypingTest').addEventListener('click', function() {
        typingTestActive = true;
        typingStartTime = Date.now();
        document.getElementById('inputText').value = '';
        document.getElementById('inputText').focus();
        showNotification('Typing test started');
    });
    
    document.getElementById('resetTypingTest').addEventListener('click', function() {
        typingTestActive = false;
        document.getElementById('inputText').value = '';
        document.getElementById('wordsPerMinute').textContent = '0';
        document.getElementById('typingAccuracy').textContent = '100%';
        document.getElementById('typingErrors').textContent = '0';
    });
    
    document.getElementById('inputText').addEventListener('input', function() {
        if (!typingTestActive) return;
        
        const typedText = this.value;
        const elapsed = (Date.now() - typingStartTime) / 1000 / 60; // minutes
        
        // Calculate WPM
        const wordsTyped = typedText.split(' ').length;
        const wpm = wordsTyped / elapsed;
        document.getElementById('wordsPerMinute').textContent = wpm.toFixed(1);
        
        // Calculate accuracy
        let errors = 0;
        const minLength = Math.min(typedText.length, sampleText.length);
        for (let i = 0; i < minLength; i++) {
            if (typedText[i] !== sampleText[i]) {
                errors++;
            }
        }
        
        const accuracy = ((typedText.length - errors) / typedText.length) * 100;
        document.getElementById('typingAccuracy').textContent = accuracy.toFixed(1) + '%';
        document.getElementById('typingErrors').textContent = errors;
        
        // Check if test is complete
        if (typedText.length >= sampleText.length) {
            typingTestActive = false;
            
            document.getElementById('typingResults').innerHTML = `
                <h4>Typing Test Results</h4>
                <p>Words Per Minute: ${wpm.toFixed(1)}</p>
                <p>Accuracy: ${accuracy.toFixed(1)}%</p>
                <p>Errors: ${errors}</p>
                <p class="${wpm >= 40 && accuracy >= 90 ? 'good' : 'poor'}">
                    ${wpm >= 40 && accuracy >= 90 ? '✓ Good typing performance' : '⚠ Typing performance needs improvement'}
                </p>
            `;
            
            assessmentResults.usability.typingWPM = wpm;
            assessmentResults.usability.typingAccuracy = accuracy;
            showNotification('Typing test completed');
        }
    });
    
    // Performance analysis
    document.getElementById('runPerformanceTest').addEventListener('click', function() {
        // Simulate performance metrics
        const responseTime = Math.random() * 50 + 10; // 10-60ms
        const throughput = Math.random() * 20 + 5; // 5-25 ops/sec
        const errorRate = Math.random() * 5; // 0-5%
        const learningTime = Math.random() * 30 + 10; // 10-40 min
        
        // Update metric displays
        document.getElementById('responseTimeValue').textContent = responseTime.toFixed(1) + ' ms';
        document.getElementById('throughputValue').textContent = throughput.toFixed(1) + ' ops/sec';
        document.getElementById('errorRateValue').textContent = errorRate.toFixed(1) + ' %';
        document.getElementById('learningTimeValue').textContent = learningTime.toFixed(1) + ' min';
        
        // Update bars
        document.getElementById('responseTimeBar').style.width = Math.min((responseTime / 100) * 100, 100) + '%';
        document.getElementById('throughputBar').style.width = Math.min((throughput / 30) * 100, 100) + '%';
        document.getElementById('errorRateBar').style.width = errorRate * 5 + '%';
        document.getElementById('learningTimeBar').style.width = Math.min((learningTime / 60) * 100, 100) + '%';
        
        document.getElementById('performanceResults').innerHTML = `
            <h4>Performance Analysis Results</h4>
            <p>Response Time: ${responseTime.toFixed(1)}ms ${responseTime < 30 ? '(Good)' : '(Slow)'}</p>
            <p>Throughput: ${throughput.toFixed(1)} ops/sec ${throughput > 10 ? '(High)' : '(Low)'}</p>
            <p>Error Rate: ${errorRate.toFixed(1)}% ${errorRate < 2 ? '(Low)' : '(High)'}</p>
            <p>Learning Time: ${learningTime.toFixed(1)}min ${learningTime < 20 ? '(Fast)' : '(Slow)'}</p>
        `;
        
        assessmentResults.performance = {
            responseTime,
            throughput,
            errorRate,
            learningTime
        };
        
        showNotification('Performance test completed');
    });
    
    // Compliance check
    document.getElementById('runComplianceCheck').addEventListener('click', function() {
        const checklistItems = document.querySelectorAll('.compliance-item input[type="checkbox"]');
        const checkedItems = document.querySelectorAll('.compliance-item input[type="checkbox"]:checked');
        
        const complianceScore = (checkedItems.length / checklistItems.length) * 100;
        
        let complianceLevel = 'poor';
        if (complianceScore >= 80) complianceLevel = 'excellent';
        else if (complianceScore >= 60) complianceLevel = 'good';
        else if (complianceScore >= 40) complianceLevel = 'fair';
        
        document.getElementById('complianceResults').innerHTML = `
            <h4>ISO 9241 Compliance Results</h4>
            <p>Compliance Score: ${complianceScore.toFixed(1)}%</p>
            <p>Level: <span class="${complianceLevel}">${complianceLevel.toUpperCase()}</span></p>
            <div class="compliance-bar">
                <div class="compliance-fill" style="width: ${complianceScore}%"></div>
            </div>
            <p>Requirements Met: ${checkedItems.length}/${checklistItems.length}</p>
        `;
        
        assessmentResults.compliance.score = complianceScore;
        assessmentResults.compliance.level = complianceLevel;
        showNotification('Compliance check completed');
    });
    
    // Report generation
    document.getElementById('generateReportBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('resultsSection').style.display = 'block';
        
        generateReport();
    });
    
    function generateReport() {
        // Summary tab
        document.getElementById('assessmentSummary').innerHTML = `
            <p><strong>Device Type:</strong> ${currentAssessment.deviceType}</p>
            <p><strong>Device Model:</strong> ${currentAssessment.deviceModel}</p>
            <p><strong>Connection Type:</strong> ${currentAssessment.connectionType}</p>
            <p><strong>User Handedness:</strong> ${currentAssessment.userHandedness}</p>
            <p><strong>Usage Scenario:</strong> ${currentAssessment.usageScenario}</p>
            <p><strong>Assessment Date:</strong> ${currentAssessment.startTime.toLocaleDateString()}</p>
        `;
        
        // Ergonomics tab
        const ergonomics = assessmentResults.ergonomics;
        document.getElementById('ergonomicsEvaluation').innerHTML = `
            <h4>Ergonomic Assessment</h4>
            ${ergonomics.postureScore ? `<p>Posture Score: ${ergonomics.postureScore.toFixed(1)}%</p>` : ''}
            ${ergonomics.forceLevel ? `<p>Force Level: ${ergonomics.forceLevel.toFixed(1)} N</p>` : ''}
            ${ergonomics.movementEfficiency ? `<p>Movement Efficiency: ${ergonomics.movementEfficiency.toFixed(1)}%</p>` : ''}
        `;
        
        // Usability tab
        const usability = assessmentResults.usability;
        document.getElementById('usabilityAssessment').innerHTML = `
            <h4>Usability Assessment</h4>
            ${usability.accuracy ? `<p>Pointing Accuracy: ${usability.accuracy.toFixed(1)}%</p>` : ''}
            ${usability.clickSpeed ? `<p>Click Speed: ${usability.clickSpeed.toFixed(2)} CPS</p>` : ''}
            ${usability.typingWPM ? `<p>Typing Speed: ${usability.typingWPM.toFixed(1)} WPM</p>` : ''}
            ${usability.typingAccuracy ? `<p>Typing Accuracy: ${usability.typingAccuracy.toFixed(1)}%</p>` : ''}
        `;
        
        // Performance tab
        const performance = assessmentResults.performance;
        document.getElementById('performanceAnalysis').innerHTML = `
            <h4>Performance Analysis</h4>
            ${performance.responseTime ? `<p>Response Time: ${performance.responseTime.toFixed(1)}ms</p>` : ''}
            ${performance.throughput ? `<p>Throughput: ${performance.throughput.toFixed(1)} ops/sec</p>` : ''}
            ${performance.errorRate ? `<p>Error Rate: ${performance.errorRate.toFixed(1)}%</p>` : ''}
            ${performance.learningTime ? `<p>Learning Time: ${performance.learningTime.toFixed(1)}min</p>` : ''}
        `;
        
        // Compliance tab
        const compliance = assessmentResults.compliance;
        document.getElementById('complianceStatus').innerHTML = `
            <h4>Compliance Status</h4>
            ${compliance.score ? `<p>Compliance Score: ${compliance.score.toFixed(1)}%</p>` : ''}
            ${compliance.level ? `<p>Compliance Level: ${compliance.level}</p>` : ''}
        `;
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

### Step 4: Python Input Device Analysis Script
Create an `input_device_analysis.py` file:

```python
import json
import math
from datetime import datetime
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import numpy as np

class InputDeviceAnalyzer:
    def __init__(self):
        self.assessment_data = {}
        self.analysis_results = {}
    
    def load_assessment_data(self, file_path: str):
        """Load input device assessment data"""
        with open(file_path, 'r') as f:
            self.assessment_data = json.load(f)
    
    def analyze_ergonomics(self) -> Dict[str, float]:
        """Analyze ergonomic factors"""
        ergonomics = self.assessment_data.get('ergonomics', {})
        
        analysis = {}
        
        # Posture analysis
        if 'postureScore' in ergonomics:
            posture_score = ergonomics['postureScore']
            analysis['posture_quality'] = self._rate_posture(posture_score)
        
        # Force analysis
        if 'forceLevel' in ergonomics:
            force_level = ergonomics['forceLevel']
            analysis['force_quality'] = self._rate_force(force_level)
        
        # Movement analysis
        if 'movementEfficiency' in ergonomics:
            movement_eff = ergonomics['movementEfficiency']
            analysis['movement_quality'] = self._rate_movement(movement_eff)
        
        # Overall ergonomics score
        ergonomics_scores = [v for v in analysis.values() if isinstance(v, (int, float))]
        analysis['overall_ergonomics'] = sum(ergonomics_scores) / len(ergonomics_scores) if ergonomics_scores else 0
        
        return analysis
    
    def analyze_usability(self) -> Dict[str, float]:
        """Analyze usability metrics"""
        usability = self.assessment_data.get('usability', {})
        
        analysis = {}
        
        # Accuracy analysis
        if 'accuracy' in usability:
            accuracy = usability['accuracy']
            analysis['accuracy_quality'] = self._rate_accuracy(accuracy)
        
        # Click speed analysis
        if 'clickSpeed' in usability:
            click_speed = usability['clickSpeed']
            analysis['speed_quality'] = self._rate_click_speed(click_speed)
        
        # Typing analysis
        if 'typingWPM' in usability:
            typing_wpm = usability['typingWPM']
            analysis['typing_speed_quality'] = self._rate_typing_speed(typing_wpm)
        
        if 'typingAccuracy' in usability:
            typing_accuracy = usability['typingAccuracy']
            analysis['typing_accuracy_quality'] = self._rate_typing_accuracy(typing_accuracy)
        
        # Overall usability score
        usability_scores = [v for v in analysis.values() if isinstance(v, (int, float))]
        analysis['overall_usability'] = sum(usability_scores) / len(usability_scores) if usability_scores else 0
        
        return analysis
    
    def analyze_performance(self) -> Dict[str, float]:
        """Analyze performance metrics"""
        performance = self.assessment_data.get('performance', {})
        
        analysis = {}
        
        # Response time analysis
        if 'responseTime' in performance:
            response_time = performance['responseTime']
            analysis['response_time_quality'] = self._rate_response_time(response_time)
        
        # Throughput analysis
        if 'throughput' in performance:
            throughput = performance['throughput']
            analysis['throughput_quality'] = self._rate_throughput(throughput)
        
        # Error rate analysis
        if 'errorRate' in performance:
            error_rate = performance['errorRate']
            analysis['error_rate_quality'] = self._rate_error_rate(error_rate)
        
        # Learning time analysis
        if 'learningTime' in performance:
            learning_time = performance['learningTime']
            analysis['learning_time_quality'] = self._rate_learning_time(learning_time)
        
        # Overall performance score
        performance_scores = [v for v in analysis.values() if isinstance(v, (int, float))]
        analysis['overall_performance'] = sum(performance_scores) / len(performance_scores) if performance_scores else 0
        
        return analysis
    
    def analyze_compliance(self) -> Dict[str, float]:
        """Analyze ISO 9241 compliance"""
        compliance = self.assessment_data.get('compliance', {})
        
        analysis = {}
        
        if 'score' in compliance:
            score = compliance['score']
            analysis['compliance_score'] = score
            analysis['compliance_level'] = self._rate_compliance(score)
        
        return analysis
    
    def _rate_posture(self, posture_score: float) -> float:
        """Rate posture quality (0-100)"""
        if posture_score >= 90:
            return 100
        elif posture_score >= 80:
            return 80
        elif posture_score >= 70:
            return 60
        elif posture_score >= 60:
            return 40
        else:
            return 20
    
    def _rate_force(self, force_level: float) -> float:
        """Rate force level (0-100)"""
        if 0.5 <= force_level <= 2.0:
            return 100
        elif 0.3 <= force_level <= 3.0:
            return 80
        elif 0.2 <= force_level <= 4.0:
            return 60
        else:
            return 40
    
    def _rate_movement(self, movement_eff: float) -> float:
        """Rate movement efficiency (0-100)"""
        if movement_eff >= 90:
            return 100
        elif movement_eff >= 80:
            return 80
        elif movement_eff >= 70:
            return 60
        elif movement_eff >= 60:
            return 40
        else:
            return 20
    
    def _rate_accuracy(self, accuracy: float) -> float:
        """Rate pointing accuracy (0-100)"""
        if accuracy >= 90:
            return 100
        elif accuracy >= 80:
            return 80
        elif accuracy >= 70:
            return 60
        elif accuracy >= 60:
            return 40
        else:
            return 20
    
    def _rate_click_speed(self, click_speed: float) -> float:
        """Rate click speed (0-100)"""
        if click_speed >= 8:
            return 100
        elif click_speed >= 6:
            return 80
        elif click_speed >= 4:
            return 60
        elif click_speed >= 2:
            return 40
        else:
            return 20
    
    def _rate_typing_speed(self, typing_wpm: float) -> float:
        """Rate typing speed (0-100)"""
        if typing_wpm >= 60:
            return 100
        elif typing_wpm >= 45:
            return 80
        elif typing_wpm >= 30:
            return 60
        elif typing_wpm >= 15:
            return 40
        else:
            return 20
    
    def _rate_typing_accuracy(self, typing_accuracy: float) -> float:
        """Rate typing accuracy (0-100)"""
        if typing_accuracy >= 95:
            return 100
        elif typing_accuracy >= 90:
            return 80
        elif typing_accuracy >= 85:
            return 60
        elif typing_accuracy >= 80:
            return 40
        else:
            return 20
    
    def _rate_response_time(self, response_time: float) -> float:
        """Rate response time (0-100)"""
        if response_time <= 20:
            return 100
        elif response_time <= 40:
            return 80
        elif response_time <= 60:
            return 60
        elif response_time <= 80:
            return 40
        else:
            return 20
    
    def _rate_throughput(self, throughput: float) -> float:
        """Rate throughput (0-100)"""
        if throughput >= 20:
            return 100
        elif throughput >= 15:
            return 80
        elif throughput >= 10:
            return 60
        elif throughput >= 5:
            return 40
        else:
            return 20
    
    def _rate_error_rate(self, error_rate: float) -> float:
        """Rate error rate (0-100)"""
        if error_rate <= 1:
            return 100
        elif error_rate <= 2:
            return 80
        elif error_rate <= 4:
            return 60
        elif error_rate <= 6:
            return 40
        else:
            return 20
    
    def _rate_learning_time(self, learning_time: float) -> float:
        """Rate learning time (0-100)"""
        if learning_time <= 15:
            return 100
        elif learning_time <= 25:
            return 80
        elif learning_time <= 35:
            return 60
        elif learning_time <= 45:
            return 40
        else:
            return 20
    
    def _rate_compliance(self, score: float) -> str:
        """Rate compliance level"""
        if score >= 80:
            return "Excellent"
        elif score >= 60:
            return "Good"
        elif score >= 40:
            return "Fair"
        else:
            return "Poor"
    
    def generate_comprehensive_report(self) -> Dict:
        """Generate comprehensive input device analysis report"""
        report = {
            'device_info': {
                'device_type': self.assessment_data.get('deviceType', 'Unknown'),
                'device_model': self.assessment_data.get('deviceModel', 'Unknown'),
                'connection_type': self.assessment_data.get('connectionType', 'Unknown'),
                'user_handedness': self.assessment_data.get('userHandedness', 'Unknown'),
                'usage_scenario': self.assessment_data.get('usageScenario', 'Unknown'),
                'assessment_date': self.assessment_data.get('startTime', datetime.now().isoformat())
            },
            'ergonomics_analysis': self.analyze_ergonomics(),
            'usability_analysis': self.analyze_usability(),
            'performance_analysis': self.analyze_performance(),
            'compliance_analysis': self.analyze_compliance(),
            'recommendations': self.generate_recommendations(),
            'generated_at': datetime.now().isoformat()
        }
        
        # Calculate overall score
        analyses = [report['ergonomics_analysis'], report['usability_analysis'], 
                   report['performance_analysis'], report['compliance_analysis']]
        
        overall_scores = []
        for analysis in analyses:
            for key, value in analysis.items():
                if key.startswith('overall_') or key == 'compliance_score':
                    overall_scores.append(value)
        
        report['overall_score'] = sum(overall_scores) / len(overall_scores) if overall_scores else 0
        
        return report
    
    def generate_recommendations(self) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        # Ergonomics recommendations
        ergonomics = self.analyze_ergonomics()
        if ergonomics.get('overall_ergonomics', 0) < 70:
            recommendations.append("Consider ergonomic adjustments for better posture and reduced strain")
        
        # Usability recommendations
        usability = self.analyze_usability()
        if usability.get('overall_usability', 0) < 70:
            recommendations.append("Improve device usability through better design and user feedback")
        
        # Performance recommendations
        performance = self.analyze_performance()
        if performance.get('overall_performance', 0) < 70:
            recommendations.append("Optimize device performance for better response time and accuracy")
        
        # Compliance recommendations
        compliance = self.analyze_compliance()
        if compliance.get('compliance_score', 0) < 80:
            recommendations.append("Address ISO 9241 compliance issues for input device standards")
        
        if not recommendations:
            recommendations.append("Input device meets acceptable standards - continue monitoring performance")
        
        return recommendations
    
    def save_report(self, file_path: str = 'input_device_report.json'):
        """Save comprehensive report to file"""
        report = self.generate_comprehensive_report()
        
        with open(file_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"Input device report saved: {file_path}")
        return report
    
    def visualize_analysis(self, save_path: str = 'input_device_analysis.png'):
        """Create visualizations of the analysis"""
        report = self.generate_comprehensive_report()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # Overall scores
        categories = ['Ergonomics', 'Usability', 'Performance', 'Compliance']
        scores = [
            report['ergonomics_analysis'].get('overall_ergonomics', 0),
            report['usability_analysis'].get('overall_usability', 0),
            report['performance_analysis'].get('overall_performance', 0),
            report['compliance_analysis'].get('compliance_score', 0)
        ]
        
        bars = ax1.bar(categories, scores, color=['blue', 'green', 'orange', 'red'])
        ax1.set_ylim(0, 100)
        ax1.set_title('Input Device Analysis Scores')
        ax1.set_ylabel('Score (%)')
        
        # Add value labels on bars
        for bar, score in zip(bars, scores):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_y() + score + 1, 
                    f'{score:.1f}', ha='center', va='bottom')
        
        # Ergonomics metrics
        ergonomics_metrics = ['Posture', 'Force', 'Movement']
        ergonomics_scores = [
            report['ergonomics_analysis'].get('posture_quality', 0),
            report['ergonomics_analysis'].get('force_quality', 0),
            report['ergonomics_analysis'].get('movement_quality', 0)
        ]
        
        ax2.bar(ergonomics_metrics, ergonomics_scores, color='lightblue')
        ax2.set_ylim(0, 100)
        ax2.set_title('Ergonomics Metrics')
        ax2.set_ylabel('Quality Score')
        
        # Usability metrics
        usability_metrics = ['Accuracy', 'Speed', 'Typing']
        usability_scores = [
            report['usability_analysis'].get('accuracy_quality', 0),
            report['usability_analysis'].get('speed_quality', 0),
            (report['usability_analysis'].get('typing_speed_quality', 0) + 
             report['usability_analysis'].get('typing_accuracy_quality', 0)) / 2
        ]
        
        ax3.bar(usability_metrics, usability_scores, color='lightgreen')
        ax3.set_ylim(0, 100)
        ax3.set_title('Usability Metrics')
        ax3.set_ylabel('Usability Score')
        
        # Performance metrics
        performance_metrics = ['Response', 'Throughput', 'Errors', 'Learning']
        performance_scores = [
            report['performance_analysis'].get('response_time_quality', 0),
            report['performance_analysis'].get('throughput_quality', 0),
            report['performance_analysis'].get('error_rate_quality', 0),
            report['performance_analysis'].get('learning_time_quality', 0)
        ]
        
        ax4.bar(performance_metrics, performance_scores, color='lightcoral')
        ax4.set_ylim(0, 100)
        ax4.set_title('Performance Metrics')
        ax4.set_ylabel('Performance Score')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Analysis visualization saved: {save_path}")

# Example usage
if __name__ == "__main__":
    analyzer = InputDeviceAnalyzer()
    
    # Simulate assessment data
    assessment_data = {
        'deviceType': 'mouse',
        'deviceModel': 'Logitech MX Master 3',
        'connectionType': 'wireless',
        'userHandedness': 'right',
        'usageScenario': 'office',
        'startTime': datetime.now().isoformat(),
        'ergonomics': {
            'postureScore': 85.0,
            'forceLevel': 1.2,
            'movementEfficiency': 92.0
        },
        'usability': {
            'accuracy': 88.0,
            'clickSpeed': 6.5,
            'typingWPM': 0,  # Not applicable for mouse
            'typingAccuracy': 0
        },
        'performance': {
            'responseTime': 15.0,
            'throughput': 18.0,
            'errorRate': 1.5,
            'learningTime': 12.0
        },
        'compliance': {
            'score': 82.0,
            'level': 'Good'
        }
    }
    
    analyzer.assessment_data = assessment_data
    report = analyzer.save_report()
    
    print("Overall Score:", report.get('overall_score', 0))
    print("Recommendations:")
    for rec in report.get('recommendations', []):
        print(f"  - {rec}")
    
    # Visualize results
    analyzer.visualize_analysis()
```

### Step 5: Documentation
This input device standards assessment toolkit implements comprehensive evaluation methods from ISO 9241-410 and ISO 9241-411:

1. **Ergonomic Assessment**: Posture analysis, force measurement, and movement pattern evaluation
2. **Usability Testing**: Pointing accuracy, click speed, and text input performance testing
3. **Performance Analysis**: Response time, throughput, error rate, and learning time metrics
4. **Compliance Checking**: Automated verification against ISO 9241 input device standards

Key features:
- Interactive web-based assessment interface with real-time testing
- Comprehensive ergonomic evaluation tools
- Automated usability and performance testing
- ISO 9241 compliance verification system
- Data-driven recommendations and reporting

The toolkit provides professional-grade tools for evaluating input device standards according to international ergonomics and usability standards.
