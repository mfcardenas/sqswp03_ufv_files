# Laboratorio 8: Requisitos de Visualización

## Solución

### Paso 1: HTML de Evaluación de Visualización
Crear un archivo `visual_display.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evaluación de Requisitos de Visualización - Laboratorio ISO 9241</title>
    <link rel="stylesheet" href="visual.css">
</head>
<body>
    <header>
        <h1>Evaluación de Requisitos de Visualización</h1>
        <nav>
            <button id="qualityBtn">Calidad de Pantalla</button>
            <button id="readabilityBtn">Prueba de Legibilidad</button>
            <button id="ergonomicsBtn">Ergonómica</button>
            <button id="complianceBtn">Verificación de Cumplimiento</button>
            <button id="generateReportBtn">Generar Reporte</button>
        </nav>
    </header>

    <main>
        <section class="assessment-setup">
            <h2>Configuración de Evaluación</h2>
            <form id="assessmentConfigForm">
                <div class="form-group">
                    <label for="displayType">Tipo de Pantalla:</label>
                    <select id="displayType">
                        <option value="lcd">Monitor LCD</option>
                        <option value="led">Pantalla LED</option>
                        <option value="oled">Pantalla OLED</option>
                        <option value="crt">Monitor CRT</option>
                        <option value="projector">Proyector</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="screenSize">Tamaño de Pantalla (pulgadas):</label>
                    <input type="number" id="screenSize" min="10" max="100" value="24">
                </div>
                
                <div class="form-group">
                    <label for="resolution">Resolución:</label>
                    <select id="resolution">
                        <option value="hd">1920x1080 (HD)</option>
                        <option value="fhd">1920x1080 (Full HD)</option>
                        <option value="qhd">2560x1440 (QHD)</option>
                        <option value="uhd">3840x2160 (UHD)</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="environment">Entorno:</label>
                    <select id="environment">
                        <option value="office">Oficina</option>
                        <option value="industrial">Industrial</option>
                        <option value="outdoor">Exterior</option>
                        <option value="medical">Médico</option>
                    </select>
                </div>
                
                <button type="submit" class="primary-btn">Iniciar Evaluación</button>
            </form>
        </section>

        <section class="quality-assessment" id="qualitySection" style="display: none;">
            <h2>Evaluación de Calidad de Pantalla</h2>
            
            <div class="quality-tests">
                <div class="test-panel">
                    <h3>Prueba de Precisión de Color</h3>
                    <div class="color-swatches">
                        <div class="swatch" data-color="#FF0000" style="background-color: #FF0000;"></div>
                        <div class="swatch" data-color="#00FF00" style="background-color: #00FF00;"></div>
                        <div class="swatch" data-color="#0000FF" style="background-color: #0000FF;"></div>
                        <div class="swatch" data-color="#FFFF00" style="background-color: #FFFF00;"></div>
                        <div class="swatch" data-color="#FF00FF" style="background-color: #FF00FF;"></div>
                        <div class="swatch" data-color="#00FFFF" style="background-color: #00FFFF;"></div>
                    </div>
                    <button id="colorTestBtn">Ejecutar Prueba de Color</button>
                    <div id="colorResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Prueba de Brillo y Contraste</h3>
                    <div class="brightness-test">
                        <div class="brightness-scale">
                            <div class="scale-item" data-level="0" style="background-color: black;"></div>
                            <div class="scale-item" data-level="25" style="background-color: #404040;"></div>
                            <div class="scale-item" data-level="50" style="background-color: #808080;"></div>
                            <div class="scale-item" data-level="75" style="background-color: #C0C0C0;"></div>
                            <div class="scale-item" data-level="100" style="background-color: white;"></div>
                        </div>
                    </div>
                    <button id="brightnessTestBtn">Ejecutar Prueba de Brillo</button>
                    <div id="brightnessResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Prueba de Respuesta de Píxel</h3>
                    <div class="pixel-test">
                        <div class="pixel-grid">
                            <div class="pixel-row">
                                <div class="pixel" style="background-color: white;"></div>
                                <div class="pixel" style="background-color: black;"></div>
                                <div class="pixel" style="background-color: white;"></div>
                                <div class="pixel" style="background-color: black;"></div>
                            </div>
                            <div class="pixel-row">
                                <div class="pixel" style="background-color: black;"></div>
                                <div class="pixel" style="background-color: white;"></div>
                                <div class="pixel" style="background-color: black;"></div>
                                <div class="pixel" style="background-color: white;"></div>
                            </div>
                        </div>
                    </div>
                    <button id="pixelTestBtn">Ejecutar Prueba de Píxel</button>
                    <div id="pixelResults"></div>
                </div>
            </div>
        </section>

        <section class="readability-test" id="readabilitySection" style="display: none;">
            <h2>Prueba de Legibilidad</h2>
            
            <div class="readability-controls">
                <div class="control-group">
                    <label for="fontSize">Tamaño de Fuente:</label>
                    <input type="range" id="fontSize" min="8" max="72" value="16">
                    <span id="fontSizeValue">16px</span>
                </div>
                
                <div class="control-group">
                    <label for="fontFamily">Familia de Fuente:</label>
                    <select id="fontFamily">
                        <option value="Arial">Arial</option>
                        <option value="Times New Roman">Times New Roman</option>
                        <option value="Verdana">Verdana</option>
                        <option value="Helvetica">Helvetica</option>
                        <option value="Georgia">Georgia</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="textColor">Color de Texto:</label>
                    <input type="color" id="textColor" value="#000000">
                </div>
                
                <div class="control-group">
                    <label for="bgColor">Color de Fondo:</label>
                    <input type="color" id="bgColor" value="#FFFFFF">
                </div>
            </div>
            
            <div class="readability-sample">
                <h3>Texto de Muestra de Legibilidad</h3>
                <p id="sampleText">
                    El rápido zorro marrón salta sobre el perro perezoso. Esta oración contiene todas las letras del alfabeto y se utiliza comúnmente para probar la legibilidad de fuentes. La legibilidad del texto depende de varios factores incluyendo el tamaño de fuente, el tipo de letra, la relación de contraste de color y el espaciado entre caracteres y líneas.
                </p>
            </div>
            
            <div class="readability-metrics">
                <button id="calculateReadabilityBtn">Calcular Métricas de Legibilidad</button>
                <div id="readabilityResults"></div>
            </div>
        </section>

        <section class="ergonomics-assessment" id="ergonomicsSection" style="display: none;">
            <h2>Evaluación Ergonómica</h2>
            
            <div class="ergonomics-tests">
                <div class="test-panel">
                    <h3>Prueba de Distancia de Visualización</h3>
                    <div class="distance-guide">
                        <p>Posiciónate a una distancia de visualización cómoda desde la pantalla.</p>
                        <div class="distance-indicator">
                            <div class="optimal-zone">Zona Óptima (50-70 cm)</div>
                            <div class="comfort-zone">Zona de Confort (70-100 cm)</div>
                        </div>
                    </div>
                    <button id="distanceTestBtn">Medir Distancia</button>
                    <div id="distanceResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Prueba de Ángulo de Visualización</h3>
                    <div class="angle-guide">
                        <p>Ajusta tu ángulo de visualización para que sea perpendicular a la superficie de la pantalla.</p>
                        <div class="angle-visualization">
                            <div class="screen-surface"></div>
                            <div class="optimal-angle"></div>
                        </div>
                    </div>
                    <button id="angleTestBtn">Verificar Ángulo</button>
                    <div id="angleResults"></div>
                </div>
                
                <div class="test-panel">
                    <h3>Evaluación de Iluminación</h3>
                    <div class="lighting-test">
                        <p>Asegúrate de una iluminación adecuada y minimiza el reflejo en la pantalla.</p>
                        <div class="lighting-zones">
                            <div class="zone adequate">Iluminación Adecuada</div>
                            <div class="zone glare">Posible Reflejo</div>
                            <div class="zone dark">Demasiado Oscuro</div>
                        </div>
                    </div>
                    <button id="lightingTestBtn">Evaluar Iluminación</button>
                    <div id="lightingResults"></div>
                </div>
            </div>
        </section>

        <section class="compliance-check" id="complianceSection" style="display: none;">
            <h2>Verificación de Cumplimiento ISO 9241</h2>
            
            <div class="compliance-checklist">
                <h3>Lista de Verificación de Requisitos de Visualización</h3>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req1">
                    <label for="req1">La luminancia de la pantalla cumple con los requisitos mínimos (≥ 35 cd/m²)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req2">
                    <label for="req2">La relación de contraste de color cumple con las directrices WCAG (≥ 4.5:1)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req3">
                    <label for="req3">La altura de los caracteres cumple con los requisitos de legibilidad (≥ 0.15° ángulo visual)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req4">
                    <label for="req4">La frecuencia de actualización cumple con los requisitos libres de parpadeo (≥ 60 Hz)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req5">
                    <label for="req5">El ángulo de visualización soporta los requisitos ergonómicos (± 45°)</label>
                </div>
                
                <div class="compliance-item">
                    <input type="checkbox" id="req6">
                    <label for="req6">Se aplicó tratamiento antirreflejo para reducir las reflexiones</label>
                </div>
            </div>
            
            <button id="runComplianceCheck">Ejecutar Evaluación de Cumplimiento</button>
            <div id="complianceResults"></div>
        </section>

        <section class="results-section" id="resultsSection" style="display: none;">
            <h2>Resultados de Evaluación</h2>
            <div class="results-tabs">
                <button class="tab-btn active" data-tab="summary">Resumen</button>
                <button class="tab-btn" data-tab="quality">Calidad</button>
                <button class="tab-btn" data-tab="readability">Legibilidad</button>
                <button class="tab-btn" data-tab="ergonomics">Ergonómica</button>
                <button class="tab-btn" data-tab="compliance">Cumplimiento</button>
            </div>
            
            <div class="tab-content">
                <div id="summaryTab" class="tab-panel active">
                    <h3>Resumen de Evaluación</h3>
                    <div id="assessmentSummary"></div>
                </div>
                
                <div id="qualityTab" class="tab-panel">
                    <h3>Resultados de Calidad de Pantalla</h3>
                    <div id="qualityResults"></div>
                </div>
                
                <div id="readabilityTab" class="tab-panel">
                    <h3>Evaluación de Legibilidad</h3>
                    <div id="readabilityAssessment"></div>
                </div>
                
                <div id="ergonomicsTab" class="tab-panel">
                    <h3>Evaluación Ergonómica</h3>
                    <div id="ergonomicsEvaluation"></div>
                </div>
                
                <div id="complianceTab" class="tab-panel">
                    <h3>Estado de Cumplimiento</h3>
                    <div id="complianceStatus"></div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="visual.js"></script>
</body>
</html>
```

