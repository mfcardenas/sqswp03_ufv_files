# Lab 1: Introduction to Requirements Engineering

## Solution

### Step 1: Requirements Engineering Dashboard
Create a `requirements_intro.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISO/IEC/IEEE 29148 - Requirements Engineering Introduction</title>
    <link rel="stylesheet" href="requirements.css">
</head>
<body>
    <header>
        <h1>ISO/IEC/IEEE 29148: Requirements Engineering</h1>
        <nav>
            <button id="conceptsBtn">Core Concepts</button>
            <button id="processBtn">RE Process</button>
            <button id="artifactsBtn">Requirements Artifacts</button>
            <button id="stakeholdersBtn">Stakeholder Analysis</button>
            <button id="qualityBtn">Requirements Quality</button>
            <button id="standardsBtn">Standards Overview</button>
        </nav>
    </header>

    <main>
        <section class="core-concepts" id="conceptsSection">
            <h2>Core Concepts of Requirements Engineering</h2>
            
            <div class="concepts-grid">
                <div class="concept-card">
                    <h3>What is Requirements Engineering?</h3>
                    <p>The systematic process of developing requirements through an iterative process of analyzing, documenting, validating, and managing software and system requirements.</p>
                    <div class="concept-details">
                        <h4>Key Activities:</h4>
                        <ul>
                            <li>Requirements Elicitation</li>
                            <li>Requirements Analysis</li>
                            <li>Requirements Specification</li>
                            <li>Requirements Validation</li>
                            <li>Requirements Management</li>
                        </ul>
                    </div>
                </div>
                
                <div class="concept-card">
                    <h3>Types of Requirements</h3>
                    <div class="requirements-types">
                        <div class="req-type">
                            <h4>Functional Requirements</h4>
                            <p>What the system should do</p>
                            <ul>
                                <li>Business rules</li>
                                <li>User interactions</li>
                                <li>Data processing</li>
                                <li>System behaviors</li>
                            </ul>
                        </div>
                        
                        <div class="req-type">
                            <h4>Non-Functional Requirements</h4>
                            <p>How well the system should perform</p>
                            <ul>
                                <li>Performance</li>
                                <li>Security</li>
                                <li>Usability</li>
                                <li>Reliability</li>
                                <li>Scalability</li>
                            </ul>
                        </div>
                        
                        <div class="req-type">
                            <h4>Constraints</h4>
                            <p>Limitations and restrictions</p>
                            <ul>
                                <li>Technical constraints</li>
                                <li>Business constraints</li>
                                <li>Regulatory constraints</li>
                                <li>Budget constraints</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="concept-card">
                    <h3>Requirements Engineering Challenges</h3>
                    <div class="challenges-list">
                        <div class="challenge-item">
                            <h4>Communication Gap</h4>
                            <p>Different stakeholders use different terminology</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Requirements Volatility</h4>
                            <p>Requirements change over time</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Ambiguity</h4>
                            <p>Requirements can be interpreted differently</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Incompleteness</h4>
                            <p>Missing or unspecified requirements</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Traceability</h4>
                            <p>Maintaining links between requirements and other artifacts</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="re-process" id="processSection" style="display: none;">
            <h2>Requirements Engineering Process (ISO/IEC/IEEE 29148)</h2>
            
            <div class="process-overview">
                <h3>Requirements Engineering Lifecycle</h3>
                <div class="process-diagram">
                    <div class="process-step" data-step="1">
                        <h4>Requirements Elicitation</h4>
                        <p>Identify and gather requirements from stakeholders</p>
                        <div class="step-details">
                            <h5>Techniques:</h5>
                            <ul>
                                <li>Interviews</li>
                                <li>Workshops</li>
                                <li>Questionnaires</li>
                                <li>Observation</li>
                                <li>Document Analysis</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="2">
                        <h4>Requirements Analysis</h4>
                        <p>Analyze and refine elicited requirements</p>
                        <div class="step-details">
                            <h5>Activities:</h5>
                            <ul>
                                <li>Requirements classification</li>
                                <li>Conflict resolution</li>
                                <li>Prioritization</li>
                                <li>Feasibility analysis</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="3">
                        <h4>Requirements Specification</h4>
                        <p>Document requirements in appropriate format</p>
                        <div class="step-details">
                            <h5>Artifacts:</h5>
                            <ul>
                                <li>Requirements Specification Document</li>
                                <li>Use Case Specifications</li>
                                <li>User Stories</li>
                                <li>Requirements Traceability Matrix</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="4">
                        <h4>Requirements Validation</h4>
                        <p>Ensure requirements are correct and complete</p>
                        <div class="step-details">
                            <h5>Validation Techniques:</h5>
                            <ul>
                                <li>Requirements reviews</li>
                                <li>Prototyping</li>
                                <li>Requirements testing</li>
                                <li>Acceptance criteria definition</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="5">
                        <h4>Requirements Management</h4>
                        <p>Maintain requirements throughout lifecycle</p>
                        <div class="step-details">
                            <h5>Management Activities:</h5>
                            <ul>
                                <li>Change control</li>
                                <li>Version control</li>
                                <li>Traceability maintenance</li>
                                <li>Requirements metrics</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="process-tools">
                <h3>Process Support Tools</h3>
                <div class="tool-buttons">
                    <button class="tool-btn" data-tool="elicitation">Elicitation Planner</button>
                    <button class="tool-btn" data-tool="analysis">Requirements Analyzer</button>
                    <button class="tool-btn" data-tool="validation">Validation Checklist</button>
                    <button class="tool-btn" data-tool="traceability">Traceability Builder</button>
                </div>
                
                <div class="tool-results" id="toolResults" style="display: none;">
                    <h4>Tool Results</h4>
                    <div id="resultsContent"></div>
                </div>
            </div>
        </section>

        <section class="requirements-artifacts" id="artifactsSection" style="display: none;">
            <h2>Requirements Artifacts</h2>
            
            <div class="artifacts-overview">
                <h3>Common Requirements Documents</h3>
                
                <div class="artifact-templates">
                    <div class="artifact-card">
                        <h4>Software Requirements Specification (SRS)</h4>
                        <p>Comprehensive document containing all software requirements</p>
                        <div class="artifact-structure">
                            <h5>Typical Structure:</h5>
                            <ol>
                                <li>Introduction</li>
                                <li>Overall Description</li>
                                <li>Specific Requirements</li>
                                <li>Appendices</li>
                            </ol>
                        </div>
                        <button class="template-btn" data-template="srs">View Template</button>
                    </div>
                    
                    <div class="artifact-card">
                        <h4>Use Case Specification</h4>
                        <p>Detailed description of user-system interactions</p>
                        <div class="artifact-structure">
                            <h5>Elements:</h5>
                            <ul>
                                <li>Use Case Name</li>
                                <li>Actors</li>
                                <li>Preconditions</li>
                                <li>Main Flow</li>
                                <li>Alternative Flows</li>
                                <li>Postconditions</li>
                            </ul>
                        </div>
                        <button class="template-btn" data-template="usecase">View Template</button>
                    </div>
                    
                    <div class="artifact-card">
                        <h4>User Story</h4>
                        <p>Simple, user-centric requirement description</p>
                        <div class="artifact-structure">
                            <h5>Format:</h5>
                            <p><strong>As a</strong> [type of user], <strong>I want</strong> [some goal] <strong>so that</strong> [some reason]</p>
                            <h5>Acceptance Criteria:</h5>
                            <ul>
                                <li>Given [context]</li>
                                <li>When [action]</li>
                                <li>Then [outcome]</li>
                            </ul>
                        </div>
                        <button class="template-btn" data-template="userstory">View Template</button>
                    </div>
                    
                    <div class="artifact-card">
                        <h4>Requirements Traceability Matrix</h4>
                        <p>Links requirements to other development artifacts</p>
                        <div class="artifact-structure">
                            <h5>Typical Columns:</h5>
                            <ul>
                                <li>Requirement ID</li>
                                <li>Description</li>
                                <li>Source</li>
                                <li>Test Case</li>
                                <li>Design Element</li>
                                <li>Code Module</li>
                            </ul>
                        </div>
                        <button class="template-btn" data-template="rtm">View Template</button>
                    </div>
                </div>
                
                <div class="template-viewer" id="templateViewer" style="display: none;">
                    <h4>Template Preview</h4>
                    <div id="templateContent"></div>
                    <button id="closeTemplate">Close</button>
                </div>
            </div>
        </section>

        <section class="stakeholder-analysis" id="stakeholdersSection" style="display: none;">
            <h2>Stakeholder Analysis</h2>
            
            <div class="stakeholder-tools">
                <h3>Stakeholder Identification and Analysis</h3>
                
                <div class="stakeholder-input">
                    <h4>Add Stakeholder</h4>
                    <form id="stakeholderForm">
                        <div class="form-group">
                            <label for="stakeholderName">Name:</label>
                            <input type="text" id="stakeholderName" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="stakeholderRole">Role:</label>
                            <input type="text" id="stakeholderRole" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="stakeholderInterest">Interest Level:</label>
                            <select id="stakeholderInterest">
                                <option value="high">High</option>
                                <option value="medium">Medium</option>
                                <option value="low">Low</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="stakeholderInfluence">Influence Level:</label>
                            <select id="stakeholderInfluence">
                                <option value="high">High</option>
                                <option value="medium">Medium</option>
                                <option value="low">Low</option>
                            </select>
                        </div>
                        
                        <button type="submit">Add Stakeholder</button>
                    </form>
                </div>
                
                <div class="stakeholder-list">
                    <h4>Stakeholder Map</h4>
                    <div id="stakeholderMap"></div>
                </div>
                
                <div class="power-interest-grid">
                    <h4>Power-Interest Grid</h4>
                    <div class="grid-container">
                        <div class="grid-quadrant" data-quadrant="high-high">
                            <h5>High Power, High Interest</h5>
                            <p>Key Players - Manage closely</p>
                            <div class="stakeholder-items" id="quadrant-high-high"></div>
                        </div>
                        
                        <div class="grid-quadrant" data-quadrant="high-low">
                            <h5>High Power, Low Interest</h5>
                            <p>Keep Satisfied</p>
                            <div class="stakeholder-items" id="quadrant-high-low"></div>
                        </div>
                        
                        <div class="grid-quadrant" data-quadrant="low-high">
                            <h5>Low Power, High Interest</h5>
                            <p>Keep Informed</p>
                            <div class="stakeholder-items" id="quadrant-low-high"></div>
                        </div>
                        
                        <div class="grid-quadrant" data-quadrant="low-low">
                            <h5>Low Power, Low Interest</h5>
                            <p>Monitor</p>
                            <div class="stakeholder-items" id="quadrant-low-low"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="requirements-quality" id="qualitySection" style="display: none;">
            <h2>Requirements Quality Assessment</h2>
            
            <div class="quality-framework">
                <h3>Requirements Quality Criteria (ISO/IEC/IEEE 29148)</h3>
                
                <div class="quality-criteria">
                    <div class="quality-category">
                        <h4>Completeness</h4>
                        <p>All requirements are defined and no necessary requirements are missing</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> All functional requirements specified</label>
                            <label><input type="checkbox"> All non-functional requirements specified</label>
                            <label><input type="checkbox"> All constraints identified</label>
                            <label><input type="checkbox"> Response to all inputs defined</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Consistency</h4>
                        <p>Requirements do not contradict each other</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> No conflicting requirements</label>
                            <label><input type="checkbox"> Consistent terminology used</label>
                            <label><input type="checkbox"> Consistent format and structure</label>
                            <label><input type="checkbox"> Consistent level of detail</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Clarity</h4>
                        <p>Requirements are unambiguous and understandable</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> Clear and concise language</label>
                            <label><input type="checkbox"> Unambiguous terms</label>
                            <label><input type="checkbox"> Measurable criteria</label>
                            <label><input type="checkbox"> Testable requirements</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Correctness</h4>
                        <p>Requirements accurately reflect stakeholder needs</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> Validated with stakeholders</label>
                            <label><input type="checkbox"> Aligned with business objectives</label>
                            <label><input type="checkbox"> Technically feasible</label>
                            <label><input type="checkbox"> Compliant with standards</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Traceability</h4>
                        <p>Requirements can be traced to sources and implementations</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> Unique identifiers assigned</label>
                            <label><input type="checkbox"> Source documented</label>
                            <label><input type="checkbox"> Links to design elements</label>
                            <label><input type="checkbox"> Links to test cases</label>
                        </div>
                    </div>
                </div>
                
                <div class="quality-assessment">
                    <h4>Quality Assessment Results</h4>
                    <div class="assessment-results">
                        <div class="quality-score">
                            <span class="score-label">Overall Quality Score:</span>
                            <span class="score-value" id="qualityScore">0%</span>
                        </div>
                        <button id="assessQuality">Assess Quality</button>
                    </div>
                </div>
            </div>
        </section>

        <section class="standards-overview" id="standardsSection" style="display: none;">
            <h2>ISO/IEC/IEEE 29148 Standards Overview</h2>
            
            <div class="standards-content">
                <h3>Standard Structure and Content</h3>
                
                <div class="standard-sections">
                    <div class="standard-card">
                        <h4>Section 1: Scope</h4>
                        <p>Defines the scope and purpose of the standard</p>
                        <ul>
                            <li>Requirements engineering processes</li>
                            <li>Requirements artifacts</li>
                            <li>Requirements management</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Section 2: Normative References</h4>
                        <p>References to other standards and documents</p>
                        <ul>
                            <li>ISO/IEC 12207 - Software Life Cycle</li>
                            <li>ISO/IEC 15288 - System Life Cycle</li>
                            <li>IEEE 830 - Software Requirements</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Section 3: Terms and Definitions</h4>
                        <p>Definitions of key terms and concepts</p>
                        <ul>
                            <li>Requirements engineering</li>
                            <li>Stakeholder</li>
                            <li>Requirements traceability</li>
                            <li>Requirements validation</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Section 4: Requirements Engineering Process</h4>
                        <p>Core processes and activities</p>
                        <ul>
                            <li>Requirements elicitation</li>
                            <li>Requirements analysis</li>
                            <li>Requirements specification</li>
                            <li>Requirements validation</li>
                            <li>Requirements management</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Section 5: Requirements Artifacts</h4>
                        <p>Documents and deliverables</p>
                        <ul>
                            <li>Requirements specification</li>
                            <li>Requirements traceability matrix</li>
                            <li>Requirements change requests</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Annexes</h4>
                        <p>Supporting information and examples</p>
                        <ul>
                            <li>Requirements templates</li>
                            <li>Process examples</li>
                            <li>Best practices</li>
                        </ul>
                    </div>
                </div>
                
                <div class="standard-benefits">
                    <h4>Benefits of Following ISO/IEC/IEEE 29148</h4>
                    <div class="benefits-grid">
                        <div class="benefit-item">
                            <h5>Improved Quality</h5>
                            <p>Better requirements lead to better software</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Reduced Risk</h5>
                            <p>Early identification of issues and conflicts</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Better Communication</h5>
                            <p>Clear requirements improve stakeholder understanding</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Cost Savings</h5>
                            <p>Fewer defects and rework</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Compliance</h5>
                            <p>Meets industry standards and regulations</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Traceability</h5>
                            <p>Better tracking of requirements throughout lifecycle</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="requirements.js"></script>
</body>
</html>
```

