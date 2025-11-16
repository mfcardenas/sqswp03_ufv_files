# Laboratorio 1: Introducción a la Ingeniería de Requisitos

## Solución

### Paso 1: Dashboard de Introducción a Requisitos
Crear un archivo `requirements_intro.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISO/IEC/IEEE 29148 - Introducción a Ingeniería de Requisitos</title>
    <link rel="stylesheet" href="requirements.css">
</head>
<body>
    <header>
        <h1>ISO/IEC/IEEE 29148: Ingeniería de Requisitos</h1>
        <nav>
            <button id="conceptsBtn">Conceptos Básicos</button>
            <button id="processBtn">Proceso ER</button>
            <button id="artifactsBtn">Artefactos de Requisitos</button>
            <button id="stakeholdersBtn">Análisis de Interesados</button>
            <button id="qualityBtn">Calidad de Requisitos</button>
            <button id="standardsBtn">Visión General de Estándares</button>
        </nav>
    </header>

    <main>
        <section class="core-concepts" id="conceptsSection">
            <h2>Conceptos Básicos de la Ingeniería de Requisitos</h2>
            
            <div class="concepts-grid">
                <div class="concept-card">
                    <h3>¿Qué es la Ingeniería de Requisitos?</h3>
                    <p>El proceso sistemático de desarrollar requisitos a través de un proceso iterativo de analizar, documentar, validar y gestionar los requisitos de software y sistema.</p>
                    <div class="concept-details">
                        <h4>Actividades Clave:</h4>
                        <ul>
                            <li>Elicitación de Requisitos</li>
                            <li>Análisis de Requisitos</li>
                            <li>Especificación de Requisitos</li>
                            <li>Validación de Requisitos</li>
                            <li>Gestión de Requisitos</li>
                        </ul>
                    </div>
                </div>
                
                <div class="concept-card">
                    <h3>Tipos de Requisitos</h3>
                    <div class="requirements-types">
                        <div class="req-type">
                            <h4>Requisitos Funcionales</h4>
                            <p>Qué debe hacer el sistema</p>
                            <ul>
                                <li>Reglas de negocio</li>
                                <li>Interacciones de usuario</li>
                                <li>Procesamiento de datos</li>
                                <li>Comportamientos del sistema</li>
                            </ul>
                        </div>
                        
                        <div class="req-type">
                            <h4>Requisitos No Funcionales</h4>
                            <p>Qué tan bien debe funcionar el sistema</p>
                            <ul>
                                <li>Rendimiento</li>
                                <li>Seguridad</li>
                                <li>Usabilidad</li>
                                <li>Confiabilidad</li>
                                <li>Escalabilidad</li>
                            </ul>
                        </div>
                        
                        <div class="req-type">
                            <h4>Restricciones</h4>
                            <p>Limitaciones y restricciones</p>
                            <ul>
                                <li>Restricciones técnicas</li>
                                <li>Restricciones de negocio</li>
                                <li>Restricciones regulatorias</li>
                                <li>Restricciones de presupuesto</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="concept-card">
                    <h3>Desafíos de la Ingeniería de Requisitos</h3>
                    <div class="challenges-list">
                        <div class="challenge-item">
                            <h4>Brecha de Comunicación</h4>
                            <p>Diferentes interesados usan terminología diferente</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Volatilidad de Requisitos</h4>
                            <p>Los requisitos cambian con el tiempo</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Ambigüedad</h4>
                            <p>Los requisitos pueden interpretarse de diferentes maneras</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Incompletitud</h4>
                            <p>Faltan requisitos o no están especificados</p>
                        </div>
                        
                        <div class="challenge-item">
                            <h4>Trazabilidad</h4>
                            <p>Mantener vínculos entre requisitos y otros artefactos</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="re-process" id="processSection" style="display: none;">
            <h2>Proceso de Ingeniería de Requisitos (ISO/IEC/IEEE 29148)</h2>
            
            <div class="process-overview">
                <h3>Ciclo de Vida de la Ingeniería de Requisitos</h3>
                <div class="process-diagram">
                    <div class="process-step" data-step="1">
                        <h4>Elicitación de Requisitos</h4>
                        <p>Identificar y recopilar requisitos de interesados</p>
                        <div class="step-details">
                            <h5>Técnicas:</h5>
                            <ul>
                                <li>Entrevistas</li>
                                <li>Talleres</li>
                                <li>Cuestionarios</li>
                                <li>Observación</li>
                                <li>Análisis de Documentos</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="2">
                        <h4>Análisis de Requisitos</h4>
                        <p>Analizar y refinar requisitos elicitados</p>
                        <div class="step-details">
                            <h5>Actividades:</h5>
                            <ul>
                                <li>Clasificación de requisitos</li>
                                <li>Resolución de conflictos</li>
                                <li>Priorización</li>
                                <li>Análisis de viabilidad</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="3">
                        <h4>Especificación de Requisitos</h4>
                        <p>Documentar requisitos en formato apropiado</p>
                        <div class="step-details">
                            <h5>Artefactos:</h5>
                            <ul>
                                <li>Documento de Especificación de Requisitos de Software</li>
                                <li>Especificaciones de Casos de Uso</li>
                                <li>Historias de Usuario</li>
                                <li>Matriz de Trazabilidad de Requisitos</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="4">
                        <h4>Validación de Requisitos</h4>
                        <p>Asegurar que los requisitos sean correctos y completos</p>
                        <div class="step-details">
                            <h5>Técnicas de Validación:</h5>
                            <ul>
                                <li>Revisiones de requisitos</li>
                                <li>Prototipado</li>
                                <li>Pruebas de requisitos</li>
                                <li>Definición de criterios de aceptación</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="process-step" data-step="5">
                        <h4>Gestión de Requisitos</h4>
                        <p>Mantener requisitos a lo largo del ciclo de vida</p>
                        <div class="step-details">
                            <h5>Actividades de Gestión:</h5>
                            <ul>
                                <li>Control de cambios</li>
                                <li>Control de versiones</li>
                                <li>Mantenimiento de trazabilidad</li>
                                <li>Métricas de requisitos</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="process-tools">
                <h3>Herramientas de Soporte al Proceso</h3>
                <div class="tool-buttons">
                    <button class="tool-btn" data-tool="elicitation">Planificador de Elicitación</button>
                    <button class="tool-btn" data-tool="analysis">Analizador de Requisitos</button>
                    <button class="tool-btn" data-tool="validation">Lista de Verificación de Validación</button>
                    <button class="tool-btn" data-tool="traceability">Constructor de Trazabilidad</button>
                </div>
                
                <div class="tool-results" id="toolResults" style="display: none;">
                    <h4>Resultados de Herramientas</h4>
                    <div id="resultsContent"></div>
                </div>
            </div>
        </section>

        <section class="requirements-artifacts" id="artifactsSection" style="display: none;">
            <h2>Artefactos de Requisitos</h2>
            
            <div class="artifacts-overview">
                <h3>Documentos Comunes de Requisitos</h3>
                
                <div class="artifact-templates">
                    <div class="artifact-card">
                        <h4>Especificación de Requisitos de Software (ERS)</h4>
                        <p>Documento comprehensivo que contiene todos los requisitos de software</p>
                        <div class="artifact-structure">
                            <h5>Estructura Típica:</h5>
                            <ol>
                                <li>Introducción</li>
                                <li>Descripción General</li>
                                <li>Requisitos Específicos</li>
                                <li>Apéndices</li>
                            </ol>
                        </div>
                        <button class="template-btn" data-template="srs">Ver Plantilla</button>
                    </div>
                    
                    <div class="artifact-card">
                        <h4>Especificación de Caso de Uso</h4>
                        <p>Descripción detallada de interacciones sistema-usuario</p>
                        <div class="artifact-structure">
                            <h5>Elementos:</h5>
                            <ul>
                                <li>Nombre del Caso de Uso</li>
                                <li>Actores</li>
                                <li>Precondiciones</li>
                                <li>Flujo Principal</li>
                                <li>Flujos Alternativos</li>
                                <li>Postcondiciones</li>
                            </ul>
                        </div>
                        <button class="template-btn" data-template="usecase">Ver Plantilla</button>
                    </div>
                    
                    <div class="artifact-card">
                        <h4>Historia de Usuario</h4>
                        <p>Descripción simple y centrada en el usuario de un requisito</p>
                        <div class="artifact-structure">
                            <h5>Formato:</h5>
                            <p><strong>Como un</strong> [tipo de usuario], <strong>quiero</strong> [algún objetivo] <strong>para que</strong> [alguna razón]</p>
                            <h5>Criterios de Aceptación:</h5>
                            <ul>
                                <li>Dado [contexto]</li>
                                <li>Cuando [acción]</li>
                                <li>Entonces [resultado]</li>
                            </ul>
                        </div>
                        <button class="template-btn" data-template="userstory">Ver Plantilla</button>
                    </div>
                    
                    <div class="artifact-card">
                        <h4>Matriz de Trazabilidad de Requisitos</h4>
                        <p>Vincula requisitos con otros artefactos de desarrollo</p>
                        <div class="artifact-structure">
                            <h5>Columnas Típicas:</h5>
                            <ul>
                                <li>ID de Requisito</li>
                                <li>Descripción</li>
                                <li>Fuente</li>
                                <li>Caso de Prueba</li>
                                <li>Elemento de Diseño</li>
                                <li>Módulo de Código</li>
                            </ul>
                        </div>
                        <button class="template-btn" data-template="rtm">Ver Plantilla</button>
                    </div>
                </div>
                
                <div class="template-viewer" id="templateViewer" style="display: none;">
                    <h4>Vista Previa de Plantilla</h4>
                    <div id="templateContent"></div>
                    <button id="closeTemplate">Cerrar</button>
                </div>
            </div>
        </section>

        <section class="stakeholder-analysis" id="stakeholdersSection" style="display: none;">
            <h2>Análisis de Interesados</h2>
            
            <div class="stakeholder-tools">
                <h3>Identificación y Análisis de Interesados</h3>
                
                <div class="stakeholder-input">
                    <h4>Agregar Interesado</h4>
                    <form id="stakeholderForm">
                        <div class="form-group">
                            <label for="stakeholderName">Nombre:</label>
                            <input type="text" id="stakeholderName" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="stakeholderRole">Rol:</label>
                            <input type="text" id="stakeholderRole" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="stakeholderInterest">Nivel de Interés:</label>
                            <select id="stakeholderInterest">
                                <option value="high">Alto</option>
                                <option value="medium">Medio</option>
                                <option value="low">Bajo</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="stakeholderInfluence">Nivel de Influencia:</label>
                            <select id="stakeholderInfluence">
                                <option value="high">Alto</option>
                                <option value="medium">Medio</option>
                                <option value="low">Bajo</option>
                            </select>
                        </div>
                        
                        <button type="submit">Agregar Interesado</button>
                    </form>
                </div>
                
                <div class="stakeholder-list">
                    <h4>Mapa de Interesados</h4>
                    <div id="stakeholderMap"></div>
                </div>
                
                <div class="power-interest-grid">
                    <h4>Cuadrante Poder-Interés</h4>
                    <div class="grid-container">
                        <div class="grid-quadrant" data-quadrant="high-high">
                            <h5>Alto Poder, Alto Interés</h5>
                            <p>Jugadores Clave - Gestionar de cerca</p>
                            <div class="stakeholder-items" id="quadrant-high-high"></div>
                        </div>
                        
                        <div class="grid-quadrant" data-quadrant="high-low">
                            <h5>Alto Poder, Bajo Interés</h5>
                            <p>Mantener Satisfechos</p>
                            <div class="stakeholder-items" id="quadrant-high-low"></div>
                        </div>
                        
                        <div class="grid-quadrant" data-quadrant="low-high">
                            <h5>Bajo Poder, Alto Interés</h5>
                            <p>Mantener Informados</p>
                            <div class="stakeholder-items" id="quadrant-low-high"></div>
                        </div>
                        
                        <div class="grid-quadrant" data-quadrant="low-low">
                            <h5>Bajo Poder, Bajo Interés</h5>
                            <p>Monitorear</p>
                            <div class="stakeholder-items" id="quadrant-low-low"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="requirements-quality" id="qualitySection" style="display: none;">
            <h2>Evaluación de Calidad de Requisitos</h2>
            
            <div class="quality-framework">
                <h3>Criterios de Calidad de Requisitos (ISO/IEC/IEEE 29148)</h3>
                
                <div class="quality-criteria">
                    <div class="quality-category">
                        <h4>Completitud</h4>
                        <p>Todos los requisitos están definidos y no faltan requisitos necesarios</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> Todos los requisitos funcionales especificados</label>
                            <label><input type="checkbox"> Todos los requisitos no funcionales especificados</label>
                            <label><input type="checkbox"> Todas las restricciones identificadas</label>
                            <label><input type="checkbox"> Respuesta a todas las entradas definida</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Consistencia</h4>
                        <p>Los requisitos no se contradicen entre sí</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> No hay requisitos contradictorios</label>
                            <label><input type="checkbox"> Terminología consistente utilizada</label>
                            <label><input type="checkbox"> Formato y estructura consistentes</label>
                            <label><input type="checkbox"> Nivel consistente de detalle</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Claridad</h4>
                        <p>Los requisitos son inequívocos y comprensibles</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> Lenguaje claro y conciso</label>
                            <label><input type="checkbox"> Términos inequívocos</label>
                            <label><input type="checkbox"> Criterios medibles</label>
                            <label><input type="checkbox"> Requisitos testeables</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Corrección</h4>
                        <p>Los requisitos reflejan con precisión las necesidades de los interesados</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> Validados con interesados</label>
                            <label><input type="checkbox"> Alineados con objetivos de negocio</label>
                            <label><input type="checkbox"> Viables técnicamente</label>
                            <label><input type="checkbox"> Cumplidores con estándares</label>
                        </div>
                    </div>
                    
                    <div class="quality-category">
                        <h4>Trazabilidad</h4>
                        <p>Los requisitos pueden trazarse a fuentes e implementaciones</p>
                        <div class="quality-checklist">
                            <label><input type="checkbox"> Identificadores únicos asignados</label>
                            <label><input type="checkbox"> Fuente documentada</label>
                            <label><input type="checkbox"> Vínculos a elementos de diseño</label>
                            <label><input type="checkbox"> Vínculos a casos de prueba</label>
                        </div>
                    </div>
                </div>
                
                <div class="quality-assessment">
                    <h4>Resultados de Evaluación de Calidad</h4>
                    <div class="assessment-results">
                        <div class="quality-score">
                            <span class="score-label">Puntuación General de Calidad:</span>
                            <span class="score-value" id="qualityScore">0%</span>
                        </div>
                        <button id="assessQuality">Evaluar Calidad</button>
                    </div>
                </div>
            </div>
        </section>

        <section class="standards-overview" id="standardsSection" style="display: none;">
            <h2>Visión General de Estándares ISO/IEC/IEEE 29148</h2>
            
            <div class="standards-content">
                <h3>Estructura y Contenido del Estándar</h3>
                
                <div class="standard-sections">
                    <div class="standard-card">
                        <h4>Sección 1: Alcance</h4>
                        <p>Define el alcance y propósito del estándar</p>
                        <ul>
                            <li>Procesos de ingeniería de requisitos</li>
                            <li>Artefactos de requisitos</li>
                            <li>Gestión de requisitos</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Sección 2: Referencias Normativas</h4>
                        <p>Referencias a otros estándares y documentos</p>
                        <ul>
                            <li>ISO/IEC 12207 - Ciclo de Vida del Software</li>
                            <li>ISO/IEC 15288 - Ciclo de Vida del Sistema</li>
                            <li>IEEE 830 - Requisitos de Software</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Sección 3: Términos y Definiciones</h4>
                        <p>Definiciones de términos y conceptos clave</p>
                        <ul>
                            <li>Ingeniería de requisitos</li>
                            <li>Interesado</li>
                            <li>Trazabilidad de requisitos</li>
                            <li>Validación de requisitos</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Sección 4: Proceso de Ingeniería de Requisitos</h4>
                        <p>Procesos y actividades principales</p>
                        <ul>
                            <li>Elicitación de requisitos</li>
                            <li>Análisis de requisitos</li>
                            <li>Especificación de requisitos</li>
                            <li>Validación de requisitos</li>
                            <li>Gestión de requisitos</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Sección 5: Artefactos de Requisitos</h4>
                        <p>Documentos y entregables</p>
                        <ul>
                            <li>Especificación de requisitos</li>
                            <li>Matriz de trazabilidad de requisitos</li>
                            <li>Solicitudes de cambio de requisitos</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>Anexos</h4>
                        <p>Información de soporte y ejemplos</p>
                        <ul>
                            <li>Plantillas de requisitos</li>
                            <li>Ejemplos de procesos</li>
                            <li>Mejores prácticas</li>
                        </ul>
                    </div>
                </div>
                
                <div class="standard-benefits">
                    <h4>Beneficios de Seguir ISO/IEC/IEEE 29148</h4>
                    <div class="benefits-grid">
                        <div class="benefit-item">
                            <h5>Calidad Mejorada</h5>
                            <p>Mejores requisitos llevan a mejor software</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Menor Riesgo</h5>
                            <p>Identificación temprana de problemas y conflictos</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Mejor Comunicación</h5>
                            <p>Requisitos claros mejoran el entendimiento de los interesados</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Ahorro de Costos</h5>
                            <p>Menos defectos y retrabajo</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Cumplimiento</h5>
                            <p>Cumple estándares de la industria y regulaciones</p>
                        </div>
                        
                        <div class="benefit-item">
                            <h5>Trazabilidad</h5>
                            <p>Mejor seguimiento de requisitos a lo largo del ciclo de vida</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="requirements.js"></script>
</body>
</html>
```

