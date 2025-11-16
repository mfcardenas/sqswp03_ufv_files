# Lab 6: Requirements Management

## Learning Objectives

After completing this laboratory, you will be able to:

1. **Design Requirements Management Systems**: Create comprehensive systems for managing requirements throughout their lifecycle
2. **Implement Version Control**: Build version control systems for requirements with audit trails
3. **Develop Change Management Workflows**: Create formal processes for managing requirement changes
4. **Build Traceability Matrices**: Implement bidirectional traceability between requirements and other artifacts
5. **Create Audit Systems**: Develop complete audit trails for compliance and governance
6. **Design REST APIs**: Build RESTful APIs for requirements management
7. **Implement Web Dashboards**: Create interactive web interfaces for requirements management
8. **Ensure ISO Compliance**: Implement systems compliant with ISO/IEC/IEEE 29148 standards

## Technical Requirements

### System Architecture
- **Backend**: Python with SQLite database (upgradeable to PostgreSQL)
- **Frontend**: HTML/CSS/JavaScript with Chart.js for visualizations
- **API**: RESTful API with JSON responses
- **Database**: Relational database with proper normalization
- **Security**: Basic authentication and authorization

### Core Components to Implement

#### 1. Requirements Repository (`requirements_manager.py`)
```python
class RequirementsManager:
    def __init__(self, db_path: str)
    def create_requirement(self, req_data: Dict, user_id: str) -> str
    def update_requirement(self, req_id: str, updates: Dict, user_id: str) -> bool
    def get_requirement(self, req_id: str) -> Optional[Dict]
    def list_requirements(self, filters: Dict = None) -> List[Dict]
    def delete_requirement(self, req_id: str, user_id: str) -> bool
    def get_requirement_history(self, req_id: str) -> List[Dict]
```

#### 2. Change Management (`change_manager.py`)
```python
class ChangeManager:
    def __init__(self, db_path: str)
    def create_change_request(self, change_data: Dict, user_id: str) -> int
    def approve_change(self, change_id: int, approver_id: str) -> bool
    def reject_change(self, change_id: int, approver_id: str, reason: str) -> bool
    def get_change_requests(self, filters: Dict = None) -> List[Dict]
```

#### 3. Traceability Engine (`traceability_manager.py`)
```python
class TraceabilityManager:
    def __init__(self, db_path: str)
    def create_traceability_link(self, source_id, target_id, rel_type, user_id) -> int
    def get_traceability_matrix(self, req_id: str) -> Dict
    def get_impact_analysis(self, req_id: str) -> Dict
```

#### 4. Web Dashboard (`requirements_dashboard.html`)
- Interactive dashboard with navigation tabs
- Requirements list with filtering and search
- Change management interface
- Traceability visualization
- Reports and analytics
- Admin panel

#### 5. REST API (`requirements_api.py`)
- CRUD endpoints for requirements
- Change management endpoints
- Traceability endpoints
- Reporting endpoints
- Health check endpoint

#### 6. Database Schema (`requirements_schema.sql`)
- Requirements table with versioning
- Changes table for workflow management
- Traceability table for links
- Audit log table for compliance
- Users and permissions tables

## Implementation Tasks

### Task 1: Database Design and Setup
1. Create comprehensive database schema
2. Implement database initialization
3. Set up proper indexes for performance
4. Create sample data for testing

### Task 2: Requirements Repository
1. Implement RequirementsManager class
2. Add CRUD operations for requirements
3. Implement version control system
4. Add search and filtering capabilities
5. Create audit logging for all operations

### Task 3: Change Management System
1. Implement ChangeManager class
2. Create change request workflow
3. Add approval/rejection functionality
4. Implement status tracking
5. Add notification system (basic)

### Task 4: Traceability Matrix
1. Implement TraceabilityManager class
2. Create bidirectional linking system
3. Implement impact analysis
4. Add relationship type management
5. Create traceability reports

### Task 5: Web Interface
1. Create responsive HTML dashboard
2. Implement navigation and tab system
3. Add requirements list with pagination
4. Create forms for CRUD operations
5. Add filtering and search functionality

### Task 6: REST API
1. Implement Flask-based REST API
2. Create endpoints for all operations
3. Add proper error handling
4. Implement CORS for frontend integration
5. Add API documentation

### Task 7: Testing and Validation
1. Create comprehensive test suite
2. Test all CRUD operations
3. Validate change management workflow
4. Test traceability functionality
5. Verify API endpoints

## Database Schema Requirements

### Requirements Table
```sql
CREATE TABLE requirements (
    id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    type VARCHAR(50) NOT NULL,
    priority VARCHAR(20) DEFAULT 'medium',
    status VARCHAR(20) DEFAULT 'draft',
    version INTEGER DEFAULT 1,
    created_by VARCHAR(100) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100),
    updated_date TIMESTAMP,
    tags TEXT,
    metadata TEXT
);
```

### Additional Required Tables
- `requirement_versions` - Version history
- `changes` - Change requests and workflow
- `traceability` - Links between requirements
- `audit_log` - Complete audit trail
- `stakeholders` - User management

## API Endpoints to Implement

### Requirements Endpoints
```
GET    /api/requirements           # List requirements with filters
POST   /api/requirements           # Create new requirement
GET    /api/requirements/<id>      # Get specific requirement
PUT    /api/requirements/<id>      # Update requirement
DELETE /api/requirements/<id>      # Delete requirement
GET    /api/requirements/<id>/history # Get version history
```

