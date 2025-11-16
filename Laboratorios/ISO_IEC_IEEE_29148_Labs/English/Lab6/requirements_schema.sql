-- Requirements Management Database Schema
-- ISO/IEC/IEEE 29148:2011 Compliant Requirements Management System
-- SQLite Database Schema

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Requirements table
CREATE TABLE IF NOT EXISTS requirements (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('functional', 'non-functional', 'business', 'technical', 'security', 'usability', 'compliance', 'process', 'documentation', 'testing')),
    priority TEXT NOT NULL CHECK (priority IN ('low', 'medium', 'high', 'critical')),
    status TEXT NOT NULL CHECK (status IN ('draft', 'review', 'approved', 'implemented', 'rejected', 'deprecated')),
    version INTEGER NOT NULL DEFAULT 1,
    created_by TEXT NOT NULL,
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by TEXT,
    updated_date DATETIME,
    tags TEXT, -- JSON array of tags
    metadata TEXT, -- JSON object with additional metadata
    parent_id TEXT, -- For hierarchical requirements
    FOREIGN KEY (parent_id) REFERENCES requirements(id) ON DELETE CASCADE
);

-- Changes table for change management
CREATE TABLE IF NOT EXISTS changes (
    id TEXT PRIMARY KEY,
    requirement_id TEXT NOT NULL,
    change_type TEXT NOT NULL CHECK (change_type IN ('enhancement', 'modification', 'correction', 'deletion', 'addition')),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    impact_analysis TEXT,
    requested_by TEXT NOT NULL,
    approved_by TEXT,
    approved_date DATETIME,
    status TEXT NOT NULL CHECK (status IN ('pending', 'approved', 'rejected', 'implemented')),
    priority TEXT NOT NULL CHECK (priority IN ('low', 'medium', 'high', 'critical')),
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    implemented_date DATETIME,
    metadata TEXT, -- JSON object with additional metadata
    FOREIGN KEY (requirement_id) REFERENCES requirements(id) ON DELETE CASCADE
);

-- Traceability matrix table
CREATE TABLE IF NOT EXISTS traceability (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT NOT NULL,
    target_id TEXT NOT NULL,
    relationship_type TEXT NOT NULL CHECK (relationship_type IN ('derives', 'implements', 'verifies', 'tests', 'supports', 'complements', 'requires', 'relates_to')),
    description TEXT,
    created_by TEXT NOT NULL,
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    strength TEXT CHECK (strength IN ('weak', 'medium', 'strong')),
    bidirectional BOOLEAN NOT NULL DEFAULT 1,
    FOREIGN KEY (source_id) REFERENCES requirements(id) ON DELETE CASCADE,
    FOREIGN KEY (target_id) REFERENCES requirements(id) ON DELETE CASCADE
);

-- Stakeholders table
CREATE TABLE IF NOT EXISTS stakeholders (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL CHECK (role IN ('administrator', 'analyst', 'designer', 'specialist', 'contributor', 'reviewer')),
    department TEXT,
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    permissions TEXT -- JSON array of permissions
);

-- Audit log table for compliance
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    record_id TEXT NOT NULL,
    action TEXT NOT NULL CHECK (action IN ('CREATE', 'UPDATE', 'DELETE')),
    old_values TEXT, -- JSON object of old values (for UPDATE)
    new_values TEXT, -- JSON object of new values (for CREATE/UPDATE)
    user_id TEXT NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ip_address TEXT,
    user_agent TEXT,
    session_id TEXT,
    FOREIGN KEY (user_id) REFERENCES stakeholders(id)
);

-- Requirements versions table for version control
CREATE TABLE IF NOT EXISTS requirement_versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requirement_id TEXT NOT NULL,
    version INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    type TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    tags TEXT,
    metadata TEXT,
    created_by TEXT NOT NULL,
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    change_reason TEXT,
    FOREIGN KEY (requirement_id) REFERENCES requirements(id) ON DELETE CASCADE
);

-- Attachments table for requirement documentation
CREATE TABLE IF NOT EXISTS attachments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requirement_id TEXT NOT NULL,
    filename TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_type TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    uploaded_by TEXT NOT NULL,
    uploaded_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (requirement_id) REFERENCES requirements(id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES stakeholders(id)
);

-- Comments table for requirement discussions
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requirement_id TEXT NOT NULL,
    comment_text TEXT NOT NULL,
    created_by TEXT NOT NULL,
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    parent_comment_id INTEGER, -- For threaded comments
    is_resolved BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (requirement_id) REFERENCES requirements(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES stakeholders(id),
    FOREIGN KEY (parent_comment_id) REFERENCES comments(id) ON DELETE CASCADE
);

-- Baselines table for requirement baselines
CREATE TABLE IF NOT EXISTS baselines (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_by TEXT NOT NULL,
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_locked BOOLEAN NOT NULL DEFAULT 0,
    locked_date DATETIME,
    locked_by TEXT,
    FOREIGN KEY (created_by) REFERENCES stakeholders(id),
    FOREIGN KEY (locked_by) REFERENCES stakeholders(id)
);

