# Lab 5: Requirements Validation

## Problem

### Introduction
In this laboratory, you will work on requirements validation following the ISO/IEC/IEEE 29148 standard. You have been provided with code containing intentional bugs that you must fix to create a complete requirements validation system.

### Code with Intentional Errors

#### 1. Validation Engine with Errors
Create a `validation_engine.py` file with the following code that contains errors:

```python
# validation_engine.py - CODE WITH ERRORS

import json
import re
from typing import List, Dict, Any, Tuple
from datetime import datetime
import statistics
from collections import defaultdict

class ValidationEngine:
    def __init__(self):
        self.requirements = []
        self.validation_results = {}
        self.test_cases = []
        # ERROR: Missing validation rules initialization
    
    def load_requirements(self, file_path: str) -> bool:
        """Load requirements from file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.requirements = data.get('requirements', [])
                return True
        except:
            return False
    
    def validate_requirements(self) -> Dict[str, Any]:
        """Validate all requirements"""
        # ERROR: Only basic validation
        results = {
            'total_requirements': len(self.requirements),
            'passed': 0,
            'failed': 0,
            'issues': []
        }
        
        for req in self.requirements:
            # ERROR: No actual validation logic
            results['passed'] += 1
        
        return results
    
    def generate_test_cases(self) -> List[Dict[str, Any]]:
        """Generate test cases from requirements"""
        # ERROR: Empty test case generation
        return []
    
    def perform_acceptance_testing(self) -> Dict[str, Any]:
        """Perform acceptance testing"""
        # ERROR: No acceptance testing implementation
        return {'status': 'not_implemented'}
    
    def validate_against_standards(self) -> Dict[str, Any]:
        """Validate against ISO/IEC/IEEE 29148"""
        # ERROR: No standard validation
        return {'compliant': True}
```

#### 2. Validation Dashboard with Errors
Create a `validation_dashboard.html` file with basic interface:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Validation Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .section { margin-bottom: 20px; }
        .metric { background: #f0f0f0; padding: 10px; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Requirements Validation Dashboard</h1>
    
    <div class="section">
        <h2>Validation Results</h2>
        <div id="results">
            <!-- ERROR: Empty results section -->
        </div>
    </div>
    
    <div class="section">
        <h2>Test Cases</h2>
        <div id="testCases">
            <!-- ERROR: Empty test cases section -->
        </div>
    </div>

    <script>
        // ERROR: No JavaScript functionality
        console.log('Dashboard loaded');
    </script>
</body>
</html>
```

### Tasks to Complete

#### Task 1: Fix Validation Engine
1. **Initialize validation rules properly**
2. **Implement comprehensive validation methods**:
   - Completeness validation
   - Consistency validation
   - Feasibility validation
   - Testability validation
3. **Generate test cases automatically** from requirements
4. **Implement acceptance testing framework**
5. **Add ISO/IEC/IEEE 29148 compliance checking**

#### Task 2: Complete Validation Dashboard
1. **Create comprehensive validation metrics display**
2. **Implement test case management interface**
3. **Add acceptance testing controls**
4. **Create compliance reporting**
5. **Add interactive validation charts**

#### Task 3: Create Supporting Files
1. **Complete CSS styling** (`validation_styles.css`)
2. **Functional JavaScript** (`validation_scripts.js`)
3. **Sample requirements data** (`validation_requirements.json`)
4. **Test suite** (`test_validation_engine.py`)

### Specific Issues to Resolve

1. **Missing validation rules**: No criteria for requirement validation
2. **Incomplete validation logic**: Only basic pass/fail counting
3. **Empty test case generation**: No automatic test case creation
4. **Missing acceptance testing**: No implementation of acceptance criteria
5. **Poor user interface**: Basic HTML without functionality
6. **No compliance checking**: Missing ISO standard validation
7. **Limited reporting**: No detailed validation reports

### Expected Results
- Complete validation engine with all validation types
- Interactive web dashboard with full functionality
- Automatic test case generation from requirements
- Acceptance testing framework
- ISO/IEC/IEEE 29148 compliance validation
- Comprehensive validation reporting

### Files to Create
1. `validation_engine.py` (fixed)
2. `validation_dashboard.html` (complete)
3. `validation_styles.css`
4. `validation_scripts.js`
5. `validation_requirements.json`
6. `test_validation_engine.py`

### Success Criteria
- ✅ Python code executes without errors
- ✅ All validation types implemented
- ✅ Test cases generated automatically
- ✅ Acceptance testing functional
- ✅ Web interface operational
- ✅ All tests pass
