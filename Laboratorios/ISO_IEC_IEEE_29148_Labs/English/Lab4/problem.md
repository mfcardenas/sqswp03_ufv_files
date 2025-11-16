# Lab 4: Requirements Specification

## 🎯 **Objective**
Master the art of requirements specification by creating comprehensive, unambiguous requirement documents using industry-standard formats and templates that meet ISO/IEC/IEEE 29148 standards.

## 📋 **Learning Outcomes**
By completing this laboratory, you will be able to:
- Create well-structured Software Requirements Specifications (SRS)
- Apply different specification formats (textual, tabular, graphical)
- Use formal specification languages and notations
- Implement requirement traceability matrices
- Validate specifications against quality criteria
- Create requirement baselines and version control

## 🛠️ **Tools & Technologies**
- **Python 3.x** for specification processing and validation
- **HTML/CSS/JavaScript** for interactive specification viewer
- **JSON/YAML** for structured requirement storage
- **PlantUML/Mermaid** for graphical specifications
- **Git** for version control and baselines

## 📝 **Problem Description**

### **Situation**
Your team has completed requirements analysis and modeling for the smart home automation system. Now you need to create formal requirement specifications that can be used by developers, testers, and stakeholders. The specifications must be clear, unambiguous, and traceable.

### **Problem**
The current requirement specifications are poorly structured and contain multiple issues:
- Lack of proper SRS structure and templates
- Missing requirement attributes and metadata
- No traceability between requirements
- Inconsistent formatting and terminology
- Missing validation and verification criteria
- No version control or baseline management

### **Your Task**
You must create a comprehensive requirements specification system that:

1. **Generates structured SRS documents** with proper sections and formatting
2. **Implements multiple specification formats** (textual, tabular, graphical)
3. **Creates traceability matrices** linking requirements to design and test
4. **Validates specifications** against quality standards
5. **Manages requirement baselines** with version control
6. **Provides interactive specification viewer** for stakeholders

### **Files with Issues**

#### **1. specification_generator.py (Specification Engine)**
This file contains multiple bugs that you must fix:

```python
# specification_generator.py - CONTAINS INTENTIONAL BUGS

import json
import yaml
from typing import List, Dict, Any, Optional
from datetime import datetime
import re
from collections import defaultdict

class SpecificationGenerator:
    def __init__(self):
        self.requirements = []
        self.specifications = {}
        self.traceability_matrix = {}
        self.baselines = {}
    
    def load_requirements(self, file_path: str) -> bool:
        """Load requirements from file"""
        # BUG: No error handling
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.requirements = data.get('requirements', [])
            return True
    
    def generate_srs(self) -> Dict[str, Any]:
        """Generate Software Requirements Specification"""
        srs = {
            'title': 'Software Requirements Specification',
            'version': '1.0',
            'date': datetime.now().isoformat(),
            'sections': {}
        }
        
        # BUG: Missing SRS sections
        srs['sections']['introduction'] = self._generate_introduction()
        # BUG: Other sections not generated
        
        return srs
    
    def _generate_introduction(self) -> Dict[str, Any]:
        """Generate introduction section"""
        return {
            'purpose': 'This document specifies the requirements for the Smart Home System',
            'scope': 'Home automation and security features',
            'definitions': {},
            'references': []
        }
    
    def apply_specification_formats(self) -> Dict[str, Any]:
        """Apply different specification formats"""
        formats = {
            'textual': self._apply_textual_format(),
            'tabular': self._apply_tabular_format(),
            'graphical': self._apply_graphical_format()
        }
        return formats
    
    def _apply_textual_format(self) -> List[str]:
        """Apply textual specification format"""
        # BUG: Empty implementation
        return []
    
    def _apply_tabular_format(self) -> List[Dict[str, Any]]:
        """Apply tabular specification format"""
        # BUG: Empty implementation
        return []
    
    def _apply_graphical_format(self) -> Dict[str, Any]:
        """Apply graphical specification format"""
        # BUG: Empty implementation
        return {}
    
    def create_traceability_matrix(self) -> Dict[str, Any]:
        """Create requirements traceability matrix"""
        # BUG: Empty implementation
        return {}
    
    def validate_specifications(self) -> Dict[str, Any]:
        """Validate specifications against quality criteria"""
        validation_results = {
            'completeness': False,
            'consistency': False,
            'traceability': False,
            'testability': False,
            'issues': []
        }
        
        # BUG: No actual validation logic
        return validation_results
    
    def create_baseline(self, version: str) -> Dict[str, Any]:
        """Create requirement baseline"""
        # BUG: Empty implementation
        return {}
    
    def export_specifications(self, format_type: str, file_path: str):
        """Export specifications in different formats"""
        # BUG: No export functionality
        pass
    
    def generate_specification_report(self) -> str:
        """Generate specification quality report"""
        # BUG: Basic report only
        report = f"""
# Specification Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Requirements: {len(self.requirements)}
"""
        return report
```

#### **2. specification_viewer.html (Interactive Viewer)**
Incomplete HTML file with basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Requirements Specification Viewer</title>
    <!-- BUG: Missing CSS link -->
</head>
<body>
    <header>
        <h1>Requirements Specification Viewer</h1>
        <!-- BUG: Missing navigation -->
    </header>

    <main>
        <!-- BUG: Missing content sections -->
        <div id="specContent">
            <p>Loading specifications...</p>
        </div>
    </main>

    <!-- BUG: Missing JavaScript -->
</body>
</html>
```

#### **3. specification_styles.css (Styling)**
Empty CSS file:

```css
/* BUG: No styles implemented */
```

#### **4. specification_scripts.js (Functionality)**
Empty JavaScript file:

```javascript
// BUG: No functionality implemented
```

### **Sample Data**
Create a `sample_requirements.json` file:

```json
{
  "requirements": [
    {
      "id": "FR1",
      "text": "System shall control lights based on time and motion",
      "type": "functional",
      "priority": "high",
      "category": "lighting"
    },
    {
      "id": "FR2", 
      "text": "System shall provide security monitoring with cameras and sensors",
      "type": "functional",
      "priority": "high",
      "category": "security"
    },
    {
      "id": "NFR1",
      "text": "System shall respond within 2 seconds to user commands",
      "type": "non_functional",
      "priority": "high",
      "category": "performance"
    }
  ]
}
```

## ✅ **Success Criteria**
- SRS documents are generated with proper structure and formatting
- Multiple specification formats are implemented and functional
- Traceability matrix links requirements correctly
- Specifications pass validation criteria
- Interactive viewer loads and displays specifications properly
- Baseline management works with version control

## 🎯 **Expected Deliverables**
1. `specification_generator.py` - Fixed and complete specification engine
2. `specification_viewer.html` - Complete interactive viewer
3. `specification_styles.css` - Complete styling
4. `specification_scripts.js` - Complete functionality
5. `sample_requirements.json` - Test data
6. Documentation of fixes and implementations

This laboratory will give you practical experience in creating professional requirements specifications according to ISO/IEC/IEEE 29148 standards!
