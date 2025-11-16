# Laboratorio 10: Estudio de Caso

## Solución

### Paso 1: Panel HTML del Estudio de Caso
Crear un archivo `case_study.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estudio de Caso Integral ISO 9241 - Laboratorio</title>
    <link rel="stylesheet" href="case.css">
</head>
<body>
    <header>
        <h1>Estudio de Caso Integral ISO 9241</h1>
        <nav>
            <button id="scenarioBtn">Escenario de Caso</button>
            <button id="assessmentBtn">Marco de Evaluación</button>
            <button id="evaluationBtn">Herramientas de Evaluación</button>
            <button id="integrationBtn">Integración de Estándares</button>
            <button id="reportsBtn">Reportes y Hallazgos</button>
            <button id="recommendationsBtn">Recomendaciones</button>
        </nav>
    </header>

    <main>
        <section class="case-scenario" id="scenarioSection">
            <h2>Escenario de Caso: Sistema de Salud Inteligente</h2>
            
            <div class="scenario-overview">
                <h3>Resumen del Proyecto</h3>
                <p>El Hospital General Metropolitano está implementando un sistema de salud inteligente integral que integra registros médicos electrónicos, sistemas de imagenología, monitoreo de pacientes y capacidades de telemedicina. El sistema sirve a 500+ profesionales de la salud y administra 10,000+ registros de pacientes diariamente.</p>
                
                <div class="project-details">
                    <div class="detail-card">
                        <h4>Componentes del Sistema</h4>
                        <ul>
                            <li>Sistema de Registros Médicos Electrónicos (EHR)</li>
                            <li>Sistema de Archivo y Comunicación de Imágenes (PACS)</li>
                            <li>Panel de Monitoreo de Pacientes</li>
                            <li>Plataforma de Telemedicina</li>
                            <li>Aplicaciones Móviles para Personal</li>
                            <li>Integración con Dispositivos Médicos</li>
                        </ul>
                    </div>
                    
                    <div class="detail-card">
                        <h4>Grupos de Usuarios</h4>
                        <ul>
                            <li>Médicos y Cirujanos</li>
                            <li>Enfermeras y Personal Clínico</li>
                            <li>Personal Administrativo</li>
                            <li>Soporte de TI</li>
                            <li>Pacientes y Familiares</li>
                        </ul>
                    </div>
                    
                    <div class="detail-card">
                        <h4>Requisitos Críticos</h4>
                        <ul>
                            <li>Disponibilidad del Sistema 24/7</li>
                            <li>Cumplimiento HIPAA</li>
                            <li>Precisión de Datos en Tiempo Real</li>
                            <li>Interfaces de Usuario Intuitivas</li>
                            <li>Diseño Ergonómico para Turnos Extendidos</li>
                            <li>Accesibilidad para Todos los Usuarios</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="challenges-identified">
                <h3>Desafíos Identificados</h3>
                <div class="challenges-grid">
                    <div class="challenge-item">
                        <h4>Preocupaciones Ergonómicas</h4>
                        <p>Los profesionales de la salud trabajan turnos de 12+ horas con intensa interacción computacional</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Problemas de Usabilidad</h4>
                        <p>Los flujos de trabajo complejos requieren interacciones eficientes y libres de errores bajo presión temporal</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Requisitos de Rendimiento</h4>
                        <p>Las decisiones de atención crítica dependen de los tiempos de respuesta del sistema y la precisión de los datos</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Estándares de Cumplimiento</h4>
                        <p>Múltiples requisitos regulatorios (HIPAA, ISO 9241, estándares de accesibilidad)</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Complejidad de Integración</h4>
                        <p>Múltiples sistemas y dispositivos deben trabajar perfectamente juntos</p>
                    </div>
                    
                    <div class="challenge-item">
                        <h4>Diversidad de Usuarios</h4>
                        <p>Amplio rango de niveles de experiencia de usuario y capacidades físicas</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="assessment-framework" id="assessmentSection" style="display: none;">
            <h2>Marco de Evaluación Integrado</h2>
            
            <div class="framework-overview">
                <h3>Enfoque de Evaluación Multi-Dimensional</h3>
                <p>Este estudio de caso integra todos los estándares ISO 9241 cubiertos en los laboratorios anteriores en un marco de evaluación integral.</p>
                
                <div class="standards-integration">
                    <div class="standard-card">
                        <h4>ISO 9241-110: Principios de Diálogo</h4>
                        <ul>
                            <li>Adecuación para la tarea</li>
                            <li>Autodescriptibilidad</li>
                            <li>Controlabilidad</li>
                            <li>Conformidad con las expectativas del usuario</li>
                            <li>Tolerancia a errores</li>
                            <li>Adecuación para la individualización</li>
                            <li>Adecuación para el aprendizaje</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>ISO 9241-210: Diseño Centrado en el Humano</h4>
                        <ul>
                            <li>Comprensión y especificación del contexto de uso</li>
                            <li>Especificación de los requisitos del usuario y la organización</li>
                            <li>Producción de soluciones de diseño</li>
                            <li>Evaluación de diseños contra requisitos</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>ISO 9241-303: Requisitos de Visualización</h4>
                        <ul>
                            <li>Calidad de visualización y legibilidad</li>
                            <li>Requisitos de legibilidad</li>
                            <li>Ergonómica visual</li>
                            <li>Verificación de cumplimiento</li>
                        </ul>
                    </div>
                    
                    <div class="standard-card">
                        <h4>ISO 9241-410: Estándares de Dispositivos de Entrada</h4>
                        <ul>
                            <li>Criterios de diseño ergonómico</li>
                            <li>Requisitos de fuerza de operación</li>
                            <li>Recorrido de tecla y retroalimentación táctil</li>
                            <li>Accesibilidad del dispositivo</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="evaluation-methodology">
                <h3>Metodología de Evaluación</h3>
                
                <div class="methodology-steps">
                    <div class="step">
                        <h4>Paso 1: Análisis de Contexto</h4>
                        <p>Analizar flujos de trabajo de atención médica, requisitos de usuario y restricciones del sistema</p>
                    </div>
                    
                    <div class="step">
                        <h4>Paso 2: Investigación de Usuario</h4>
                        <p>Realizar entrevistas, observaciones y pruebas de usabilidad con profesionales de la salud</p>
                    </div>
                    
                    <div class="step">
                        <h4>Paso 3: Mapeo de Estándares</h4>
                        <p>Mapear requisitos ISO 9241 a componentes específicos del sistema y casos de uso</p>
                    </div>
                    
                    <div class="step">
                        <h4>Paso 4: Ejecución de Evaluación</h4>
                        <p>Ejecutar evaluaciones integrales utilizando herramientas de evaluación integradas</p>
                    </div>
                    
                    <div class="step">
                        <h4>Paso 5: Integración de Hallazgos</h4>
                        <p>Integrar hallazgos en todos los estándares e identificar problemas sistémicos</p>
                    </div>
                    
                    <div class="step">
                        <h4>Paso 6: Desarrollo de Recomendaciones</h4>
                        <p>Desarrollar recomendaciones priorizadas para mejoras del sistema</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="evaluation-tools" id="evaluationSection" style="display: none;">
            <h2>Herramientas de Evaluación Integradas</h2>
            
            <div class="tools-overview">
                <h3>Kit de Herramientas de Evaluación Integral</h3>
                <p>Herramientas que integran múltiples estándares ISO 9241 para evaluación holística del sistema.</p>
                
                <div class="tool-categories">
                    <div class="tool-category">
                        <h4>Herramientas de Evaluación Ergonómica</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>Evaluador de Estación de Trabajo Ergonómica</h5>
                                <p>Evalúa configuración de escritorio, posicionamiento de monitor y colocación de dispositivos de entrada</p>
                                <button class="tool-btn" data-tool="workstation">Lanzar Herramienta</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Monitor de Fatiga de Turno</h5>
                                <p>Monitorea niveles de fatiga del usuario durante sesiones de trabajo extendidas</p>
                                <button class="tool-btn" data-tool="fatigue">Lanzar Herramienta</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tool-category">
                        <h4>Herramientas de Prueba de Usabilidad</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>Analizador de Eficiencia de Flujo de Trabajo</h5>
                                <p>Analiza eficiencia de flujo de trabajo clínico e identifica cuellos de botella</p>
                                <button class="tool-btn" data-tool="workflow">Lanzar Herramienta</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Escáner de Prevención de Errores</h5>
                                <p>Escanea el sistema en busca de condiciones de error potenciales y medidas de prevención</p>
                                <button class="tool-btn" data-tool="error">Lanzar Herramienta</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tool-category">
                        <h4>Herramientas de Monitoreo de Rendimiento</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>Monitor de Tiempo de Respuesta del Sistema</h5>
                                <p>Monitorea tiempos de respuesta del sistema en todas las funciones críticas</p>
                                <button class="tool-btn" data-tool="response">Lanzar Herramienta</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Validador de Precisión de Datos</h5>
                                <p>Valida precisión e integridad de datos en todo el sistema</p>
                                <button class="tool-btn" data-tool="accuracy">Lanzar Herramienta</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tool-category">
                        <h4>Herramientas de Verificación de Cumplimiento</h4>
                        <div class="tool-list">
                            <div class="tool-item">
                                <h5>Verificador de Cumplimiento ISO 9241</h5>
                                <p>Verificación automatizada de cumplimiento contra estándares ISO 9241</p>
                                <button class="tool-btn" data-tool="compliance">Lanzar Herramienta</button>
                            </div>
                            
                            <div class="tool-item">
                                <h5>Auditor de Accesibilidad</h5>
                                <p>Audita cumplimiento de accesibilidad del sistema</p>
                                <button class="tool-btn" data-tool="accessibility">Lanzar Herramienta</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="tool-results" id="toolResults" style="display: none;">
                <h3>Resultados de Herramientas</h3>
                <div id="resultsContent"></div>
            </div>
        </section>

        <section class="standards-integration" id="integrationSection" style="display: none;">
            <h2>Matriz de Integración de Estándares</h2>
            
            <div class="integration-matrix">
                <h3>Integración de Estándares ISO 9241</h3>
                <p>Cómo funcionan juntos diferentes estándares en el contexto del sistema de salud.</p>
                
                <table class="standards-table">
                    <thead>
                        <tr>
                            <th>Componente del Sistema</th>
                            <th>ISO 9241-110</th>
                            <th>ISO 9241-210</th>
                            <th>ISO 9241-303</th>
                            <th>ISO 9241-410</th>
                            <th>Notas de Integración</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Interfaz EHR</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>Integración completa requerida para seguridad del paciente</td>
                        </tr>
                        <tr>
                            <td>Estación de Trabajo PACS</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>Crítico para precisión diagnóstica</td>
                        </tr>
                        <tr>
                            <td>Monitor de Paciente</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✗</td>
                            <td>Estándares de visualización más críticos</td>
                        </tr>
                        <tr>
                            <td>Aplicaciones Móviles</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>Todos los estándares aplican al contexto móvil</td>
                        </tr>
                        <tr>
                            <td>Dispositivos Médicos</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>✓</td>
                            <td>Cumplimiento completo obligatorio</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="integration-analysis">
                <h3>Análisis de Integración</h3>
                
                <div class="analysis-cards">
                    <div class="analysis-card">
                        <h4>Fortalezas de la Integración</h4>
                        <ul>
                            <li>Cobertura integral de necesidades del usuario</li>
                            <li>Metodología de evaluación consistente</li>
                            <li>Identificación sistemática de problemas</li>
                            <li>Recomendaciones basadas en evidencia</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-card">
                        <h4>Desafíos de Integración</h4>
                        <ul>
                            <li>Complejidad de evaluación multi-estándar</li>
                            <li>Requisitos de recursos para evaluación integral</li>
                            <li>Coordinación entre diferentes áreas de experiencia</li>
                            <li>Equilibrar requisitos conflictivos</li>
                        </ul>
                    </div>
                    
                    <div class="analysis-card">
                        <h4>Mejores Prácticas</h4>
                        <ul>
                            <li>Comenzar con principios de diseño centrado en el usuario</li>
                            <li>Usar marcos de evaluación integrados</li>
                            <li>Establecer criterios de evaluación claros</li>
                            <li>Documentar todos los hallazgos sistemáticamente</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="reports-findings" id="reportsSection" style="display: none;">
            <h2>Reportes y Hallazgos del Estudio de Caso</h2>
            
            <div class="findings-overview">
                <h3>Resumen de Hallazgos Clave</h3>
                
                <div class="findings-metrics">
                    <div class="metric-card">
                        <h4>Puntaje General del Sistema</h4>
                        <div class="score-display">
                            <div class="score-value">78%</div>
                            <div class="score-bar">
                                <div class="score-fill" style="width: 78%"></div>
                            </div>
                        </div>
                        <p>Rendimiento bueno con espacio para mejora</p>
                    </div>
                    
                    <div class="metric-card">
                        <h4>Problemas Críticos Encontrados</h4>
                        <div class="issues-count">12</div>
                        <p>Problemas que requieren atención inmediata</p>
                    </div>
                    
                    <div class="metric-card">
                        <h4>Nivel de Cumplimiento</h4>
                        <div class="compliance-level">85%</div>
                        <p>Base sólida de cumplimiento</p>
                    </div>
                    
                    <div class="metric-card">
                        <h4>Satisfacción del Usuario</h4>
                        <div class="satisfaction-score">82%</div>
                        <p>Retroalimentación positiva del usuario generalmente</p>
                    </div>
                </div>
            </div>
            
            <div class="detailed-findings">
                <h3>Hallazgos Detallados por Categoría</h3>
                
                <div class="findings-categories">
                    <div class="findings-category">
                        <h4>Problemas Ergonómicos</h4>
                        <ul>
                            <li>Posicionamiento de monitor subóptimo para 40% de estaciones de trabajo</li>
                            <li>Bandejas de teclado no ajustables en 25% de ubicaciones</li>
                            <li>Ergonómica de silla inadecuada para turnos extendidos</li>
                            <li>Condiciones de iluminación causan fatiga visual en radiología</li>
                        </ul>
                    </div>
                    
                    <div class="findings-category">
                        <h4>Problemas de Usabilidad</h4>
                        <ul>
                            <li>Navegación EHR requiere 8+ clics para tareas comunes</li>
                            <li>Funcionalidad de búsqueda inconsistente entre módulos</li>
                            <li>Mensajes de error no amigables para el usuario</li>
                            <li>Requisitos de capacitación exceden tiempo disponible</li>
                        </ul>
                    </div>
                    
                    <div class="findings-category">
                        <h4>Problemas de Rendimiento</h4>
                        <ul>
                            <li>Carga de imágenes PACS toma 3-5 segundos en horas pico</li>
                            <li>Tiempo de respuesta del sistema se degrada bajo alta carga</li>
                            <li>Retrasos en sincronización de datos entre dispositivos</li>
                            <li>Rendimiento de aplicación móvil inconsistente en dispositivos antiguos</li>
                        </ul>
                    </div>
                    
                    <div class="findings-category">
                        <h4>Brezas de Cumplimiento</h4>
                        <ul>
                            <li>Relaciones de contraste de color por debajo de estándares WCAG en 3 módulos</li>
                            <li>Atajos de teclado no disponibles para usuarios con impedimentos motores</li>
                            <li>Registros de auditoría incompletos para requisitos regulatorios</li>
                            <li>Procedimientos de acceso de emergencia no documentados completamente</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="impact-analysis">
                <h3>Análisis de Impacto</h3>
                
                <div class="impact-matrix">
                    <table class="impact-table">
                        <thead>
                            <tr>
                                <th>Categoría de Problema</th>
                                <th>Gravedad</th>
                                <th>Impacto en Usuario</th>
                                <th>Seguridad del Paciente</th>
                                <th>Costo Operacional</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Problemas Ergonómicos</td>
                                <td>Medio</td>
                                <td>Alto</td>
                                <td>Medio</td>
                                <td>Medio</td>
                            </tr>
                            <tr>
                                <td>Problemas de Usabilidad</td>
                                <td>Alto</td>
                                <td>Alto</td>
                                <td>Alto</td>
                                <td>Alto</td>
                            </tr>
                            <tr>
                                <td>Problemas de Rendimiento</td>
                                <td>Alto</td>
                                <td>Medio</td>
                                <td>Alto</td>
                                <td>Medio</td>
                            </tr>
                            <tr>
                                <td>Brezas de Cumplimiento</td>
                                <td>Crítico</td>
                                <td>Medio</td>
                                <td>Crítico</td>
                                <td>Bajo</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <section class="recommendations" id="recommendationsSection" style="display: none;">
            <h2>Recomendaciones e Plan de Implementación</h2>
            
            <div class="priority-recommendations">
                <h3>Recomendaciones Prioritarias</h3>
                
                <div class="recommendation-phases">
                    <div class="phase">
                        <h4>Fase 1: Correcciones Críticas (0-3 meses)</h4>
                        <div class="recommendation-list">
                            <div class="recommendation-item priority-critical">
                                <h5>Corregir Problemas de Contraste de Color</h5>
                                <p>Actualizar esquemas de color UI para cumplir con estándares WCAG AA</p>
                                <span class="effort">Esfuerzo: Bajo</span>
                                <span class="impact">Impacto: Alto</span>
                            </div>
                            
                            <div class="recommendation-item priority-critical">
                                <h5>Optimizar Tiempos de Respuesta PACS</h5>
                                <p>Implementar estrategias de caché y optimizar consultas de base de datos</p>
                                <span class="effort">Esfuerzo: Medio</span>
                                <span class="impact">Impacto: Alto</span>
                            </div>
                            
                            <div class="recommendation-item priority-critical">
                                <h5>Mejorar Navegación EHR</h5>
                                <p>Rediseñar flujo de trabajo para reducir clics en 50%</p>
                                <span class="effort">Esfuerzo: Alto</span>
                                <span class="impact">Impacto: Alto</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="phase">
                        <h4>Fase 2: Mejoras Mayores (3-6 meses)</h4>
                        <div class="recommendation-list">
                            <div class="recommendation-item priority-high">
                                <h5>Actualizaciones de Estación de Trabajo Ergonómica</h5>
                                <p>Reemplazar equipo obsoleto y proporcionar muebles ajustables</p>
                                <span class="effort">Esfuerzo: Alto</span>
                                <span class="impact">Impacto: Medio</span>
                            </div>
                            
                            <div class="recommendation-item priority-high">
                                <h5>Programa de Capacitación Mejorado</h5>
                                <p>Desarrollar módulos de capacitación específicos por rol y guías de referencia rápida</p>
                                <span class="effort">Esfuerzo: Medio</span>
                                <span class="impact">Impacto: Alto</span>
                            </div>
                            
                            <div class="recommendation-item priority-high">
                                <h5>Optimización de Aplicación Móvil</h5>
                                <p>Mejorar rendimiento y agregar capacidades offline</p>
                                <span class="effort">Esfuerzo: Medio</span>
                                <span class="impact">Impacto: Medio</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="phase">
                        <h4>Fase 3: Mejoras a Largo Plazo (6-12 meses)</h4>
                        <div class="recommendation-list">
                            <div class="recommendation-item priority-medium">
                                <h5>Integración de Analítica Avanzada</h5>
                                <p>Implementar analítica predictiva para optimización del sistema</p>
                                <span class="effort">Esfuerzo: Alto</span>
                                <span class="impact">Impacto: Medio</span>
                            </div>
                            
                            <div class="recommendation-item priority-medium">
                                <h5>Características de Usabilidad Impulsadas por IA</h5>
                                <p>Agregar sugerencias inteligentes y flujos de trabajo automatizados</p>
                                <span class="effort">Esfuerzo: Alto</span>
                                <span class="impact">Impacto: Alto</span>
                            </div>
                            
                            <div class="recommendation-item priority-medium">
                                <h5>Auditoría Integral de Accesibilidad</h5>
                                <p>Programa completo de cumplimiento y pruebas de accesibilidad</p>
                                <span class="effort">Esfuerzo: Medio</span>
                                <span class="impact">Impacto: Medio</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="implementation-plan">
                <h3>Plan de Implementación</h3>
                
                <div class="implementation-timeline">
                    <div class="timeline-item">
                        <h4>Mes 1-2: Evaluación y Planificación</h4>
                        <ul>
                            <li>Completar análisis detallado de requisitos</li>
                            <li>Desarrollar mapa vial de implementación</li>
                            <li>Establecer métricas de éxito</li>
                            <li>Obtener aceptación de interesados</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Mes 3-4: Implementación de Correcciones Críticas</h4>
                        <ul>
                            <li>Desplegar recomendaciones de Fase 1</li>
                            <li>Realizar pruebas de aceptación de usuario</li>
                            <li>Proporcionar capacitación en nuevas características</li>
                            <li>Monitorear rendimiento del sistema</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Mes 5-8: Mejoras Mayores</h4>
                        <ul>
                            <li>Implementar recomendaciones de Fase 2</li>
                            <li>Realizar pruebas integrales</li>
                            <li>Implementar cambios en fases</li>
                            <li>Recopilar retroalimentación de usuario</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Mes 9-12: Optimización y Mejora</h4>
                        <ul>
                            <li>Desplegar características avanzadas</li>
                            <li>Optimizar rendimiento del sistema</li>
                            <li>Realizar evaluación final</li>
                            <li>Documentar lecciones aprendidas</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="success-metrics">
                <h3>Métricas de Éxito</h3>
                
                <div class="metrics-grid">
                    <div class="metric-item">
                        <h4>Satisfacción del Usuario</h4>
                        <p>Objetivo: 90% de satisfacción</p>
                        <p>Actual: 82%</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Tiempo de Finalización de Tarea</h4>
                        <p>Objetivo: 25% de reducción en tareas comunes</p>
                        <p>Actual: Línea base establecida</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Tasa de Error</h4>
                        <p>Objetivo: 50% de reducción en errores de usuario</p>
                        <p>Actual: Línea base establecida</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Tiempo de Actividad del Sistema</h4>
                        <p>Objetivo: 99.9% de disponibilidad</p>
                        <p>Actual: 99.5%</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Puntaje de Cumplimiento</h4>
                        <p>Objetivo: 95% de cumplimiento ISO 9241</p>
                        <p>Actual: 85%</p>
                    </div>
                    
                    <div class="metric-item">
                        <h4>Tiempo de Capacitación</h4>
                        <p>Objetivo: 30% de reducción en tiempo de capacitación</p>
                        <p>Actual: Línea base establecida</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="case.js"></script>
</body>
</html>
```