### Change Management Endpoints
```
GET    /api/changes                # List change requests
POST   /api/changes                # Create change request
POST   /api/changes/<id>/approve   # Approve change
POST   /api/changes/<id>/reject    # Reject change
```

### Traceability Endpoints
```
POST   /api/traceability           # Create traceability link
GET    /api/traceability/<id>      # Get traceability matrix
GET    /api/traceability/<id>/impact # Get impact analysis
```

## Frontend Requirements

### Dashboard Features
- **Navigation**: Tab-based navigation system
- **Requirements List**: Sortable, filterable table
- **Search**: Real-time search functionality
- **Forms**: Modal forms for create/edit operations
- **Charts**: Status and analytics visualizations
- **Responsive**: Mobile-friendly design

### Key Components
1. **Header**: Logo, user info, navigation
2. **Dashboard**: Metrics cards and recent activity
3. **Requirements**: List, filters, CRUD operations
4. **Changes**: Change requests management
5. **Traceability**: Link creation and visualization
6. **Reports**: Charts and analytics
7. **Admin**: User management and settings

## Testing Requirements

### Unit Tests
- Test all CRUD operations
- Validate version control
- Test change workflow
- Verify traceability links
- Check audit logging

### Integration Tests
- Test API endpoints
- Validate database operations
- Test frontend-backend integration
- Verify data consistency

### Performance Tests
- Test with 1000+ requirements
- Validate query performance
- Check memory usage
- Test concurrent operations

## Success Criteria

### Functional Requirements (60%)
- ✅ Requirements CRUD operations fully functional
- ✅ Version control system working
- ✅ Change management workflow operational
- ✅ Traceability matrix implemented
- ✅ Web dashboard interactive and responsive
- ✅ REST API complete with all endpoints
- ✅ Database properly normalized and indexed

### Code Quality (20%)
- ✅ Clean, well-documented code
- ✅ Proper error handling and validation
- ✅ Unit tests with >80% coverage
- ✅ RESTful API design
- ✅ Secure coding practices

### User Experience (10%)
- ✅ Intuitive web interface
- ✅ Fast loading times (<2s)
- ✅ Responsive design
- ✅ Clear error messages
- ✅ Accessible forms and navigation

### Compliance & Documentation (10%)
- ✅ ISO/IEC/IEEE 29148 compliant
- ✅ Complete audit trail
- ✅ Comprehensive documentation
- ✅ API documentation included

## Deliverables Checklist

### Code Files
- [ ] `requirements_manager.py` - Core requirements management
- [ ] `change_manager.py` - Change management workflow
- [ ] `traceability_manager.py` - Traceability engine
- [ ] `requirements_api.py` - REST API
- [ ] `requirements_dashboard.html` - Web interface
- [ ] `requirements_styles.css` - CSS styling
- [ ] `requirements_scripts.js` - Frontend JavaScript
- [ ] `requirements_tests.py` - Test suite

### Database Files
- [ ] `requirements_schema.sql` - Database schema
- [ ] `sample_requirements.json` - Sample data

### Documentation
- [ ] `README.md` - Setup and usage instructions
- [ ] `API_DOCUMENTATION.md` - API reference
- [ ] `USER_GUIDE.md` - User manual

## Time Allocation
- **Planning & Design**: 3 hours
- **Database Implementation**: 4 hours
- **Core Logic Development**: 6 hours
- **API Development**: 4 hours
- **Frontend Development**: 6 hours
- **Testing & Debugging**: 4 hours
- **Documentation**: 3 hours
- **Total**: 30 hours

## Advanced Challenges (Optional)

### Challenge 1: Real-time Collaboration
Implement WebSocket support for real-time updates when multiple users are working simultaneously.

### Challenge 2: Advanced Reporting
Add PDF report generation and email notifications for requirement changes.

### Challenge 3: Integration Capabilities
Implement webhooks for integration with external systems like Jira or Azure DevOps.

### Challenge 4: Performance Optimization
Optimize for handling 10,000+ requirements with sub-second query response times.

## Resources

### Python Libraries
- `flask` - Web framework for API
- `flask-cors` - CORS support
- `sqlite3` - Database operations
- `json` - Data serialization
- `datetime` - Date/time handling

### Frontend Libraries
- `Chart.js` - Data visualization
- `Font Awesome` - Icons
- `Google Fonts` - Typography

### Development Tools
- `unittest` - Python testing framework
- `Postman` - API testing
- `DB Browser for SQLite` - Database inspection

## Evaluation Rubric

### Requirements Management (25%)
- Complete CRUD operations implemented
- Version control system functional
- Search and filtering working
- Audit trail complete

### Change Management (20%)
- Change request workflow implemented
- Approval/rejection process working
- Status tracking functional
- Notifications implemented

### Traceability (20%)
- Bidirectional links working
- Impact analysis functional
- Relationship types supported
- Matrix visualization implemented

### API & Integration (15%)
- RESTful API complete
- All endpoints functional
- Proper error handling
- CORS configured

### User Interface (10%)
- Responsive design
- Intuitive navigation
- Forms functional
- Charts displaying data

### Testing & Quality (10%)
- Unit tests comprehensive
- Integration tests passing
- Code well-documented
- Error handling robust

Implement a production-ready requirements management system that demonstrates enterprise-level software engineering practices and full compliance with ISO/IEC/IEEE 29148 standards.
