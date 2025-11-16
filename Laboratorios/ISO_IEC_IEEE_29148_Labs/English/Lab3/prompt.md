# Lab 3: Requirements Analysis & Modeling - Student Instructions

## 🎯 **Objective**
Apply systematic requirements analysis techniques and create multiple requirement models to transform raw requirements into structured, analyzable artifacts that support software development.

## 📋 **Learning Outcomes**
By completing this laboratory, you will be able to:
- Analyze requirements for quality attributes (completeness, consistency, ambiguity)
- Categorize requirements by type (functional, non-functional, constraints)
- Identify and document requirement dependencies
- Create different types of requirement models
- Implement requirement prioritization schemes
- Validate requirements against quality criteria

## 🛠️ **Tools & Technologies**
- **Python 3.x** for analysis engine
- **HTML/CSS/JavaScript** for interactive dashboard
- **JSON** for data storage
- **Chart.js** for data visualization
- **Unit testing framework** for validation

## 📝 **Tasks**

### **Task 1: Fix the Requirements Analysis Tool (60 points)**

#### **Step 1.1: Fix File Loading Issues**
- Locate the `load_requirements()` method in `requirements_analysis.py`
- Add proper error handling for missing files
- Implement JSON parsing error handling
- Add informative error messages for different failure scenarios

#### **Step 1.2: Fix Analysis Logic Bugs**
- Fix the `analyze_requirements()` method to properly process all requirements
- Correct the quality score calculation algorithm
- Implement proper issue tracking and reporting
- Add comprehensive analysis results structure

#### **Step 1.3: Enhance Ambiguity Detection**
- Improve the `check_ambiguity()` method with more sophisticated patterns
- Add detection for vague quantifiers ("some", "many", "few")
- Implement length-based ambiguity checks
- Add context-aware ambiguity detection

#### **Step 1.4: Implement Completeness Checking**
- Fix the `check_completeness()` method to properly validate modal verbs
- Add checks for subject-verb-object structure
- Implement action verb validation
- Add completeness scoring

#### **Step 1.5: Add Consistency Validation**
- Implement the `check_basic_consistency()` method
- Add detection of contradictory terms
- Implement basic conflict identification
- Add consistency scoring

#### **Step 1.6: Fix Categorization Logic**
- Correct the `categorize_requirements()` method
- Improve requirement type identification patterns
- Add support for interface requirements
- Implement proper category assignment

#### **Step 1.7: Implement Dependency Analysis**
- Complete the `identify_dependencies()` method
- Add sequential dependency detection
- Implement conditional dependency identification
- Add functional dependency analysis

#### **Step 1.8: Add Prioritization System**
- Implement the `prioritize_requirements()` method
- Add multi-factor priority scoring
- Implement business value assessment
- Add priority-based sorting

#### **Step 1.9: Create Model Generation**
- Complete the `generate_models()` method
- Implement functional hierarchy generation
- Add data flow model creation
- Create use case and dependency models

#### **Step 1.10: Add Export Functionality**
- Implement the `export_analysis()` method
- Add comprehensive results export
- Include model data in exports
- Add timestamp tracking

### **Task 2: Fix the Modeling Dashboard (30 points)**

#### **Step 2.1: Complete HTML Structure**
- Fix the navigation system in `modeling_dashboard.html`
- Add proper section switching functionality
- Implement content area management
- Add loading states and placeholders

#### **Step 2.2: Implement CSS Styling**
- Complete the `modeling_styles.css` file
- Add responsive design elements
- Implement proper navigation styling
- Add model canvas styling

#### **Step 2.3: Add JavaScript Functionality**
- Complete the `modeling_scripts.js` file
- Implement section navigation
- Add analysis result display
- Create model visualization functions

#### **Step 2.4: Add Chart Integration**
- Integrate Chart.js for quality metrics visualization
- Implement interactive charts
- Add chart update functionality
- Create multiple chart types

#### **Step 2.5: Implement Model Display**
- Add functional hierarchy visualization
- Implement data flow diagram display
- Create use case diagram representation
- Add dependency graph visualization

### **Task 3: Create Test Suite (10 points)**

#### **Step 3.1: Implement Unit Tests**
- Create comprehensive test cases in `test_requirements_analysis.py`
- Test all major functionality
- Add edge case testing
- Implement test data management

#### **Step 3.2: Test Analysis Functions**
- Test ambiguity detection accuracy
- Validate completeness checking
- Test categorization logic
- Verify prioritization algorithms

#### **Step 3.3: Test Model Generation**
- Test model creation functions
- Validate model data structures
- Test export functionality
- Verify error handling

