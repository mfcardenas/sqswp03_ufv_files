# Lab 6: Requirements Management System
## ISO/IEC/IEEE 29148:2011 Requirements Management

This laboratory implements a comprehensive requirements management system following ISO/IEC/IEEE 29148:2011 standards, providing tools for requirement tracking, change management, traceability, and audit compliance.

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

1. **Implement Requirements Management Systems** - Build a complete requirements management platform
2. **Apply Change Management Processes** - Handle requirement changes with formal approval workflows
3. **Establish Traceability** - Create and maintain bidirectional traceability between requirements
4. **Ensure Audit Compliance** - Implement comprehensive audit logging and compliance features
5. **Design Database Schemas** - Create normalized database structures for requirements data
6. **Develop REST APIs** - Build RESTful APIs for requirements management operations
7. **Create Interactive Dashboards** - Develop web-based interfaces for requirements visualization

## 📋 Requirements

### Functional Requirements

- **REQ-001**: User Authentication System
  - Secure user authentication with role-based access control
  - Support for multiple authentication methods
  - Session management and security controls

- **REQ-002**: Requirements CRUD Operations
  - Create, read, update, and delete requirements
  - Version control for requirement changes
  - Status tracking (draft, review, approved, implemented)

- **REQ-003**: Change Management Workflow
  - Formal change request process
  - Approval workflows with multiple stakeholders
  - Impact analysis and change tracking

- **REQ-004**: Traceability Matrix
  - Bidirectional traceability between requirements
  - Relationship types (derives, implements, verifies, tests)
  - Impact analysis for changes

- **REQ-005**: Audit Trail System
  - Comprehensive audit logging for all operations
  - Compliance reporting and data integrity
  - User activity tracking

### Non-Functional Requirements

- **Performance**: Handle up to 10,000 requirements with sub-second query response
- **Security**: Implement authentication, authorization, and data encryption
- **Usability**: Intuitive web interface with responsive design
- **Reliability**: 99.9% uptime with automatic backup and recovery
- **Compliance**: Full ISO/IEC/IEEE 29148:2011 compliance

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Interface │    │   REST API      │    │   Database      │
│                 │    │                 │    │                 │
│ - Dashboard     │◄──►│ - Requirements  │◄──►│ - SQLite        │
│ - Forms         │    │ - Changes       │    │ - Normalized    │
│ - Reports       │    │ - Traceability  │    │ - Indexed       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                    ┌─────────────────┐
                    │   Audit Logger  │
                    │                 │
                    │ - Compliance    │
                    │ - Security      │
                    └─────────────────┘
```

## 📁 Project Structure

```
Lab6/
├── requirements_dashboard.html    # Main web interface
├── requirements_styles.css        # CSS styling
├── requirements_scripts.js        # JavaScript functionality
├── requirements_schema.sql        # Database schema
├── sample_requirements.json       # Sample data
├── requirements_tests.py          # Test suite
├── requirements_api.py           # REST API (to implement)
├── requirements_manager.py       # Core business logic (to implement)
├── change_manager.py             # Change management (to implement)
├── traceability_manager.py       # Traceability logic (to implement)
├── audit_logger.py               # Audit logging (to implement)
└── README.md                     # This file
```

## 🚀 Getting Started

### 1. Database Setup

```bash
# Create the database
sqlite3 requirements.db < requirements_schema.sql

# Load sample data (optional)
python3 -c "
import json
import sqlite3
with open('sample_requirements.json') as f:
    data = json.load(f)
# Insert sample data into database
"
```

### 2. Install Dependencies

```bash
pip install flask flask-cors sqlite3
```

### 3. Run the Application

```bash
# Start the Flask API server
python3 requirements_api.py

# Open requirements_dashboard.html in your browser
# Or serve it with a local web server
python3 -m http.server 8000
```

### 4. Access the System

- **Web Interface**: http://localhost:8000/requirements_dashboard.html
- **API Endpoints**: http://localhost:5000/api/
- **Database**: requirements.db (SQLite)

## 🔧 API Endpoints

### Requirements Management

```http
GET    /api/requirements          # List all requirements
GET    /api/requirements/{id}     # Get specific requirement
POST   /api/requirements          # Create new requirement
PUT    /api/requirements/{id}     # Update requirement
DELETE /api/requirements/{id}     # Delete requirement
```

### Change Management

```http
GET    /api/changes               # List all changes
GET    /api/changes/{id}          # Get specific change
POST   /api/changes               # Create change request
PUT    /api/changes/{id}/approve  # Approve change
```

### Traceability

```http
GET    /api/traceability/{id}     # Get traceability for requirement
POST   /api/traceability          # Create traceability link
DELETE /api/traceability/{id}     # Remove traceability link
```

### Audit

```http
GET    /api/audit/{record_id}     # Get audit trail
GET    /api/audit                 # Get all audit logs
```

## 📊 Dashboard Features

### Requirements Overview
- **Status Distribution**: Pie chart showing requirements by status
- **Priority Breakdown**: Bar chart of requirements by priority
- **Type Analysis**: Distribution of requirement types
- **Timeline View**: Requirements created over time

### Change Management
- **Pending Changes**: List of changes awaiting approval
- **Change History**: Timeline of approved changes
- **Impact Analysis**: Requirements affected by changes

### Traceability Matrix
- **Interactive Matrix**: Visual representation of relationships
- **Impact Analysis**: Show downstream effects of changes
- **Coverage Reports**: Requirements coverage analysis

### Audit & Compliance
- **Activity Logs**: Recent system activities
- **Compliance Reports**: Audit reports for compliance
- **User Activity**: Activity tracking per user

## 🧪 Testing

### Run the Test Suite

```bash
# Run all tests
python3 -m unittest requirements_tests.py -v

