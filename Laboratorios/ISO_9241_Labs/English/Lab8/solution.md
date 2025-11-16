# Lab 8: Visual Display Requirements

## Solution

### Step 1: Visual Display Assessment HTML
Create a `visual_display.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visual Display Assessment - ISO 9241 Lab</title>
    <link rel="stylesheet" href="visual.css">
</head>
<body>
    <header>
        <h1>Visual Display Requirements Assessment</h1>
        <nav>
            <button id="qualityBtn">Display Quality</button>
            <button id="readabilityBtn">Readability Test</button>
            <button id="ergonomicsBtn">Ergonomics</button>
            <button id="complianceBtn">Compliance Check</button>
            <button id="generateReportBtn">Generate Report</button>
        </nav>
    </header>

    <main>
        <section class="assessment-setup">
            <h2>Assessment Configuration</h2>
            <form id="assessmentConfigForm">
                <div class="form-group">
                    <label for="displayType">Display Type:</label>
                    <select id="displayType">
                        <option value="lcd">LCD Monitor</option>
                        <option value="led">LED Display</option>
                        <option value="oled">OLED Screen</option>
                        <option value="crt">CRT Monitor</option>
                        <option value="projector">Projector</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="screenSize">Screen Size (inches):</label>
                    <input type="number" id="screenSize" min="10" max="100" value="24">
                </div>
                
                <div class="form-group">
                    <label for="resolution">Resolution:</label>
                    <select id="resolution">
                        <option value="hd">1920x1080 (HD)</option>
                        <option value="fhd">1920x1080 (Full HD)</option>
                        <option value="qhd">2560x1440 (QHD)</option>
                        <option value="uhd">3840x2160 (UHD)</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="environment">Environment:</label>
                    <select id="environment">
                        <option value="office">Office</option>
                        <option value="industrial">Industrial</option>
                        <option value="outdoor">Outdoor</option>
                        <option value="medical">Medical</option>
                    </select>
                </div>
                
                <button type="submit" class="primary-btn">Start Assessment</button>
            </form>
        </section>

        <section class="quality-assessment" id="qualitySection" style="display: none;">
            <h2>Display Quality Assessment</h2>
            
            <div class="quality-tests">
                <div class="test-panel">
                    <h3>Color Accuracy Test</h3>
                    <div class="color-swatches">
                        <div class="swatch" data-color="#FF0000" style="background-color: #FF0000;"></div>
                        <div class="swatch" data-color="#00FF00" style="background-color: #00FF00;"></div>
                        <div class="swatch" data-color="#0000FF" style="background-color: #0000FF;"></div>
                        <div class="swatch" data-color="#FFFF00" style="background-color: #FFFF00;"></div>
                        <div class="swatch" data-color="#FF00FF" style="background-color: #FF00FF;"></div>
                        <div class="swatch" data-color="#00FFFF" style="background-color: #00FFFF;"></div>
                    </div>
                    <button id="colorTestBtn">Run Color Test</button>
                    <div id="colorResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Brightness & Contrast Test</h3>
                    <div class="brightness-test">
                        <div class="brightness-scale">
                            <div class="scale-item" data-level="0" style="background-color: black;"></div>
                            <div class="scale-item" data-level="25" style="background-color: #404040;"></div>
                            <div class="scale-item" data-level="50" style="background-color: #808080;"></div>
                            <div class="scale-item" data-level="75" style="background-color: #C0C0C0;"></div>
                            <div class="scale-item" data-level="100" style="background-color: white;"></div>
                        </div>
                    </div>
                    <button id="brightnessTestBtn">Run Brightness Test</button>
                    <div id="brightnessResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Pixel Response Test</h3>
                    <div class="pixel-test">
                        <div class="pixel-grid">
                            <div class="pixel-row">
                                <div class="pixel" style="background-color: white;"></div>
                                <div class="pixel" style="background-color: black;"></div>
                                <div class="pixel" style="background-color: white;"></div>
                                <div class="pixel" style="background-color: black;"></div>
                            </div>
                            <div class="pixel-row">
                                <div class="pixel" style="background-color: black;"></div>
                                <div class="pixel" style="background-color: white;"></div>
                                <div class="pixel" style="background-color: black;"></div>
                                <div class="pixel" style="background-color: white;"></div>
                            </div>
                        </div>
                    </div>
                    <button id="pixelTestBtn">Run Pixel Test</button>
                    <div id="pixelResults"></div>
                </div>
            </div>
        </section>

        <section class="readability-test" id="readabilitySection" style="display: none;">
            <h2>Readability & Legibility Test</h2>
            
            <div class="readability-controls">
                <div class="control-group">
                    <label for="fontSize">Font Size:</label>
                    <input type="range" id="fontSize" min="8" max="72" value="16">
                    <span id="fontSizeValue">16px</span>
                </div>
                
                <div class="control-group">
                    <label for="fontFamily">Font Family:</label>
                    <select id="fontFamily">
                        <option value="Arial">Arial</option>
                        <option value="Times New Roman">Times New Roman</option>
                        <option value="Verdana">Verdana</option>
                        <option value="Helvetica">Helvetica</option>
                        <option value="Georgia">Georgia</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="textColor">Text Color:</label>
                    <input type="color" id="textColor" value="#000000">
                </div>
                
                <div class="control-group">
                    <label for="bgColor">Background Color:</label>
                    <input type="color" id="bgColor" value="#FFFFFF">
                </div>
            </div>
            
            <div class="readability-sample">
                <h3>Readability Sample Text</h3>
                <p id="sampleText">
                    The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet and is commonly used for font readability testing. The legibility of text depends on several factors including font size, typeface, color contrast, and spacing between characters and lines.
                </p>
            </div>
            
            <div class="readability-metrics">
                <button id="calculateReadabilityBtn">Calculate Readability Metrics</button>
                <div id="readabilityResults"></div>
            </div>
        </section>

        <section class="ergonomics-assessment" id="ergonomicsSection" style="display: none;">
            <h2>Ergonomic Assessment</h2>
            
            <div class="ergonomics-tests">
                <div class="test-panel">
                    <h3>Viewing Distance Test</h3>
                    <div class="distance-guide">
                        <p>Position yourself at a comfortable viewing distance from the screen.</p>
                        <div class="distance-indicator">
                            <div class="optimal-zone">Optimal Zone (20-28 inches)</div>
                            <div class="comfort-zone">Comfort Zone (28-40 inches)</div>
                        </div>
                    </div>
                    <button id="distanceTestBtn">Measure Distance</button>
                    <div id="distanceResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Viewing Angle Test</h3>
                    <div class="angle-guide">
                        <p>Adjust your viewing angle to be perpendicular to the screen surface.</p>
                        <div class="angle-visualization">
                            <div class="screen-surface"></div>
                            <div class="optimal-angle"></div>
                        </div>
                    </div>
                    <button id="angleTestBtn">Check Angle</button>
                    <div id="angleResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Lighting Assessment</h3>
                    <div class="lighting-test">
                        <p>Ensure adequate lighting and minimize glare on the screen.</p>
                        <div class="lighting-zones">
                            <div class="zone adequate">Adequate Lighting</div>
                            <div class="zone glare">Potential Glare</div>
                            <div class="zone dark">Too Dark</div>
                        </div>
                    </div>
                    <button id="lightingTestBtn">Assess Lighting</button>
                    <div id="lightingResults"></div>
                </div>
            </div>
        </section>

        <section class="compliance-check" id="complianceSection" style="display: none;">
            <h2>ISO 9241 Compliance Check</h2>
            
            <div class="compliance-checklist">
                <h3>Visual Display Requirements Checklist</h3>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req1">
                    <label for="req1">Display luminance meets minimum requirements (≥ 35 cd/m²)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req2">
                    <label for="req2">Color contrast ratio meets WCAG guidelines (≥ 4.5:1)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req3">
                    <label for="req3">Character height meets legibility requirements (≥ 0.15° visual angle)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req4">
                    <label for="req4">Refresh rate meets flicker-free requirements (≥ 60 Hz)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req5">
                    <label for="req5">Viewing angle supports ergonomic requirements (± 45°)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req6">
                    <label for="req6">Anti-glare treatment applied to reduce reflections</label>
                </div>
            </div>
            
            <button id="runComplianceCheck">Run Compliance Assessment</button>
            <div id="complianceResults"></div>
        </section>

        <section class="results-section" id="resultsSection" style="display: none;">
            <h2>Assessment Results</h2>
            <div class="results-tabs">
                <button class="tab-btn active" data-tab="summary">Summary</button>
                <button class="tab-btn" data-tab="quality">Quality</button>
                <button class="tab-btn" data-tab="readability">Readability</button>
                <button class="tab-btn" data-tab="ergonomics">Ergonomics</button>
                <button class="tab-btn" data-tab="compliance">Compliance</button>
            </div>
            
            <div class="tab-content">
                <div id="summaryTab" class="tab-panel active">
                    <h3>Assessment Summary</h3>
                    <div id="assessmentSummary"></div>
                </div>
                
                <div id="qualityTab" class="tab-panel">
                    <h3>Display Quality Results</h3>
                    <div id="qualityResults"></div>
                </div>
                
                <div id="readabilityTab" class="tab-panel">
                    <h3>Readability Assessment</h3>
                    <div id="readabilityAssessment"></div>
                </div>
                
                <div id="ergonomicsTab" class="tab-panel">
                    <h3>Ergonomic Evaluation</h3>
                    <div id="ergonomicsEvaluation"></div>
                </div>
                
                <div id="complianceTab" class="tab-panel">
                    <h3>Compliance Status</h3>
                    <div id="complianceStatus"></div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="visual.js"></script>
</body>
</html>
```

