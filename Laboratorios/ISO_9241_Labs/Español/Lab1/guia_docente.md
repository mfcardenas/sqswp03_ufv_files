# Guía Docente - Laboratorio 1: Análisis de Contexto de Uso

## 📋 Ficha Técnica del Laboratorio

| Aspecto | Detalle |
|---------|---------|
| **Nombre del Laboratorio** | Análisis de Contexto de Uso - Plataforma de Reservas Turísticas |
| **Estándar ISO aplicado** | ISO 9241-11:2018 - Ergonomía de la interacción humano-sistema - Parte 11: Usabilidad: Definiciones y conceptos |
| **Duración total** | 8-9 horas (3h preparación + 2h presencial + 3-4h trabajo final) |
| **Modalidad** | Híbrida (preparación autónoma + sesión presencial + entregable final) |
| **Nivel de complejidad** | ⭐⭐⭐ Medio |
| **Tamaño de equipos** | 2-3 estudiantes |
| **Requisitos previos** | Ninguno (es el primer laboratorio) |
| **Conocimientos asumidos** | Uso básico de navegadores web, procesadores de texto, IA generativa |

---

## 🎯 Objetivos de Aprendizaje (Taxonomía de Bloom)

Al finalizar este laboratorio, el estudiante será capaz de:

### Nivel 1 - Recordar
- **Definir** los tres componentes de usabilidad según ISO 9241-11: efectividad, eficiencia y satisfacción
- **Identificar** los elementos que componen el contexto de uso: usuarios, tareas, equipos y entorno

### Nivel 2 - Comprender
- **Explicar** la diferencia entre efectividad, eficiencia y satisfacción con ejemplos concretos
- **Interpretar** cómo el contexto de uso afecta los requisitos de usabilidad de un sistema

### Nivel 3 - Aplicar
- **Implementar** un análisis de contexto de uso siguiendo la metodología de ISO 9241-11
- **Usar** herramientas de IA generativa para crear personas y escenarios de uso

### Nivel 4 - Analizar
- **Distinguir** entre diferentes perfiles de usuario y sus necesidades específicas
- **Examinar** cómo las tareas, equipos y entornos varían según el tipo de usuario

### Nivel 5 - Evaluar
- **Juzgar** la calidad y completitud de un análisis de contexto de uso
- **Validar** si las métricas de usabilidad definidas son apropiadas para cada contexto

### Nivel 6 - Crear
- **Diseñar** personas detalladas basadas en investigación de usuarios
- **Desarrollar** métricas de usabilidad específicas para contextos de uso identificados

---

## 📚 Materiales Necesarios

### Para el Docente

**Materiales incluidos en este laboratorio:**
- ✅ Esta guía docente (guia_docente.md)
- ✅ Material para estudiantes (material_estudiante.md)
- ✅ Lecturas preparatorias con referencias (lecturas_preparatorias.md)
- ✅ Prompts de IA probados y listos (prompts_ia.md)
- ✅ Rúbrica de evaluación detallada (rubrica_evaluacion.md)
- ✅ Solución de referencia (solucion_referencia.md)
- ✅ Presentación de introducción (crear PowerPoint/PDF basado en esta guía)

**Materiales que el docente debe preparar:**
- [ ] Acceso al LMS (Moodle, Canvas, Blackboard) para subir materiales
- [ ] Quiz de comprensión de lecturas (5-7 preguntas, ver sección 6)
- [ ] Plantilla de informe de lectura previa (documento Word/Google Docs)
- [ ] Plantilla de análisis de contexto de uso (Excel/Google Sheets)
- [ ] Plantilla de informe técnico final (documento Word/Google Docs)

**Herramientas tecnológicas necesarias:**
- [ ] Acceso a IA generativa (al menos una de):
  - ChatGPT (versión gratuita suficiente, Plus recomendado)
  - Claude (Anthropic)
  - Gemini (Google)
  - Copilot (Microsoft)
- [ ] Navegador web actualizado
- [ ] Proyector/pantalla para sesión presencial
- [ ] Timer visible (proyectar cronómetro)

### Para los Estudiantes

**Materiales que recibirán:**
- Material del estudiante con descripción del caso
- Lecturas preparatorias (artículos en PDF)
- Plantillas de documentos
- Prompts de IA listos para usar
- Checklist de evaluación

**Herramientas que necesitan:**
- Cuenta en al menos una plataforma de IA generativa (gratuita)
- Procesador de texto
- Hoja de cálculo
- Navegador web

---

## ⏱️ Planificación Temporal Detallada

### FASE 1: Trabajo Preparatorio (Autónomo - 3 horas)

**Objetivo:** Los estudiantes llegan a la sesión presencial con comprensión sólida de ISO 9241-11

#### Actividades (Tiempo estimado: 2.5-3 horas)

**[00:00 - 01:30] Lectura de Material Teórico (90 min)**

1. **Lectura obligatoria 1: ISO 9241-11:2018** (45 min)
   - Secciones específicas:
     - Introducción (páginas 1-3)
     - Sección 3: Términos y definiciones (páginas 4-6)
     - Sección 5: Contexto de uso (páginas 8-11)
     - Sección 6: Medidas de usabilidad (páginas 11-14)
   
   📌 **Nota docente:** Proporcionar PDF de estas secciones específicas. El estándar completo tiene ~30 páginas, pero solo necesitan estas secciones para este lab.

2. **Lectura obligatoria 2: Paper académico** (45 min)
   - Bevan, N., Carter, J., & Harker, S. (2015). "ISO 9241-11 Revised: What Have We Learnt About Usability Since 1998?"
   - Alternativamente: Cualquier paper sobre análisis de contexto de uso en turismo/e-commerce
   
   📌 **Nota docente:** Proporcionar el PDF en carpeta /lecturas

**[01:30 - 02:15] Completar Cuestionario de Comprensión (45 min)**