### Paso 2: CSS para Panel del Estudio de Caso
Crear un archivo `case.css`:

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
    background-color: #007bff;
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
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
}

nav button:hover, nav button:focus {
    background-color: rgba(255, 255, 255, 0.3);
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
    color: #495057;
    border-bottom: 2px solid #007bff;
    padding-bottom: 0.5rem;
    margin-bottom: 2rem;
}

h3 {
    color: #007bff;
    margin-bottom: 1rem;
}

h4 {
    color: #495057;
    margin-bottom: 0.5rem;
}

/* Sección de Escenario */
.project-details {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.detail-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.detail-card h4 {
    margin-top: 0;
    color: #007bff;
}

.detail-card ul {
    margin: 0;
    padding-left: 1.5rem;
}

.detail-card li {
    margin-bottom: 0.5rem;
}

.challenges-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.challenge-item {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    padding: 1.5rem;
    border-radius: 8px;
}

.challenge-item h4 {
    margin-top: 0;
    color: #856404;
}

/* Marco de Evaluación */
.standards-integration {
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

.standard-card h4 {
    margin-top: 0;
    color: #007bff;
}

.standard-card ul {
    margin: 0;
    padding-left: 1.5rem;
}

.methodology-steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.step {
    background-color: #e9ecef;
    padding: 1.5rem;
    border-radius: 8px;
    border-left: 4px solid #007bff;
}

.step h4 {
    margin-top: 0;
    color: #007bff;
}

/* Herramientas de Evaluación */
.tool-categories {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.tool-category h4 {
    color: #007bff;
    margin-bottom: 1rem;
}

.tool-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.tool-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.tool-item h5 {
    margin-top: 0;
    color: #495057;
}

.tool-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
    transition: background-color 0.3s ease;
}

.tool-btn:hover {
    background-color: #0056b3;
}

/* Integración de Estándares */
.standards-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background-color: white;
}

.standards-table th, .standards-table td {
    padding: 1rem;
    text-align: left;
    border: 1px solid #dee2e6;
}

.standards-table th {
    background-color: #f8f9fa;
    font-weight: bold;
    color: #495057;
}

.standards-table tr:nth-child(even) {
    background-color: #f8f9fa;
}

.analysis-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.analysis-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.analysis-card h4 {
    margin-top: 0;
    color: #007bff;
}

/* Reportes y Hallazgos */
.findings-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.metric-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    border: 1px solid #dee2e6;
}

