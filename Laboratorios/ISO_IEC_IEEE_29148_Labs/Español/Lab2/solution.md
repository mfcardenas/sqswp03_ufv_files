# Laboratorio 2: Técnicas de Elicitación de Requisitos

## Solución

### Paso 1: Dashboard Interactivo de Elicitación
Crear un archivo `elicitation_dashboard.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Técnicas de Elicitación de Requisitos</title>
    <link rel="stylesheet" href="elicitation_styles.css">
</head>
<body>
    <header>
        <h1>Técnicas de Elicitación de Requisitos</h1>
        <nav>
            <button id="interviewsBtn">Entrevistas</button>
            <button id="questionnairesBtn">Cuestionarios</button>
            <button id="observationBtn">Observación</button>
            <button id="documentsBtn">Análisis de Documentos</button>
            <button id="prototypingBtn">Prototipado</button>
            <button id="integrationBtn">Integración de Técnicas</button>
        </nav>
    </header>

    <main>
        <section class="interviews" id="interviewsSection">
            <h2>Sistema de Gestión de Entrevistas</h2>
            
            <div class="interview-tools">
                <h3>Planificación y Ejecución de Entrevistas</h3>
                
                <div class="interview-setup">
                    <h4>Configuración de Entrevista</h4>
                    <form id="interviewSetupForm">
                        <div class="form-group">
                            <label for="intervieweeName">Nombre del Entrevistado:</label>
                            <input type="text" id="intervieweeName" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="intervieweeRole">Rol:</label>
                            <input type="text" id="intervieweeRole" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="interviewType">Tipo de Entrevista:</label>
                            <select id="interviewType">
                                <option value="structured">Estructurada</option>
                                <option value="semi-structured">Semi-Estructurada</option>
                                <option value="unstructured">No Estructurada</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="interviewTopic">Tema Principal:</label>
                            <input type="text" id="interviewTopic" required>
                        </div>
                        
                        <button type="submit">Iniciar Entrevista</button>
                    </form>
                </div>
                
                <div class="question-generator">
                    <h4>Generador de Preguntas</h4>
                    <div class="question-controls">
                        <select id="questionCategory">
                            <option value="functional">Requisitos Funcionales</option>
                            <option value="non-functional">Requisitos No Funcionales</option>
                            <option value="constraints">Restricciones y Limitaciones</option>
                            <option value="stakeholder">Preocupaciones de Interesados</option>
                        </select>
                        <button id="generateQuestions">Generar Preguntas</button>
                    </div>
                    
                    <div class="questions-list" id="questionsList">
                        <p>Haz clic en "Generar Preguntas" para crear preguntas de entrevista</p>
                    </div>
                </div>
                
                <div class="response-recorder">
                    <h4>Grabación de Respuestas</h4>
                    <div class="recording-controls">
                        <button id="startRecording">Iniciar Grabación</button>
                        <button id="stopRecording">Detener Grabación</button>
                        <button id="saveResponse">Guardar Respuesta</button>
                    </div>
                    
                    <div class="response-text">
                        <textarea id="responseText" placeholder="Registra las respuestas del entrevistado aquí..."></textarea>
                    </div>
                    
                    <div class="response-analysis">
                        <h5>Análisis de Respuesta</h5>
                        <div class="analysis-results" id="responseAnalysis">
                            <p>Los resultados del análisis aparecerán aquí</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="questionnaires" id="questionnairesSection" style="display: none;">
            <h2>Constructor y Análisis de Cuestionarios</h2>
            
            <div class="questionnaire-tools">
                <h3>Diseño y Distribución de Encuestas</h3>
                
                <div class="survey-builder">
                    <h4>Constructor de Encuestas</h4>
                    <div class="survey-form">
                        <div class="form-group">
                            <label for="surveyTitle">Título de la Encuesta:</label>
                            <input type="text" id="surveyTitle" placeholder="Ingresa el título de la encuesta">
                        </div>
                        
                        <div class="form-group">
                            <label for="surveyDescription">Descripción:</label>
                            <textarea id="surveyDescription" placeholder="Describe el propósito de esta encuesta"></textarea>
                        </div>
                        
                        <div class="question-builder">
                            <h5>Agregar Pregunta</h5>
                            <select id="questionType">
                                <option value="multiple-choice">Opción Múltiple</option>
                                <option value="rating">Escala de Calificación</option>
                                <option value="open-ended">Pregunta Abierta</option>
                                <option value="yes-no">Sí/No</option>
                            </select>
                            <input type="text" id="questionText" placeholder="Ingresa el texto de la pregunta">
                            <button id="addQuestion">Agregar Pregunta</button>
                        </div>
                        
                        <div class="survey-preview" id="surveyPreview">
                            <h5>Vista Previa de la Encuesta</h5>
                            <div id="previewContent"></div>
                        </div>
                    </div>
                </div>
                
                <div class="response-collection">
                    <h4>Recolección de Respuestas</h4>
                    <div class="collection-tools">
                        <button id="generateSurveyLink">Generar Enlace de Encuesta</button>
                        <button id="exportSurvey">Exportar Encuesta</button>
                        <div class="survey-link" id="surveyLink" style="display: none;">
                            <p>Enlace de Encuesta: <span id="linkText"></span></p>
                            <button id="copyLink">Copiar Enlace</button>
                        </div>
                    </div>
                </div>
                
                <div class="response-analysis">
                    <h4>Análisis de Respuestas</h4>
                    <div class="analysis-tools">
                        <button id="loadResponses">Cargar Respuestas de Ejemplo</button>
                        <button id="analyzeResponses">Analizar Respuestas</button>
                        <div class="analysis-results" id="surveyAnalysis">
                            <p>Los resultados del análisis aparecerán aquí</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="observation" id="observationSection" style="display: none;">
            <h2>Observación e Investigación Contextual</h2>
            
            <div class="observation-tools">
                <h3>Sistema de Observación de Actividades</h3>
                
                <div class="observation-setup">
                    <h4>Configuración de Sesión de Observación</h4>
                    <form id="observationSetupForm">
                        <div class="form-group">
                            <label for="observationContext">Contexto:</label>
                            <input type="text" id="observationContext" placeholder="ej. Flujo de trabajo diario, Interacción con clientes">
                        </div>
                        
                        <div class="form-group">
                            <label for="observationDuration">Duración (minutos):</label>
                            <input type="number" id="observationDuration" min="15" max="480">
                        </div>
                        
                        <div class="form-group">
                            <label for="observationType">Tipo de Observación:</label>
                            <select id="observationType">
                                <option value="passive">Observación Pasiva</option>
                                <option value="active">Participación Activa</option>
                                <option value="contextual">Investigación Contextual</option>
                            </select>
                        </div>
                        
                        <button type="submit">Iniciar Observación</button>
                    </form>
                </div>
                
                <div class="activity-logger">
                    <h4>Registrador de Actividades</h4>
                    <div class="logging-controls">
                        <button id="startLogging">Iniciar Registro</button>
                        <button id="pauseLogging">Pausar/Reanudar</button>
                        <button id="stopLogging">Detener Registro</button>
                    </div>
                    
                    <div class="activity-entry">
                        <input type="text" id="activityDescription" placeholder="Describe la actividad observada">
                        <select id="activityCategory">
                            <option value="task">Ejecución de Tarea</option>
                            <option value="communication">Comunicación</option>
                            <option value="decision">Toma de Decisiones</option>
                            <option value="problem">Resolución de Problemas</option>
                            <option value="waiting">Espera/Tiempo Inactivo</option>
                        </select>
                        <button id="logActivity">Registrar Actividad</button>
                    </div>
                    
                    <div class="activity-timeline" id="activityTimeline">
                        <h5>Línea de Tiempo de Actividades</h5>
                        <div id="timelineContent"></div>
                    </div>
                </div>
                
                <div class="workflow-analysis">
                    <h4>Análisis de Flujo de Trabajo</h4>
                    <div class="analysis-tools">
                        <button id="analyzeWorkflow">Analizar Flujo de Trabajo</button>
                        <button id="identifyBottlenecks">Identificar Cuellos de Botella</button>
                        <div class="workflow-results" id="workflowResults">
                            <p>Los resultados del análisis de flujo de trabajo aparecerán aquí</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="documents" id="documentsSection" style="display: none;">
            <h2>Sistema de Análisis de Documentos</h2>
            
            <div class="document-tools">
                <h3>Extracción de Requisitos de Documentos</h3>
                
                <div class="document-upload">
                    <h4>Carga de Documentos</h4>
                    <div class="upload-area">
                        <input type="file" id="documentFile" multiple accept=".pdf,.doc,.docx,.txt">
                        <div class="upload-prompt">
                            <p>Arrastra y suelta documentos aquí o haz clic para buscar</p>
                            <button id="browseFiles">Buscar Archivos</button>
                        </div>
                    </div>
                    
                    <div class="uploaded-documents" id="uploadedDocuments">
                        <h5>Documentos Cargados</h5>
                        <div id="documentList"></div>
                    </div>
                </div>
                
                <div class="requirements-extraction">
                    <h4>Extracción de Requisitos</h4>
                    <div class="extraction-controls">
                        <button id="extractRequirements">Extraer Requisitos</button>
                        <button id="analyzeGaps">Analizar Brechas</button>
                        <button id="consolidateRequirements">Consolidar Requisitos</button>
                    </div>
                    
                    <div class="extraction-results" id="extractionResults">
                        <h5>Resultados de Extracción</h5>
                        <div id="resultsContent"></div>
                    </div>
                </div>
                
                <div class="document-comparison">
                    <h4>Comparación de Documentos</h4>
                    <div class="comparison-tools">
                        <select id="doc1Select" class="doc-selector"></select>
                        <select id="doc2Select" class="doc-selector"></select>
                        <button id="compareDocuments">Comparar Documentos</button>
                        
                        <div class="comparison-results" id="comparisonResults">
                            <p>Los resultados de comparación aparecerán aquí</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="prototyping" id="prototypingSection" style="display: none;">
            <h2>Prototipado para Validación de Requisitos</h2>
            
            <div class="prototyping-tools">
                <h3>Constructor de Prototipos Interactivos</h3>
                
                <div class="prototype-canvas">
                    <h4>Lienzo de Prototipo</h4>
                    <div class="canvas-controls">
                        <button id="addElement">Agregar Elemento</button>
                        <button id="addScreen">Agregar Pantalla</button>
                        <button id="connectElements">Conectar Elementos</button>
                        <button id="clearCanvas">Limpiar Lienzo</button>
                    </div>
                    
                    <div class="canvas-area" id="prototypeCanvas">
                        <div class="canvas-placeholder">
                            <p>Haz clic en "Agregar Pantalla" para comenzar a construir tu prototipo</p>
                        </div>
                    </div>
                </div>
                
                <div class="element-library">
                    <h4>Biblioteca de Elementos</h4>
                    <div class="element-types">
                        <button class="element-btn" data-type="button">Botón</button>
                        <button class="element-btn" data-type="input">Entrada de Texto</button>
                        <button class="element-btn" data-type="label">Etiqueta</button>
                        <button class="element-btn" data-type="image">Imagen</button>
                        <button class="element-btn" data-type="list">Lista</button>
                    </div>
                </div>
                
                <div class="feedback-collection">
                    <h4>Recolección de Retroalimentación de Usuarios</h4>
                    <div class="feedback-form">
                        <div class="form-group">
                            <label for="feedbackUser">Nombre del Usuario:</label>
                            <input type="text" id="feedbackUser">
                        </div>
                        
                        <div class="form-group">
                            <label for="feedbackRating">Calificación General:</label>
                            <select id="feedbackRating">
                                <option value="5">Excelente (5)</option>
                                <option value="4">Bueno (4)</option>
                                <option value="3">Promedio (3)</option>
                                <option value="2">Deficiente (2)</option>
                                <option value="1">Muy Deficiente (1)</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="feedbackComments">Comentarios:</label>
                            <textarea id="feedbackComments" placeholder="¿Qué funcionó bien? ¿Qué necesita mejora?"></textarea>
                        </div>
                        
                        <button id="submitFeedback">Enviar Retroalimentación</button>
                    </div>
                    
                    <div class="feedback-summary" id="feedbackSummary">
                        <h5>Resumen de Retroalimentación</h5>
                        <div id="summaryContent"></div>
                    </div>
                </div>
            </div>
        </section>

        <section class="integration" id="integrationSection" style="display: none;">
            <h2>Integración de Técnicas y Síntesis</h2>
            
            <div class="integration-tools">
                <h3>Síntesis de Requisitos Multi-Técnica</h3>
                
                <div class="technique-combination">
                    <h4>Matriz de Combinación de Técnicas</h4>
                    <div class="combination-matrix">
                        <table class="technique-table">
                            <thead>
                                <tr>
                                    <th>Técnica</th>
                                    <th>Mejor Para</th>
                                    <th>Fortalezas</th>
                                    <th>Limitaciones</th>
                                    <th>Combinar Con</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Entrevistas</td>
                                    <td>Requisitos detallados</td>
                                    <td>Datos cualitativos ricos</td>
                                    <td>Consume tiempo</td>
                                    <td>Cuestionarios</td>
                                </tr>
                                <tr>
                                    <td>Cuestionarios</td>
                                    <td>Grupos grandes</td>
                                    <td>Datos cuantitativos</td>
                                    <td>Profundidad limitada</td>
                                    <td>Entrevistas</td>
                                </tr>
                                <tr>
                                    <td>Observación</td>
                                    <td>Flujos de trabajo reales</td>
                                    <td>Comportamiento real</td>
                                    <td>Efecto del observador</td>
                                    <td>Análisis de documentos</td>
                                </tr>
                                <tr>
                                    <td>Análisis de Documentos</td>
                                    <td>Sistemas existentes</td>
                                    <td>Datos históricos</td>
                                    <td>Información desactualizada</td>
                                    <td>Prototipado</td>
                                </tr>
                                <tr>
                                    <td>Prototipado</td>
                                    <td>Requisitos de UI</td>
                                    <td>Validación visual</td>
                                    <td>Consume tiempo</td>
                                    <td>Todas las técnicas</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <div class="requirements-synthesis">
                    <h4>Síntesis de Requisitos</h4>
                    <div class="synthesis-tools">
                        <button id="loadTechniqueData">Cargar Datos de Técnicas</button>
                        <button id="synthesizeRequirements">Sintetizar Requisitos</button>
                        <button id="resolveConflicts">Resolver Conflictos</button>
                        <button id="prioritizeRequirements">Priorizar Requisitos</button>
                    </div>
                    
                    <div class="synthesis-results" id="synthesisResults">
                        <h5>Resultados de Síntesis</h5>
                        <div id="synthesisContent"></div>
                    </div>
                </div>
                
                <div class="validation-dashboard">
                    <h4>Dashboard de Validación</h4>
                    <div class="validation-metrics">
                        <div class="metric">
                            <h5>Cobertura de Requisitos</h5>
                            <div class="progress-bar">
                                <div class="progress-fill" id="coverageProgress" style="width: 0%"></div>
                            </div>
                            <span id="coverageText">0%</span>
                        </div>
                        
                        <div class="metric">
                            <h5>Acuerdo de Interesados</h5>
                            <div class="progress-bar">
                                <div class="progress-fill" id="agreementProgress" style="width: 0%"></div>
                            </div>
                            <span id="agreementText">0%</span>
                        </div>
                        
                        <div class="metric">
                            <h5>Calidad de Requisitos</h5>
                            <div class="progress-bar">
                                <div class="progress-fill" id="qualityProgress" style="width: 0%"></div>
                            </div>
                            <span id="qualityText">0%</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="elicitation_scripts.js"></script>
</body>
</html>
```