- Quiz en LMS (5-7 preguntas de opción múltiple + 2-3 preguntas abiertas cortas)
- Ejemplos de preguntas (ver sección 6 de esta guía)
- **Requisito:** Aprobar con mínimo 70% para acceder a sesión presencial
- **Intentos:** 2 intentos permitidos

📌 **Nota docente:** El quiz es FUNDAMENTAL para asegurar que todos llegan preparados. No es punitivo (solo 5-10% de la nota), pero es obligatorio.

**[02:15 - 03:00] Redactar Informe de Lectura Previa (45 min)**

Usando la plantilla proporcionada, cada estudiante individualmente debe:

1. **Resumen conceptual** (1 página):
   - ¿Qué es usabilidad según ISO 9241-11?
   - ¿Cuáles son los 4 componentes del contexto de uso?
   - ¿Cómo se miden efectividad, eficiencia y satisfacción?

2. **Reflexión personal** (½ página):
   - ¿Qué sistema/aplicación que uses regularmente tiene buena usabilidad? ¿Por qué?
   - ¿Qué sistema tiene mala usabilidad? ¿Qué falla?

3. **Preguntas para clase** (3-5 preguntas):
   - Dudas conceptuales sobre el estándar
   - Preguntas sobre aplicabilidad práctica

**Entrega:** Subir a LMS 24 horas antes de la sesión presencial

📌 **Nota docente:** Revisar rápidamente estos informes antes de la clase. Identificar preguntas comunes para abordarlas en la introducción.

---

### FASE 2: Sesión Presencial en Laboratorio (2 horas)

**Configuración del aula:**
- Estudiantes en equipos de 2-3 personas (formados previamente o al inicio)
- Cada equipo con computadora y acceso a internet
- Proyector con timer visible
- Pizarra/pantalla para conceptos clave

#### [00:00 - 00:15] INTRODUCCIÓN Y CONTEXTUALIZACIÓN (15 min)

**Actividades del docente:**

1. **Bienvenida y objetivos del día** (3 min)
   - Presentar agenda de la sesión
   - Explicar entregas esperadas
   - Resolver dudas logísticas

2. **Revisión de conceptos clave de ISO 9241-11** (7 min)
   - Presentación con 8-10 slides:
     - Slide 1: ¿Qué es ISO 9241?
     - Slide 2: Definición de usabilidad (efectividad, eficiencia, satisfacción)
     - Slide 3: Los 4 componentes del contexto de uso
     - Slide 4: Usuarios (tipos, características, competencias)
     - Slide 5: Tareas (objetivos, pasos, frecuencia)
     - Slide 6: Equipos (hardware, software, materiales)
     - Slide 7: Entornos (físico, técnico, social, cultural)
     - Slide 8: Métricas de usabilidad (ejemplos concretos)
   
   📌 **Tip pedagógico:** Usar ejemplos visuales. Mostrar capturas de sistemas conocidos (Amazon, Booking, Google Maps).

3. **Resolución de preguntas comunes** (3 min)
   - Abordar 2-3 preguntas que aparecieron en informes de lectura
   - Aclarar confusiones conceptuales identificadas en el quiz

4. **Presentación del caso práctico: "TravelEase"** (2 min)
   - Explicar que es una plataforma de reservas de experiencias turísticas
   - Mostrar ejemplo visual (puede ser wireframe simple o competidor similar)
   - Asignar roles en equipos (ver sección 4 de esta guía)

📌 **Checkpoint:** Verificar que todos los equipos tienen acceso a IA generativa y materiales.

---

#### [00:15 - 00:45] FASE 1: ANÁLISIS DE CONTEXTO DE USO (30 min)

**Objetivo:** Equipos identifican y documentan el contexto de uso de TravelEase

**Actividades de los equipos:**

1. **Identificar perfiles de usuario** (10 min)
   - Leer el caso en material_estudiante.md
   - Brainstorming: ¿Qué tipos de usuarios usarían TravelEase?
   - Documentar al menos 5 perfiles diferentes
   - Para cada perfil, anotar:
     - Edad aproximada
     - Competencias tecnológicas
     - Motivaciones para viajar
     - Dispositivos que usaría

   📌 **Entregable parcial:** Lista de perfiles en plantilla

2. **Definir tareas principales por perfil** (10 min)
   - Seleccionar 2-3 perfiles principales
   - Para cada uno, listar 5-8 tareas que realizaría
   - Clasificar tareas por:
     - Frecuencia (diaria, semanal, ocasional)
     - Complejidad (simple, media, compleja)
     - Criticidad (alta, media, baja)

   📌 **Entregable parcial:** Tabla de tareas por perfil

3. **Analizar equipos y entornos** (10 min)
   - Equipos: ¿Qué dispositivos usa cada perfil? (móvil, tablet, desktop)
   - Entornos:
     - Físico: ¿Dónde usaría el sistema? (casa, oficina, aeropuerto, destino)
     - Técnico: ¿Qué conectividad? (WiFi, 4G/5G, variable)
     - Social: ¿Solo o acompañado? (individual, familia, grupo)
     - Cultural: ¿Qué idiomas? ¿Qué nivel de familiaridad con plataformas digitales?

   📌 **Entregable parcial:** Análisis de contexto completo

**Rol del docente durante esta fase:**
- ✅ Circular entre equipos constantemente
- ✅ Hacer preguntas detonantes:
  - "¿Han considerado usuarios con discapacidad?"
  - "¿Qué pasa si el usuario está en el extranjero con datos limitados?"
  - "¿Un turista de 70 años usa el sistema igual que uno de 25?"
- ✅ NO dar respuestas directas, sino guiar con preguntas
- ✅ Identificar equipos que van muy rápido → darles desafío adicional
- ✅ Identificar equipos atascados → darles pista específica

**⏰ Checkpoint (minuto 25):** 
- Detener a todos momentáneamente
- Preguntar: "¿Cuántos perfiles de usuario han identificado?" (respuestas rápidas)
- Dar tip general si es necesario

---

#### [00:45 - 01:30] FASE 2: GENERACIÓN DE PERSONAS CON IA (45 min)

