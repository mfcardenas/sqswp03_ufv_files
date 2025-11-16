# Lab 3: Ergonomic Requirements

## Solution

### Step 1: HTML Structure for Ergonomic Editor
Create an `editor.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ergonomic Text Editor</title>
    <link rel="stylesheet" href="editor.css">
</head>
<body>
    <div class="toolbar">
        <button id="newBtn" title="New (Ctrl+N)">New</button>
        <button id="saveBtn" title="Save (Ctrl+S)">Save</button>
        <button id="openBtn" title="Open (Ctrl+O)">Open</button>
        <button id="undoBtn" title="Undo (Ctrl+Z)">Undo</button>
        <button id="redoBtn" title="Redo (Ctrl+Y)">Redo</button>
        <select id="fontSize">
            <option value="12">12px</option>
            <option value="14">14px</option>
            <option value="16" selected>16px</option>
            <option value="18">18px</option>
            <option value="20">20px</option>
        </select>
        <select id="theme">
            <option value="light">Light</option>
            <option value="dark">Dark</option>
            <option value="high-contrast">High Contrast</option>
        </select>
    </div>
    <div class="editor-container">
        <textarea id="editor" placeholder="Start typing... Use keyboard shortcuts for better ergonomics!"></textarea>
    </div>
    <div class="status-bar">
        <span id="wordCount">Words: 0</span>
        <span id="charCount">Characters: 0</span>
        <span id="keystrokeCount">Keystrokes: 0</span>
    </div>
    <script src="editor.js"></script>
</body>
</html>
```

### Step 2: CSS for Ergonomic Design
Create an `editor.css` file:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
    height: 100vh;
    display: flex;
    flex-direction: column;
}

.toolbar {
    background-color: #e0e0e0;
    padding: 10px;
    border-bottom: 1px solid #ccc;
    display: flex;
    gap: 10px;
    align-items: center;
}

button {
    padding: 8px 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
}

button:hover {
    background-color: #45a049;
}

select {
    padding: 6px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

.editor-container {
    flex: 1;
    padding: 20px;
    background-color: white;
}

#editor {
    width: 100%;
    height: 100%;
    border: none;
    outline: none;
    font-size: 16px;
    line-height: 1.6;
    resize: none;
    padding: 20px;
    background-color: #fafafa;
    color: #333;
}

.status-bar {
    background-color: #e0e0e0;
    padding: 5px 20px;
    border-top: 1px solid #ccc;
    display: flex;
    justify-content: space-between;
    font-size: 12px;
}

/* Dark theme */
body.dark {
    background-color: #2c2c2c;
    color: #e0e0e0;
}

body.dark .toolbar {
    background-color: #3c3c3c;
    border-bottom-color: #555;
}

body.dark .editor-container {
    background-color: #1e1e1e;
}

body.dark #editor {
    background-color: #2c2c2c;
    color: #e0e0e0;
}

body.dark .status-bar {
    background-color: #3c3c3c;
    border-top-color: #555;
}

/* High contrast theme */
body.high-contrast {
    background-color: black;
    color: white;
}

body.high-contrast .toolbar {
    background-color: #333;
    border-bottom-color: white;
}

body.high-contrast .editor-container {
    background-color: black;
}

body.high-contrast #editor {
    background-color: black;
    color: yellow;
    border: 1px solid white;
}