### Paso 2: CSS para Dashboard de Elicitación
Crear un archivo `elicitation_styles.css`:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
    color: #333;
    line-height: 1.6;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
    margin: 0;
    font-size: 1.8rem;
}

nav {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}

nav button {
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
}

nav button:hover, nav button:focus, nav button.active {
    background-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

main {
    max-width: 1400px;
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
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
    margin-bottom: 2rem;
}

h3 {
    color: #3498db;
    margin-bottom: 1rem;
}

h4 {
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.form-group input, .form-group select, .form-group textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
}

.form-group textarea {
    min-height: 100px;
    resize: vertical;
}

button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #2980b9;
}

button:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
}

/* Sección de Entrevistas */
.interview-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.question-generator, .response-recorder {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.questions-list {
    margin-top: 1rem;
    max-height: 300px;
    overflow-y: auto;
}

.question-item {
    background-color: white;
    padding: 1rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

.recording-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
}

/* Sección de Cuestionarios */
.questionnaire-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.survey-builder, .response-collection, .response-analysis {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.question-builder {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin: 1rem 0;
}

.question-builder select, .question-builder input {
    flex: 1;
}

.survey-link {
    margin-top: 1rem;
    padding: 1rem;
    background-color: white;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

/* Sección de Observación */
.observation-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.observation-setup, .activity-logger, .workflow-analysis {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.logging-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
}

.activity-entry {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin: 1rem 0;
}

.activity-entry input, .activity-entry select {
    flex: 1;
}

.activity-timeline {
    margin-top: 1rem;
    max-height: 300px;
    overflow-y: auto;
}

.timeline-item {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    font-size: 0.9rem;
}

/* Sección de Análisis de Documentos */
.document-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.document-upload, .requirements-extraction, .document-comparison {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.upload-area {
    border: 2px dashed #dee2e6;
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
    margin: 1rem 0;
}

.upload-prompt p {
    margin-bottom: 1rem;
    color: #6c757d;
}

.document-item {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.doc-selector {
    margin: 0 1rem;
    padding: 0.5rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
}

/* Sección de Prototipado */
.prototyping-tools {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 2rem;
}

.prototype-canvas {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.canvas-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}

.canvas-area {
    border: 1px solid #dee2e6;
    border-radius: 4px;
    min-height: 400px;
    background-color: white;
    position: relative;
    overflow: hidden;
}

.canvas-placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #6c757d;
}

.element-library {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.element-types {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.element-btn {
    text-align: left;
    padding: 0.5rem;
    background-color: white;
    border: 1px solid #dee2e6;
}

.element-btn:hover {
    background-color: #e9ecef;
}

.feedback-collection {
    grid-column: 1 / -1;
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    margin-top: 2rem;
}

.feedback-summary {
    margin-top: 2rem;
}

/* Sección de Integración */
.integration-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.technique-combination, .requirements-synthesis, .validation-dashboard {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.technique-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}

.technique-table th, .technique-table td {
    padding: 0.5rem;
    text-align: left;
    border: 1px solid #dee2e6;
}

.technique-table th {
    background-color: #e9ecef;
    font-weight: bold;
}

.synthesis-tools {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
    flex-wrap: wrap;
}

.validation-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.metric {
    background-color: white;
    padding: 1rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    text-align: center;
}

.progress-bar {
    background-color: #e9ecef;
    height: 20px;
    border-radius: 10px;
    margin: 0.5rem 0;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background-color: #28a745;
    transition: width 0.3s ease;
}

/* Notificación */
.notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #3498db;
    color: white;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    display: none;
    max-width: 300px;
    z-index: 1000;
}

/* Responsive */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    nav {
        justify-content: center;
    }
    
    .interview-tools, .questionnaire-tools, .observation-tools, 
    .document-tools, .prototyping-tools, .integration-tools {
        grid-template-columns: 1fr;
    }
    
    .activity-entry, .question-builder {
        flex-direction: column;
        align-items: stretch;
    }
    
    .logging-controls, .canvas-controls, .synthesis-tools {
        justify-content: center;
    }
}
```

### Paso 3: JavaScript para Dashboard de Elicitación
Crear un archivo `elicitation_scripts.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Sistema de navegación
    const sections = {
        interviews: document.getElementById('interviewsSection'),
        questionnaires: document.getElementById('questionnairesSection'),
        observation: document.getElementById('observationSection'),
        documents: document.getElementById('documentsSection'),
        prototyping: document.getElementById('prototypingSection'),
        integration: document.getElementById('integrationSection')
    };
    
    // Botones de navegación
    document.getElementById('interviewsBtn').addEventListener('click', () => showSection('interviews'));
    document.getElementById('questionnairesBtn').addEventListener('click', () => showSection('questionnaires'));
    document.getElementById('observationBtn').addEventListener('click', () => showSection('observation'));
    document.getElementById('documentsBtn').addEventListener('click', () => showSection('documents'));
    document.getElementById('prototypingBtn').addEventListener('click', () => showSection('prototyping'));
    document.getElementById('integrationBtn').addEventListener('click', () => showSection('integration'));
    
    function showSection(sectionName) {
        // Ocultar todas las secciones
        Object.values(sections).forEach(section => {
            section.style.display = 'none';
        });
        
        // Mostrar sección seleccionada
        sections[sectionName].style.display = 'block';
        
        // Actualizar botones de navegación
        document.querySelectorAll('nav button').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Agregar clase activa al botón actual
        const currentBtn = document.getElementById(sectionName + 'Btn');
        if (currentBtn) {
            currentBtn.classList.add('active');
        }
        
        showNotification(`Cambiado a sección ${sectionName}`);
    }
    
    // Gestión de Entrevistas
    let currentInterview = null;
    let isRecording = false;
    
    document.getElementById('interviewSetupForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const interviewee = document.getElementById('intervieweeName').value;
        const role = document.getElementById('intervieweeRole').value;
        const type = document.getElementById('interviewType').value;
        const topic = document.getElementById('interviewTopic').value;
        
        currentInterview = {
            interviewee: interviewee,
            role: role,
            type: type,
            topic: topic,
            startTime: new Date(),
            questions: [],
            responses: []
        };
        
        showNotification(`Entrevista iniciada con ${interviewee}`);
        this.reset();
    });
    
    document.getElementById('generateQuestions').addEventListener('click', function() {
        const category = document.getElementById('questionCategory').value;
        const questions = generateQuestions(category);
        
        const questionsList = document.getElementById('questionsList');
        questionsList.innerHTML = '';
        
        questions.forEach((question, index) => {
            const questionItem = document.createElement('div');
            questionItem.className = 'question-item';
            questionItem.innerHTML = `
                <strong>P${index + 1}:</strong> ${question}
                <button class="ask-question" data-question="${question}">Preguntar</button>
            `;
            questionsList.appendChild(questionItem);
            
            if (currentInterview) {
                currentInterview.questions.push(question);
            }
        });
        
        showNotification(`Generadas ${questions.length} preguntas`);
    });
    
    function generateQuestions(category) {
        const questionTemplates = {
            functional: [
                "¿Cuáles son las tareas principales que realizas en tu rol?",
                "¿Qué información necesitas para completar tu trabajo?",
                "¿Cuáles son los resultados más importantes que necesitas lograr?",
                "¿Cuáles son los mayores desafíos que enfrentas en tu trabajo?",
                "¿Cómo manejas actualmente [proceso específico]?"
            ],
            non_functional: [
                "¿Qué tan rápido necesitas respuestas a tus solicitudes?",
                "¿Cuáles son tus requisitos de disponibilidad?",
                "¿Cuántos usuarios necesitan acceder al sistema simultáneamente?",
                "¿Cuáles son tus requisitos de seguridad y privacidad?",
                "¿Qué nivel de confiabilidad necesitas?"
            ],
            constraints: [
                "¿Qué limitaciones o restricciones trabajas?",
                "¿Qué requisitos regulatorios deben cumplirse?",
                "¿Qué restricciones presupuestarias afectan tu trabajo?",
                "¿Qué restricciones tecnológicas existen?",
                "¿Qué políticas organizacionales impactan tus requisitos?"
            ],
            stakeholder: [
                "¿Cuáles son tus principales preocupaciones sobre este proyecto?",
                "¿Cómo afectará este sistema tu trabajo diario?",
                "¿Cuáles son tus criterios de éxito para este proyecto?",
                "¿Quién más se verá afectado por este sistema?",
                "¿Qué capacitación o soporte necesitarás?"
            ]
        };
        
        return questionTemplates[category] || [];
    }
    
    // Controles de grabación
    document.getElementById('startRecording').addEventListener('click', function() {
        isRecording = true;
        this.disabled = true;
        document.getElementById('stopRecording').disabled = false;
        showNotification('Grabación iniciada');
    });
    
    document.getElementById('stopRecording').addEventListener('click', function() {
        isRecording = false;
        this.disabled = true;
        document.getElementById('startRecording').disabled = false;
        showNotification('Grabación detenida');
    });
    
    document.getElementById('saveResponse').addEventListener('click', function() {
        const responseText = document.getElementById('responseText').value;
        if (responseText && currentInterview) {
            currentInterview.responses.push({
                timestamp: new Date(),
                text: responseText
            });
            
            // Analizar respuesta
            analyzeResponse(responseText);
            
            document.getElementById('responseText').value = '';
            showNotification('Respuesta guardada');
        }
    });
    
    function analyzeResponse(text) {
        const analysis = document.getElementById('responseAnalysis');
        
        // Análisis simple de palabras clave
        const keywords = {
            requirements: ['necesito', 'requiero', 'debo', 'debería', 'quiero'],
            problems: ['problema', 'problemas', 'desafío', 'dificultad', 'problema'],
            processes: ['proceso', 'flujo de trabajo', 'procedimiento', 'paso', 'tarea'],
            stakeholders: ['usuario', 'cliente', 'gerente', 'equipo', 'departamento']
        };
        
        let findings = [];
        
        Object.keys(keywords).forEach(category => {
            const found = keywords[category].some(keyword => 
                text.toLowerCase().includes(keyword)
            );
            if (found) {
                findings.push(category);
            }
        });
        
        analysis.innerHTML = `
            <h6>Resultados de Análisis:</h6>
            <p><strong>Categorías identificadas:</strong> ${findings.join(', ') || 'Ninguna'}</p>
            <p><strong>Conteo de palabras:</strong> ${text.split(' ').length}</p>
            <p><strong>Requisitos potenciales:</strong> ${findings.includes('requirements') ? 'Sí' : 'Revisión necesaria'}</p>
        `;
    }
    
    // Constructor de Cuestionarios
    let currentSurvey = { title: '', description: '', questions: [] };
    
    document.getElementById('addQuestion').addEventListener('click', function() {
        const type = document.getElementById('questionType').value;
        const text = document.getElementById('questionText').value;
        
        if (text) {
            const question = {
                id: Date.now(),
                type: type,
                text: text,
                options: []
            };
            
            currentSurvey.questions.push(question);
            updateSurveyPreview();
            
            document.getElementById('questionText').value = '';
            showNotification('Pregunta agregada a la encuesta');
        }
    });
    
    function updateSurveyPreview() {
        const preview = document.getElementById('previewContent');
        const title = document.getElementById('surveyTitle').value;
        const description = document.getElementById('surveyDescription').value;
        
        currentSurvey.title = title;
        currentSurvey.description = description;
        
        let html = `<h4>${title || 'Encuesta Sin Título'}</h4>`;
        if (description) {
            html += `<p>${description}</p>`;
        }
        
        currentSurvey.questions.forEach((q, index) => {
            html += `<div class="preview-question">
                <p><strong>P${index + 1}:</strong> ${q.text}</p>
                <div class="question-response">
                    ${generateQuestionResponse(q)}
                </div>
            </div>`;
        });
        
        preview.innerHTML = html;
    }
    
    function generateQuestionResponse(question) {
        switch(question.type) {
            case 'multiple-choice':
                return `
                    <div class="options">
                        <label><input type="radio" name="q${question.id}"> Opción 1</label><br>
                        <label><input type="radio" name="q${question.id}"> Opción 2</label><br>
                        <label><input type="radio" name="q${question.id}"> Opción 3</label><br>
                        <label><input type="radio" name="q${question.id}"> Otro</label>
                    </div>
                `;
            case 'rating':
                return `
                    <div class="rating">
                        <span>1</span> <input type="range" min="1" max="5"> <span>5</span>
                    </div>
                `;
            case 'open-ended':
                return `<textarea placeholder="Tu respuesta aquí..."></textarea>`;
            case 'yes-no':
                return `
                    <label><input type="radio" name="q${question.id}"> Sí</label>
                    <label><input type="radio" name="q${question.id}"> No</label>
                `;
            default:
                return '';
        }
    }
    
    document.getElementById('generateSurveyLink').addEventListener('click', function() {
        const linkText = document.getElementById('linkText');
        const surveyLink = document.getElementById('surveyLink');
        
        // Generar enlace de encuesta mock
        const surveyId = Date.now();
        linkText.textContent = `https://elicitation.example.com/encuesta/${surveyId}`;
        surveyLink.style.display = 'block';
        
        showNotification('Enlace de encuesta generado');
    });
    
    document.getElementById('copyLink').addEventListener('click', function() {
        const linkText = document.getElementById('linkText').textContent;
        navigator.clipboard.writeText(linkText);
        showNotification('Enlace copiado al portapapeles');
    });
    
    document.getElementById('loadResponses').addEventListener('click', function() {
        // Cargar respuestas de ejemplo
        const sampleResponses = generateSampleResponses();
        showNotification(`Cargadas ${sampleResponses.length} respuestas de ejemplo`);
    });
    
    function generateSampleResponses() {
        return [
            { questionId: 1, response: 'Sí', respondent: 'Usuario1' },
            { questionId: 1, response: 'No', respondent: 'Usuario2' },
            { questionId: 2, response: '4', respondent: 'Usuario1' },
            { questionId: 2, response: '5', respondent: 'Usuario2' }
        ];
    }
    
    // Herramientas de Observación
    let observationSession = null;
    let isLogging = false;
    let activityLog = [];
    
    document.getElementById('observationSetupForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const context = document.getElementById('observationContext').value;
        const duration = document.getElementById('observationDuration').value;
        const type = document.getElementById('observationType').value;
        
        observationSession = {
            context: context,
            duration: duration,
            type: type,
            startTime: new Date(),
            activities: []
        };
        
        showNotification(`Sesión de observación iniciada: ${context}`);
        this.reset();
    });
    
    document.getElementById('startLogging').addEventListener('click', function() {
        isLogging = true;
        this.disabled = true;
        document.getElementById('pauseLogging').disabled = false;
        document.getElementById('stopLogging').disabled = false;
        showNotification('Registro de actividad iniciado');
    });
    
    document.getElementById('stopLogging').addEventListener('click', function() {
        isLogging = false;
        this.disabled = true;
        document.getElementById('startLogging').disabled = false;
        document.getElementById('pauseLogging').disabled = true;
        showNotification('Registro de actividad detenido');
    });
    
    document.getElementById('logActivity').addEventListener('click', function() {
        const description = document.getElementById('activityDescription').value;
        const category = document.getElementById('activityCategory').value;
        
        if (description && isLogging) {
            const activity = {
                timestamp: new Date(),
                description: description,
                category: category
            };
            
            activityLog.push(activity);
            updateActivityTimeline();
            
            document.getElementById('activityDescription').value = '';
            showNotification('Actividad registrada');
        }
    });
    
    function updateActivityTimeline() {
        const timeline = document.getElementById('timelineContent');
        timeline.innerHTML = '';
        
        activityLog.forEach(activity => {
            const item = document.createElement('div');
            item.className = 'timeline-item';
            item.innerHTML = `
                <strong>${activity.timestamp.toLocaleTimeString()}</strong> - 
                <span class="category">${activity.category}</span>: 
                ${activity.description}
            `;
            timeline.appendChild(item);
        });
    }
    
    // Análisis de Documentos
    let uploadedDocuments = [];
    
    document.getElementById('documentFile').addEventListener('change', function(e) {
        const files = e.target.files;
        
        for (let file of files) {
            const document = {
                id: Date.now(),
                name: file.name,
                type: file.type,
                size: file.size,
                uploadTime: new Date()
            };
            
            uploadedDocuments.push(document);
        }
        
        updateDocumentList();
        showNotification(`Subidos ${files.length} documento(s)`);
    });
    
    function updateDocumentList() {
        const documentList = document.getElementById('documentList');
        documentList.innerHTML = '';
        
        uploadedDocuments.forEach(doc => {
            const item = document.createElement('div');
            item.className = 'document-item';
            item.innerHTML = `
                <div>
                    <strong>${doc.name}</strong>
                    <small>${(doc.size / 1024).toFixed(1)} KB</small>
                </div>
                <button class="remove-doc" data-id="${doc.id}">Remover</button>
            `;
            documentList.appendChild(item);
        });
        
        // Actualizar selectores de comparación
        updateDocumentSelectors();
    }
    
    function updateDocumentSelectors() {
        const selectors = document.querySelectorAll('.doc-selector');
        selectors.forEach(selector => {
            selector.innerHTML = '<option value="">Seleccionar documento</option>';
            uploadedDocuments.forEach(doc => {
                const option = document.createElement('option');
                option.value = doc.id;
                option.textContent = doc.name;
                selector.appendChild(option);
            });
        });
    }
    
    document.getElementById('extractRequirements').addEventListener('click', function() {
        if (uploadedDocuments.length === 0) {
            showNotification('No hay documentos subidos');
            return;
        }
        
        // Simular extracción de requisitos
        const extractedReqs = [
            "El sistema debe proporcionar autenticación de usuario",
            "El sistema debe validar datos",
            "El sistema debe generar reportes",
            "El sistema debe soportar múltiples roles de usuario"
        ];
        
        const results = document.getElementById('resultsContent');
        results.innerHTML = `
            <h6>Requisitos Extraídos:</h6>
            <ul>
                ${extractedReqs.map(req => `<li>${req}</li>`).join('')}
            </ul>
        `;
        
        showNotification('Requisitos extraídos de documentos');
    });
    
    // Herramientas de Prototipado
    let prototypeElements = [];
    let currentScreen = null;
    
    document.getElementById('addScreen').addEventListener('click', function() {
        const canvas = document.getElementById('prototypeCanvas');
        const placeholder = canvas.querySelector('.canvas-placeholder');
        
        if (placeholder) {
            placeholder.remove();
        }
        
        const screen = document.createElement('div');
        screen.className = 'prototype-screen';
        screen.style.cssText = `
            position: absolute;
            width: 300px;
            height: 400px;
            background-color: white;
            border: 2px solid #3498db;
            border-radius: 8px;
            top: 50px;
            left: 50px;
        `;
        
        screen.innerHTML = '<div class="screen-header">Pantalla 1</div>';
        canvas.appendChild(screen);
        
        currentScreen = screen;
        showNotification('Nueva pantalla agregada al prototipo');
    });
    
    document.getElementById('addElement').addEventListener('click', function() {
        if (!currentScreen) {
            showNotification('Por favor agrega una pantalla primero');
            return;
        }
        
        const element = document.createElement('div');
        element.className = 'prototype-element';
        element.style.cssText = `
            position: absolute;
            width: 100px;
            height: 30px;
            background-color: #e9ecef;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            top: 60px;
            left: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        `;
        element.textContent = 'Botón';
        
        currentScreen.appendChild(element);
        showNotification('Elemento agregado a la pantalla');
    });
    
    // Recolección de Retroalimentación
    let feedbackData = [];
    
    document.getElementById('submitFeedback').addEventListener('click', function() {
        const user = document.getElementById('feedbackUser').value;
        const rating = document.getElementById('feedbackRating').value;
        const comments = document.getElementById('feedbackComments').value;
        
        if (user && rating) {
            const feedback = {
                user: user,
                rating: parseInt(rating),
                comments: comments,
                timestamp: new Date()
            };
            
            feedbackData.push(feedback);
            updateFeedbackSummary();
            
            // Resetear formulario
            document.getElementById('feedbackUser').value = '';
            document.getElementById('feedbackComments').value = '';
            
            showNotification('Retroalimentación enviada');
        }
    });
    
    function updateFeedbackSummary() {
        const summary = document.getElementById('summaryContent');
        
        if (feedbackData.length === 0) {
            summary.innerHTML = '<p>No se ha enviado retroalimentación aún</p>';
            return;
        }
        
        const avgRating = feedbackData.reduce((sum, f) => sum + f.rating, 0) / feedbackData.length;
        
        summary.innerHTML = `
            <p><strong>Retroalimentación Total:</strong> ${feedbackData.length}</p>
            <p><strong>Calificación Promedio:</strong> ${avgRating.toFixed(1)}/5</p>
            <div class="recent-comments">
                <h6>Comentarios Recientes:</h6>
                <ul>
                    ${feedbackData.slice(-3).map(f => `<li>${f.comments || 'Sin comentarios'}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    // Herramientas de Integración
    document.getElementById('synthesizeRequirements').addEventListener('click', function() {
        const synthesis = document.getElementById('synthesisContent');
        
        // Simular síntesis de requisitos
        const synthesizedReqs = [
            "REQ-001: Sistema de autenticación de usuario (de entrevistas & cuestionarios)",
            "REQ-002: Procesamiento de datos en tiempo real (de observación & prototipado)",
            "REQ-003: Soporte multi-usuario (de análisis de documentos)",
            "REQ-004: Reportes automatizados (de retroalimentación de interesados)"
        ];
        
        synthesis.innerHTML = `
            <h6>Requisitos Sintetizados:</h6>
            <ul>
                ${synthesizedReqs.map(req => `<li>${req}</li>`).join('')}
            </ul>
            <p><strong>Conflictos resueltos:</strong> 2 (requisitos similares fusionados)</p>
            <p><strong>Requisitos nuevos identificados:</strong> 1</p>
        `;
        
        // Actualizar métricas de validación
        updateValidationMetrics(75, 80, 70);
        showNotification('Requisitos sintetizados');
    });
    
    function updateValidationMetrics(coverage, agreement, quality) {
        document.getElementById('coverageProgress').style.width = coverage + '%';
        document.getElementById('coverageText').textContent = coverage + '%';
        
        document.getElementById('agreementProgress').style.width = agreement + '%';
        document.getElementById('agreementText').textContent = agreement + '%';
        
        document.getElementById('qualityProgress').style.width = quality + '%';
        document.getElementById('qualityText').textContent = quality + '%';
    }
    
    // Sistema de notificaciones
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
    
    // Inicializar con sección de entrevistas visible
    showSection('interviews');
    
    // Actualizar vista previa de encuesta en cambios de entrada
    document.getElementById('surveyTitle').addEventListener('input', updateSurveyPreview);
    document.getElementById('surveyDescription').addEventListener('input', updateSurveyPreview);
});
```

### Paso 4: Herramienta de Análisis de Elicitación en Python
Crear un archivo `elicitation_analyzer.py`:

```python
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
import re
from textblob import TextBlob
import numpy as np

class AnalizadorElicitacion:
    def __init__(self):
        self.datos_entrevistas = []
        self.datos_cuestionarios = []
        self.datos_observacion = []
        self.datos_documentos = []
        self.datos_retroalimentacion = []
        
        # Inicializar recursos NLTK
        try:
            nltk.data.find('vader_lexicon')
        except LookupError:
            nltk.download('vader_lexicon')
        
        try:
            nltk.data.find('punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('stopwords')
        except LookupError:
            nltk.download('stopwords')
        
        self.sia = SentimentIntensityAnalyzer()
        self.palabras_vacias = set(stopwords.words('spanish'))
    
    def cargar_datos_entrevistas(self, ruta_archivo: str):
        """Cargar transcripciones de entrevistas desde archivo JSON"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            self.datos_entrevistas = datos.get('entrevistas', [])
    
    def cargar_datos_cuestionarios(self, ruta_archivo: str):
        """Cargar respuestas de cuestionarios desde archivo JSON"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            self.datos_cuestionarios = datos.get('respuestas', [])
    
    def cargar_datos_observacion(self, ruta_archivo: str):
        """Cargar registros de observación desde archivo JSON"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            self.datos_observacion = datos.get('observaciones', [])
    
    def analizar_transcripcion_entrevista(self, transcripcion: str) -> Dict[str, Any]:
        """Analizar una transcripción de entrevista individual"""
        # Análisis de sentimiento
        sentimiento = self.sia.polarity_scores(transcripcion)
        
        # Extracción de palabras clave
        palabras = word_tokenize(transcripcion.lower())
        palabras_filtradas = [palabra for palabra in palabras if palabra.isalnum() and palabra not in self.palabras_vacias]
        frecuencia_palabras = Counter(palabras_filtradas)
        
        # Identificación de requisitos
        palabras_clave_requisitos = [
            'necesito', 'requiero', 'debo', 'debería', 'quiero', 'tengo que',
            'necesario', 'importante', 'crítico', 'esencial'
        ]
        
        requisitos_potenciales = []
        oraciones = nltk.sent_tokenize(transcripcion)
        
        for oracion in oraciones:
            if any(palabra_clave in oracion.lower() for palabra_clave in palabras_clave_requisitos):
                requisitos_potenciales.append(oracion.strip())
        
        # Análisis de temas
        temas = self._extraer_temas(transcripcion)
        
        return {
            'sentimiento': sentimiento,
            'frecuencia_palabras': dict(frecuencia_palabras.most_common(20)),
            'requisitos_potenciales': requisitos_potenciales,
            'temas': temas,
            'conteo_palabras': len(palabras),
            'conteo_oraciones': len(oraciones)
        }
    
    def _extraer_temas(self, texto: str) -> List[str]:
        """Extraer temas principales del texto"""
        palabras_clave_temas = {
            'funcionalidad': ['funcion', 'característica', 'capacidad', 'trabajo', 'hacer'],
            'usabilidad': ['fácil', 'simple', 'amigable', 'intuitivo', 'interfaz'],
            'rendimiento': ['rápido', 'veloz', 'rendimiento', 'velocidad', 'eficiente'],
            'seguridad': ['seguro', 'seguridad', 'proteger', 'privacidad', 'seguro'],
            'fiabilidad': ['confiable', 'dependable', 'estable', 'consistente']
        }
        
        texto_minuscula = texto.lower()
        temas = []
        
        for tema, palabras_clave in palabras_clave_temas.items():
            if any(palabra_clave in texto_minuscula for palabra_clave in palabras_clave):
                temas.append(tema)
        
        return temas
    
    def analizar_respuestas_cuestionario(self, respuestas: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analizar respuestas de cuestionarios"""
        df = pd.DataFrame(respuestas)
        
        analisis = {
            'total_respuestas': len(respuestas),
            'tasa_completitud': len(df.dropna()) / len(df) if len(df) > 0 else 0,
            'analisis_preguntas': {}
        }
        
        # Analizar cada pregunta
        for columna in df.columns:
            if columna != 'id_encuestado':
                datos_pregunta = df[columna].dropna()
                
                if datos_pregunta.dtype == 'object':
                    # Análisis de texto
                    analisis['analisis_preguntas'][columna] = self._analizar_respuestas_texto(datos_pregunta.tolist())
                else:
                    # Análisis numérico
                    analisis['analisis_preguntas'][columna] = {
                        'promedio': datos_pregunta.mean(),
                        'mediana': datos_pregunta.median(),
                        'desviacion_estandar': datos_pregunta.std(),
                        'minimo': datos_pregunta.min(),
                        'maximo': datos_pregunta.max()
                    }
        
        return analisis
    
    def _analizar_respuestas_texto(self, respuestas: List[str]) -> Dict[str, Any]:
        """Analizar respuestas de texto abiertas"""
        if not respuestas:
            return {}
        
        # Combinar todas las respuestas
        texto_combinado = ' '.join(respuestas)
        
        # Análisis de sentimiento
        sentimientos = [self.sia.polarity_scores(respuesta) for respuesta in respuestas]
        sentimiento_promedio = {
            'compuesto': np.mean([s['compound'] for s in sentimientos]),
            'positivo': np.mean([s['pos'] for s in sentimientos]),
            'negativo': np.mean([s['neg'] for s in sentimientos]),
            'neutral': np.mean([s['neu'] for s in sentimientos])
        }
        
        # Temas comunes
        todas_palabras = []
        for respuesta in respuestas:
            palabras = word_tokenize(respuesta.lower())
            palabras_filtradas = [palabra for palabra in palabras if palabra.isalnum() and palabra not in self.palabras_vacias]
            todas_palabras.extend(palabras_filtradas)
        
        frecuencia_palabras = Counter(todas_palabras)
        
        return {
            'conteo_respuestas': len(respuestas),
            'sentimiento_promedio': sentimiento_promedio,
            'palabras_comunes': dict(frecuencia_palabras.most_common(10)),
            'temas': self._extraer_temas(texto_combinado)
        }
    
    def analizar_datos_observacion(self, observaciones: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analizar registros de observación"""
        df = pd.DataFrame(observaciones)
        
        analisis = {
            'total_observaciones': len(observaciones),
            'periodo_observacion': self._calcular_periodo_observacion(observaciones),
            'desglose_actividades': {},
            'flujo_procesos': [],
            'cuellos_botella': []
        }
        
        if 'categoria' in df.columns:
            analisis['desglose_actividades'] = df['categoria'].value_counts().to_dict()
        
        # Identificar flujo de procesos
        if 'timestamp' in df.columns and 'descripcion' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.sort_values('timestamp')
            
            analisis['flujo_procesos'] = df[['timestamp', 'descripcion', 'categoria']].to_dict('records')
        
        # Identificar cuellos de botella (actividades que toman mucho tiempo)
        if 'duracion' in df.columns:
            actividades_largas = df[df['duracion'] > df['duracion'].quantile(0.75)]
            analisis['cuellos_botella'] = actividades_largas['descripcion'].tolist()
        
        return analisis
    
    def _calcular_periodo_observacion(self, observaciones: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calcular el período de observación"""
        if not observaciones or 'timestamp' not in observaciones[0]:
            return {}
        
        timestamps = [obs['timestamp'] for obs in observaciones if 'timestamp' in obs]
        
        if timestamps:
            timestamps.sort()
            return {
                'inicio': timestamps[0],
                'fin': timestamps[-1],
                'duracion_horas': (datetime.fromisoformat(timestamps[-1]) - datetime.fromisoformat(timestamps[0])).total_seconds() / 3600
            }
        
        return {}
    
    def extraer_requisitos_documentos(self, documentos: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extraer requisitos de documentos de texto"""
        todos_requisitos = []
        analisis_documentos = {}
        
        for doc in documentos:
            if 'contenido' in doc:
                contenido = doc['contenido']
                
                # Encontrar patrones de requisitos
                patrones_requisitos = [
                    r'(?:deberá|debe|podrá|podría)\s+[^.]*',
                    r'(?:el\s+sistema|el\s+usuario)\s+(?:deberá|debe|podrá)\s+[^.]*',
                    r'(?:el\s+sistema|el\s+usuario)\s+(?:necesita|requiere|quiere)\s+[^.]*'
                ]
                
                requisitos_doc = []
                for patron in patrones_requisitos:
                    coincidencias = re.findall(patron, contenido, re.IGNORECASE)
                    requisitos_doc.extend(coincidencias)
                
                analisis_documentos[doc['nombre']] = {
                    'requisitos_encontrados': len(requisitos_doc),
                    'requisitos': requisitos_doc
                }
                
                todos_requisitos.extend(requisitos_doc)
        
        return {
            'total_requisitos': len(todos_requisitos),
            'requisitos_unicos': len(set(todos_requisitos)),
            'analisis_documentos': analisis_documentos,
            'requisitos_consolidados': list(set(todos_requisitos))
        }
    
    def sintetizar_tecnicas(self, datos_tecnicas: Dict[str, List]) -> Dict[str, Any]:
        """Sintetizar datos de múltiples técnicas de elicitación"""
        sintesis = {
            'requisitos_consolidados': [],
            'conflictos': [],
            'brechas': [],
            'requisitos_priorizados': [],
            'consenso_interesados': {}
        }
        
        # Combinar requisitos de todas las técnicas
        todos_requisitos = []
        
        if 'requisitos_entrevistas' in datos_tecnicas:
            todos_requisitos.extend(datos_tecnicas['requisitos_entrevistas'])
        
        if 'requisitos_cuestionarios' in datos_tecnicas:
            todos_requisitos.extend(datos_tecnicas['requisitos_cuestionarios'])
        
        if 'requisitos_observacion' in datos_tecnicas:
            todos_requisitos.extend(datos_tecnicas['requisitos_observacion'])
        
        if 'requisitos_documentos' in datos_tecnicas:
            todos_requisitos.extend(datos_tecnicas['requisitos_documentos'])
        
        # Eliminar duplicados y consolidar requisitos similares
        sintesis['requisitos_consolidados'] = self._consolidar_requisitos(todos_requisitos)
        
        # Identificar conflictos
        sintesis['conflictos'] = self._identificar_conflictos(todos_requisitos)
        
        # Identificar brechas
        sintesis['brechas'] = self._identificar_brechas(datos_tecnicas)
        
        # Priorizar requisitos
        sintesis['requisitos_priorizados'] = self._priorizar_requisitos(sintesis['requisitos_consolidados'])
        
        return sintesis
    
    def _consolidar_requisitos(self, requisitos: List[str]) -> List[str]:
        """Consolidar requisitos similares"""
        # Consolidación simple - eliminar duplicados exactos
        return list(set(requisitos))
    
    def _identificar_conflictos(self, requisitos: List[str]) -> List[Dict[str, Any]]:
        """Identificar requisitos conflictivos"""
        conflictos = []
        
        # Detección simple de conflictos - buscar términos contradictorios
        pares_contradictorios = [
            ('debe', 'no debe'),
            ('deberá', 'no deberá'),
            ('requerido', 'opcional'),
            ('siempre', 'nunca')
        ]
        
        for i, req1 in enumerate(requisitos):
            for j, req2 in enumerate(requisitos[i+1:], i+1):
                for positivo, negativo in pares_contradictorios:
                    if (positivo in req1.lower() and negativo in req2.lower()) or \
                       (positivo in req2.lower() and negativo in req1.lower()):
                        conflictos.append({
                            'requisito1': req1,
                            'requisito2': req2,
                            'tipo_conflicto': f'{positivo} vs {negativo}'
                        })
        
        return conflictos
    
    def _identificar_brechas(self, datos_tecnicas: Dict[str, List]) -> List[str]:
        """Identificar brechas en cobertura de requisitos"""
        brechas = []
        
        # Verificar tipos de requisitos faltantes
        tipos_requeridos = ['funcional', 'no_funcional', 'restricciones', 'interfaz']
        
        for tipo_req in tipos_requeridos:
            encontrado = False
            for tecnica, datos in datos_tecnicas.items():
                if any(tipo_req in str(req).lower() for req in datos):
                    encontrado = True
                    break
            
            if not encontrado:
                brechas.append(f'Requisitos {tipo_req} faltantes')
        
        return brechas
    
    def _priorizar_requisitos(self, requisitos: List[str]) -> List[Tuple[str, int]]:
        """Priorizar requisitos basados en palabras clave"""
        palabras_clave_prioridad = {
            'alto': ['crítico', 'esencial', 'debe', 'requerido', 'importante'],
            'medio': ['debería', 'preferible', 'agradable'],
            'bajo': ['podrá', 'opcional', 'podría']
        }
        
        priorizados = []
        
        for req in requisitos:
            prioridad_puntuacion = 1  # Prioridad baja por defecto
            
            req_minuscula = req.lower()
            for nivel, palabras_clave in palabras_clave_prioridad.items():
                if any(palabra_clave in req_minuscula for palabra_clave in palabras_clave):
                    if nivel == 'alto':
                        prioridad_puntuacion = 3
                    elif nivel == 'medio':
                        prioridad_puntuacion = 2
                    break
            
            priorizados.append((req, prioridad_puntuacion))
        
        # Ordenar por prioridad (alto a bajo)
        priorizados.sort(key=lambda x: x[1], reverse=True)
        return priorizados
    
    def generar_reporte_elicitacion(self) -> Dict[str, Any]:
        """Generar reporte comprehensivo de análisis de elicitación"""
        reporte = {
            'resumen': {
                'entrevistas_analizadas': len(self.datos_entrevistas),
                'respuestas_cuestionarios': len(self.datos_cuestionarios),
                'sesiones_observacion': len(self.datos_observacion),
                'documentos_procesados': len(self.datos_documentos)
            },
            'analisis_entrevistas': [],
            'analisis_cuestionarios': {},
            'analisis_observacion': {},
            'analisis_documentos': {},
            'sintesis': {}
        }
        
        # Analizar entrevistas
        for entrevista in self.datos_entrevistas:
            if 'transcripcion' in entrevista:
                analisis = self.analizar_transcripcion_entrevista(entrevista['transcripcion'])
                analisis['id_entrevista'] = entrevista.get('id', 'Desconocido')
                reporte['analisis_entrevistas'].append(analisis)
        
        # Analizar cuestionarios
        if self.datos_cuestionarios:
            reporte['analisis_cuestionarios'] = self.analizar_respuestas_cuestionario(self.datos_cuestionarios)
        
        # Analizar observaciones
        if self.datos_observacion:
            reporte['analisis_observacion'] = self.analizar_datos_observacion(self.datos_observacion)
        
        # Analizar documentos
        if self.datos_documentos:
            reporte['analisis_documentos'] = self.extraer_requisitos_documentos(self.datos_documentos)
        
        # Sintetizar todas las técnicas
        datos_tecnicas = {
            'requisitos_entrevistas': [req for analisis in reporte['analisis_entrevistas'] 
                                    for req in analisis.get('requisitos_potenciales', [])],
            'requisitos_cuestionarios': self.datos_cuestionarios,
            'requisitos_observacion': self.datos_observacion,
            'requisitos_documentos': reporte['analisis_documentos'].get('requisitos_consolidados', [])
        }
        
        reporte['sintesis'] = self.sintetizar_tecnicas(datos_tecnicas)
        
        return reporte
    
    def crear_visualizaciones_elicitacion(self, ruta_guardado: str = 'analisis_elicitacion.png'):
        """Crear visualizaciones comprehensivas de análisis de elicitación"""
        if not any([self.datos_entrevistas, self.datos_cuestionarios, self.datos_observacion]):
            print("No hay datos de elicitación disponibles para visualización")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Uso de técnicas de elicitación
        tecnicas = ['Entrevistas', 'Cuestionarios', 'Observaciones', 'Documentos']
        conteos = [
            len(self.datos_entrevistas),
            len(self.datos_cuestionarios),
            len(self.datos_observacion),
            len(self.datos_documentos)
        ]
        
        barras1 = ax1.bar(tecnicas, conteos, color=['azul', 'verde', 'naranja', 'rojo'])
        ax1.set_title('Técnicas de Elicitación Utilizadas', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Conteo', fontsize=12)
        
        for barra, conteo in zip(barras1, conteos):
            ax1.text(barra.get_x() + barra.get_width()/2, barra.get_y() + conteo + 0.1, 
                    str(conteo), ha='center', va='bottom', fontweight='bold')
        
        # Análisis de sentimiento de entrevistas
        if self.datos_entrevistas:
            sentimientos = []
            for entrevista in self.datos_entrevistas:
                if 'transcripcion' in entrevista:
                    sentimiento = self.sia.polarity_scores(entrevista['transcripcion'])
                    sentimientos.append(sentimiento['compound'])
            
            if sentimientos:
                ax2.hist(sentimientos, bins=10, edgecolor='black', alpha=0.7)
                ax2.set_title('Distribución de Sentimiento en Entrevistas', fontsize=14, fontweight='bold')
                ax2.set_xlabel('Puntuación de Sentimiento', fontsize=12)
                ax2.set_ylabel('Frecuencia', fontsize=12)
                ax2.axvline(sum(sentimientos)/len(sentimientos), color='red', linestyle='--', 
                           label=f'Promedio: {sum(sentimientos)/len(sentimientos):.2f}')
                ax2.legend()
        
        # Distribución de respuestas de cuestionarios
        if self.datos_cuestionarios:
            df = pd.DataFrame(self.datos_cuestionarios)
            columnas_numericas = df.select_dtypes(include=[np.number]).columns
            
            if len(columnas_numericas) > 0:
                df[columnas_numericas].boxplot(ax=ax3)
                ax3.set_title('Distribución de Respuestas de Cuestionarios', fontsize=14, fontweight='bold')
                ax3.set_ylabel('Valor de Respuesta', fontsize=12)
        
        # Desglose de actividades de observación
        if self.datos_observacion:
            df = pd.DataFrame(self.datos_observacion)
            if 'categoria' in df.columns:
                conteos_categoria = df['categoria'].value_counts()
                conteos_categoria.plot(kind='pie', autopct='%1.1f%%', ax=ax4)
                ax4.set_title('Desglose de Actividades de Observación', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Visualizaciones de análisis de elicitación guardadas: {ruta_guardado}")
    
    def exportar_datos_elicitacion(self, ruta_archivo: str):
        """Exportar datos de análisis de elicitación a archivo JSON"""
        datos = {
            'entrevistas': self.datos_entrevistas,
            'cuestionarios': self.datos_cuestionarios,
            'observaciones': self.datos_observacion,
            'documentos': self.datos_documentos,
            'retroalimentacion': self.datos_retroalimentacion,
            'exportado_en': datetime.now().isoformat()
        }
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"Datos de elicitación exportados a {ruta_archivo}")

# Ejemplo de uso y datos de muestra
def crear_datos_muestra():
    """Crear datos de elicitación de muestra para demostración"""
    analizador = AnalizadorElicitacion()
    
    # Datos de muestra de entrevistas
    analizador.datos_entrevistas = [
        {
            'id': 'ENT-001',
            'entrevistado': 'Juan Pérez',
            'rol': 'Gerente de Producto',
            'transcripcion': "Necesito que el sistema sea rápido y responsivo. Los usuarios deben poder autenticarse rápidamente y de forma segura. El sistema debe manejar al menos 1000 usuarios concurrentes sin problemas."
        },
        {
            'id': 'ENT-002',
            'entrevistado': 'María González',
            'rol': 'Desarrolladora',
            'transcripcion': "La aplicación debe tener una interfaz limpia. La seguridad es crítica - no podemos tener brechas de datos. El sistema debe ser fácil de mantener y actualizar."
        }
    ]
    
    # Datos de muestra de cuestionarios
    analizador.datos_cuestionarios = [
        {'id_encuestado': 'R001', 'importancia_autenticacion': 5, 'importancia_ui': 4, 'importancia_seguridad': 5, 'comentarios': 'Necesito mejor soporte móvil'},
        {'id_encuestado': 'R002', 'importancia_autenticacion': 4, 'importancia_ui': 5, 'importancia_seguridad': 5, 'comentarios': 'El rendimiento es clave'},
        {'id_encuestado': 'R003', 'importancia_autenticacion': 5, 'importancia_ui': 3, 'importancia_seguridad': 4, 'comentarios': 'La seguridad primero'}
    ]
    
    # Datos de muestra de observación
    analizador.datos_observacion = [
        {'timestamp': '2024-01-01T09:00:00', 'descripcion': 'Usuario inicia sesión en el sistema', 'categoria': 'tarea', 'duracion': 30},
        {'timestamp': '2024-01-01T09:05:00', 'descripcion': 'Usuario navega al dashboard', 'categoria': 'tarea', 'duracion': 15},
        {'timestamp': '2024-01-01T09:10:00', 'descripcion': 'Usuario espera carga de datos', 'categoria': 'espera', 'duracion': 45},
        {'timestamp': '2024-01-01T09:15:00', 'descripcion': 'Usuario genera reporte', 'categoria': 'tarea', 'duracion': 60}
    ]
    
    # Datos de muestra de documentos
    analizador.datos_documentos = [
        {
            'nombre': 'requisitos_doc.pdf',
            'contenido': 'El sistema deberá proporcionar autenticación de usuario. El sistema debe ser seguro. Los usuarios deberían tener una interfaz intuitiva.'
        }
    ]
    
    return analizador

if __name__ == "__main__":
    # Crear datos de muestra
    analizador = crear_datos_muestra()
    
    # Generar reporte
    reporte = analizador.generar_reporte_elicitacion()
    
    print("Reporte de Análisis de Elicitación")
    print("=" * 50)
    print(f"Entrevistas Analizadas: {reporte['resumen']['entrevistas_analizadas']}")
    print(f"Respuestas de Cuestionarios: {reporte['resumen']['respuestas_cuestionarios']}")
    print(f"Sesiones de Observación: {reporte['resumen']['sesiones_observacion']}")
    print(f"Documentos Procesados: {reporte['resumen']['documentos_procesados']}")
    
    if reporte['analisis_entrevistas']:
        sentimiento_promedio = sum([ae['sentimiento']['compound'] for ae in reporte['analisis_entrevistas']]) / len(reporte['analisis_entrevistas'])
        print(f"Sentimiento Promedio de Entrevistas: {sentimiento_promedio:.2f}")
    
    if reporte['sintesis']['requisitos_consolidados']:
        print(f"Requisitos Consolidados: {len(reporte['sintesis']['requisitos_consolidados'])}")
    
    # Exportar datos
    analizador.exportar_datos_elicitacion('datos_elicitacion_muestra.json')
    
    # Crear visualizaciones
    analizador.crear_visualizaciones_elicitacion()
    
    print("\nAnálisis de elicitación completado!")
```

### Paso 5: Documentación
Este laboratorio comprehensivo cubre todas las técnicas principales de elicitación de requisitos según ISO/IEC/IEEE 29148. El dashboard interactivo proporciona experiencia práctica con:

- **Gestión de Entrevistas**: Entrevistas estructuradas, generación de preguntas, análisis de respuestas
- **Constructor de Cuestionarios**: Diseño de encuestas, recolección de respuestas, análisis estadístico
- **Herramientas de Observación**: Registro de actividades, análisis de flujo de trabajo, identificación de cuellos de botella
- **Análisis de Documentos**: Extracción de requisitos, análisis de brechas, consolidación
- **Prototipado para Validación**: Prototipos interactivos, recolección de retroalimentación de usuarios
- **Integración de Técnicas**: Síntesis multi-técnica, resolución de conflictos, priorización

La herramienta de análisis Python proporciona análisis automatizado de todos los tipos de datos de elicitación, incluyendo análisis de sentimiento, extracción de temas, análisis estadístico, y reportes comprehensivos con visualizaciones. Este laboratorio sirve como base para entender las mejores prácticas de elicitación de requisitos y técnicas.