## 📊 **Deliverables**

### **Code Files:**
1. `requirements_analysis.py` - Fixed and complete analysis engine
2. `modeling_dashboard.html` - Complete web interface
3. `modeling_styles.css` - Complete styling
4. `modeling_scripts.js` - Complete functionality
5. `test_requirements_analysis.py` - Comprehensive test suite

### **Data Files:**
1. `sample_requirements.json` - Test data file
2. `requirements_analysis_results.json` - Analysis output
3. `requirements_analysis_report.md` - Generated report

### **Documentation:**
1. Code comments explaining all fixes and implementations
2. Test results and coverage report
3. Usage examples and demonstrations

## ✅ **Validation Criteria**

### **Functional Requirements:**
- [ ] All Python syntax errors fixed
- [ ] File loading works with proper error handling
- [ ] Analysis produces correct results
- [ ] Quality metrics calculated accurately
- [ ] Models generated successfully
- [ ] Dashboard loads and functions properly
- [ ] Charts display correctly
- [ ] Export functionality works

### **Quality Requirements:**
- [ ] Code follows PEP 8 style guidelines
- [ ] Functions have proper docstrings
- [ ] Error handling implemented throughout
- [ ] Unit tests pass with 100% coverage
- [ ] HTML validates without errors
- [ ] CSS is responsive and accessible
- [ ] JavaScript follows modern best practices

### **Analysis Accuracy:**
- [ ] Ambiguity detection identifies 90%+ of ambiguous terms
- [ ] Completeness checking validates modal verbs correctly
- [ ] Categorization assigns correct types to 95%+ requirements
- [ ] Prioritization produces logical ranking
- [ ] Dependency analysis identifies relationships accurately

## 🧪 **Testing Instructions**

### **Step 1: Run the Analysis Tool**
```bash
python requirements_analysis.py
```

### **Step 2: Open the Dashboard**
- Open `modeling_dashboard.html` in a web browser
- Test all navigation sections
- Load and analyze requirements
- Generate and view models

### **Step 3: Run Unit Tests**
```bash
python -m unittest test_requirements_analysis.py
```

### **Step 4: Validate Results**
- Check analysis output for correctness
- Verify model generation
- Test export functionality
- Review generated reports

## 📈 **Assessment Rubric**

| Criteria | Excellent (90-100) | Good (80-89) | Satisfactory (70-79) | Needs Improvement (<70) |
|----------|-------------------|--------------|---------------------|----------------------|
| **Code Quality** | Clean, well-documented, follows best practices | Good structure, some documentation | Basic functionality, minimal documentation | Poor structure, missing functionality |
| **Bug Fixes** | All issues identified and fixed correctly | Most issues fixed, minor problems remain | Some fixes implemented, major issues persist | Few fixes, significant problems remain |
| **Analysis Accuracy** | 95%+ accuracy in all analysis functions | 85-94% accuracy | 70-84% accuracy | <70% accuracy |
| **Model Generation** | All models created correctly with proper visualization | Most models work, minor visualization issues | Basic models created, significant visualization problems | Models incomplete or non-functional |
| **Testing** | Comprehensive tests with 100% coverage | Good test coverage, some edge cases missed | Basic tests implemented | Minimal or no testing |
| **Documentation** | Complete documentation with examples | Good documentation, some areas unclear | Basic documentation | Poor or missing documentation |

## 🎯 **Success Criteria**
- All Python code runs without syntax errors
- Analysis tool produces correct results for sample data
- Web dashboard loads and functions properly
- All unit tests pass
- Models are generated and displayed correctly
- Export functionality works as expected
- Code is well-documented and maintainable

## 💡 **Hints & Tips**

### **Debugging the Analysis Tool:**
- Start with simple test cases
- Use print statements to trace execution
- Check data types and structures
- Validate JSON parsing

### **Fixing the Dashboard:**
- Test HTML structure first
- Add CSS incrementally
- Implement JavaScript functions one at a time
- Use browser developer tools for debugging

### **Model Generation:**
- Start with simple models (functional hierarchy)
- Build complexity gradually
- Test each model type separately
- Validate data structures

### **Testing Best Practices:**
- Write tests for each function
- Include edge cases and error conditions
- Test with different data sets
- Verify expected vs actual results

## 🚀 **Next Steps**
After completing this laboratory:
1. Apply these techniques to real project requirements
2. Explore advanced modeling techniques (UML, BPMN)
3. Implement automated requirement validation
4. Integrate with requirement management tools

Remember: Requirements analysis and modeling are iterative processes. The quality of your analysis directly impacts the success of the software development project!
