# Laboratorio 7: Métodos de Evaluación

## Solución

### Paso 1: HTML del Marco de Evaluación de Usabilidad
Crear un archivo `usability_testing.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marco de Evaluación de Usabilidad - Laboratorio ISO 9241</title>
    <link rel="stylesheet" href="usability.css">
</head>
<body>
    <header>
        <h1>Marco de Evaluación de Usabilidad</h1>
        <nav>
            <button id="startTestBtn">Iniciar Nueva Prueba</button>
            <button id="heuristicBtn">Evaluación Heurística</button>
            <button id="accessibilityBtn">Verificación de Accesibilidad</button>
            <button id="generateReportBtn">Generar Reporte</button>
        </nav>
    </header>

    <main>
        <section class="test-setup">
            <h2>Configuración de Prueba</h2>
            <form id="testConfigForm">
                <div class="form-group">
                    <label for="testName">Nombre de Prueba:</label>
                    <input type="text" id="testName" required>
                </div>
                
                <div class="form-group">
                    <label for="evaluatorName">Nombre del Evaluador:</label>
                    <input type="text" id="evaluatorName" required>
                </div>
                
                <div class="form-group">
                    <label for="testType">Método de Evaluación:</label>
                    <select id="testType">
                        <option value="usability">Pruebas de Usabilidad</option>
                        <option value="heuristic">Evaluación Heurística</option>
                        <option value="cognitive">Caminata Cognitiva</option>
                        <option value="accessibility">Auditoría de Accesibilidad</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="participants">Número de Participantes:</label>
                    <input type="number" id="participants" min="1" max="20" value="5">
                </div>
                
                <button type="submit" class="primary-btn">Configurar Prueba</button>
            </form>
        </section>

        <section class="test-interface" id="testInterface" style="display: none;">
            <h2>Interfaz de Pruebas de Usabilidad</h2>
            
            <div class="test-controls">
                <button id="recordBtn" class="record-btn">Iniciar Grabación</button>
                <button id="pauseBtn" class="pause-btn" disabled>Pausar</button>
                <button id="stopBtn" class="stop-btn" disabled>Detener Prueba</button>
                <div id="timer">00:00:00</div>
            </div>
            
            <div class="test-area">
                <div class="task-panel">
                    <h3>Tarea Actual</h3>
                    <div id="currentTask">No se ha asignado tarea</div>
                    <div class="task-controls">
                        <button id="successBtn" class="success-btn" disabled>Éxito en Tarea</button>
                        <button id="failureBtn" class="failure-btn" disabled>Falla en Tarea</button>
                    </div>
                </div>
                
                <div class="observation-panel">
                    <h3>Observaciones</h3>
                    <textarea id="observations" placeholder="Registre sus observaciones aquí..."></textarea>
                    <button id="addObservationBtn">Agregar Observación</button>
                </div>
                
                <div class="metrics-panel">
                    <h3>Métricas en Tiempo Real</h3>
                    <div class="metric" id="taskTime">Tiempo de Tarea: 00:00</div>
                    <div class="metric" id="clickCount">Clics: 0</div>
                    <div class="metric" id="errorCount">Errores: 0</div>
                    <div class="metric" id="completionRate">Finalización: 0%</div>
                </div>
            </div>
        </section>

        <section class="heuristic-evaluation" id="heuristicSection" style="display: none;">
            <h2>Evaluación Heurística</h2>
            <div class="heuristic-checklist">
                <h3>10 Heurísticas de Usabilidad de Nielsen</h3>
                <div class="heuristic-item">
                    <h4>1. Visibilidad del estado del sistema</h4>
                    <div class="rating">
                        <input type="radio" name="heuristic1" value="1">1
                        <input type="radio" name="heuristic1" value="2">2
                        <input type="radio" name="heuristic1" value="3">3
                        <input type="radio" name="heuristic1" value="4">4
                        <input type="radio" name="heuristic1" value="5" checked>5
                    </div>
                    <textarea placeholder="Comentarios..."></textarea>
                </div>
                
                <div class="heuristic-item">
                    <h4>2. Concordancia entre el sistema y el mundo real</h4>
                    <div class="rating">
                        <input type="radio" name="heuristic2" value="1">1
                        <input type="radio" name="heuristic2" value="2">2
                        <input type="radio" name="heuristic2" value="3">3
                        <input type="radio" name="heuristic2" value="4">4
                        <input type="radio" name="heuristic2" value="5" checked>5
                    </div>
                    <textarea placeholder="Comentarios..."></textarea>
                </div>
                
                <!-- Agregar las restantes 8 heurísticas de manera similar -->
            </div>
            
            <button id="calculateHeuristicScore">Calcular Puntaje Heurístico</button>
            <div id="heuristicResults"></div>
        </section>

        <section class="accessibility-check" id="accessibilitySection" style="display: none;">
            <h2>Auditoría de Accesibilidad</h2>
            <div class="accessibility-tools">
                <button id="runAccessibilityCheck">Ejecutar Verificación Automatizada</button>
                <button id="manualAuditBtn">Auditoría Manual</button>
            </div>
            
            <div id="accessibilityResults"></div>
        </section>

        <section class="results-section" id="resultsSection" style="display: none;">
            <h2>Resultados de Evaluación</h2>
            <div class="results-tabs">
                <button class="tab-btn active" data-tab="summary">Resumen</button>
                <button class="tab-btn" data-tab="metrics">Métricas</button>
                <button class="tab-btn" data-tab="issues">Problemas</button>
                <button class="tab-btn" data-tab="recommendations">Recomendaciones</button>
            </div>
            
            <div class="tab-content">
                <div id="summaryTab" class="tab-panel active">
                    <h3>Resumen de Prueba</h3>
                    <div id="testSummary"></div>
                </div>
                
                <div id="metricsTab" class="tab-panel">
                    <h3>Métricas de Usabilidad</h3>
                    <canvas id="metricsChart"></canvas>
                </div>
                
                <div id="issuesTab" class="tab-panel">
                    <h3>Problemas Identificados</h3>
                    <div id="issuesList"></div>
                </div>
                
                <div id="recommendationsTab" class="tab-panel">
                    <h3>Recomendaciones</h3>
                    <div id="recommendationsList"></div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="usability.js"></script>
</body>
</html>
```

