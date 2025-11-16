# Laboratorio 1: Introducción a la Ingeniería de Requisitos

## Objetivos de Aprendizaje
Al finalizar este laboratorio, los estudiantes podrán:

1. Comprender los conceptos fundamentales de la Ingeniería de Requisitos
2. Identificar diferentes tipos de requisitos y sus características
3. Aplicar el proceso de Ingeniería de Requisitos según ISO/IEC/IEEE 29148
4. Crear artefactos básicos de requisitos usando plantillas estándar
5. Realizar análisis de interesados y mapeo
6. Evaluar la calidad de requisitos usando criterios establecidos
7. Utilizar herramientas Python para análisis y reporte de requisitos

## Requisitos Previos
- Conocimiento básico de conceptos de desarrollo de software
- Familiaridad con HTML, CSS y JavaScript (recomendado)
- Conocimiento de programación Python (recomendado)
- Editor de texto o IDE para desarrollo de código

## Materiales Necesarios
- Computadora con acceso a internet
- Navegador web (Chrome, Firefox o Edge recomendado)
- Python 3.x instalado
- Editor de texto (VS Code, Sublime Text o similar)
- Servidor web local (opcional, para características avanzadas)

## Tareas del Laboratorio

### Tarea 1: Dashboard Interactivo de Ingeniería de Requisitos (40 puntos)
Crear un dashboard web interactivo que demuestre conceptos de Ingeniería de Requisitos:

1. **Sección de Conceptos Básicos**: Implementar una sección que explique:
   - ¿Qué es la Ingeniería de Requisitos?
   - Tipos de requisitos (funcionales, no funcionales, restricciones)
   - Desafíos comunes y cómo abordarlos

2. **Sección de Proceso**: Crear un diagrama de proceso interactivo mostrando:
   - Técnicas de elicitación de requisitos
   - Actividades de análisis y especificación
   - Procesos de validación y gestión
   - Incluir herramientas clicables para cada paso del proceso

3. **Sección de Artefactos**: Desarrollar plantillas para:
   - Especificación de Requisitos de Software (ERS)
   - Especificaciones de casos de uso
   - Historias de usuario con criterios de aceptación
   - Matriz de trazabilidad de requisitos

4. **Sección de Análisis de Interesados**: Implementar:
   - Formulario de entrada de interesados
   - Visualización de cuadrante poder-interés
   - Mapeo dinámico de interesados

5. **Sección de Evaluación de Calidad**: Crear:
   - Listas de verificación de criterios de calidad
   - Puntuación de calidad automatizada
   - Recomendaciones de mejora

6. **Sección de Visión General de Estándares**: Documentar:
   - Estructura de ISO/IEC/IEEE 29148
   - Propósitos de secciones clave
   - Beneficios de seguir el estándar

**Entregables**:
- `requirements_intro.html` - Archivo principal del dashboard
- `requirements.css` - Estilos para el dashboard
- `requirements.js` - Funcionalidad interactiva
- Capturas de pantalla del dashboard funcionando

### Tarea 2: Herramienta Python de Análisis de Requisitos (35 puntos)
Desarrollar una clase Python para análisis automatizado de requisitos:

1. **Gestión de Requisitos**: Implementar métodos para:
   - Agregar nuevos requisitos con metadatos
   - Cargar requisitos desde archivos JSON
   - Clasificar requisitos por tipo y prioridad
   - Rastrear estado y cambios de requisitos

2. **Evaluación de Calidad**: Crear funcionalidad para:
   - Verificación automática de calidad contra criterios
   - Detección de ambigüedad en texto de requisitos
   - Puntuación de calidad y recomendaciones
   - Evaluación de calidad por lotes para múltiples requisitos

3. **Construcción de Trazabilidad**: Implementar:
   - Vinculación requisito-elemento de diseño
   - Mapeo requisito-caso de prueba
   - Generación de matriz de trazabilidad
   - Visualización de relaciones

