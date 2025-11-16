# Lab 6: Interaction Design

## Solution

### Step 1: Interactive Application HTML
Create an `interactive_app.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Design Demo - ISO 9241 Lab</title>
    <link rel="stylesheet" href="interaction.css">
</head>
<body>
    <header>
        <h1>Interactive Design Principles</h1>
        <nav>
            <button id="undoBtn" disabled>Undo</button>
            <button id="redoBtn" disabled>Redo</button>
            <button id="resetBtn">Reset</button>
            <button id="helpBtn">Help</button>
        </nav>
    </header>

    <main>
        <section class="gesture-area">
            <h2>Gesture-Based Navigation</h2>
            <div id="gestureCanvas" tabindex="0" aria-label="Gesture interaction area">
                <p>Use mouse or touch gestures to interact:</p>
                <ul>
                    <li>Swipe left/right to navigate</li>
                    <li>Pinch to zoom</li>
                    <li>Double-click to reset</li>
                </ul>
            </div>
            <div id="gestureFeedback"></div>
        </section>

        <section class="drag-drop-area">
            <h2>Drag and Drop Interface</h2>
            <div class="container">
                <div class="source-area">
                    <h3>Source Items</h3>
                    <div class="item" draggable="true" data-type="text">Text Block</div>
                    <div class="item" draggable="true" data-type="image">Image Placeholder</div>
                    <div class="item" draggable="true" data-type="button">Button Element</div>
                    <div class="item" draggable="true" data-type="input">Input Field</div>
                </div>
                
                <div class="drop-area" id="dropZone">
                    <h3>Drop Zone</h3>
                    <p>Drag items here to build your interface</p>
                </div>
            </div>
        </section>

        <section class="context-help">
            <h2>Context-Aware Help</h2>
            <div class="interactive-element" data-help="This is a sample interactive element. Hover or focus for help.">
                Sample Element
            </div>
            <div id="helpTooltip" class="tooltip" role="tooltip" aria-hidden="true"></div>
        </section>

        <section class="pattern-demo">
            <h2>Consistent Interaction Patterns</h2>
            <div class="pattern-grid">
                <div class="pattern-card">
                    <h4>Card Title</h4>
                    <p>Card content with consistent styling.</p>
                    <button class="action-btn">Action</button>
                </div>
                <div class="pattern-card">
                    <h4>Another Card</h4>
                    <p>More content following the same pattern.</p>
                    <button class="action-btn">Action</button>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite" aria-atomic="true"></div>
    
    <script src="interaction.js"></script>
</body>
</html>
```

### Step 2: CSS for Interactive Design
Create an `interaction.css` file:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
    color: #333;
}

header {
    background-color: #007bff;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    margin: 0;
}

nav button {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 0.5rem 1rem;
    margin-left: 0.5rem;
    border-radius: 4px;
    cursor: pointer;
}

nav button:hover, nav button:focus {
    background-color: rgba(255, 255, 255, 0.3);
}

nav button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

main {
    max-width: 1200px;
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
    color: #495057;
    border-bottom: 2px solid #007bff;
    padding-bottom: 0.5rem;
}

/* Gesture Area */
#gestureCanvas {
    width: 100%;
    height: 300px;
    border: 2px dashed #dee2e6;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #f8f9fa;
    cursor: grab;
    outline: none;
}

#gestureCanvas:active {
    cursor: grabbing;
}

#gestureFeedback {
    margin-top: 1rem;
    padding: 1rem;
    background-color: #e9ecef;
    border-radius: 4px;
    min-height: 2rem;
}

/* Drag and Drop */
.container {
    display: flex;
    gap: 2rem;
    margin-top: 1rem;
}

.source-area, .drop-area {
    flex: 1;
    padding: 1rem;
    border: 2px dashed #dee2e6;
    border-radius: 8px;
    min-height: 200px;
}

.source-area h3, .drop-area h3 {
    margin-top: 0;
    color: #495057;
}

.item {
    background-color: #007bff;
    color: white;
    padding: 0.75rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    cursor: grab;
    user-select: none;
}

.item:hover {
    background-color: #0056b3;
}

.item:active {
    cursor: grabbing;
}

.item.dragging {
    opacity: 0.5;
}

.drop-area.drag-over {
    background-color: #e9ecef;
    border-color: #007bff;
}

/* Context Help */
.interactive-element {
    background-color: #28a745;
    color: white;
    padding: 1rem;
    border-radius: 4px;
    cursor: pointer;
    display: inline-block;
    position: relative;
}