### Paso 2: CSS para Interfaz de Pruebas de Usabilidad
Crear un archivo `usability.css`:

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

/* Estilos de Formulario */
.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.form-group input, .form-group select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    font-size: 1rem;
}

.primary-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
}

.primary-btn:hover {
    background-color: #0056b3;
}

/* Interfaz de Prueba */
.test-controls {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin-bottom: 2rem;
}

.record-btn {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
}

.record-btn:hover {
    background-color: #c82333;
}

.pause-btn, .stop-btn {
    background-color: #ffc107;
    color: #212529;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
}

.pause-btn:hover, .stop-btn:hover {
    background-color: #e0a800;
}

#timer {
    font-size: 1.5rem;
    font-weight: bold;
    margin-left: auto;
}

.test-area {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.task-panel, .observation-panel, .metrics-panel {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.task-panel h3, .observation-panel h3, .metrics-panel h3 {
    margin-top: 0;
    color: #495057;
}

#currentTask {
    background-color: white;
    padding: 1rem;
    border-radius: 4px;
    margin-bottom: 1rem;
    min-height: 3rem;
    display: flex;
    align-items: center;
}

.task-controls {
    display: flex;
    gap: 1rem;
}

.success-btn {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
}

.success-btn:hover {
    background-color: #218838;
}

.failure-btn {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
}

.failure-btn:hover {
    background-color: #c82333;
}

#observations {
    width: 100%;
    height: 150px;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    resize: vertical;
}