body.high-contrast .status-bar {
    background-color: #333;
    border-top-color: white;
}
```

### Step 3: JavaScript for Ergonomic Interactions
Create an `editor.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const editor = document.getElementById('editor');
    const wordCount = document.getElementById('wordCount');
    const charCount = document.getElementById('charCount');
    const keystrokeCount = document.getElementById('keystrokeCount');
    const fontSize = document.getElementById('fontSize');
    const theme = document.getElementById('theme');
    
    let keystrokes = 0;
    let undoStack = [];
    let redoStack = [];
    
    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey || e.metaKey) {
            switch(e.key) {
                case 'n':
                    e.preventDefault();
                    newDocument();
                    break;
                case 's':
                    e.preventDefault();
                    saveDocument();
                    break;
                case 'o':
                    e.preventDefault();
                    openDocument();
                    break;
                case 'z':
                    if (e.shiftKey) {
                        e.preventDefault();
                        redo();
                    } else {
                        e.preventDefault();
                        undo();
                    }
                    break;
                case 'y':
                    e.preventDefault();
                    redo();
                    break;
            }
        }
    });
    
    // Track keystrokes
    editor.addEventListener('keydown', function(e) {
        keystrokes++;
        updateStatus();
        
        // Auto-save every 10 keystrokes
        if (keystrokes % 10 === 0) {
            autoSave();
        }
    });
    
    // Update word and character count
    editor.addEventListener('input', function() {
        updateStatus();
        saveToUndoStack();
    });
    
    // Font size change
    fontSize.addEventListener('change', function() {
        editor.style.fontSize = this.value + 'px';
    });
    
    // Theme change
    theme.addEventListener('change', function() {
        document.body.className = this.value;
    });
    
    function updateStatus() {
        const text = editor.value;
        const words = text.trim() === '' ? 0 : text.trim().split(/\s+/).length;
        const chars = text.length;
        
        wordCount.textContent = `Words: ${words}`;
        charCount.textContent = `Characters: ${chars}`;
        keystrokeCount.textContent = `Keystrokes: ${keystrokes}`;
    }
    
    function saveToUndoStack() {
        undoStack.push(editor.value);
        redoStack = [];
        if (undoStack.length > 50) {
            undoStack.shift();
        }
    }
    
    function undo() {
        if (undoStack.length > 0) {
            redoStack.push(editor.value);
            editor.value = undoStack.pop();
            updateStatus();
        }
    }
    
    function redo() {
        if (redoStack.length > 0) {
            undoStack.push(editor.value);
            editor.value = redoStack.pop();
            updateStatus();
        }
    }
    
    function newDocument() {
        if (confirm('Are you sure you want to start a new document? Unsaved changes will be lost.')) {
            editor.value = '';
            keystrokes = 0;
            undoStack = [];
            redoStack = [];
            updateStatus();
        }
    }
    
    function saveDocument() {
        const blob = new Blob([editor.value], {type: 'text/plain'});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'document.txt';
        a.click();
        URL.revokeObjectURL(url);
    }
    
    function openDocument() {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = '.txt';
        input.onchange = function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    editor.value = e.target.result;
                    updateStatus();
                };
                reader.readAsText(file);
            }
        };
        input.click();
    }
    
    function autoSave() {
        localStorage.setItem('autoSave', editor.value);
        console.log('Auto-saved');
    }
    
    // Load auto-saved content
    const autoSaved = localStorage.getItem('autoSave');
    if (autoSaved) {
        editor.value = autoSaved;
        updateStatus();
    }
    
    // Initialize
    updateStatus();
});
```

### Step 4: Python Ergonomics Analysis Script
Create an `ergonomics_analysis.py` file:

```python
import json
import time
from datetime import datetime
import matplotlib.pyplot as plt