4. **Reportes y Visualización**: Desarrollar:
   - Reportes comprehensivos de requisitos
   - Análisis estadístico de requisitos
   - Visualización de datos usando matplotlib/seaborn
   - Funcionalidad de exportación a JSON

**Entregables**:
- `requirements_analyzer.py` - Clase Python completa
- Archivo de datos de muestra con requisitos de prueba
- Reportes y visualizaciones generadas
- Pruebas unitarias para funcionalidad clave

### Tarea 3: Aplicación del Proceso de Ingeniería de Requisitos (25 puntos)
Aplicar los conceptos aprendidos a un escenario del mundo real:

1. **Análisis de Escenario**: Elegir uno de los siguientes escenarios:
   - Sistema de banca en línea
   - Plataforma de comercio electrónico
   - Sistema de gestión de salud
   - Sistema de gestión educativa

2. **Elicitación de Requisitos**: Para el escenario elegido:
   - Identificar interesados clave
   - Listar técnicas potenciales de elicitación
   - Crear un mapa de interesados

3. **Desarrollo de Requisitos**: Desarrollar:
   - 5 requisitos funcionales
   - 3 requisitos no funcionales
   - 2 restricciones
   - Usar formato apropiado de requisitos

4. **Evaluación de Calidad**: Evaluar los requisitos usando:
   - Los criterios de calidad del dashboard
   - La herramienta de análisis Python
   - Documentar recomendaciones de mejora

5. **Configuración de Trazabilidad**: Crear:
   - Matriz de trazabilidad de requisitos
   - Vínculos a elementos de diseño potenciales
   - Mapeos de casos de prueba

**Entregables**:
- `scenario_analysis.md` - Documento completo de análisis
- Artefactos de requisitos en formatos apropiados
- Resultados de evaluación de calidad
- Documentación de trazabilidad

## Criterios de Evaluación

### Tarea 1: Dashboard Interactivo (40%)
- **Funcionalidad (15%)**: Todas las secciones funcionan correctamente
- **Interactividad (10%)**: Funcionalidad JavaScript implementada
- **Diseño (10%)**: Apariencia profesional y usabilidad
- **Precisión de Contenido (5%)**: Conceptos y estándares correctos de ER

### Tarea 2: Herramienta Python (35%)
- **Calidad de Código (10%)**: Código bien estructurado y documentado
- **Funcionalidad (15%)**: Todos los métodos requeridos implementados
- **Características de Análisis (5%)**: Evaluación de calidad y reportes
- **Visualización (5%)**: Gráficos y diagramas generados correctamente

### Tarea 3: Aplicación de Proceso (25%)
- **Análisis de Escenario (5%)**: Identificación apropiada de interesados
- **Calidad de Requisitos (10%)**: Requisitos bien escritos y completos
- **Trazabilidad (5%)**: Vinculación y documentación apropiadas
- **Documentación (5%)**: Presentación clara y profesional

## Requisitos de Entrega
1. Todos los archivos de código fuente con comentarios apropiados
2. Dashboard web funcionando (HTML/CSS/JS)
3. Herramienta de análisis Python con datos de muestra
4. Documento de análisis de escenario
5. Capturas de pantalla de aplicaciones funcionando
6. Informe breve explicando decisiones de implementación

## Estimación de Tiempo
- Tarea 1: 4-6 horas
- Tarea 2: 3-4 horas
- Tarea 3: 2-3 horas
- Total: 9-13 horas

## Recursos Adicionales
- Documentación del Estándar ISO/IEC/IEEE 29148
- Libros de texto de Ingeniería de Requisitos
- Tutoriales en línea para HTML/CSS/JavaScript
- Documentación Python para análisis de datos
- Documentos de muestra de requisitos de proyectos reales

## Consejos para el Éxito
1. Comenzar con la estructura HTML, luego agregar estilos CSS
2. Implementar funcionalidad JavaScript de manera incremental
3. Probar la herramienta Python con datos de muestra temprano
4. Usar el dashboard para entender conceptos antes de aplicarlos
5. Documentar el trabajo conforme se progresa
6. Pedir ayuda si se atasca en algún concepto