### Step 2: CSS for Requirements Engineering Dashboard
Create a `requirements.css` file:

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
    background-color: #2c3e50;
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
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
}

nav button:hover, nav button:focus, nav button.active {
    background-color: rgba(255, 255, 255, 0.2);
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
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
    margin-bottom: 2rem;
}

h3 {
    color: #3498db;
    margin-bottom: 1rem;
}

h4 {
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

/* Core Concepts Section */
.concepts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.concept-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.requirements-types {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.req-type {
    background-color: white;
    padding: 1rem;
    border-radius: 6px;
    border: 1px solid #dee2e6;
}

.challenges-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.challenge-item {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    padding: 1rem;
    border-radius: 6px;
}

.challenge-item h4 {
    margin-top: 0;
    color: #856404;
}

/* Process Section */
.process-diagram {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.process-step {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    position: relative;
}

.process-step::before {
    content: attr(data-step);
    position: absolute;
    top: -10px;
    left: -10px;
    background-color: #3498db;
    color: white;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}

.step-details {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid #dee2e6;
}

.tool-buttons {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin: 2rem 0;
}

.tool-btn {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.tool-btn:hover {
    background-color: #2980b9;
}

/* Artifacts Section */
.artifact-templates {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.artifact-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.template-btn {
    background-color: #27ae60;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
    transition: background-color 0.3s ease;
}

.template-btn:hover {
    background-color: #229954;
}

.template-viewer {
    background-color: #f8f9fa;
    padding: 2rem;
    border-radius: 8px;
    margin-top: 2rem;
    border: 1px solid #dee2e6;
}

/* Stakeholder Analysis Section */
.stakeholder-input {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    border: 1px solid #dee2e6;
}

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
}

.stakeholder-input button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.stakeholder-input button:hover {
    background-color: #2980b9;
}

.power-interest-grid {
    margin-top: 2rem;
}

.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 1rem;
    height: 400px;
}

.grid-quadrant {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    position: relative;
}

.grid-quadrant h5 {
    margin-top: 0;
    color: #2c3e50;
}

.stakeholder-items {
    margin-top: 1rem;
}

.stakeholder-item {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    font-size: 0.9rem;
}

/* Quality Assessment Section */
.quality-criteria {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.quality-category {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.quality-checklist {
    margin-top: 1rem;
}

.quality-checklist label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.assessment-results {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 2rem;
    border: 1px solid #dee2e6;
    text-align: center;
}

.quality-score {
    margin-bottom: 1rem;
}

.score-label {
    font-weight: bold;
    margin-right: 1rem;
}

.score-value {
    font-size: 1.5rem;
    color: #27ae60;
    font-weight: bold;
}

.assessment-results button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.assessment-results button:hover {
    background-color: #2980b9;
}

/* Standards Overview Section */
.standard-sections {
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

.benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 2rem;
}

.benefit-item {
    background-color: #d4edda;
    padding: 1rem;
    border-radius: 6px;
    text-align: center;
    border: 1px solid #c3e6cb;
}

.benefit-item h5 {
    margin-top: 0;
    color: #155724;
}

/* Notification */
.notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #3498db;
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
    
    .concepts-grid, .process-diagram, .artifact-templates, 
    .quality-criteria, .standard-sections, .requirements-types,
    .challenges-list, .benefits-grid {
        grid-template-columns: 1fr;
    }
    
    .grid-container {
        grid-template-columns: 1fr;
        grid-template-rows: repeat(4, 1fr);
        height: auto;
    }
}
```

### Step 3: JavaScript for Requirements Engineering Dashboard
Create a `requirements.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Navigation system
    const sections = {
        concepts: document.getElementById('conceptsSection'),
        process: document.getElementById('processSection'),
        artifacts: document.getElementById('artifactsSection'),
        stakeholders: document.getElementById('stakeholdersSection'),
        quality: document.getElementById('qualitySection'),
        standards: document.getElementById('standardsSection')
    };
    
    // Navigation buttons
    document.getElementById('conceptsBtn').addEventListener('click', () => showSection('concepts'));
    document.getElementById('processBtn').addEventListener('click', () => showSection('process'));
    document.getElementById('artifactsBtn').addEventListener('click', () => showSection('artifacts'));
    document.getElementById('stakeholdersBtn').addEventListener('click', () => showSection('stakeholders'));
    document.getElementById('qualityBtn').addEventListener('click', () => showSection('quality'));
    document.getElementById('standardsBtn').addEventListener('click', () => showSection('standards'));
    
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
    
    // Stakeholder management
    let stakeholders = [];
    
    document.getElementById('stakeholderForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('stakeholderName').value;
        const role = document.getElementById('stakeholderRole').value;
        const interest = document.getElementById('stakeholderInterest').value;
        const influence = document.getElementById('stakeholderInfluence').value;
        
        const stakeholder = {
            id: Date.now(),
            name: name,
            role: role,
            interest: interest,
            influence: influence
        };
        
        stakeholders.push(stakeholder);
        updateStakeholderDisplay();
        
        // Reset form
        this.reset();
        showNotification(`Added stakeholder: ${name}`);
    });
    
    function updateStakeholderDisplay() {
        // Clear all quadrants
        document.querySelectorAll('.stakeholder-items').forEach(quadrant => {
            quadrant.innerHTML = '';
        });
        
        // Add stakeholders to appropriate quadrants
        stakeholders.forEach(stakeholder => {
            const quadrantId = `quadrant-${stakeholder.influence}-${stakeholder.interest}`;
            const quadrant = document.getElementById(quadrantId);
            
            if (quadrant) {
                const item = document.createElement('div');
                item.className = 'stakeholder-item';
                item.textContent = `${stakeholder.name} (${stakeholder.role})`;
                quadrant.appendChild(item);
            }
        });
    }
    
    // Template viewer
    document.querySelectorAll('.template-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const templateType = this.dataset.template;
            showTemplate(templateType);
        });
    });
    
    document.getElementById('closeTemplate').addEventListener('click', function() {
        document.getElementById('templateViewer').style.display = 'none';
    });
    
    function showTemplate(templateType) {
        const viewer = document.getElementById('templateViewer');
        const content = document.getElementById('templateContent');
        
        let templateContent = '';
        
        switch(templateType) {
            case 'srs':
                templateContent = getSRSTemplate();
                break;
            case 'usecase':
                templateContent = getUseCaseTemplate();
                break;
            case 'userstory':
                templateContent = getUserStoryTemplate();
                break;
            case 'rtm':
                templateContent = getRTMTemplate();
                break;
        }
        
        content.innerHTML = templateContent;
        viewer.style.display = 'block';
    }
    
    function getSRSTemplate() {
        return `
            <h4>Software Requirements Specification Template</h4>
            <div class="template-content">
                <h5>1. Introduction</h5>
                <ul>
                    <li>1.1 Purpose</li>
                    <li>1.2 Scope</li>
                    <li>1.3 Definitions, Acronyms, and Abbreviations</li>
                    <li>1.4 References</li>
                    <li>1.5 Overview</li>
                </ul>
                
                <h5>2. Overall Description</h5>
                <ul>
                    <li>2.1 Product Perspective</li>
                    <li>2.2 Product Functions</li>
                    <li>2.3 User Characteristics</li>
                    <li>2.4 Constraints</li>
                    <li>2.5 Assumptions and Dependencies</li>
                </ul>
                
                <h5>3. Specific Requirements</h5>
                <ul>
                    <li>3.1 External Interface Requirements</li>
                    <li>3.2 Functional Requirements</li>
                    <li>3.3 Performance Requirements</li>
                    <li>3.4 Design Constraints</li>
                    <li>3.5 Software System Attributes</li>
                    <li>3.6 Other Requirements</li>
                </ul>
                
                <h5>Appendices</h5>
                <ul>
                    <li>Appendix A: Glossary</li>
                    <li>Appendix B: Analysis Models</li>
                    <li>Appendix C: Issues List</li>
                </ul>
            </div>
        `;
    }
    
    function getUseCaseTemplate() {
        return `
            <h4>Use Case Specification Template</h4>
            <div class="template-content">
                <h5>Use Case: [Use Case Name]</h5>
                
                <h6>1. Brief Description</h6>
                <p>[Brief description of the use case]</p>
                
                <h6>2. Actors</h6>
                <ul>
                    <li>Primary Actor: [Primary actor name]</li>
                    <li>Secondary Actors: [List of secondary actors]</li>
                </ul>
                
                <h6>3. Preconditions</h6>
                <ul>
                    <li>[Precondition 1]</li>
                    <li>[Precondition 2]</li>
                </ul>
                
                <h6>4. Main Success Scenario</h6>
                <ol>
                    <li>User [action]</li>
                    <li>System [response]</li>
                    <li>User [action]</li>
                    <li>System [response]</li>
                </ol>
                
                <h6>5. Alternative Flows</h6>
                <ul>
                    <li>Alternative Flow 1: [Description]</li>
                    <li>Alternative Flow 2: [Description]</li>
                </ul>
                
                <h6>6. Exception Flows</h6>
                <ul>
                    <li>Exception 1: [Description]</li>
                    <li>Exception 2: [Description]</li>
                </ul>
                
                <h6>7. Postconditions</h6>
                <ul>
                    <li>[Postcondition 1]</li>
                    <li>[Postcondition 2]</li>
                </ul>
                
                <h6>8. Business Rules</h6>
                <ul>
                    <li>[Business rule 1]</li>
                    <li>[Business rule 2]</li>
                </ul>
            </div>
        `;
    }
    
    function getUserStoryTemplate() {
        return `
            <h4>User Story Template</h4>
            <div class="template-content">
                <h5>User Story Format</h5>
                <div class="story-format">
                    <strong>As a</strong> [type of user],<br>
                    <strong>I want</strong> [some goal]<br>
                    <strong>so that</strong> [some reason].
                </div>
                
                <h6>Example:</h6>
                <div class="story-example">
                    <strong>As a</strong> bank customer,<br>
                    <strong>I want</strong> to transfer money between my accounts,<br>
                    <strong>so that</strong> I can manage my finances easily.
                </div>
                
                <h6>Acceptance Criteria:</h6>
                <ul>
                    <li><strong>Given</strong> I am logged into my account</li>
                    <li><strong>When</strong> I select transfer funds</li>
                    <li><strong>Then</strong> I should see my account balances</li>
                    <li><strong>And</strong> I should be able to select source and destination accounts</li>
                    <li><strong>And</strong> I should receive confirmation of successful transfer</li>
                </ul>
                
                <h6>Definition of Done:</h6>
                <ul>
                    <li>Code is written and reviewed</li>
                    <li>Unit tests are written and passing</li>
                    <li>Acceptance criteria are met</li>
                    <li>Documentation is updated</li>
                    <li>Product owner accepts the story</li>
                </ul>
            </div>
        `;
    }
    
    function getRTMTemplate() {
        return `
            <h4>Requirements Traceability Matrix Template</h4>
            <div class="template-content">
                <table class="rtm-table">
                    <thead>
                        <tr>
                            <th>Req ID</th>
                            <th>Description</th>
                            <th>Source</th>
                            <th>Priority</th>
                            <th>Test Case</th>
                            <th>Design Element</th>
                            <th>Code Module</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>REQ-001</td>
                            <td>User shall be able to login</td>
                            <td>Stakeholder Interview</td>
                            <td>High</td>
                            <td>TC-001</td>
                            <td>LoginController</td>
                            <td>AuthModule</td>
                            <td>Implemented</td>
                        </tr>
                        <tr>
                            <td>REQ-002</td>
                            <td>System shall validate password</td>
                            <td>Security Policy</td>
                            <td>High</td>
                            <td>TC-002</td>
                            <td>PasswordValidator</td>
                            <td>SecurityModule</td>
                            <td>Implemented</td>
                        </tr>
                        <tr>
                            <td>REQ-003</td>
                            <td>Response time < 2 seconds</td>
                            <td>Performance Req</td>
                            <td>Medium</td>
                            <td>TC-003</td>
                            <td>PerformanceMonitor</td>
                            <td>MonitoringModule</td>
                            <td>Testing</td>
                        </tr>
                    </tbody>
                </table>
                
                <h6>Traceability Types:</h6>
                <ul>
                    <li><strong>Forward Traceability:</strong> From requirements to design/code/tests</li>
                    <li><strong>Backward Traceability:</strong> From code/tests back to requirements</li>
                    <li><strong>Horizontal Traceability:</strong> Between requirements at same level</li>
                </ul>
            </div>
        `;
    }
    
    // Quality assessment
    document.getElementById('assessQuality').addEventListener('click', function() {
        const checkboxes = document.querySelectorAll('.quality-checklist input[type="checkbox"]');
        const checkedCount = document.querySelectorAll('.quality-checklist input[type="checkbox"]:checked').length;
        const totalCount = checkboxes.length;
        
        const score = Math.round((checkedCount / totalCount) * 100);
        document.getElementById('qualityScore').textContent = score + '%';
        
        showNotification(`Quality assessment completed: ${score}%`);
    });
    
    // Process tools
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
            case 'elicitation':
                results = generateElicitationPlanner();
                break;
            case 'analysis':
                results = generateRequirementsAnalyzer();
                break;
            case 'validation':
                results = generateValidationChecklist();
                break;
            case 'traceability':
                results = generateTraceabilityBuilder();
                break;
        }
        
        resultsContent.innerHTML = results;
        showNotification(`Launched ${toolType} tool`);
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    function generateElicitationPlanner() {
        return `
            <h4>Requirements Elicitation Planning Tool</h4>
            <div class="tool-results-content">
                <h5>Recommended Elicitation Techniques:</h5>
                <div class="technique-grid">
                    <div class="technique">
                        <h6>Interviews</h6>
                        <p>One-on-one discussions with stakeholders</p>
                        <ul>
                            <li>Best for: Detailed requirements</li>
                            <li>Time: 30-60 minutes per stakeholder</li>
                            <li>Preparation: Interview questions</li>
                        </ul>
                    </div>
                    
                    <div class="technique">
                        <h6>Workshops</h6>
                        <p>Group sessions with multiple stakeholders</p>
                        <ul>
                            <li>Best for: Resolving conflicts</li>
                            <li>Time: 2-4 hours</li>
                            <li>Preparation: Agenda and materials</li>
                        </ul>
                    </div>
                    
                    <div class="technique">
                        <h6>Questionnaires</h6>
                        <p>Structured surveys for large groups</p>
                        <ul>
                            <li>Best for: Quantitative data</li>
                            <li>Time: 15-30 minutes per respondent</li>
                            <li>Preparation: Clear questions</li>
                        </ul>
                    </div>
                    
                    <div class="technique">
                        <h6>Observation</h6>
                        <p>Watch users perform their tasks</p>
                        <ul>
                            <li>Best for: Understanding workflows</li>
                            <li>Time: 1-2 hours per session</li>
                            <li>Preparation: Observation protocol</li>
                        </ul>
                    </div>
                </div>
                
                <h5>Elicitation Plan Template:</h5>
                <div class="plan-template">
                    <h6>1. Stakeholder Identification</h6>
                    <ul>
                        <li>List all potential stakeholders</li>
                        <li>Prioritize based on interest and influence</li>
                        <li>Schedule interviews/workshops</li>
                    </ul>
                    
                    <h6>2. Preparation</h6>
                    <ul>
                        <li>Develop interview questions</li>
                        <li>Prepare workshop materials</li>
                        <li>Set up meeting logistics</li>
                    </ul>
                    
                    <h6>3. Execution</h6>
                    <ul>
                        <li>Conduct elicitation sessions</li>
                        <li>Take detailed notes</li>
                        <li>Record audio/video if permitted</li>
                    </ul>
                    
                    <h6>4. Follow-up</h6>
                    <ul>
                        <li>Send meeting summaries</li>
                        <li>Clarify any ambiguities</li>
                        <li>Schedule follow-up sessions if needed</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    function generateRequirementsAnalyzer() {
        return `
            <h4>Requirements Analysis Tool</h4>
            <div class="tool-results-content">
                <h5>Analysis Framework:</h5>
                <div class="analysis-framework">
                    <div class="analysis-step">
                        <h6>1. Requirements Classification</h6>
                        <ul>
                            <li>Functional vs Non-functional</li>
                            <li>Business vs Technical</li>
                            <li>Mandatory vs Optional</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-step">
                        <h6>2. Conflict Resolution</h6>
                        <ul>
                            <li>Identify conflicting requirements</li>
                            <li>Negotiate with stakeholders</li>
                            <li>Document resolution decisions</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-step">
                        <h6>3. Prioritization</h6>
                        <ul>
                            <li>MoSCoW method (Must, Should, Could, Won't)</li>
                            <li>Kano analysis</li>
                            <li>Risk-based prioritization</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-step">
                        <h6>4. Feasibility Analysis</h6>
                        <ul>
                            <li>Technical feasibility</li>
                            <li>Economic feasibility</li>
                            <li>Operational feasibility</li>
                            <li>Schedule feasibility</li>
                        </ul>
                    </div>
                </div>
                
                <h5>Requirements Quality Checklist:</h5>
                <div class="quality-checklist">
                    <h6>Completeness:</h6>
                    <ul>
                        <li>☐ All functional requirements specified</li>
                        <li>☐ All non-functional requirements specified</li>
                        <li>☐ All interfaces defined</li>
                        <li>☐ All constraints identified</li>
                    </ul>
                    
                    <h6>Consistency:</h6>
                    <ul>
                        <li>☐ No conflicting requirements</li>
                        <li>☐ Consistent terminology</li>
                        <li>☐ Consistent level of detail</li>
                    </ul>
                    
                    <h6>Clarity:</h6>
                    <ul>
                        <li>☐ Unambiguous language</li>
                        <li>☐ Measurable criteria</li>
                        <li>☐ Testable requirements</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    function generateValidationChecklist() {
        return `
            <h4>Requirements Validation Checklist</h4>
            <div class="tool-results-content">
                <h5>Validation Activities:</h5>
                <div class="validation-activities">
                    <div class="activity">
                        <h6>Requirements Review</h6>
                        <ul>
                            <li>☐ Peer review completed</li>
                            <li>☐ Stakeholder review completed</li>
                            <li>☐ Expert review completed</li>
                            <li>☐ Review comments addressed</li>
                        </ul>
                    </div>
                    
                    <div class="activity">
                        <h6>Prototyping</h6>
                        <ul>
                            <li>☐ UI prototypes developed</li>
                            <li>☐ User feedback collected</li>
                            <li>☐ Prototypes validated with users</li>
                            <li>☐ Requirements updated based on feedback</li>
                        </ul>
                    </div>
                    
                    <div class="activity">
                        <h6>Requirements Testing</h6>
                        <ul>
                            <li>☐ Acceptance criteria defined</li>
                            <li>☐ Test cases developed</li>
                            <li>☐ Requirements testable</li>
                            <li>☐ Test results documented</li>
                        </ul>
                    </div>
                </div>
                
                <h5>Validation Checklist:</h5>
                <div class="validation-checklist">
                    <h6>Content Validation:</h6>
                    <ul>
                        <li>☐ Requirements are complete</li>
                        <li>☐ Requirements are consistent</li>
                        <li>☐ Requirements are unambiguous</li>
                        <li>☐ Requirements are feasible</li>
                        <li>☐ Requirements are testable</li>
                    </ul>
                    
                    <h6>Stakeholder Validation:</h6>
                    <ul>
                        <li>☐ All stakeholders represented</li>
                        <li>☐ Stakeholder concerns addressed</li>
                        <li>☐ Requirements approved by stakeholders</li>
                        <li>☐ Sign-off obtained</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    function generateTraceabilityBuilder() {
        return `
            <h4>Requirements Traceability Builder</h4>
            <div class="tool-results-content">
                <h5>Traceability Matrix Template:</h5>
                <div class="traceability-matrix">
                    <table class="traceability-table">
                        <thead>
                            <tr>
                                <th>Requirement ID</th>
                                <th>Description</th>
                                <th>Source</th>
                                <th>Design Element</th>
                                <th>Test Case</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>REQ-001</td>
                                <td>User authentication</td>
                                <td>Stakeholder Interview</td>
                                <td>AuthController</td>
                                <td>TC-AUTH-001</td>
                                <td>Implemented</td>
                            </tr>
                            <tr>
                                <td>REQ-002</td>
                                <td>Data encryption</td>
                                <td>Security Policy</td>
                                <td>EncryptionModule</td>
                                <td>TC-SEC-001</td>
                                <td>Testing</td>
                            </tr>
                            <tr>
                                <td>REQ-003</td>
                                <td>Response time < 2s</td>
                                <td>Performance Req</td>
                                <td>PerformanceMonitor</td>
                                <td>TC-PERF-001</td>
                                <td>Pending</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <h5>Traceability Best Practices:</h5>
                <div class="traceability-practices">
                    <h6>Establish Traceability Early:</h6>
                    <ul>
                        <li>Define traceability strategy at project start</li>
                        <li>Identify traceability relationships</li>
                        <li>Set up traceability tools and processes</li>
                    </ul>
                    
                    <h6>Maintain Traceability:</h6>
                    <ul>
                        <li>Update traceability as requirements change</li>
                        <li>Review traceability regularly</li>
                        <li>Use automated tools where possible</li>
                    </ul>
                    
                    <h6>Verify Traceability:</h6>
                    <ul>
                        <li>Conduct traceability audits</li>
                        <li>Ensure all requirements are traced</li>
                        <li>Validate traceability accuracy</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    // Notification system
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
    
    // Initialize with concepts section visible
    showSection('concepts');
});
```

### Step 4: Python Requirements Analysis Tool
Create a `requirements_analyzer.py` file:

```python
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
import re

class RequirementsAnalyzer:
    def __init__(self):
        self.requirements = []
        self.stakeholders = []
        self.traceability_matrix = {}
        self.quality_metrics = {}
    
    def load_requirements(self, file_path: str):
        """Load requirements from JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.requirements = data.get('requirements', [])
            self.stakeholders = data.get('stakeholders', [])
    
    def add_requirement(self, req_id: str, description: str, req_type: str, 
                       priority: str, source: str) -> Dict[str, Any]:
        """Add a new requirement to the system"""
        requirement = {
            'id': req_id,
            'description': description,
            'type': req_type,
            'priority': priority,
            'source': source,
            'status': 'Draft',
            'created_date': datetime.now().isoformat(),
            'last_modified': datetime.now().isoformat(),
            'stakeholders': [],
            'test_cases': [],
            'design_elements': [],
            'quality_score': 0
        }
        
        self.requirements.append(requirement)
        return requirement
    
    def classify_requirements(self) -> Dict[str, List[Dict[str, Any]]]:
        """Classify requirements by type and priority"""
        classification = {
            'functional': [],
            'non_functional': [],
            'constraints': [],
            'high_priority': [],
            'medium_priority': [],
            'low_priority': []
        }
        
        for req in self.requirements:
            # Classify by type
            if req['type'].lower() in ['functional', 'function']:
                classification['functional'].append(req)
            elif req['type'].lower() in ['non-functional', 'non_functional', 'quality']:
                classification['non_functional'].append(req)
            elif req['type'].lower() in ['constraint', 'limitation']:
                classification['constraints'].append(req)
            
            # Classify by priority
            if req['priority'].lower() == 'high':
                classification['high_priority'].append(req)
            elif req['priority'].lower() == 'medium':
                classification['medium_priority'].append(req)
            elif req['priority'].lower() == 'low':
                classification['low_priority'].append(req)
        
        return classification
    
    def assess_requirement_quality(self, requirement: Dict[str, Any]) -> Dict[str, Any]:
        """Assess the quality of a requirement"""
        quality_criteria = {
            'completeness': 0,
            'consistency': 0,
            'clarity': 0,
            'correctness': 0,
            'traceability': 0
        }
        
        description = requirement['description']
        
        # Completeness check
        if len(description.split()) > 10:  # Has sufficient detail
            quality_criteria['completeness'] = 1
        
        # Clarity check
        if not self._has_ambiguous_terms(description):
            quality_criteria['clarity'] = 1
        
        # Traceability check
        if requirement.get('source') and requirement.get('stakeholders'):
            quality_criteria['traceability'] = 1
        
        # Consistency check (simplified)
        quality_criteria['consistency'] = 1  # Assume consistent for now
        
        # Correctness check (simplified)
        quality_criteria['correctness'] = 1  # Assume correct for now
        
        overall_score = sum(quality_criteria.values()) / len(quality_criteria)
        requirement['quality_score'] = overall_score
        
        return {
            'requirement_id': requirement['id'],
            'quality_score': overall_score,
            'criteria': quality_criteria,
            'recommendations': self._generate_quality_recommendations(quality_criteria)
        }
    
    def _has_ambiguous_terms(self, text: str) -> bool:
        """Check for ambiguous terms in requirement text"""
        ambiguous_terms = [
            'flexible', 'robust', 'efficient', 'user-friendly', 
            'fast', 'reliable', 'scalable', 'etc', 'and so on'
        ]
        
        text_lower = text.lower()
        for term in ambiguous_terms:
            if term in text_lower:
                return True
        return False
    
    def _generate_quality_recommendations(self, criteria: Dict[str, int]) -> List[str]:
        """Generate quality improvement recommendations"""
        recommendations = []
        
        if criteria['completeness'] == 0:
            recommendations.append("Add more detail to the requirement description")
        
        if criteria['clarity'] == 0:
            recommendations.append("Replace ambiguous terms with specific, measurable criteria")
        
        if criteria['traceability'] == 0:
            recommendations.append("Add source information and stakeholder references")
        
        return recommendations
    
    def build_traceability_matrix(self) -> Dict[str, Any]:
        """Build requirements traceability matrix"""
        matrix = {
            'requirements': [],
            'design_elements': [],
            'test_cases': [],
            'relationships': []
        }
        
        for req in self.requirements:
            matrix['requirements'].append({
                'id': req['id'],
                'description': req['description'][:50] + '...',
                'status': req['status']
            })
            
            # Add design elements
            for design_element in req.get('design_elements', []):
                if design_element not in [de['id'] for de in matrix['design_elements']]:
                    matrix['design_elements'].append({
                        'id': design_element,
                        'type': 'Design Element'
                    })
                
                matrix['relationships'].append({
                    'from': req['id'],
                    'to': design_element,
                    'type': 'implements'
                })
            
            # Add test cases
            for test_case in req.get('test_cases', []):
                if test_case not in [tc['id'] for tc in matrix['test_cases']]:
                    matrix['test_cases'].append({
                        'id': test_case,
                        'type': 'Test Case'
                    })
                
                matrix['relationships'].append({
                    'from': req['id'],
                    'to': test_case,
                    'type': 'verifies'
                })
        
        return matrix
    
    def generate_requirements_report(self) -> Dict[str, Any]:
        """Generate comprehensive requirements report"""
        classification = self.classify_requirements()
        traceability = self.build_traceability_matrix()
        
        # Quality assessment for all requirements
        quality_assessments = []
        for req in self.requirements:
            assessment = self.assess_requirement_quality(req)
            quality_assessments.append(assessment)
        
        report = {
            'summary': {
                'total_requirements': len(self.requirements),
                'functional_requirements': len(classification['functional']),
                'non_functional_requirements': len(classification['non_functional']),
                'constraints': len(classification['constraints']),
                'high_priority': len(classification['high_priority']),
                'medium_priority': len(classification['medium_priority']),
                'low_priority': len(classification['low_priority'])
            },
            'classification': classification,
            'quality_assessment': {
                'overall_average': sum([qa['quality_score'] for qa in quality_assessments]) / len(quality_assessments) if quality_assessments else 0,
                'assessments': quality_assessments
            },
            'traceability': traceability,
            'generated_at': datetime.now().isoformat()
        }
        
        return report
    
    def create_stakeholder_map(self) -> Dict[str, List[Dict[str, Any]]]:
        """Create stakeholder power-interest map"""
        stakeholder_map = {
            'high_power_high_interest': [],
            'high_power_low_interest': [],
            'low_power_high_interest': [],
            'low_power_low_interest': []
        }
        
        for stakeholder in self.stakeholders:
            power = stakeholder.get('power', 'medium')
            interest = stakeholder.get('interest', 'medium')
            
            quadrant = f"{power}_power_{interest}_interest"
            if quadrant in stakeholder_map:
                stakeholder_map[quadrant].append(stakeholder)
        
        return stakeholder_map
    
    def analyze_requirements_volatility(self) -> Dict[str, Any]:
        """Analyze requirements volatility and change patterns"""
        changes_by_month = defaultdict(int)
        changes_by_type = defaultdict(int)
        
        for req in self.requirements:
            if 'change_history' in req:
                for change in req['change_history']:
                    change_date = datetime.fromisoformat(change['date'])
                    month_key = f"{change_date.year}-{change_date.month:02d}"
                    changes_by_month[month_key] += 1
                    changes_by_type[change.get('type', 'unknown')] += 1
        
        return {
            'changes_by_month': dict(changes_by_month),
            'changes_by_type': dict(changes_by_type),
            'total_changes': sum(changes_by_month.values()),
            'volatility_index': sum(changes_by_month.values()) / len(self.requirements) if self.requirements else 0
        }
    
    def export_to_json(self, file_path: str):
        """Export requirements data to JSON file"""
        data = {
            'requirements': self.requirements,
            'stakeholders': self.stakeholders,
            'exported_at': datetime.now().isoformat()
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        print(f"Requirements exported to {file_path}")
    
    def create_visualizations(self, save_path: str = 'requirements_analysis.png'):
        """Create comprehensive requirements analysis visualizations"""
        if not self.requirements:
            print("No requirements data available for visualization")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Requirements by type
        types = ['Functional', 'Non-Functional', 'Constraints']
        counts = [
            len([r for r in self.requirements if r['type'].lower() in ['functional', 'function']]),
            len([r for r in self.requirements if r['type'].lower() in ['non-functional', 'non_functional', 'quality']]),
            len([r for r in self.requirements if r['type'].lower() in ['constraint', 'limitation']])
        ]
        
        bars1 = ax1.bar(types, counts, color=['blue', 'green', 'orange'])
        ax1.set_title('Requirements by Type', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Count', fontsize=12)
        
        # Add value labels
        for bar, count in zip(bars1, counts):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_y() + count + 0.1, 
                    str(count), ha='center', va='bottom', fontweight='bold')
        
        # Requirements by priority
        priorities = ['High', 'Medium', 'Low']
        priority_counts = [
            len([r for r in self.requirements if r['priority'].lower() == 'high']),
            len([r for r in self.requirements if r['priority'].lower() == 'medium']),
            len([r for r in self.requirements if r['priority'].lower() == 'low'])
        ]
        
        bars2 = ax2.bar(priorities, priority_counts, color=['red', 'yellow', 'green'])
        ax2.set_title('Requirements by Priority', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Count', fontsize=12)
        
        # Add value labels
        for bar, count in zip(bars2, priority_counts):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_y() + count + 0.1, 
                    str(count), ha='center', va='bottom', fontweight='bold')
        
        # Requirements status
        status_counts = defaultdict(int)
        for req in self.requirements:
            status_counts[req.get('status', 'Unknown')] += 1
        
        ax3.pie(status_counts.values(), labels=status_counts.keys(), autopct='%1.1f%%')
        ax3.set_title('Requirements Status Distribution', fontsize=14, fontweight='bold')
        
        # Quality scores
        quality_scores = [req.get('quality_score', 0) for req in self.requirements]
        ax4.hist(quality_scores, bins=10, edgecolor='black', alpha=0.7)
        ax4.set_title('Requirements Quality Distribution', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Quality Score', fontsize=12)
        ax4.set_ylabel('Frequency', fontsize=12)
        ax4.axvline(sum(quality_scores)/len(quality_scores), color='red', linestyle='--', 
                   label=f'Average: {sum(quality_scores)/len(quality_scores):.2f}')
        ax4.legend()
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Requirements analysis visualizations saved: {save_path}")

# Example usage and sample data
def create_sample_data():
    """Create sample requirements data for demonstration"""
    analyzer = RequirementsAnalyzer()
    
    # Add sample requirements
    analyzer.add_requirement('REQ-001', 
                           'The system shall allow users to authenticate using username and password',
                           'functional', 'high', 'Stakeholder Interview')
    
    analyzer.add_requirement('REQ-002', 
                           'The system shall respond to user actions within 2 seconds',
                           'non-functional', 'medium', 'Performance Requirements')
    
    analyzer.add_requirement('REQ-003', 
                           'The system shall comply with GDPR data protection regulations',
                           'constraint', 'high', 'Legal Requirements')
    
    analyzer.add_requirement('REQ-004', 
                           'The system shall be available 99.9% of the time',
                           'non-functional', 'high', 'Business Requirements')
    
    analyzer.add_requirement('REQ-005', 
                           'The system shall support at least 1000 concurrent users',
                           'non-functional', 'medium', 'Scalability Requirements')
    
    # Add sample stakeholders
    analyzer.stakeholders = [
        {'name': 'John Doe', 'role': 'Product Manager', 'power': 'high', 'interest': 'high'},
        {'name': 'Jane Smith', 'role': 'Developer', 'power': 'medium', 'interest': 'medium'},
        {'name': 'Bob Johnson', 'role': 'End User', 'power': 'low', 'interest': 'high'}
    ]
    
    return analyzer

if __name__ == "__main__":
    # Create sample data
    analyzer = create_sample_data()
    
    # Generate report
    report = analyzer.generate_requirements_report()
    
    print("Requirements Analysis Report")
    print("=" * 50)
    print(f"Total Requirements: {report['summary']['total_requirements']}")
    print(f"Functional: {report['summary']['functional_requirements']}")
    print(f"Non-Functional: {report['summary']['non_functional_requirements']}")
    print(f"Constraints: {report['summary']['constraints']}")
    print(f"Average Quality Score: {report['quality_assessment']['overall_average']:.2f}")
    
    # Export data
    analyzer.export_to_json('sample_requirements.json')
    
    # Create visualizations
    analyzer.create_visualizations()
    
    print("\nSample requirements analysis completed!")
```

### Step 5: Documentation
This comprehensive laboratory covers the fundamental concepts of Requirements Engineering according to ISO/IEC/IEEE 29148. The interactive dashboard provides hands-on experience with:

- **Core Concepts**: Requirements types, challenges, and terminology
- **Process Framework**: Complete RE process with interactive tools
- **Artifacts**: Templates for SRS, use cases, user stories, and RTM
- **Stakeholder Analysis**: Power-interest mapping and management
- **Quality Assessment**: Automated quality checking and recommendations
- **Standards Overview**: ISO/IEC/IEEE 29148 structure and benefits

The Python analysis tool provides automated requirements classification, quality assessment, traceability building, and comprehensive reporting with visualizations. This laboratory serves as the foundation for understanding requirements engineering principles and practices.
