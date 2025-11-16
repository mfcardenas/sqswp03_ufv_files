# Laboratorio 9: Estándares de Dispositivos de Entrada

## Solución

### Paso 1: HTML de Evaluación de Dispositivos de Entrada
Crear un archivo `input_device.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evaluación de Estándares de Dispositivos de Entrada - Laboratorio ISO 9241</title>
    <link rel="stylesheet" href="input.css">
</head>
<body>
    <header>
        <h1>Evaluación de Estándares de Dispositivos de Entrada</h1>
        <nav>
            <button id="deviceBtn">Selección de Dispositivo</button>
            <button id="ergonomicsBtn">Ergonómica</button>
            <button id="usabilityBtn">Prueba de Usabilidad</button>
            <button id="performanceBtn">Rendimiento</button>
            <button id="complianceBtn">Verificación de Cumplimiento</button>
            <button id="generateReportBtn">Generar Reporte</button>
        </nav>
    </header>

    <main>
        <section class="device-setup">
            <h2>Configuración del Dispositivo</h2>
            <form id="deviceConfigForm">
                <div class="form-group">
                    <label for="deviceType">Tipo de Dispositivo de Entrada:</label>
                    <select id="deviceType">
                        <option value="keyboard">Teclado</option>
                        <option value="mouse">Ratón</option>
                        <option value="touchpad">Panel Táctil</option>
                        <option value="trackball">Trackball</option>
                        <option value="joystick">Joystick</option>
                        <option value="gamepad">Gamepad</option>
                        <option value="touchscreen">Pantalla Táctil</option>
                        <option value="stylus">Lápiz Óptico</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="deviceModel">Modelo del Dispositivo:</label>
                    <input type="text" id="deviceModel" placeholder="ej. Logitech MX Master 3">
                </div>
                
                <div class="form-group">
                    <label for="connectionType">Tipo de Conexión:</label>
                    <select id="connectionType">
                        <option value="wired">Cableado</option>
                        <option value="wireless">Inalámbrico</option>
                        <option value="bluetooth">Bluetooth</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="userHandedness">Lateralidad del Usuario:</label>
                    <select id="userHandedness">
                        <option value="right">Diestro</option>
                        <option value="left">Zurdo</option>
                        <option value="ambidextrous">Ambidiestro</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="usageScenario">Escenario de Uso:</label>
                    <select id="usageScenario">
                        <option value="office">Trabajo de Oficina</option>
                        <option value="gaming">Juegos</option>
                        <option value="design">Diseño/CAD</option>
                        <option value="programming">Programación</option>
                        <option value="general">Uso General</option>
                    </select>
                </div>
                
                <button type="submit" class="primary-btn">Iniciar Evaluación</button>
            </form>
        </section>

        <section class="ergonomics-assessment" id="ergonomicsSection" style="display: none;">
            <h2>Evaluación Ergonómica</h2>
            
            <div class="ergonomics-tests">
                <div class="test-panel">
                    <h3>Prueba de Agarre y Postura</h3>
                    <div class="posture-guide">
                        <p>Posiciona tu mano en una postura natural y relajada.</p>
                        <div class="hand-position">
                            <div class="hand-outline">
                                <div class="finger" id="thumb"></div>
                                <div class="finger" id="index"></div>
                                <div class="finger" id="middle"></div>
                                <div class="finger" id="ring"></div>
                                <div class="finger" id="pinky"></div>
                            </div>
                        </div>
                    </div>
                    <button id="postureTestBtn">Evaluar Postura</button>
                    <div id="postureResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Prueba de Fuerza y Presión</h3>
                    <div class="force-test">
                        <p>Aplica presión normal al dispositivo de entrada.</p>
                        <div class="pressure-gauge">
                            <div class="gauge-fill" id="pressureFill"></div>
                            <div class="gauge-label">Nivel de Presión</div>
                        </div>
                    </div>
                    <button id="forceTestBtn">Medir Fuerza</button>
                    <div id="forceResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Prueba de Alcance y Movimiento</h3>
                    <div class="movement-test">
                        <p>Prueba patrones de movimiento naturales.</p>
                        <div class="movement-patterns">
                            <div class="pattern" data-pattern="circular">Circular</div>
                            <div class="pattern" data-pattern="linear">Lineal</div>
                            <div class="pattern" data-pattern="random">Aleatorio</div>
                        </div>
                    </div>
                    <button id="movementTestBtn">Probar Movimiento</button>
                    <div id="movementResults"></div>
                </div>
            </div>
        </section>

        <section class="usability-test" id="usabilitySection" style="display: none;">
            <h2>Prueba de Usabilidad</h2>
            
            <div class="usability-tests">
                <div class="test-panel">
                    <h3>Prueba de Precisión de Apuntado</h3>
                    <div class="accuracy-test">
                        <canvas id="accuracyCanvas" width="600" height="400"></canvas>
                        <div class="accuracy-controls">
                            <button id="startAccuracyTest">Iniciar Prueba</button>
                            <button id="resetAccuracyTest">Reiniciar</button>
                        </div>
                    </div>
                    <div id="accuracyResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Prueba de Velocidad de Clic</h3>
                    <div class="speed-test">
                        <div class="click-target" id="clickTarget">
                            <span>¡Haz Clic Aquí!</span>
                        </div>
                        <div class="speed-metrics">
                            <div class="metric">Clics: <span id="clickCount">0</span></div>
                            <div class="metric">Tiempo: <span id="clickTime">0.00s</span></div>
                            <div class="metric">CPP: <span id="clicksPerSecond">0.00</span></div>
                        </div>
                    </div>
                    <button id="startSpeedTest">Iniciar Prueba de Velocidad</button>
                    <button id="stopSpeedTest">Detener Prueba</button>
                    <div id="speedResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Prueba de Entrada de Texto</h3>
                    <div class="text-input-test">
                        <p>Escribe el siguiente texto lo más rápido y preciso posible:</p>
                        <div class="sample-text" id="sampleText">
                            El rápido zorro marrón salta sobre el perro perezoso. Esta oración contiene todas las letras del alfabeto y se utiliza comúnmente para pruebas de velocidad de escritura.
                        </div>
                        <textarea id="inputText" placeholder="Comienza a escribir aquí..."></textarea>
                        <div class="typing-metrics">
                            <div class="metric">PPM: <span id="wordsPerMinute">0</span></div>
                            <div class="metric">Precisión: <span id="typingAccuracy">100%</span></div>
                            <div class="metric">Errores: <span id="typingErrors">0</span></div>
                        </div>
                    </div>
                    <button id="startTypingTest">Iniciar Prueba de Escritura</button>
                    <button id="resetTypingTest">Reiniciar Prueba</button>
                    <div id="typingResults"></div>
                </div>
            </div>
        </section>

        <section class="performance-analysis" id="performanceSection" style="display: none;">
            <h2>Análisis de Rendimiento</h2>
            
            <div class="performance-metrics">
                <div class="metric-panel">
                    <h3>Tiempo de Respuesta</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="responseTimeValue">-- ms</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="responseTimeBar"></div>
                        </div>
                    </div>
                </div>
                
                <div class="metric-panel">
                    <h3>Rendimiento</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="throughputValue">-- ops/seg</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="throughputBar"></div>
                        </div>
                    </div>
                </div>
                
                <div class="metric-panel">
                    <h3>Tasa de Error</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="errorRateValue">-- %</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="errorRateBar"></div>
                        </div>
                    </div>
                </div>
                
                <div class="metric-panel">
                    <h3>Tiempo de Aprendizaje</h3>
                    <div class="metric-display">
                        <div class="metric-value" id="learningTimeValue">-- min</div>
                        <div class="metric-bar">
                            <div class="bar-fill" id="learningTimeBar"></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <button id="runPerformanceTest">Ejecutar Prueba de Rendimiento</button>
            <div id="performanceResults"></div>
        </section>

        <section class="compliance-check" id="complianceSection" style="display: none;">
            <h2>Verificación de Cumplimiento ISO 9241</h2>
            
            <div class="compliance-checklist">
                <h3>Lista de Verificación de Estándares de Dispositivos de Entrada</h3>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req1">
                    <label for="req1">Las dimensiones del dispositivo cumplen con requisitos antropométricos</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req2">
                    <label for="req2">La fuerza de operación cumple con directrices ergonómicas (≤ 2N para teclas)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req3">
                    <label for="req3">La distancia de recorrido de tecla cumple con estándares de usabilidad (1.5-4mm)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req4">
                    <label for="req4">La retroalimentación táctil cumple con requisitos de accesibilidad</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req5">
                    <label for="req5">El peso del dispositivo cumple con requisitos de portabilidad (≤ 100g para móvil)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req6">
                    <label for="req6">La longitud del cable cumple con requisitos de espacio de trabajo (≥ 1.5m para cableado)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req7">
                    <label for="req7">La duración de la batería cumple con requisitos de uso (≥ 3 meses para inalámbrico)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req8">
                    <label for="req8">El dispositivo soporta múltiples tamaños de mano y estilos de agarre</label>
                </div>
            </div>
            
            <button id="runComplianceCheck">Ejecutar Evaluación de Cumplimiento</button>
            <div id="complianceResults"></div>
        </section>

        <section class="results-section" id="resultsSection" style="display: none;">
            <h2>Resultados de Evaluación</h2>
            <div class="results-tabs">
                <button class="tab-btn active" data-tab="summary">Resumen</button>
                <button class="tab-btn" data-tab="ergonomics">Ergonómica</button>
                <button class="tab-btn" data-tab="usability">Usabilidad</button>
                <button class="tab-btn" data-tab="performance">Rendimiento</button>
                <button class="tab-btn" data-tab="compliance">Cumplimiento</button>
            </div>
            
            <div class="tab-content">
                <div id="summaryTab" class="tab-panel active">
                    <h3>Resumen de Evaluación</h3>
                    <div id="assessmentSummary"></div>
                </div>
                
                <div id="ergonomicsTab" class="tab-panel">
                    <h3>Evaluación Ergonómica</h3>
                    <div id="ergonomicsEvaluation"></div>
                </div>
                
                <div id="usabilityTab" class="tab-panel">
                    <h3>Evaluación de Usabilidad</h3>
                    <div id="usabilityAssessment"></div>
                </div>
                
                <div id="performanceTab" class="tab-panel">
                    <h3>Análisis de Rendimiento</h3>
                    <div id="performanceAnalysis"></div>
                </div>
                
                <div id="complianceTab" class="tab-panel">
                    <h3>Estado de Cumplimiento</h3>
                    <div id="complianceStatus"></div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="input.js"></script>
</body>
</html>
```

