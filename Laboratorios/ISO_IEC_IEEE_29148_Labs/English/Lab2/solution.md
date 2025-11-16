# Lab 2: Requirements Elicitation Techniques

## Solution

### Step 1: Interactive Elicitation Dashboard
Create an `elicitation_dashboard.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Requirements Elicitation Techniques Dashboard</title>
    <link rel="stylesheet" href="elicitation_styles.css">
</head>
<body>
    <header>
        <h1>Requirements Elicitation Techniques</h1>
        <nav>
            <button id="interviewsBtn">Interviews</button>
            <button id="questionnairesBtn">Questionnaires</button>
            <button id="observationBtn">Observation</button>
            <button id="documentsBtn">Document Analysis</button>
            <button id="prototypingBtn">Prototyping</button>
            <button id="integrationBtn">Technique Integration</button>
        </nav>
    </header>

    <main>
        <section class="interviews" id="interviewsSection">
            <h2>Interview Management System</h2>
            
            <div class="interview-tools">
                <h3>Interview Planning & Execution</h3>
                
                <div class="interview-setup">
                    <h4>Interview Setup</h4>
                    <form id="interviewSetupForm">
                        <div class="form-group">
                            <label for="intervieweeName">Interviewee Name:</label>
                            <input type="text" id="intervieweeName" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="intervieweeRole">Role:</label>
                            <input type="text" id="intervieweeRole" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="interviewType">Interview Type:</label>
                            <select id="interviewType">
                                <option value="structured">Structured</option>
                                <option value="semi-structured">Semi-Structured</option>
                                <option value="unstructured">Unstructured</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="interviewTopic">Primary Topic:</label>
                            <input type="text" id="interviewTopic" required>
                        </div>
                        
                        <button type="submit">Start Interview</button>
                    </form>
                </div>
                
                <div class="question-generator">
                    <h4>Question Generator</h4>
                    <div class="question-controls">
                        <select id="questionCategory">
                            <option value="functional">Functional Requirements</option>
                            <option value="non-functional">Non-Functional Requirements</option>
                            <option value="constraints">Constraints & Limitations</option>
                            <option value="stakeholder">Stakeholder Concerns</option>
                        </select>
                        <button id="generateQuestions">Generate Questions</button>
                    </div>
                    
                    <div class="questions-list" id="questionsList">
                        <p>Click "Generate Questions" to create interview questions</p>
                    </div>
                </div>
                
                <div class="response-recorder">
                    <h4>Response Recording</h4>
                    <div class="recording-controls">
                        <button id="startRecording">Start Recording</button>
                        <button id="stopRecording">Stop Recording</button>
                        <button id="saveResponse">Save Response</button>
                    </div>
                    
                    <div class="response-text">
                        <textarea id="responseText" placeholder="Record interviewee responses here..."></textarea>
                    </div>
                    
                    <div class="response-analysis">
                        <h5>Response Analysis</h5>
                        <div class="analysis-results" id="responseAnalysis">
                            <p>Analysis results will appear here</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="questionnaires" id="questionnairesSection" style="display: none;">
            <h2>Questionnaire Builder & Analysis</h2>
            
            <div class="questionnaire-tools">
                <h3>Survey Design & Distribution</h3>
                
                <div class="survey-builder">
                    <h4>Survey Builder</h4>
                    <div class="survey-form">
                        <div class="form-group">
                            <label for="surveyTitle">Survey Title:</label>
                            <input type="text" id="surveyTitle" placeholder="Enter survey title">
                        </div>
                        
                        <div class="form-group">
                            <label for="surveyDescription">Description:</label>
                            <textarea id="surveyDescription" placeholder="Describe the purpose of this survey"></textarea>
                        </div>
                        
                        <div class="question-builder">
                            <h5>Add Question</h5>
                            <select id="questionType">
                                <option value="multiple-choice">Multiple Choice</option>
                                <option value="rating">Rating Scale</option>
                                <option value="open-ended">Open-Ended</option>
                                <option value="yes-no">Yes/No</option>
                            </select>
                            <input type="text" id="questionText" placeholder="Enter question text">
                            <button id="addQuestion">Add Question</button>
                        </div>
                        
                        <div class="survey-preview" id="surveyPreview">
                            <h5>Survey Preview</h5>
                            <div id="previewContent"></div>
                        </div>
                    </div>
                </div>
                
                <div class="response-collection">
                    <h4>Response Collection</h4>
                    <div class="collection-tools">
                        <button id="generateSurveyLink">Generate Survey Link</button>
                        <button id="exportSurvey">Export Survey</button>
                        <div class="survey-link" id="surveyLink" style="display: none;">
                            <p>Survey Link: <span id="linkText"></span></p>
                            <button id="copyLink">Copy Link</button>
                        </div>
                    </div>
                </div>
                
                <div class="response-analysis">
                    <h4>Response Analysis</h4>
                    <div class="analysis-tools">
                        <button id="loadResponses">Load Sample Responses</button>
                        <button id="analyzeResponses">Analyze Responses</button>
                        <div class="analysis-results" id="surveyAnalysis">
                            <p>Analysis results will appear here</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="observation" id="observationSection" style="display: none;">
            <h2>Observation & Contextual Inquiry</h2>
            
            <div class="observation-tools">
                <h3>Activity Observation System</h3>
                
                <div class="observation-setup">
                    <h4>Observation Session Setup</h4>
                    <form id="observationSetupForm">
                        <div class="form-group">
                            <label for="observationContext">Context:</label>
                            <input type="text" id="observationContext" placeholder="e.g., Daily workflow, Customer interaction">
                        </div>
                        
                        <div class="form-group">
                            <label for="observationDuration">Duration (minutes):</label>
                            <input type="number" id="observationDuration" min="15" max="480">
                        </div>
                        
                        <div class="form-group">
                            <label for="observationType">Observation Type:</label>
                            <select id="observationType">
                                <option value="passive">Passive Observation</option>
                                <option value="active">Active Participation</option>
                                <option value="contextual">Contextual Inquiry</option>
                            </select>
                        </div>
                        
                        <button type="submit">Start Observation</button>
                    </form>
                </div>
                
                <div class="activity-logger">
                    <h4>Activity Logger</h4>
                    <div class="logging-controls">
                        <button id="startLogging">Start Logging</button>
                        <button id="pauseLogging">Pause/Resume</button>
                        <button id="stopLogging">Stop Logging</button>
                    </div>
                    
                    <div class="activity-entry">
                        <input type="text" id="activityDescription" placeholder="Describe the activity observed">
                        <select id="activityCategory">
                            <option value="task">Task Execution</option>
                            <option value="communication">Communication</option>
                            <option value="decision">Decision Making</option>
                            <option value="problem">Problem Solving</option>
                            <option value="waiting">Waiting/Idle Time</option>
                        </select>
                        <button id="logActivity">Log Activity</button>
                    </div>
                    
                    <div class="activity-timeline" id="activityTimeline">
                        <h5>Activity Timeline</h5>
                        <div id="timelineContent"></div>
                    </div>
                </div>
                
                <div class="workflow-analysis">
                    <h4>Workflow Analysis</h4>
                    <div class="analysis-tools">
                        <button id="analyzeWorkflow">Analyze Workflow</button>
                        <button id="identifyBottlenecks">Identify Bottlenecks</button>
                        <div class="workflow-results" id="workflowResults">
                            <p>Workflow analysis results will appear here</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="documents" id="documentsSection" style="display: none;">
            <h2>Document Analysis System</h2>
            
            <div class="document-tools">
                <h3>Requirements Extraction from Documents</h3>
                
                <div class="document-upload">
                    <h4>Document Upload</h4>
                    <div class="upload-area">
                        <input type="file" id="documentFile" multiple accept=".pdf,.doc,.docx,.txt">
                        <div class="upload-prompt">
                            <p>Drag and drop documents here or click to browse</p>
                            <button id="browseFiles">Browse Files</button>
                        </div>
                    </div>
                    
                    <div class="uploaded-documents" id="uploadedDocuments">
                        <h5>Uploaded Documents</h5>
                        <div id="documentList"></div>
                    </div>
                </div>
                
                <div class="requirements-extraction">
                    <h4>Requirements Extraction</h4>
                    <div class="extraction-controls">
                        <button id="extractRequirements">Extract Requirements</button>
                        <button id="analyzeGaps">Analyze Gaps</button>
                        <button id="consolidateRequirements">Consolidate Requirements</button>
                    </div>
                    
                    <div class="extraction-results" id="extractionResults">
                        <h5>Extraction Results</h5>
                        <div id="resultsContent"></div>
                    </div>
                </div>
                
                <div class="document-comparison">
                    <h4>Document Comparison</h4>
                    <div class="comparison-tools">
                        <select id="doc1Select" class="doc-selector"></select>
                        <select id="doc2Select" class="doc-selector"></select>
                        <button id="compareDocuments">Compare Documents</button>
                        
                        <div class="comparison-results" id="comparisonResults">
                            <p>Comparison results will appear here</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="prototyping" id="prototypingSection" style="display: none;">
            <h2>Prototyping for Requirements Validation</h2>
            
            <div class="prototyping-tools">
                <h3>Interactive Prototype Builder</h3>
                
                <div class="prototype-canvas">
                    <h4>Prototype Canvas</h4>
                    <div class="canvas-controls">
                        <button id="addElement">Add Element</button>
                        <button id="addScreen">Add Screen</button>
                        <button id="connectElements">Connect Elements</button>
                        <button id="clearCanvas">Clear Canvas</button>
                    </div>
                    
                    <div class="canvas-area" id="prototypeCanvas">
                        <div class="canvas-placeholder">
                            <p>Click "Add Screen" to start building your prototype</p>
                        </div>
                    </div>
                </div>
                
                <div class="element-library">
                    <h4>Element Library</h4>
                    <div class="element-types">
                        <button class="element-btn" data-type="button">Button</button>
                        <button class="element-btn" data-type="input">Text Input</button>
                        <button class="element-btn" data-type="label">Label</button>
                        <button class="element-btn" data-type="image">Image</button>
                        <button class="element-btn" data-type="list">List</button>
                    </div>
                </div>
                
                <div class="feedback-collection">
                    <h4>User Feedback Collection</h4>
                    <div class="feedback-form">
                        <div class="form-group">
                            <label for="feedbackUser">User Name:</label>
                            <input type="text" id="feedbackUser">
                        </div>
                        
                        <div class="form-group">
                            <label for="feedbackRating">Overall Rating:</label>
                            <select id="feedbackRating">
                                <option value="5">Excellent (5)</option>
                                <option value="4">Good (4)</option>
                                <option value="3">Average (3)</option>
                                <option value="2">Poor (2)</option>
                                <option value="1">Very Poor (1)</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="feedbackComments">Comments:</label>
                            <textarea id="feedbackComments" placeholder="What worked well? What needs improvement?"></textarea>
                        </div>
                        
                        <button id="submitFeedback">Submit Feedback</button>
                    </div>
                    
                    <div class="feedback-summary" id="feedbackSummary">
                        <h5>Feedback Summary</h5>
                        <div id="summaryContent"></div>
                    </div>
                </div>
            </div>
        </section>

        <section class="integration" id="integrationSection" style="display: none;">
            <h2>Technique Integration & Synthesis</h2>
            
            <div class="integration-tools">
                <h3>Multi-Technique Requirements Synthesis</h3>
                
                <div class="technique-combination">
                    <h4>Technique Combination Matrix</h4>
                    <div class="combination-matrix">
                        <table class="technique-table">
                            <thead>
                                <tr>
                                    <th>Technique</th>
                                    <th>Best For</th>
                                    <th>Strengths</th>
                                    <th>Limitations</th>
                                    <th>Combine With</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Interviews</td>
                                    <td>Detailed requirements</td>
                                    <td>Rich qualitative data</td>
                                    <td>Time-consuming</td>
                                    <td>Questionnaires</td>
                                </tr>
                                <tr>
                                    <td>Questionnaires</td>
                                    <td>Large groups</td>
                                    <td>Quantitative data</td>
                                    <td>Limited depth</td>
                                    <td>Interviews</td>
                                </tr>
                                <tr>
                                    <td>Observation</td>
                                    <td>Actual workflows</td>
                                    <td>Real behavior</td>
                                    <td>Observer effect</td>
                                    <td>Document analysis</td>
                                </tr>
                                <tr>
                                    <td>Document Analysis</td>
                                    <td>Existing systems</td>
                                    <td>Historical data</td>
                                    <td>Outdated info</td>
                                    <td>Prototyping</td>
                                </tr>
                                <tr>
                                    <td>Prototyping</td>
                                    <td>UI requirements</td>
                                    <td>Visual validation</td>
                                    <td>Time intensive</td>
                                    <td>All techniques</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <div class="requirements-synthesis">
                    <h4>Requirements Synthesis</h4>
                    <div class="synthesis-tools">
                        <button id="loadTechniqueData">Load Technique Data</button>
                        <button id="synthesizeRequirements">Synthesize Requirements</button>
                        <button id="resolveConflicts">Resolve Conflicts</button>
                        <button id="prioritizeRequirements">Prioritize Requirements</button>
                    </div>
                    
                    <div class="synthesis-results" id="synthesisResults">
                        <h5>Synthesis Results</h5>
                        <div id="synthesisContent"></div>
                    </div>
                </div>
                
                <div class="validation-dashboard">
                    <h4>Validation Dashboard</h4>
                    <div class="validation-metrics">
                        <div class="metric">
                            <h5>Requirements Coverage</h5>
                            <div class="progress-bar">
                                <div class="progress-fill" id="coverageProgress" style="width: 0%"></div>
                            </div>
                            <span id="coverageText">0%</span>
                        </div>
                        
                        <div class="metric">
                            <h5>Stakeholder Agreement</h5>
                            <div class="progress-bar">
                                <div class="progress-fill" id="agreementProgress" style="width: 0%"></div>
                            </div>
                            <span id="agreementText">0%</span>
                        </div>
                        
                        <div class="metric">
                            <h5>Requirements Quality</h5>
                            <div class="progress-bar">
                                <div class="progress-fill" id="qualityProgress" style="width: 0%"></div>
                            </div>
                            <span id="qualityText">0%</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="elicitation_scripts.js"></script>
</body>
</html>
```