.tooltip {
    position: absolute;
    background-color: #333;
    color: white;
    padding: 0.5rem;
    border-radius: 4px;
    max-width: 300px;
    z-index: 1000;
    display: none;
}

.tooltip::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #333 transparent transparent transparent;
}

/* Pattern Demo */
.pattern-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.pattern-card {
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 1rem;
    background-color: #f8f9fa;
}

.pattern-card h4 {
    margin-top: 0;
    color: #007bff;
}

.action-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 0.5rem;
}

.action-btn:hover {
    background-color: #0056b3;
}

/* Notification */
.notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #007bff;
    color: white;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    display: none;
    max-width: 300px;
}

/* Focus and interaction states */
*:focus {
    outline: 2px solid #007bff;
    outline-offset: 2px;
}

.item:focus {
    outline: 2px solid #fff;
}

/* Responsive design */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    .container {
        flex-direction: column;
    }
    
    .pattern-grid {
        grid-template-columns: 1fr;
    }
}
```

### Step 3: JavaScript for Advanced Interactions
Create an `interaction.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Undo/Redo functionality
    let actionHistory = [];
    let historyIndex = -1;
    
    function executeAction(action) {
        action.execute();
        actionHistory = actionHistory.slice(0, historyIndex + 1);
        actionHistory.push(action);
        historyIndex++;
        updateUndoRedoButtons();
    }
    
    function undo() {
        if (historyIndex >= 0) {
            actionHistory[historyIndex].undo();
            historyIndex--;
            updateUndoRedoButtons();
        }
    }
    
    function redo() {
        if (historyIndex < actionHistory.length - 1) {
            historyIndex++;
            actionHistory[historyIndex].execute();
            updateUndoRedoButtons();
        }
    }
    
    function updateUndoRedoButtons() {
        document.getElementById('undoBtn').disabled = historyIndex < 0;
        document.getElementById('redoBtn').disabled = historyIndex >= actionHistory.length - 1;
    }
    
    // Gesture recognition
    const gestureCanvas = document.getElementById('gestureCanvas');
    const gestureFeedback = document.getElementById('gestureFeedback');
    let startX, startY, isDragging = false;
    
    gestureCanvas.addEventListener('mousedown', startGesture);
    gestureCanvas.addEventListener('touchstart', startGesture);
    document.addEventListener('mousemove', moveGesture);
    document.addEventListener('touchmove', moveGesture);
    document.addEventListener('mouseup', endGesture);
    document.addEventListener('touchend', endGesture);
    
    function startGesture(e) {
        e.preventDefault();
        const point = getPoint(e);
        startX = point.x;
        startY = point.y;
        isDragging = true;
        gestureFeedback.textContent = 'Gesture started...';
    }
    
    function moveGesture(e) {
        if (!isDragging) return;
        e.preventDefault();
        const point = getPoint(e);
        const deltaX = point.x - startX;
        const deltaY = point.y - startY;
        
        if (Math.abs(deltaX) > 50) {
            gestureFeedback.textContent = deltaX > 0 ? 'Swiping right' : 'Swiping left';
        } else if (Math.abs(deltaY) > 50) {
            gestureFeedback.textContent = deltaY > 0 ? 'Swiping down' : 'Swiping up';
        }
    }
    
    function endGesture(e) {
        if (!isDragging) return;
        e.preventDefault();
        isDragging = false;
        
        const point = getPoint(e);
        const deltaX = point.x - startX;
        const deltaY = point.y - startY;
        
        if (Math.abs(deltaX) > 100) {
            showNotification(deltaX > 0 ? 'Navigated to next section' : 'Navigated to previous section');
        } else if (Math.abs(deltaY) > 100) {
            showNotification(deltaY > 0 ? 'Scrolled down' : 'Scrolled up');
        } else {
            gestureFeedback.textContent = 'Tap or click detected';
        }
    }
    
    function getPoint(e) {
        if (e.touches) {
            return { x: e.touches[0].clientX, y: e.touches[0].clientY };
        }
        return { x: e.clientX, y: e.clientY };
    }
    
    // Double-click gesture
    gestureCanvas.addEventListener('dblclick', function() {
        gestureFeedback.textContent = 'Double-click detected - resetting view';
        showNotification('View reset');
    });
    
    // Drag and Drop functionality
    const items = document.querySelectorAll('.item');
    const dropZone = document.getElementById('dropZone');
    let draggedItem = null;
    
    items.forEach(item => {
        item.addEventListener('dragstart', function(e) {
            draggedItem = this;
            this.classList.add('dragging');
            e.dataTransfer.setData('text/html', this.outerHTML);
            e.dataTransfer.effectAllowed = 'copy';
        });
        
        item.addEventListener('dragend', function() {
            this.classList.remove('dragging');
        });
    });
    
    dropZone.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.classList.add('drag-over');
        e.dataTransfer.dropEffect = 'copy';
    });
    
    dropZone.addEventListener('dragleave', function() {
        this.classList.remove('drag-over');
    });
    
    dropZone.addEventListener('drop', function(e) {
        e.preventDefault();
        this.classList.remove('drag-over');
        
        if (draggedItem) {
            const newItem = draggedItem.cloneNode(true);
            newItem.draggable = false;
            newItem.classList.add('dropped-item');
            
            // Add remove button
            const removeBtn = document.createElement('button');
            removeBtn.textContent = '×';
            removeBtn.className = 'remove-btn';
            removeBtn.onclick = function() {
                newItem.remove();
                executeAction({
                    execute: () => {},
                    undo: () => dropZone.appendChild(newItem)
                });
            };
            newItem.appendChild(removeBtn);
            
            this.appendChild(newItem);
            
            executeAction({
                execute: () => dropZone.appendChild(newItem),
                undo: () => newItem.remove()
            });
            
            showNotification(`Added ${draggedItem.textContent} to the interface`);
        }
    });
    
    // Context-aware help
    const interactiveElement = document.querySelector('.interactive-element');
    const tooltip = document.getElementById('helpTooltip');
    
    function showTooltip() {
        const helpText = interactiveElement.dataset.help;
        tooltip.textContent = helpText;
        tooltip.style.display = 'block';
        tooltip.setAttribute('aria-hidden', 'false');
        
        const rect = interactiveElement.getBoundingClientRect();
        tooltip.style.left = rect.left + 'px';
        tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
    }
    
    function hideTooltip() {
        tooltip.style.display = 'none';
        tooltip.setAttribute('aria-hidden', 'true');
    }
    
    interactiveElement.addEventListener('mouseenter', showTooltip);
    interactiveElement.addEventListener('mouseleave', hideTooltip);
    interactiveElement.addEventListener('focus', showTooltip);
    interactiveElement.addEventListener('blur', hideTooltip);
    
    // Button event listeners
    document.getElementById('undoBtn').addEventListener('click', undo);
    document.getElementById('redoBtn').addEventListener('click', redo);
    document.getElementById('resetBtn').addEventListener('click', function() {
        location.reload();
    });
    document.getElementById('helpBtn').addEventListener('click', function() {
        showNotification('Use gestures, drag and drop, and explore the interactive elements!');
    });
    
    // Notification system
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
    
    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey || e.metaKey) {
            switch(e.key) {
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
    
    // Initialize
    updateUndoRedoButtons();
});
```

### Step 4: Python Interaction Analysis Script
Create an `interaction_analysis.py` file:

```python
import json
import time
from datetime import datetime
from collections import defaultdict