### Paso 2: CSS para Dashboard de Ingeniería de Requisitos
Crear un archivo `requirements.css`:

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

/* Sección de Conceptos Básicos */
.concepts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.concept-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.requirements-types {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.req-type {
    background-color: white;
    padding: 1rem;
    border-radius: 6px;
    border: 1px solid #dee2e6;
}

.challenges-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.challenge-item {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    padding: 1rem;
    border-radius: 6px;
}

.challenge-item h4 {
    margin-top: 0;
    color: #856404;
}

/* Sección de Proceso */
.process-diagram {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.process-step {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    position: relative;
}

.process-step::before {
    content: attr(data-step);
    position: absolute;
    top: -10px;
    left: -10px;
    background-color: #3498db;
    color: white;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}

.step-details {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid #dee2e6;
}

.tool-buttons {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin: 2rem 0;
}

.tool-btn {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.tool-btn:hover {
    background-color: #2980b9;
}

/* Sección de Artefactos */
.artifact-templates {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.artifact-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.template-btn {
    background-color: #27ae60;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
    transition: background-color 0.3s ease;
}

.template-btn:hover {
    background-color: #229954;
}

.template-viewer {
    background-color: #f8f9fa;
    padding: 2rem;
    border-radius: 8px;
    margin-top: 2rem;
    border: 1px solid #dee2e6;
}

/* Sección de Análisis de Interesados */
.stakeholder-input {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    border: 1px solid #dee2e6;
}

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
}

.stakeholder-input button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.stakeholder-input button:hover {
    background-color: #2980b9;
}

.power-interest-grid {
    margin-top: 2rem;
}

.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 1rem;
    height: 400px;
}

.grid-quadrant {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    position: relative;
}

.grid-quadrant h5 {
    margin-top: 0;
    color: #2c3e50;
}

.stakeholder-items {
    margin-top: 1rem;
}

.stakeholder-item {
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    font-size: 0.9rem;
}

/* Sección de Calidad de Requisitos */
.quality-criteria {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.quality-category {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.quality-checklist {
    margin-top: 1rem;
}

.quality-checklist label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.assessment-results {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 2rem;
    border: 1px solid #dee2e6;
    text-align: center;
}

.quality-score {
    margin-bottom: 1rem;
}

.score-label {
    font-weight: bold;
    margin-right: 1rem;
}

.score-value {
    font-size: 1.5rem;
    color: #27ae60;
    font-weight: bold;
}

.assessment-results button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.assessment-results button:hover {
    background-color: #2980b9;
}

/* Sección de Visión General de Estándares */
.standard-sections {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.standard-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 2rem;
}

.benefit-item {
    background-color: #d4edda;
    padding: 1rem;
    border-radius: 6px;
    text-align: center;
    border: 1px solid #c3e6cb;
}

.benefit-item h5 {
    margin-top: 0;
    color: #155724;
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
    
    .concepts-grid, .process-diagram, .artifact-templates, 
    .quality-criteria, .standard-sections, .requirements-types,
    .challenges-list, .benefits-grid {
        grid-template-columns: 1fr;
    }
    
    .grid-container {
        grid-template-columns: 1fr;
        grid-template-rows: repeat(4, 1fr);
        height: auto;
    }
}
```

### Paso 3: JavaScript para Dashboard de Ingeniería de Requisitos
Crear un archivo `requirements.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Sistema de navegación
    const sections = {
        concepts: document.getElementById('conceptsSection'),
        process: document.getElementById('processSection'),
        artifacts: document.getElementById('artifactsSection'),
        stakeholders: document.getElementById('stakeholdersSection'),
        quality: document.getElementById('qualitySection'),
        standards: document.getElementById('standardsSection')
    };
    
    // Botones de navegación
    document.getElementById('conceptsBtn').addEventListener('click', () => showSection('concepts'));
    document.getElementById('processBtn').addEventListener('click', () => showSection('process'));
    document.getElementById('artifactsBtn').addEventListener('click', () => showSection('artifacts'));
    document.getElementById('stakeholdersBtn').addEventListener('click', () => showSection('stakeholders'));
    document.getElementById('qualityBtn').addEventListener('click', () => showSection('quality'));
    document.getElementById('standardsBtn').addEventListener('click', () => showSection('standards'));
    
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
    
    // Gestión de interesados
    let stakeholders = [];
    
    document.getElementById('stakeholderForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('stakeholderName').value;
        const role = document.getElementById('stakeholderRole').value;
        const interest = document.getElementById('stakeholderInterest').value;
        const influence = document.getElementById('stakeholderInfluence').value;
        
        const stakeholder = {
            id: Date.now(),
            name: name,
            role: role,
            interest: interest,
            influence: influence
        };
        
        stakeholders.push(stakeholder);
        updateStakeholderDisplay();
        
        // Reiniciar formulario
        this.reset();
        showNotification(`Agregado interesado: ${name}`);
    });
    
    function updateStakeholderDisplay() {
        // Limpiar todos los cuadrantes
        document.querySelectorAll('.stakeholder-items').forEach(quadrant => {
            quadrant.innerHTML = '';
        });
        
        // Agregar interesados a cuadrantes apropiados
        stakeholders.forEach(stakeholder => {
            const quadrantId = `quadrant-${stakeholder.influence}-${stakeholder.interest}`;
            const quadrant = document.getElementById(quadrantId);
            
            if (quadrant) {
                const item = document.createElement('div');
                item.className = 'stakeholder-item';
                item.textContent = `${stakeholder.name} (${stakeholder.role})`;
                quadrant.appendChild(item);
            }
        });
    }
    
    // Visor de plantillas
    document.querySelectorAll('.template-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const templateType = this.dataset.template;
            showTemplate(templateType);
        });
    });
    
    document.getElementById('closeTemplate').addEventListener('click', function() {
        document.getElementById('templateViewer').style.display = 'none';
    });
    
    function showTemplate(templateType) {
        const viewer = document.getElementById('templateViewer');
        const content = document.getElementById('templateContent');
        
        let templateContent = '';
        
        switch(templateType) {
            case 'srs':
                templateContent = getSRSTemplate();
                break;
            case 'usecase':
                templateContent = getUseCaseTemplate();
                break;
            case 'userstory':
                templateContent = getUserStoryTemplate();
                break;
            case 'rtm':
                templateContent = getRTMTemplate();
                break;
        }
        
        content.innerHTML = templateContent;
        viewer.style.display = 'block';
    }
    
    function getSRSTemplate() {
        return `
            <h4>Plantilla de Especificación de Requisitos de Software</h4>
            <div class="template-content">
                <h5>1. Introducción</h5>
                <ul>
                    <li>1.1 Propósito</li>
                    <li>1.2 Alcance</li>
                    <li>1.3 Definiciones, Acrónimos y Abreviaturas</li>
                    <li>1.4 Referencias</li>
                    <li>1.5 Visión General</li>
                </ul>
                
                <h5>2. Descripción General</h5>
                <ul>
                    <li>2.1 Perspectiva del Producto</li>
                    <li>2.2 Funciones del Producto</li>
                    <li>2.3 Características del Usuario</li>
                    <li>2.4 Restricciones</li>
                    <li>2.5 Suposiciones y Dependencias</li>
                </ul>
                
                <h5>3. Requisitos Específicos</h5>
                <ul>
                    <li>3.1 Requisitos de Interfaz Externa</li>
                    <li>3.2 Requisitos Funcionales</li>
                    <li>3.3 Requisitos de Rendimiento</li>
                    <li>3.4 Restricciones de Diseño</li>
                    <li>3.5 Atributos del Sistema de Software</li>
                    <li>3.6 Otros Requisitos</li>
                </ul>
                
                <h5>Apéndices</h5>
                <ul>
                    <li>Apéndice A: Glosario</li>
                    <li>Apéndice B: Modelos de Análisis</li>
                    <li>Apéndice C: Lista de Problemas</li>
                </ul>
            </div>
        `;
    }
    
    function getUseCaseTemplate() {
        return `
            <h4>Plantilla de Especificación de Caso de Uso</h4>
            <div class="template-content">
                <h5>Caso de Uso: [Nombre del Caso de Uso]</h5>
                
                <h6>1. Descripción Breve</h6>
                <p>[Descripción breve del caso de uso]</p>
                
                <h6>2. Actores</h6>
                <ul>
                    <li>Actor Primario: [Nombre del actor primario]</li>
                    <li>Actores Secundarios: [Lista de actores secundarios]</li>
                </ul>
                
                <h6>3. Precondiciones</h6>
                <ul>
                    <li>[Precondición 1]</li>
                    <li>[Precondición 2]</li>
                </ul>
                
                <h6>4. Escenario de Éxito Principal</h6>
                <ol>
                    <li>El usuario [acción]</li>
                    <li>El sistema [respuesta]</li>
                    <li>El usuario [acción]</li>
                    <li>El sistema [respuesta]</li>
                </ol>
                
                <h6>5. Flujos Alternativos</h6>
                <ul>
                    <li>Flujo Alternativo 1: [Descripción]</li>
                    <li>Flujo Alternativo 2: [Descripción]</li>
                </ul>
                
                <h6>6. Flujos de Excepción</h6>
                <ul>
                    <li>Excepción 1: [Descripción]</li>
                    <li>Excepción 2: [Descripción]</li>
                </ul>
                
                <h6>7. Postcondiciones</h6>
                <ul>
                    <li>[Postcondición 1]</li>
                    <li>[Postcondición 2]</li>
                </ul>
                
                <h6>8. Reglas de Negocio</h6>
                <ul>
                    <li>[Regla de negocio 1]</li>
                    <li>[Regla de negocio 2]</li>
                </ul>
            </div>
        `;
    }
    
    function getUserStoryTemplate() {
        return `
            <h4>Plantilla de Historia de Usuario</h4>
            <div class="template-content">
                <h5>Formato de Historia de Usuario</h5>
                <div class="story-format">
                    <strong>Como un</strong> [tipo de usuario],<br>
                    <strong>quiero</strong> [algún objetivo]<br>
                    <strong>para que</strong> [alguna razón].
                </div>
                
                <h6>Ejemplo:</h6>
                <div class="story-example">
                    <strong>Como un</strong> cliente de banco,<br>
                    <strong>quiero</strong> transferir dinero entre mis cuentas,<br>
                    <strong>para que</strong> pueda gestionar mis finanzas fácilmente.
                </div>
                
                <h6>Criterios de Aceptación:</h6>
                <ul>
                    <li><strong>Dado</strong> que estoy conectado a mi cuenta</li>
                    <li><strong>Cuando</strong> selecciono transferir fondos</li>
                    <li><strong>Entonces</strong> debo ver los saldos de mis cuentas</li>
                    <li><strong>Y</strong> debo poder seleccionar cuentas origen y destino</li>
                    <li><strong>Y</strong> debo recibir confirmación de transferencia exitosa</li>
                </ul>
                
                <h6>Definición de Terminado:</h6>
                <ul>
                    <li>El código está escrito y revisado</li>
                    <li>Las pruebas unitarias están escritas y pasan</li>
                    <li>Los criterios de aceptación se cumplen</li>
                    <li>La documentación está actualizada</li>
                    <li>El propietario del producto acepta la historia</li>
                </ul>
            </div>
        `;
    }
    
    function getRTMTemplate() {
        return `
            <h4>Plantilla de Matriz de Trazabilidad de Requisitos</h4>
            <div class="template-content">
                <table class="rtm-table">
                    <thead>
                        <tr>
                            <th>ID Req</th>
                            <th>Descripción</th>
                            <th>Fuente</th>
                            <th>Prioridad</th>
                            <th>Caso Prueba</th>
                            <th>Elem Diseño</th>
                            <th>Mód Código</th>
                            <th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>REQ-001</td>
                            <td>El usuario debe poder iniciar sesión</td>
                            <td>Entrevista Interesado</td>
                            <td>Alta</td>
                            <td>TC-001</td>
                            <td>AuthController</td>
                            <td>AuthModule</td>
                            <td>Implementado</td>
                        </tr>
                        <tr>
                            <td>REQ-002</td>
                            <td>El sistema debe validar contraseña</td>
                            <td>Política Seguridad</td>
                            <td>Alta</td>
                            <td>TC-002</td>
                            <td>PasswordValidator</td>
                            <td>SecurityModule</td>
                            <td>Implementado</td>
                        </tr>
                        <tr>
                            <td>REQ-003</td>
                            <td>Tiempo respuesta < 2 segundos</td>
                            <td>Req Rendimiento</td>
                            <td>Media</td>
                            <td>TC-003</td>
                            <td>PerformanceMonitor</td>
                            <td>MonitoringModule</td>
                            <td>Probando</td>
                        </tr>
                    </tbody>
                </table>
                
                <h6>Tipos de Trazabilidad:</h6>
                <ul>
                    <li><strong>Trazabilidad Directa:</strong> De requisitos a diseño/código/pruebas</li>
                    <li><strong>Trazabilidad Inversa:</strong> Del código/pruebas de vuelta a requisitos</li>
                    <li><strong>Trazabilidad Horizontal:</strong> Entre requisitos del mismo nivel</li>
                </ul>
            </div>
        `;
    }
    
    // Evaluación de calidad
    document.getElementById('assessQuality').addEventListener('click', function() {
        const checkboxes = document.querySelectorAll('.quality-checklist input[type="checkbox"]');
        const checkedCount = document.querySelectorAll('.quality-checklist input[type="checkbox"]:checked').length;
        const totalCount = checkboxes.length;
        
        const score = Math.round((checkedCount / totalCount) * 100);
        document.getElementById('qualityScore').textContent = score + '%';
        
        showNotification(`Evaluación de calidad completada: ${score}%`);
    });
    
    // Herramientas de proceso
    document.querySelectorAll('.tool-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const toolType = this.dataset.tool;
            launchTool(toolType);
        });
    });
    
    function launchTool(toolType) {
        const resultsSection = document.getElementById('toolResults');
        const resultsContent = document.getElementById('resultsContent');
        
        // Mostrar sección de resultados
        resultsSection.style.display = 'block';
        
        // Generar resultados de herramienta basados en tipo
        let results = '';
        switch(toolType) {
            case 'elicitation':
                results = generateElicitationPlanner();
                break;
            case 'analysis':
                results = generateRequirementsAnalyzer();
                break;
            case 'validation':
                results = generateValidationChecklist();
                break;
            case 'traceability':
                results = generateTraceabilityBuilder();
                break;
        }
        
        resultsContent.innerHTML = results;
        showNotification(`Herramienta ${toolType} lanzada`);
        
        // Desplazar a resultados
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    function generateElicitationPlanner() {
        return `
            <h4>Herramienta de Planificación de Elicitación de Requisitos</h4>
            <div class="tool-results-content">
                <h5>Técnicas Recomendadas de Elicitación:</h5>
                <div class="technique-grid">
                    <div class="technique">
                        <h6>Entrevistas</h6>
                        <p>Discusiones uno a uno con interesados</p>
                        <ul>
                            <li>Mejor para: Requisitos detallados</li>
                            <li>Tiempo: 30-60 minutos por interesado</li>
                            <li>Preparación: Preguntas de entrevista</li>
                        </ul>
                    </div>
                    
                    <div class="technique">
                        <h6>Talleres</h6>
                        <p>Sesiones grupales con múltiples interesados</p>
                        <ul>
                            <li>Mejor para: Resolver conflictos</li>
                            <li>Tiempo: 2-4 horas</li>
                            <li>Preparación: Agenda y materiales</li>
                        </ul>
                    </div>
                    
                    <div class="technique">
                        <h6>Cuestionarios</h6>
                        <p>Encuestas estructuradas para grupos grandes</p>
                        <ul>
                            <li>Mejor para: Datos cuantitativos</li>
                            <li>Tiempo: 15-30 minutos por respondedor</li>
                            <li>Preparación: Preguntas claras</li>
                        </ul>
                    </div>
                    
                    <div class="technique">
                        <h6>Observación</h6>
                        <p>Observar a usuarios realizando sus tareas</p>
                        <ul>
                            <li>Mejor para: Entender flujos de trabajo</li>
                            <li>Tiempo: 1-2 horas por sesión</li>
                            <li>Preparación: Protocolo de observación</li>
                        </ul>
                    </div>
                </div>
                
                <h5>Plantilla de Plan de Elicitación:</h5>
                <div class="plan-template">
                    <h6>1. Identificación de Interesados</h6>
                    <ul>
                        <li>Listar todos los interesados potenciales</li>
                        <li>Priorizar basado en interés e influencia</li>
                        <li>Programar entrevistas/talleres</li>
                    </ul>
                    
                    <h6>2. Preparación</h6>
                    <ul>
                        <li>Desarrollar preguntas de entrevista</li>
                        <li>Preparar materiales de taller</li>
                        <li>Configurar logística de reuniones</li>
                    </ul>
                    
                    <h6>3. Ejecución</h6>
                    <ul>
                        <li>Conducir sesiones de elicitación</li>
                        <li>Tomar notas detalladas</li>
                        <li>Grabar audio/video si está permitido</li>
                    </ul>
                    
                    <h6>4. Seguimiento</h6>
                    <ul>
                        <li>Enviar resúmenes de reuniones</li>
                        <li>Clarificar cualquier ambigüedad</li>
                        <li>Programar sesiones de seguimiento si es necesario</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    function generateRequirementsAnalyzer() {
        return `
            <h4>Herramienta Analizadora de Requisitos</h4>
            <div class="tool-results-content">
                <h5>Marco de Análisis:</h5>
                <div class="analysis-framework">
                    <div class="analysis-step">
                        <h6>1. Clasificación de Requisitos</h6>
                        <ul>
                            <li>Funcionales vs No funcionales</li>
                            <li>De negocio vs Técnicos</li>
                            <li>Mandatorios vs Opcionales</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-step">
                        <h6>2. Resolución de Conflictos</h6>
                        <ul>
                            <li>Identificar requisitos conflictivos</li>
                            <li>Negociar con interesados</li>
                            <li>Documentar decisiones de resolución</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-step">
                        <h6>3. Priorización</h6>
                        <ul>
                            <li>Método MoSCoW (Debe, Debería, Podría, No)</li>
                            <li>Análisis Kano</li>
                            <li>Priorización basada en riesgo</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-step">
                        <h6>4. Análisis de Viabilidad</h6>
                        <ul>
                            <li>Viabilidad técnica</li>
                            <li>Viabilidad económica</li>
                            <li>Viabilidad operativa</li>
                            <li>Viabilidad de calendario</li>
                        </ul>
                    </div>
                </div>
                
                <h5>Lista de Verificación de Calidad de Requisitos:</h5>
                <div class="quality-checklist">
                    <h6>Completitud:</h6>
                    <ul>
                        <li>☐ Todos los requisitos funcionales especificados</li>
                        <li>☐ Todos los requisitos no funcionales especificados</li>
                        <li>☐ Todas las interfaces definidas</li>
                        <li>☐ Todas las restricciones identificadas</li>
                    </ul>
                    
                    <h6>Consistencia:</h6>
                    <ul>
                        <li>☐ No hay requisitos contradictorios</li>
                        <li>☐ Terminología consistente utilizada</li>
                        <li>☐ Nivel consistente de detalle</li>
                    </ul>
                    
                    <h6>Claridad:</h6>
                    <ul>
                        <li>☐ Lenguaje claro y conciso</li>
                        <li>☐ Términos inequívocos</li>
                        <li>☐ Criterios medibles</li>
                        <li>☐ Requisitos testeables</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    function generateValidationChecklist() {
        return `
            <h4>Lista de Verificación de Validación de Requisitos</h4>
            <div class="tool-results-content">
                <h5>Actividades de Validación:</h5>
                <div class="validation-activities">
                    <div class="activity">
                        <h6>Revisión de Requisitos</h6>
                        <ul>
                            <li>☐ Revisión por pares completada</li>
                            <li>☐ Revisión de interesados completada</li>
                            <li>☐ Revisión de expertos completada</li>
                            <li>☐ Comentarios de revisión abordados</li>
                        </ul>
                    </div>
                    
                    <div class="activity">
                        <h6>Prototipado</h6>
                        <ul>
                            <li>☐ Prototipos de UI desarrollados</li>
                            <li>☐ Retroalimentación de usuarios recolectada</li>
                            <li>☐ Prototipos validados con usuarios</li>
                            <li>☐ Requisitos actualizados basados en retroalimentación</li>
                        </ul>
                    </div>
                    
                    <div class="activity">
                        <h6>Pruebas de Requisitos</h6>
                        <ul>
                            <li>☐ Criterios de aceptación definidos</li>
                            <li>☐ Casos de prueba desarrollados</li>
                            <li>☐ Requisitos testeables</li>
                            <li>☐ Resultados de pruebas documentados</li>
                        </ul>
                    </div>
                </div>
                
                <h5>Lista de Verificación de Validación:</h5>
                <div class="validation-checklist">
                    <h6>Validación de Contenido:</h6>
                    <ul>
                        <li>☐ Los requisitos son completos</li>
                        <li>☐ Los requisitos son consistentes</li>
                        <li>☐ Los requisitos son inequívocos</li>
                        <li>☐ Los requisitos son viables</li>
                        <li>☐ Los requisitos son testeables</li>
                    </ul>
                    
                    <h6>Validación de Interesados:</h6>
                    <ul>
                        <li>☐ Todos los interesados representados</li>
                        <li>☐ Preocupaciones de interesados abordadas</li>
                        <li>☐ Requisitos aprobados por interesados</li>
                        <li>☐ Firma obtenida</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    function generateTraceabilityBuilder() {
        return `
            <h4>Constructor de Trazabilidad de Requisitos</h4>
            <div class="tool-results-content">
                <h5>Plantilla de Matriz de Trazabilidad:</h5>
                <div class="traceability-matrix">
                    <table class="traceability-table">
                        <thead>
                            <tr>
                                <th>ID Requisito</th>
                                <th>Descripción</th>
                                <th>Fuente</th>
                                <th>Elemento Diseño</th>
                                <th>Caso Prueba</th>
                                <th>Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>REQ-001</td>
                                <td>Autenticación de usuario</td>
                                <td>Entrevista Interesado</td>
                                <td>AuthController</td>
                                <td>TC-AUTH-001</td>
                                <td>Implementado</td>
                            </tr>
                            <tr>
                                <td>REQ-002</td>
                                <td>Encriptación de datos</td>
                                <td>Política Seguridad</td>
                                <td>EncryptionModule</td>
                                <td>TC-SEC-001</td>
                                <td>Probando</td>
                            </tr>
                            <tr>
                                <td>REQ-003</td>
                                <td>Tiempo respuesta < 2s</td>
                                <td>Req Rendimiento</td>
                                <td>PerformanceMonitor</td>
                                <td>TC-PERF-001</td>
                                <td>Pendiente</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <h5>Mejores Prácticas de Trazabilidad:</h5>
                <div class="traceability-practices">
                    <h6>Establecer Trazabilidad Temprano:</h6>
                    <ul>
                        <li>Definir estrategia de trazabilidad al inicio del proyecto</li>
                        <li>Identificar relaciones de trazabilidad</li>
                        <li>Configurar herramientas y procesos de trazabilidad</li>
                    </ul>
                    
                    <h6>Mantener Trazabilidad:</h6>
                    <ul>
                        <li>Actualizar trazabilidad conforme cambian requisitos</li>
                        <li>Revisar trazabilidad regularmente</li>
                        <li>Usar herramientas automatizadas cuando sea posible</li>
                    </ul>
                    
                    <h6>Verificar Trazabilidad:</h6>
                    <ul>
                        <li>Conducir auditorías de trazabilidad</li>
                        <li>Asegurar que todos los requisitos estén trazados</li>
                        <li>Validar precisión de trazabilidad</li>
                    </ul>
                </div>
            </div>
        `;
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
    
    // Inicializar con sección de conceptos visible
    showSection('concepts');
});
```

### Paso 4: Herramienta Python de Análisis de Requisitos
Crear un archivo `requirements_analyzer.py`:

```python
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
import re

class RequirementsAnalyzer:
    def __init__(self):
        self.requirements = []
        self.stakeholders = []
        self.traceability_matrix = {}
        self.quality_metrics = {}
    
    def load_requirements(self, file_path: str):
        """Cargar requisitos desde archivo JSON"""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.requirements = data.get('requirements', [])
            self.stakeholders = data.get('stakeholders', [])
    
    def add_requirement(self, req_id: str, description: str, req_type: str, 
                       priority: str, source: str) -> Dict[str, Any]:
        """Agregar un nuevo requisito al sistema"""
        requirement = {
            'id': req_id,
            'description': description,
            'type': req_type,
            'priority': priority,
            'source': source,
            'status': 'Draft',
            'created_date': datetime.now().isoformat(),
            'last_modified': datetime.now().isoformat(),
            'stakeholders': [],
            'test_cases': [],
            'design_elements': [],
            'quality_score': 0
        }
        
        self.requirements.append(requirement)
        return requirement
    
    def classify_requirements(self) -> Dict[str, List[Dict[str, Any]]]:
        """Clasificar requisitos por tipo y prioridad"""
        classification = {
            'functional': [],
            'non_functional': [],
            'constraints': [],
            'high_priority': [],
            'medium_priority': [],
            'low_priority': []
        }
        
        for req in self.requirements:
            # Clasificar por tipo
            if req['type'].lower() in ['functional', 'function']:
                classification['functional'].append(req)
            elif req['type'].lower() in ['non-functional', 'non_functional', 'quality']:
                classification['non_functional'].append(req)
            elif req['type'].lower() in ['constraint', 'limitation']:
                classification['constraints'].append(req)
            
            # Clasificar por prioridad
            if req['priority'].lower() == 'high':
                classification['high_priority'].append(req)
            elif req['priority'].lower() == 'medium':
                classification['medium_priority'].append(req)
            elif req['priority'].lower() == 'low':
                classification['low_priority'].append(req)
        
        return classification
    
    def assess_requirement_quality(self, requirement: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluar la calidad de un requisito"""
        quality_criteria = {
            'completeness': 0,
            'consistency': 0,
            'clarity': 0,
            'correctness': 0,
            'traceability': 0
        }
        
        description = requirement['description']
        
        # Verificación de completitud
        if len(description.split()) > 10:  # Tiene detalle suficiente
            quality_criteria['completeness'] = 1
        
        # Verificación de claridad
        if not self._has_ambiguous_terms(description):
            quality_criteria['clarity'] = 1
        
        # Verificación de trazabilidad
        if requirement.get('source') and requirement.get('stakeholders'):
            quality_criteria['traceability'] = 1
        
        # Verificación de consistencia (simplificada)
        quality_criteria['consistency'] = 1  # Asumir consistente por ahora
        
        # Verificación de corrección (simplificada)
        quality_criteria['correctness'] = 1  # Asumir correcto por ahora
        
        overall_score = sum(quality_criteria.values()) / len(quality_criteria)
        requirement['quality_score'] = overall_score
        
        return {
            'requirement_id': requirement['id'],
            'quality_score': overall_score,
            'criteria': quality_criteria,
            'recommendations': self._generate_quality_recommendations(quality_criteria)
        }
    
    def _has_ambiguous_terms(self, text: str) -> bool:
        """Verificar términos ambiguos en texto de requisito"""
        ambiguous_terms = [
            'flexible', 'robust', 'efficient', 'user-friendly', 
            'fast', 'reliable', 'scalable', 'etc', 'and so on'
        ]
        
        text_lower = text.lower()
        for term in ambiguous_terms:
            if term in text_lower:
                return True
        return False
    
    def _generate_quality_recommendations(self, criteria: Dict[str, int]) -> List[str]:
        """Generar recomendaciones de mejora de calidad"""
        recommendations = []
        
        if criteria['completeness'] == 0:
            recommendations.append("Agregar más detalle a la descripción del requisito")
        
        if criteria['clarity'] == 0:
            recommendations.append("Reemplazar términos ambiguos con criterios específicos y medibles")
        
        if criteria['traceability'] == 0:
            recommendations.append("Agregar información de fuente y referencias de interesados")
        
        return recommendations
    
    def build_traceability_matrix(self) -> Dict[str, Any]:
        """Construir matriz de trazabilidad de requisitos"""
        matrix = {
            'requirements': [],
            'design_elements': [],
            'test_cases': [],
            'relationships': []
        }
        
        for req in self.requirements:
            matrix['requirements'].append({
                'id': req['id'],
                'description': req['description'][:50] + '...',
                'status': req['status']
            })
            
            # Agregar elementos de diseño
            for design_element in req.get('design_elements', []):
                if design_element not in [de['id'] for de in matrix['design_elements']]:
                    matrix['design_elements'].append({
                        'id': design_element,
                        'type': 'Design Element'
                    })
                
                matrix['relationships'].append({
                    'from': req['id'],
                    'to': design_element,
                    'type': 'implements'
                })
            
            # Agregar casos de prueba
            for test_case in req.get('test_cases', []):
                if test_case not in [tc['id'] for tc in matrix['test_cases']]:
                    matrix['test_cases'].append({
                        'id': test_case,
                        'type': 'Test Case'
                    })
                
                matrix['relationships'].append({
                    'from': req['id'],
                    'to': test_case,
                    'type': 'verifies'
                })
        
        return matrix
    
    def generate_requirements_report(self) -> Dict[str, Any]:
        """Generar reporte comprehensivo de requisitos"""
        classification = self.classify_requirements()
        traceability = self.build_traceability_matrix()
        
        # Evaluación de calidad para todos los requisitos
        quality_assessments = []
        for req in self.requirements:
            assessment = self.assess_requirement_quality(req)
            quality_assessments.append(assessment)
        
        report = {
            'summary': {
                'total_requirements': len(self.requirements),
                'functional_requirements': len(classification['functional']),
                'non_functional_requirements': len(classification['non_functional']),
                'constraints': len(classification['constraints']),
                'high_priority': len(classification['high_priority']),
                'medium_priority': len(classification['medium_priority']),
                'low_priority': len(classification['low_priority'])
            },
            'classification': classification,
            'quality_assessment': {
                'overall_average': sum([qa['quality_score'] for qa in quality_assessments]) / len(quality_assessments) if quality_assessments else 0,
                'assessments': quality_assessments
            },
            'traceability': traceability,
            'generated_at': datetime.now().isoformat()
        }
        
        return report
    
    def create_stakeholder_map(self) -> Dict[str, List[Dict[str, Any]]]:
        """Crear mapa de poder-interés de interesados"""
        stakeholder_map = {
            'high_power_high_interest': [],
            'high_power_low_interest': [],
            'low_power_high_interest': [],
            'low_power_low_interest': []
        }
        
        for stakeholder in self.stakeholders:
            power = stakeholder.get('power', 'medium')
            interest = stakeholder.get('interest', 'medium')
            
            quadrant = f"{power}_power_{interest}_interest"
            if quadrant in stakeholder_map:
                stakeholder_map[quadrant].append(stakeholder)
        
        return stakeholder_map
    
    def analyze_requirements_volatility(self) -> Dict[str, Any]:
        """Analizar volatilidad de requisitos y patrones de cambio"""
        changes_by_month = defaultdict(int)
        changes_by_type = defaultdict(int)
        
        for req in self.requirements:
            if 'change_history' in req:
                for change in req['change_history']:
                    change_date = datetime.fromisoformat(change['date'])
                    month_key = f"{change_date.year}-{change_date.month:02d}"
                    changes_by_month[month_key] += 1
                    changes_by_type[change.get('type', 'unknown')] += 1
        
        return {
            'changes_by_month': dict(changes_by_month),
            'changes_by_type': dict(changes_by_type),
            'total_changes': sum(changes_by_month.values()),
            'volatility_index': sum(changes_by_month.values()) / len(self.requirements) if self.requirements else 0
        }
    
    def export_to_json(self, file_path: str):
        """Exportar datos de requisitos a archivo JSON"""
        data = {
            'requirements': self.requirements,
            'stakeholders': self.stakeholders,
            'exported_at': datetime.now().isoformat()
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        print(f"Requisitos exportados a {file_path}")
    
    def create_visualizations(self, save_path: str = 'requirements_analysis.png'):
        """Crear visualizaciones comprehensivas de análisis de requisitos"""
        if not self.requirements:
            print("No hay datos de requisitos disponibles para visualización")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Requisitos por tipo
        types = ['Funcional', 'No Funcional', 'Restricciones']
        counts = [
            len([r for r in self.requirements if r['type'].lower() in ['functional', 'function']]),
            len([r for r in self.requirements if r['type'].lower() in ['non-functional', 'non_functional', 'quality']]),
            len([r for r in self.requirements if r['type'].lower() in ['constraint', 'limitation']])
        ]
        
        bars1 = ax1.bar(types, counts, color=['blue', 'green', 'orange'])
        ax1.set_title('Requisitos por Tipo', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Conteo', fontsize=12)
        
        # Agregar etiquetas de valor
        for bar, count in zip(bars1, counts):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_y() + count + 0.1, 
                    str(count), ha='center', va='bottom', fontweight='bold')
        
        # Requisitos por prioridad
        priorities = ['Alta', 'Media', 'Baja']
        priority_counts = [
            len([r for r in self.requirements if r['priority'].lower() == 'high']),
            len([r for r in self.requirements if r['priority'].lower() == 'medium']),
            len([r for r in self.requirements if r['priority'].lower() == 'low'])
        ]
        
        bars2 = ax2.bar(priorities, priority_counts, color=['red', 'yellow', 'green'])
        ax2.set_title('Requisitos por Prioridad', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Conteo', fontsize=12)
        
        # Agregar etiquetas de valor
        for bar, count in zip(bars2, priority_counts):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_y() + count + 0.1, 
                    str(count), ha='center', va='bottom', fontweight='bold')
        
        # Estado de requisitos
        status_counts = defaultdict(int)
        for req in self.requirements:
            status_counts[req.get('status', 'Unknown')] += 1
        
        ax3.pie(status_counts.values(), labels=status_counts.keys(), autopct='%1.1f%%')
        ax3.set_title('Distribución de Estado de Requisitos', fontsize=14, fontweight='bold')
        
        # Puntuaciones de calidad
        quality_scores = [req.get('quality_score', 0) for req in self.requirements]
        ax4.hist(quality_scores, bins=10, edgecolor='black', alpha=0.7)
        ax4.set_title('Distribución de Calidad de Requisitos', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Puntuación de Calidad', fontsize=12)
        ax4.set_ylabel('Frecuencia', fontsize=12)
        ax4.axvline(sum(quality_scores)/len(quality_scores), color='red', linestyle='--', 
                   label=f'Promedio: {sum(quality_scores)/len(quality_scores):.2f}')
        ax4.legend()
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Visualizaciones de análisis de requisitos guardadas: {save_path}")

# Ejemplo de uso y datos de muestra
def create_sample_data():
    """Crear datos de muestra de requisitos para demostración"""
    analyzer = RequirementsAnalyzer()
    
    # Agregar requisitos de muestra
    analyzer.add_requirement('REQ-001', 
                           'El sistema debe permitir a los usuarios autenticarse usando nombre de usuario y contraseña',
                           'functional', 'high', 'Entrevista de Interesado')
    
    analyzer.add_requirement('REQ-002', 
                           'El sistema debe responder a acciones de usuario dentro de 2 segundos',
                           'non-functional', 'medium', 'Requisitos de Rendimiento')
    
    analyzer.add_requirement('REQ-003', 
                           'El sistema debe cumplir con regulaciones GDPR de protección de datos',
                           'constraint', 'high', 'Requisitos Legales')
    
    analyzer.add_requirement('REQ-004', 
                           'El sistema debe estar disponible 99.9% del tiempo',
                           'non-functional', 'high', 'Requisitos de Negocio')
    
    analyzer.add_requirement('REQ-005', 
                           'El sistema debe soportar al menos 1000 usuarios concurrentes',
                           'non-functional', 'medium', 'Requisitos de Escalabilidad')
    
    # Agregar interesados de muestra
    analyzer.stakeholders = [
        {'name': 'Juan Pérez', 'role': 'Gerente de Producto', 'power': 'high', 'interest': 'high'},
        {'name': 'María González', 'role': 'Desarrollador', 'power': 'medium', 'interest': 'medium'},
        {'name': 'Carlos Rodríguez', 'role': 'Usuario Final', 'power': 'low', 'interest': 'high'}
    ]
    
    return analyzer

if __name__ == "__main__":
    # Crear datos de muestra
    analyzer = create_sample_data()
    
    # Generar reporte
    report = analyzer.generate_requirements_report()
    
    print("Reporte de Análisis de Requisitos")
    print("=" * 50)
    print(f"Requisitos Totales: {report['summary']['total_requirements']}")
    print(f"Funcionales: {report['summary']['functional_requirements']}")
    print(f"No Funcionales: {report['summary']['non_functional_requirements']}")
    print(f"Restricciones: {report['summary']['constraints']}")
    print(f"Puntuación Promedio de Calidad: {report['quality_assessment']['overall_average']:.2f}")
    
    # Exportar datos
    analyzer.export_to_json('sample_requirements.json')
    
    # Crear visualizaciones
    analyzer.create_visualizations()
    
    print("\nAnálisis de muestra de requisitos completado!")
```

### Paso 5: Documentación
Este laboratorio comprehensivo cubre los conceptos fundamentales de Ingeniería de Requisitos según ISO/IEC/IEEE 29148. El dashboard interactivo proporciona experiencia práctica con:

- **Conceptos Básicos**: Tipos de requisitos, desafíos comunes y cómo abordarlos
- **Marco de Proceso**: Proceso completo de ER con herramientas interactivas
- **Artefactos**: Plantillas para ERS, casos de uso, historias de usuario y matriz de trazabilidad
- **Análisis de Interesados**: Mapeo de cuadrante poder-interés y gestión
- **Evaluación de Calidad**: Verificación automática de calidad y recomendaciones
- **Visión General de Estándares**: Estructura de ISO/IEC/IEEE 29148 y beneficios

La herramienta de análisis Python proporciona clasificación automatizada de requisitos, evaluación de calidad, construcción de trazabilidad y reportes comprehensivos con visualizaciones. Este laboratorio sirve como base para entender principios y prácticas de ingeniería de requisitos.