### Step 2: CSS for Elicitation Dashboard
Create an `elicitation_styles.css` file:

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

.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.form-group input, .form-group select, .form-group textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
}

.form-group textarea {
    min-height: 100px;
    resize: vertical;
}

button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #2980b9;
}

button:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
}

/* Interview Section */
.interview-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.question-generator, .response-recorder {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.questions-list {
    margin-top: 1rem;
    max-height: 300px;
    overflow-y: auto;
}

.question-item {
    background-color: white;
    padding: 1rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

.recording-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
}

/* Questionnaire Section */
.questionnaire-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.survey-builder, .response-collection, .response-analysis {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.question-builder {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin: 1rem 0;
}

.question-builder select, .question-builder input {
    flex: 1;
}

.survey-link {
    margin-top: 1rem;
    padding: 1rem;
    background-color: white;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

/* Observation Section */
.observation-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.observation-setup, .activity-logger, .workflow-analysis {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.logging-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
}

.activity-entry {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin: 1rem 0;
}

.activity-entry input, .activity-entry select {
    flex: 1;
}

.activity-timeline {
    margin-top: 1rem;
    max-height: 300px;
    overflow-y: auto;
}

.timeline-item {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    font-size: 0.9rem;
}

/* Document Analysis Section */
.document-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.document-upload, .requirements-extraction, .document-comparison {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.upload-area {
    border: 2px dashed #dee2e6;
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
    margin: 1rem 0;
}

.upload-prompt p {
    margin-bottom: 1rem;
    color: #6c757d;
}

.document-item {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.doc-selector {
    margin: 0 1rem;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
}

/* Prototyping Section */
.prototyping-tools {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 2rem;
}

.prototype-canvas {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.canvas-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}

.canvas-area {
    border: 1px solid #dee2e6;
    border-radius: 4px;
    min-height: 400px;
    background-color: white;
    position: relative;
    overflow: hidden;
}

.canvas-placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #6c757d;
}

.element-library {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.element-types {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.element-btn {
    text-align: left;
    padding: 0.5rem;
    background-color: white;
    border: 1px solid #dee2e6;
}

.element-btn:hover {
    background-color: #e9ecef;
}

.feedback-collection {
    grid-column: 1 / -1;
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    margin-top: 2rem;
}

.feedback-summary {
    margin-top: 2rem;
}

/* Integration Section */
.integration-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.technique-combination, .requirements-synthesis, .validation-dashboard {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.technique-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}

.technique-table th, .technique-table td {
    padding: 0.5rem;
    text-align: left;
    border: 1px solid #dee2e6;
}

.technique-table th {
    background-color: #e9ecef;
    font-weight: bold;
}

.synthesis-tools {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
    flex-wrap: wrap;
}

.validation-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.metric {
    background-color: white;
    padding: 1rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    text-align: center;
}

.progress-bar {
    background-color: #e9ecef;
    height: 20px;
    border-radius: 10px;
    margin: 0.5rem 0;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background-color: #28a745;
    transition: width 0.3s ease;
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
    
    .interview-tools, .questionnaire-tools, .observation-tools, 
    .document-tools, .prototyping-tools, .integration-tools {
        grid-template-columns: 1fr;
    }
    
    .activity-entry, .question-builder {
        flex-direction: column;
        align-items: stretch;
    }
    
    .logging-controls, .canvas-controls, .synthesis-tools {
        justify-content: center;
    }
}
```

### Step 3: JavaScript for Elicitation Dashboard
Create an `elicitation_scripts.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Navigation system
    const sections = {
        interviews: document.getElementById('interviewsSection'),
        questionnaires: document.getElementById('questionnairesSection'),
        observation: document.getElementById('observationSection'),
        documents: document.getElementById('documentsSection'),
        prototyping: document.getElementById('prototypingSection'),
        integration: document.getElementById('integrationSection')
    };
    
    // Navigation buttons
    document.getElementById('interviewsBtn').addEventListener('click', () => showSection('interviews'));
    document.getElementById('questionnairesBtn').addEventListener('click', () => showSection('questionnaires'));
    document.getElementById('observationBtn').addEventListener('click', () => showSection('observation'));
    document.getElementById('documentsBtn').addEventListener('click', () => showSection('documents'));
    document.getElementById('prototypingBtn').addEventListener('click', () => showSection('prototyping'));
    document.getElementById('integrationBtn').addEventListener('click', () => showSection('integration'));
    
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
    
    // Interview Management
    let currentInterview = null;
    let isRecording = false;
    
    document.getElementById('interviewSetupForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const interviewee = document.getElementById('intervieweeName').value;
        const role = document.getElementById('intervieweeRole').value;
        const type = document.getElementById('interviewType').value;
        const topic = document.getElementById('interviewTopic').value;
        
        currentInterview = {
            interviewee: interviewee,
            role: role,
            type: type,
            topic: topic,
            startTime: new Date(),
            questions: [],
            responses: []
        };
        
        showNotification(`Interview started with ${interviewee}`);
        this.reset();
    });
    
    document.getElementById('generateQuestions').addEventListener('click', function() {
        const category = document.getElementById('questionCategory').value;
        const questions = generateQuestions(category);
        
        const questionsList = document.getElementById('questionsList');
        questionsList.innerHTML = '';
        
        questions.forEach((question, index) => {
            const questionItem = document.createElement('div');
            questionItem.className = 'question-item';
            questionItem.innerHTML = `
                <strong>Q${index + 1}:</strong> ${question}
                <button class="ask-question" data-question="${question}">Ask</button>
            `;
            questionsList.appendChild(questionItem);
            
            if (currentInterview) {
                currentInterview.questions.push(question);
            }
        });
        
        showNotification(`Generated ${questions.length} questions`);
    });
    
    function generateQuestions(category) {
        const questionTemplates = {
            functional: [
                "What are the main tasks you perform in your role?",
                "What information do you need to complete your work?",
                "What are the most important outcomes you need to achieve?",
                "What are the biggest challenges you face in your work?",
                "How do you currently handle [specific process]?"
            ],
            non_functional: [
                "How quickly do you need responses to your requests?",
                "What are your availability requirements?",
                "How many users need to access the system simultaneously?",
                "What are your security and privacy requirements?",
                "What level of reliability do you need?"
            ],
            constraints: [
                "What limitations or restrictions do you work with?",
                "What regulatory requirements must be met?",
                "What budget constraints affect your work?",
                "What technology constraints exist?",
                "What organizational policies impact your requirements?"
            ],
            stakeholder: [
                "What are your main concerns about this project?",
                "How will this system affect your daily work?",
                "What are your success criteria for this project?",
                "Who else will be affected by this system?",
                "What training or support will you need?"
            ]
        };
        
        return questionTemplates[category] || [];
    }
    
    // Recording controls
    document.getElementById('startRecording').addEventListener('click', function() {
        isRecording = true;
        this.disabled = true;
        document.getElementById('stopRecording').disabled = false;
        showNotification('Recording started');
    });
    
    document.getElementById('stopRecording').addEventListener('click', function() {
        isRecording = false;
        this.disabled = true;
        document.getElementById('startRecording').disabled = false;
        showNotification('Recording stopped');
    });
    
    document.getElementById('saveResponse').addEventListener('click', function() {
        const responseText = document.getElementById('responseText').value;
        if (responseText && currentInterview) {
            currentInterview.responses.push({
                timestamp: new Date(),
                text: responseText
            });
            
            // Analyze response
            analyzeResponse(responseText);
            
            document.getElementById('responseText').value = '';
            showNotification('Response saved');
        }
    });
    
    function analyzeResponse(text) {
        const analysis = document.getElementById('responseAnalysis');
        
        // Simple keyword analysis
        const keywords = {
            requirements: ['need', 'require', 'must', 'should', 'want'],
            problems: ['problem', 'issue', 'challenge', 'difficulty', 'trouble'],
            processes: ['process', 'workflow', 'procedure', 'step', 'task'],
            stakeholders: ['user', 'customer', 'manager', 'team', 'department']
        };
        
        let findings = [];
        
        Object.keys(keywords).forEach(category => {
            const found = keywords[category].some(keyword => 
                text.toLowerCase().includes(keyword)
            );
            if (found) {
                findings.push(category);
            }
        });
        
        analysis.innerHTML = `
            <h6>Analysis Results:</h6>
            <p><strong>Categories identified:</strong> ${findings.join(', ') || 'None'}</p>
            <p><strong>Word count:</strong> ${text.split(' ').length}</p>
            <p><strong>Potential requirements:</strong> ${findings.includes('requirements') ? 'Yes' : 'Review needed'}</p>
        `;
    }
    
    // Questionnaire Builder
    let currentSurvey = { title: '', description: '', questions: [] };
    
    document.getElementById('addQuestion').addEventListener('click', function() {
        const type = document.getElementById('questionType').value;
        const text = document.getElementById('questionText').value;
        
        if (text) {
            const question = {
                id: Date.now(),
                type: type,
                text: text,
                options: []
            };
            
            currentSurvey.questions.push(question);
            updateSurveyPreview();
            
            document.getElementById('questionText').value = '';
            showNotification('Question added to survey');
        }
    });
    
    function updateSurveyPreview() {
        const preview = document.getElementById('previewContent');
        const title = document.getElementById('surveyTitle').value;
        const description = document.getElementById('surveyDescription').value;
        
        currentSurvey.title = title;
        currentSurvey.description = description;
        
        let html = `<h4>${title || 'Untitled Survey'}</h4>`;
        if (description) {
            html += `<p>${description}</p>`;
        }
        
        currentSurvey.questions.forEach((q, index) => {
            html += `<div class="preview-question">
                <p><strong>Q${index + 1}:</strong> ${q.text}</p>
                <div class="question-response">
                    ${generateQuestionResponse(q)}
                </div>
            </div>`;
        });
        
        preview.innerHTML = html;
    }
    
    function generateQuestionResponse(question) {
        switch(question.type) {
            case 'multiple-choice':
                return `
                    <div class="options">
                        <label><input type="radio" name="q${question.id}"> Option 1</label><br>
                        <label><input type="radio" name="q${question.id}"> Option 2</label><br>
                        <label><input type="radio" name="q${question.id}"> Option 3</label><br>
                        <label><input type="radio" name="q${question.id}"> Other</label>
                    </div>
                `;
            case 'rating':
                return `
                    <div class="rating">
                        <span>1</span> <input type="range" min="1" max="5"> <span>5</span>
                    </div>
                `;
            case 'open-ended':
                return `<textarea placeholder="Your answer here..."></textarea>`;
            case 'yes-no':
                return `
                    <label><input type="radio" name="q${question.id}"> Yes</label>
                    <label><input type="radio" name="q${question.id}"> No</label>
                `;
            default:
                return '';
        }
    }
    
    document.getElementById('generateSurveyLink').addEventListener('click', function() {
        const linkText = document.getElementById('linkText');
        const surveyLink = document.getElementById('surveyLink');
        
        // Generate a mock survey link
        const surveyId = Date.now();
        linkText.textContent = `https://elicitation.example.com/survey/${surveyId}`;
        surveyLink.style.display = 'block';
        
        showNotification('Survey link generated');
    });
    
    document.getElementById('copyLink').addEventListener('click', function() {
        const linkText = document.getElementById('linkText').textContent;
        navigator.clipboard.writeText(linkText);
        showNotification('Link copied to clipboard');
    });
    
    document.getElementById('loadResponses').addEventListener('click', function() {
        // Load sample responses
        const sampleResponses = generateSampleResponses();
        showNotification(`Loaded ${sampleResponses.length} sample responses`);
    });
    
    function generateSampleResponses() {
        return [
            { questionId: 1, response: 'Yes', respondent: 'User1' },
            { questionId: 1, response: 'No', respondent: 'User2' },
            { questionId: 2, response: '4', respondent: 'User1' },
            { questionId: 2, response: '5', respondent: 'User2' }
        ];
    }
    
    // Observation Tools
    let observationSession = null;
    let isLogging = false;
    let activityLog = [];
    
    document.getElementById('observationSetupForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const context = document.getElementById('observationContext').value;
        const duration = document.getElementById('observationDuration').value;
        const type = document.getElementById('observationType').value;
        
        observationSession = {
            context: context,
            duration: duration,
            type: type,
            startTime: new Date(),
            activities: []
        };
        
        showNotification(`Observation session started: ${context}`);
        this.reset();
    });
    
    document.getElementById('startLogging').addEventListener('click', function() {
        isLogging = true;
        this.disabled = true;
        document.getElementById('pauseLogging').disabled = false;
        document.getElementById('stopLogging').disabled = false;
        showNotification('Activity logging started');
    });
    
    document.getElementById('stopLogging').addEventListener('click', function() {
        isLogging = false;
        this.disabled = true;
        document.getElementById('startLogging').disabled = false;
        document.getElementById('pauseLogging').disabled = true;
        showNotification('Activity logging stopped');
    });
    
    document.getElementById('logActivity').addEventListener('click', function() {
        const description = document.getElementById('activityDescription').value;
        const category = document.getElementById('activityCategory').value;
        
        if (description && isLogging) {
            const activity = {
                timestamp: new Date(),
                description: description,
                category: category
            };
            
            activityLog.push(activity);
            updateActivityTimeline();
            
            document.getElementById('activityDescription').value = '';
            showNotification('Activity logged');
        }
    });
    
    function updateActivityTimeline() {
        const timeline = document.getElementById('timelineContent');
        timeline.innerHTML = '';
        
        activityLog.forEach(activity => {
            const item = document.createElement('div');
            item.className = 'timeline-item';
            item.innerHTML = `
                <strong>${activity.timestamp.toLocaleTimeString()}</strong> - 
                <span class="category">${activity.category}</span>: 
                ${activity.description}
            `;
            timeline.appendChild(item);
        });
    }
    
    // Document Analysis
    let uploadedDocuments = [];
    
    document.getElementById('documentFile').addEventListener('change', function(e) {
        const files = e.target.files;
        
        for (let file of files) {
            const document = {
                id: Date.now(),
                name: file.name,
                type: file.type,
                size: file.size,
                uploadTime: new Date()
            };
            
            uploadedDocuments.push(document);
        }
        
        updateDocumentList();
        showNotification(`Uploaded ${files.length} document(s)`);
    });
    
    function updateDocumentList() {
        const documentList = document.getElementById('documentList');
        documentList.innerHTML = '';
        
        uploadedDocuments.forEach(doc => {
            const item = document.createElement('div');
            item.className = 'document-item';
            item.innerHTML = `
                <div>
                    <strong>${doc.name}</strong>
                    <small>${(doc.size / 1024).toFixed(1)} KB</small>
                </div>
                <button class="remove-doc" data-id="${doc.id}">Remove</button>
            `;
            documentList.appendChild(item);
        });
        
        // Update comparison selectors
        updateDocumentSelectors();
    }
    
    function updateDocumentSelectors() {
        const selectors = document.querySelectorAll('.doc-selector');
        selectors.forEach(selector => {
            selector.innerHTML = '<option value="">Select document</option>';
            uploadedDocuments.forEach(doc => {
                const option = document.createElement('option');
                option.value = doc.id;
                option.textContent = doc.name;
                selector.appendChild(option);
            });
        });
    }
    
    document.getElementById('extractRequirements').addEventListener('click', function() {
        if (uploadedDocuments.length === 0) {
            showNotification('No documents uploaded');
            return;
        }
        
        // Simulate requirements extraction
        const extractedReqs = [
            "System shall allow user authentication",
            "System shall provide data validation",
            "System shall generate reports",
            "System shall support multiple user roles"
        ];
        
        const results = document.getElementById('resultsContent');
        results.innerHTML = `
            <h6>Extracted Requirements:</h6>
            <ul>
                ${extractedReqs.map(req => `<li>${req}</li>`).join('')}
            </ul>
        `;
        
        showNotification('Requirements extracted from documents');
    });
    
    // Prototyping Tools
    let prototypeElements = [];
    let currentScreen = null;
    
    document.getElementById('addScreen').addEventListener('click', function() {
        const canvas = document.getElementById('prototypeCanvas');
        const placeholder = canvas.querySelector('.canvas-placeholder');
        
        if (placeholder) {
            placeholder.remove();
        }
        
        const screen = document.createElement('div');
        screen.className = 'prototype-screen';
        screen.style.cssText = `
            position: absolute;
            width: 300px;
            height: 400px;
            background-color: white;
            border: 2px solid #3498db;
            border-radius: 8px;
            top: 50px;
            left: 50px;
        `;
        
        screen.innerHTML = '<div class="screen-header">Screen 1</div>';
        canvas.appendChild(screen);
        
        currentScreen = screen;
        showNotification('New screen added to prototype');
    });
    
    document.getElementById('addElement').addEventListener('click', function() {
        if (!currentScreen) {
            showNotification('Please add a screen first');
            return;
        }
        
        const element = document.createElement('div');
        element.className = 'prototype-element';
        element.style.cssText = `
            position: absolute;
            width: 100px;
            height: 30px;
            background-color: #e9ecef;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            top: 60px;
            left: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        `;
        element.textContent = 'Button';
        
        currentScreen.appendChild(element);
        showNotification('Element added to screen');
    });
    
    // Feedback Collection
    let feedbackData = [];
    
    document.getElementById('submitFeedback').addEventListener('click', function() {
        const user = document.getElementById('feedbackUser').value;
        const rating = document.getElementById('feedbackRating').value;
        const comments = document.getElementById('feedbackComments').value;
        
        if (user && rating) {
            const feedback = {
                user: user,
                rating: parseInt(rating),
                comments: comments,
                timestamp: new Date()
            };
            
            feedbackData.push(feedback);
            updateFeedbackSummary();
            
            // Reset form
            document.getElementById('feedbackUser').value = '';
            document.getElementById('feedbackComments').value = '';
            
            showNotification('Feedback submitted');
        }
    });
    
    function updateFeedbackSummary() {
        const summary = document.getElementById('summaryContent');
        
        if (feedbackData.length === 0) {
            summary.innerHTML = '<p>No feedback submitted yet</p>';
            return;
        }
        
        const avgRating = feedbackData.reduce((sum, f) => sum + f.rating, 0) / feedbackData.length;
        
        summary.innerHTML = `
            <p><strong>Total Feedback:</strong> ${feedbackData.length}</p>
            <p><strong>Average Rating:</strong> ${avgRating.toFixed(1)}/5</p>
            <div class="recent-comments">
                <h6>Recent Comments:</h6>
                <ul>
                    ${feedbackData.slice(-3).map(f => `<li>${f.comments || 'No comments'}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    // Integration Tools
    document.getElementById('synthesizeRequirements').addEventListener('click', function() {
        const synthesis = document.getElementById('synthesisContent');
        
        // Simulate requirements synthesis
        const synthesizedReqs = [
            "REQ-001: User authentication system (from interviews & questionnaires)",
            "REQ-002: Real-time data processing (from observation & prototyping)",
            "REQ-003: Multi-user support (from document analysis)",
            "REQ-004: Automated reporting (from stakeholder feedback)"
        ];
        
        synthesis.innerHTML = `
            <h6>Synthesized Requirements:</h6>
            <ul>
                ${synthesizedReqs.map(req => `<li>${req}</li>`).join('')}
            </ul>
            <p><strong>Conflicts resolved:</strong> 2 (merged similar requirements)</p>
            <p><strong>New requirements identified:</strong> 1</p>
        `;
        
        // Update validation metrics
        updateValidationMetrics(75, 80, 70);
        showNotification('Requirements synthesized');
    });
    
    function updateValidationMetrics(coverage, agreement, quality) {
        document.getElementById('coverageProgress').style.width = coverage + '%';
        document.getElementById('coverageText').textContent = coverage + '%';
        
        document.getElementById('agreementProgress').style.width = agreement + '%';
        document.getElementById('agreementText').textContent = agreement + '%';
        
        document.getElementById('qualityProgress').style.width = quality + '%';
        document.getElementById('qualityText').textContent = quality + '%';
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
    
    // Initialize with interviews section visible
    showSection('interviews');
    
    // Update survey preview on input changes
    document.getElementById('surveyTitle').addEventListener('input', updateSurveyPreview);
    document.getElementById('surveyDescription').addEventListener('input', updateSurveyPreview);
});
```

### Step 4: Python Elicitation Analysis Tool
Create an `elicitation_analyzer.py` file:

```python
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
import re
from textblob import TextBlob
import numpy as np

class ElicitationAnalyzer:
    def __init__(self):
        self.interview_data = []
        self.questionnaire_data = []
        self.observation_data = []
        self.document_data = []
        self.feedback_data = []
        
        # Initialize NLTK resources
        try:
            nltk.data.find('vader_lexicon')
        except LookupError:
            nltk.download('vader_lexicon')
        
        try:
            nltk.data.find('punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('stopwords')
        except LookupError:
            nltk.download('stopwords')
        
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))
    
    def load_interview_data(self, file_path: str):
        """Load interview transcripts from JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.interview_data = data.get('interviews', [])
    
    def load_questionnaire_data(self, file_path: str):
        """Load questionnaire responses from JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.questionnaire_data = data.get('responses', [])
    
    def load_observation_data(self, file_path: str):
        """Load observation logs from JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.observation_data = data.get('observations', [])
    
    def analyze_interview_transcript(self, transcript: str) -> Dict[str, Any]:
        """Analyze a single interview transcript"""
        # Sentiment analysis
        sentiment = self.sia.polarity_scores(transcript)
        
        # Keyword extraction
        words = word_tokenize(transcript.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in self.stop_words]
        word_freq = Counter(filtered_words)
        
        # Requirements identification
        requirements_keywords = [
            'need', 'require', 'must', 'should', 'want', 'have to',
            'necessary', 'important', 'critical', 'essential'
        ]
        
        potential_requirements = []
        sentences = nltk.sent_tokenize(transcript)
        
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in requirements_keywords):
                potential_requirements.append(sentence.strip())
        
        # Theme analysis
        themes = self._extract_themes(transcript)
        
        return {
            'sentiment': sentiment,
            'word_frequency': dict(word_freq.most_common(20)),
            'potential_requirements': potential_requirements,
            'themes': themes,
            'word_count': len(words),
            'sentence_count': len(sentences)
        }
    
    def _extract_themes(self, text: str) -> List[str]:
        """Extract main themes from text"""
        theme_keywords = {
            'functionality': ['function', 'feature', 'capability', 'work', 'do'],
            'usability': ['easy', 'simple', 'user-friendly', 'intuitive', 'interface'],
            'performance': ['fast', 'quick', 'performance', 'speed', 'efficient'],
            'security': ['secure', 'security', 'protect', 'privacy', 'safe'],
            'reliability': ['reliable', 'dependable', 'stable', 'consistent']
        }
        
        text_lower = text.lower()
        themes = []
        
        for theme, keywords in theme_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                themes.append(theme)
        
        return themes
    
    def analyze_questionnaire_responses(self, responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze questionnaire responses"""
        df = pd.DataFrame(responses)
        
        analysis = {
            'total_responses': len(responses),
            'completion_rate': len(df.dropna()) / len(df) if len(df) > 0 else 0,
            'question_analysis': {}
        }
        
        # Analyze each question
        for column in df.columns:
            if column != 'respondent_id':
                question_data = df[column].dropna()
                
                if question_data.dtype == 'object':
                    # Text analysis
                    analysis['question_analysis'][column] = self._analyze_text_responses(question_data.tolist())
                else:
                    # Numeric analysis
                    analysis['question_analysis'][column] = {
                        'mean': question_data.mean(),
                        'median': question_data.median(),
                        'std': question_data.std(),
                        'min': question_data.min(),
                        'max': question_data.max()
                    }
        
        return analysis
    
    def _analyze_text_responses(self, responses: List[str]) -> Dict[str, Any]:
        """Analyze open-ended text responses"""
        if not responses:
            return {}
        
        # Combine all responses
        combined_text = ' '.join(responses)
        
        # Sentiment analysis
        sentiments = [self.sia.polarity_scores(response) for response in responses]
        avg_sentiment = {
            'compound': np.mean([s['compound'] for s in sentiments]),
            'positive': np.mean([s['pos'] for s in sentiments]),
            'negative': np.mean([s['neg'] for s in sentiments]),
            'neutral': np.mean([s['neu'] for s in sentiments])
        }
        
        # Common themes
        all_words = []
        for response in responses:
            words = word_tokenize(response.lower())
            filtered_words = [word for word in words if word.isalnum() and word not in self.stop_words]
            all_words.extend(filtered_words)
        
        word_freq = Counter(all_words)
        
        return {
            'response_count': len(responses),
            'average_sentiment': avg_sentiment,
            'common_words': dict(word_freq.most_common(10)),
            'themes': self._extract_themes(combined_text)
        }
    
    def analyze_observation_data(self, observations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze observation logs"""
        df = pd.DataFrame(observations)
        
        analysis = {
            'total_observations': len(observations),
            'observation_period': self._calculate_observation_period(observations),
            'activity_breakdown': {},
            'process_flow': [],
            'bottlenecks': []
        }
        
        if 'category' in df.columns:
            analysis['activity_breakdown'] = df['category'].value_counts().to_dict()
        
        # Identify process flow
        if 'timestamp' in df.columns and 'description' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.sort_values('timestamp')
            
            analysis['process_flow'] = df[['timestamp', 'description', 'category']].to_dict('records')
        
        # Identify bottlenecks (activities taking long time)
        if 'duration' in df.columns:
            long_activities = df[df['duration'] > df['duration'].quantile(0.75)]
            analysis['bottlenecks'] = long_activities['description'].tolist()
        
        return analysis
    
    def _calculate_observation_period(self, observations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate the observation period"""
        if not observations or 'timestamp' not in observations[0]:
            return {}
        
        timestamps = [obs['timestamp'] for obs in observations if 'timestamp' in obs]
        
        if timestamps:
            timestamps.sort()
            return {
                'start': timestamps[0],
                'end': timestamps[-1],
                'duration_hours': (datetime.fromisoformat(timestamps[-1]) - datetime.fromisoformat(timestamps[0])).total_seconds() / 3600
            }
        
        return {}
    
    def extract_requirements_from_documents(self, documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract requirements from document text"""
        all_requirements = []
        document_analysis = {}
        
        for doc in documents:
            if 'content' in doc:
                content = doc['content']
                
                # Find requirement patterns
                requirement_patterns = [
                    r'(?:shall|must|should|will|may|can|cannot)\s+[^.]*',
                    r'(?:system|user|application)\s+(?:shall|must|should|will)\s+[^.]*',
                    r'(?:the\s+system|the\s+user)\s+(?:needs|requires|wants)\s+[^.]*'
                ]
                
                doc_requirements = []
                for pattern in requirement_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    doc_requirements.extend(matches)
                
                document_analysis[doc['name']] = {
                    'requirements_found': len(doc_requirements),
                    'requirements': doc_requirements
                }
                
                all_requirements.extend(doc_requirements)
        
        return {
            'total_requirements': len(all_requirements),
            'unique_requirements': len(set(all_requirements)),
            'document_analysis': document_analysis,
            'consolidated_requirements': list(set(all_requirements))
        }
    
    def synthesize_techniques(self, technique_data: Dict[str, List]) -> Dict[str, Any]:
        """Synthesize data from multiple elicitation techniques"""
        synthesis = {
            'consolidated_requirements': [],
            'conflicts': [],
            'gaps': [],
            'prioritized_requirements': [],
            'stakeholder_consensus': {}
        }
        
        # Combine requirements from all techniques
        all_requirements = []
        
        if 'interview_requirements' in technique_data:
            all_requirements.extend(technique_data['interview_requirements'])
        
        if 'questionnaire_requirements' in technique_data:
            all_requirements.extend(technique_data['questionnaire_requirements'])
        
        if 'observation_requirements' in technique_data:
            all_requirements.extend(technique_data['observation_requirements'])
        
        if 'document_requirements' in technique_data:
            all_requirements.extend(technique_data['document_requirements'])
        
        # Remove duplicates and similar requirements
        synthesis['consolidated_requirements'] = self._consolidate_requirements(all_requirements)
        
        # Identify conflicts
        synthesis['conflicts'] = self._identify_conflicts(all_requirements)
        
        # Identify gaps
        synthesis['gaps'] = self._identify_gaps(technique_data)
        
        # Prioritize requirements
        synthesis['prioritized_requirements'] = self._prioritize_requirements(synthesis['consolidated_requirements'])
        
        return synthesis
    
    def _consolidate_requirements(self, requirements: List[str]) -> List[str]:
        """Consolidate similar requirements"""
        # Simple consolidation - remove exact duplicates
        return list(set(requirements))
    
    def _identify_conflicts(self, requirements: List[str]) -> List[Dict[str, Any]]:
        """Identify conflicting requirements"""
        conflicts = []
        
        # Simple conflict detection - look for contradictory terms
        contradictory_pairs = [
            ('must', 'cannot'),
            ('shall', 'shall not'),
            ('required', 'optional'),
            ('always', 'never')
        ]
        
        for i, req1 in enumerate(requirements):
            for j, req2 in enumerate(requirements[i+1:], i+1):
                for pos, neg in contradictory_pairs:
                    if (pos in req1.lower() and neg in req2.lower()) or \
                       (pos in req2.lower() and neg in req1.lower()):
                        conflicts.append({
                            'requirement1': req1,
                            'requirement2': req2,
                            'conflict_type': f'{pos} vs {neg}'
                        })
        
        return conflicts
    
    def _identify_gaps(self, technique_data: Dict[str, List]) -> List[str]:
        """Identify gaps in requirements coverage"""
        gaps = []
        
        # Check for missing requirement types
        required_types = ['functional', 'non-functional', 'constraints', 'interface']
        
        for req_type in required_types:
            found = False
            for technique, data in technique_data.items():
                if any(req_type in str(req).lower() for req in data):
                    found = True
                    break
            
            if not found:
                gaps.append(f'Missing {req_type} requirements')
        
        return gaps
    
    def _prioritize_requirements(self, requirements: List[str]) -> List[Tuple[str, int]]:
        """Prioritize requirements based on keywords"""
        priority_keywords = {
            'high': ['critical', 'essential', 'must', 'required', 'important'],
            'medium': ['should', 'preferable', 'nice to have'],
            'low': ['may', 'optional', 'could']
        }
        
        prioritized = []
        
        for req in requirements:
            priority_score = 1  # Default low priority
            
            req_lower = req.lower()
            for level, keywords in priority_keywords.items():
                if any(keyword in req_lower for keyword in keywords):
                    if level == 'high':
                        priority_score = 3
                    elif level == 'medium':
                        priority_score = 2
                    break
            
            prioritized.append((req, priority_score))
        
        # Sort by priority (high to low)
        prioritized.sort(key=lambda x: x[1], reverse=True)
        return prioritized
    
    def generate_elicitation_report(self) -> Dict[str, Any]:
        """Generate comprehensive elicitation analysis report"""
        report = {
            'summary': {
                'interviews_analyzed': len(self.interview_data),
                'questionnaire_responses': len(self.questionnaire_data),
                'observation_sessions': len(self.observation_data),
                'documents_processed': len(self.document_data)
            },
            'interview_analysis': [],
            'questionnaire_analysis': {},
            'observation_analysis': {},
            'document_analysis': {},
            'synthesis': {}
        }
        
        # Analyze interviews
        for interview in self.interview_data:
            if 'transcript' in interview:
                analysis = self.analyze_interview_transcript(interview['transcript'])
                analysis['interview_id'] = interview.get('id', 'Unknown')
                report['interview_analysis'].append(analysis)
        
        # Analyze questionnaires
        if self.questionnaire_data:
            report['questionnaire_analysis'] = self.analyze_questionnaire_responses(self.questionnaire_data)
        
        # Analyze observations
        if self.observation_data:
            report['observation_analysis'] = self.analyze_observation_data(self.observation_data)
        
        # Analyze documents
        if self.document_data:
            report['document_analysis'] = self.extract_requirements_from_documents(self.document_data)
        
        # Synthesize all techniques
        technique_data = {
            'interview_requirements': [req for analysis in report['interview_analysis'] 
                                    for req in analysis.get('potential_requirements', [])],
            'questionnaire_requirements': self.questionnaire_data,
            'observation_requirements': self.observation_data,
            'document_requirements': report['document_analysis'].get('consolidated_requirements', [])
        }
        
        report['synthesis'] = self.synthesize_techniques(technique_data)
        
        return report
    
    def create_elicitation_visualizations(self, save_path: str = 'elicitation_analysis.png'):
        """Create comprehensive elicitation analysis visualizations"""
        if not any([self.interview_data, self.questionnaire_data, self.observation_data]):
            print("No elicitation data available for visualization")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Technique usage
        techniques = ['Interviews', 'Questionnaires', 'Observations', 'Documents']
        counts = [
            len(self.interview_data),
            len(self.questionnaire_data),
            len(self.observation_data),
            len(self.document_data)
        ]
        
        bars1 = ax1.bar(techniques, counts, color=['blue', 'green', 'orange', 'red'])
        ax1.set_title('Elicitation Techniques Used', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Count', fontsize=12)
        
        for bar, count in zip(bars1, counts):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_y() + count + 0.1, 
                    str(count), ha='center', va='bottom', fontweight='bold')
        
        # Interview sentiment analysis
        if self.interview_data:
            sentiments = []
            for interview in self.interview_data:
                if 'transcript' in interview:
                    sentiment = self.sia.polarity_scores(interview['transcript'])
                    sentiments.append(sentiment['compound'])
            
            if sentiments:
                ax2.hist(sentiments, bins=10, edgecolor='black', alpha=0.7)
                ax2.set_title('Interview Sentiment Distribution', fontsize=14, fontweight='bold')
                ax2.set_xlabel('Sentiment Score', fontsize=12)
                ax2.set_ylabel('Frequency', fontsize=12)
                ax2.axvline(sum(sentiments)/len(sentiments), color='red', linestyle='--', 
                           label=f'Average: {sum(sentiments)/len(sentiments):.2f}')
                ax2.legend()
        
        # Questionnaire response distribution
        if self.questionnaire_data:
            df = pd.DataFrame(self.questionnaire_data)
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            
            if len(numeric_cols) > 0:
                df[numeric_cols].boxplot(ax=ax3)
                ax3.set_title('Questionnaire Response Distribution', fontsize=14, fontweight='bold')
                ax3.set_ylabel('Response Value', fontsize=12)
        
        # Activity breakdown from observations
        if self.observation_data:
            df = pd.DataFrame(self.observation_data)
            if 'category' in df.columns:
                category_counts = df['category'].value_counts()
                category_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax4)
                ax4.set_title('Observation Activity Breakdown', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Elicitation analysis visualizations saved: {save_path}")
    
    def export_elicitation_data(self, file_path: str):
        """Export elicitation analysis data to JSON file"""
        data = {
            'interviews': self.interview_data,
            'questionnaires': self.questionnaire_data,
            'observations': self.observation_data,
            'documents': self.document_data,
            'feedback': self.feedback_data,
            'exported_at': datetime.now().isoformat()
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        print(f"Elicitation data exported to {file_path}")

# Example usage and sample data
def create_sample_data():
    """Create sample elicitation data for demonstration"""
    analyzer = ElicitationAnalyzer()
    
    # Sample interview data
    analyzer.interview_data = [
        {
            'id': 'INT-001',
            'interviewee': 'John Doe',
            'role': 'Product Manager',
            'transcript': "I need the system to be fast and responsive. Users must be able to authenticate quickly and securely. The system should handle at least 1000 concurrent users without issues."
        },
        {
            'id': 'INT-002',
            'interviewee': 'Jane Smith',
            'role': 'Developer',
            'transcript': "The application must have a clean interface. Security is critical - we cannot have any data breaches. The system should be easy to maintain and update."
        }
    ]
    
    # Sample questionnaire data
    analyzer.questionnaire_data = [
        {'respondent_id': 'R001', 'auth_importance': 5, 'ui_importance': 4, 'security_importance': 5, 'comments': 'Need better mobile support'},
        {'respondent_id': 'R002', 'auth_importance': 4, 'ui_importance': 5, 'security_importance': 5, 'comments': 'Performance is key'},
        {'respondent_id': 'R003', 'auth_importance': 5, 'ui_importance': 3, 'security_importance': 4, 'comments': 'Security first'}
    ]
    
    # Sample observation data
    analyzer.observation_data = [
        {'timestamp': '2024-01-01T09:00:00', 'description': 'User logs into system', 'category': 'task', 'duration': 30},
        {'timestamp': '2024-01-01T09:05:00', 'description': 'User navigates to dashboard', 'category': 'task', 'duration': 15},
        {'timestamp': '2024-01-01T09:10:00', 'description': 'User waits for data to load', 'category': 'waiting', 'duration': 45},
        {'timestamp': '2024-01-01T09:15:00', 'description': 'User generates report', 'category': 'task', 'duration': 60}
    ]
    
    # Sample document data
    analyzer.document_data = [
        {
            'name': 'requirements_doc.pdf',
            'content': 'The system shall provide user authentication. The system must be secure. Users should have an intuitive interface.'
        }
    ]
    
    return analyzer

if __name__ == "__main__":
    # Create sample data
    analyzer = create_sample_data()
    
    # Generate report
    report = analyzer.generate_elicitation_report()
    
    print("Elicitation Analysis Report")
    print("=" * 50)
    print(f"Interviews Analyzed: {report['summary']['interviews_analyzed']}")
    print(f"Questionnaire Responses: {report['summary']['questionnaire_responses']}")
    print(f"Observation Sessions: {report['summary']['observation_sessions']}")
    print(f"Documents Processed: {report['summary']['documents_processed']}")
    
    if report['interview_analysis']:
        avg_sentiment = sum([ia['sentiment']['compound'] for ia in report['interview_analysis']]) / len(report['interview_analysis'])
        print(f"Average Interview Sentiment: {avg_sentiment:.2f}")
    
    if report['synthesis']['consolidated_requirements']:
        print(f"Consolidated Requirements: {len(report['synthesis']['consolidated_requirements'])}")
    
    # Export data
    analyzer.export_elicitation_data('sample_elicitation.json')
    
    # Create visualizations
    analyzer.create_elicitation_visualizations()
    
    print("\nElicitation analysis completed!")
```

### Step 5: Documentation
This comprehensive laboratory covers all major requirements elicitation techniques according to ISO/IEC/IEEE 29148. The interactive dashboard provides hands-on experience with:

- **Interview Management**: Structured interviews, question generation, response analysis
- **Questionnaire Builder**: Survey design, response collection, statistical analysis
- **Observation Tools**: Activity logging, workflow analysis, bottleneck identification
- **Document Analysis**: Requirements extraction, gap analysis, consolidation
- **Prototyping Interface**: Interactive prototypes, user feedback collection
- **Technique Integration**: Multi-method synthesis, conflict resolution, prioritization

The Python analysis tool provides automated analysis of all elicitation data types, including sentiment analysis, theme extraction, statistical analysis, and comprehensive reporting with visualizations. This laboratory serves as the foundation for understanding requirements elicitation best practices and techniques.