class InteractionAnalyzer:
    def __init__(self):
        self.interactions = []
        self.start_time = None
        self.end_time = None
    
    def start_session(self):
        self.start_time = datetime.now()
        print("Interaction analysis session started")
    
    def end_session(self):
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds()
        print(f"Session ended. Duration: {duration:.2f} seconds")
        self.analyze_interactions()
    
    def log_interaction(self, interaction_type, details=None):
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'type': interaction_type,
            'details': details or {}
        }
        self.interactions.append(interaction)
        print(f"Logged {interaction_type} interaction")
    
    def analyze_interactions(self):
        if not self.interactions:
            print("No interactions to analyze")
            return
        
        # Basic statistics
        total_interactions = len(self.interactions)
        interaction_types = defaultdict(int)
        interaction_sequence = []
        
        for interaction in self.interactions:
            interaction_types[interaction['type']] += 1
            interaction_sequence.append(interaction['type'])
        
        # Time-based analysis
        if len(self.interactions) > 1:
            start_time = datetime.fromisoformat(self.interactions[0]['timestamp'])
            end_time = datetime.fromisoformat(self.interactions[-1]['timestamp'])
            total_duration = (end_time - start_time).total_seconds()
            avg_interaction_rate = total_interactions / total_duration if total_duration > 0 else 0
        else:
            avg_interaction_rate = 0
        
        # Pattern analysis
        gesture_sequence = [i for i in interaction_sequence if 'gesture' in i.lower()]
        drag_drop_sequence = [i for i in interaction_sequence if 'drag' in i.lower() or 'drop' in i.lower()]
        
        # Generate report
        self.generate_report({
            'total_interactions': total_interactions,
            'interaction_types': dict(interaction_types),
            'avg_interaction_rate': avg_interaction_rate,
            'gesture_count': len(gesture_sequence),
            'drag_drop_count': len(drag_drop_sequence),
            'interaction_sequence': interaction_sequence
        })
    
    def generate_report(self, stats):
        print("\n=== Interaction Analysis Report ===")
        print(f"Total Interactions: {stats['total_interactions']}")
        print(f"Average Interaction Rate: {stats['avg_interaction_rate']:.2f} per second")
        print(f"Gesture Interactions: {stats['gesture_count']}")
        print(f"Drag & Drop Interactions: {stats['drag_drop_count']}")
        
        print("\nInteraction Types:")
        for interaction_type, count in stats['interaction_types'].items():
            print(f"  {interaction_type}: {count}")
        
        print("\nInteraction Sequence:")
        for i, interaction in enumerate(stats['interaction_sequence'][:20]):  # Show first 20
            print(f"  {i+1}. {interaction}")
        
        if len(stats['interaction_sequence']) > 20:
            print(f"  ... and {len(stats['interaction_sequence']) - 20} more")
        
        # Usability insights
        print("\n=== Usability Insights ===")
        if stats['gesture_count'] > stats['total_interactions'] * 0.3:
            print("✅ Good use of gesture-based interactions")
        else:
            print("⚠️  Limited gesture usage - consider encouraging more gesture interactions")
        
        if stats['drag_drop_count'] > 0:
            print("✅ Drag and drop functionality is being used")
        else:
            print("⚠️  No drag and drop interactions detected")
        
        if stats['avg_interaction_rate'] > 0.5:
            print("✅ High interaction rate indicates engaged users")
        else:
            print("ℹ️  Moderate interaction rate - users may need more guidance")
        
        # Save detailed data
        report_data = {
            'session_info': {
                'start_time': self.start_time.isoformat() if self.start_time else None,
                'end_time': self.end_time.isoformat() if self.end_time else None,
                'duration': (self.end_time - self.start_time).total_seconds() if self.start_time and self.end_time else 0
            },
            'statistics': stats,
            'interactions': self.interactions
        }
        
        with open('interaction_analysis.json', 'w') as f:
            json.dump(report_data, f, indent=2, default=str)
        
        print("\nDetailed analysis saved to interaction_analysis.json")