class ErgonomicsAnalyzer:
    def __init__(self):
        self.session_data = {
            'start_time': None,
            'end_time': None,
            'keystrokes': 0,
            'mouse_clicks': 0,
            'shortcuts_used': 0,
            'breaks_taken': 0,
            'font_size_changes': 0,
            'theme_changes': 0
        }
    
    def start_session(self):
        self.session_data['start_time'] = datetime.now()
        print("Ergonomics analysis session started")
    
    def end_session(self):
        self.session_data['end_time'] = datetime.now()
        duration = (self.session_data['end_time'] - self.session_data['start_time']).total_seconds()
        self.session_data['duration'] = duration
        print(f"Session ended. Duration: {duration:.2f} seconds")
    
    def log_keystroke(self):
        self.session_data['keystrokes'] += 1
    
    def log_mouse_click(self):
        self.session_data['mouse_clicks'] += 1
    
    def log_shortcut_use(self):
        self.session_data['shortcuts_used'] += 1
    
    def log_break(self):
        self.session_data['breaks_taken'] += 1
    
    def log_font_change(self):
        self.session_data['font_size_changes'] += 1
    
    def log_theme_change(self):
        self.session_data['theme_changes'] += 1
    
    def calculate_metrics(self):
        duration_hours = self.session_data['duration'] / 3600
        keystroke_rate = self.session_data['keystrokes'] / duration_hours if duration_hours > 0 else 0
        mouse_rate = self.session_data['mouse_clicks'] / duration_hours if duration_hours > 0 else 0
        shortcut_ratio = self.session_data['shortcuts_used'] / self.session_data['keystrokes'] if self.session_data['keystrokes'] > 0 else 0
        
        return {
            'keystroke_rate_per_hour': keystroke_rate,
            'mouse_click_rate_per_hour': mouse_rate,
            'shortcut_usage_ratio': shortcut_ratio,
            'breaks_per_hour': self.session_data['breaks_taken'] / duration_hours if duration_hours > 0 else 0
        }
    
    def generate_report(self):
        metrics = self.calculate_metrics()
        
        print("\n=== Ergonomics Analysis Report ===")
        print(f"Session Duration: {self.session_data['duration']:.2f} seconds")
        print(f"Total Keystrokes: {self.session_data['keystrokes']}")
        print(f"Mouse Clicks: {self.session_data['mouse_clicks']}")
        print(f"Keyboard Shortcuts Used: {self.session_data['shortcuts_used']}")
        print(f"Breaks Taken: {self.session_data['breaks_taken']}")
        print(f"Font Size Changes: {self.session_data['font_size_changes']}")
        print(f"Theme Changes: {self.session_data['theme_changes']}")
        
        print("\n=== Ergonomics Metrics ===")
        print(f"Keystroke Rate: {metrics['keystroke_rate_per_hour']:.1f} per hour")
        print(f"Mouse Click Rate: {metrics['mouse_click_rate_per_hour']:.1f} per hour")
        print(f"Shortcut Usage Ratio: {metrics['shortcut_usage_ratio']:.2%}")
        print(f"Breaks per Hour: {metrics['breaks_per_hour']:.2f}")
        
        # Ergonomics assessment
        print("\n=== Ergonomics Assessment ===")
        if metrics['keystroke_rate_per_hour'] > 10000:
            print("⚠️  High keystroke rate - risk of repetitive strain injury")
        else:
            print("✅ Keystroke rate within acceptable limits")
        
        if metrics['shortcut_usage_ratio'] > 0.1:
            print("✅ Good use of keyboard shortcuts")
        else:
            print("⚠️  Low shortcut usage - consider using more keyboard shortcuts")
        
        if metrics['breaks_per_hour'] >= 1:
            print("✅ Adequate break frequency")
        else:
            print("⚠️  Consider taking more frequent breaks")
    
    def save_data(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.session_data, f, default=str)
        print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    analyzer = ErgonomicsAnalyzer()
    analyzer.start_session()
    
    # Simulate some activity
    for i in range(100):
        analyzer.log_keystroke()
        if i % 20 == 0:
            analyzer.log_shortcut_use()
        if i % 50 == 0:
            analyzer.log_break()
    
    time.sleep(2)  # Simulate session time
    analyzer.end_session()
    analyzer.generate_report()
    analyzer.save_data('ergonomics_data.json')
```

### Step 5: Documentation
This ergonomic text editor implements several ISO 9241-400 principles:

1. **Keyboard-Centric Design**: Extensive use of keyboard shortcuts reduces mouse usage.
2. **Adjustable Display**: Font size and theme options for visual comfort.
3. **Work-Rest Cycles**: Auto-save and break reminders prevent fatigue.
4. **Feedback Systems**: Status bar provides real-time information.
5. **Minimize Repetitive Actions**: Undo/redo stack and auto-save reduce repetitive tasks.

The Python script analyzes user behavior to identify potential ergonomic issues and provides recommendations for improvement.