**Objetivo:** Usar IA generativa para crear personas detalladas y escenarios de uso

**Actividades de los equipos:**

1. **Seleccionar 3 perfiles prioritarios** (5 min)
   - De los perfiles identificados, elegir los 3 más importantes
   - Justificar selección basándose en:
     - Frecuencia de uso del sistema
     - Impacto en negocio
     - Diversidad de necesidades

2. **Generar personas con IA** (25 min)
   - Usar los prompts proporcionados en prompts_ia.md
   - Para cada uno de los 3 perfiles, generar:
     - **Persona detallada** con:
       - Nombre, edad, ocupación, ubicación
       - Background personal y profesional
       - Objetivos y motivaciones
       - Frustraciones y pain points
       - Competencias tecnológicas
       - Dispositivos y herramientas que usa
       - Cita representativa
     - **Escenario de uso** con narrativa concreta

   📌 **Instrucción importante:** Estudiantes deben:
   - Copiar el prompt base de prompts_ia.md
   - Personalizarlo con los datos de su análisis
   - Ejecutar en la IA
   - **NO aceptar la primera respuesta si no es suficientemente detallada**
   - Iterar con la IA para mejorar

   **Ejemplo de iteración:**
   ```
   Primera respuesta de IA → muy genérica
   Estudiante: "Hazlo más específico. Este usuario viaja por negocios 
   frecuentemente a Asia. Dale detalles concretos de sus frustraciones 
   con plataformas actuales."
   Segunda respuesta de IA → mucho mejor
   ```

3. **Validar y refinar personas** (10 min)
   - Revisar las personas generadas
   - Verificar que incluyen:
     - ✅ Información demográfica realista
     - ✅ Competencias tecnológicas claras
     - ✅ Objetivos concretos (no vagos)
     - ✅ Frustraciones específicas
     - ✅ Contexto de uso bien definido
   - Editar manualmente si algo no tiene sentido

4. **Documentar el proceso** (5 min)
   - Capturar screenshots de las conversaciones con la IA
   - Anotar qué prompts funcionaron mejor
   - Documentar iteraciones realizadas

   📌 **Esto es importante para el informe final**

**Rol del docente durante esta fase:**
- ✅ Ayudar con problemas técnicos de IA (ej: prompt no funciona, IA da error)
- ✅ Revisar personas generadas en tiempo real
- ✅ Dar feedback: "Esta persona es muy genérica, pídele a la IA más detalles concretos"
- ✅ Compartir ejemplos buenos entre equipos (sin revelar autoría)
- ✅ Tener prompts de respaldo si alguno no funciona

**⏰ Checkpoint (minuto 70):** 
- "Todos los equipos deberían tener al menos 2 personas generadas. ¿Alguien necesita ayuda?"

📌 **Problema común:** IA genera personas demasiado genéricas o estereotipadas.
**Solución:** Enseñar a los estudiantes a dar contexto específico en el prompt. Ver prompts_ia.md para ejemplos.

---

#### [01:30 - 01:50] FASE 3: DEFINICIÓN DE MÉTRICAS DE USABILIDAD (20 min)

**Objetivo:** Definir métricas específicas de efectividad, eficiencia y satisfacción para cada contexto

**Actividades de los equipos:**

1. **Revisar ISO 9241-11 sobre métricas** (5 min)
   - Releer la sección 6 del estándar (páginas 11-14)
   - Recordar definiciones:
     - **Efectividad:** Exactitud y completitud con la que los usuarios alcanzan objetivos
     - **Eficiencia:** Recursos empleados en relación con la exactitud y completitud
     - **Satisfacción:** Grado en que se satisfacen las necesidades del usuario

2. **Definir métricas para cada persona** (12 min)
   - Para cada una de las 3 personas creadas, definir:
   
   **Métricas de Efectividad:**
   - ¿Cómo medirías si logra su objetivo?
   - Ejemplos: % de reservas completadas con éxito, % de tareas finalizadas, tasa de error
   
   **Métricas de Eficiencia:**
   - ¿Cómo medirías los recursos empleados?
   - Ejemplos: Tiempo para completar reserva, número de clics/pasos, tiempo en página
   
   **Métricas de Satisfacción:**
   - ¿Cómo medirías su satisfacción?
   - Ejemplos: Puntuación SUS (System Usability Scale), NPS (Net Promoter Score), valoración post-uso

   📌 **Las métricas deben ser:**
   - ✅ Específicas (no vagas como "buena experiencia")
   - ✅ Medibles (con número o escala)
   - ✅ Relevantes para ese perfil de usuario
   - ✅ Realistas de obtener

3. **Documentar en plantilla** (3 min)
   - Completar tabla de métricas
   - Formato sugerido:

   | Persona | Métrica Efectividad | Métrica Eficiencia | Métrica Satisfacción |
   |---------|--------------------|--------------------|---------------------|
   | Laura (Turista joven) | 95% reservas exitosas | < 3 min para reservar | SUS > 80 |
   | ... | ... | ... | ... |

**Rol del docente:**
- ✅ Verificar que métricas son **específicas y medibles**
- ✅ Desafiar métricas vagas: "¿Cómo medirías exactamente eso?"
- ✅ Dar ejemplos de buenas métricas si es necesario
- ✅ Conectar con casos reales: "¿Cómo creen que Booking mide su usabilidad?"

---

#### [01:50 - 02:00] CIERRE Y ASIGNACIÓN DE ENTREGABLE FINAL (10 min)

**Actividades del docente:**

1. **Recapitulación de conceptos** (4 min)
   - Resumir qué hicieron hoy:
     - ✅ Analizaron contexto de uso (usuarios, tareas, equipos, entornos)
     - ✅ Crearon personas detalladas con IA
     - ✅ Definieron métricas de usabilidad específicas
   - Conectar con ISO 9241-11:
     - "Esto es exactamente lo que pide el estándar en la fase de análisis de contexto"