# Example usage and simulation
if __name__ == "__main__":
    analyzer = InteractionAnalyzer()
    analyzer.start_session()
    
    # Simulate some interactions
    interactions = [
        ('gesture_start', {'x': 100, 'y': 200}),
        ('gesture_move', {'deltaX': 50, 'deltaY': 0}),
        ('gesture_end', {'direction': 'right'}),
        ('drag_start', {'item': 'text_block'}),
        ('drag_end', {'dropped': True}),
        ('button_click', {'button': 'help'}),
        ('keyboard_shortcut', {'keys': 'Ctrl+Z'}),
    ]
    
    for interaction_type, details in interactions:
        analyzer.log_interaction(interaction_type, details)
        time.sleep(0.5)  # Simulate time between interactions
    
    analyzer.end_session()
```

### Step 5: Documentation
This interactive application demonstrates key interaction design principles from ISO 9241-110:

1. **Suitability for the task**: Interactions match user goals and context
2. **Self-descriptiveness**: Clear affordances and feedback
3. **Controllability**: Undo/redo functionality and user control
4. **Conformity with user expectations**: Consistent patterns
5. **Error tolerance**: Graceful error handling
6. **Suitability for individualization**: Customizable interactions
7. **Suitability for learning**: Intuitive and discoverable features

Key features implemented:
- Gesture-based navigation with visual feedback
- Drag-and-drop interface with state management
- Context-aware help system
- Undo/redo functionality for complex interactions
- Consistent interaction patterns across the application
- Keyboard accessibility and shortcuts

The Python script analyzes user interaction patterns to provide insights into usability and engagement metrics.
