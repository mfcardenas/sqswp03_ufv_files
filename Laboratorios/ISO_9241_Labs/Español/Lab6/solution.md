# Laboratorio 6: Diseño de Interacción

## Solución

### Paso 1: HTML de Aplicación Interactiva
Crear un archivo `interactive_app.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo de Diseño Interactivo - Laboratorio ISO 9241</title>
    <link rel="stylesheet" href="interaction.css">
</head>
<body>
    <header>
        <h1>Principios de Diseño Interactivo</h1>
        <nav>
            <button id="undoBtn" disabled>Deshacer</button>
            <button id="redoBtn" disabled>Rehacer</button>
            <button id="resetBtn">Reiniciar</button>
            <button id="helpBtn">Ayuda</button>
        </nav>
    </header>

    <main>
        <section class="gesture-area">
            <h2>Navegación Basada en Gestos</h2>
            <div id="gestureCanvas" tabindex="0" aria-label="Área de interacción de gestos">
                <p>Usa gestos de mouse o táctiles para interactuar:</p>
                <ul>
                    <li>Deslizar izquierda/derecha para navegar</li>
                    <li>Pellizcar para hacer zoom</li>
                    <li>Doble clic para reiniciar</li>
                </ul>
            </div>
            <div id="gestureFeedback"></div>
        </section>

        <section class="drag-drop-area">
            <h2>Interfaz de Arrastrar y Soltar</h2>
            <div class="container">
                <div class="source-area">
                    <h3>Elementos Fuente</h3>
                    <div class="item" draggable="true" data-type="text">Bloque de Texto</div>
                    <div class="item" draggable="true" data-type="image">Marcador de Imagen</div>
                    <div class="item" draggable="true" data-type="button">Elemento Botón</div>
                    <div class="item" draggable="true" data-type="input">Campo de Entrada</div>
                </div>
                
                <div class="drop-area" id="dropZone">
                    <h3>Zona de Destino</h3>
                    <p>Arrastra elementos aquí para construir tu interfaz</p>
                </div>
            </div>
        </section>

        <section class="context-help">
            <h2>Ayuda Sensible al Contexto</h2>
            <div class="interactive-element" data-help="Este es un elemento interactivo de muestra. Pasa el mouse o enfócate para obtener ayuda.">
                Elemento de Muestra
            </div>
            <div id="helpTooltip" class="tooltip" role="tooltip" aria-hidden="true"></div>
        </section>

        <section class="pattern-demo">
            <h2>Patrones de Interacción Consistentes</h2>
            <div class="pattern-grid">
                <div class="pattern-card">
                    <h4>Título de Tarjeta</h4>
                    <p>Contenido de tarjeta con estilo consistente.</p>
                    <button class="action-btn">Acción</button>
                </div>
                <div class="pattern-card">
                    <h4>Otra Tarjeta</h4>
                    <p>Más contenido siguiendo el mismo patrón.</p>
                    <button class="action-btn">Acción</button>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite" aria-atomic="true"></div>
    
    <script src="interaction.js"></script>
</body>
</html>
```

### Paso 2: CSS para Diseño Interactivo
Crear un archivo `interaction.css`:

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

/* Área de Gestos */
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

/* Arrastrar y Soltar */
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

/* Ayuda de Contexto */
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

/* Demo de Patrón */
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

/* Notificación */
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

/* Estados de foco e interacción */
*:focus {
    outline: 2px solid #007bff;
    outline-offset: 2px;
}

.item:focus {
    outline: 2px solid #fff;
}

/* Diseño responsivo */
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

### Paso 3: JavaScript para Interacciones Avanzadas
Crear un archivo `interaction.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Funcionalidad de deshacer/rehacer
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
    
    // Reconocimiento de gestos
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
        gestureFeedback.textContent = 'Gesto iniciado...';
    }
    
    function moveGesture(e) {
        if (!isDragging) return;
        e.preventDefault();
        const point = getPoint(e);
        const deltaX = point.x - startX;
        const deltaY = point.y - startY;
        
        if (Math.abs(deltaX) > 50) {
            gestureFeedback.textContent = deltaX > 0 ? 'Deslizando a la derecha' : 'Deslizando a la izquierda';
        } else if (Math.abs(deltaY) > 50) {
            gestureFeedback.textContent = deltaY > 0 ? 'Deslizando hacia abajo' : 'Deslizando hacia arriba';
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
            showNotification(deltaX > 0 ? 'Navegado a la siguiente sección' : 'Navegado a la sección anterior');
        } else if (Math.abs(deltaY) > 100) {
            showNotification(deltaY > 0 ? 'Desplazado hacia abajo' : 'Desplazado hacia arriba');
        } else {
            gestureFeedback.textContent = 'Toque o clic detectado';
        }
    }
    
    function getPoint(e) {
        if (e.touches) {
            return { x: e.touches[0].clientX, y: e.touches[0].clientY };
        }
        return { x: e.clientX, y: e.clientY };
    }
    
    // Gesto de doble clic
    gestureCanvas.addEventListener('dblclick', function() {
        gestureFeedback.textContent = 'Doble clic detectado - reiniciando vista';
        showNotification('Vista reiniciada');
    });
    
    // Funcionalidad de arrastrar y soltar
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
            
            // Agregar botón de remover
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
            
            showNotification(`Agregado ${draggedItem.textContent} a la interfaz`);
        }
    });
    
    // Ayuda sensible al contexto
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
    
    // Event listeners de botones
    document.getElementById('undoBtn').addEventListener('click', undo);
    document.getElementById('redoBtn').addEventListener('click', redo);
    document.getElementById('resetBtn').addEventListener('click', function() {
        location.reload();
    });
    document.getElementById('helpBtn').addEventListener('click', function() {
        showNotification('¡Usa gestos, arrastra y suelta, y explora los elementos interactivos!');
    });
    
    // Sistema de notificaciones
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
    
    // Atajos de teclado
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
    
    // Inicializar
    updateUndoRedoButtons();
});
```

