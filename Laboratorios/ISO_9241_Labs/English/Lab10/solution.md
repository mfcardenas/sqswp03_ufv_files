# Lab 10: Case Study

## Solution

### Step 1: Case Study HTML Dashboard
Create a `case_study.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISO 9241 Comprehensive Case Study - Lab</title>
    <link rel="stylesheet" href="case.css">
</head>
<body>
    <header>
        <h1>ISO 9241 Comprehensive Case Study</h1>
        <nav>
            <button id="scenarioBtn">Case Scenario</button>
            <button id="assessmentBtn">Assessment Framework</button>
            <button id="evaluationBtn">Evaluation Tools</button>
            <button id="integrationBtn">Standards Integration</button>
            <button id="reportsBtn">Reports & Findings</button>
            <button id="recommendationsBtn">Recommendations</button>
        </nav>
    </header>

    <main>
        <section class="case-scenario" id="scenarioSection">
            <h2>Case Study Scenario: Smart Healthcare System</h2>
            
            <div class="scenario-overview">
                <h3>Project Overview</h3>
                <p>The Metropolitan General Hospital is implementing a comprehensive smart healthcare system that integrates electronic health records, medical imaging, patient monitoring, and telemedicine capabilities. The system serves 500+ healthcare professionals and manages 10,000+ patient records daily.</p>
                
                <div class="project-details">
                    <div class="detail-card">
                        <h4>System Components</h4>
                        <ul>
                            <li>Electronic Health Records (EHR) System</li>
                            <li>Picture Archiving and Communication System (PACS)</li>
                            <li>Patient Monitoring Dashboard</li>
                            <li>Telemedicine Platform</li>
                            <li>Mobile Applications for Staff</li>
                            <li>Integration with Medical Devices</li>
                        </ul>
                    </div>
                    
                    <div class="detail-card">
                        <h4>User Groups</h4>
                        <ul>
                            <li>Physicians and Surgeons</li>
                            <li>Nurses and Clinical Staff</li>
                            <li>Administrative Personnel</li>
                            <li>IT Support Staff</li>
                            <li>Patients and Family Members</li>
                        </ul>
                    </div>
                    
                    <div class="detail-card">
                        <h4>Critical Requirements</h4>
                        <ul>
                            <li>24/7 System Availability</li>
                            <li>HIPAA Compliance</li>
                            <li>Real-time Data Accuracy</li>
                            <li>Intuitive User Interfaces</li>
                            <li>Ergonomic Design for Long Shifts</li>
                            <li>Accessibility for All Users</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="challenges-identified">
                <h3>Identified Challenges</h3>
                <div class="challenges-grid">
                    <div class="challenge-item">
                        <h4>Ergonomic Concerns</h4>
                        <p>Healthcare professionals work 12+ hour shifts with intensive computer interaction</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Usability Issues</h4>
                        <p>Complex workflows require efficient, error-free interactions under time pressure</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Performance Requirements</h4>
                        <p>Critical care decisions depend on system response times and data accuracy</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Compliance Standards</h4>
                        <p>Multiple regulatory requirements (HIPAA, ISO 9241, accessibility standards)</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Integration Complexity</h4>
                        <p>Multiple systems and devices must work seamlessly together</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>User Diversity</h4>
                        <p>Wide range of user expertise levels and physical capabilities</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="assessment-framework" id="assessmentSection" style="display: none;">
            <h2>Integrated Assessment Framework</h2>
            
            <div class="framework-overview">
                <h3>Multi-Dimensional Evaluation Approach</h3>
                <p>This case study integrates all ISO 9241 standards covered in previous laboratories into a comprehensive evaluation framework.</p>
                
                <div class="standards-integration">
                    <div class="standard-card">
                        <h4>ISO 9241-110: Dialogue Principles</h4>
                        <ul>
                            <li>Suitability for the task</li>
                            <li>Self-descriptiveness</li>
                            <li>Controllability</li>
                            <li>Conformity with user expectations</li>
                            <li>Error tolerance</li>
                            <li>Suitability for individualization</li>
                            <li>Suitability for learning</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>ISO 9241-210: Human-Centred Design</h4>
                        <ul>
                            <li>Understanding and specifying the context of use</li>
                            <li>Specifying the user and organizational requirements</li>
                            <li>Producing design solutions</li>
                            <li>Evaluating designs against requirements</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>ISO 9241-303: Visual Display Requirements</h4>
                        <ul>
                            <li>Display quality and legibility</li>
                            <li>Readability requirements</li>
                            <li>Visual ergonomics</li>
                            <li>Compliance checking</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>ISO 9241-410: Input Device Standards</h4>
                        <ul>
                            <li>Ergonomic design criteria</li>
                            <li>Operating force requirements</li>
                            <li>Key travel and tactile feedback</li>
                            <li>Device accessibility</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="evaluation-methodology">
                <h3>Evaluation Methodology</h3>
                
                <div class="methodology-steps">
                    <div class="step">
                        <h4>Step 1: Context Analysis</h4>
                        <p>Analyze healthcare workflows, user requirements, and system constraints</p>
                    </div>
                    
                    <div class="step">
                        <h4>Step 2: User Research</h4>
                        <p>Conduct interviews, observations, and usability testing with healthcare professionals</p>
                    </div>
                    
                    <div class="step">
                        <h4>Step 3: Standards Mapping</h4>
                        <p>Map ISO 9241 requirements to specific system components and use cases</p>
                    </div>
                    
                    <div class="step">
                        <h4>Step 4: Assessment Execution</h4>
                        <p>Execute comprehensive evaluations using integrated assessment tools</p>
                    </div>
                    
                    <div class="step">
                        <h4>Step 5: Findings Integration</h4>
                        <p>Integrate findings across all standards and identify systemic issues</p>
                    </div>
                    
                    <div class="step">
                        <h4>Step 6: Recommendations Development</h4>
                        <p>Develop prioritized recommendations for system improvements</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="evaluation-tools" id="evaluationSection" style="display: none;">
            <h2>Integrated Evaluation Tools</h2>
            
            <div class="tools-overview">
                <h3>Comprehensive Assessment Toolkit</h3>
                <p>Tools that integrate multiple ISO 9241 standards for holistic system evaluation.</p>
                
                <div class="tool-categories">
                    <div class="tool-category">
                        <h4>Ergonomic Assessment Tools</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>Workstation Ergonomics Evaluator</h5>
                                <p>Assesses desk setup, monitor positioning, and input device placement</p>
                                <button class="tool-btn" data-tool="workstation">Launch Tool</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Shift Fatigue Monitor</h5>
                                <p>Monitors user fatigue levels during extended work sessions</p>
                                <button class="tool-btn" data-tool="fatigue">Launch Tool</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tool-category">
                        <h4>Usability Testing Tools</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>Workflow Efficiency Analyzer</h5>
                                <p>Analyzes clinical workflow efficiency and identifies bottlenecks</p>
                                <button class="tool-btn" data-tool="workflow">Launch Tool</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Error Prevention Scanner</h5>
                                <p>Scans system for potential error conditions and prevention measures</p>
                                <button class="tool-btn" data-tool="error">Launch Tool</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tool-category">
                        <h4>Performance Monitoring Tools</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>System Response Time Monitor</h5>
                                <p>Monitors system response times across all critical functions</p>
                                <button class="tool-btn" data-tool="response">Launch Tool</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Data Accuracy Validator</h5>
                                <p>Validates data accuracy and integrity across the system</p>
                                <button class="tool-btn" data-tool="accuracy">Launch Tool</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tool-category">
                        <h4>Compliance Verification Tools</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>ISO 9241 Compliance Checker</h5>
                                <p>Automated compliance verification against ISO 9241 standards</p>
                                <button class="tool-btn" data-tool="compliance">Launch Tool</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Accessibility Auditor</h5>
                                <p>Audits system accessibility compliance</p>
                                <button class="tool-btn" data-tool="accessibility">Launch Tool</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="tool-results" id="toolResults" style="display: none;">
                <h3>Tool Results</h3>
                <div id="resultsContent"></div>
            </div>
        </section>

        <section class="standards-integration" id="integrationSection" style="display: none;">
            <h2>Standards Integration Matrix</h2>
            
            <div class="integration-matrix">
                <h3>ISO 9241 Standards Integration</h3>
                <p>How different standards work together in the healthcare system context.</p>
                
                <table class="standards-table">
                    <thead>
                        <tr>
                            <th>System Component</th>
                            <th>ISO 9241-110</th>
                            <th>ISO 9241-210</th>
                            <th>ISO 9241-303</th>
                            <th>ISO 9241-410</th>
                            <th>Integration Notes</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>EHR Interface</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>Complete integration required for patient safety</td>
                        </tr>
                        <tr>
                            <td>PACS Workstation</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>Critical for diagnostic accuracy</td>
                        </tr>
                        <tr>
                            <td>Patient Monitor</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✗</td>
                            <td>Display standards most critical</td>
                        </tr>
                        <tr>
                            <td>Mobile Apps</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>All standards apply to mobile context</td>
                        </tr>
                        <tr>
                            <td>Medical Devices</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>Full compliance mandatory</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="integration-analysis">
                <h3>Integration Analysis</h3>
                
                <div class="analysis-cards">
                    <div class="analysis-card">
                        <h4>Strengths of Integration</h4>
                        <ul>
                            <li>Comprehensive coverage of user needs</li>
                            <li>Consistent evaluation methodology</li>
                            <li>Systematic identification of issues</li>
                            <li>Evidence-based recommendations</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-card">
                        <h4>Integration Challenges</h4>
                        <ul>
                            <li>Complexity of multi-standard assessment</li>
                            <li>Resource requirements for comprehensive evaluation</li>
                            <li>Coordination across different expertise areas</li>
                            <li>Balancing conflicting requirements</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-card">
                        <h4>Best Practices</h4>
                        <ul>
                            <li>Start with user-centered design principles</li>
                            <li>Use integrated assessment frameworks</li>
                            <li>Establish clear evaluation criteria</li>
                            <li>Document all findings systematically</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="reports-findings" id="reportsSection" style="display: none;">
            <h2>Case Study Reports & Findings</h2>
            
            <div class="findings-overview">
                <h3>Key Findings Summary</h3>
                
                <div class="findings-metrics">
                    <div class="metric-card">
                        <h4>Overall System Score</h4>
                        <div class="score-display">
                            <div class="score-value">78%</div>
                            <div class="score-bar">
                                <div class="score-fill" style="width: 78%"></div>
                            </div>
                        </div>
                        <p>Good performance with room for improvement</p>
                    </div>
                    
                    <div class="metric-card">
                        <h4>Critical Issues Found</h4>
                        <div class="issues-count">12</div>
                        <p>Issues requiring immediate attention</p>
                    </div>
                    
                    <div class="metric-card">
                        <h4>Compliance Level</h4>
                        <div class="compliance-level">85%</div>
                        <p>Strong compliance foundation</p>
                    </div>
                    
                    <div class="metric-card">
                        <h4>User Satisfaction</h4>
                        <div class="satisfaction-score">82%</div>
                        <p>Generally positive user feedback</p>
                    </div>
                </div>
            </div>
            
            <div class="detailed-findings">
                <h3>Detailed Findings by Category</h3>
                
                <div class="findings-categories">
                    <div class="findings-category">
                        <h4>Ergonomic Issues</h4>
                        <ul>
                            <li>Monitor positioning suboptimal for 40% of workstations</li>
                            <li>Keyboard trays not adjustable in 25% of locations</li>
                            <li>Chair ergonomics inadequate for extended shifts</li>
                            <li>Lighting conditions cause eye strain in radiology</li>
                        </ul>
                    </div>
                    
                    <div class="findings-category">
                        <h4>Usability Problems</h4>
                        <ul>
                            <li>EHR navigation requires 8+ clicks for common tasks</li>
                            <li>Search functionality inconsistent across modules</li>
                            <li>Error messages not user-friendly</li>
                            <li>Training requirements exceed available time</li>
                        </ul>
                    </div>
                    
                    <div class="findings-category">
                        <h4>Performance Issues</h4>
                        <ul>
                            <li>PACS image loading takes 3-5 seconds during peak hours</li>
                            <li>System response time degrades under high load</li>
                            <li>Data synchronization delays between devices</li>
                            <li>Mobile app performance inconsistent on older devices</li>
                        </ul>
                    </div>
                    
                    <div class="findings-category">
                        <h4>Compliance Gaps</h4>
                        <ul>
                            <li>Color contrast ratios below WCAG standards in 3 modules</li>
                            <li>Keyboard shortcuts not available for motor-impaired users</li>
                            <li>Audit trails incomplete for regulatory requirements</li>
                            <li>Emergency access procedures not fully documented</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="impact-analysis">
                <h3>Impact Analysis</h3>
                
                <div class="impact-matrix">
                    <table class="impact-table">
                        <thead>
                            <tr>
                                <th>Issue Category</th>
                                <th>Severity</th>
                                <th>User Impact</th>
                                <th>Patient Safety</th>
                                <th>Operational Cost</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Ergonomic Issues</td>
                                <td>Medium</td>
                                <td>High</td>
                                <td>Medium</td>
                                <td>Medium</td>
                            </tr>
                            <tr>
                                <td>Usability Problems</td>
                                <td>High</td>
                                <td>High</td>
                                <td>High</td>
                                <td>High</td>
                            </tr>
                            <tr>
                                <td>Performance Issues</td>
                                <td>High</td>
                                <td>Medium</td>
                                <td>High</td>
                                <td>Medium</td>
                            </tr>
                            <tr>
                                <td>Compliance Gaps</td>
                                <td>Critical</td>
                                <td>Medium</td>
                                <td>Critical</td>
                                <td>Low</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <section class="recommendations" id="recommendationsSection" style="display: none;">
            <h2>Recommendations & Implementation Plan</h2>
            
            <div class="priority-recommendations">
                <h3>Priority Recommendations</h3>
                
                <div class="recommendation-phases">
                    <div class="phase">
                        <h4>Phase 1: Critical Fixes (0-3 months)</h4>
                        <div class="recommendation-list">
                            <div class="recommendation-item priority-critical">
                                <h5>Fix Color Contrast Issues</h5>
                                <p>Update UI color schemes to meet WCAG AA standards</p>
                                <span class="effort">Effort: Low</span>
                                <span class="impact">Impact: High</span>
                            </div>
                            
                            <div class="recommendation-item priority-critical">
                                <h5>Optimize PACS Response Times</h5>
                                <p>Implement caching and optimize database queries</p>
                                <span class="effort">Effort: Medium</span>
                                <span class="impact">Impact: High</span>
                            </div>
                            
                            <div class="recommendation-item priority-critical">
                                <h5>Improve EHR Navigation</h5>
                                <p>Redesign workflow to reduce clicks by 50%</p>
                                <span class="effort">Effort: High</span>
                                <span class="impact">Impact: High</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="phase">
                        <h4>Phase 2: Major Improvements (3-6 months)</h4>
                        <div class="recommendation-list">
                            <div class="recommendation-item priority-high">
                                <h5>Ergonomic Workstation Upgrades</h5>
                                <p>Replace outdated equipment and provide adjustable furniture</p>
                                <span class="effort">Effort: High</span>
                                <span class="impact">Impact: Medium</span>
                            </div>
                            
                            <div class="recommendation-item priority-high">
                                <h5>Enhanced Training Program</h5>
                                <p>Develop role-specific training modules and quick reference guides</p>
                                <span class="effort">Effort: Medium</span>
                                <span class="impact">Impact: High</span>
                            </div>
                            
                            <div class="recommendation-item priority-high">
                                <h5>Mobile App Optimization</h5>
                                <p>Improve performance and add offline capabilities</p>
                                <span class="effort">Effort: Medium</span>
                                <span class="impact">Impact: Medium</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="phase">
                        <h4>Phase 3: Long-term Enhancements (6-12 months)</h4>
                        <div class="recommendation-list">
                            <div class="recommendation-item priority-medium">
                                <h5>Advanced Analytics Integration</h5>
                                <p>Implement predictive analytics for system optimization</p>
                                <span class="effort">Effort: High</span>
                                <span class="impact">Impact: Medium</span>
                            </div>
                            
                            <div class="recommendation-item priority-medium">
                                <h5>AI-Powered Usability Features</h5>
                                <p>Add intelligent suggestions and automated workflows</p>
                                <span class="effort">Effort: High</span>
                                <span class="impact">Impact: High</span>
                            </div>
                            
                            <div class="recommendation-item priority-medium">
                                <h5>Comprehensive Accessibility Audit</h5>
                                <p>Full accessibility compliance and testing program</p>
                                <span class="effort">Effort: Medium</span>
                                <span class="impact">Impact: Medium</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="implementation-plan">
                <h3>Implementation Plan</h3>
                
                <div class="implementation-timeline">
                    <div class="timeline-item">
                        <h4>Month 1-2: Assessment & Planning</h4>
                        <ul>
                            <li>Complete detailed requirements analysis</li>
                            <li>Develop implementation roadmap</li>
                            <li>Establish success metrics</li>
                            <li>Secure stakeholder buy-in</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Month 3-4: Critical Fixes Implementation</h4>
                        <ul>
                            <li>Deploy Phase 1 recommendations</li>
                            <li>Conduct user acceptance testing</li>
                            <li>Provide training on new features</li>
                            <li>Monitor system performance</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Month 5-8: Major Improvements</h4>
                        <ul>
                            <li>Implement Phase 2 recommendations</li>
                            <li>Conduct comprehensive testing</li>
                            <li>Roll out changes in phases</li>
                            <li>Gather user feedback</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Month 9-12: Optimization & Enhancement</h4>
                        <ul>
                            <li>Deploy advanced features</li>
                            <li>Optimize system performance</li>
                            <li>Conduct final evaluation</li>
                            <li>Document lessons learned</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="success-metrics">
                <h3>Success Metrics</h3>
                
                <div class="metrics-grid">
                    <div class="metric-item">
                        <h4>User Satisfaction</h4>
                        <p>Target: 90% satisfaction rate</p>
                        <p>Current: 82%</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Task Completion Time</h4>
                        <p>Target: 25% reduction in common tasks</p>
                        <p>Current: Baseline established</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Error Rate</h4>
                        <p>Target: 50% reduction in user errors</p>
                        <p>Current: Baseline established</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>System Uptime</h4>
                        <p>Target: 99.9% availability</p>
                        <p>Current: 99.5%</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Compliance Score</h4>
                        <p>Target: 95% ISO 9241 compliance</p>
                        <p>Current: 85%</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Training Time</h4>
                        <p>Target: 30% reduction in training time</p>
                        <p>Current: Baseline established</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="case.js"></script>
</body>
</html>
```