.metric {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

/* Evaluación Heurística */
.heuristic-item {
    margin-bottom: 2rem;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 8px;
}

.heuristic-item h4 {
    margin-top: 0;
    color: #007bff;
}

.rating {
    margin: 1rem 0;
}

.rating input {
    margin-right: 0.5rem;
}

.heuristic-item textarea {
    width: 100%;
    height: 80px;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    resize: vertical;
}

/* Sección de Resultados */
.results-tabs {
    display: flex;
    margin-bottom: 2rem;
}

.tab-btn {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 0.75rem 1.5rem;
    cursor: pointer;
    border-radius: 4px 4px 0 0;
}

.tab-btn.active {
    background-color: white;
    border-bottom: 1px solid white;
}

.tab-panel {
    display: none;
    padding: 2rem;
    background-color: white;
    border: 1px solid #dee2e6;
    border-radius: 0 4px 4px 4px;
}

.tab-panel.active {
    display: block;
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

/* Responsivo */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    .test-area {
        grid-template-columns: 1fr;
    }
    
    .results-tabs {
        flex-direction: column;
    }
    
    .tab-btn {
        border-radius: 0;
    }
}
```

### Paso 3: JavaScript para Pruebas de Usabilidad
Crear un archivo `usability.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Configuración de prueba
    let currentTest = null;
    let testStartTime = null;
    let testTimer = null;
    let observations = [];
    let metrics = {
        clicks: 0,
        errors: 0,
        taskTime: 0,
        completionRate: 0
    };
    
    // Formulario de configuración de prueba
    document.getElementById('testConfigForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        currentTest = {
            name: document.getElementById('testName').value,
            evaluator: document.getElementById('evaluatorName').value,
            type: document.getElementById('testType').value,
            participants: parseInt(document.getElementById('participants').value),
            startTime: new Date(),
            tasks: [],
            observations: [],
            metrics: { ...metrics }
        };
        
        document.querySelector('.test-setup').style.display = 'none';
        document.getElementById('testInterface').style.display = 'block';
        
        showNotification('Prueba configurada exitosamente');
    });
    
    // Controles de grabación
    document.getElementById('recordBtn').addEventListener('click', function() {
        startRecording();
    });
    
    document.getElementById('pauseBtn').addEventListener('click', function() {
        pauseRecording();
    });
    
    document.getElementById('stopBtn').addEventListener('click', function() {
        stopRecording();
    });
    
    function startRecording() {
        testStartTime = new Date();
        testTimer = setInterval(updateTimer, 1000);
        
        document.getElementById('recordBtn').disabled = true;
        document.getElementById('pauseBtn').disabled = false;
        document.getElementById('stopBtn').disabled = false;
        document.getElementById('successBtn').disabled = false;
        document.getElementById('failureBtn').disabled = false;
        
        showNotification('Grabación iniciada');
    }
    
    function pauseRecording() {
        clearInterval(testTimer);
        
        document.getElementById('recordBtn').disabled = false;
        document.getElementById('pauseBtn').disabled = true;
        
        showNotification('Grabación pausada');
    }
    
    function stopRecording() {
        clearInterval(testTimer);
        
        document.getElementById('recordBtn').disabled = false;
        document.getElementById('pauseBtn').disabled = true;
        document.getElementById('stopBtn').disabled = true;
        document.getElementById('successBtn').disabled = true;
        document.getElementById('failureBtn').disabled = true;
        
        showNotification('Grabación detenida');
    }
    
    function updateTimer() {
        const now = new Date();
        const elapsed = Math.floor((now - testStartTime) / 1000);
        const hours = Math.floor(elapsed / 3600);
        const minutes = Math.floor((elapsed % 3600) / 60);
        const seconds = elapsed % 60;
        
        document.getElementById('timer').textContent = 
            `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    // Controles de tarea
    document.getElementById('successBtn').addEventListener('click', function() {
        recordTaskResult(true);
    });
    
    document.getElementById('failureBtn').addEventListener('click', function() {
        recordTaskResult(false);
    });
    
    function recordTaskResult(success) {
        const taskTime = Math.floor((new Date() - testStartTime) / 1000);
        
        const task = {
            description: document.getElementById('currentTask').textContent,
            success: success,
            time: taskTime,
            timestamp: new Date().toISOString()
        };
        
        currentTest.tasks.push(task);
        metrics.taskTime = taskTime;
        metrics.completionRate = success ? 100 : 0;
        
        updateMetrics();
        showNotification(`Tarea ${success ? 'completada exitosamente' : 'fallida'}`);
    }
    
    // Observaciones
    document.getElementById('addObservationBtn').addEventListener('click', function() {
        const observationText = document.getElementById('observations').value.trim();
        if (observationText) {
            const observation = {
                text: observationText,
                timestamp: new Date().toISOString(),
                type: 'manual'
            };
            
            observations.push(observation);
            currentTest.observations.push(observation);
            
            document.getElementById('observations').value = '';
            showNotification('Observación agregada');
        }
    });
    
    // Seguimiento de clics
    document.addEventListener('click', function(e) {
        if (testStartTime && !e.target.closest('nav') && !e.target.closest('.test-controls')) {
            metrics.clicks++;
            updateMetrics();
        }
    });
    
    // Seguimiento de errores (simplificado)
    window.addEventListener('error', function() {
        metrics.errors++;
        updateMetrics();
    });
    
    function updateMetrics() {
        document.getElementById('clickCount').textContent = `Clics: ${metrics.clicks}`;
        document.getElementById('errorCount').textContent = `Errores: ${metrics.errors}`;
        document.getElementById('taskTime').textContent = `Tiempo de Tarea: ${Math.floor(metrics.taskTime / 60)}:${(metrics.taskTime % 60).toString().padStart(2, '0')}`;
        document.getElementById('completionRate').textContent = `Finalización: ${metrics.completionRate}%`;
        
        currentTest.metrics = { ...metrics };
    }
    
    // Evaluación heurística
    document.getElementById('heuristicBtn').addEventListener('click', function() {
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('heuristicSection').style.display = 'block';
    });
    
    document.getElementById('calculateHeuristicScore').addEventListener('click', function() {
        const heuristicItems = document.querySelectorAll('.heuristic-item');
        let totalScore = 0;
        let maxScore = heuristicItems.length * 5;
        
        heuristicItems.forEach(item => {
            const radioButtons = item.querySelectorAll('input[type="radio"]:checked');
            if (radioButtons.length > 0) {
                totalScore += parseInt(radioButtons[0].value);
            }
        });
        
        const percentage = Math.round((totalScore / maxScore) * 100);
        
        document.getElementById('heuristicResults').innerHTML = `
            <h3>Resultados de Evaluación Heurística</h3>
            <p>Puntaje Total: ${totalScore}/${maxScore}</p>
            <p>Calificación de Usabilidad: ${percentage}%</p>
            <div class="score-bar">
                <div class="score-fill" style="width: ${percentage}%"></div>
            </div>
        `;
    });
    
    // Verificación de accesibilidad
    document.getElementById('accessibilityBtn').addEventListener('click', function() {
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('accessibilitySection').style.display = 'block';
    });
    
    document.getElementById('runAccessibilityCheck').addEventListener('click', function() {
        // Simular verificación de accesibilidad
        const results = [
            { type: 'error', message: 'Texto alternativo faltante en imágenes', count: 3 },
            { type: 'warning', message: 'Relación de contraste de color baja', count: 5 },
            { type: 'info', message: 'Etiquetas de formulario faltantes', count: 2 }
        ];
        
        let resultsHTML = '<h3>Resultados de Verificación de Accesibilidad</h3>';
        results.forEach(result => {
            resultsHTML += `<div class="accessibility-result ${result.type}">
                <strong>${result.type.toUpperCase()}:</strong> ${result.message} (${result.count} instancias)
            </div>`;
        });
        
        document.getElementById('accessibilityResults').innerHTML = resultsHTML;
    });
    
    // Generación de reporte
    document.getElementById('generateReportBtn').addEventListener('click', function() {
        if (!currentTest) {
            showNotification('No hay datos de prueba disponibles');
            return;
        }
        
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'block';
        
        generateReport();
    });
    
    function generateReport() {
        // Pestaña de resumen
        document.getElementById('testSummary').innerHTML = `
            <p><strong>Nombre de Prueba:</strong> ${currentTest.name}</p>
            <p><strong>Evaluador:</strong> ${currentTest.evaluator}</p>
            <p><strong>Tipo de Prueba:</strong> ${currentTest.type}</p>
            <p><strong>Duración:</strong> ${document.getElementById('timer').textContent}</p>
            <p><strong>Tareas Completadas:</strong> ${currentTest.tasks.length}</p>
            <p><strong>Observaciones:</strong> ${currentTest.observations.length}</p>
        `;
        
        // Pestaña de problemas
        let issuesHTML = '';
        if (metrics.errors > 0) {
            issuesHTML += `<div class="issue error">Errores detectados: ${metrics.errors}</div>`;
        }
        if (metrics.completionRate < 100) {
            issuesHTML += `<div class="issue warning">Tasa de finalización de tarea: ${metrics.completionRate}%</div>`;
        }
        document.getElementById('issuesList').innerHTML = issuesHTML || '<p>No se detectaron problemas mayores</p>';
        
        // Pestaña de recomendaciones
        const recommendations = [
            'Mejorar el manejo de errores y retroalimentación de usuario',
            'Simplificar tareas complejas y flujos de trabajo',
            'Agregar más elementos de navegación intuitivos',
            'Mejorar las características de accesibilidad',
            'Realizar sesiones adicionales de pruebas de usuario'
        ];
        
        let recHTML = '<ul>';
        recommendations.forEach(rec => {
            recHTML += `<li>${rec}</li>`;
        });
        recHTML += '</ul>';
        
        document.getElementById('recommendationsList').innerHTML = recHTML;
    }
    
    // Cambio de pestañas
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const tabName = this.dataset.tab;
            
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            
            this.classList.add('active');
            document.getElementById(tabName + 'Tab').classList.add('active');
        });
    });
    
    // Navegación
    document.getElementById('startTestBtn').addEventListener('click', function() {
        document.getElementById('testInterface').style.display = 'none';
        document.getElementById('heuristicSection').style.display = 'none';
        document.getElementById('accessibilitySection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
        document.querySelector('.test-setup').style.display = 'block';
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
});
```

### Paso 4: Calculador de Métricas de Usabilidad en Python
Crear un archivo `usability_metrics.py`:

```python
import json
import statistics
from datetime import datetime
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import numpy as np

class CalculadorMétricasUsabilidad:
    def __init__(self):
        self.datos_prueba = []
        self.metricas = {}
    
    def cargar_datos_prueba(self, ruta_archivo: str):
        """Cargar datos de prueba desde archivo JSON"""
        with open(ruta_archivo, 'r') as f:
            self.datos_prueba = json.load(f)
    
    def calcular_metricas_basicas(self) -> Dict[str, Any]:
        """Calcular métricas básicas de usabilidad"""
        if not self.datos_prueba:
            return {}
        
        total_tareas = len(self.datos_prueba.get('tasks', []))
        tareas_exitosas = sum(1 for tarea in self.datos_prueba.get('tasks', []) if tarea.get('success', False))
        
        tiempos_tarea = [tarea.get('time', 0) for tarea in self.datos_prueba.get('tasks', []) if tarea.get('success', False)]
        
        metricas = {
            'total_tareas': total_tareas,
            'tareas_exitosas': tareas_exitosas,
            'tasa_finalizacion': (tareas_exitosas / total_tareas * 100) if total_tareas > 0 else 0,
            'tiempo_promedio_tarea': statistics.mean(tiempos_tarea) if tiempos_tarea else 0,
            'tiempo_mediano_tarea': statistics.median(tiempos_tarea) if tiempos_tarea else 0,
            'desviacion_estandar_tiempo': statistics.stdev(tiempos_tarea) if len(tiempos_tarea) > 1 else 0,
            'total_observaciones': len(self.datos_prueba.get('observations', [])),
            'total_clics': self.datos_prueba.get('metrics', {}).get('clicks', 0),
            'total_errores': self.datos_prueba.get('metrics', {}).get('errors', 0)
        }
        
        self.metricas.update(metricas)
        return metricas
    
    def calcular_puntaje_sus(self, respuestas: List[int]) -> float:
        """Calcular puntaje de Escala de Usabilidad del Sistema (SUS)"""
        if len(respuestas) != 10:
            raise ValueError("SUS requiere exactamente 10 respuestas")
        
        # Puntuación SUS: restar 1 de elementos impares, 5-menos de elementos pares
        puntaje = 0
        for i, respuesta in enumerate(respuestas):
            if i % 2 == 0:  # Elementos impares (1,3,5,7,9)
                puntaje += respuesta - 1
            else:  # Elementos pares (2,4,6,8,10)
                puntaje += 5 - respuesta
        
        return puntaje * 2.5  # Escalar a 0-100
    
    def calcular_puntaje_nps(self, respuestas: List[int]) -> float:
        """Calcular Puntaje de Promotor Neto"""
        promotores = sum(1 for r in respuestas if r >= 9)
        detractores = sum(1 for r in respuestas if r <= 6)
        total = len(respuestas)
        
        if total == 0:
            return 0
        
        return ((promotores - detractores) / total) * 100
    
    def analizar_patron_observaciones(self) -> Dict[str, Any]:
        """Analizar patrones en observaciones de usuario"""
        observaciones = self.datos_prueba.get('observations', [])
        
        # Categorizar observaciones (simplificado)
        categorias = {
            'problemas_usabilidad': 0,
            'retroalimentacion_positiva': 0,
            'sugerencias': 0,
            'errores': 0,
            'navegacion': 0
        }
        
        palabras_clave = {
            'problemas_usabilidad': ['dificil', 'confuso', 'duro', 'problema'],
            'retroalimentacion_positiva': ['bueno', 'facil', 'genial', 'util', 'claro'],
            'sugerencias': ['deberia', 'podria', 'sugerir', 'mejorar'],
            'errores': ['error', 'equivocacion', 'equivocado', 'fallado'],
            'navegacion': ['encontrar', 'localizar', 'navegar', 'menu', 'boton']
        }
        
        for obs in observaciones:
            texto = obs.get('text', '').lower()
            for categoria, palabras in palabras_clave.items():
                if any(palabra in texto for palabra in palabras):
                    categorias[categoria] += 1
        
        return categorias
    
    def generar_recomendaciones(self) -> List[str]:
        """Generar recomendaciones procesables basadas en métricas"""
        recomendaciones = []
        
        if self.metricas.get('tasa_finalizacion', 0) < 80:
            recomendaciones.append("Mejorar la tasa de finalización de tareas mediante mejor guía de usuario")
        
        if self.metricas.get('tiempo_promedio_tarea', 0) > 300:  # 5 minutos
            recomendaciones.append("Reducir el tiempo de finalización de tareas simplificando flujos de trabajo")
        
        if self.metricas.get('total_errores', 0) > 5:
            recomendaciones.append("Abordar áreas propensas a errores con mejor validación y retroalimentación")
        
        analisis_observaciones = self.analizar_patron_observaciones()
        if analisis_observaciones.get('problemas_usabilidad', 0) > analisis_observaciones.get('retroalimentacion_positiva', 0):
            recomendaciones.append("Enfocarse en resolver problemas de usabilidad identificados")
        
        if len(recomendaciones) == 0:
            recomendaciones.append("La usabilidad general es buena, considerar refinamientos menores")
        
        return recomendaciones
    
    def crear_reporte_metricas(self, archivo_salida: str = 'reporte_usabilidad.json'):
        """Crear reporte integral de métricas"""
        reporte = {
            'info_prueba': {
                'nombre': self.datos_prueba.get('name', 'Desconocido'),
                'evaluador': self.datos_prueba.get('evaluator', 'Desconocido'),
                'tipo': self.datos_prueba.get('type', 'Desconocido'),
                'fecha': self.datos_prueba.get('startTime', datetime.now().isoformat())
            },
            'metricas': self.metricas,
            'analisis_observaciones': self.analizar_patron_observaciones(),
            'recomendaciones': self.generar_recomendaciones(),
            'generado_en': datetime.now().isoformat()
        }
        
        with open(archivo_salida, 'w') as f:
            json.dump(reporte, f, indent=2, default=str)
        
        print(f"Reporte de usabilidad generado: {archivo_salida}")
        return reporte
    
    def visualizar_metricas(self, ruta_guardado: str = 'metricas_usabilidad.png'):
        """Crear visualizaciones de métricas de usabilidad"""
        if not self.metricas:
            print("No hay métricas disponibles para visualización")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
        
        # Tasa de Finalización
        tasa_finalizacion = self.metricas.get('tasa_finalizacion', 0)
        ax1.bar(['Tasa de Finalización'], [tasa_finalizacion], color='skyblue')
        ax1.set_ylim(0, 100)
        ax1.set_title('Tasa de Finalización de Tareas (%)')
        ax1.text(0, tasa_finalizacion + 1, f'{tasa_finalizacion:.1f}%', ha='center')
        
        # Tiempos de Tarea
        tiempos_tarea = [tarea.get('time', 0) for tarea in self.datos_prueba.get('tasks', [])]
        if tiempos_tarea:
            ax2.hist(tiempos_tarea, bins=10, color='lightgreen', edgecolor='black')
            ax2.set_title('Tiempos de Finalización de Tareas (segundos)')
            ax2.set_xlabel('Tiempo (segundos)')
            ax2.set_ylabel('Frecuencia')
        
        # Análisis de Errores
        errores = self.metricas.get('total_errores', 0)
        clics = self.metricas.get('total_clics', 0)
        ax3.bar(['Clics', 'Errores'], [clics, errores], color=['blue', 'red'])
        ax3.set_title('Interacciones de Usuario')
        ax3.set_ylabel('Conteo')
        
        # Análisis de Observaciones
        analisis_obs = self.analizar_patron_observaciones()
        categorias = list(analisis_obs.keys())
        valores = list(analisis_obs.values())
        ax4.bar(categorias, valores, color='orange')
        ax4.set_title('Categorías de Observación')
        ax4.set_ylabel('Conteo')
        ax4.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Visualización de métricas guardada: {ruta_guardado}")

# Ejemplo de uso
if __name__ == "__main__":
    calculador = CalculadorMétricasUsabilidad()
    
    # Simular datos de prueba
    datos_prueba = {
        'name': 'Prueba de Usabilidad de Muestra',
        'evaluator': 'Evaluador de Prueba',
        'type': 'usability',
        'startTime': datetime.now().isoformat(),
        'tasks': [
            {'description': 'Tarea de inicio de sesión', 'success': True, 'time': 45},
            {'description': 'Tarea de navegación', 'success': False, 'time': 120},
            {'description': 'Tarea de búsqueda', 'success': True, 'time': 30}
        ],
        'observations': [
            {'text': 'El inicio de sesión fue fácil de encontrar', 'timestamp': datetime.now().isoformat()},
            {'text': 'El menú de navegación fue confuso', 'timestamp': datetime.now().isoformat()},
            {'text': 'Los resultados de búsqueda deberían cargar más rápido', 'timestamp': datetime.now().isoformat()}
        ],
        'metrics': {
            'clicks': 25,
            'errors': 3,
            'completionRate': 67
        }
    }
    
    calculador.datos_prueba = datos_prueba
    metricas = calculador.calcular_metricas_basicas()
    
    print("Métricas Básicas:")
    for clave, valor in metricas.items():
        print(f"  {clave}: {valor}")
    
    # Cálculo SUS de ejemplo
    respuestas_sus = [4, 3, 5, 2, 4, 3, 5, 2, 4, 3]  # Respuestas SUS de muestra
    puntaje_sus = calculador.calcular_puntaje_sus(respuestas_sus)
    print(f"\nPuntaje SUS: {puntaje_sus:.1f}")
    
    # Generar reporte
    reporte = calculador.crear_reporte_metricas()
    
    # Visualizar métricas
    calculador.visualizar_metricas()
```

### Paso 5: Documentación
Este marco de evaluación de usabilidad implementa múltiples métodos de evaluación del ISO 9241-11:

1. **Pruebas de Usabilidad**: Monitoreo de tareas en tiempo real con recopilación de métricas
2. **Evaluación Heurística**: Evaluación de las 10 heurísticas de usabilidad de Nielsen
3. **Auditoría de Accesibilidad**: Verificación automatizada y manual de accesibilidad
4. **Cálculo de Métricas**: Métricas integrales de usabilidad con análisis en Python

Características clave:
- Marco de evaluación multi-método
- Recopilación de datos en tiempo real y análisis
- Puntuación heurística automatizada
- Generación de reportes integral con recomendaciones
- Visualización de datos y exportación

El marco proporciona un kit de herramientas completo para realizar evaluaciones de usabilidad profesionales según estándares ISO 9241.