2. **Explicar entregable final** (4 min)
   - **Qué:** Informe técnico de análisis de contexto de uso (ver rubrica_evaluacion.md)
   - **Cuándo:** [X días después de esta sesión, ej: 1 semana]
   - **Cómo:** Subir PDF a LMS
   - **Estructura:** Ver plantilla proporcionada
   - **Extensión:** 8-12 páginas (sin contar anexos)

3. **Preguntas y dudas** (2 min)
   - Responder dudas sobre el entregable
   - Aclarar criterios de evaluación

4. **Adelanto del Lab 2** (30 seg)
   - "En el siguiente laboratorio tomaremos estas personas y diseñaremos la interfaz de búsqueda aplicando los 7 principios de diálogo de ISO 9241-110"
   - Generar expectativa y continuidad

📌 **Consejo:** Enviar por correo/LMS ese mismo día:
- Resumen de conceptos clave (1 página)
- Recordatorio de fecha de entrega
- Enlace a plantilla de informe final
- Horario de consultas/tutorías si las hay

---

### FASE 3: Trabajo Post-Laboratorio (Autónomo - 3-4 horas)

**Objetivo:** Completar y pulir el informe técnico final

#### Actividades de los equipos (Tiempo estimado: 3-4 horas)

**[00:00 - 01:30] Completar análisis y refinamiento (90 min)**

1. **Revisar y mejorar personas** (30 min)
   - Releer personas generadas en la sesión
   - Añadir detalles faltantes
   - Asegurar coherencia entre las 3 personas
   - Opcional: Generar imágenes ilustrativas (con IA o bancos de imágenes)

2. **Ampliar escenarios de uso** (30 min)
   - Desarrollar narrativas completas para cada persona
   - Describir un viaje típico usando TravelEase
   - Incluir emociones, pensamientos, puntos de fricción

3. **Validar métricas** (30 min)
   - Revisar que métricas definidas son completas
   - Agregar valores objetivo (ej: "tiempo de reserva < 3 min")
   - Justificar por qué esas métricas son adecuadas

**[01:30 - 03:30] Redacción de informe técnico (120 min)**

Usando la plantilla proporcionada, redactar informe con estructura:

1. **Portada** (5 min)
   - Título del laboratorio
   - Nombres de integrantes del equipo
   - Fecha
   - Asignatura

2. **Resumen ejecutivo** (15 min)
   - ½ página con síntesis del análisis realizado
   - Principales hallazgos
   - Conclusiones clave

3. **Introducción** (20 min)
   - Contexto del caso TravelEase
   - Objetivos del análisis
   - Metodología utilizada (análisis según ISO 9241-11)

4. **Análisis de contexto de uso** (40 min)
   - **4.1 Identificación de usuarios**
     - Perfiles identificados (breve descripción de todos)
     - Justificación de selección de 3 perfiles principales
   - **4.2 Análisis de tareas**
     - Tabla de tareas por perfil
     - Descripción de tareas críticas
   - **4.3 Equipos y entornos**
     - Análisis de dispositivos utilizados
     - Contextos de uso (físico, técnico, social, cultural)

5. **Personas y escenarios** (30 min)
   - Presentación de las 3 personas (1-2 páginas cada una)
   - Escenarios de uso narrativos
   - Capturas de la generación con IA (anexo)

6. **Métricas de usabilidad** (20 min)
   - Tabla completa de métricas
   - Justificación de cada métrica
   - Relación con ISO 9241-11

7. **Reflexión y aprendizajes** (15 min)
   - ¿Qué aprendieron sobre análisis de contexto de uso?
   - ¿Cómo les ayudó la IA en el proceso?
   - ¿Qué desafíos encontraron?
   - ¿Cómo aplicarían esto en un proyecto real?

8. **Conclusiones** (10 min)
   - Síntesis de hallazgos
   - Importancia del análisis de contexto para el diseño

9. **Referencias** (5 min)
   - ISO 9241-11:2018
   - Papers leídos
   - Otras fuentes consultadas

**[03:30 - 04:00] Revisión y entrega final (30 min)**

- Revisar formato y ortografía
- Verificar que cumple rúbrica (autoevaluación)
- Generar PDF
- Subir a LMS antes de la fecha límite

---

## 👥 Gestión de Equipos y Roles

### Tamaño de Equipos
**Recomendado:** 2-3 estudiantes por equipo

**Justificación:**
- 2 personas: Bueno para clases pequeñas, permite más equipos, pero puede ser limitado para brainstorming
- 3 personas: **Ideal** - suficiente diversidad de ideas, roles claros, no demasiado grande
- 4+ personas: NO recomendado - riesgo de pasajeros, difícil coordinar

### Asignación de Roles (Rotan en cada lab)

**ROL 1: Analista ISO** 🔍
- Responsabilidades:
  - Interpretar el estándar ISO 9241-11
  - Verificar que el análisis cumple con requisitos
  - Liderar definición de métricas de usabilidad
  - Documentar decisiones basadas en el estándar
- Habilidades desarrolladas:
  - Lectura e interpretación de documentos técnicos
  - Pensamiento crítico
  - Atención al detalle

**ROL 2: Ingeniero de Prompts** 🤖
- Responsabilidades:
  - Gestionar interacciones con IA generativa
  - Adaptar prompts a necesidades específicas
  - Iterar para mejorar resultados de IA
  - Documentar proceso de generación
- Habilidades desarrolladas:
  - Prompt engineering
  - Comunicación con IA
  - Iteración y refinamiento

**ROL 3: Sintetizador de Información** 📊
- Responsabilidades:
  - Organizar información recopilada
  - Completar plantillas y tablas
  - Coordinar redacción de informe final
  - Asegurar coherencia del documento
- Habilidades desarrolladas:
  - Organización de información
  - Redacción técnica
  - Gestión de proyecto

📌 **Nota importante:** En equipos de 2, combinar roles 2 y 3.

### Estrategia de Rotación