### Paso 4: Script de Análisis de Interacción en Python
Crear un archivo `interaction_analysis.py`:

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
        print("Sesión de análisis de interacción iniciada")
    
    def end_session(self):
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds()
        print(f"Sesión terminada. Duración: {duration:.2f} segundos")
        self.analyze_interactions()
    
    def log_interaction(self, interaction_type, details=None):
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'type': interaction_type,
            'details': details or {}
        }
        self.interactions.append(interaction)
        print(f"Registrada interacción {interaction_type}")
    
    def analyze_interactions(self):
        if not self.interactions:
            print("No hay interacciones para analizar")
            return
        
        # Estadísticas básicas
        total_interactions = len(self.interactions)
        interaction_types = defaultdict(int)
        interaction_sequence = []
        
        for interaction in self.interactions:
            interaction_types[interaction['type']] += 1
            interaction_sequence.append(interaction['type'])
        
        # Análisis basado en tiempo
        if len(self.interactions) > 1:
            start_time = datetime.fromisoformat(self.interactions[0]['timestamp'])
            end_time = datetime.fromisoformat(self.interactions[-1]['timestamp'])
            total_duration = (end_time - start_time).total_seconds()
            avg_interaction_rate = total_interactions / total_duration if total_duration > 0 else 0
        else:
            avg_interaction_rate = 0
        
        # Análisis de patrones
        gesture_sequence = [i for i in interaction_sequence if 'gesture' in i.lower()]
        drag_drop_sequence = [i for i in interaction_sequence if 'drag' in i.lower() or 'drop' in i.lower()]
        
        # Generar reporte
        self.generate_report({
            'total_interactions': total_interactions,
            'interaction_types': dict(interaction_types),
            'avg_interaction_rate': avg_interaction_rate,
            'gesture_count': len(gesture_sequence),
            'drag_drop_count': len(drag_drop_sequence),
            'interaction_sequence': interaction_sequence
        })
    
    def generate_report(self, stats):
        print("\n=== Reporte de Análisis de Interacción ===")
        print(f"Total de Interacciones: {stats['total_interactions']}")
        print(f"Tasa Promedio de Interacción: {stats['avg_interaction_rate']:.2f} por segundo")
        print(f"Interacciones de Gestos: {stats['gesture_count']}")
        print(f"Interacciones de Arrastrar y Soltar: {stats['drag_drop_count']}")
        
        print("\nTipos de Interacción:")
        for interaction_type, count in stats['interaction_types'].items():
            print(f"  {interaction_type}: {count}")
        
        print("\nSecuencia de Interacción:")
        for i, interaction in enumerate(stats['interaction_sequence'][:20]):  # Mostrar primeras 20
            print(f"  {i+1}. {interaction}")
        
        if len(stats['interaction_sequence']) > 20:
            print(f"  ... y {len(stats['interaction_sequence']) - 20} más")
        
        # Perspectivas de usabilidad
        print("\n=== Perspectivas de Usabilidad ===")
        if stats['gesture_count'] > stats['total_interactions'] * 0.3:
            print("✅ Buen uso de interacciones basadas en gestos")
        else:
            print("⚠️  Uso limitado de gestos - considera fomentar más interacciones de gestos")
        
        if stats['drag_drop_count'] > 0:
            print("✅ La funcionalidad de arrastrar y soltar está siendo usada")
        else:
            print("⚠️  No se detectaron interacciones de arrastrar y soltar")
        
        if stats['avg_interaction_rate'] > 0.5:
            print("✅ Alta tasa de interacción indica usuarios comprometidos")
        else:
            print("ℹ️  Tasa moderada de interacción - los usuarios pueden necesitar más guía")
        
        # Guardar datos detallados
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
        
        print("\nAnálisis detallado guardado en interaction_analysis.json")

# Ejemplo de uso y simulación
if __name__ == "__main__":
    analyzer = InteractionAnalyzer()
    analyzer.start_session()
    
    # Simular algunas interacciones
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
        time.sleep(0.5)  # Simular tiempo entre interacciones
    
    analyzer.end_session()
```

### Paso 5: Documentación
Esta aplicación interactiva demuestra principios clave de diseño de interacción del ISO 9241-110:

1. **Adecuación para la tarea**: Las interacciones coinciden con objetivos y contexto del usuario
2. **Autodescriptividad**: Afordancias claras y retroalimentación
3. **Controlabilidad**: Funcionalidad de deshacer/rehacer y control del usuario
4. **Conformidad con expectativas del usuario**: Patrones consistentes
5. **Tolerancia a errores**: Manejo de errores elegante
6. **Adecuación para individualización**: Interacciones personalizables
7. **Adecuación para aprendizaje**: Características intuitivas y descubribles

Características clave implementadas:
- Navegación basada en gestos con retroalimentación visual
- Interfaz de arrastrar y soltar con gestión de estado
- Sistema de ayuda sensible al contexto
- Funcionalidad de deshacer/rehacer para interacciones complejas
- Patrones de interacción consistentes en toda la aplicación
- Accesibilidad por teclado y atajos

El script en Python analiza patrones de interacción del usuario para proporcionar perspectivas sobre usabilidad y métricas de compromiso.
