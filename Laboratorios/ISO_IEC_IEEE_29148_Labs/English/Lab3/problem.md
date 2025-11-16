# Lab 3: Requirements Analysis & Modeling

## Learning Objectives
By the end of this laboratory, students will be able to:

1. **Analyze requirements** using systematic decomposition techniques
2. **Create different types of requirement models** (functional, data, behavioral)
3. **Identify and resolve requirement inconsistencies** through analysis
4. **Apply quality criteria** to evaluate requirement specifications
5. **Use modeling tools** to represent complex requirement relationships
6. **Perform requirement prioritization** and dependency analysis

## Scenario: Smart Home Automation System

You are developing a smart home automation system that integrates lighting, security, climate control, and entertainment systems. The system needs to provide seamless automation while maintaining user control and security.

## Task: Requirements Analysis & Modeling

### Problem Statement
Your team has collected initial requirements through elicitation, but they contain inconsistencies, ambiguities, and missing information. You need to analyze these requirements, identify issues, and create proper models.

### Initial Requirements (with intentional issues for you to fix):

**Functional Requirements:**
- FR1: System shall control lights
- FR2: System shall control lights based on time
- FR3: System shall control lights based on motion
- FR4: System shall control lights based on user preference
- FR5: System shall provide security monitoring
- FR6: System shall provide security monitoring with cameras
- FR7: System shall provide security monitoring with sensors
- FR8: System shall control temperature
- FR9: System shall control temperature automatically
- FR10: System shall control temperature manually

**Non-Functional Requirements:**
- NFR1: System shall respond within 2 seconds
- NFR2: System shall be available 99.9% of time
- NFR3: System shall be secure
- NFR4: System shall be user friendly
- NFR5: System shall support 100 users

**Constraints:**
- C1: System shall use wireless communication
- C2: System shall work with existing home wiring
- C3: System shall cost less than $500
- C4: System shall be installed by homeowner

## Code Base with Issues (Fix the problems!)

### Step 1: Create a requirements analysis tool
Here's the initial code with several bugs and issues that you need to fix:

```python
# requirements_analysis.py - FIX THE BUGS!

import json
from typing import List, Dict, Any
from collections import defaultdict

class RequirementsAnalyzer:
    def __init__(self):
        self.requirements = []
        self.issues = []
    
    def load_requirements(self, file_path: str):
        """Load requirements from JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.requirements = data.get('requirements', [])
    
    def analyze_requirements(self) -> Dict[str, Any]:
        """Analyze requirements for quality issues"""
        analysis = {
            'total_requirements': len(self.requirements),
            'quality_score': 0,
            'issues_found': [],
            'recommendations': []
        }
        
        # BUG: This loop doesn't work correctly
        for req in self.requirements:
            if self.check_ambiguity(req):
                analysis['issues_found'].append(f"Ambiguous: {req['id']}")
            if self.check_completeness(req):
                analysis['issues_found'].append(f"Incomplete: {req['id']}")
            if self.check_consistency(req):
                analysis['issues_found'].append(f"Inconsistent: {req['id']}")
        
        # BUG: Quality score calculation is wrong
        analysis['quality_score'] = len(self.requirements) - len(analysis['issues_found'])
        
        return analysis
    
    def check_ambiguity(self, requirement: Dict[str, Any]) -> bool:
        """Check if requirement is ambiguous"""
        text = requirement.get('text', '').lower()
        
        # BUG: This check is too simple and misses many cases
        ambiguous_words = ['etc', 'and/or', 'as appropriate']
        return any(word in text for word in ambiguous_words)
    
    def check_completeness(self, requirement: Dict[str, Any]) -> bool:
        """Check if requirement is complete"""
        text = requirement.get('text', '')
        
        # BUG: Missing proper completeness checks
        required_elements = ['shall', 'should', 'must']
        return not any(elem in text for elem in required_elements)
    
    def check_consistency(self, requirement: Dict[str, Any]) -> bool:
        """Check if requirement is consistent with others"""
        # BUG: This doesn't actually check consistency
        return False
    
    def categorize_requirements(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize requirements by type"""
        categories = defaultdict(list)
        
        # BUG: Categorization logic is incomplete
        for req in self.requirements:
            text = req.get('text', '').lower()
            if 'control' in text:
                categories['functional'].append(req)
            elif 'shall respond' in text:
                categories['non_functional'].append(req)
            else:
                categories['other'].append(req)
        
        return dict(categories)
    
    def identify_dependencies(self) -> List[Tuple[str, str]]:
        """Identify dependencies between requirements"""
        dependencies = []
        
        # BUG: No dependency identification logic implemented
        return dependencies
    
    def prioritize_requirements(self) -> List[Dict[str, Any]]:
        """Prioritize requirements based on criteria"""
        # BUG: Simple prioritization that doesn't consider multiple factors
        return sorted(self.requirements, key=lambda x: x.get('id', ''))
    
    def generate_models(self) -> Dict[str, Any]:
        """Generate different types of requirement models"""
        models = {
            'functional_hierarchy': {},
            'data_flow': {},
            'state_machine': {},
            'use_case': {}
        }
        
        # BUG: Model generation is not implemented
        return models

# BUGGY USAGE EXAMPLE
if __name__ == "__main__":
    analyzer = RequirementsAnalyzer()
    
    # This will fail because the file doesn't exist
    analyzer.load_requirements('requirements.json')
    
    analysis = analyzer.analyze_requirements()
    print(f"Analysis: {analysis}")
    
    categories = analyzer.categorize_requirements()
    print(f"Categories: {categories}")
```