| Laboratorio | Estudiante A | Estudiante B | Estudiante C |
|-------------|--------------|--------------|--------------|
| Lab 1 | Analista ISO | Ing. Prompts | Sintetizador |
| Lab 2 | Sintetizador | Analista ISO | Ing. Prompts |
| Lab 3 | Ing. Prompts | Sintetizador | Analista ISO |
| ... | (rotación continúa) | | |

**Beneficio:** Todos desarrollan todas las habilidades.

---

## 🎓 Estrategias Pedagógicas

### ANTES de la Sesión Presencial

#### 1 Semana Antes
- [ ] Subir todos los materiales al LMS en carpeta organizada:
  ```
  Lab 1 - Análisis de Contexto de Uso/
  ├── 📘 Guía del Estudiante
  ├── 📚 Lecturas Preparatorias/
  │   ├── ISO_9241-11_Extracto.pdf
  │   └── Paper_Context_of_Use.pdf
  ├── 📝 Plantillas/
  │   ├── Plantilla_Informe_Lectura.docx
  │   ├── Plantilla_Analisis_Contexto.xlsx
  │   └── Plantilla_Informe_Final.docx
  ├── 🤖 Prompts de IA
  └── ✅ Rúbrica de Evaluación
  ```
- [ ] Enviar correo/anuncio recordando:
  - Fecha de sesión presencial
  - Importancia de completar lecturas
  - Fecha límite de quiz y informe de lectura previa

#### 3 Días Antes
- [ ] Verificar que al menos 80% de estudiantes han accedido a materiales
- [ ] Enviar recordatorio a quienes no han accedido
- [ ] Probar que prompts de IA funcionan (pueden cambiar si actualizan modelos)

#### 1 Día Antes
- [ ] Revisar informes de lectura previa subidos
- [ ] Identificar preguntas comunes para abordar en clase
- [ ] Identificar estudiantes con conceptos incorrectos (contactar si es crítico)
- [ ] Preparar ejemplos adicionales si detecto confusión generalizada
- [ ] Formar equipos (si no se formaron antes) - considerar:
  - Diversidad de habilidades
  - Balance de personalidades (evitar equipos solo de tímidos o solo de dominantes)
  - Opcional: Usar herramienta como TeamMaker

#### Día de la Sesión (Antes de Clase)
- [ ] Llegar 15 min antes para preparar aula
- [ ] Verificar proyector, internet, timer
- [ ] Tener presentación abierta
- [ ] Tener prompts de respaldo en documento separado
- [ ] Imprimir checklist de evaluación (1 por equipo)
- [ ] Tener agua/café (¡es importante!)

---

### DURANTE la Sesión Presencial

#### Técnicas de Facilitación Activa

**1. Circulación Constante (80% del tiempo)**
- NO quedarse sentado en el escritorio
- Visitar cada equipo al menos 3 veces durante la sesión
- Patrón sugerido: rotación sistemática, no ir siempre a los mismos

**2. Preguntas Detonantes (No dar respuestas directas)**

En lugar de decir "Deberías considerar usuarios senior", preguntar:
- ❓ "¿Qué rango de edades han considerado?"
- ❓ "¿Todos los turistas usan tecnología de la misma manera?"
- ❓ "¿Qué pasa con personas con limitaciones físicas o cognitivas?"

**Banco de preguntas detonantes para este lab:**
- "¿Han pensado en usuarios internacionales que no hablan español?"
- "¿Qué dispositivo usaría alguien que está en el aeropuerto?"
- "¿Cómo cambia el contexto de uso si estás planificando vs. si ya estás viajando?"
- "¿Qué frustraciones tendrías tú al reservar un viaje online?"
- "¿Esta métrica es realmente medible? ¿Cómo la obtendrías?"

**3. Gestión de Ritmo**

**Equipos que van muy rápido:**
- Darles desafíos adicionales:
  - "Consideren un perfil de usuario extremo (ej: turista con discapacidad visual)"
  - "Generen una cuarta persona con características muy diferentes"
  - "Investiguen qué métricas usa realmente Booking.com o Airbnb"

**Equipos que van lentos:**
- Identificar el bloqueo:
  - ¿No entienden el concepto?
  - ¿Problemas técnicos con IA?
  - ¿Parálisis por análisis?
- Dar "ayuda calibrada":
  - Mostrar ejemplo de otro equipo (sin identificar)
  - Dar primer paso concreto: "Empiecen describiendo a alguien de su familia que viaje"
  - Simplificar: "Por ahora enfóquense en solo 2 perfiles, no 5"

**4. Checkpoints Grupales**

Cada 20-25 minutos, detener a todos por 1-2 minutos:
- "¿En qué punto están? Levanten la mano si ya tienen X"
- "Equipo 3, compartan rápidamente un perfil interesante que identificaron"
- "Tip general: He notado que algunos están... Recuerden que..."

**Beneficio:** 
- Sincroniza ritmo
- Permite compartir aprendizajes entre equipos
- Da descanso mental micro

**5. Fomentar Debate Respetuoso**

Cuando surgen discusiones en equipo (¡es bueno!):
- ✅ Permitir debate (no intervenir inmediatamente)
- ✅ Si se estancan, preguntar: "¿Qué dice ISO 9241-11 sobre esto?"
- ✅ Si persiste desacuerdo: "Interesante. Documenten ambas perspectivas en su informe"

**6. Gestión de Problemas Técnicos**

**IA no funciona / genera basura:**
- Tener prompts de respaldo probados
- Sugerir cambiar de IA (ChatGPT → Claude → Gemini)
- Si falla todo: tener ejemplos de personas pre-generadas como recurso de emergencia

**Internet caído:**
- Plan B: Trabajo en plantillas offline
- Generar personas manualmente basándose en ejemplos
- Continuar con análisis conceptual

---

### DESPUÉS de la Sesión Presencial

#### Mismo Día
- [ ] Enviar por correo/LMS:
  - Resumen de conceptos clave (1 página PDF)
  - Recordatorio de entregable final con fecha
  - Respuestas a preguntas comunes que surgieron
  - Mejores prácticas observadas (sin nombrar equipos)

