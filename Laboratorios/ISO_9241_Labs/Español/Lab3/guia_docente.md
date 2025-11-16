# Laboratorio 3: Evaluación Heurística y Testing de Usabilidad
## Guía Docente

### Información General
- **Asignatura:** Interacción Persona-Computador
- **Laboratorio:** Lab 3 - Evaluación de Usabilidad
- **Estándares:** ISO 9241-11 (Usabilidad) e ISO 9241-110 (Principios de Diálogo)
- **Plataforma de análisis:** Airbnb (https://www.airbnb.es)
- **Duración:** 2 horas presenciales + trabajo preparatorio
- **Modalidad:** Presencial con componente práctico

---

## OBJETIVOS DE APRENDIZAJE

### Objetivos Generales
- Aplicar métodos de evaluación de usabilidad según ISO 9241-11
- Realizar evaluación heurística basada en ISO 9241-110
- Medir eficacia, eficiencia y satisfacción en interfaces reales
- Generar reportes de usabilidad con recomendaciones priorizadas

### Competencias Específicas
1. **Competencia evaluativa:** Aplicar métodos sistemáticos de evaluación de usabilidad
2. **Competencia analítica:** Identificar problemas de usabilidad y clasificarlos por severidad
3. **Competencia normativa:** Aplicar estándares ISO en evaluación de interfaces
4. **Competencia práctica:** Usar herramientas profesionales de testing de usabilidad

---

## ESTRUCTURA TEMPORAL

### Trabajo Preparatorio (1 hora)
**Semana previa al laboratorio:**
- Lectura de materiales ISO 9241-11 y 9241-110
- Familiarización con Airbnb como usuario
- Revisión de métodos de evaluación heurística
- Preparación de materiales de testing

### Sesión Presencial (2 horas)

#### **Bloque 1: Testing de Usuarios (50 minutos)**
- **10 min:** Explicación del protocolo ISO 9241-11
- **30 min:** Ejecución de testing con observación
- **10 min:** Consolidación de datos y métricas

#### **Bloque 2: Evaluación Heurística (50 minutos)**
- **10 min:** Repaso de principios ISO 9241-110
- **35 min:** Evaluación sistemática de Airbnb
- **5 min:** Puntuación y clasificación de hallazgos

#### **Bloque 3: Síntesis y Reporte (20 minutos)**
- **15 min:** Integración de resultados de ambos métodos
- **5 min:** Planificación del reporte final

### Trabajo Post-Laboratorio (2 horas)
- Análisis detallado de datos recopilados
- Redacción del reporte de usabilidad
- Propuestas de mejora priorizadas

---

## METODOLOGÍA DE TRABAJO

### Organización de Equipos
- **Equipos de 3 estudiantes** (óptimo para roles diferenciados)
- **Roles rotativos:**
  - **Usuario:** Ejecuta tareas mientras verbaliza pensamientos
  - **Observador:** Registra tiempos, errores y comentarios
  - **Moderador:** Guía el proceso y toma notas adicionales

### Materiales Necesarios por Equipo
- **Hardware:**
  - 1 ordenador con conexión a internet
  - Cronómetro (físico o app móvil)
  - Hojas para anotaciones o tablet
- **Software:**
  - Navegador web actualizado
  - Acceso a Airbnb.es
  - Plantillas de evaluación (proporcionadas)

### Protocolo de Seguridad Digital
- **No crear cuentas reales** en Airbnb durante el testing
- **Usar modo navegación privada** para consistencia
- **No proporcionar datos personales** reales
- **Detenerse antes del pago** en proceso de reserva

---

## DESARROLLO DE LA SESIÓN

### BLOQUE 1: Testing de Usuarios según ISO 9241-11

#### **Preparación (10 minutos)**

**Explicación del protocolo:**
```
Protocolo ISO 9241-11 - Testing de Usabilidad:

1. EFICACIA: ¿Se completan las tareas correctamente?
   - Medición: % de tareas completadas exitosamente
   - Registro: Sí/No para cada subtarea

2. EFICIENCIA: ¿Cuánto esfuerzo requiere completar las tareas?
   - Medición: Tiempo por tarea, número de errores
   - Registro: Cronómetro + contador de errores

3. SATISFACCIÓN: ¿Qué opina el usuario de la experiencia?
   - Medición: Escala SUS + comentarios cualitativos
   - Registro: Cuestionario post-tarea
```

**Configuración del entorno:**
- Abrir Airbnb.es en modo incógnito
- Tener plantillas de registro preparadas
- Asignar roles iniciales en el equipo
- Verificar funcionamiento del cronómetro

#### **Ejecución del Testing (30 minutos)**

**Tareas específicas a evaluar:**

**Tarea 1: Búsqueda básica (8 minutos)**
```
Contexto: Quieres ir a Barcelona el próximo fin de semana
Objetivo: Encontrar un apartamento para 2 personas, 1 noche
Subtareas:
□ Introducir destino "Barcelona"
□ Seleccionar fechas (próximo sábado-domingo)
□ Configurar 2 huéspedes
□ Ejecutar búsqueda
□ Revisar primeros 5 resultados

Métricas a registrar:
- Tiempo total: _____ segundos
- Errores cometidos: _____ 
- Tarea completada: Sí / No
- Comentarios del usuario: ________________
```

**Tarea 2: Filtrado avanzado (10 minutos)**
```
Contexto: Los resultados son muchos, necesitas filtrar
Objetivo: Aplicar filtros específicos para encontrar opciones ideales
Subtareas:
□ Aplicar filtro de precio: 50-100€ por noche
□ Seleccionar tipo: "Apartamento entero"
□ Activar amenidad: "WiFi gratuito"
□ Revisar cambios en resultados
□ Limpiar filtros y volver a aplicar uno diferente

Métricas a registrar:
- Tiempo total: _____ segundos
- Errores cometidos: _____ 
- Número de filtros aplicados correctamente: _____
- Facilidad de uso (1-5): _____
```

**Tarea 3: Exploración de alojamiento (12 minutos)**
```
Contexto: Has encontrado un apartamento interesante
Objetivo: Obtener información detallada para decidir reserva
Subtareas:
□ Seleccionar un alojamiento de los resultados
□ Revisar fotos y descripción
□ Verificar ubicación en el mapa
□ Leer reseñas de otros huéspedes
□ Revisar políticas de cancelación
□ Identificar precio total (con tasas)

Métricas a registrar:
- Tiempo total: _____ segundos
- Información encontrada exitosamente: ___/6
- Claridad de la información (1-5): _____
- Confianza para reservar (1-5): _____
```

#### **Consolidación de Datos (10 minutos)**

**Cálculo de métricas ISO 9241-11:**
```
EFICACIA:
- Tareas completadas exitosamente: ___/3 (___%)
- Subtareas completadas: ___/17 (___%)

EFICIENCIA:
- Tiempo promedio por tarea: _____ segundos
- Errores totales: _____
- Eficiencia relativa: _____ tareas/minuto

SATISFACCIÓN:
- Facilidad de uso promedio: ___/5
- Confianza promedio: ___/5
- ¿Recomendaría Airbnb? Sí / No
```

### BLOQUE 2: Evaluación Heurística según ISO 9241-110

#### **Repaso de Principios (10 minutos)**

**Los 7 Principios de Diálogo ISO 9241-110:**
```
1. ADECUACIÓN A LA TAREA
   ¿Proporciona exactamente lo necesario para completar tareas?

2. AUTODESCRIPCIÓN  
   ¿Es inmediatamente comprensible qué hacer en cada momento?

3. CONTROLABILIDAD
   ¿Puede el usuario controlar el ritmo y secuencia de acciones?

4. CONFORMIDAD CON EXPECTATIVAS
   ¿Se comporta como esperan los usuarios basado en convenciones?

5. TOLERANCIA A ERRORES
   ¿Previene errores y permite recuperación fácil?

6. ADAPTABILIDAD
   ¿Se puede personalizar según necesidades del usuario?

7. CAPACIDAD DE APRENDIZAJE
   ¿Es fácil de aprender y mejorar con la práctica?
```

#### **Evaluación Sistemática (35 minutos)**

**Metodología por principio (5 minutos cada uno):**

**Principio 1: Adecuación a la tarea**
```
Áreas a evaluar en Airbnb:
□ Página principal: ¿Enfocada en búsqueda de alojamiento?
□ Filtros: ¿Relevantes para seleccionar alojamiento?
□ Resultados: ¿Información esencial visible?
□ Detalle: ¿Datos necesarios para decisión de reserva?

Escala de evaluación:
1 = Muy inadecuado  |  3 = Neutral  |  5 = Muy adecuado

Puntuación: ___/5
Problemas identificados:
_________________________________
Evidencias específicas:
_________________________________
```

**[Similar estructura para los 6 principios restantes]**

#### **Clasificación de Hallazgos (5 minutos)**

**Sistema de severidad:**
```
CRÍTICO (Puntuación 1-2):
- Impide completar tareas principales
- Frustra significativamente al usuario
- Viola múltiples principios ISO

MAYOR (Puntuación 2-3):
- Dificulta completar tareas
- Causa confusión o demoras
- Viola claramente un principio ISO

MENOR (Puntuación 3-4):
- Molestia leve o inconsistencia
- No impide completar tareas
- Mejora potencial identificada

COSMÉTICO (Puntuación 4-5):
- Mejora estética o de pulimento
- No afecta usabilidad funcional
- Optimización de experiencia
```

### BLOQUE 3: Síntesis y Planificación (20 minutos)

#### **Integración de Resultados (15 minutos)**

**Template de síntesis:**
```
RESUMEN EJECUTIVO:

Testing de Usuarios (ISO 9241-11):
- Eficacia general: ___% 
- Eficiencia promedio: ___ seg/tarea
- Satisfacción: ___/5
- Principales obstáculos: ________________

Evaluación Heurística (ISO 9241-110):
- Puntuación global: ___/35 (___%)
- Principio más violado: ________________
- Principio mejor cumplido: ________________
- Problemas críticos: ___ | Mayores: ___ | Menores: ___

CORRELACIONES:
- ¿Los problemas heurísticos explican los errores de usuario? ________
- ¿Los principios bien evaluados correlacionan con alta satisfacción? ________
```

#### **Planificación del Reporte (5 minutos)**

**Estructura del reporte final:**
```
1. INTRODUCCIÓN (500 palabras)
   - Objetivos de la evaluación
   - Metodología aplicada (ISO 9241-11 y 9241-110)
   - Descripción de participantes

2. RESULTADOS TESTING DE USUARIOS (800 palabras)
   - Métricas de eficacia, eficiencia y satisfacción
   - Análisis por tarea
   - Principales obstáculos identificados

3. RESULTADOS EVALUACIÓN HEURÍSTICA (800 palabras)
   - Puntuación por principio ISO 9241-110
   - Problemas clasificados por severidad
   - Evidencias específicas por hallazgo

4. RECOMENDACIONES (600 palabras)
   - Top 5 mejoras priorizadas
   - Impacto esperado en métricas ISO
   - Esfuerzo de implementación estimado

5. CONCLUSIONES (300 palabras)
   - Síntesis de hallazgos
   - Reflexiones sobre métodos aplicados
```

---

## GESTIÓN DE DIFICULTADES

### Problemas Técnicos Comunes

**Problema: Airbnb no carga o es muy lento**
```
Solución inmediata:
1. Verificar conexión a internet
2. Cambiar a navegador alternativo
3. Usar datos móviles como backup
4. Si persiste: usar capturas pre-preparadas para evaluación heurística
```

**Problema: Estudiantes no pueden avanzar en una tarea**
```
Protocolo de intervención:
1. Permitir 2 minutos adicionales de intento
2. Registrar como "no completada" en métricas
3. Guiar al paso siguiente para continuar evaluación
4. Documentar obstáculo como hallazgo crítico
```

### Dinamización de Equipos

**Si un equipo va muy lento:**
- Asignar cronómetros más estrictos
- Enfocar en problemas más evidentes
- Priorizar completar todas las tareas vs. análisis exhaustivo

**Si un equipo termina muy rápido:**
- Solicitar mayor detalle en observaciones
- Añadir tarea opcional: evaluar versión móvil
- Que actúen como "consultores" para otros equipos

### Gestión de Discusiones

**Si hay desacuerdo en puntuaciones:**
```
Protocolo de resolución:
1. Revisar definición del principio ISO específico
2. Buscar evidencias concretas en la interfaz
3. Documentar ambas perspectivas si persiste desacuerdo
4. Enfocar en justificación más que en consenso
```

---

## EVALUACIÓN DE LA SESIÓN

### Objetivos de Aprendizaje Verificables

**Al finalizar la sesión, los estudiantes deben poder:**

✅ **Aplicar protocolo ISO 9241-11:**
- Diseñar tareas representativas para testing
- Medir eficacia, eficiencia y satisfacción
- Calcular métricas objetivas de usabilidad

✅ **Ejecutar evaluación heurística ISO 9241-110:**
- Identificar violaciones de cada principio
- Clasificar problemas por severidad
- Proporcionar evidencias específicas

✅ **Integrar métodos de evaluación:**
- Correlacionar hallazgos cuantitativos y cualitativos
- Priorizar recomendaciones basado en impacto
- Generar reportes profesionales de usabilidad

### Indicadores de Éxito de la Sesión

**Participación activa (observable durante sesión):**
- Equipos completan al menos 2 de las 3 tareas de testing
- Todos los estudiantes participan en roles asignados
- Se registran datos en todas las plantillas proporcionadas

**Comprensión conceptual (verificable en discusiones):**
- Estudiantes pueden explicar diferencia entre eficacia y eficiencia
- Identifican al menos 3 principios ISO 9241-110 en Airbnb
- Relacionan problemas observados con métricas medidas

**Aplicación práctica (evidenciable en entregas):**
- Reportes incluyen métricas cuantificadas según ISO 9241-11
- Evaluaciones heurísticas justificadas con evidencias
- Recomendaciones priorizadas por severidad e impacto

---

## MATERIALES DE APOYO

### Plantillas Imprimibles
- Formulario de registro de testing de usuarios
- Checklist de evaluación heurística ISO 9241-110
- Template de síntesis de resultados
- Cronograma de sesión para equipos

### Recursos Digitales
- Acceso a Airbnb.es (verificar disponibilidad previa)
- Timer online compartido para toda la clase
- Documento colaborativo para consolidar hallazgos
- Grabación de pantalla opcional para análisis posterior

### Referencias Normativas
- ISO 9241-11:2018 - Ergonomics of human-system interaction
- ISO 9241-110:2020 - Dialogue principles
- Nielsen, J. (1994) - 10 Usability Heuristics (correlación con ISO)
- Brooke, J. (1995) - System Usability Scale (SUS)

---

## CONEXIÓN CON OTROS LABORATORIOS

### Prerequisitos de Laboratorios Anteriores
- **Lab 1:** Conocimiento de personas y contextos de uso
- **Lab 2:** Comprensión de principios de diseño de diálogo
- **Conceptos base:** Familiaridad con usabilidad y UX

### Preparación para Laboratorios Siguientes
- **Lab 4:** Testing de accesibilidad (WCAG + ISO 9241)
- **Lab 5:** Diseño iterativo basado en evaluaciones
- **Habilidades:** Métodos cuantitativos de evaluación de UX

### Aplicación Transversal
- **Proyectos finales:** Evaluación de prototipos desarrollados
- **Casos reales:** Metodología aplicable a cualquier interfaz
- **Competencias profesionales:** Testing de usabilidad en la industria

---

## ADAPTACIONES PARA DIFERENTES CONTEXTOS

### Modalidad Online (si necesaria)
- **Testing colaborativo:** Un estudiante comparte pantalla mientras otros observan
- **Breakout rooms:** Equipos pequeños para evaluación heurística
- **Herramientas:** Miro/Mural para colaboración visual
- **Grabación:** Sesiones grabadas para revisión posterior

### Grupos Grandes (+30 estudiantes)
- **Rotación de estaciones:** 3 estaciones con diferentes aspectos de Airbnb
- **Consolidación grupal:** Resultados agregados de todos los equipos
- **Competencia:** Ranking de equipos por completitud de evaluación

### Estudiantes con Experiencia Avanzada
- **Tareas adicionales:** Evaluación de versión móvil vs. desktop
- **Análisis comparativo:** Airbnb vs. Booking vs. Vrbo en paralelo
- **Métodos avanzados:** Eye tracking simulado, Think Aloud Protocol

---

## SEGUIMIENTO POST-LABORATORIO

### Entregables Esperados (1 semana después)
- **Reporte individual:** 3000 palabras aplicando plantilla proporcionada
- **Datos cuantitativos:** Hojas de cálculo con métricas ISO 9241-11
- **Propuestas de mejora:** Top 5 recomendaciones priorizadas

### Criterios de Calidad
- **Rigor metodológico:** Aplicación correcta de protocolos ISO
- **Evidencias:** Capturas de pantalla y datos específicos
- **Análisis:** Correlación entre métodos cuantitativos y cualitativos
- **Practicidad:** Recomendaciones implementables y justificadas

### Retroalimentación Estructurada
- **Rubrica detallada:** Disponible en rubrica_evaluacion.md
- **Feedback individual:** Comentarios sobre aplicación de métodos ISO
- **Consolidación grupal:** Discusión de hallazgos comunes en clase siguiente

---

**Elaborado por:** [Nombre del docente]  
**Fecha de última actualización:** Noviembre 2024  
**Versión:** 1.0  
**Tiempo de preparación estimado:** 30 minutos