### Step 2: CSS for Case Study Dashboard
Create a `case.css` file:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
    color: #333;
    line-height: 1.6;
}

header {
    background-color: #007bff;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
    margin: 0;
    font-size: 1.8rem;
}

nav {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}

nav button {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
}

nav button:hover, nav button:focus {
    background-color: rgba(255, 255, 255, 0.3);
    transform: translateY(-1px);
}

main {
    max-width: 1400px;
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
    margin-bottom: 2rem;
}

h3 {
    color: #007bff;
    margin-bottom: 1rem;
}

h4 {
    color: #495057;
    margin-bottom: 0.5rem;
}

/* Scenario Section */
.project-details {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.detail-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.detail-card h4 {
    margin-top: 0;
    color: #007bff;
}

.detail-card ul {
    margin: 0;
    padding-left: 1.5rem;
}

.detail-card li {
    margin-bottom: 0.5rem;
}

.challenges-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.challenge-item {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    padding: 1.5rem;
    border-radius: 8px;
}

.challenge-item h4 {
    margin-top: 0;
    color: #856404;
}

/* Assessment Framework */
.standards-integration {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.standard-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.standard-card h4 {
    margin-top: 0;
    color: #007bff;
}

.standard-card ul {
    margin: 0;
    padding-left: 1.5rem;
}

.methodology-steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.step {
    background-color: #e9ecef;
    padding: 1.5rem;
    border-radius: 8px;
    border-left: 4px solid #007bff;
}

.step h4 {
    margin-top: 0;
    color: #007bff;
}

/* Evaluation Tools */
.tool-categories {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.tool-category h4 {
    color: #007bff;
    margin-bottom: 1rem;
}

.tool-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.tool-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.tool-item h5 {
    margin-top: 0;
    color: #495057;
}

.tool-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
    transition: background-color 0.3s ease;
}

.tool-btn:hover {
    background-color: #0056b3;
}

/* Standards Integration */
.standards-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background-color: white;
}

.standards-table th, .standards-table td {
    padding: 1rem;
    text-align: left;
    border: 1px solid #dee2e6;
}

.standards-table th {
    background-color: #f8f9fa;
    font-weight: bold;
    color: #495057;
}

.standards-table tr:nth-child(even) {
    background-color: #f8f9fa;
}

.analysis-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.analysis-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.analysis-card h4 {
    margin-top: 0;
    color: #007bff;
}

/* Reports & Findings */
.findings-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.metric-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    border: 1px solid #dee2e6;
}