#### Durante Período de Trabajo Autónomo
- [ ] Estar disponible para consultas (definir horario de tutoría)
- [ ] Responder dudas por correo/foro en máximo 24 horas
- [ ] Opcional: Sesión de consulta grupal online (30-45 min) a mitad de plazo

#### Después de Recibir Entregas
- [ ] Evaluar usando rúbrica (ver rubrica_evaluacion.md)
- [ ] Dar feedback individual por equipo en 48-72 horas
- [ ] Identificar errores comunes para abordar en siguiente lab
- [ ] Seleccionar 2-3 mejores trabajos (anónimos) para compartir como referencia

#### Feedback Efectivo (Modelo de Feedback Constructivo)

**Estructura de feedback individual por equipo:**

```
Equipo X - Lab 1: Análisis de Contexto de Uso
Calificación: [X/10 o letra según sistema]

🎯 FORTALEZAS (lo que hicieron muy bien):
- [Aspecto específico bien logrado]
- [Ejemplo concreto de su trabajo]

📈 ÁREAS DE MEJORA (para crecer):
- [Aspecto específico a mejorar]
- [Sugerencia concreta de cómo mejorarlo]

💡 RECOMENDACIONES para Lab 2:
- [Consejo específico aplicable al siguiente lab]

📋 DETALLE DE EVALUACIÓN:
[Ver rúbrica adjunta con puntajes por criterio]
```

---

## ⚠️ Puntos Críticos y Soluciones

### Problema 1: Estudiantes no completan lecturas preparatorias

**Señales:**
- Quiz con tasas de aprobación < 60%
- Informes de lectura muy superficiales o copiados
- Preguntas básicas en clase que revelan no haber leído

**Impacto:**
- Sesión presencial se convierte en clase teórica (pérdida de tiempo de lab)
- Equipos no pueden hacer análisis de calidad sin base conceptual

**Soluciones preventivas:**
- ✅ Hacer quiz **obligatorio** y que valga % de nota (aunque sea pequeño, 5-10%)
- ✅ No permitir entrar a sesión presencial sin quiz aprobado (política estricta)
- ✅ Enviar recordatorios 1 semana, 3 días y 1 día antes
- ✅ Hacer lecturas más accesibles (extractos, no documento completo)

**Soluciones correctivas (si ya pasó):**
- Plan B: Convertir primeros 30 min de sesión en mini-clase teórica
- Reducir complejidad de las actividades
- Dar más guía directa (menos descubrimiento)

---

### Problema 2: IA no genera código/contenido esperado

**Señales:**
- Estudiantes dicen "la IA no funciona"
- Resultados muy genéricos o irrelevantes
- Frustración visible con la herramienta

**Causas comunes:**
- Prompts mal formulados (demasiado vagos o demasiado complejos)
- IA caída o con límite de uso alcanzado
- Estudiantes no entienden cómo iterar con IA

**Soluciones preventivas:**
- ✅ Probar todos los prompts 1-2 días antes de la sesión
- ✅ Tener prompts probados en múltiples IAs (ChatGPT, Claude, Gemini)
- ✅ Incluir ejemplos de "buena iteración" en materiales
- ✅ Explicar brevemente prompt engineering al inicio

**Soluciones correctivas:**
- Tener ejemplos de personas ya generadas como respaldo
- Ayudar a estudiantes a reformular prompts
- Permitir uso de otra IA alternativa
- En caso extremo: proveer contenido base y pedir que lo adapten

---

### Problema 3: Equipos terminan muy rápido (y superficialmente)

**Señales:**
- Equipo dice "ya terminamos" en minuto 40 de 120
- Entregables muy breves o superficiales
- Personas genéricas tipo "María, 30 años, le gusta viajar"

**Causa:**
- Falta de profundidad en análisis
- No entendieron el nivel de detalle esperado

**Soluciones preventivas:**
- ✅ Mostrar ejemplos de buenas personas vs. malas personas al inicio
- ✅ Tener clara rúbrica de evaluación (que vean que superficial = nota baja)
- ✅ Preparar "desafíos adicionales" de antemano

**Soluciones correctivas:**
- Hacer preguntas que revelen superficialidad:
  - "¿Por qué eligieron esa métrica específicamente?"
  - "¿Cómo validaron que esta persona es representativa?"
  - "¿Qué dice ISO 9241-11 sobre este elemento?"
- Asignar extensión del análisis:
  - "Generen una cuarta persona de un perfil muy diferente"
  - "Investiguen métricas que usa una plataforma real y compárenlas"
  - "Desarrollen el escenario de uso con más detalle narrativo"

---

### Problema 4: Equipos van muy lentos (parálisis por análisis)

**Señales:**
- Minuto 60 y aún no han generado nada con IA
- Discusiones interminables sobre detalles menores
- Ansiedad visible, preocupación por "hacerlo perfecto"

**Causa:**
- Perfeccionismo excesivo
- Falta de confianza para tomar decisiones
- Miedo a equivocarse

**Soluciones preventivas:**
- ✅ Enfatizar que es un proceso iterativo (pueden mejorar después)
- ✅ Establecer timeboxing estricto: "En X minutos pasamos a siguiente fase"
- ✅ Mostrar que no hay "una respuesta correcta"

**Soluciones correctivas:**
- Intervención directa: "Tomen una decisión ahora, tienen 2 minutos"
- Simplificar alcance: "Por ahora trabajen con 2 perfiles, no 5"
- Dar permiso para imperfección: "Lo importante es aplicar el proceso, pueden refinar después"
- Proveer ejemplo/base para que modifiquen (no empiecen de cero)

---

### Problema 5: Discrepancias en interpretación del estándar

**Señales:**
- Equipos llegan a conclusiones diferentes sobre el mismo concepto
- Confusión sobre si algo cumple o no ISO 9241-11
- Preguntas tipo "¿esto está bien o mal?"