.metric-card h4 {
    margin-top: 0;
    color: #007bff;
}

.score-display {
    margin: 1rem 0;
}

.score-value {
    font-size: 2.5rem;
    font-weight: bold;
    color: #007bff;
}

.score-bar {
    width: 100%;
    height: 20px;
    background-color: #e9ecef;
    border-radius: 10px;
    overflow: hidden;
    margin: 0.5rem 0;
}

.score-fill {
    height: 100%;
    background-color: #007bff;
    width: 0%;
    transition: width 0.3s ease;
}

.issues-count {
    font-size: 3rem;
    font-weight: bold;
    color: #dc3545;
}

.compliance-level, .satisfaction-score {
    font-size: 2.5rem;
    font-weight: bold;
    color: #28a745;
}

.findings-categories {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.findings-category {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.findings-category h4 {
    margin-top: 0;
    color: #007bff;
}

.impact-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background-color: white;
}

.impact-table th, .impact-table td {
    padding: 1rem;
    text-align: left;
    border: 1px solid #dee2e6;
}

.impact-table th {
    background-color: #f8f9fa;
    font-weight: bold;
    color: #495057;
}

/* Recomendaciones */
.recommendation-phases {
    margin: 2rem 0;
}

.phase {
    margin-bottom: 3rem;
}

.phase h4 {
    color: #007bff;
    border-bottom: 1px solid #dee2e6;
    padding-bottom: 0.5rem;
}

.recommendation-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.recommendation-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    position: relative;
}