# Run specific test class
python3 -m unittest requirements_tests.TestRequirementsManager -v

# Run with coverage (if coverage installed)
coverage run -m unittest requirements_tests.py
coverage report
```

### Test Coverage

The test suite covers:
- ✅ Requirements CRUD operations
- ✅ Change management workflows
- ✅ Traceability matrix functionality
- ✅ Audit logging
- ✅ Database schema validation
- ✅ API integration (mocked)
- ✅ Data validation
- ✅ Performance testing

## 📈 Key Features Implemented

### 1. Requirements Management
- Full CRUD operations with validation
- Version control and change tracking
- Status workflow management
- Tag-based organization
- Metadata support

### 2. Change Management
- Formal change request process
- Multi-level approval workflows
- Impact analysis
- Change history tracking
- Automated notifications

### 3. Traceability
- Bidirectional traceability links
- Multiple relationship types
- Impact analysis for changes
- Visual traceability matrix
- Coverage reporting

### 4. Audit & Compliance
- Comprehensive audit logging
- User activity tracking
- Compliance reporting
- Data integrity validation
- Security event logging

### 5. Database Design
- Normalized schema design
- Proper indexing for performance
- Foreign key constraints
- Trigger-based audit logging
- Sample data for testing

### 6. Web Interface
- Responsive dashboard design
- Interactive charts and graphs
- Real-time data updates
- Form validation
- Modern UI/UX principles

## 🎯 Implementation Tasks

### Phase 1: Core Implementation
1. **Implement RequirementsManager class**
   - Database connection and operations
   - CRUD methods with validation
   - Version control logic

2. **Implement ChangeManager class**
   - Change request creation
   - Approval workflow
   - Status tracking

3. **Implement TraceabilityManager class**
   - Link creation and management
   - Matrix generation
   - Impact analysis

### Phase 2: API Development
4. **Implement Flask REST API**
   - Route definitions
   - Request/response handling
   - Error handling and validation

5. **Implement AuditLogger class**
   - Audit trail creation
   - Log retrieval
   - Compliance reporting

### Phase 3: Integration & Testing
6. **Integrate all components**
   - Database connections
   - API endpoints
   - Web interface integration

7. **Comprehensive testing**
   - Unit tests for all classes
   - Integration tests
   - Performance testing

## 📚 Learning Outcomes

After completing this lab, you will understand:

1. **Requirements Management Best Practices**
   - How to structure requirements databases
   - Change management processes
   - Traceability implementation

2. **Software Architecture Patterns**
   - RESTful API design
   - Database normalization
   - MVC architecture

3. **Quality Assurance**
   - Comprehensive testing strategies
   - Code coverage analysis
   - Performance testing

4. **Compliance & Security**
   - Audit logging implementation
   - Data integrity
   - Security best practices

## 🔗 Related Standards

- **ISO/IEC/IEEE 29148:2011**: Systems and software engineering — Life cycle processes — Requirements engineering
- **ISO/IEC 12207**: Systems and software engineering — Software life cycle processes
- **IEEE 830**: Recommended Practice for Software Requirements Specifications
- **CMMI-DEV**: Capability Maturity Model Integration for Development

## 📞 Support

For questions or issues with this lab:
1. Check the test suite for examples
2. Review the sample data structure
3. Examine the database schema
4. Refer to the API documentation above

## 🎉 Success Criteria

Your implementation is complete when:
- ✅ All tests pass (requirements_tests.py)
- ✅ Web dashboard loads and displays data
- ✅ API endpoints return correct responses
- ✅ Database operations work correctly
- ✅ Change management workflow functions
- ✅ Traceability matrix generates properly
- ✅ Audit logs capture all activities

---

**Note**: This lab provides a complete foundation for a production-ready requirements management system. The modular design allows for easy extension and customization based on specific organizational needs.