**Realidad:**
- ¡Esto NO es un problema! Es DESEADO
- ISO 9241 requiere interpretación y aplicación al contexto

**Manejo pedagógico:**
- ✅ Fomentar el debate: "¿Qué piensan otros equipos?"
- ✅ Hacer que justifiquen con el estándar: "Muéstrenme dónde dice eso en ISO 9241-11"
- ✅ Permitir múltiples interpretaciones válidas si están fundamentadas
- ✅ NO dar "la respuesta correcta" si no es necesario

**En el informe:**
- Pedir que documenten su interpretación y justificación
- Valorar razonamiento, no coincidencia con "respuesta modelo"

---

### Problema 6: Problemas de dinámica de equipo

**Señales:**
- Un miembro domina, otros no participan
- Conflictos visibles, tensión
- Un miembro hace todo el trabajo

**Soluciones preventivas:**
- ✅ Asignar roles claros con responsabilidades específicas
- ✅ Rotar roles en cada lab (el dominante no puede ser siempre líder)
- ✅ Evaluación individual además de grupal (ver rúbrica)

**Soluciones correctivas:**
- Hablar con el equipo: "¿Cómo están distribuyendo el trabajo?"
- Intervenir si es necesario: "Quiero escuchar la opinión de [persona callada]"
- Si es grave: permitir cambio de equipo o trabajo individual (última instancia)

---

## 📊 Evaluación y Rúbrica

### Distribución de Calificación

| Componente | Peso | Momento |
|-----------|------|---------|
| **Informe de lectura previa** | 10% | Antes de sesión |
| **Participación en sesión presencial** | 15% | Durante sesión |
| **Informe técnico final** | 75% | Post-sesión |
| **TOTAL** | **100%** | |

---

### Rúbrica Detallada

Ver archivo completo: `rubrica_evaluacion.md`

**Resumen de criterios principales:**

1. **Comprensión de ISO 9241-11** (20%)
   - Definición correcta de usabilidad
   - Identificación de componentes de contexto de uso
   - Aplicación adecuada del estándar

2. **Calidad del análisis de contexto** (25%)
   - Diversidad y profundidad de perfiles de usuario
   - Completitud del análisis de tareas
   - Consideración de equipos y entornos

3. **Personas y escenarios** (20%)
   - Detalle y realismo de personas
   - Coherencia y relevancia de escenarios
   - Uso efectivo de IA generativa

4. **Métricas de usabilidad** (15%)
   - Especificidad y medibilidad
   - Alineación con ISO 9241-11
   - Adecuación al contexto

5. **Calidad del informe** (15%)
   - Estructura y organización
   - Redacción y claridad
   - Formato y presentación

6. **Reflexión y aprendizaje** (5%)
   - Profundidad de reflexión
   - Conexión teoría-práctica
   - Autocrítica constructiva

---

## 📝 Quiz de Comprensión de Lecturas (Ejemplos)

### Preguntas de Opción Múltiple (5-7 preguntas)

**Pregunta 1:**
Según ISO 9241-11, la usabilidad se define como:
- a) La facilidad de uso de un sistema
- b) El grado en que un sistema es intuitivo
- c) El grado en que un producto puede ser utilizado por usuarios específicos para lograr objetivos específicos con efectividad, eficiencia y satisfacción en un contexto de uso específico ✅
- d) La calidad de la experiencia del usuario

**Pregunta 2:**
Los cuatro componentes del contexto de uso según ISO 9241-11 son:
- a) Usuarios, objetivos, restricciones y resultados
- b) Usuarios, tareas, equipos y entornos ✅
- c) Personas, escenarios, dispositivos y métricas
- d) Efectividad, eficiencia, satisfacción y accesibilidad

**Pregunta 3:**
La efectividad en usabilidad se refiere a:
- a) La rapidez con la que se completa una tarea
- b) La satisfacción del usuario con el sistema
- c) La exactitud y completitud con la que los usuarios logran objetivos específicos ✅
- d) El número de errores cometidos

**Pregunta 4:**
Una métrica de eficiencia apropiada sería:
- a) Porcentaje de usuarios satisfechos
- b) Tiempo necesario para completar una tarea ✅
- c) Número de funcionalidades disponibles
- d) Calidad del diseño visual

**Pregunta 5:**
¿Cuál de los siguientes NO es un componente del entorno según ISO 9241-11?
- a) Entorno físico (iluminación, ruido, etc.)
- b) Entorno técnico (plataformas, conectividad)
- c) Entorno competitivo (otros productos similares) ✅
- d) Entorno social y cultural

### Preguntas Abiertas Cortas (2-3 preguntas)

**Pregunta 6:**
Explica con tus propias palabras la diferencia entre eficiencia y efectividad en usabilidad. Da un ejemplo concreto de cada una.

**Respuesta esperada (rúbrica):**
- Efectividad = logro de objetivos (¿lo completó?)
- Eficiencia = recursos empleados (¿cuánto esfuerzo requirió?)
- Ejemplo concreto y correcto de cada uno

**Pregunta 7:**
¿Por qué es importante analizar el contexto de uso antes de diseñar un sistema? ¿Qué podría pasar si no se hace?

**Respuesta esperada:**
- Importancia: diseñar para usuarios/contextos reales, no asumidos
- Consecuencias de no hacerlo: sistema no útil/usable, rechazo de usuarios
- Menciona al menos 2 razones válidas

---

## 🔗 Conexión con Otros Laboratorios

### Laboratorios Previos Requeridos
- **Ninguno** (Este es el Lab 1, introductorio)

### Este Laboratorio Prepara Para:

**Lab 2: Principios de Diálogo (ISO 9241-110)**
- Las personas creadas aquí se usan para diseñar la interfaz de búsqueda
- Los contextos de uso informan decisiones de diseño
- Las métricas definidas se usarán para evaluar diseños