.metric-card h4 {
    margin-top: 0;
    color: #007bff;
}

.score-display {
    margin: 1rem 0;
}

.score-value {
    font-size: 2.5rem;
    font-weight: bold;
    color: #007bff;
}

.score-bar {
    width: 100%;
    height: 20px;
    background-color: #e9ecef;
    border-radius: 10px;
    overflow: hidden;
    margin: 0.5rem 0;
}

.score-fill {
    height: 100%;
    background-color: #007bff;
    width: 0%;
    transition: width 0.3s ease;
}

.issues-count {
    font-size: 3rem;
    font-weight: bold;
    color: #dc3545;
}

.compliance-level, .satisfaction-score {
    font-size: 2.5rem;
    font-weight: bold;
    color: #28a745;
}

.findings-categories {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.findings-category {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.findings-category h4 {
    margin-top: 0;
    color: #007bff;
}

.impact-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background-color: white;
}

.impact-table th, .impact-table td {
    padding: 1rem;
    text-align: left;
    border: 1px solid #dee2e6;
}

.impact-table th {
    background-color: #f8f9fa;
    font-weight: bold;
    color: #495057;
}

/* Recommendations */
.recommendation-phases {
    margin: 2rem 0;
}

.phase {
    margin-bottom: 3rem;
}

.phase h4 {
    color: #007bff;
    border-bottom: 1px solid #dee2e6;
    padding-bottom: 0.5rem;
}

.recommendation-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.recommendation-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    position: relative;
}