-- Baseline requirements junction table
CREATE TABLE IF NOT EXISTS baseline_requirements (
    baseline_id TEXT NOT NULL,
    requirement_id TEXT NOT NULL,
    requirement_version INTEGER NOT NULL,
    added_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (baseline_id, requirement_id),
    FOREIGN KEY (baseline_id) REFERENCES baselines(id) ON DELETE CASCADE,
    FOREIGN KEY (requirement_id) REFERENCES requirements(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_requirements_type ON requirements(type);
CREATE INDEX IF NOT EXISTS idx_requirements_status ON requirements(status);
CREATE INDEX IF NOT EXISTS idx_requirements_priority ON requirements(priority);
CREATE INDEX IF NOT EXISTS idx_requirements_created_by ON requirements(created_by);
CREATE INDEX IF NOT EXISTS idx_requirements_updated_date ON requirements(updated_date);

CREATE INDEX IF NOT EXISTS idx_changes_requirement_id ON changes(requirement_id);
CREATE INDEX IF NOT EXISTS idx_changes_status ON changes(status);
CREATE INDEX IF NOT EXISTS idx_changes_priority ON changes(priority);
CREATE INDEX IF NOT EXISTS idx_changes_created_date ON changes(created_date);

CREATE INDEX IF NOT EXISTS idx_traceability_source ON traceability(source_id);
CREATE INDEX IF NOT EXISTS idx_traceability_target ON traceability(target_id);
CREATE INDEX IF NOT EXISTS idx_traceability_type ON traceability(relationship_type);

CREATE INDEX IF NOT EXISTS idx_audit_log_table ON audit_log(table_name);
CREATE INDEX IF NOT EXISTS idx_audit_log_record ON audit_log(record_id);
CREATE INDEX IF NOT EXISTS idx_audit_log_user ON audit_log(user_id);
CREATE INDEX IF NOT EXISTS idx_audit_log_timestamp ON audit_log(timestamp);

CREATE INDEX IF NOT EXISTS idx_requirement_versions_req_id ON requirement_versions(requirement_id);
CREATE INDEX IF NOT EXISTS idx_requirement_versions_version ON requirement_versions(version);

CREATE INDEX IF NOT EXISTS idx_attachments_requirement ON attachments(requirement_id);
CREATE INDEX IF NOT EXISTS idx_comments_requirement ON comments(requirement_id);
CREATE INDEX IF NOT EXISTS idx_comments_parent ON comments(parent_comment_id);

-- Create triggers for audit logging
CREATE TRIGGER IF NOT EXISTS audit_requirements_insert
    AFTER INSERT ON requirements
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, new_values, user_id, timestamp)
    VALUES ('requirements', NEW.id, 'CREATE', json_object(
        'id', NEW.id,
        'title', NEW.title,
        'description', NEW.description,
        'type', NEW.type,
        'priority', NEW.priority,
        'status', NEW.status,
        'version', NEW.version,
        'created_by', NEW.created_by,
        'created_date', NEW.created_date
    ), NEW.created_by, datetime('now'));
END;

CREATE TRIGGER IF NOT EXISTS audit_requirements_update
    AFTER UPDATE ON requirements
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, old_values, new_values, user_id, timestamp)
    VALUES ('requirements', NEW.id, 'UPDATE', json_object(
        'title', OLD.title,
        'description', OLD.description,
        'type', OLD.type,
        'priority', OLD.priority,
        'status', OLD.status,
        'version', OLD.version,
        'updated_by', OLD.updated_by,
        'updated_date', OLD.updated_date
    ), json_object(
        'title', NEW.title,
        'description', NEW.description,
        'type', NEW.type,
        'priority', NEW.priority,
        'status', NEW.status,
        'version', NEW.version,
        'updated_by', NEW.updated_by,
        'updated_date', NEW.updated_date
    ), COALESCE(NEW.updated_by, 'system'), datetime('now'));
END;

CREATE TRIGGER IF NOT EXISTS audit_changes_insert
    AFTER INSERT ON changes
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, new_values, user_id, timestamp)
    VALUES ('changes', NEW.id, 'CREATE', json_object(
        'id', NEW.id,
        'requirement_id', NEW.requirement_id,
        'change_type', NEW.change_type,
        'title', NEW.title,
        'description', NEW.description,
        'requested_by', NEW.requested_by,
        'status', NEW.status,
        'priority', NEW.priority,
        'created_date', NEW.created_date
    ), NEW.requested_by, datetime('now'));
END;

-- Insert sample data
INSERT OR IGNORE INTO stakeholders (id, name, email, role, department) VALUES
('admin', 'System Administrator', 'admin@company.com', 'administrator', 'IT'),
('analyst1', 'Business Analyst', 'analyst@company.com', 'analyst', 'Business'),
('developer1', 'Software Developer', 'developer@company.com', 'specialist', 'IT'),
('tester1', 'QA Tester', 'tester@company.com', 'reviewer', 'QA');

-- Insert sample requirements
INSERT OR IGNORE INTO requirements (id, title, description, type, priority, status, version, created_by, tags, metadata) VALUES
('REQ-001', 'User Authentication', 'System shall provide secure user authentication', 'security', 'high', 'approved', 1, 'admin', '["security", "authentication"]', '{"estimated_effort": "2 weeks", "business_value": "critical"}'),
('REQ-002', 'Database Design', 'Design normalized database schema', 'technical', 'high', 'approved', 1, 'developer1', '["database", "schema"]', '{"database_type": "SQLite", "tables_count": 8}'),
('REQ-003', 'API Documentation', 'Create comprehensive API documentation', 'documentation', 'medium', 'draft', 1, 'analyst1', '["api", "documentation"]', '{"format": "OpenAPI 3.0", "endpoints_count": 15}');

-- Insert sample traceability
INSERT OR IGNORE INTO traceability (source_id, target_id, relationship_type, description, created_by, strength) VALUES
('REQ-001', 'REQ-002', 'implements', 'Authentication system uses database', 'developer1', 'strong'),
('REQ-002', 'REQ-003', 'supports', 'Database design supports API documentation', 'analyst1', 'medium');