**Lab 3: Diseño Centrado en Usuario (ISO 9241-210)**
- El análisis de contexto es la primera fase del proceso UCD
- Las personas son usuarios representativos para tests
- Las tareas identificadas guían el diseño iterativo

**Labs 4-10:**
- Todos los laboratorios subsecuentes usan las personas y contextos definidos aquí
- El sistema TravelEase se construye progresivamente considerando estos usuarios

### Conceptos que se Retoman:
- **Ninguno** (primer laboratorio)

---

## 📚 Recursos Adicionales para el Docente

### Lecturas de Profundización (Opcional para docentes)

1. **ISO 9241-11:2018 completa**
   - Para entender el contexto completo del estándar
   
2. **Bevan, N. (2009). "International standards for HCI"**
   - Encyclopedia of Human-Computer Interaction, Chapter on ISO 9241

3. **Norman, D. (2013). "The Design of Everyday Things"**
   - Capítulo sobre User-Centered Design (complementa ISO 9241-210)

4. **Cooper, A., Reimann, R., Cronin, D. (2014). "About Face: The Essentials of Interaction Design"**
   - Capítulo sobre Personas (técnica en profundidad)

### Videos Recomendados (Para mostrar en clase si hay tiempo)

1. **"What is Usability?"** - Nielsen Norman Group (5 min)
   - Introducción visual a usabilidad

2. **"Creating Personas"** - Interaction Design Foundation (8 min)
   - Cómo crear personas efectivas

### Herramientas Útiles

1. **Generadores de Personas:**
   - Xtensio User Persona Creator (plantillas visuales)
   - HubSpot Make My Persona (interactivo)

2. **Calculadoras de Métricas:**
   - System Usability Scale (SUS) Calculator
   - NPS Calculator

3. **Bancos de Imágenes para Personas:**
   - Generated Photos (rostros generados con IA)
   - Unsplash, Pexels (fotos libres)

---

## ✅ Checklist Pre-Sesión para Docente

**1 Semana Antes:**
- [ ] Materiales subidos a LMS
- [ ] Quiz configurado y funcional
- [ ] Plantillas creadas y accesibles
- [ ] Correo de anuncio enviado

**3 Días Antes:**
- [ ] Verificar acceso de estudiantes a materiales (analytics de LMS)
- [ ] Probar prompts de IA (ChatGPT, Claude, Gemini)
- [ ] Recordatorio enviado

**1 Día Antes:**
- [ ] Revisar informes de lectura subidos
- [ ] Identificar conceptos para reforzar
- [ ] Formar equipos (si aplicable)
- [ ] Preparar presentación

**Día de la Sesión:**
- [ ] Llegar 15 min antes
- [ ] Verificar tecnología (proyector, internet, timer)
- [ ] Tener prompts de respaldo
- [ ] Imprimir checklists (1 por equipo)
- [ ] Café/agua ☕

**Durante Sesión:**
- [ ] Circular constantemente (no quedarse sentado)
- [ ] Hacer preguntas detonantes (no dar respuestas directas)
- [ ] Checkpoints cada 20-25 min
- [ ] Monitorear ritmo (ayudar a lentos, desafiar a rápidos)

**Mismo Día Post-Sesión:**
- [ ] Enviar resumen de conceptos
- [ ] Recordar fecha de entrega
- [ ] Compartir mejores prácticas observadas

---

## 🎓 Notas Finales para el Docente

### Filosofía Pedagógica de Este Laboratorio

Este laboratorio está diseñado bajo los principios de:

1. **Aprendizaje Activo:** Estudiantes construyen conocimiento haciendo, no solo escuchando
2. **Constructivismo Social:** Trabajo en equipo, discusión, múltiples perspectivas
3. **Aprendizaje Basado en Casos:** Caso realista que motiva y da contexto
4. **Reflexión Metacognitiva:** Estudiantes piensan sobre su propio proceso de aprendizaje
5. **Tecnología como Herramienta:** IA facilita, no sustituye el pensamiento crítico

### Su Rol como Docente

**Usted NO es:**
- ❌ Un instructor que da respuestas correctas
- ❌ Un técnico que resuelve problemas de IA
- ❌ Un evaluador que busca errores

**Usted ES:**
- ✅ Un facilitador que guía el descubrimiento
- ✅ Un diseñador de experiencias de aprendizaje
- ✅ Un coach que desarrolla habilidades de pensamiento
- ✅ Un experto que conecta teoría (ISO 9241) con práctica (caso turismo)

### Adaptabilidad

Esta guía es **exhaustiva intencionalmente** para cubrir múltiples escenarios, pero:

- ✅ **Adáptela** a su contexto institucional
- ✅ **Simplifíquela** si su grupo es pequeño o tiene menos tiempo
- ✅ **Amplíela** si tiene recursos adicionales
- ✅ **Personalícela** con ejemplos de su región/cultura

**Lo esencial que NO debe cambiar:**
1. Preparación previa con lecturas (estudiantes deben llegar preparados)
2. Uso de ISO 9241-11 como referencia técnica
3. IA como herramienta de desarrollo (no programación manual)
4. Énfasis en análisis y evaluación (no solo ejecución)
5. Conexión explícita entre teoría del estándar y práctica del caso

---

## 📧 Contacto y Mejora Continua

**Para el Docente que Usa Este Material:**

Después de impartir este laboratorio, considere:

1. **Autoevaluación:**
   - ¿Qué funcionó bien?
   - ¿Qué ajustaría para la próxima vez?
   - ¿Los tiempos fueron realistas?

2. **Feedback de Estudiantes:**
   - Incluir 2-3 preguntas de feedback en el informe final
   - ¿Qué fue más útil? ¿Qué fue confuso?

3. **Mejora del Material:**
   - Actualizar esta guía con aprendizajes
   - Compartir mejores prácticas con colegas
   - Adaptar según evolución de herramientas (IA cambia rápido)

---

**¡Éxito con el laboratorio! 🚀**

*Este material es parte de la serie de 10 laboratorios sobre ISO 9241 aplicado a sistemas de gestión turística.*