.recommendation-item h5 {
    margin-top: 0;
    color: #495057;
}

.priority-critical {
    border-left: 4px solid #dc3545;
}

.priority-high {
    border-left: 4px solid #fd7e14;
}

.priority-medium {
    border-left: 4px solid #ffc107;
}

.effort, .impact {
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
    margin-right: 0.5rem;
    margin-top: 0.5rem;
}

.implementation-timeline {
    margin: 2rem 0;
}

.timeline-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    border-left: 4px solid #007bff;
}

.timeline-item h4 {
    margin-top: 0;
    color: #007bff;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.metric-item {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.metric-item h4 {
    margin-top: 0;
    color: #007bff;
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
    z-index: 1000;
}

/* Responsivo */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    nav {
        justify-content: center;
    }
    
    .project-details, .challenges-grid, .standards-integration, 
    .methodology-steps, .tool-categories, .analysis-cards,
    .findings-metrics, .findings-categories, .recommendation-list,
    .metrics-grid {
        grid-template-columns: 1fr;
    }
    
    .standards-table {
        font-size: 0.9rem;
    }
    
    .standards-table th, .standards-table td {
        padding: 0.5rem;
    }
    
    .impact-table {
        font-size: 0.9rem;
    }
    
    .impact-table th, .impact-table td {
        padding: 0.5rem;
    }
}
```

### Paso 3: JavaScript para Panel del Estudio de Caso
Crear un archivo `case.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Sistema de navegación
    const sections = {
        scenario: document.getElementById('scenarioSection'),
        assessment: document.getElementById('assessmentSection'),
        evaluation: document.getElementById('evaluationSection'),
        integration: document.getElementById('integrationSection'),
        reports: document.getElementById('reportsSection'),
        recommendations: document.getElementById('recommendationsSection')
    };
    
    // Botones de navegación
    document.getElementById('scenarioBtn').addEventListener('click', () => showSection('scenario'));
    document.getElementById('assessmentBtn').addEventListener('click', () => showSection('assessment'));
    document.getElementById('evaluationBtn').addEventListener('click', () => showSection('evaluation'));
    document.getElementById('integrationBtn').addEventListener('click', () => showSection('integration'));
    document.getElementById('reportsBtn').addEventListener('click', () => showSection('reports'));
    document.getElementById('recommendationsBtn').addEventListener('click', () => showSection('recommendations'));
    
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
    
    // Funcionalidad de lanzamiento de herramienta
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
            case 'workstation':
                results = generateWorkstationResults();
                break;
            case 'fatigue':
                results = generateFatigueResults();
                break;
            case 'workflow':
                results = generateWorkflowResults();
                break;
            case 'error':
                results = generateErrorResults();
                break;
            case 'response':
                results = generateResponseResults();
                break;
            case 'accuracy':
                results = generateAccuracyResults();
                break;
            case 'compliance':
                results = generateComplianceResults();
                break;
            case 'accessibility':
                results = generateAccessibilityResults();
                break;
            default:
                results = '<p>Los resultados de la herramienta se mostrarán aquí.</p>';
        }
        
        resultsContent.innerHTML = results;
        showNotification(`Herramienta ${toolType} lanzada`);
        
        // Desplazar a resultados
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    function generateWorkstationResults() {
        return `
            <h4>Resultados de Evaluación Ergonómica de Estación de Trabajo</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Posicionamiento de Monitor</h5>
                    <p>Puntaje: 75/100</p>
                    <p>Problemas: Altura de monitor subóptima para 40% de estaciones de trabajo</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 75%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Configuración de Teclado</h5>
                    <p>Puntaje: 68/100</p>
                    <p>Problemas: 25% carecen de bandejas de teclado ajustables</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 68%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Ergonómica de Silla</h5>
                    <p>Puntaje: 72/100</p>
                    <p>Problemas: Soporte inadecuado para turnos extendidos</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 72%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Condiciones de Iluminación</h5>
                    <p>Puntaje: 65/100</p>
                    <p>Problemas: Brillo y iluminación insuficiente</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 65%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Ajustar alturas de monitores a nivel de ojos</li>
                    <li>Instalar bandejas de teclado ajustables</li>
                    <li>Reemplazar sillas con modelos ergonómicos</li>
                    <li>Mejorar condiciones de iluminación</li>
                </ul>
            </div>
        `;
    }
    
    function generateFatigueResults() {
        return `
            <h4>Resultados de Monitoreo de Fatiga de Turno</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Niveles de Fatiga por Turno</h5>
                    <p>Aumento promedio de fatiga: 35% durante turnos de 12 horas</p>
                    <p> Pico de fatiga: Horas 8-12 del turno</p>
                </div>
                
                <div class="result-item">
                    <h5>Correlación de Errores</h5>
                    <p>45% aumento de errores durante períodos de alta fatiga</p>
                    <p>Tareas críticas más afectadas</p>
                </div>
                
                <div class="result-item">
                    <h5>Patrones de Recuperación</h5>
                    <p>Recuperación completa requiere 48-72 horas</p>
                    <p>Recuperación parcial con descansos de 24 horas</p>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Implementar horarios de descanso obligatorios</li>
                    <li>Rotar tareas de alta fatiga</li>
                    <li>Monitorear indicadores de fatiga</li>
                    <li>Proporcionar instalaciones de recuperación</li>
                </ul>
            </div>
        `;
    }
    
    function generateWorkflowResults() {
        return `
            <h4>Resultados de Análisis de Eficiencia de Flujo de Trabajo</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Eficiencia de Navegación EHR</h5>
                    <p>Clics promedio: 8.5 por tarea común</p>
                    <p>Objetivo: Máximo 4 clics</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 47%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Tiempo de Finalización de Tarea</h5>
                    <p>Actual: 12.5 minutos por registro de paciente</p>
                    <p>Objetivo: 8 minutos</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 64%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Cuellos de Botella de Flujo de Trabajo</h5>
                    <p>Cuello de botella principal: Orden de medicamentos (3.2 min retraso)</p>
                    <p>Segundo: Revisión de resultados de laboratorio (2.8 min retraso)</p>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Rediseñar navegación EHR</li>
                    <li>Implementar atajos de flujo de trabajo</li>
                    <li>Agilizar orden de medicamentos</li>
                    <li>Automatizar tareas rutinarias</li>
                </ul>
            </div>
        `;
    }
    
    function generateErrorResults() {
        return `
            <h4>Resultados de Análisis de Prevención de Errores</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Tipos de Error Identificados</h5>
                    <ul>
                        <li>Errores de entrada de datos: 45%</li>
                        <li>Errores de selección: 30%</li>
                        <li>Errores de navegación: 15%</li>
                        <li>Errores del sistema: 10%</li>
                    </ul>
                </div>
                
                <div class="result-item">
                    <h5>Evaluación de Riesgo</h5>
                    <p>Errores de alto riesgo: 12 identificados</p>
                    <p>Errores de riesgo medio: 28 identificados</p>
                    <p>Errores de bajo riesgo: 45 identificados</p>
                </div>
                
                <div class="result-item">
                    <h5>Medidas de Prevención</h5>
                    <p>Cobertura actual: 65%</p>
                    <p>Cobertura recomendada: 90%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 65%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Implementar validación de entrada</li>
                    <li>Agregar diálogos de confirmación para acciones críticas</li>
                    <li>Mejorar mensajes de error</li>
                    <li>Proporcionar funcionalidad de deshacer</li>
                </ul>
            </div>
        `;
    }
    
    function generateResponseResults() {
        return `
            <h4>Resultados de Análisis de Tiempo de Respuesta del Sistema</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Carga de Imágenes PACS</h5>
                    <p>Actual: 3.2 segundos (objetivo: 2.0s)</p>
                    <p>Horas pico: 4.8 segundos</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 63%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Acceso a Registro EHR</h5>
                    <p>Actual: 1.8 segundos (objetivo: 1.0s)</p>
                    <p>Percentil 95: 3.5 segundos</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 56%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Generación de Reportes</h5>
                    <p>Actual: 45 segundos (objetivo: 30s)</p>
                    <p>Reportes grandes: 120 segundos</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 67%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Implementar estrategias de caché</li>
                    <li>Optimizar consultas de base de datos</li>
                    <li>Actualizar infraestructura de red</li>
                    <li>Agregar balanceo de carga</li>
                </ul>
            </div>
        `;
    }
    
    function generateAccuracyResults() {
        return `
            <h4>Resultados de Validación de Precisión de Datos</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Precisión de Datos de Pacientes</h5>
                    <p>Precisión general: 98.7%</p>
                    <p>Tasa de error: 1.3%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 99%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Registros de Medicamentos</h5>
                    <p>Precisión: 99.2%</p>
                    <p>Errores críticos: 0.1%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 99%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Resultados de Laboratorio</h5>
                    <p>Precisión: 99.8%</p>
                    <p>Errores de transcripción: 0.2%</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 100%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Implementar validación automática de datos</li>
                    <li>Agregar detección de duplicados</li>
                    <li>Mejorar registros de auditoría</li>
                    <li>Auditorías regulares de precisión</li>
                </ul>
            </div>
        `;
    }
    
    function generateComplianceResults() {
        return `
            <h4>Resultados de Evaluación de Cumplimiento ISO 9241</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Cumplimiento General</h5>
                    <p>Puntaje: 85/100</p>
                    <p>Nivel: Bueno</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 85%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Principios de Diálogo (ISO 9241-110)</h5>
                    <p>Puntaje: 82/100</p>
                    <p>Fuerte en controlabilidad, débil en autodescriptibilidad</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 82%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Visualización (ISO 9241-303)</h5>
                    <p>Puntaje: 78/100</p>
                    <p>Legibilidad buena, necesita mejoras de contraste</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 78%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Dispositivos de Entrada (ISO 9241-410)</h5>
                    <p>Puntaje: 88/100</p>
                    <p>Cumplimiento excelente de estándares de dispositivo</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 88%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Mejorar autodescriptibilidad del sistema</li>
                    <li>Corregir relaciones de contraste de color</li>
                    <li>Mejorar mensajes de error</li>
                    <li>Documentar procedimientos de cumplimiento</li>
                </ul>
            </div>
        `;
    }
    
    function generateAccessibilityResults() {
        return `
            <h4>Resultados de Auditoría de Accesibilidad</h4>
            <div class="assessment-results">
                <div class="result-item">
                    <h5>Cumplimiento WCAG 2.1 AA</h5>
                    <p>Puntaje: 78/100</p>
                    <p>12 problemas identificados</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 78%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Navegación por Teclado</h5>
                    <p>Puntaje: 85/100</p>
                    <p>La mayoría de funciones accesibles mediante teclado</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 85%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Soporte de Lector de Pantalla</h5>
                    <p>Puntaje: 72/100</p>
                    <p>Necesita etiquetas ARIA y marcado semántico</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 72%"></div>
                    </div>
                </div>
                
                <div class="result-item">
                    <h5>Contraste de Color</h5>
                    <p>Puntaje: 65/100</p>
                    <p>3 módulos por debajo de relaciones de contraste mínimas</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 65%"></div>
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h5>Recomendaciones Clave:</h5>
                <ul>
                    <li>Corregir problemas de contraste de color</li>
                    <li>Agregar etiquetas y roles ARIA</li>
                    <li>Mejorar estructura HTML semántica</li>
                    <li>Probar con lectores de pantalla</li>
                </ul>
            </div>
        `;
    }
    
    // Animar barras de progreso cuando entran en vista
    function animateProgressBars() {
        const progressBars = document.querySelectorAll('.progress-fill');
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';
            setTimeout(() => {
                bar.style.width = width;
            }, 500);
        });
    }
    
    // Observar cuando la sección de resultados se vuelve visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateProgressBars();
            }
        });
    });
    
    observer.observe(document.getElementById('toolResults'));
    
    // Sistema de notificaciones
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
    
    // Inicializar con sección de escenario visible
    showSection('scenario');
});
```

### Paso 4: Script de Análisis de Estudio de Caso en Python
Crear un archivo `case_study_analysis.py`:

```python
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from typing import Dict, List, Tuple, Any
import numpy as np
from collections import defaultdict

