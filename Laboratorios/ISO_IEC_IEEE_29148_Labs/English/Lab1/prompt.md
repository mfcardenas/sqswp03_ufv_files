# Lab 1: Introduction to Requirements Engineering

## Learning Objectives
By the end of this laboratory, students will be able to:

1. Understand the fundamental concepts of Requirements Engineering
2. Identify different types of requirements and their characteristics
3. Apply the ISO/IEC/IEEE 29148 Requirements Engineering process
4. Create basic requirements artifacts using standard templates
5. Perform stakeholder analysis and mapping
6. Assess requirements quality using established criteria
7. Use Python tools for requirements analysis and reporting

## Prerequisites
- Basic understanding of software development concepts
- Familiarity with HTML, CSS, and JavaScript (recommended)
- Python programming knowledge (recommended)
- Text editor or IDE for code development

## Materials Needed
- Computer with internet access
- Web browser (Chrome, Firefox, or Edge recommended)
- Python 3.x installed
- Text editor (VS Code, Sublime Text, or similar)
- Local web server (optional, for advanced features)

## Laboratory Tasks

### Task 1: Interactive Requirements Engineering Dashboard (40 points)
Create an interactive web-based dashboard that demonstrates Requirements Engineering concepts:

1. **Core Concepts Section**: Implement a section that explains:
   - What is Requirements Engineering?
   - Types of requirements (functional, non-functional, constraints)
   - Common challenges and how to address them

2. **Process Section**: Create an interactive process diagram showing:
   - Requirements Elicitation techniques
   - Analysis and specification activities
   - Validation and management processes
   - Include clickable tools for each process step

3. **Artifacts Section**: Develop templates for:
   - Software Requirements Specification (SRS)
   - Use Case specifications
   - User Stories with acceptance criteria
   - Requirements Traceability Matrix

4. **Stakeholder Analysis Section**: Implement:
   - Stakeholder input form
   - Power-Interest grid visualization
   - Dynamic stakeholder mapping

5. **Quality Assessment Section**: Create:
   - Quality criteria checklists
   - Automated quality scoring
   - Recommendations for improvement

6. **Standards Overview Section**: Document:
   - ISO/IEC/IEEE 29148 structure
   - Key sections and their purposes
   - Benefits of following the standard

**Deliverables**:
- `requirements_intro.html` - Main dashboard file
- `requirements.css` - Styling for the dashboard
- `requirements.js` - Interactive functionality
- Screenshots of the working dashboard

### Task 2: Python Requirements Analysis Tool (35 points)
Develop a Python class for automated requirements analysis:

1. **Requirements Management**: Implement methods for:
   - Adding new requirements with metadata
   - Loading requirements from JSON files
   - Classifying requirements by type and priority
   - Tracking requirement status and changes

2. **Quality Assessment**: Create functionality for:
   - Automated quality checking against criteria
   - Ambiguity detection in requirement text
   - Quality scoring and recommendations
   - Batch quality assessment for multiple requirements

3. **Traceability Building**: Implement:
   - Requirements-to-design element linking
   - Requirements-to-test case mapping
   - Traceability matrix generation
   - Relationship visualization

4. **Reporting and Visualization**: Develop:
   - Comprehensive requirements reports
   - Statistical analysis of requirements
   - Data visualization using matplotlib/seaborn
   - Export functionality to JSON

**Deliverables**:
- `requirements_analyzer.py` - Complete Python class
- Sample data file with test requirements
- Generated reports and visualizations
- Unit tests for key functionality

### Task 3: Requirements Engineering Process Application (25 points)
Apply the learned concepts to a real-world scenario:

1. **Scenario Analysis**: Choose one of the following scenarios:
   - Online banking system
   - E-commerce platform
   - Healthcare management system
   - Educational management system

2. **Requirements Elicitation**: For your chosen scenario:
   - Identify key stakeholders
   - List potential elicitation techniques
   - Create a stakeholder map

3. **Requirements Development**: Develop:
   - 5 functional requirements
   - 3 non-functional requirements
   - 2 constraints
   - Use proper requirement formatting

4. **Quality Assessment**: Evaluate your requirements using:
   - The quality criteria from the dashboard
   - The Python analysis tool
   - Document improvement recommendations

5. **Traceability Setup**: Create:
   - Requirements Traceability Matrix
   - Links to potential design elements
   - Test case mappings

**Deliverables**:
- `scenario_analysis.md` - Complete analysis document
- Requirements artifacts in appropriate formats
- Quality assessment results
- Traceability documentation

## Assessment Criteria

### Task 1: Interactive Dashboard (40%)
- **Functionality (15%)**: All sections work correctly
- **Interactivity (10%)**: JavaScript functionality is implemented
- **Design (10%)**: Professional appearance and usability
- **Content Accuracy (5%)**: Correct RE concepts and standards

### Task 2: Python Tool (35%)
- **Code Quality (10%)**: Well-structured, documented code
- **Functionality (15%)**: All required methods implemented
- **Analysis Features (5%)**: Quality assessment and reporting
- **Visualization (5%)**: Charts and graphs generated correctly

### Task 3: Process Application (25%)
- **Scenario Analysis (5%)**: Appropriate stakeholder identification
- **Requirements Quality (10%)**: Well-written, complete requirements
- **Traceability (5%)**: Proper linking and documentation
- **Documentation (5%)**: Clear, professional presentation

## Submission Requirements
1. All source code files with proper comments
2. Working web dashboard (HTML/CSS/JS)
3. Python analysis tool with sample data
4. Scenario analysis document
5. Screenshots of working applications
6. Brief report explaining implementation decisions

## Time Estimate
- Task 1: 4-6 hours
- Task 2: 3-4 hours
- Task 3: 2-3 hours
- Total: 9-13 hours

## Additional Resources
- ISO/IEC/IEEE 29148 Standard Documentation
- Requirements Engineering textbooks
- Online tutorials for HTML/CSS/JavaScript
- Python documentation for data analysis
- Sample requirements documents from real projects

## Tips for Success
1. Start with the HTML structure, then add CSS styling
2. Implement JavaScript functionality incrementally
3. Test the Python tool with sample data early
4. Use the dashboard to understand concepts before applying them
5. Document your work as you progress
6. Ask for help if you get stuck on any concept