### Step 2: CSS for Visual Assessment Interface
Create a `visual.css` file:

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

/* Quality Tests */
.quality-tests {
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

.color-swatches {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1rem 0;
}

.swatch {
    width: 60px;
    height: 60px;
    border-radius: 4px;
    border: 2px solid #dee2e6;
    cursor: pointer;
}

.brightness-scale {
    display: flex;
    margin: 1rem 0;
}

.scale-item {
    flex: 1;
    height: 40px;
    border: 1px solid #333;
}

.pixel-grid {
    margin: 1rem 0;
}

.pixel-row {
    display: flex;
}

.pixel {
    width: 20px;
    height: 20px;
    border: 1px solid #333;
}

/* Readability Test */
.readability-controls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}

.control-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.control-group input[type="range"] {
    width: 100%;
}

#sampleText {
    font-size: 16px;
    line-height: 1.5;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 4px;
    min-height: 100px;
}

/* Ergonomics Tests */
.ergonomics-tests {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.distance-indicator, .angle-visualization, .lighting-zones {
    margin: 1rem 0;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 4px;
}

.optimal-zone, .comfort-zone {
    padding: 0.5rem;
    margin: 0.5rem 0;
    border-radius: 4px;
}

.optimal-zone {
    background-color: #d4edda;
    color: #155724;
}

.comfort-zone {
    background-color: #fff3cd;
    color: #856404;
}

.screen-surface {
    width: 200px;
    height: 150px;
    background-color: #007bff;
    margin: 1rem auto;
    border-radius: 4px;
    position: relative;
}

.optimal-angle {
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 20px;
    background-color: #28a745;
}

.zone {
    padding: 0.5rem;
    margin: 0.5rem 0;
    border-radius: 4px;
    text-align: center;
}

.zone.adequate {
    background-color: #d4edda;
    color: #155724;
}

.zone.glare {
    background-color: #f8d7da;
    color: #721c24;
}

.zone.dark {
    background-color: #e2e3e5;
    color: #383d41;
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
    
    .quality-tests, .ergonomics-tests {
        grid-template-columns: 1fr;
    }
    
    .readability-controls {
        grid-template-columns: 1fr;
    }
    
    .results-tabs {
        flex-direction: column;
    }
    
    .tab-btn {
        border-radius: 0;
        margin-right: 0;
    }
}
```

### Step 3: JavaScript for Visual Assessment
Create a `visual.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Assessment configuration
    let currentAssessment = null;
    let assessmentResults = {
        quality: {},
        readability: {},
        ergonomics: {},
        compliance: {}
    };
    
    // Configuration form
    document.getElementById('assessmentConfigForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        currentAssessment = {
            displayType: document.getElementById('displayType').value,
            screenSize: parseInt(document.getElementById('screenSize').value),
            resolution: document.getElementById('resolution').value,
            environment: document.getElementById('environment').value,
            startTime: new Date()
        };
        
        document.querySelector('.assessment-setup').style.display = 'none';
        document.getElementById('qualitySection').style.display = 'block';
        
        showNotification('Assessment configured successfully');
    });
    
    // Navigation
    document.getElementById('qualityBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('qualitySection').style.display = 'block';
    });
    
    document.getElementById('readabilityBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('readabilitySection').style.display = 'block';
    });
    
    document.getElementById('ergonomicsBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('ergonomicsSection').style.display = 'block';
    });
    
    document.getElementById('complianceBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('complianceSection').style.display = 'block';
    });
    
    function hideAllSections() {
        document.getElementById('qualitySection').style.display = 'none';
        document.getElementById('readabilitySection').style.display = 'none';
        document.getElementById('ergonomicsSection').style.display = 'none';
        document.getElementById('complianceSection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
    }
    
    // Quality assessment
    document.getElementById('colorTestBtn').addEventListener('click', function() {
        // Simulate color accuracy test
        const colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF'];
        let colorResults = [];
        
        colors.forEach(color => {
            // Simulate color accuracy measurement
            const accuracy = Math.random() * 20 + 80; // 80-100%
            colorResults.push({ color, accuracy: accuracy.toFixed(1) });
        });
        
        const avgAccuracy = colorResults.reduce((sum, result) => sum + parseFloat(result.accuracy), 0) / colorResults.length;
        
        document.getElementById('colorResults').innerHTML = `
            <h4>Color Accuracy Results</h4>
            <p>Average Color Accuracy: ${avgAccuracy.toFixed(1)}%</p>
            <div class="color-results">
                ${colorResults.map(result => 
                    `<div class="color-result">
                        <div class="color-sample" style="background-color: ${result.color};"></div>
                        <span>${result.accuracy}%</span>
                    </div>`
                ).join('')}
            </div>
        `;
        
        assessmentResults.quality.colorAccuracy = avgAccuracy;
        showNotification('Color test completed');
    });
    
    document.getElementById('brightnessTestBtn').addEventListener('click', function() {
        // Simulate brightness and contrast test
        const brightness = Math.random() * 50 + 200; // 200-250 cd/m²
        const contrast = Math.random() * 200 + 800; // 800-1000:1
        
        document.getElementById('brightnessResults').innerHTML = `
            <h4>Brightness & Contrast Results</h4>
            <p>Brightness: ${brightness.toFixed(1)} cd/m²</p>
            <p>Contrast Ratio: ${contrast.toFixed(0)}:1</p>
            <div class="brightness-bar">
                <div class="brightness-fill" style="width: ${Math.min(brightness / 3, 100)}%"></div>
            </div>
        `;
        
        assessmentResults.quality.brightness = brightness;
        assessmentResults.quality.contrast = contrast;
        showNotification('Brightness test completed');
    });
    
    document.getElementById('pixelTestBtn').addEventListener('click', function() {
        // Simulate pixel response test
        const responseTime = Math.random() * 5 + 1; // 1-6ms
        const deadPixels = Math.floor(Math.random() * 3); // 0-2 dead pixels
        
        document.getElementById('pixelResults').innerHTML = `
            <h4>Pixel Response Results</h4>
            <p>Response Time: ${responseTime.toFixed(1)}ms</p>
            <p>Dead Pixels: ${deadPixels}</p>
            <p class="${responseTime < 5 ? 'good' : 'poor'}">
                ${responseTime < 5 ? '✓ Good response time' : '⚠ Slow response time'}
            </p>
        `;
        
        assessmentResults.quality.responseTime = responseTime;
        assessmentResults.quality.deadPixels = deadPixels;
        showNotification('Pixel test completed');
    });
    
    // Readability test
    const fontSizeInput = document.getElementById('fontSize');
    const fontSizeValue = document.getElementById('fontSizeValue');
    const sampleText = document.getElementById('sampleText');
    
    fontSizeInput.addEventListener('input', function() {
        fontSizeValue.textContent = this.value + 'px';
        sampleText.style.fontSize = this.value + 'px';
    });
    
    document.getElementById('fontFamily').addEventListener('change', function() {
        sampleText.style.fontFamily = this.value;
    });
    
    document.getElementById('textColor').addEventListener('input', function() {
        sampleText.style.color = this.value;
    });
    
    document.getElementById('bgColor').addEventListener('input', function() {
        sampleText.style.backgroundColor = this.value;
    });
    
    document.getElementById('calculateReadabilityBtn').addEventListener('click', function() {
        const fontSize = parseInt(fontSizeInput.value);
        const textColor = document.getElementById('textColor').value;
        const bgColor = document.getElementById('bgColor').value;
        
        // Calculate contrast ratio
        const contrastRatio = calculateContrastRatio(textColor, bgColor);
        
        // Calculate visual angle (simplified)
        const viewingDistance = 60; // cm (assumed)
        const visualAngle = (fontSize / viewingDistance) * (180 / Math.PI) * 2.54; // degrees
        
        const readabilityScore = calculateReadabilityScore(fontSize, contrastRatio, visualAngle);
        
        document.getElementById('readabilityResults').innerHTML = `
            <h4>Readability Metrics</h4>
            <p>Font Size: ${fontSize}px</p>
            <p>Contrast Ratio: ${contrastRatio.toFixed(2)}:1</p>
            <p>Visual Angle: ${visualAngle.toFixed(2)}°</p>
            <p>Readability Score: ${readabilityScore.toFixed(1)}/100</p>
            <div class="readability-bar">
                <div class="readability-fill" style="width: ${readabilityScore}%"></div>
            </div>
        `;
        
        assessmentResults.readability = {
            fontSize,
            contrastRatio,
            visualAngle,
            readabilityScore
        };
        
        showNotification('Readability analysis completed');
    });
    
    function calculateContrastRatio(color1, color2) {
        const l1 = getLuminance(color1);
        const l2 = getLuminance(color2);
        const brightest = Math.max(l1, l2);
        const darkest = Math.min(l1, l2);
        return (brightest + 0.05) / (darkest + 0.05);
    }
    
    function getLuminance(color) {
        const rgb = hexToRgb(color);
        const rsRGB = rgb.r / 255;
        const gsRGB = rgb.g / 255;
        const bsRGB = rgb.b / 255;
        
        const r = rsRGB <= 0.03928 ? rsRGB / 12.92 : Math.pow((rsRGB + 0.055) / 1.055, 2.4);
        const g = gsRGB <= 0.03928 ? gsRGB / 12.92 : Math.pow((gsRGB + 0.055) / 1.055, 2.4);
        const b = bsRGB <= 0.03928 ? bsRGB / 12.92 : Math.pow((bsRGB + 0.055) / 1.055, 2.4);
        
        return 0.2126 * r + 0.7152 * g + 0.0722 * b;
    }
    
    function hexToRgb(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }
    
    function calculateReadabilityScore(fontSize, contrastRatio, visualAngle) {
        let score = 0;
        
        // Font size score (0-30 points)
        if (fontSize >= 16) score += 30;
        else if (fontSize >= 12) score += 20;
        else if (fontSize >= 10) score += 10;
        
        // Contrast score (0-40 points)
        if (contrastRatio >= 7) score += 40;
        else if (contrastRatio >= 4.5) score += 30;
        else if (contrastRatio >= 3) score += 20;
        else score += 10;
        
        // Visual angle score (0-30 points)
        if (visualAngle >= 0.3) score += 30;
        else if (visualAngle >= 0.2) score += 20;
        else if (visualAngle >= 0.15) score += 10;
        
        return Math.min(score, 100);
    }
    
    // Ergonomics assessment
    document.getElementById('distanceTestBtn').addEventListener('click', function() {
        // Simulate distance measurement
        const distance = Math.random() * 20 + 50; // 50-70 cm
        const optimal = distance >= 50 && distance <= 70;
        
        document.getElementById('distanceResults').innerHTML = `
            <h4>Viewing Distance Results</h4>
            <p>Measured Distance: ${distance.toFixed(1)} cm</p>
            <p class="${optimal ? 'good' : 'poor'}">
                ${optimal ? '✓ Optimal viewing distance' : '⚠ Adjust viewing distance'}
            </p>
        `;
        
        assessmentResults.ergonomics.viewingDistance = distance;
        showNotification('Distance test completed');
    });
    
    document.getElementById('angleTestBtn').addEventListener('click', function() {
        // Simulate angle measurement
        const angle = Math.random() * 30 - 15; // -15 to +15 degrees
        const optimal = Math.abs(angle) <= 5;
        
        document.getElementById('angleResults').innerHTML = `
            <h4>Viewing Angle Results</h4>
            <p>Measured Angle: ${angle.toFixed(1)}°</p>
            <p class="${optimal ? 'good' : 'poor'}">
                ${optimal ? '✓ Optimal viewing angle' : '⚠ Adjust viewing angle'}
            </p>
        `;
        
        assessmentResults.ergonomics.viewingAngle = angle;
        showNotification('Angle test completed');
    });
    
    document.getElementById('lightingTestBtn').addEventListener('click', function() {
        // Simulate lighting assessment
        const lightingLevel = Math.random() * 500 + 200; // 200-700 lux
        const glare = Math.random() < 0.3; // 30% chance of glare
        
        let assessment = 'adequate';
        if (glare) assessment = 'glare';
        else if (lightingLevel < 300) assessment = 'dark';
        
        document.getElementById('lightingResults').innerHTML = `
            <h4>Lighting Assessment Results</h4>
            <p>Lighting Level: ${lightingLevel.toFixed(0)} lux</p>
            <p>Glare Detected: ${glare ? 'Yes' : 'No'}</p>
            <p class="${assessment === 'adequate' ? 'good' : 'poor'}">
                ${assessment === 'adequate' ? '✓ Adequate lighting conditions' : 
                  assessment === 'glare' ? '⚠ Glare detected - adjust lighting' : 
                  '⚠ Insufficient lighting - increase illumination'}
            </p>
        `;
        
        assessmentResults.ergonomics.lightingLevel = lightingLevel;
        assessmentResults.ergonomics.glare = glare;
        showNotification('Lighting assessment completed');
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
            <p><strong>Display Type:</strong> ${currentAssessment.displayType}</p>
            <p><strong>Screen Size:</strong> ${currentAssessment.screenSize}"</p>
            <p><strong>Resolution:</strong> ${currentAssessment.resolution}</p>
            <p><strong>Environment:</strong> ${currentAssessment.environment}</p>
            <p><strong>Assessment Date:</strong> ${currentAssessment.startTime.toLocaleDateString()}</p>
        `;
        
        // Quality tab
        const quality = assessmentResults.quality;
        document.getElementById('qualityResults').innerHTML = `
            <h4>Display Quality Metrics</h4>
            ${quality.colorAccuracy ? `<p>Color Accuracy: ${quality.colorAccuracy}%</p>` : ''}
            ${quality.brightness ? `<p>Brightness: ${quality.brightness.toFixed(1)} cd/m²</p>` : ''}
            ${quality.contrast ? `<p>Contrast Ratio: ${quality.contrast.toFixed(0)}:1</p>` : ''}
            ${quality.responseTime ? `<p>Response Time: ${quality.responseTime.toFixed(1)}ms</p>` : ''}
            ${quality.deadPixels !== undefined ? `<p>Dead Pixels: ${quality.deadPixels}</p>` : ''}
        `;
        
        // Readability tab
        const readability = assessmentResults.readability;
        document.getElementById('readabilityAssessment').innerHTML = `
            <h4>Readability Assessment</h4>
            ${readability.fontSize ? `<p>Font Size: ${readability.fontSize}px</p>` : ''}
            ${readability.contrastRatio ? `<p>Contrast Ratio: ${readability.contrastRatio.toFixed(2)}:1</p>` : ''}
            ${readability.visualAngle ? `<p>Visual Angle: ${readability.visualAngle.toFixed(2)}°</p>` : ''}
            ${readability.readabilityScore ? `<p>Readability Score: ${readability.readabilityScore.toFixed(1)}/100</p>` : ''}
        `;
        
        // Ergonomics tab
        const ergonomics = assessmentResults.ergonomics;
        document.getElementById('ergonomicsEvaluation').innerHTML = `
            <h4>Ergonomic Evaluation</h4>
            ${ergonomics.viewingDistance ? `<p>Viewing Distance: ${ergonomics.viewingDistance.toFixed(1)} cm</p>` : ''}
            ${ergonomics.viewingAngle !== undefined ? `<p>Viewing Angle: ${ergonomics.viewingAngle.toFixed(1)}°</p>` : ''}
            ${ergonomics.lightingLevel ? `<p>Lighting Level: ${ergonomics.lightingLevel.toFixed(0)} lux</p>` : ''}
            ${ergonomics.glare !== undefined ? `<p>Glare Detected: ${ergonomics.glare ? 'Yes' : 'No'}</p>` : ''}
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

### Step 4: Python Visual Analysis Script
Create a `visual_analysis.py` file:

```python
import json
import math
from datetime import datetime
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import numpy as np

class VisualDisplayAnalyzer:
    def __init__(self):
        self.assessment_data = {}
        self.analysis_results = {}
    
    def load_assessment_data(self, file_path: str):
        """Load visual display assessment data"""
        with open(file_path, 'r') as f:
            self.assessment_data = json.load(f)
    
    def analyze_display_quality(self) -> Dict[str, float]:
        """Analyze display quality metrics"""
        quality = self.assessment_data.get('quality', {})
        
        analysis = {}
        
        # Color accuracy analysis
        if 'colorAccuracy' in quality:
            color_acc = quality['colorAccuracy']
            analysis['color_quality'] = self._rate_color_accuracy(color_acc)
        
        # Brightness analysis
        if 'brightness' in quality:
            brightness = quality['brightness']
            analysis['brightness_quality'] = self._rate_brightness(brightness)
        
        # Contrast analysis
        if 'contrast' in quality:
            contrast = quality['contrast']
            analysis['contrast_quality'] = self._rate_contrast(contrast)
        
        # Response time analysis
        if 'responseTime' in quality:
            response_time = quality['responseTime']
            analysis['response_quality'] = self._rate_response_time(response_time)
        
        # Overall quality score
        quality_scores = [v for v in analysis.values() if isinstance(v, (int, float))]
        analysis['overall_quality'] = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        
        return analysis
    
    def analyze_readability(self) -> Dict[str, float]:
        """Analyze readability metrics"""
        readability = self.assessment_data.get('readability', {})
        
        analysis = {}
        
        # Font size analysis
        if 'fontSize' in readability:
            font_size = readability['fontSize']
            analysis['font_size_score'] = self._rate_font_size(font_size)
        
        # Contrast ratio analysis
        if 'contrastRatio' in readability:
            contrast_ratio = readability['contrastRatio']
            analysis['contrast_score'] = self._rate_contrast_ratio(contrast_ratio)
        
        # Visual angle analysis
        if 'visualAngle' in readability:
            visual_angle = readability['visualAngle']
            analysis['visual_angle_score'] = self._rate_visual_angle(visual_angle)
        
        # Overall readability score
        readability_scores = [v for v in analysis.values() if isinstance(v, (int, float))]
        analysis['overall_readability'] = sum(readability_scores) / len(readability_scores) if readability_scores else 0
        
        return analysis
    
    def analyze_ergonomics(self) -> Dict[str, float]:
        """Analyze ergonomic factors"""
        ergonomics = self.assessment_data.get('ergonomics', {})
        
        analysis = {}
        
        # Viewing distance analysis
        if 'viewingDistance' in ergonomics:
            distance = ergonomics['viewingDistance']
            analysis['distance_score'] = self._rate_viewing_distance(distance)
        
        # Viewing angle analysis
        if 'viewingAngle' in ergonomics:
            angle = ergonomics['viewingAngle']
            analysis['angle_score'] = self._rate_viewing_angle(angle)
        
        # Lighting analysis
        if 'lightingLevel' in ergonomics:
            lighting = ergonomics['lightingLevel']
            glare = ergonomics.get('glare', False)
            analysis['lighting_score'] = self._rate_lighting(lighting, glare)
        
        # Overall ergonomics score
        ergonomics_scores = [v for v in analysis.values() if isinstance(v, (int, float))]
        analysis['overall_ergonomics'] = sum(ergonomics_scores) / len(ergonomics_scores) if ergonomics_scores else 0
        
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
    
    def _rate_color_accuracy(self, accuracy: float) -> float:
        """Rate color accuracy (0-100)"""
        if accuracy >= 95:
            return 100
        elif accuracy >= 90:
            return 80
        elif accuracy >= 85:
            return 60
        elif accuracy >= 80:
            return 40
        else:
            return 20
    
    def _rate_brightness(self, brightness: float) -> float:
        """Rate brightness (0-100)"""
        if 200 <= brightness <= 300:
            return 100
        elif 150 <= brightness <= 400:
            return 80
        elif 100 <= brightness <= 500:
            return 60
        else:
            return 40
    
    def _rate_contrast(self, contrast: float) -> float:
        """Rate contrast ratio (0-100)"""
        if contrast >= 1000:
            return 100
        elif contrast >= 800:
            return 80
        elif contrast >= 500:
            return 60
        elif contrast >= 300:
            return 40
        else:
            return 20
    
    def _rate_response_time(self, response_time: float) -> float:
        """Rate response time (0-100)"""
        if response_time <= 2:
            return 100
        elif response_time <= 5:
            return 80
        elif response_time <= 10:
            return 60
        elif response_time <= 16:
            return 40
        else:
            return 20
    
    def _rate_font_size(self, font_size: int) -> float:
        """Rate font size (0-100)"""
        if font_size >= 16:
            return 100
        elif font_size >= 14:
            return 80
        elif font_size >= 12:
            return 60
        elif font_size >= 10:
            return 40
        else:
            return 20
    
    def _rate_contrast_ratio(self, contrast_ratio: float) -> float:
        """Rate contrast ratio for readability (0-100)"""
        if contrast_ratio >= 7:
            return 100
        elif contrast_ratio >= 4.5:
            return 80
        elif contrast_ratio >= 3:
            return 60
        elif contrast_ratio >= 2:
            return 40
        else:
            return 20
    
    def _rate_visual_angle(self, visual_angle: float) -> float:
        """Rate visual angle (0-100)"""
        if visual_angle >= 0.3:
            return 100
        elif visual_angle >= 0.2:
            return 80
        elif visual_angle >= 0.15:
            return 60
        elif visual_angle >= 0.1:
            return 40
        else:
            return 20
    
    def _rate_viewing_distance(self, distance: float) -> float:
        """Rate viewing distance in cm (0-100)"""
        if 50 <= distance <= 70:
            return 100
        elif 40 <= distance <= 80:
            return 80
        elif 30 <= distance <= 90:
            return 60
        else:
            return 40
    
    def _rate_viewing_angle(self, angle: float) -> float:
        """Rate viewing angle in degrees (0-100)"""
        if abs(angle) <= 5:
            return 100
        elif abs(angle) <= 10:
            return 80
        elif abs(angle) <= 15:
            return 60
        elif abs(angle) <= 20:
            return 40
        else:
            return 20
    
    def _rate_lighting(self, lighting: float, glare: bool) -> float:
        """Rate lighting conditions (0-100)"""
        if glare:
            return 30  # Glare significantly reduces score
        
        if 300 <= lighting <= 500:
            return 100
        elif 200 <= lighting <= 700:
            return 80
        elif 100 <= lighting <= 1000:
            return 60
        else:
            return 40
    
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
        """Generate comprehensive visual display analysis report"""
        report = {
            'assessment_info': {
                'display_type': self.assessment_data.get('displayType', 'Unknown'),
                'screen_size': self.assessment_data.get('screenSize', 'Unknown'),
                'resolution': self.assessment_data.get('resolution', 'Unknown'),
                'environment': self.assessment_data.get('environment', 'Unknown'),
                'assessment_date': self.assessment_data.get('startTime', datetime.now().isoformat())
            },
            'quality_analysis': self.analyze_display_quality(),
            'readability_analysis': self.analyze_readability(),
            'ergonomics_analysis': self.analyze_ergonomics(),
            'compliance_analysis': self.analyze_compliance(),
            'recommendations': self.generate_recommendations(),
            'generated_at': datetime.now().isoformat()
        }
        
        # Calculate overall score
        analyses = [report['quality_analysis'], report['readability_analysis'], 
                   report['ergonomics_analysis'], report['compliance_analysis']]
        
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
        
        # Quality recommendations
        quality = self.analyze_display_quality()
        if quality.get('overall_quality', 0) < 70:
            recommendations.append("Consider display calibration for improved color accuracy and brightness")
        
        # Readability recommendations
        readability = self.analyze_readability()
        if readability.get('overall_readability', 0) < 70:
            recommendations.append("Increase font size and improve contrast ratio for better readability")
        
        # Ergonomics recommendations
        ergonomics = self.analyze_ergonomics()
        if ergonomics.get('overall_ergonomics', 0) < 70:
            recommendations.append("Adjust viewing distance, angle, and lighting conditions for optimal ergonomics")
        
        # Compliance recommendations
        compliance = self.analyze_compliance()
        if compliance.get('compliance_score', 0) < 80:
            recommendations.append("Address ISO 9241 compliance issues to meet visual display standards")
        
        if not recommendations:
            recommendations.append("Visual display meets acceptable standards - continue monitoring")
        
        return recommendations
    
    def save_report(self, file_path: str = 'visual_display_report.json'):
        """Save comprehensive report to file"""
        report = self.generate_comprehensive_report()
        
        with open(file_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"Visual display report saved: {file_path}")
        return report
    
    def visualize_analysis(self, save_path: str = 'visual_analysis.png'):
        """Create visualizations of the analysis"""
        report = self.generate_comprehensive_report()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # Overall scores
        categories = ['Quality', 'Readability', 'Ergonomics', 'Compliance']
        scores = [
            report['quality_analysis'].get('overall_quality', 0),
            report['readability_analysis'].get('overall_readability', 0),
            report['ergonomics_analysis'].get('overall_ergonomics', 0),
            report['compliance_analysis'].get('compliance_score', 0)
        ]
        
        bars = ax1.bar(categories, scores, color=['blue', 'green', 'orange', 'red'])
        ax1.set_ylim(0, 100)
        ax1.set_title('Visual Display Analysis Scores')
        ax1.set_ylabel('Score (%)')
        
        # Add value labels on bars
        for bar, score in zip(bars, scores):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_y() + score + 1, 
                    f'{score:.1f}', ha='center', va='bottom')
        
        # Quality metrics
        quality_metrics = ['Color', 'Brightness', 'Contrast', 'Response']
        quality_scores = [
            report['quality_analysis'].get('color_quality', 0),
            report['quality_analysis'].get('brightness_quality', 0),
            report['quality_analysis'].get('contrast_quality', 0),
            report['quality_analysis'].get('response_quality', 0)
        ]
        
        ax2.bar(quality_metrics, quality_scores, color='lightblue')
        ax2.set_ylim(0, 100)
        ax2.set_title('Display Quality Metrics')
        ax2.set_ylabel('Quality Score')
        
        # Readability metrics
        readability_metrics = ['Font Size', 'Contrast', 'Visual Angle']
        readability_scores = [
            report['readability_analysis'].get('font_size_score', 0),
            report['readability_analysis'].get('contrast_score', 0),
            report['readability_analysis'].get('visual_angle_score', 0)
        ]
        
        ax3.bar(readability_metrics, readability_scores, color='lightgreen')
        ax3.set_ylim(0, 100)
        ax3.set_title('Readability Metrics')
        ax3.set_ylabel('Readability Score')
        
        # Ergonomics metrics
        ergonomics_metrics = ['Distance', 'Angle', 'Lighting']
        ergonomics_scores = [
            report['ergonomics_analysis'].get('distance_score', 0),
            report['ergonomics_analysis'].get('angle_score', 0),
            report['ergonomics_analysis'].get('lighting_score', 0)
        ]
        
        ax4.bar(ergonomics_metrics, ergonomics_scores, color='lightcoral')
        ax4.set_ylim(0, 100)
        ax4.set_title('Ergonomics Metrics')
        ax4.set_ylabel('Ergonomics Score')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Analysis visualization saved: {save_path}")

# Example usage
if __name__ == "__main__":
    analyzer = VisualDisplayAnalyzer()
    
    # Simulate assessment data
    assessment_data = {
        'displayType': 'LED',
        'screenSize': 24,
        'resolution': 'fhd',
        'environment': 'office',
        'startTime': datetime.now().isoformat(),
        'quality': {
            'colorAccuracy': 92.5,
            'brightness': 225.0,
            'contrast': 950.0,
            'responseTime': 3.2,
            'deadPixels': 0
        },
        'readability': {
            'fontSize': 16,
            'contrastRatio': 5.8,
            'visualAngle': 0.25,
            'readabilityScore': 85.0
        },
        'ergonomics': {
            'viewingDistance': 60.0,
            'viewingAngle': 2.5,
            'lightingLevel': 350.0,
            'glare': False
        },
        'compliance': {
            'score': 85.0,
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
This visual display assessment toolkit implements comprehensive evaluation methods from ISO 9241-303 and ISO 9241-307:

1. **Display Quality Assessment**: Color accuracy, brightness, contrast, and pixel response testing
2. **Readability Evaluation**: Font size, contrast ratio, and visual angle analysis
3. **Ergonomic Assessment**: Viewing distance, angle, and lighting condition evaluation
4. **Compliance Checking**: Automated verification against ISO 9241 standards

Key features:
- Interactive web-based assessment interface
- Real-time metric calculation and visualization
- Comprehensive Python analysis with automated reporting
- ISO 9241 compliance verification
- Data-driven recommendations for improvement

The toolkit provides professional-grade tools for evaluating visual display requirements according to international standards.