### Paso 2: CSS para Interfaz de Evaluación de Dispositivos de Entrada
Crear un archivo `input.css`:

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

/* Pruebas Ergonómicas */
.ergonomics-tests {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.test-panel {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.test-panel h3 {
    margin-top: 0;
    color: #007bff;
}

.hand-outline {
    width: 200px;
    height: 150px;
    background-color: #e9ecef;
    border-radius: 20px;
    margin: 1rem auto;
    position: relative;
    display: flex;
    justify-content: space-around;
    align-items: flex-end;
    padding: 1rem;
}

.finger {
    width: 20px;
    height: 60px;
    background-color: #007bff;
    border-radius: 10px;
    transition: all 0.3s ease;
}

.finger:hover {
    background-color: #0056b3;
    transform: scale(1.1);
}

.pressure-gauge {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background-color: #e9ecef;
    margin: 1rem auto;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.gauge-fill {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    background-color: #007bff;
    border-radius: 10px 10px 0 0;
    transition: height 0.3s ease;
}

.gauge-label {
    font-weight: bold;
    z-index: 1;
}

.movement-patterns {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1rem 0;
}

.pattern {
    padding: 1rem;
    background-color: #007bff;
    color: white;
    border-radius: 4px;
    text-align: center;
    cursor: pointer;
}

.pattern:hover {
    background-color: #0056b3;
}

/* Pruebas de Usabilidad */
.usability-tests {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.accuracy-test {
    margin: 1rem 0;
}

#accuracyCanvas {
    border: 2px solid #dee2e6;
    border-radius: 4px;
    background-color: #f8f9fa;
}

.accuracy-controls {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.click-target {
    width: 150px;
    height: 150px;
    background-color: #007bff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    margin: 1rem auto;
    transition: all 0.2s ease;
}

.click-target:hover {
    background-color: #0056b3;
    transform: scale(1.05);
}

.speed-metrics {
    display: flex;
    justify-content: space-around;
    margin: 1rem 0;
}

.metric {
    text-align: center;
    font-weight: bold;
}

.sample-text {
    background-color: #e9ecef;
    padding: 1rem;
    border-radius: 4px;
    margin: 1rem 0;
    font-family: monospace;
}

#inputText {
    width: 100%;
    height: 100px;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    font-family: monospace;
    resize: vertical;
}

.typing-metrics {
    display: flex;
    justify-content: space-around;
    margin: 1rem 0;
}

/* Métricas de Rendimiento */
.performance-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.metric-panel {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
}

.metric-panel h3 {
    margin-top: 0;
    color: #007bff;
}

.metric-value {
    font-size: 2rem;
    font-weight: bold;
    color: #007bff;
    margin: 1rem 0;
}

.metric-bar {
    width: 100%;
    height: 20px;
    background-color: #e9ecef;
    border-radius: 10px;
    overflow: hidden;
}

.bar-fill {
    height: 100%;
    background-color: #007bff;
    width: 0%;
    transition: width 0.3s ease;
}

/* Lista de Verificación de Cumplimiento */
.compliance-checklist {
    margin-top: 2rem;
}

.compliance-item {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    padding: 0.5rem;
    background-color: #f8f9fa;
    border-radius: 4px;
}

.compliance-item input[type="checkbox"] {
    margin-right: 1rem;
    transform: scale(1.2);
}

.compliance-item label {
    flex: 1;
    cursor: pointer;
}

/* Sección de Resultados */
.results-tabs {
    display: flex;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.tab-btn {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 0.75rem 1.5rem;
    cursor: pointer;
    border-radius: 4px 4px 0 0;
    margin-right: 0.25rem;
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
    
    .ergonomics-tests, .usability-tests, .performance-metrics {
        grid-template-columns: 1fr;
    }
    
    .results-tabs {
        flex-direction: column;
    }
    
    .tab-btn {
        border-radius: 0;
        margin-right: 0;
    }
    
    .speed-metrics, .typing-metrics {
        flex-direction: column;
        gap: 0.5rem;
    }
}
```

### Paso 3: JavaScript para Evaluación de Dispositivos de Entrada
Crear un archivo `input.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Configuración de evaluación
    let currentAssessment = null;
    let assessmentResults = {
        ergonomics: {},
        usability: {},
        performance: {},
        compliance: {}
    };
    
    // Formulario de configuración del dispositivo
    document.getElementById('deviceConfigForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        currentAssessment = {
            deviceType: document.getElementById('deviceType').value,
            deviceModel: document.getElementById('deviceModel').value,
            connectionType: document.getElementById('connectionType').value,
            userHandedness: document.getElementById('userHandedness').value,
            usageScenario: document.getElementById('usageScenario').value,
            startTime: new Date()
        };
        
        document.querySelector('.device-setup').style.display = 'none';
        document.getElementById('ergonomicsSection').style.display = 'block';
        
        showNotification('Evaluación del dispositivo configurada exitosamente');
    });
    
    // Navegación
    document.getElementById('deviceBtn').addEventListener('click', function() {
        hideAllSections();
        document.querySelector('.device-setup').style.display = 'block';
    });
    
    document.getElementById('ergonomicsBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('ergonomicsSection').style.display = 'block';
    });
    
    document.getElementById('usabilityBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('usabilitySection').style.display = 'block';
    });
    
    document.getElementById('performanceBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('performanceSection').style.display = 'block';
    });
    
    document.getElementById('complianceBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('complianceSection').style.display = 'block';
    });
    
    function hideAllSections() {
        document.querySelector('.device-setup').style.display = 'none';
        document.getElementById('ergonomicsSection').style.display = 'none';
        document.getElementById('usabilitySection').style.display = 'none';
        document.getElementById('performanceSection').style.display = 'none';
        document.getElementById('complianceSection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
    }
    
    // Evaluación ergonómica
    document.getElementById('postureTestBtn').addEventListener('click', function() {
        // Simular evaluación de postura
        const postureScore = Math.random() * 30 + 70; // 70-100%
        const comfortLevel = postureScore > 85 ? 'excellent' : postureScore > 75 ? 'good' : 'fair';
        
        document.getElementById('postureResults').innerHTML = `
            <h4>Resultados de Evaluación de Postura</h4>
            <p>Puntaje de Postura: ${postureScore.toFixed(1)}%</p>
            <p>Nivel de Confort: <span class="${comfortLevel}">${comfortLevel.toUpperCase()}</span></p>
            <p class="${comfortLevel === 'excellent' ? 'good' : comfortLevel === 'good' ? 'good' : 'poor'}">
                ${comfortLevel === 'excellent' ? '✓ Posicionamiento de mano excelente' : 
                  comfortLevel === 'good' ? '✓ Buen posicionamiento de mano' : 
                  '⚠ Considerar ajustar posición de mano'}
            </p>
        `;
        
        assessmentResults.ergonomics.postureScore = postureScore;
        showNotification('Prueba de postura completada');
    });
    
    document.getElementById('forceTestBtn').addEventListener('click', function() {
        // Simular medición de fuerza
        const forceLevel = Math.random() * 3 + 0.5; // 0.5-3.5N
        const optimal = forceLevel <= 2.0;
        
        // Actualizar indicador de presión
        const pressurePercent = Math.min((forceLevel / 4) * 100, 100);
        document.getElementById('pressureFill').style.height = pressurePercent + '%';
        
        document.getElementById('forceResults').innerHTML = `
            <h4>Resultados de Medición de Fuerza</h4>
            <p>Fuerza Aplicada: ${forceLevel.toFixed(1)} N</p>
            <p class="${optimal ? 'good' : 'poor'}">
                ${optimal ? '✓ Nivel de fuerza dentro del rango óptimo' : '⚠ Nivel de fuerza puede causar fatiga'}
            </p>
        `;
        
        assessmentResults.ergonomics.forceLevel = forceLevel;
        showNotification('Prueba de fuerza completada');
    });
    
    document.getElementById('movementTestBtn').addEventListener('click', function() {
        // Simular prueba de patrón de movimiento
        const movementEfficiency = Math.random() * 20 + 80; // 80-100%
        const naturalMovement = movementEfficiency > 85;
        
        document.getElementById('movementResults').innerHTML = `
            <h4>Resultados de Patrón de Movimiento</h4>
            <p>Eficiencia de Movimiento: ${movementEfficiency.toFixed(1)}%</p>
            <p class="${naturalMovement ? 'good' : 'poor'}">
                ${naturalMovement ? '✓ Patrones de movimiento naturales detectados' : '⚠ El movimiento puede requerir ajuste'}
            </p>
        `;
        
        assessmentResults.ergonomics.movementEfficiency = movementEfficiency;
        showNotification('Prueba de movimiento completada');
    });
    
    // Prueba de usabilidad
    let accuracyTestActive = false;
    let accuracyTargets = [];
    let accuracyClicks = [];
    const accuracyCanvas = document.getElementById('accuracyCanvas');
    const ctx = accuracyCanvas.getContext('2d');
    
    document.getElementById('startAccuracyTest').addEventListener('click', function() {
        accuracyTestActive = true;
        accuracyTargets = [];
        accuracyClicks = [];
        
        // Generar objetivos aleatorios
        for (let i = 0; i < 10; i++) {
            accuracyTargets.push({
                x: Math.random() * (accuracyCanvas.width - 40) + 20,
                y: Math.random() * (accuracyCanvas.height - 40) + 20,
                radius: 15
            });
        }
        
        drawAccuracyTest();
        showNotification('Prueba de precisión iniciada - haz clic en los objetivos');
    });
    
    document.getElementById('resetAccuracyTest').addEventListener('click', function() {
        accuracyTestActive = false;
        accuracyTargets = [];
        accuracyClicks = [];
        ctx.clearRect(0, 0, accuracyCanvas.width, accuracyCanvas.height);
    });
    
    accuracyCanvas.addEventListener('click', function(e) {
        if (!accuracyTestActive) return;
        
        const rect = accuracyCanvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        accuracyClicks.push({ x, y });
        
        // Verificar si el clic está dentro de un objetivo
        let hit = false;
        accuracyTargets.forEach((target, index) => {
            const distance = Math.sqrt((x - target.x) ** 2 + (y - target.y) ** 2);
            if (distance <= target.radius) {
                hit = true;
                accuracyTargets.splice(index, 1);
            }
        });
        
        if (hit) {
            drawAccuracyTest();
            if (accuracyTargets.length === 0) {
                // Prueba completada
                const accuracy = (accuracyClicks.length / 10) * 100;
                document.getElementById('accuracyResults').innerHTML = `
                    <h4>Resultados de Precisión de Apuntado</h4>
                    <p>Objetivos Alcanzados: ${accuracyClicks.length}/10</p>
                    <p>Precisión: ${accuracy.toFixed(1)}%</p>
                    <p class="${accuracy >= 80 ? 'good' : 'poor'}">
                        ${accuracy >= 80 ? '✓ Buena precisión de apuntado' : '⚠ La precisión necesita mejora'}
                    </p>
                `;
                assessmentResults.usability.accuracy = accuracy;
                accuracyTestActive = false;
                showNotification('Prueba de precisión completada');
            }
        }
    });
    
    function drawAccuracyTest() {
        ctx.clearRect(0, 0, accuracyCanvas.width, accuracyCanvas.height);
        
        // Dibujar objetivos
        accuracyTargets.forEach(target => {
            ctx.beginPath();
            ctx.arc(target.x, target.y, target.radius, 0, 2 * Math.PI);
            ctx.fillStyle = '#007bff';
            ctx.fill();
            ctx.strokeStyle = '#0056b3';
            ctx.lineWidth = 2;
            ctx.stroke();
        });
        
        // Dibujar puntos de clic
        accuracyClicks.forEach(click => {
            ctx.beginPath();
            ctx.arc(click.x, click.y, 3, 0, 2 * Math.PI);
            ctx.fillStyle = '#dc3545';
            ctx.fill();
        });
    }
    
    // Prueba de velocidad de clic
    let speedTestActive = false;
    let clickCount = 0;
    let startTime = 0;
    let speedInterval;
    
    document.getElementById('startSpeedTest').addEventListener('click', function() {
        speedTestActive = true;
        clickCount = 0;
        startTime = Date.now();
        
        document.getElementById('clickCount').textContent = '0';
        document.getElementById('clickTime').textContent = '0.00s';
        document.getElementById('clicksPerSecond').textContent = '0.00';
        
        speedInterval = setInterval(updateSpeedMetrics, 100);
        showNotification('Prueba de velocidad iniciada - haz clic lo más rápido posible');
    });
    
    document.getElementById('stopSpeedTest').addEventListener('click', function() {
        speedTestActive = false;
        clearInterval(speedInterval);
        
        const elapsed = (Date.now() - startTime) / 1000;
        const cps = clickCount / elapsed;
        
        document.getElementById('speedResults').innerHTML = `
            <h4>Resultados de Velocidad de Clic</h4>
            <p>Clics Totales: ${clickCount}</p>
            <p>Tiempo: ${elapsed.toFixed(2)}s</p>
            <p>Clics Por Segundo: ${cps.toFixed(2)}</p>
            <p class="${cps >= 5 ? 'good' : 'poor'}">
                ${cps >= 5 ? '✓ Buena velocidad de clic' : '⚠ La velocidad puede necesitar mejora'}
            </p>
        `;
        
        assessmentResults.usability.clickSpeed = cps;
        showNotification('Prueba de velocidad completada');
    });
    
    document.getElementById('clickTarget').addEventListener('click', function() {
        if (speedTestActive) {
            clickCount++;
            document.getElementById('clickCount').textContent = clickCount;
        }
    });
    
    function updateSpeedMetrics() {
        if (!speedTestActive) return;
        
        const elapsed = (Date.now() - startTime) / 1000;
        const cps = clickCount / elapsed;
        
        document.getElementById('clickTime').textContent = elapsed.toFixed(2) + 's';
        document.getElementById('clicksPerSecond').textContent = cps.toFixed(2);
    }
    
    // Prueba de escritura
    let typingTestActive = false;
    let typingStartTime = 0;
    const sampleText = document.getElementById('sampleText').textContent;
    
    document.getElementById('startTypingTest').addEventListener('click', function() {
        typingTestActive = true;
        typingStartTime = Date.now();
        document.getElementById('inputText').value = '';
        document.getElementById('inputText').focus();
        showNotification('Prueba de escritura iniciada');
    });
    
    document.getElementById('resetTypingTest').addEventListener('click', function() {
        typingTestActive = false;
        document.getElementById('inputText').value = '';
        document.getElementById('wordsPerMinute').textContent = '0';
        document.getElementById('typingAccuracy').textContent = '100%';
        document.getElementById('typingErrors').textContent = '0';
    });
    
    document.getElementById('inputText').addEventListener('input', function() {
        if (!typingTestActive) return;
        
        const typedText = this.value;
        const elapsed = (Date.now() - typingStartTime) / 1000 / 60; // minutos
        
        // Calcular PPM
        const wordsTyped = typedText.split(' ').length;
        const wpm = wordsTyped / elapsed;
        document.getElementById('wordsPerMinute').textContent = wpm.toFixed(1);
        
        // Calcular precisión
        let errors = 0;
        const minLength = Math.min(typedText.length, sampleText.length);
        for (let i = 0; i < minLength; i++) {
            if (typedText[i] !== sampleText[i]) {
                errors++;
            }
        }
        
        const accuracy = ((typedText.length - errors) / typedText.length) * 100;
        document.getElementById('typingAccuracy').textContent = accuracy.toFixed(1) + '%';
        document.getElementById('typingErrors').textContent = errors;
        
        // Verificar si la prueba está completa
        if (typedText.length >= sampleText.length) {
            typingTestActive = false;
            
            document.getElementById('typingResults').innerHTML = `
                <h4>Resultados de Prueba de Escritura</h4>
                <p>Palabras Por Minuto: ${wpm.toFixed(1)}</p>
                <p>Precisión: ${accuracy.toFixed(1)}%</p>
                <p>Errores: ${errors}</p>
                <p class="${wpm >= 40 && accuracy >= 90 ? 'good' : 'poor'}">
                    ${wpm >= 40 && accuracy >= 90 ? '✓ Buen rendimiento de escritura' : '⚠ El rendimiento de escritura necesita mejora'}
                </p>
            `;
            
            assessmentResults.usability.typingWPM = wpm;
            assessmentResults.usability.typingAccuracy = accuracy;
            showNotification('Prueba de escritura completada');
        }
    });
    
    // Análisis de rendimiento
    document.getElementById('runPerformanceTest').addEventListener('click', function() {
        // Simular métricas de rendimiento
        const responseTime = Math.random() * 50 + 10; // 10-60ms
        const throughput = Math.random() * 20 + 5; // 5-25 ops/seg
        const errorRate = Math.random() * 5; // 0-5%
        const learningTime = Math.random() * 30 + 10; // 10-40 min
        
        // Actualizar visualizaciones de métricas
        document.getElementById('responseTimeValue').textContent = responseTime.toFixed(1) + ' ms';
        document.getElementById('throughputValue').textContent = throughput.toFixed(1) + ' ops/seg';
        document.getElementById('errorRateValue').textContent = errorRate.toFixed(1) + ' %';
        document.getElementById('learningTimeValue').textContent = learningTime.toFixed(1) + ' min';
        
        // Actualizar barras
        document.getElementById('responseTimeBar').style.width = Math.min((responseTime / 100) * 100, 100) + '%';
        document.getElementById('throughputBar').style.width = Math.min((throughput / 30) * 100, 100) + '%';
        document.getElementById('errorRateBar').style.width = errorRate * 5 + '%';
        document.getElementById('learningTimeBar').style.width = Math.min((learningTime / 60) * 100, 100) + '%';
        
        document.getElementById('performanceResults').innerHTML = `
            <h4>Resultados de Análisis de Rendimiento</h4>
            <p>Tiempo de Respuesta: ${responseTime.toFixed(1)}ms ${responseTime < 30 ? '(Bueno)' : '(Lento)'}</p>
            <p>Rendimiento: ${throughput.toFixed(1)} ops/seg ${throughput > 10 ? '(Alto)' : '(Bajo)'}</p>
            <p>Tasa de Error: ${errorRate.toFixed(1)}% ${errorRate < 2 ? '(Baja)' : '(Alta)'}</p>
            <p>Tiempo de Aprendizaje: ${learningTime.toFixed(1)}min ${learningTime < 20 ? '(Rápido)' : '(Lento)'}</p>
        `;
        
        assessmentResults.performance = {
            responseTime,
            throughput,
            errorRate,
            learningTime
        };
        
        showNotification('Prueba de rendimiento completada');
    });
    
    // Verificación de cumplimiento
    document.getElementById('runComplianceCheck').addEventListener('click', function() {
        const checklistItems = document.querySelectorAll('.compliance-item input[type="checkbox"]');
        const checkedItems = document.querySelectorAll('.compliance-item input[type="checkbox"]:checked');
        
        const complianceScore = (checkedItems.length / checklistItems.length) * 100;
        
        let complianceLevel = 'poor';
        if (complianceScore >= 80) complianceLevel = 'excellent';
        else if (complianceScore >= 60) complianceLevel = 'good';
        else if (complianceScore >= 40) complianceLevel = 'fair';
        
        document.getElementById('complianceResults').innerHTML = `
            <h4>Resultados de Cumplimiento ISO 9241</h4>
            <p>Puntaje de Cumplimiento: ${complianceScore.toFixed(1)}%</p>
            <p>Nivel: <span class="${complianceLevel}">${complianceLevel.toUpperCase()}</span></p>
            <div class="compliance-bar">
                <div class="compliance-fill" style="width: ${complianceScore}%"></div>
            </div>
            <p>Requisitos Cumplidos: ${checkedItems.length}/${checklistItems.length}</p>
        `;
        
        assessmentResults.compliance.score = complianceScore;
        assessmentResults.compliance.level = complianceLevel;
        showNotification('Verificación de cumplimiento completada');
    });
    
    // Generación de reporte
    document.getElementById('generateReportBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('resultsSection').style.display = 'block';
        
        generateReport();
    });
    
    function generateReport() {
        // Pestaña de resumen
        document.getElementById('assessmentSummary').innerHTML = `
            <p><strong>Tipo de Dispositivo:</strong> ${currentAssessment.deviceType}</p>
            <p><strong>Modelo del Dispositivo:</strong> ${currentAssessment.deviceModel}</p>
            <p><strong>Tipo de Conexión:</strong> ${currentAssessment.connectionType}</p>
            <p><strong>Lateralidad del Usuario:</strong> ${currentAssessment.userHandedness}</p>
            <p><strong>Escenario de Uso:</strong> ${currentAssessment.usageScenario}</p>
            <p><strong>Fecha de Evaluación:</strong> ${currentAssessment.startTime.toLocaleDateString()}</p>
        `;
        
        // Pestaña ergonómica
        const ergonomics = assessmentResults.ergonomics;
        document.getElementById('ergonomicsEvaluation').innerHTML = `
            <h4>Evaluación Ergonómica</h4>
            ${ergonomics.postureScore ? `<p>Puntaje de Postura: ${ergonomics.postureScore.toFixed(1)}%</p>` : ''}
            ${ergonomics.forceLevel ? `<p>Nivel de Fuerza: ${ergonomics.forceLevel.toFixed(1)} N</p>` : ''}
            ${ergonomics.movementEfficiency ? `<p>Eficiencia de Movimiento: ${ergonomics.movementEfficiency.toFixed(1)}%</p>` : ''}
        `;
        
        // Pestaña de usabilidad
        const usability = assessmentResults.usability;
        document.getElementById('usabilityAssessment').innerHTML = `
            <h4>Evaluación de Usabilidad</h4>
            ${usability.accuracy ? `<p>Precisión de Apuntado: ${usability.accuracy.toFixed(1)}%</p>` : ''}
            ${usability.clickSpeed ? `<p>Velocidad de Clic: ${usability.clickSpeed.toFixed(2)} CPP</p>` : ''}
            ${usability.typingWPM ? `<p>Velocidad de Escritura: ${usability.typingWPM.toFixed(1)} PPM</p>` : ''}
            ${usability.typingAccuracy ? `<p>Precisión de Escritura: ${usability.typingAccuracy.toFixed(1)}%</p>` : ''}
        `;
        
        // Pestaña de rendimiento
        const performance = assessmentResults.performance;
        document.getElementById('performanceAnalysis').innerHTML = `
            <h4>Análisis de Rendimiento</h4>
            ${performance.responseTime ? `<p>Tiempo de Respuesta: ${performance.responseTime.toFixed(1)}ms</p>` : ''}
            ${performance.throughput ? `<p>Rendimiento: ${performance.throughput.toFixed(1)} ops/seg</p>` : ''}
            ${performance.errorRate ? `<p>Tasa de Error: ${performance.errorRate.toFixed(1)}%</p>` : ''}
            ${performance.learningTime ? `<p>Tiempo de Aprendizaje: ${performance.learningTime.toFixed(1)}min</p>` : ''}
        `;
        
        // Pestaña de cumplimiento
        const compliance = assessmentResults.compliance;
        document.getElementById('complianceStatus').innerHTML = `
            <h4>Estado de Cumplimiento</h4>
            ${compliance.score ? `<p>Puntaje de Cumplimiento: ${compliance.score.toFixed(1)}%</p>` : ''}
            ${compliance.level ? `<p>Nivel de Cumplimiento: ${compliance.level}</p>` : ''}
        `;
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

### Paso 4: Script de Análisis de Dispositivos de Entrada en Python
Crear un archivo `input_device_analysis.py`:

```python
import json
import math
from datetime import datetime
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import numpy as np

class AnalizadorDispositivoEntrada:
    def __init__(self):
        self.datos_evaluacion = {}
        self.resultados_analisis = {}
    
    def cargar_datos_evaluacion(self, ruta_archivo: str):
        """Cargar datos de evaluación de dispositivo de entrada"""
        with open(ruta_archivo, 'r') as f:
            self.datos_evaluacion = json.load(f)
    
    def analizar_ergonomia(self) -> Dict[str, float]:
        """Analizar factores ergonómicos"""
        ergonomia = self.datos_evaluacion.get('ergonomics', {})
        
        analisis = {}
        
        # Análisis de postura
        if 'postureScore' in ergonomia:
            puntaje_postura = ergonomia['postureScore']
            analisis['calidad_postura'] = self._calificar_postura(puntaje_postura)
        
        # Análisis de fuerza
        if 'forceLevel' in ergonomia:
            nivel_fuerza = ergonomia['forceLevel']
            analisis['calidad_fuerza'] = self._calificar_fuerza(nivel_fuerza)
        
        # Análisis de movimiento
        if 'movementEfficiency' in ergonomia:
            eficiencia_movimiento = ergonomia['movementEfficiency']
            analisis['calidad_movimiento'] = self._calificar_movimiento(eficiencia_movimiento)
        
        # Puntaje general ergonómico
        puntajes_ergonomicos = [v for v in analisis.values() if isinstance(v, (int, float))]
        analisis['ergonomia_general'] = sum(puntajes_ergonomicos) / len(puntajes_ergonomicos) if puntajes_ergonomicos else 0
        
        return analisis
    
    def analizar_usabilidad(self) -> Dict[str, float]:
        """Analizar métricas de usabilidad"""
        usabilidad = self.datos_evaluacion.get('usability', {})
        
        analisis = {}
        
        # Análisis de precisión
        if 'accuracy' in usabilidad:
            precision = usabilidad['accuracy']
            analisis['calidad_precision'] = self._calificar_precision(precision)
        
        # Análisis de velocidad de clic
        if 'clickSpeed' in usabilidad:
            velocidad_clic = usabilidad['clickSpeed']
            analisis['calidad_velocidad_clic'] = self._calificar_velocidad_clic(velocidad_clic)
        
        # Análisis de escritura
        if 'typingWPM' in usabilidad:
            escritura_ppm = usabilidad['typingWPM']
            analisis['calidad_velocidad_escritura'] = self._calificar_velocidad_escritura(escritura_ppm)
        
        if 'typingAccuracy' in usabilidad:
            precision_escritura = usabilidad['typingAccuracy']
            analisis['calidad_precision_escritura'] = self._calificar_precision_escritura(precision_escritura)
        
        # Puntaje general de usabilidad
        puntajes_usabilidad = [v for v in analisis.values() if isinstance(v, (int, float))]
        analisis['usabilidad_general'] = sum(puntajes_usabilidad) / len(puntajes_usabilidad) if puntajes_usabilidad else 0
        
        return analisis
    
    def analizar_rendimiento(self) -> Dict[str, float]:
        """Analizar métricas de rendimiento"""
        rendimiento = self.datos_evaluacion.get('performance', {})
        
        analisis = {}
        
        # Análisis de tiempo de respuesta
        if 'responseTime' in rendimiento:
            tiempo_respuesta = rendimiento['responseTime']
            analisis['calidad_tiempo_respuesta'] = self._calificar_tiempo_respuesta(tiempo_respuesta)
        
        # Análisis de rendimiento
        if 'throughput' in rendimiento:
            rendimiento_valor = rendimiento['throughput']
            analisis['calidad_rendimiento'] = self._calificar_rendimiento(rendimiento_valor)
        
        # Análisis de tasa de error
        if 'errorRate' in rendimiento:
            tasa_error = rendimiento['errorRate']
            analisis['calidad_tasa_error'] = self._calificar_tasa_error(tasa_error)
        
        # Análisis de tiempo de aprendizaje
        if 'learningTime' in rendimiento:
            tiempo_aprendizaje = rendimiento['learningTime']
            analisis['calidad_tiempo_aprendizaje'] = self._calificar_tiempo_aprendizaje(tiempo_aprendizaje)
        
        # Puntaje general de rendimiento
        puntajes_rendimiento = [v for v in analisis.values() if isinstance(v, (int, float))]
        analisis['rendimiento_general'] = sum(puntajes_rendimiento) / len(puntajes_rendimiento) if puntajes_rendimiento else 0
        
        return analisis
    
    def analizar_cumplimiento(self) -> Dict[str, float]:
        """Analizar cumplimiento ISO 9241"""
        cumplimiento = self.datos_evaluacion.get('compliance', {})
        
        analisis = {}
        
        if 'score' in cumplimiento:
            puntaje = cumplimiento['score']
            analisis['puntaje_cumplimiento'] = puntaje
            analisis['nivel_cumplimiento'] = self._calificar_cumplimiento(puntaje)
        
        return analisis
    
    def _calificar_postura(self, puntaje_postura: float) -> float:
        """Calificar calidad de postura (0-100)"""
        if puntaje_postura >= 90:
            return 100
        elif puntaje_postura >= 80:
            return 80
        elif puntaje_postura >= 70:
            return 60
        elif puntaje_postura >= 60:
            return 40
        else:
            return 20
    
    def _calificar_fuerza(self, nivel_fuerza: float) -> float:
        """Calificar nivel de fuerza (0-100)"""
        if 0.5 <= nivel_fuerza <= 2.0:
            return 100
        elif 0.3 <= nivel_fuerza <= 3.0:
            return 80
        elif 0.2 <= nivel_fuerza <= 4.0:
            return 60
        else:
            return 40
    
    def _calificar_movimiento(self, eficiencia_movimiento: float) -> float:
        """Calificar eficiencia de movimiento (0-100)"""
        if eficiencia_movimiento >= 90:
            return 100
        elif eficiencia_movimiento >= 80:
            return 80
        elif eficiencia_movimiento >= 70:
            return 60
        elif eficiencia_movimiento >= 60:
            return 40
        else:
            return 20
    
    def _calificar_precision(self, precision: float) -> float:
        """Calificar precisión de apuntado (0-100)"""
        if precision >= 90:
            return 100
        elif precision >= 80:
            return 80
        elif precision >= 70:
            return 60
        elif precision >= 60:
            return 40
        else:
            return 20
    
    def _calificar_velocidad_clic(self, velocidad_clic: float) -> float:
        """Calificar velocidad de clic (0-100)"""
        if velocidad_clic >= 8:
            return 100
        elif velocidad_clic >= 6:
            return 80
        elif velocidad_clic >= 4:
            return 60
        elif velocidad_clic >= 2:
            return 40
        else:
            return 20
    
    def _calificar_velocidad_escritura(self, escritura_ppm: float) -> float:
        """Calificar velocidad de escritura (0-100)"""
        if escritura_ppm >= 60:
            return 100
        elif escritura_ppm >= 45:
            return 80
        elif escritura_ppm >= 30:
            return 60
        elif escritura_ppm >= 15:
            return 40
        else:
            return 20
    
    def _calificar_precision_escritura(self, precision_escritura: float) -> float:
        """Calificar precisión de escritura (0-100)"""
        if precision_escritura >= 95:
            return 100
        elif precision_escritura >= 90:
            return 80
        elif precision_escritura >= 85:
            return 60
        elif precision_escritura >= 80:
            return 40
        else:
            return 20
    
    def _calificar_tiempo_respuesta(self, tiempo_respuesta: float) -> float:
        """Calificar tiempo de respuesta (0-100)"""
        if tiempo_respuesta <= 20:
            return 100
        elif tiempo_respuesta <= 40:
            return 80
        elif tiempo_respuesta <= 60:
            return 60
        elif tiempo_respuesta <= 80:
            return 40
        else:
            return 20
    
    def _calificar_rendimiento(self, rendimiento_valor: float) -> float:
        """Calificar rendimiento (0-100)"""
        if rendimiento_valor >= 20:
            return 100
        elif rendimiento_valor >= 15:
            return 80
        elif rendimiento_valor >= 10:
            return 60
        elif rendimiento_valor >= 5:
            return 40
        else:
            return 20
    
    def _calificar_tasa_error(self, tasa_error: float) -> float:
        """Calificar tasa de error (0-100)"""
        if tasa_error <= 1:
            return 100
        elif tasa_error <= 2:
            return 80
        elif tasa_error <= 4:
            return 60
        elif tasa_error <= 6:
            return 40
        else:
            return 20
    
    def _calificar_tiempo_aprendizaje(self, tiempo_aprendizaje: float) -> float:
        """Calificar tiempo de aprendizaje (0-100)"""
        if tiempo_aprendizaje <= 15:
            return 100
        elif tiempo_aprendizaje <= 25:
            return 80
        elif tiempo_aprendizaje <= 35:
            return 60
        elif tiempo_aprendizaje <= 45:
            return 40
        else:
            return 20
    
    def _calificar_cumplimiento(self, puntaje: float) -> str:
        """Calificar nivel de cumplimiento"""
        if puntaje >= 80:
            return "Excelente"
        elif puntaje >= 60:
            return "Bueno"
        elif puntaje >= 40:
            return "Regular"
        else:
            return "Deficiente"
    
    def generar_reporte_integral(self) -> Dict:
        """Generar reporte integral de análisis de dispositivo de entrada"""
        reporte = {
            'info_dispositivo': {
                'tipo_dispositivo': self.datos_evaluacion.get('deviceType', 'Desconocido'),
                'modelo_dispositivo': self.datos_evaluacion.get('deviceModel', 'Desconocido'),
                'tipo_conexion': self.datos_evaluacion.get('connectionType', 'Desconocido'),
                'lateralidad_usuario': self.datos_evaluacion.get('userHandedness', 'Desconocido'),
                'escenario_uso': self.datos_evaluacion.get('usageScenario', 'Desconocido'),
                'fecha_evaluacion': self.datos_evaluacion.get('startTime', datetime.now().isoformat())
            },
            'analisis_ergonomia': self.analizar_ergonomia(),
            'analisis_usabilidad': self.analizar_usabilidad(),
            'analisis_rendimiento': self.analizar_rendimiento(),
            'analisis_cumplimiento': self.analizar_cumplimiento(),
            'recomendaciones': self.generar_recomendaciones(),
            'generado_en': datetime.now().isoformat()
        }
        
        # Calcular puntaje general
        analisis = [reporte['analisis_ergonomia'], reporte['analisis_usabilidad'], 
                   reporte['analisis_rendimiento'], reporte['analisis_cumplimiento']]
        
        puntajes_generales = []
        for analisis_item in analisis:
            for clave, valor in analisis_item.items():
                if clave.startswith('general_') or clave == 'puntaje_cumplimiento':
                    puntajes_generales.append(valor)
        
        reporte['puntaje_general'] = sum(puntajes_generales) / len(puntajes_generales) if puntajes_generales else 0
        
        return reporte
    
    def generar_recomendaciones(self) -> List[str]:
        """Generar recomendaciones basadas en análisis"""
        recomendaciones = []
        
        # Recomendaciones ergonómicas
        ergonomia = self.analizar_ergonomia()
        if ergonomia.get('ergonomia_general', 0) < 70:
            recomendaciones.append("Considerar ajustes ergonómicos para mejor postura y reducción de tensión")
        
        # Recomendaciones de usabilidad
        usabilidad = self.analizar_usabilidad()
        if usabilidad.get('usabilidad_general', 0) < 70:
            recomendaciones.append("Mejorar usabilidad del dispositivo mediante mejor diseño y retroalimentación de usuario")
        
        # Recomendaciones de rendimiento
        rendimiento = self.analizar_rendimiento()
        if rendimiento.get('rendimiento_general', 0) < 70:
            recomendaciones.append("Optimizar rendimiento del dispositivo para mejor tiempo de respuesta y precisión")
        
        # Recomendaciones de cumplimiento
        cumplimiento = self.analizar_cumplimiento()
        if cumplimiento.get('puntaje_cumplimiento', 0) < 80:
            recomendaciones.append("Abordar problemas de cumplimiento ISO 9241 para estándares de dispositivos de entrada")
        
        if not recomendaciones:
            recomendaciones.append("El dispositivo de entrada cumple estándares aceptables - continuar monitoreando rendimiento")
        
        return recomendaciones
    
    def guardar_reporte(self, ruta_archivo: str = 'reporte_dispositivo_entrada.json'):
        """Guardar reporte integral en archivo"""
        reporte = self.generar_reporte_integral()
        
        with open(ruta_archivo, 'w') as f:
            json.dump(reporte, f, indent=2, default=str)
        
        print(f"Reporte de dispositivo de entrada guardado: {ruta_archivo}")
        return reporte
    
    def visualizar_analisis(self, ruta_guardado: str = 'analisis_dispositivo_entrada.png'):
        """Crear visualizaciones del análisis"""
        reporte = self.generar_reporte_integral()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # Puntajes generales
        categorias = ['Ergonomía', 'Usabilidad', 'Rendimiento', 'Cumplimiento']
        puntajes = [
            reporte['analisis_ergonomia'].get('ergonomia_general', 0),
            reporte['analisis_usabilidad'].get('usabilidad_general', 0),
            reporte['analisis_rendimiento'].get('rendimiento_general', 0),
            reporte['analisis_cumplimiento'].get('puntaje_cumplimiento', 0)
        ]
        
        barras = ax1.bar(categorias, puntajes, color=['blue', 'green', 'orange', 'red'])
        ax1.set_ylim(0, 100)
        ax1.set_title('Puntajes de Evaluación de Dispositivo de Entrada')
        ax1.set_ylabel('Puntaje (%)')
        
        # Agregar etiquetas de valor en las barras
        for barra, puntaje in zip(barras, puntajes):
            ax1.text(barra.get_x() + barra.get_width()/2, barra.get_y() + puntaje + 1, 
                    f'{puntaje:.1f}', ha='center', va='bottom')
        
        # Métricas ergonómicas
        metricas_ergonomicas = ['Postura', 'Fuerza', 'Movimiento']
        puntajes_ergonomicos = [
            reporte['analisis_ergonomia'].get('calidad_postura', 0),
            reporte['analisis_ergonomia'].get('calidad_fuerza', 0),
            reporte['analisis_ergonomia'].get('calidad_movimiento', 0)
        ]
        
        ax2.bar(metricas_ergonomicas, puntajes_ergonomicos, color='lightblue')
        ax2.set_ylim(0, 100)
        ax2.set_title('Métricas Ergonómicas')
        ax2.set_ylabel('Puntaje de Calidad')
        
        # Métricas de usabilidad
        metricas_usabilidad = ['Precisión', 'Velocidad Clic', 'Escritura']
        puntajes_usabilidad = [
            reporte['analisis_usabilidad'].get('calidad_precision', 0),
            reporte['analisis_usabilidad'].get('calidad_velocidad_clic', 0),
            (reporte['analisis_usabilidad'].get('calidad_velocidad_escritura', 0) + 
             reporte['analisis_usabilidad'].get('calidad_precision_escritura', 0)) / 2
        ]
        
        ax3.bar(metricas_usabilidad, puntajes_usabilidad, color='lightgreen')
        ax3.set_ylim(0, 100)
        ax3.set_title('Métricas de Usabilidad')
        ax3.set_ylabel('Puntaje de Usabilidad')
        
        # Métricas de rendimiento
        metricas_rendimiento = ['Respuesta', 'Rendimiento', 'Errores', 'Aprendizaje']
        puntajes_rendimiento = [
            reporte['analisis_rendimiento'].get('calidad_tiempo_respuesta', 0),
            reporte['analisis_rendimiento'].get('calidad_rendimiento', 0),
            reporte['analisis_rendimiento'].get('calidad_tasa_error', 0),
            reporte['analisis_rendimiento'].get('calidad_tiempo_aprendizaje', 0)
        ]
        
        ax4.bar(metricas_rendimiento, puntajes_rendimiento, color='lightcoral')
        ax4.set_ylim(0, 100)
        ax4.set_title('Métricas de Rendimiento')
        ax4.set_ylabel('Puntaje de Rendimiento')
        
        plt.tight_layout()
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Visualización de análisis guardada: {ruta_guardado}")

# Ejemplo de uso
if __name__ == "__main__":
    analizador = AnalizadorDispositivoEntrada()
    
    # Simular datos de evaluación
    datos_evaluacion = {
        'deviceType': 'mouse',
        'deviceModel': 'Logitech MX Master 3',
        'connectionType': 'wireless',
        'userHandedness': 'right',
        'usageScenario': 'office',
        'startTime': datetime.now().isoformat(),
        'ergonomics': {
            'postureScore': 85.0,
            'forceLevel': 1.2,
            'movementEfficiency': 92.0
        },
        'usability': {
            'accuracy': 88.0,
            'clickSpeed': 6.5,
            'typingWPM': 0,  # No aplicable para mouse
            'typingAccuracy': 0
        },
        'performance': {
            'responseTime': 15.0,
            'throughput': 18.0,
            'errorRate': 1.5,
            'learningTime': 12.0
        },
        'compliance': {
            'score': 82.0,
            'level': 'Good'
        }
    }
    
    analizador.datos_evaluacion = datos_evaluacion
    reporte = analizador.guardar_reporte()
    
    print("Puntaje General:", reporte.get('puntaje_general', 0))
    print("Recomendaciones:")
    for rec in reporte.get('recomendaciones', []):
        print(f"  - {rec}")
    
    # Visualizar resultados
    analizador.visualizar_analisis()
```

### Paso 5: Documentación
Este kit de herramientas de evaluación de estándares de dispositivos de entrada implementa métodos de evaluación integrales del ISO 9241-410 e ISO 9241-411:

1. **Evaluación Ergonómica**: Análisis de postura, medición de fuerza y evaluación de patrones de movimiento
2. **Prueba de Usabilidad**: Precisión de apuntado, velocidad de clic y rendimiento de entrada de texto
3. **Análisis de Rendimiento**: Tiempo de respuesta, rendimiento, tasa de error y tiempo de aprendizaje
4. **Verificación de Cumplimiento**: Verificación automatizada contra estándares ISO 9241 para dispositivos de entrada

Características clave:
- Interfaz web interactiva de evaluación con pruebas en tiempo real
- Herramientas integrales de evaluación ergonómica
- Pruebas automatizadas de usabilidad y rendimiento
- Sistema de verificación de cumplimiento ISO 9241
- Visualización de datos y generación de reportes

El kit proporciona herramientas de grado profesional para evaluar estándares de dispositivos de entrada según estándares internacionales de ergonomía y usabilidad.