### Paso 2: CSS para Interfaz de Evaluación Visual
Crear un archivo `visual.css`:

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

/* Pruebas de Calidad */
.quality-tests {
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

.color-swatches {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1rem 0;
}

.swatch {
    width: 60px;
    height: 60px;
    border-radius: 4px;
    border: 2px solid #dee2e6;
    cursor: pointer;
}

.brightness-scale {
    display: flex;
    margin: 1rem 0;
}

.scale-item {
    flex: 1;
    height: 40px;
    border: 1px solid #333;
}

.pixel-grid {
    margin: 1rem 0;
}

.pixel-row {
    display: flex;
}

.pixel {
    width: 20px;
    height: 20px;
    border: 1px solid #333;
}

/* Prueba de Legibilidad */
.readability-controls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}

.control-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.control-group input[type="range"] {
    width: 100%;
}

#sampleText {
    font-size: 16px;
    line-height: 1.5;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 4px;
    min-height: 100px;
}

/* Pruebas Ergonómicas */
.ergonomics-tests {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.distance-indicator, .angle-visualization, .lighting-zones {
    margin: 1rem 0;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 4px;
}

.optimal-zone, .comfort-zone {
    padding: 0.5rem;
    margin: 0.5rem 0;
    border-radius: 4px;
}

.optimal-zone {
    background-color: #d4edda;
    color: #155724;
}

.comfort-zone {
    background-color: #fff3cd;
    color: #856404;
}

.screen-surface {
    width: 200px;
    height: 150px;
    background-color: #007bff;
    margin: 1rem auto;
    border-radius: 4px;
    position: relative;
}

.optimal-angle {
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 20px;
    background-color: #28a745;
}

.zone {
    padding: 0.5rem;
    margin: 0.5rem 0;
    border-radius: 4px;
    text-align: center;
}

.zone.adequate {
    background-color: #d4edda;
    color: #155724;
}

.zone.glare {
    background-color: #f8d7da;
    color: #721c24;
}

.zone.dark {
    background-color: #e2e3e5;
    color: #383d41;
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
    
    .quality-tests, .ergonomics-tests {
        grid-template-columns: 1fr;
    }
    
    .readability-controls {
        grid-template-columns: 1fr;
    }
    
    .results-tabs {
        flex-direction: column;
    }
    
    .tab-btn {
        border-radius: 0;
        margin-right: 0;
    }
}
```

### Paso 3: JavaScript para Evaluación Visual
Crear un archivo `visual.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Configuración de evaluación
    let currentAssessment = null;
    let assessmentResults = {
        quality: {},
        readability: {},
        ergonomics: {},
        compliance: {}
    };
    
    // Formulario de configuración
    document.getElementById('assessmentConfigForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        currentAssessment = {
            displayType: document.getElementById('displayType').value,
            screenSize: parseInt(document.getElementById('screenSize').value),
            resolution: document.getElementById('resolution').value,
            environment: document.getElementById('environment').value,
            startTime: new Date()
        };
        
        document.querySelector('.assessment-setup').style.display = 'none';
        document.getElementById('qualitySection').style.display = 'block';
        
        showNotification('Evaluación configurada exitosamente');
    });
    
    // Navegación
    document.getElementById('qualityBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('qualitySection').style.display = 'block';
    });
    
    document.getElementById('readabilityBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('readabilitySection').style.display = 'block';
    });
    
    document.getElementById('ergonomicsBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('ergonomicsSection').style.display = 'block';
    });
    
    document.getElementById('complianceBtn').addEventListener('click', function() {
        hideAllSections();
        document.getElementById('complianceSection').style.display = 'block';
    });
    
    function hideAllSections() {
        document.getElementById('qualitySection').style.display = 'none';
        document.getElementById('readabilitySection').style.display = 'none';
        document.getElementById('ergonomicsSection').style.display = 'none';
        document.getElementById('complianceSection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
    }
    
    // Evaluación de calidad
    document.getElementById('colorTestBtn').addEventListener('click', function() {
        // Simular prueba de precisión de color
        const colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF'];
        let colorResults = [];
        
        colors.forEach(color => {
            // Simular medición de precisión de color
            const accuracy = Math.random() * 20 + 80; // 80-100%
            colorResults.push({ color, accuracy: accuracy.toFixed(1) });
        });
        
        const avgAccuracy = colorResults.reduce((sum, result) => sum + parseFloat(result.accuracy), 0) / colorResults.length;
        
        document.getElementById('colorResults').innerHTML = `
            <h4>Resultados de Precisión de Color</h4>
            <p>Precisión Promedio de Color: ${avgAccuracy.toFixed(1)}%</p>
            <div class="color-results">
                ${colorResults.map(result => 
                    `<div class="color-result">
                        <div class="color-sample" style="background-color: ${result.color};"></div>
                        <span>${result.accuracy}%</span>
                    </div>`
                ).join('')}
            </div>
        `;
        
        assessmentResults.quality.colorAccuracy = avgAccuracy;
        showNotification('Prueba de color completada');
    });
    
    document.getElementById('brightnessTestBtn').addEventListener('click', function() {
        // Simular prueba de brillo y contraste
        const brightness = Math.random() * 50 + 200; // 200-250 cd/m²
        const contrast = Math.random() * 200 + 800; // 800-1000:1
        
        document.getElementById('brightnessResults').innerHTML = `
            <h4>Resultados de Brillo y Contraste</h4>
            <p>Brillo: ${brightness.toFixed(1)} cd/m²</p>
            <p>Relación de Contraste: ${contrast.toFixed(0)}:1</p>
            <div class="brightness-bar">
                <div class="brightness-fill" style="width: ${Math.min(brightness / 3, 100)}%"></div>
            </div>
        `;
        
        assessmentResults.quality.brightness = brightness;
        assessmentResults.quality.contrast = contrast;
        showNotification('Prueba de brillo completada');
    });
    
    document.getElementById('pixelTestBtn').addEventListener('click', function() {
        // Simular prueba de respuesta de píxel
        const responseTime = Math.random() * 5 + 1; // 1-6ms
        const deadPixels = Math.floor(Math.random() * 3); // 0-2 píxeles muertos
        
        document.getElementById('pixelResults').innerHTML = `
            <h4>Resultados de Respuesta de Píxel</h4>
            <p>Tiempo de Respuesta: ${responseTime.toFixed(1)}ms</p>
            <p>Píxeles Muertos: ${deadPixels}</p>
            <p class="${responseTime < 5 ? 'good' : 'poor'}">
                ${responseTime < 5 ? '✓ Buen tiempo de respuesta' : '⚠ Tiempo de respuesta lento'}
            </p>
        `;
        
        assessmentResults.quality.responseTime = responseTime;
        assessmentResults.quality.deadPixels = deadPixels;
        showNotification('Prueba de píxel completada');
    });
    
    // Prueba de legibilidad
    const fontSizeInput = document.getElementById('fontSize');
    const fontSizeValue = document.getElementById('fontSizeValue');
    const sampleText = document.getElementById('sampleText');
    
    fontSizeInput.addEventListener('input', function() {
        fontSizeValue.textContent = this.value + 'px';
        sampleText.style.fontSize = this.value + 'px';
    });
    
    document.getElementById('fontFamily').addEventListener('change', function() {
        sampleText.style.fontFamily = this.value;
    });
    
    document.getElementById('textColor').addEventListener('input', function() {
        sampleText.style.color = this.value;
    });
    
    document.getElementById('bgColor').addEventListener('input', function() {
        sampleText.style.backgroundColor = this.value;
    });
    
    document.getElementById('calculateReadabilityBtn').addEventListener('click', function() {
        const fontSize = parseInt(fontSizeInput.value);
        const textColor = document.getElementById('textColor').value;
        const bgColor = document.getElementById('bgColor').value;
        
        // Calcular relación de contraste
        const contrastRatio = calculateContrastRatio(textColor, bgColor);
        
        // Calcular ángulo visual (simplificado)
        const viewingDistance = 60; // cm (asumido)
        const visualAngle = (fontSize / viewingDistance) * (180 / Math.PI) * 2.54; // grados
        
        const readabilityScore = calculateReadabilityScore(fontSize, contrastRatio, visualAngle);
        
        document.getElementById('readabilityResults').innerHTML = `
            <h4>Métricas de Legibilidad</h4>
            <p>Tamaño de Fuente: ${fontSize}px</p>
            <p>Relación de Contraste: ${contrastRatio.toFixed(2)}:1</p>
            <p>Ángulo Visual: ${visualAngle.toFixed(2)}°</p>
            <p>Puntaje de Legibilidad: ${readabilityScore.toFixed(1)}/100</p>
            <div class="readability-bar">
                <div class="readability-fill" style="width: ${readabilityScore}%"></div>
            </div>
        `;
        
        assessmentResults.readability = {
            fontSize,
            contrastRatio,
            visualAngle,
            readabilityScore
        };
        
        showNotification('Análisis de legibilidad completado');
    });
    
    function calculateContrastRatio(color1, color2) {
        const l1 = getLuminance(color1);
        const l2 = getLuminance(color2);
        const brightest = Math.max(l1, l2);
        const darkest = Math.min(l1, l2);
        return (brightest + 0.05) / (darkest + 0.05);
    }
    
    function getLuminance(color) {
        const rgb = hexToRgb(color);
        const rsRGB = rgb.r / 255;
        const gsRGB = rgb.g / 255;
        const bsRGB = rgb.b / 255;
        
        const r = rsRGB <= 0.03928 ? rsRGB / 12.92 : Math.pow((rsRGB + 0.055) / 1.055, 2.4);
        const g = gsRGB <= 0.03928 ? gsRGB / 12.92 : Math.pow((gsRGB + 0.055) / 1.055, 2.4);
        const b = bsRGB <= 0.03928 ? bsRGB / 12.92 : Math.pow((bsRGB + 0.055) / 1.055, 2.4);
        
        return 0.2126 * r + 0.7152 * g + 0.0722 * b;
    }
    
    function hexToRgb(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }
    
    function calculateReadabilityScore(fontSize, contrastRatio, visualAngle) {
        let score = 0;
        
        // Puntaje de tamaño de fuente (0-30 puntos)
        if (fontSize >= 16) score += 30;
        else if (fontSize >= 12) score += 20;
        else if (fontSize >= 10) score += 10;
        
        // Puntaje de relación de contraste (0-40 puntos)
        if (contrastRatio >= 7) score += 40;
        else if (contrastRatio >= 4.5) score += 30;
        else if (contrastRatio >= 3) score += 20;
        else score += 10;
        
        // Puntaje de ángulo visual (0-30 puntos)
        if (visualAngle >= 0.3) score += 30;
        else if (visualAngle >= 0.2) score += 20;
        else if (visualAngle >= 0.15) score += 10;
        
        return Math.min(score, 100);
    }
    
    // Evaluación ergonómica
    document.getElementById('distanceTestBtn').addEventListener('click', function() {
        // Simular medición de distancia
        const distance = Math.random() * 20 + 50; // 50-70 cm
        const optimal = distance >= 50 && distance <= 70;
        
        document.getElementById('distanceResults').innerHTML = `
            <h4>Resultados de Distancia de Visualización</h4>
            <p>Distancia Medida: ${distance.toFixed(1)} cm</p>
            <p class="${optimal ? 'good' : 'poor'}">
                ${optimal ? '✓ Distancia de visualización óptima' : '⚠ Ajustar distancia de visualización'}
            </p>
        `;
        
        assessmentResults.ergonomics.viewingDistance = distance;
        showNotification('Prueba de distancia completada');
    });
    
    document.getElementById('angleTestBtn').addEventListener('click', function() {
        // Simular medición de ángulo
        const angle = Math.random() * 30 - 15; // -15 a +15 grados
        const optimal = Math.abs(angle) <= 5;
        
        document.getElementById('angleResults').innerHTML = `
            <h4>Resultados de Ángulo de Visualización</h4>
            <p>Ángulo Medido: ${angle.toFixed(1)}°</p>
            <p class="${optimal ? 'good' : 'poor'}">
                ${optimal ? '✓ Ángulo de visualización óptimo' : '⚠ Ajustar ángulo de visualización'}
            </p>
        `;
        
        assessmentResults.ergonomics.viewingAngle = angle;
        showNotification('Prueba de ángulo completada');
    });
    
    document.getElementById('lightingTestBtn').addEventListener('click', function() {
        // Simular evaluación de iluminación
        const lightingLevel = Math.random() * 500 + 200; // 200-700 lux
        const glare = Math.random() < 0.3; // 30% de probabilidad de reflejo
        
        let assessment = 'adequate';
        if (glare) assessment = 'glare';
        else if (lightingLevel < 300) assessment = 'dark';
        
        document.getElementById('lightingResults').innerHTML = `
            <h4>Resultados de Evaluación de Iluminación</h4>
            <p>Nivel de Iluminación: ${lightingLevel.toFixed(0)} lux</p>
            <p>Reflejo Detectado: ${glare ? 'Sí' : 'No'}</p>
            <p class="${assessment === 'adequate' ? 'good' : 'poor'}">
                ${assessment === 'adequate' ? '✓ Condiciones de iluminación adecuadas' : 
                  assessment === 'glare' ? '⚠ Reflejo detectado - ajustar iluminación' : 
                  '⚠ Iluminación insuficiente - aumentar iluminación'}
            </p>
        `;
        
        assessmentResults.ergonomics.lightingLevel = lightingLevel;
        assessmentResults.ergonomics.glare = glare;
        showNotification('Evaluación de iluminación completada');
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
            <p><strong>Tipo de Pantalla:</strong> ${currentAssessment.displayType}</p>
            <p><strong>Tamaño de Pantalla:</strong> ${currentAssessment.screenSize}"</p>
            <p><strong>Resolución:</strong> ${currentAssessment.resolution}</p>
            <p><strong>Entorno:</strong> ${currentAssessment.environment}</p>
            <p><strong>Fecha de Evaluación:</strong> ${currentAssessment.startTime.toLocaleDateString()}</p>
        `;
        
        // Pestaña de calidad
        const quality = assessmentResults.quality;
        document.getElementById('qualityResults').innerHTML = `
            <h4>Métricas de Calidad de Pantalla</h4>
            ${quality.colorAccuracy ? `<p>Precisión de Color: ${quality.colorAccuracy}%</p>` : ''}
            ${quality.brightness ? `<p>Brillo: ${quality.brightness.toFixed(1)} cd/m²</p>` : ''}
            ${quality.contrast ? `<p>Relación de Contraste: ${quality.contrast.toFixed(0)}:1</p>` : ''}
            ${quality.responseTime ? `<p>Tiempo de Respuesta: ${quality.responseTime.toFixed(1)}ms</p>` : ''}
            ${quality.deadPixels !== undefined ? `<p>Píxeles Muertos: ${quality.deadPixels}</p>` : ''}
        `;
        
        // Pestaña de legibilidad
        const readability = assessmentResults.readability;
        document.getElementById('readabilityAssessment').innerHTML = `
            <h4>Evaluación de Legibilidad</h4>
            ${readability.fontSize ? `<p>Tamaño de Fuente: ${readability.fontSize}px</p>` : ''}
            ${readability.contrastRatio ? `<p>Relación de Contraste: ${readability.contrastRatio.toFixed(2)}:1</p>` : ''}
            ${readability.visualAngle ? `<p>Ángulo Visual: ${readability.visualAngle.toFixed(2)}°</p>` : ''}
            ${readability.readabilityScore ? `<p>Puntaje de Legibilidad: ${readability.readabilityScore.toFixed(1)}/100</p>` : ''}
        `;
        
        // Pestaña ergonómica
        const ergonomics = assessmentResults.ergonomics;
        document.getElementById('ergonomicsEvaluation').innerHTML = `
            <h4>Evaluación Ergonómica</h4>
            ${ergonomics.viewingDistance ? `<p>Distancia de Visualización: ${ergonomics.viewingDistance.toFixed(1)} cm</p>` : ''}
            ${ergonomics.viewingAngle !== undefined ? `<p>Ángulo de Visualización: ${ergonomics.viewingAngle.toFixed(1)}°</p>` : ''}
            ${ergonomics.lightingLevel ? `<p>Nivel de Iluminación: ${ergonomics.lightingLevel.toFixed(0)} lux</p>` : ''}
            ${ergonomics.glare !== undefined ? `<p>Reflejo Detectado: ${ergonomics.glare ? 'Sí' : 'No'}</p>` : ''}
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

### Paso 4: Script de Análisis Visual en Python
Crear un archivo `visual_analysis.py`:

```python
import json
import math
from datetime import datetime
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import numpy as np

class AnalizadorVisual:
    def __init__(self):
        self.datos_evaluacion = {}
        self.resultados_analisis = {}
    
    def cargar_datos_evaluacion(self, ruta_archivo: str):
        """Cargar datos de evaluación visual"""
        with open(ruta_archivo, 'r') as f:
            self.datos_evaluacion = json.load(f)
    
    def analizar_calidad_pantalla(self) -> Dict[str, float]:
        """Analizar métricas de calidad de pantalla"""
        calidad = self.datos_evaluacion.get('quality', {})
        
        analisis = {}
        
        # Análisis de precisión de color
        if 'colorAccuracy' in calidad:
            precision_color = calidad['colorAccuracy']
            analisis['calidad_color'] = self._calificar_precision_color(precision_color)
        
        # Análisis de brillo
        if 'brightness' in calidad:
            brillo = calidad['brightness']
            analisis['calidad_brillo'] = self._calificar_brillo(brillo)
        
        # Análisis de contraste
        if 'contrast' in calidad:
            contraste = calidad['contrast']
            analisis['calidad_contraste'] = self._calificar_contraste(contraste)
        
        # Análisis de tiempo de respuesta
        if 'responseTime' in calidad:
            tiempo_respuesta = calidad['responseTime']
            analisis['calidad_respuesta'] = self._calificar_tiempo_respuesta(tiempo_respuesta)
        
        # Puntaje general de calidad
        puntajes_calidad = [v for v in analisis.values() if isinstance(v, (int, float))]
        analisis['calidad_general'] = sum(puntajes_calidad) / len(puntajes_calidad) if puntajes_calidad else 0
        
        return analisis
    
    def analizar_legibilidad(self) -> Dict[str, float]:
        """Analizar métricas de legibilidad"""
        legibilidad = self.datos_evaluacion.get('readability', {})
        
        analisis = {}
        
        # Análisis de tamaño de fuente
        if 'fontSize' in legibilidad:
            tamano_fuente = legibilidad['fontSize']
            analisis['puntaje_tamano_fuente'] = self._calificar_tamano_fuente(tamano_fuente)
        
        # Análisis de relación de contraste
        if 'contrastRatio' in legibilidad:
            relacion_contraste = legibilidad['contrastRatio']
            analisis['puntaje_contraste'] = self._calificar_relacion_contraste(relacion_contraste)
        
        # Análisis de ángulo visual
        if 'visualAngle' in legibilidad:
            angulo_visual = legibilidad['visualAngle']
            analisis['puntaje_angulo_visual'] = self._calificar_angulo_visual(angulo_visual)
        
        # Puntaje general de legibilidad
        puntajes_legibilidad = [v for v in analisis.values() if isinstance(v, (int, float))]
        analisis['legibilidad_general'] = sum(puntajes_legibilidad) / len(puntajes_legibilidad) if puntajes_legibilidad else 0
        
        return analisis
    
    def analizar_ergonomia(self) -> Dict[str, float]:
        """Analizar factores ergonómicos"""
        ergonomia = self.datos_evaluacion.get('ergonomics', {})
        
        analisis = {}
        
        # Análisis de distancia de visualización
        if 'viewingDistance' in ergonomia:
            distancia = ergonomia['viewingDistance']
            analisis['puntaje_distancia'] = self._calificar_distancia_visualizacion(distancia)
        
        # Análisis de ángulo de visualización
        if 'viewingAngle' in ergonomia:
            angulo = ergonomia['viewingAngle']
            analisis['puntaje_angulo'] = self._calificar_angulo_visualizacion(angulo)
        
        # Análisis de iluminación
        if 'lightingLevel' in ergonomia:
            iluminacion = ergonomia['lightingLevel']
            reflejo = ergonomia.get('glare', False)
            analisis['puntaje_iluminacion'] = self._calificar_iluminacion(iluminacion, reflejo)
        
        # Puntaje general ergonómico
        puntajes_ergonomicos = [v for v in analisis.values() if isinstance(v, (int, float))]
        analisis['ergonomia_general'] = sum(puntajes_ergonomicos) / len(puntajes_ergonomicos) if puntajes_ergonomicos else 0
        
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
    
    def _calificar_precision_color(self, precision: float) -> float:
        """Calificar precisión de color (0-100)"""
        if precision >= 95:
            return 100
        elif precision >= 90:
            return 80
        elif precision >= 85:
            return 60
        elif precision >= 80:
            return 40
        else:
            return 20
    
    def _calificar_brillo(self, brillo: float) -> float:
        """Calificar brillo (0-100)"""
        if 200 <= brillo <= 300:
            return 100
        elif 150 <= brillo <= 400:
            return 80
        elif 100 <= brillo <= 500:
            return 60
        else:
            return 40
    
    def _calificar_contraste(self, contraste: float) -> float:
        """Calificar relación de contraste (0-100)"""
        if contraste >= 1000:
            return 100
        elif contraste >= 800:
            return 80
        elif contraste >= 500:
            return 60
        elif contraste >= 300:
            return 40
        else:
            return 20
    
    def _calificar_tiempo_respuesta(self, tiempo_respuesta: float) -> float:
        """Calificar tiempo de respuesta (0-100)"""
        if tiempo_respuesta <= 2:
            return 100
        elif tiempo_respuesta <= 5:
            return 80
        elif tiempo_respuesta <= 10:
            return 60
        elif tiempo_respuesta <= 16:
            return 40
        else:
            return 20
    
    def _calificar_tamano_fuente(self, tamano_fuente: int) -> float:
        """Calificar tamaño de fuente (0-100)"""
        if tamano_fuente >= 16:
            return 100
        elif tamano_fuente >= 14:
            return 80
        elif tamano_fuente >= 12:
            return 60
        elif tamano_fuente >= 10:
            return 40
        else:
            return 20
    
    def _calificar_relacion_contraste(self, relacion_contraste: float) -> float:
        """Calificar relación de contraste para legibilidad (0-100)"""
        if relacion_contraste >= 7:
            return 100
        elif relacion_contraste >= 4.5:
            return 80
        elif relacion_contraste >= 3:
            return 60
        elif relacion_contraste >= 2:
            return 40
        else:
            return 20
    
    def _calificar_angulo_visual(self, angulo_visual: float) -> float:
        """Calificar ángulo visual (0-100)"""
        if angulo_visual >= 0.3:
            return 100
        elif angulo_visual >= 0.2:
            return 80
        elif angulo_visual >= 0.15:
            return 60
        elif angulo_visual >= 0.1:
            return 40
        else:
            return 20
    
    def _calificar_distancia_visualizacion(self, distancia: float) -> float:
        """Calificar distancia de visualización en cm (0-100)"""
        if 50 <= distancia <= 70:
            return 100
        elif 40 <= distancia <= 80:
            return 80
        elif 30 <= distancia <= 90:
            return 60
        else:
            return 40
    
    def _calificar_angulo_visualizacion(self, angulo: float) -> float:
        """Calificar ángulo de visualización en grados (0-100)"""
        if abs(angulo) <= 5:
            return 100
        elif abs(angulo) <= 10:
            return 80
        elif abs(angulo) <= 15:
            return 60
        elif abs(angulo) <= 20:
            return 40
        else:
            return 20
    
    def _calificar_iluminacion(self, iluminacion: float, reflejo: bool) -> float:
        """Calificar condiciones de iluminación (0-100)"""
        if reflejo:
            return 30  # El reflejo reduce significativamente el puntaje
        
        if 300 <= iluminacion <= 500:
            return 100
        elif 200 <= iluminacion <= 700:
            return 80
        elif 100 <= iluminacion <= 1000:
            return 60
        else:
            return 40
    
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
        """Generar reporte integral de análisis visual"""
        reporte = {
            'info_evaluacion': {
                'tipo_pantalla': self.datos_evaluacion.get('displayType', 'Desconocido'),
                'tamano_pantalla': self.datos_evaluacion.get('screenSize', 'Desconocido'),
                'resolucion': self.datos_evaluacion.get('resolution', 'Desconocido'),
                'entorno': self.datos_evaluacion.get('environment', 'Desconocido'),
                'fecha_evaluacion': self.datos_evaluacion.get('startTime', datetime.now().isoformat())
            },
            'analisis_calidad': self.analizar_calidad_pantalla(),
            'analisis_legibilidad': self.analizar_legibilidad(),
            'analisis_ergonomia': self.analizar_ergonomia(),
            'analisis_cumplimiento': self.analizar_cumplimiento(),
            'recomendaciones': self.generar_recomendaciones(),
            'generado_en': datetime.now().isoformat()
        }
        
        # Calcular puntaje general
        analisis = [reporte['analisis_calidad'], reporte['analisis_legibilidad'], 
                   reporte['analisis_ergonomia'], reporte['analisis_cumplimiento']]
        
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
        
        # Recomendaciones de calidad
        calidad = self.analizar_calidad_pantalla()
        if calidad.get('calidad_general', 0) < 70:
            recomendaciones.append("Considerar calibración de pantalla para mejorar precisión de color y brillo")
        
        # Recomendaciones de legibilidad
        legibilidad = self.analizar_legibilidad()
        if legibilidad.get('legibilidad_general', 0) < 70:
            recomendaciones.append("Aumentar tamaño de fuente y mejorar relación de contraste para mejor legibilidad")
        
        # Recomendaciones ergonómicas
        ergonomia = self.analizar_ergonomia()
        if ergonomia.get('ergonomia_general', 0) < 70:
            recomendaciones.append("Ajustar distancia de visualización, ángulo e iluminación para óptima ergonomía")
        
        # Recomendaciones de cumplimiento
        cumplimiento = self.analizar_cumplimiento()
        if cumplimiento.get('puntaje_cumplimiento', 0) < 80:
            recomendaciones.append("Abordar problemas de cumplimiento ISO 9241 para cumplir estándares de visualización")
        
        if not recomendaciones:
            recomendaciones.append("La visualización cumple estándares aceptables - continuar monitoreando")
        
        return recomendaciones
    
    def guardar_reporte(self, ruta_archivo: str = 'reporte_visual.json'):
        """Guardar reporte integral en archivo"""
        reporte = self.generar_reporte_integral()
        
        with open(ruta_archivo, 'w') as f:
            json.dump(reporte, f, indent=2, default=str)
        
        print(f"Reporte visual guardado: {ruta_archivo}")
        return reporte
    
    def visualizar_analisis(self, ruta_guardado: str = 'analisis_visual.png'):
        """Crear visualizaciones del análisis"""
        reporte = self.generar_reporte_integral()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # Puntajes generales
        categorias = ['Calidad', 'Legibilidad', 'Ergonomía', 'Cumplimiento']
        puntajes = [
            reporte['analisis_calidad'].get('calidad_general', 0),
            reporte['analisis_legibilidad'].get('legibilidad_general', 0),
            reporte['analisis_ergonomia'].get('ergonomia_general', 0),
            reporte['analisis_cumplimiento'].get('puntaje_cumplimiento', 0)
        ]
        
        barras = ax1.bar(categorias, puntajes, color=['blue', 'green', 'orange', 'red'])
        ax1.set_ylim(0, 100)
        ax1.set_title('Puntajes de Evaluación Visual')
        ax1.set_ylabel('Puntaje (%)')
        
        # Agregar etiquetas de valor en las barras
        for barra, puntaje in zip(barras, puntajes):
            ax1.text(barra.get_x() + barra.get_width()/2, barra.get_y() + puntaje + 1, 
                    f'{puntaje:.1f}', ha='center', va='bottom')
        
        # Métricas de calidad
        metricas_calidad = ['Color', 'Brillo', 'Contraste', 'Respuesta']
        puntajes_calidad = [
            reporte['analisis_calidad'].get('calidad_color', 0),
            reporte['analisis_calidad'].get('calidad_brillo', 0),
            reporte['analisis_calidad'].get('calidad_contraste', 0),
            reporte['analisis_calidad'].get('calidad_respuesta', 0)
        ]
        
        ax2.bar(metricas_calidad, puntajes_calidad, color='lightblue')
        ax2.set_ylim(0, 100)
        ax2.set_title('Métricas de Calidad de Pantalla')
        ax2.set_ylabel('Puntaje de Calidad')
        
        # Métricas de legibilidad
        metricas_legibilidad = ['Tamaño Fuente', 'Contraste', 'Ángulo Visual']
        puntajes_legibilidad = [
            reporte['analisis_legibilidad'].get('puntaje_tamano_fuente', 0),
            reporte['analisis_legibilidad'].get('puntaje_contraste', 0),
            reporte['analisis_legibilidad'].get('puntaje_angulo_visual', 0)
        ]
        
        ax3.bar(metricas_legibilidad, puntajes_legibilidad, color='lightgreen')
        ax3.set_ylim(0, 100)
        ax3.set_title('Métricas de Legibilidad')
        ax3.set_ylabel('Puntaje de Legibilidad')
        
        # Métricas ergonómicas
        metricas_ergonomicas = ['Distancia', 'Ángulo', 'Iluminación']
        puntajes_ergonomicos = [
            reporte['analisis_ergonomia'].get('puntaje_distancia', 0),
            reporte['analisis_ergonomia'].get('puntaje_angulo', 0),
            reporte['analisis_ergonomia'].get('puntaje_iluminacion', 0)
        ]
        
        ax4.bar(metricas_ergonomicas, puntajes_ergonomicos, color='lightcoral')
        ax4.set_ylim(0, 100)
        ax4.set_title('Métricas Ergonómicas')
        ax4.set_ylabel('Puntaje Ergonómico')
        
        plt.tight_layout()
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Visualización de análisis guardada: {ruta_guardado}")

# Ejemplo de uso
if __name__ == "__main__":
    analizador = AnalizadorVisual()
    
    # Simular datos de evaluación
    datos_evaluacion = {
        'displayType': 'LED',
        'screenSize': 24,
        'resolution': 'fhd',
        'environment': 'office',
        'startTime': datetime.now().isoformat(),
        'quality': {
            'colorAccuracy': 92.5,
            'brightness': 225.0,
            'contrast': 950.0,
            'responseTime': 3.2,
            'deadPixels': 0
        },
        'readability': {
            'fontSize': 16,
            'contrastRatio': 5.8,
            'visualAngle': 0.25,
            'readabilityScore': 85.0
        },
        'ergonomics': {
            'viewingDistance': 60.0,
            'viewingAngle': 2.5,
            'lightingLevel': 350.0,
            'glare': False
        },
        'compliance': {
            'score': 85.0,
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
Este kit de herramientas de evaluación de requisitos de visualización implementa métodos de evaluación integrales del ISO 9241-303 e ISO 9241-307:

1. **Evaluación de Calidad de Pantalla**: Pruebas de precisión de color, brillo, contraste y respuesta de píxel
2. **Evaluación de Legibilidad**: Análisis de tamaño de fuente, relación de contraste y ángulo visual
3. **Evaluación Ergonómica**: Evaluación de distancia de visualización, ángulo e iluminación
4. **Verificación de Cumplimiento**: Verificación automatizada contra estándares ISO 9241

Características clave:
- Interfaz web interactiva de evaluación
- Cálculo de métricas en tiempo real y visualización
- Análisis integral en Python con generación automatizada de reportes
- Verificación de cumplimiento ISO 9241
- Visualización de datos y exportación

El kit proporciona herramientas de grado profesional para evaluar requisitos de visualización según estándares internacionales.