.recommendation-item h5 {
    margin-top: 0;
    color: #495057;
}

.priority-critical {
    border-left: 4px solid #dc3545;
}

.priority-high {
    border-left: 4px solid #fd7e14;
}

.priority-medium {
    border-left: 4px solid #ffc107;
}

.effort, .impact {
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
    margin-right: 0.5rem;
    margin-top: 0.5rem;
}

.implementation-timeline {
    margin: 2rem 0;
}

.timeline-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    border-left: 4px solid #007bff;
}

.timeline-item h4 {
    margin-top: 0;
    color: #007bff;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.metric-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.metric-item h4 {
    margin-top: 0;
    color: #007bff;
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
    z-index: 1000;
}

/* Responsive */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    nav {
        justify-content: center;
    }
    
    .project-details, .challenges-grid, .standards-integration, 
    .methodology-steps, .tool-categories, .analysis-cards,
    .findings-metrics, .findings-categories, .recommendation-list,
    .metrics-grid {
        grid-template-columns: 1fr;
    }
    
    .standards-table {
        font-size: 0.9rem;
    }
    
    .standards-table th, .standards-table td {
        padding: 0.5rem;
    }
    
    .impact-table {
        font-size: 0.9rem;
    }
    
    .impact-table th, .impact-table td {
        padding: 0.5rem;
    }
}
```

### Step 3: JavaScript for Case Study Dashboard
Create a `case.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Navigation system
    const sections = {
        scenario: document.getElementById('scenarioSection'),
        assessment: document.getElementById('assessmentSection'),
        evaluation: document.getElementById('evaluationSection'),
        integration: document.getElementById('integrationSection'),
        reports: document.getElementById('reportsSection'),
        recommendations: document.getElementById('recommendationsSection')
    };
    
    // Navigation buttons
    document.getElementById('scenarioBtn').addEventListener('click', () => showSection('scenario'));
    document.getElementById('assessmentBtn').addEventListener('click', () => showSection('assessment'));
    document.getElementById('evaluationBtn').addEventListener('click', () => showSection('evaluation'));
    document.getElementById('integrationBtn').addEventListener('click', () => showSection('integration'));
    document.getElementById('reportsBtn').addEventListener('click', () => showSection('reports'));
    document.getElementById('recommendationsBtn').addEventListener('click', () => showSection('recommendations'));
    
    function showSection(sectionName) {
        // Hide all sections
        Object.values(sections).forEach(section => {
            section.style.display = 'none';
        });
        
        // Show selected section
        sections[sectionName].style.display = 'block';
        
        // Update navigation buttons
        document.querySelectorAll('nav button').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Add active class to current button
        const currentBtn = document.getElementById(sectionName + 'Btn');
        if (currentBtn) {
            currentBtn.classList.add('active');
        }
        
        showNotification(`Switched to ${sectionName} section`);
    }
    
    // Tool launch functionality
    document.querySelectorAll('.tool-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const toolType = this.dataset.tool;
            launchTool(toolType);
        });
    });
    
    function launchTool(toolType) {
        const resultsSection = document.getElementById('toolResults');
        const resultsContent = document.getElementById('resultsContent');
        
        // Show results section
        resultsSection.style.display = 'block';
        
        // Generate tool results based on type
        let results = '';
        switch(toolType) {
            case 'workstation':
                results = generateWorkstationResults();
                break;
            case 'fatigue':
                results = generateFatigueResults();
                break;
            case 'workflow':
                results = generateWorkflowResults();
                break;
            case 'error':
                results = generateErrorResults();
                break;
            case 'response':
                results = generateResponseResults();
                break;
            case 'accuracy':
                results = generateAccuracyResults();
                break;
            case 'compliance':
                results = generateComplianceResults();
                break;
            case 'accessibility':
                results = generateAccessibilityResults();
                break;
            default:
                results = '<p>Tool results will be displayed here.</p>';
        }
        
        resultsContent.innerHTML = results;
        showNotification(`Launched ${toolType} assessment tool`);
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    function generateWorkstationResults() {
        return `
            <h4>Workstation Ergonomics Assessment Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Monitor Positioning</h5>
                    <p>Score: 75/100</p>
                    <p>Issues: 40% of workstations have suboptimal monitor height</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 75%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Keyboard Setup</h5>
                    <p>Score: 68/100</p>
                    <p>Issues: 25% lack adjustable keyboard trays</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 68%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Chair Ergonomics</h5>
                    <p>Score: 72/100</p>
                    <p>Issues: Seat height and back support inadequate</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 72%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Lighting Conditions</h5>
                    <p>Score: 65/100</p>
                    <p>Issues: Glare and insufficient task lighting</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 65%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Adjust monitor heights to eye level</li>
                    <li>Install adjustable keyboard trays</li>
                    <li>Replace chairs with ergonomic models</li>
                    <li>Improve lighting conditions</li>
                </ul>
            </div>
        `;
    }
    
    function generateFatigueResults() {
        return `
            <h4>Shift Fatigue Monitoring Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Fatigue Levels by Shift</h5>
                    <p>Average fatigue increase: 35% over 12-hour shifts</p>
                    <p>Peak fatigue: Hours 8-12 of shift</p>
                </div>
                
                <div class="result-item">
                    <h5>Error Correlation</h5>
                    <p>45% increase in errors during high fatigue periods</p>
                    <p>Critical tasks most affected</p>
                </div>
                
                <div class="result-item">
                    <h5>Recovery Patterns</h5>
                    <p>Full recovery requires 48-72 hours</p>
                    <p>Partial recovery with 24-hour breaks</p>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Implement mandatory break schedules</li>
                    <li>Rotate high-fatigue tasks</li>
                    <li>Monitor fatigue indicators</li>
                    <li>Provide recovery facilities</li>
                </ul>
            </div>
        `;
    }
    
    function generateWorkflowResults() {
        return `
            <h4>Workflow Efficiency Analysis Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>EHR Navigation Efficiency</h5>
                    <p>Average clicks: 8.5 per common task</p>
                    <p>Target: 4 clicks maximum</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 47%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Task Completion Time</h5>
                    <p>Current: 12.5 minutes per patient record</p>
                    <p>Target: 8 minutes</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 64%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Workflow Bottlenecks</h5>
                    <p>Top bottleneck: Medication ordering (3.2 min delay)</p>
                    <p>Second: Lab result review (2.8 min delay)</p>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Redesign EHR navigation flow</li>
                    <li>Implement workflow shortcuts</li>
                    <li>Streamline medication ordering</li>
                    <li>Automate routine tasks</li>
                </ul>
            </div>
        `;
    }
    
    function generateErrorResults() {
        return `
            <h4>Error Prevention Analysis Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Error Types Identified</h5>
                    <ul>
                        <li>Data entry errors: 45%</li>
                        <li>Selection errors: 30%</li>
                        <li>Navigation errors: 15%</li>
                        <li>System errors: 10%</li>
                    </ul>
                </div>
                
                <div class="result-item">
                    <h5>Risk Assessment</h5>
                    <p>High-risk errors: 12 identified</p>
                    <p>Medium-risk errors: 28 identified</p>
                    <p>Low-risk errors: 45 identified</p>
                </div>
                
                <div class="result-item">
                    <h5>Prevention Measures</h5>
                    <p>Current coverage: 65%</p>
                    <p>Recommended coverage: 90%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 65%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Implement input validation</li>
                    <li>Add confirmation dialogs for critical actions</li>
                    <li>Improve error messaging</li>
                    <li>Provide undo functionality</li>
                </ul>
            </div>
        `;
    }
    
    function generateResponseResults() {
        return `
            <h4>System Response Time Analysis Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>PACS Image Loading</h5>
                    <p>Current: 3.2 seconds (target: 2.0s)</p>
                    <p>Peak hours: 4.8 seconds</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 63%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>EHR Record Access</h5>
                    <p>Current: 1.8 seconds (target: 1.0s)</p>
                    <p>95th percentile: 3.5 seconds</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 56%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Report Generation</h5>
                    <p>Current: 45 seconds (target: 30s)</p>
                    <p>Large reports: 120 seconds</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 67%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Implement caching strategies</li>
                    <li>Optimize database queries</li>
                    <li>Upgrade network infrastructure</li>
                    <li>Add load balancing</li>
                </ul>
            </div>
        `;
    }
    
    function generateAccuracyResults() {
        return `
            <h4>Data Accuracy Validation Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Patient Data Accuracy</h5>
                    <p>Overall accuracy: 98.7%</p>
                    <p>Error rate: 1.3%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 99%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Medication Records</h5>
                    <p>Accuracy: 99.2%</p>
                    <p>Critical errors: 0.1%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 99%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Lab Results</h5>
                    <p>Accuracy: 99.8%</p>
                    <p>Transcription errors: 0.2%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 100%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Implement automated data validation</li>
                    <li>Add duplicate detection</li>
                    <li>Enhance audit trails</li>
                    <li>Regular accuracy audits</li>
                </ul>
            </div>
        `;
    }
    
    function generateComplianceResults() {
        return `
            <h4>ISO 9241 Compliance Assessment Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Overall Compliance</h5>
                    <p>Score: 85/100</p>
                    <p>Level: Good</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 85%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Dialogue Principles (ISO 9241-110)</h5>
                    <p>Score: 82/100</p>
                    <p>Strong in controllability, weak in self-descriptiveness</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 82%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Visual Display (ISO 9241-303)</h5>
                    <p>Score: 78/100</p>
                    <p>Good readability, needs contrast improvements</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 78%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Input Devices (ISO 9241-410)</h5>
                    <p>Score: 88/100</p>
                    <p>Excellent device standards compliance</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 88%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Improve system self-descriptiveness</li>
                    <li>Fix color contrast ratios</li>
                    <li>Enhance error messaging</li>
                    <li>Document compliance procedures</li>
                </ul>
            </div>
        `;
    }
    
    function generateAccessibilityResults() {
        return `
            <h4>Accessibility Audit Results</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>WCAG 2.1 AA Compliance</h5>
                    <p>Score: 78/100</p>
                    <p>12 issues identified</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 78%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Keyboard Navigation</h5>
                    <p>Score: 85/100</p>
                    <p>Most functions accessible via keyboard</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 85%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Screen Reader Support</h5>
                    <p>Score: 72/100</p>
                    <p>Needs ARIA labels and semantic markup</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 72%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Color Contrast</h5>
                    <p>Score: 65/100</p>
                    <p>3 modules below minimum contrast ratios</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 65%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Key Recommendations:</h5>
                <ul>
                    <li>Fix color contrast issues</li>
                    <li>Add ARIA labels and roles</li>
                    <li>Improve semantic HTML structure</li>
                    <li>Test with screen readers</li>
                </ul>
            </div>
        `;
    }
    
    // Animate progress bars when they come into view
    function animateProgressBars() {
        const progressBars = document.querySelectorAll('.progress-fill');
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';
            setTimeout(() => {
                bar.style.width = width;
            }, 500);
        });
    }
    
    // Observe when results section becomes visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateProgressBars();
            }
        });
    });
    
    observer.observe(document.getElementById('toolResults'));
    
    // Notification system
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
    
    // Initialize with scenario section visible
    showSection('scenario');
});
```

### Step 4: Python Case Study Analysis Script
Create a `case_study_analysis.py` file:

```python
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from typing import Dict, List, Tuple, Any
import numpy as np
from collections import defaultdict