### Step 2: Create a modeling dashboard
Here's the HTML code with issues to fix:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Requirements Modeling Dashboard - FIX ME!</title>
    <link rel="stylesheet" href="modeling_styles.css">
</head>
<body>
    <header>
        <h1>Requirements Analysis & Modeling</h1>
        <nav>
            <button id="analysisBtn">Analysis</button>
            <button id="modelingBtn">Modeling</button>
            <button id="validationBtn">Validation</button>
        </nav>
    </header>

    <main>
        <section id="analysisSection">
            <h2>Requirements Analysis</h2>
            <div id="analysisContent">
                <!-- BUG: No content loaded initially -->
            </div>
        </section>

        <section id="modelingSection" style="display: none;">
            <h2>Requirements Modeling</h2>
            <div class="modeling-tools">
                <div class="model-type">
                    <h3>Functional Hierarchy</h3>
                    <div id="functionalModel" class="model-canvas">
                        <!-- BUG: Empty canvas -->
                    </div>
                </div>
                
                <div class="model-type">
                    <h3>Data Flow Diagram</h3>
                    <div id="dataFlowModel" class="model-canvas">
                        <!-- BUG: Empty canvas -->
                    </div>
                </div>
                
                <div class="model-type">
                    <h3>Use Case Diagram</h3>
                    <div id="useCaseModel" class="model-canvas">
                        <!-- BUG: Empty canvas -->
                    </div>
                </div>
            </div>
        </section>

        <section id="validationSection" style="display: none;">
            <h2>Requirements Validation</h2>
            <div id="validationContent">
                <!-- BUG: No validation tools -->
            </div>
        </section>
    </main>

    <script src="modeling_scripts.js"></script>
</body>
</html>
```

## Tasks to Complete

### Task 1: Fix the Python Analysis Tool (40 points)
1. **Fix the requirement loading** - Handle missing files gracefully
2. **Improve ambiguity detection** - Add more sophisticated checks
3. **Fix completeness checking** - Implement proper completeness criteria
4. **Implement consistency checking** - Compare requirements for conflicts
5. **Enhance categorization** - Add more requirement types and better logic
6. **Add dependency identification** - Find relationships between requirements
7. **Improve prioritization** - Consider multiple prioritization factors
8. **Implement model generation** - Create basic functional, data, and behavioral models

### Task 2: Fix the Modeling Dashboard (30 points)
1. **Add navigation functionality** - Make tabs work properly
2. **Implement analysis display** - Show analysis results dynamically
3. **Create modeling canvases** - Add interactive modeling capabilities
4. **Add validation tools** - Implement requirement validation features
5. **Improve user interface** - Make it more intuitive and professional

### Task 3: Create Sample Data & Testing (20 points)
1. **Create sample requirements data** - JSON file with the smart home requirements
2. **Add comprehensive tests** - Unit tests for all analysis functions
3. **Generate sample models** - Create example diagrams and hierarchies
4. **Add error handling** - Robust error handling throughout

### Task 4: Documentation & Reporting (10 points)
1. **Add comprehensive comments** - Document all functions and classes
2. **Create usage examples** - Show how to use the analysis tools
3. **Generate analysis reports** - Create formatted output reports
4. **Add model visualization** - Export models to different formats

## Assessment Criteria

### Code Quality (40%)
- **Bug Fixes**: All identified issues resolved
- **Functionality**: All features work as specified
- **Error Handling**: Proper exception handling
- **Code Structure**: Well-organized and maintainable

### Requirements Engineering (35%)
- **Analysis Quality**: Proper identification of requirement issues
- **Modeling Accuracy**: Correct representation of requirement relationships
- **Validation Completeness**: Thorough validation of requirements
- **Documentation**: Clear and comprehensive

### Technical Implementation (25%)
- **Algorithm Correctness**: Proper analysis and modeling algorithms
- **Data Structures**: Appropriate use of data structures
- **Performance**: Efficient processing of requirements
- **Extensibility**: Easy to add new analysis features

## Deliverables
- Fixed Python analysis tool with all bugs resolved
- Working modeling dashboard with interactive features
- Sample requirements data file
- Comprehensive test suite
- Documentation and usage examples

## Success Metrics
- All Python functions work without errors
- Dashboard loads and displays analysis results
- Sample data processed correctly
- Models generated for different requirement types
- Test coverage > 80%

Remember: Focus on systematic analysis and proper modeling techniques. The code has intentional bugs that you need to identify and fix while implementing the missing functionality.