class AnalizadorEstudioCaso:
    def __init__(self):
        self.datos_caso = {}
        self.resultados_analisis = {}
        self.datos_evaluacion = {}
    
    def cargar_datos_caso(self, ruta_archivo: str):
        """Cargar datos de evaluación de estudio de caso"""
        with open(ruta_archivo, 'r') as f:
            self.datos_caso = json.load(f)
    
    def cargar_resultados_evaluacion(self, archivos_evaluacion: List[str]):
        """Cargar resultados de herramientas de evaluación individuales"""
        for ruta_archivo in archivos_evaluacion:
            nombre_herramienta = ruta_archivo.split('/')[-1].replace('.json', '')
            with open(ruta_archivo, 'r') as f:
                self.datos_evaluacion[nombre_herramienta] = json.load(f)
    
    def realizar_analisis_integral(self) -> Dict[str, Any]:
        """Realizar análisis integral integral"""
        analisis = {
            'resumen_sistema': self.analizar_resumen_sistema(),
            'hallazgos_integrados': self.analizar_hallazgos_integrados(),
            'cumplimiento_estandares': self.analizar_cumplimiento_estandares(),
            'evaluacion_impacto': self.analizar_evaluacion_impacto(),
            'recomendaciones': self.generar_recomendaciones_integradas(),
            'plan_implementacion': self.crear_plan_implementacion(),
            'metricas_exito': self.definir_metricas_exito(),
            'generado_en': datetime.now().isoformat()
        }
        
        return analisis
    
    def analizar_resumen_sistema(self) -> Dict[str, Any]:
        """Analizar características generales del sistema"""
        return {
            'nombre_sistema': 'Sistema de Salud Inteligente',
            'organizacion': 'Hospital General Metropolitano',
            'base_usuarios': '500+ profesionales de la salud',
            'volumen_diario': '10,000+ registros de pacientes',
            'componentes_criticos': [
                'Registros Médicos Electrónicos (EHR)',
                'Sistema de Archivo y Comunicación de Imágenes (PACS)',
                'Panel de Monitoreo de Pacientes',
                'Plataforma de Telemedicina',
                'Aplicaciones Móviles'
            ],
            'requisitos_clave': [
                'Disponibilidad del sistema 24/7',
                'Cumplimiento HIPAA',
                'Precisión de datos en tiempo real',
                'Interfaces de usuario intuitivas',
                'Diseño ergonómico'
            ]
        }
    
    def analizar_hallazgos_integrados(self) -> Dict[str, Any]:
        """Analizar hallazgos en todas las áreas de evaluación"""
        hallazgos = {
            'problemas_ergonomicos': self._analizar_hallazgos_ergonomicos(),
            'problemas_usabilidad': self._analizar_hallazgos_usabilidad(),
            'problemas_rendimiento': self._analizar_hallazgos_rendimiento(),
            'brechas_cumplimiento': self._analizar_hallazgos_cumplimiento(),
            'evaluacion_general': self._calcular_evaluacion_general()
        }
        
        return hallazgos
    
    def _analizar_hallazgos_ergonomicos(self) -> Dict[str, Any]:
        """Analizar hallazgos de evaluación ergonómica"""
        return {
            'posicionamiento_monitor': {
                'puntaje': 75,
                'problemas': 'altura subóptima para 40%',
                'gravedad': 'Media',
                'usuarios_afectados': '200+ estaciones de trabajo'
            },
            'configuracion_teclado': {
                'puntaje': 68,
                'problemas': '25% carecen de bandejas ajustables',
                'gravedad': 'Media',
                'usuarios_afectados': '125+ usuarios'
            },
            'ergonomica_silla': {
                'puntaje': 72,
                'problemas': 'soporte inadecuado',
                'gravedad': 'Media',
                'usuarios_afectados': '300+ usuarios'
            },
            'condiciones_iluminacion': {
                'puntaje': 65,
                'problemas': 'brillo e iluminación insuficiente',
                'gravedad': 'Alta',
                'usuarios_afectados': 'departamento de radiología'
            }
        }
    
    def _analizar_hallazgos_usabilidad(self) -> Dict[str, Any]:
        """Analizar hallazgos de evaluación de usabilidad"""
        return {
            'eficiencia_navegacion': {
                'puntaje': 47,
                'problemas': '8.5 clics por tarea',
                'objetivo': 'máximo 4 clics',
                'impacto': 'Alto'
            },
            'completacion_tarea': {
                'puntaje': 64,
                'problemas': '12.5 min por registro',
                'objetivo': '8 min',
                'impacto': 'Alto'
            },
            'prevencion_errores': {
                'puntaje': 65,
                'problemas': 'múltiples tipos de error',
                'cobertura_prevencion': '65%',
                'impacto': 'Crítico'
            }
        }
    
    def _analizar_hallazgos_rendimiento(self) -> Dict[str, Any]:
        """Analizar hallazgos de evaluación de rendimiento"""
        return {
            'carga_imagenes_pacs': {
                'actual': '3.2s',
                'objetivo': '2.0s',
                'rendimiento_pico': '4.8s',
                'impacto': 'Alto'
            },
            'acceso_ehr': {
                'actual': '1.8s',
                'objetivo': '1.0s',
                'percentil_95': '3.5s',
                'impacto': 'Medio'
            },
            'precision_datos': {
                'general': '98.7%',
                'registros_medicamentos': '99.2%',
                'resultados_laboratorio': '99.8%',
                'impacto': 'Crítico'
            }
        }
    
    def _analizar_hallazgos_cumplimiento(self) -> Dict[str, Any]:
        """Analizar hallazgos de evaluación de cumplimiento"""
        return {
            'iso9241_general': {
                'puntaje': 85,
                'nivel': 'Bueno',
                'fortalezas': ['dispositivos de entrada', 'principios de diálogo'],
                'debilidades': ['visualización', 'autodescriptibilidad']
            },
            'accesibilidad': {
                'puntaje_wcag': 78,
                'problemas': 12,
                'navegacion_teclado': 85,
                'soporte_lector_pantalla': 72,
                'contraste_color': 65
            },
            'cumplimiento_hipaa': {
                'puntaje': 92,
                'registros_auditoria': 'completos',
                'controles_acceso': 'fuertes',
                'encriptacion_datos': 'adecuada'
            }
        }
    
    def _calcular_evaluacion_general(self) -> Dict[str, Any]:
        """Calcular evaluación general del sistema"""
        categorias = ['ergonomica', 'usabilidad', 'rendimiento', 'cumplimiento']
        puntajes = [71, 59, 72, 85]  # Puntajes promedio de hallazgos
        
        puntaje_general = sum(puntajes) / len(puntajes)
        
        return {
            'puntaje_general': round(puntaje_general, 1),
            'puntajes_categoria': dict(zip(categorias, puntajes)),
            'nivel_evaluacion': self._obtener_nivel_evaluacion(puntaje_general),
            'problemas_criticos': 12,
            'elementos_prioridad_alta': 8,
            'elementos_prioridad_media': 15
        }
    
    def _obtener_nivel_evaluacion(self, puntaje: float) -> str:
        """Obtener nivel de evaluación basado en puntaje"""
        if puntaje >= 90:
            return 'Excelente'
        elif puntaje >= 80:
            return 'Bueno'
        elif puntaje >= 70:
            return 'Regular'
        elif puntaje >= 60:
            return 'Deficiente'
        else:
            return 'Crítico'
    
    def analizar_cumplimiento_estandares(self) -> Dict[str, Any]:
        """Analizar cumplimiento con estándares ISO 9241"""
        return {
            'iso9241_110': {  # Principios de diálogo
                'puntaje_cumplimiento': 82,
                'adecuacion_tarea': 85,
                'autodescriptibilidad': 75,
                'controlabilidad': 88,
                'conformidad_expectativas': 80,
                'tolerancia_errores': 82,
                'adecuacion_aprendizaje': 78
            },
            'iso9241_210': {  # Diseño centrado en el humano
                'puntaje_cumplimiento': 79,
                'contexto_uso': 85,
                'requisitos_usuario': 75,
                'soluciones_diseno': 80,
                'evaluacion_diseno': 78
            },
            'iso9241_303': {  # Requisitos de visualización
                'puntaje_cumplimiento': 78,
                'legibilidad': 82,
                'legibilidad': 75,
                'ergonomica_visual': 80,
                'verificacion_cumplimiento': 76
            },
            'iso9241_410': {  # Estándares de dispositivos de entrada
                'puntaje_cumplimiento': 88,
                'diseno_ergonomico': 90,
                'fuerza_operacion': 85,
                'recorrido_tecla': 88,
                'retroalimentacion_tactil': 86,
                'accesibilidad': 92
            }
        }
    
    def analizar_evaluacion_impacto(self) -> Dict[str, Any]:
        """Analizar impacto de problemas identificados"""
        return {
            'impacto_usuario': {
                'problemas_ergonomicos': 'Alto',
                'problemas_usabilidad': 'Alto',
                'problemas_rendimiento': 'Medio',
                'brechas_cumplimiento': 'Medio'
            },
            'seguridad_paciente': {
                'problemas_ergonomicos': 'Medio',
                'problemas_usabilidad': 'Alto',
                'problemas_rendimiento': 'Alto',
                'brechas_cumplimiento': 'Crítico'
            },
            'costo_operacional': {
                'problemas_ergonomicos': 'Medio',
                'problemas_usabilidad': 'Alto',
                'problemas_rendimiento': 'Medio',
                'brechas_cumplimiento': 'Bajo'
            },
            'evaluacion_riesgos': {
                'problemas_alto_riesgo': 5,
                'problemas_riesgo_medio': 12,
                'problemas_bajo_riesgo': 18,
                'total_riesgos': 35
            }
        }
    
    def generar_recomendaciones_integradas(self) -> List[Dict[str, Any]]:
        """Generar recomendaciones integradas"""
        recomendaciones = [
            {
                'fase': 'Correcciones Críticas (0-3 meses)',
                'prioridad': 'Crítica',
                'categoria': 'Cumplimiento',
                'titulo': 'Corregir Problemas de Contraste de Color',
                'descripcion': 'Actualizar esquemas de color UI para cumplir con estándares WCAG AA',
                'esfuerzo': 'Bajo',
                'impacto': 'Alto',
                'cronograma': '1 mes'
            },
            {
                'fase': 'Correcciones Críticas (0-3 meses)',
                'prioridad': 'Crítica',
                'categoria': 'Rendimiento',
                'titulo': 'Optimizar Tiempos de Respuesta PACS',
                'descripcion': 'Implementar estrategias de caché y optimizar consultas de base de datos',
                'esfuerzo': 'Medio',
                'impacto': 'Alto',
                'cronograma': '2 meses'
            },
            {
                'fase': 'Correcciones Críticas (0-3 meses)',
                'prioridad': 'Crítica',
                'categoria': 'Usabilidad',
                'titulo': 'Mejorar Navegación EHR',
                'descripcion': 'Rediseñar flujo de trabajo para reducir clics en 50%',
                'esfuerzo': 'Alto',
                'impacto': 'Alto',
                'cronograma': '3 meses'
            },
            {
                'fase': 'Mejoras Mayores (3-6 meses)',
                'prioridad': 'Alta',
                'categoria': 'Ergonómica',
                'titulo': 'Actualizaciones de Estación de Trabajo Ergonómica',
                'descripcion': 'Reemplazar equipo obsoleto y proporcionar muebles ajustables',
                'esfuerzo': 'Alto',
                'impacto': 'Medio',
                'cronograma': '4 meses'
            },
            {
                'fase': 'Mejoras Mayores (3-6 meses)',
                'prioridad': 'Alta',
                'categoria': 'Capacitación',
                'titulo': 'Programa de Capacitación Mejorado',
                'descripcion': 'Desarrollar módulos de capacitación específicos por rol y guías de referencia rápida',
                'esfuerzo': 'Medio',
                'impacto': 'Alto',
                'cronograma': '5 meses'
            },
            {
                'fase': 'Mejoras Mayores (3-6 meses)',
                'prioridad': 'Alta',
                'categoria': 'Rendimiento',
                'titulo': 'Optimización de Aplicación Móvil',
                'descripcion': 'Mejorar rendimiento y agregar capacidades offline',
                'esfuerzo': 'Medio',
                'impacto': 'Medio',
                'cronograma': '6 meses'
            }
        ]
        
        return recomendaciones
    
    def crear_plan_implementacion(self) -> Dict[str, Any]:
        """Crear plan de implementación detallado"""
        return {
            'fase_1': {
                'duracion': 'Meses 1-2',
                'enfoque': 'Evaluación y Planificación',
                'actividades': [
                    'Completar análisis detallado de requisitos',
                    'Desarrollar mapa vial de implementación',
                    'Establecer métricas de éxito',
                    'Obtener aceptación de interesados'
                ]
            },
            'fase_2': {
                'duracion': 'Meses 3-4',
                'enfoque': 'Implementación de Correcciones Críticas',
                'actividades': [
                    'Desplegar recomendaciones de Fase 1',
                    'Realizar pruebas de aceptación de usuario',
                    'Proporcionar capacitación en nuevas características',
                    'Monitorear rendimiento del sistema'
                ]
            },
            'fase_3': {
                'duracion': 'Meses 5-8',
                'enfoque': 'Mejoras Mayores',
                'actividades': [
                    'Implementar recomendaciones de Fase 2',
                    'Realizar pruebas integrales',
                    'Implementar cambios en fases',
                    'Recopilar retroalimentación de usuario'
                ]
            },
            'fase_4': {
                'duracion': 'Meses 9-12',
                'enfoque': 'Optimización y Mejora',
                'actividades': [
                    'Desplegar características avanzadas',
                    'Optimizar rendimiento del sistema',
                    'Realizar evaluación final',
                    'Documentar lecciones aprendidas'
                ]
            }
        }
    
    def definir_metricas_exito(self) -> Dict[str, Any]:
        """Definir métricas de éxito para el estudio de caso"""
        return {
            'satisfaccion_usuario': {
                'objetivo': '90%',
                'actual': '82%',
                'medicion': 'Encuestas trimestrales'
            },
            'tiempo_completacion_tarea': {
                'objetivo': '25% de reducción',
                'actual': 'línea base establecida',
                'medicion': 'Sistema de seguimiento de tiempo'
            },
            'tasa_error': {
                'objetivo': '50% de reducción',
                'actual': 'línea base establecida',
                'medicion': 'Sistema de registro de errores'
            },
            'tiempo_actividad_sistema': {
                'objetivo': '99.9%',
                'actual': '99.5%',
                'medicion': 'Monitoreo del sistema'
            },
            'puntaje_cumplimiento': {
                'objetivo': '95%',
                'actual': '85%',
                'medicion': 'Verificación automatizada de cumplimiento'
            },
            'tiempo_capacitacion': {
                'objetivo': '30% de reducción',
                'actual': 'línea base establecida',
                'medicion': 'Seguimiento de finalización de capacitación'
            }
        }
    
    def generar_reporte_integral(self) -> Dict[str, Any]:
        """Generar reporte integral de estudio de caso"""
        analisis = self.realizar_analisis_integral()
        
        reporte = {
            'titulo_estudio_caso': 'Evaluación de Cumplimiento ISO 9241 del Sistema de Salud Inteligente',
            'organizacion': 'Hospital General Metropolitano',
            'fecha_evaluacion': datetime.now().isoformat(),
            'evaluadores': ['Equipo Experto ISO 9241'],
            'resumen_ejecutivo': self._generar_resumen_ejecutivo(analisis),
            'metodologia': 'Marco de evaluación multi-estándar integrado',
            'hallazgos': analisis,
            'conclusiones': self._generar_conclusiones(analisis),
            'proximos_pasos': 'Implementación de recomendaciones priorizadas'
        }
        
        return reporte
    
    def _generar_resumen_ejecutivo(self, analisis: Dict[str, Any]) -> str:
        """Generar resumen ejecutivo"""
        puntaje_general = analisis['hallazgos_integrados']['evaluacion_general']['puntaje_general']
        
        return f"""
        El Sistema de Salud Inteligente del Hospital General Metropolitano fue sometido a una evaluación integral de cumplimiento ISO 9241. El sistema recibió un puntaje general de {puntaje_general}%, indicando buen rendimiento con espacio significativo para mejora. 
        
        Hallazgos clave incluyen 12 problemas críticos que requieren atención inmediata, base sólida de cumplimiento (85% de cumplimiento ISO 9241), y oportunidades para mejoras sustanciales en usabilidad y ergonomía visual. La evaluación cubrió ergonomía, usabilidad, rendimiento y cumplimiento en todos los componentes principales del sistema.
        
        Se espera que la implementación de las mejoras recomendadas mejore significativamente la satisfacción del usuario, reduzca errores y mejore los resultados de seguridad del paciente.
        """
    
    def _generar_conclusiones(self, analisis: Dict[str, Any]) -> str:
        """Generar conclusiones"""
        return """
        Este estudio de caso integral demuestra el valor de la evaluación integrada ISO 9241 en sistemas de salud. El enfoque de evaluación multi-dimensional identificó exitosamente problemas críticos en ergonomía, usabilidad, rendimiento y cumplimiento de dominios.
        
        El contexto de la salud presenta desafíos únicos que requieren un equilibrio cuidadoso de necesidades del usuario, requisitos de seguridad del paciente y eficiencia operacional. La evaluación reveló que aunque el sistema tiene una base sólida, se necesitan mejoras significativas en usabilidad y ergonomía visual para cumplir con los requisitos exigentes de los profesionales de la salud.
        
        El plan de implementación priorizado proporciona un mapa vial claro para mejora sistemática, con beneficios esperados en satisfacción del usuario, reducción de errores y eficiencia operacional.
        """
    
    def guardar_reporte(self, ruta_archivo: str = 'reporte_estudio_caso.json'):
        """Guardar reporte integral en archivo"""
        reporte = self.generar_reporte_integral()
        
        with open(ruta_archivo, 'w') as f:
            json.dump(reporte, f, indent=2, default=str)
        
        print(f"Reporte de estudio de caso guardado: {ruta_archivo}")
        return reporte
    
    def crear_visualizaciones(self, ruta_guardado: str = 'analisis_estudio_caso.png'):
        """Crear visualizaciones integrales"""
        analisis = self.realizar_analisis_integral()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Puntajes de evaluación por categoría
        categorias = ['Ergonómica', 'Usabilidad', 'Rendimiento', 'Cumplimiento']
        puntajes = [
            71, 59, 72, 85  # De hallazgos integrados
        ]
        
        barras = ax1.bar(categorias, puntajes, color=['red', 'orange', 'yellow', 'green'])
        ax1.set_ylim(0, 100)
        ax1.set_title('Puntajes de Evaluación por Categoría', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Puntaje (%)', fontsize=12)
        ax1.axhline(y=80, color='green', linestyle='--', alpha=0.7, label='Bueno')
        ax1.axhline(y=60, color='orange', linestyle='--', alpha=0.7, label='Necesita Mejora')
        ax1.legend()
        
        # Agregar etiquetas de valor en las barras
        for barra, puntaje in zip(barras, puntajes):
            ax1.text(barra.get_x() + barra.get_width()/2, barra.get_y() + puntaje + 1, 
                    f'{puntaje}', ha='center', va='bottom', fontweight='bold')
        
        # Cumplimiento de estándares
        estandares = ['ISO 9241-110', 'ISO 9241-210', 'ISO 9241-303', 'ISO 9241-410']
        puntajes_cumplimiento = [82, 79, 78, 88]
        
        ax2.bar(estandares, puntajes_cumplimiento, color='lightblue')
        ax2.set_ylim(0, 100)
        ax2.set_title('Cumplimiento de Estándares ISO 9241', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Puntaje de Cumplimiento (%)', fontsize=12)
        ax2.tick_params(axis='x', rotation=45)
        
        # Evaluación de impacto
        categorias_impacto = ['Impacto Usuario', 'Seguridad Paciente', 'Costo Operacional']
        impacto_ergonomico = [3, 2, 2]  # Alto, Medio, Medio
        impacto_usabilidad = [3, 3, 3]  # Alto, Alto, Alto
        impacto_rendimiento = [2, 3, 2]  # Medio, Alto, Medio
        impacto_cumplimiento = [2, 4, 1]  # Medio, Crítico, Bajo
        
        x = np.arange(len(categorias_impacto))
        width = 0.2
        
        ax3.bar(x - 1.5*width, impacto_ergonomico, width, label='Ergonómica', color='red')
        ax3.bar(x - 0.5*width, impacto_usabilidad, width, label='Usabilidad', color='orange')
        ax3.bar(x + 0.5*width, impacto_rendimiento, width, label='Rendimiento', color='yellow')
        ax3.bar(x + 1.5*width, impacto_cumplimiento, width, label='Cumplimiento', color='green')
        
        ax3.set_title('Evaluación de Impacto por Categoría', fontsize=14, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(categorias_impacto)
        ax3.set_ylabel('Nivel de Impacto (1-4)', fontsize=12)
        ax3.legend()
        
        # Cronograma de implementación priorizada
        fases = ['Fase 1\n(0-3 meses)', 'Fase 2\n(3-6 meses)', 'Fase 3\n(6-12 meses)']
        elementos_criticos = [3, 0, 0]
        elementos_altos = [0, 3, 0]
        elementos_medios = [0, 0, 3]
        
        ax4.bar(fases, elementos_criticos, label='Críticos', color='red')
        ax4.bar(fases, elementos_altos, bottom=elementos_criticos, label='Altos', color='orange')
        ax4.bar(fases, elementos_medios, bottom=[c + h for c, h in zip(elementos_criticos, elementos_altos)], 
               label='Medios', color='yellow')
        
        ax4.set_title('Cronograma de Implementación', fontsize=14, fontweight='bold')
        ax4.set_ylabel('Número de Recomendaciones', fontsize=12)
        ax4.legend()
        
        plt.tight_layout()
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Visualizaciones de estudio de caso guardadas: {ruta_guardado}")

# Ejemplo de uso
if __name__ == "__main__":
    analizador = AnalizadorEstudioCaso()
    
    # Generar análisis integral de estudio de caso
    reporte = analizador.guardar_reporte()
    
    print("Análisis de Estudio de Caso Completado")
    print(f"Puntaje de Evaluación General: {reporte['hallazgos']['hallazgos_integrados']['evaluacion_general']['puntaje_general']}%")
    print(f"Problemas Críticos Identificados: {reporte['hallazgos']['hallazgos_integrados']['evaluacion_general']['problemas_criticos']}")
    print(f"Puntaje de Cumplimiento: {reporte['hallazgos']['cumplimiento_estandares']['iso9241_110']['puntaje_cumplimiento']}%")
    
    # Crear visualizaciones
    analizador.crear_visualizaciones()
```

### Paso 5: Documentación
Este estudio de caso integral integra todos los estándares ISO 9241 cubiertos en la serie de laboratorios en un escenario del mundo real de evaluación de un sistema de salud inteligente. El estudio de caso demuestra la aplicación de principios ergonómicos, evaluación de usabilidad y verificación de cumplimiento en un sistema complejo, crítico para la misión.

Características clave:
- **Marco de Evaluación Integrado**: Combina todos los estándares ISO 9241 (110, 210, 303, 410) en una metodología de evaluación cohesiva
- **Escenario del Mundo Real**: Sistema de salud inteligente con múltiples grupos de usuarios y requisitos críticos
- **Análisis Multi-Dimensional**: Evaluación de ergonomía, usabilidad, rendimiento y cumplimiento
- **Panel Interactivo**: Interfaz web para explorar hallazgos y recomendaciones del estudio de caso
- **Reportes Integrales**: Análisis detallado con plan de implementación priorizado
- **Analítica Visual**: Gráficos y diagramas para perspectivas basadas en datos

El estudio de caso proporciona una plantilla completa para realizar evaluaciones integrales ISO 9241 en entornos organizacionales complejos, con relevancia particular para la atención médica, pero aplicable a cualquier industria que requiera altos estándares de usabilidad y seguridad.