class CaseStudyAnalyzer:
    def __init__(self):
        self.case_data = {}
        self.analysis_results = {}
        self.assessment_data = {}
    
    def load_case_data(self, file_path: str):
        """Load case study assessment data"""
        with open(file_path, 'r') as f:
            self.case_data = json.load(f)
    
    def load_assessment_results(self, assessment_files: List[str]):
        """Load results from individual assessment tools"""
        for file_path in assessment_files:
            tool_name = file_path.split('/')[-1].replace('.json', '')
            with open(file_path, 'r') as f:
                self.assessment_data[tool_name] = json.load(f)
    
    def perform_integrated_analysis(self) -> Dict[str, Any]:
        """Perform comprehensive integrated analysis"""
        analysis = {
            'system_overview': self.analyze_system_overview(),
            'integrated_findings': self.analyze_integrated_findings(),
            'standards_compliance': self.analyze_standards_compliance(),
            'impact_assessment': self.analyze_impact_assessment(),
            'recommendations': self.generate_integrated_recommendations(),
            'implementation_plan': self.create_implementation_plan(),
            'success_metrics': self.define_success_metrics(),
            'generated_at': datetime.now().isoformat()
        }
        
        return analysis
    
    def analyze_system_overview(self) -> Dict[str, Any]:
        """Analyze overall system characteristics"""
        return {
            'system_name': 'Smart Healthcare System',
            'organization': 'Metropolitan General Hospital',
            'user_base': '500+ healthcare professionals',
            'daily_volume': '10,000+ patient records',
            'critical_components': [
                'Electronic Health Records (EHR)',
                'Picture Archiving and Communication System (PACS)',
                'Patient Monitoring Dashboard',
                'Telemedicine Platform',
                'Mobile Applications'
            ],
            'key_requirements': [
                '24/7 system availability',
                'HIPAA compliance',
                'Real-time data accuracy',
                'Intuitive user interfaces',
                'Ergonomic design'
            ]
        }
    
    def analyze_integrated_findings(self) -> Dict[str, Any]:
        """Analyze findings across all assessment areas"""
        findings = {
            'ergonomic_issues': self._analyze_ergonomic_findings(),
            'usability_problems': self._analyze_usability_findings(),
            'performance_issues': self._analyze_performance_findings(),
            'compliance_gaps': self._analyze_compliance_findings(),
            'overall_assessment': self._calculate_overall_assessment()
        }
        
        return findings
    
    def _analyze_ergonomic_findings(self) -> Dict[str, Any]:
        """Analyze ergonomic assessment findings"""
        return {
            'monitor_positioning': {
                'score': 75,
                'issues': '40% suboptimal height',
                'severity': 'Medium',
                'affected_users': '200+ workstations'
            },
            'keyboard_setup': {
                'score': 68,
                'issues': '25% lack adjustable trays',
                'severity': 'Medium',
                'affected_users': '125+ users'
            },
            'chair_ergonomics': {
                'score': 72,
                'issues': 'Inadequate support',
                'severity': 'Medium',
                'affected_users': '300+ users'
            },
            'lighting_conditions': {
                'score': 65,
                'issues': 'Glare and insufficient lighting',
                'severity': 'High',
                'affected_users': 'Radiology department'
            }
        }
    
    def _analyze_usability_findings(self) -> Dict[str, Any]:
        """Analyze usability assessment findings"""
        return {
            'navigation_efficiency': {
                'score': 47,
                'issues': '8.5 clicks per task',
                'target': '4 clicks maximum',
                'impact': 'High'
            },
            'task_completion': {
                'score': 64,
                'issues': '12.5 min per record',
                'target': '8 min',
                'impact': 'High'
            },
            'error_prevention': {
                'score': 65,
                'issues': 'Multiple error types',
                'prevention_coverage': '65%',
                'impact': 'Critical'
            }
        }
    
    def _analyze_performance_findings(self) -> Dict[str, Any]:
        """Analyze performance assessment findings"""
        return {
            'pacs_loading': {
                'current': '3.2s',
                'target': '2.0s',
                'peak_performance': '4.8s',
                'impact': 'High'
            },
            'ehr_access': {
                'current': '1.8s',
                'target': '1.0s',
                'percentile_95': '3.5s',
                'impact': 'Medium'
            },
            'data_accuracy': {
                'overall': '98.7%',
                'medication_records': '99.2%',
                'lab_results': '99.8%',
                'impact': 'Critical'
            }
        }
    
    def _analyze_compliance_findings(self) -> Dict[str, Any]:
        """Analyze compliance assessment findings"""
        return {
            'iso9241_overall': {
                'score': 85,
                'level': 'Good',
                'strengths': ['Input devices', 'Dialogue principles'],
                'weaknesses': ['Visual display', 'Self-descriptiveness']
            },
            'accessibility': {
                'wcag_score': 78,
                'issues': 12,
                'keyboard_navigation': 85,
                'screen_reader_support': 72,
                'color_contrast': 65
            },
            'hipaa_compliance': {
                'score': 92,
                'audit_trails': 'Complete',
                'access_controls': 'Strong',
                'data_encryption': 'Adequate'
            }
        }
    
    def _calculate_overall_assessment(self) -> Dict[str, Any]:
        """Calculate overall system assessment"""
        categories = ['ergonomics', 'usability', 'performance', 'compliance']
        scores = [71, 59, 72, 85]  # Average scores from findings
        
        overall_score = sum(scores) / len(scores)
        
        return {
            'overall_score': round(overall_score, 1),
            'category_scores': dict(zip(categories, scores)),
            'assessment_level': self._get_assessment_level(overall_score),
            'critical_issues': 12,
            'high_priority_items': 8,
            'medium_priority_items': 15
        }
    
    def _get_assessment_level(self, score: float) -> str:
        """Get assessment level based on score"""
        if score >= 90:
            return 'Excellent'
        elif score >= 80:
            return 'Good'
        elif score >= 70:
            return 'Fair'
        elif score >= 60:
            return 'Poor'
        else:
            return 'Critical'
    
    def analyze_standards_compliance(self) -> Dict[str, Any]:
        """Analyze compliance with ISO 9241 standards"""
        return {
            'iso9241_110': {  # Dialogue principles
                'compliance_score': 82,
                'suitability_for_task': 85,
                'self_descriptiveness': 75,
                'controllability': 88,
                'conformity_with_expectations': 80,
                'error_tolerance': 82,
                'suitability_for_learning': 78
            },
            'iso9241_210': {  # Human-centred design
                'compliance_score': 79,
                'context_of_use': 85,
                'user_requirements': 75,
                'design_solutions': 80,
                'evaluation_designs': 78
            },
            'iso9241_303': {  # Visual display
                'compliance_score': 78,
                'legibility': 82,
                'readability': 75,
                'visual_ergonomics': 80,
                'compliance_checking': 76
            },
            'iso9241_410': {  # Input devices
                'compliance_score': 88,
                'ergonomic_design': 90,
                'operating_force': 85,
                'key_travel': 88,
                'tactile_feedback': 86,
                'accessibility': 92
            }
        }
    
    def analyze_impact_assessment(self) -> Dict[str, Any]:
        """Analyze impact of identified issues"""
        return {
            'user_impact': {
                'ergonomic_issues': 'High',
                'usability_problems': 'High',
                'performance_issues': 'Medium',
                'compliance_gaps': 'Medium'
            },
            'patient_safety': {
                'ergonomic_issues': 'Medium',
                'usability_problems': 'High',
                'performance_issues': 'High',
                'compliance_gaps': 'Critical'
            },
            'operational_cost': {
                'ergonomic_issues': 'Medium',
                'usability_problems': 'High',
                'performance_issues': 'Medium',
                'compliance_gaps': 'Low'
            },
            'risk_assessment': {
                'high_risk_issues': 5,
                'medium_risk_issues': 12,
                'low_risk_issues': 18,
                'total_risks': 35
            }
        }
    
    def generate_integrated_recommendations(self) -> List[Dict[str, Any]]:
        """Generate integrated recommendations"""
        recommendations = [
            {
                'phase': 'Critical Fixes (0-3 months)',
                'priority': 'Critical',
                'category': 'Compliance',
                'title': 'Fix Color Contrast Issues',
                'description': 'Update UI color schemes to meet WCAG AA standards',
                'effort': 'Low',
                'impact': 'High',
                'timeline': '1 month'
            },
            {
                'phase': 'Critical Fixes (0-3 months)',
                'priority': 'Critical',
                'category': 'Performance',
                'title': 'Optimize PACS Response Times',
                'description': 'Implement caching and optimize database queries',
                'effort': 'Medium',
                'impact': 'High',
                'timeline': '2 months'
            },
            {
                'phase': 'Critical Fixes (0-3 months)',
                'priority': 'Critical',
                'category': 'Usability',
                'title': 'Improve EHR Navigation',
                'description': 'Redesign workflow to reduce clicks by 50%',
                'effort': 'High',
                'impact': 'High',
                'timeline': '3 months'
            },
            {
                'phase': 'Major Improvements (3-6 months)',
                'priority': 'High',
                'category': 'Ergonomics',
                'title': 'Ergonomic Workstation Upgrades',
                'description': 'Replace outdated equipment and provide adjustable furniture',
                'effort': 'High',
                'impact': 'Medium',
                'timeline': '4 months'
            },
            {
                'phase': 'Major Improvements (3-6 months)',
                'priority': 'High',
                'category': 'Training',
                'title': 'Enhanced Training Program',
                'description': 'Develop role-specific training modules and quick reference guides',
                'effort': 'Medium',
                'impact': 'High',
                'timeline': '5 months'
            },
            {
                'phase': 'Major Improvements (3-6 months)',
                'priority': 'High',
                'category': 'Performance',
                'title': 'Mobile App Optimization',
                'description': 'Improve performance and add offline capabilities',
                'effort': 'Medium',
                'impact': 'Medium',
                'timeline': '6 months'
            }
        ]
        
        return recommendations
    
    def create_implementation_plan(self) -> Dict[str, Any]:
        """Create detailed implementation plan"""
        return {
            'phase_1': {
                'duration': 'Months 1-2',
                'focus': 'Assessment & Planning',
                'activities': [
                    'Complete detailed requirements analysis',
                    'Develop implementation roadmap',
                    'Establish success metrics',
                    'Secure stakeholder buy-in'
                ]
            },
            'phase_2': {
                'duration': 'Months 3-4',
                'focus': 'Critical Fixes Implementation',
                'activities': [
                    'Deploy Phase 1 recommendations',
                    'Conduct user acceptance testing',
                    'Provide training on new features',
                    'Monitor system performance'
                ]
            },
            'phase_3': {
                'duration': 'Months 5-8',
                'focus': 'Major Improvements',
                'activities': [
                    'Implement Phase 2 recommendations',
                    'Conduct comprehensive testing',
                    'Roll out changes in phases',
                    'Gather user feedback'
                ]
            },
            'phase_4': {
                'duration': 'Months 9-12',
                'focus': 'Optimization & Enhancement',
                'activities': [
                    'Deploy advanced features',
                    'Optimize system performance',
                    'Conduct final evaluation',
                    'Document lessons learned'
                ]
            }
        }
    
    def define_success_metrics(self) -> Dict[str, Any]:
        """Define success metrics for the case study"""
        return {
            'user_satisfaction': {
                'target': '90%',
                'current': '82%',
                'measurement': 'Quarterly surveys'
            },
            'task_completion_time': {
                'target': '25% reduction',
                'current': 'Baseline established',
                'measurement': 'Time tracking system'
            },
            'error_rate': {
                'target': '50% reduction',
                'current': 'Baseline established',
                'measurement': 'Error logging system'
            },
            'system_uptime': {
                'target': '99.9%',
                'current': '99.5%',
                'measurement': 'System monitoring'
            },
            'compliance_score': {
                'target': '95%',
                'current': '85%',
                'measurement': 'Automated compliance checking'
            },
            'training_time': {
                'target': '30% reduction',
                'current': 'Baseline established',
                'measurement': 'Training completion tracking'
            }
        }
    
    def generate_comprehensive_report(self) -> Dict[str, Any]:
        """Generate comprehensive case study report"""
        analysis = self.perform_integrated_analysis()
        
        report = {
            'case_study_title': 'Smart Healthcare System ISO 9241 Compliance Assessment',
            'organization': 'Metropolitan General Hospital',
            'assessment_date': datetime.now().isoformat(),
            'assessors': ['ISO 9241 Expert Team'],
            'executive_summary': self._generate_executive_summary(analysis),
            'methodology': 'Integrated multi-standard assessment framework',
            'findings': analysis,
            'conclusions': self._generate_conclusions(analysis),
            'next_steps': 'Implementation of prioritized recommendations'
        }
        
        return report
    
    def _generate_executive_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate executive summary"""
        overall_score = analysis['integrated_findings']['overall_assessment']['overall_score']
        
        return f"""
        The Metropolitan General Hospital's Smart Healthcare System underwent a comprehensive 
        ISO 9241 compliance assessment. The system received an overall score of {overall_score}%, 
        indicating good performance with significant room for improvement. 
        
        Key findings include 12 critical issues requiring immediate attention, strong compliance 
        foundation (85% ISO 9241 compliance), and opportunities for substantial usability and 
        performance enhancements. The assessment covered ergonomics, usability, performance, 
        and compliance across all major system components.
        
        Implementation of the recommended improvements is expected to significantly enhance 
        user satisfaction, reduce errors, and improve patient safety outcomes.
        """
    
    def _generate_conclusions(self, analysis: Dict[str, Any]) -> str:
        """Generate conclusions"""
        return """
        This comprehensive case study demonstrates the value of integrated ISO 9241 assessment 
        in healthcare systems. The multi-dimensional evaluation approach successfully identified 
        critical issues across ergonomics, usability, performance, and compliance domains.
        
        The healthcare context presents unique challenges that require careful balancing of 
        user needs, patient safety requirements, and operational efficiency. The assessment 
        revealed that while the system has a solid foundation, significant improvements are 
        needed in usability and visual ergonomics to meet the demanding requirements of 
        healthcare professionals.
        
        The prioritized implementation plan provides a clear roadmap for systematic improvement, 
        with expected benefits in user satisfaction, error reduction, and operational efficiency.
        """
    
    def save_report(self, file_path: str = 'case_study_report.json'):
        """Save comprehensive report to file"""
        report = self.generate_comprehensive_report()
        
        with open(file_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"Case study report saved: {file_path}")
        return report
    
    def create_visualizations(self, save_path: str = 'case_study_analysis.png'):
        """Create comprehensive visualizations"""
        analysis = self.perform_integrated_analysis()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Overall assessment scores
        categories = ['Ergonomics', 'Usability', 'Performance', 'Compliance']
        scores = [
            71, 59, 72, 85  # From integrated findings
        ]
        
        bars = ax1.bar(categories, scores, color=['red', 'orange', 'yellow', 'green'])
        ax1.set_ylim(0, 100)
        ax1.set_title('Assessment Scores by Category', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Score (%)', fontsize=12)
        ax1.axhline(y=80, color='green', linestyle='--', alpha=0.7, label='Good')
        ax1.axhline(y=60, color='orange', linestyle='--', alpha=0.7, label='Needs Improvement')
        ax1.legend()
        
        # Add value labels
        for bar, score in zip(bars, scores):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_y() + score + 1, 
                    f'{score}', ha='center', va='bottom', fontweight='bold')
        
        # Standards compliance
        standards = ['ISO 9241-110', 'ISO 9241-210', 'ISO 9241-303', 'ISO 9241-410']
        compliance_scores = [82, 79, 78, 88]
        
        ax2.bar(standards, compliance_scores, color='lightblue')
        ax2.set_ylim(0, 100)
        ax2.set_title('ISO 9241 Standards Compliance', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Compliance Score (%)', fontsize=12)
        ax2.tick_params(axis='x', rotation=45)
        
        # Impact assessment
        impact_categories = ['User Impact', 'Patient Safety', 'Operational Cost']
        ergonomic_impact = [3, 2, 2]  # High, Medium, Medium
        usability_impact = [3, 3, 3]  # High, High, High
        performance_impact = [2, 3, 2]  # Medium, High, Medium
        compliance_impact = [2, 4, 1]  # Medium, Critical, Low
        
        x = np.arange(len(impact_categories))
        width = 0.2
        
        ax3.bar(x - 1.5*width, ergonomic_impact, width, label='Ergonomics', color='red')
        ax3.bar(x - 0.5*width, usability_impact, width, label='Usability', color='orange')
        ax3.bar(x + 0.5*width, performance_impact, width, label='Performance', color='yellow')
        ax3.bar(x + 1.5*width, compliance_impact, width, label='Compliance', color='green')
        
        ax3.set_title('Impact Assessment by Category', fontsize=14, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(impact_categories)
        ax3.set_ylabel('Impact Level (1-4)', fontsize=12)
        ax3.legend()
        
        # Priority recommendations timeline
        phases = ['Phase 1\n(0-3 months)', 'Phase 2\n(3-6 months)', 'Phase 3\n(6-12 months)']
        critical_items = [3, 0, 0]
        high_items = [0, 3, 0]
        medium_items = [0, 0, 3]
        
        ax4.bar(phases, critical_items, label='Critical', color='red')
        ax4.bar(phases, high_items, bottom=critical_items, label='High', color='orange')
        ax4.bar(phases, medium_items, bottom=[c + h for c, h in zip(critical_items, high_items)], 
               label='Medium', color='yellow')
        
        ax4.set_title('Implementation Timeline', fontsize=14, fontweight='bold')
        ax4.set_ylabel('Number of Recommendations', fontsize=12)
        ax4.legend()
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Case study visualizations saved: {save_path}")

# Example usage
if __name__ == "__main__":
    analyzer = CaseStudyAnalyzer()
    
    # Generate comprehensive case study analysis
    report = analyzer.save_report()
    
    print("Case Study Analysis Complete")
    print(f"Overall Assessment Score: {report['findings']['integrated_findings']['overall_assessment']['overall_score']}%")
    print(f"Critical Issues Identified: {report['findings']['integrated_findings']['overall_assessment']['critical_issues']}")
    print(f"Compliance Score: {report['findings']['standards_compliance']['iso9241_110']['compliance_score']}%")
    
    # Create visualizations
    analyzer.create_visualizations()
```

### Step 5: Documentation
This comprehensive case study integrates all ISO 9241 standards covered in the laboratory series into a real-world healthcare system assessment. The case study demonstrates the application of ergonomic principles, usability evaluation, and compliance verification across a complex, mission-critical system.

Key features:
- **Integrated Assessment Framework**: Combines all ISO 9241 standards (110, 210, 303, 410) into a cohesive evaluation methodology
- **Real-World Scenario**: Smart healthcare system with multiple user groups and critical requirements
- **Multi-Dimensional Analysis**: Ergonomics, usability, performance, and compliance assessment
- **Interactive Dashboard**: Web-based interface for exploring case study findings and recommendations
- **Comprehensive Reporting**: Detailed analysis with prioritized implementation plan
- **Visual Analytics**: Charts and graphs for data-driven insights

The case study provides a complete template for conducting integrated ISO 9241 assessments in complex organizational environments, with particular relevance to healthcare, but applicable to any industry requiring high usability and safety standards.
