````markdown
# Laboratorio 5: Evaluación Integral de Usabilidad con Métodos Mixtos

## 📋 Información General

| Aspecto | Detalle |
|---------|---------|
| **Estándar aplicado** | ISO 9241-11:2018 (Métricas de Usabilidad) + ISO 9241-110:2020 |
| **Duración total** | 10-12 horas |
| **Distribución** | 3h preparación + 3h presencial + 4-6h análisis y reporte |
| **Trabajo en equipo** | SÍ - MISMOS equipos Labs anteriores (2-3 personas) |
| **Modalidad** | Híbrida con componente práctico intensivo |
| **Ponderación** | 15% de la asignatura |
| **Prerequisitos** | ⚠️ **Labs 1-4 COMPLETADOS** (necesitas personas, diseños y evaluaciones previas) |

---

## 🎯 Objetivos de Aprendizaje

Al completar este laboratorio, serás capaz de:

✅ **Planificar** estudios de usabilidad aplicando metodología científica ISO 9241-11  
✅ **Ejecutar** testing de usabilidad con usuarios reales y mediciones objetivas  
✅ **Combinar** evaluación heurística con testing empírico para validación cruzada  
✅ **Analizar** datos cuantitativos y cualitativos usando herramientas estadísticas  
✅ **Generar** recomendaciones priorizadas basadas en evidencia científica  
✅ **Presentar** hallazgos de usabilidad a stakeholders técnicos y de negocio

---

## 🔬 Fundamentos Metodológicos

### ISO 9241-11: Metodología de Medición de Usabilidad

**Usabilidad = f(Efectividad, Eficiencia, Satisfacción, Contexto)**

**EFECTIVIDAD (¿Se logra el objetivo?)**
- **Métrica primaria:** Tasa de finalización de tareas (%)
- **Métricas secundarias:** Tasa de errores, calidad del resultado
- **Cálculo:** (Tareas completadas exitosamente / Tareas totales intentadas) × 100

**EFICIENCIA (¿Con qué esfuerzo?)**
- **Métrica primaria:** Tiempo por tarea (segundos)
- **Métricas secundarias:** Clicks/taps, cognitive load, eficiencia relativa
- **Cálculo:** Tareas exitosas por unidad de tiempo o esfuerzo

**SATISFACCIÓN (¿Qué siente el usuario?)**
- **Métrica primaria:** System Usability Scale (SUS)
- **Métricas secundarias:** Net Promoter Score (NPS), emociones, preferencias
- **Cálculo:** Escalas estandarizadas + análisis cualitativo

### Metodología de Investigación Mixta

**CUANTITATIVO (What + How much)**
- Métricas objetivas de rendimiento
- Análisis estadístico de diferencias
- Comparación con benchmarks industriales

**CUALITATIVO (Why + How)**
- Think-aloud protocols
- Observación de comportamiento
- Entrevistas post-sesión

**TRIANGULACIÓN**
- Validación cruzada entre métodos
- Identificación de discrepancias
- Construcción de narrativa completa

---

## 📚 Fase 1: Preparación y Planificación (3 horas)

### 📖 Actividad 1: Revisión Metodológica Avanzada (90 min)

**Material obligatorio:**

**Lectura 1: ISO 9241-11:2018 - Secciones avanzadas**
- Sección 6: Especificación y medición de usabilidad (páginas 12-18)
- Sección 7: Explicación de las medidas de usabilidad (páginas 18-25)
- Anexo A: Orientación sobre la especificación de contexto de uso (páginas 26-30)

**Lectura 2: Paper metodológico**
- Tullis & Albert (2013). "Measuring the User Experience" - Capítulo 3: "Performance Metrics"
- Enfoque en: reliability, validity, statistical significance

**Lectura 3: Benchmarks industriales**
- Sauro & Lewis (2016). "Quantifying the User Experience" - Appendix A: "UX Benchmark Datasets"

**Mientras lees, anota:**
- ¿Cómo calcular intervalos de confianza para métricas de usabilidad?
- ¿Cuándo usar tests paramétricos vs. no-paramétricos?
- ¿Qué tamaño de muestra es necesario para detectar diferencias significativas?
- ¿Cómo interpretar una puntuación SUS de 68 vs. 74?

### 🎯 Actividad 2: Diseño del Estudio de Usabilidad (60 min)

**Objetivo:** Crear protocolo completo para evaluar el diseño que desarrollaron en Lab 2.

#### Paso 2.1: Definir Preguntas de Investigación (15 min)

**Preguntas obligatorias a responder:**

**RQ1: Efectividad**
- ¿Los usuarios pueden completar tareas de búsqueda de experiencias turísticas?
- ¿Cuál es la tasa de errores por tipo de tarea?
- ¿Qué tareas son más problemáticas?

**RQ2: Eficiencia** 
- ¿Cuánto tiempo toman las tareas principales?
- ¿Cómo se compara con benchmarks de la industria (Booking.com, Airbnb)?
- ¿Cuál es la curva de aprendizaje?

**RQ3: Satisfacción**
- ¿Cuál es la puntuación SUS del diseño?
- ¿Los usuarios recomendarían TravelEase?
- ¿Qué aspectos generan más frustración o satisfacción?

**RQ4: Validación de Lab 2**
- ¿Los principios ISO 9241-110 aplicados realmente mejoraron la usabilidad?
- ¿Hay correlación entre cumplimiento de principios y métricas objetivas?

#### Paso 2.2: Operacionalizar Variables (20 min)

**Completa esta tabla:**

| Variable | Definición Operacional | Método de Medición | Meta/Benchmark |
|----------|------------------------|-------------------|----------------|
| Efectividad | % de tareas completadas sin errores críticos | Observación binaria (éxito/fallo) | >80% (estándar industria) |
| Eficiencia temporal | Tiempo promedio para completar búsqueda completa | Cronómetro (segundos) | <120 seg (benchmark Booking) |
| Eficiencia de interacción | Clicks/taps hasta completar reserva | Contador de interacciones | <15 clicks (benchmark Airbnb) |
| Satisfacción general | Puntuación SUS | Cuestionario SUS (10 items) | >70 (promedio industria) |
| Intención de uso | Net Promoter Score | "¿Recomendarías TravelEase?" (0-10) | >6 (promotores netos) |
| Carga cognitiva | Esfuerzo mental percibido | NASA-TLX (subscala mental demand) | <60/100 |

#### Paso 2.3: Diseñar Tareas de Testing (25 min)

**Basándote en las personas del Lab 1, diseña 5-6 tareas:**

**TAREA 1: Búsqueda básica (Laura - mochilera)**
- **Contexto:** "Eres una estudiante de 24 años que quiere viajar a Lisboa con 400€ de presupuesto total"
- **Objetivo:** Encontrar y preseleccionar 2 opciones de experiencias completas
- **Criterios de éxito:** 
  - Encuentra opciones dentro del presupuesto
  - Incluye alojamiento + actividades
  - Guarda o marca las opciones seleccionadas
- **Tiempo límite:** 5 minutos
- **Métrica principal:** Tiempo hasta encontrar primera opción viable

**TAREA 2: Filtrado avanzado (Usuario experto)**
- **Contexto:** "Planificas viaje familiar a Barcelona, 2 adultos + 1 niño de 8 años"
- **Objetivo:** Usar filtros para encontrar experiencias child-friendly
- **Criterios de éxito:**
  - Aplica filtros de grupo familiar
  - Identifica servicios para niños
  - Compara al menos 3 opciones
- **Tiempo límite:** 4 minutos
- **Métrica principal:** Número de filtros utilizados correctamente

**TAREA 3: Evaluación de confianza (Todos los perfiles)**
- **Contexto:** "Has encontrado una experiencia que te interesa"
- **Objetivo:** Decidir si tienes suficiente información para reservar
- **Criterios de éxito:**
  - Revisa detalles de la experiencia
  - Lee reseñas de usuarios
  - Evalúa políticas de cancelación
- **Tiempo límite:** 6 minutos
- **Métrica principal:** Nivel de confianza declarado (1-7)

**TAREA 4: Recuperación de errores**
- **Contexto:** "Te das cuenta que las fechas que seleccionaste están mal"
- **Objetivo:** Corregir fechas sin perder filtros aplicados
- **Criterios de éxito:**
  - Modifica fechas
  - Mantiene otras configuraciones
  - Obtiene nuevos resultados
- **Tiempo límite:** 2 minutos
- **Métrica principal:** ¿Logra corregir sin empezar de nuevo? (Sí/No)

**TAREA 5: Exploración libre**
- **Contexto:** "Explora TravelEase como lo harías normalmente"
- **Objetivo:** Interacción natural sin restricciones
- **Criterios de éxito:** Navegación fluida por 5 minutos
- **Métrica principal:** Número de funcionalidades descubiertas

#### Paso 2.4: Planificación de Participantes (15 min)

**Criterios de selección:**

**Muestra objetivo:** 9-12 participantes
- 3-4 representando Persona 1 (mochileros jóvenes)
- 3-4 representando Persona 2 (familias)
- 3-4 representando Persona 3 (viajeros de negocios)

**Criterios de inclusión:**
- Edad 18-65 años
- Experiencia con plataformas de viajes online
- Sin discapacidades que afecten uso de interfaces web
- Consentimiento informado firmado

**Criterios de exclusión:**
- Estudiantes del curso (para evitar sesgo)
- Empleados de industria turística
- Familiares directos del equipo evaluador

**Plan de reclutamiento:**
- Universidad: estudiantes de otras facultades
- Redes sociales: convocatoria específica
- Red de contactos: amigos, conocidos
- Incentivo: [definir con docente]

### ✅ Actividad 3: Validación del Protocolo (30 min)

**Paso 3.1: Pilot testing (15 min)**
- Un miembro del equipo actúa como participante
- Otro ejecuta el protocolo completo
- Tercero toma notas de problemas

**Qué revisar:**
- ¿Las instrucciones son claras?
- ¿Los tiempos límite son realistas?
- ¿Las métricas se pueden capturar fácilmente?
- ¿El equipamiento funciona correctamente?

**Paso 3.2: Ajustes al protocolo (15 min)**
- Lista problemas identificados
- Propón soluciones específicas
- Actualiza documentación del protocolo
- Prepara materials finales

---

## 🧪 Fase 2: Ejecución del Testing (3 horas presenciales)

### Preparación del Laboratorio

**Equipment checklist:**
- [ ] Computadoras con navegador actualizado
- [ ] Software de screen recording (OBS, Camtasia, etc.)
- [ ] Cronómetros (físicos o digitales)
- [ ] Formularios de consentimiento impresos
- [ ] Cuestionarios SUS y NASA-TLX impresos
- [ ] Cámaras para grabar gestos y expresiones (opcional)
- [ ] Conexión a internet estable
- [ ] Ambiente silencioso y sin distracciones

**Configuración de TravelEase:**
- Prototipo desplegado y funcionando
- URLs de testing listas
- Datos de prueba preparados (si aplica)
- Backup del sistema en caso de fallos

### Protocolo de Sesión Individual

**Cada sesión dura ~30 minutos:**

**Pre-sesión (5 min)**
1. **Bienvenida y consentimiento**
   - Explicar propósito del estudio
   - Firmar formulario de consentimiento
   - Explicar think-aloud protocol
   - Iniciar grabación (si consentido)

2. **Datos demográficos breves**
   - Edad, ocupación, experiencia con viajes online
   - Frecuencia de uso de plataformas similares
   - Nivel de confort con tecnología (1-7)

**Sesión principal (20 min)**
3. **Introducción a TravelEase** (2 min)
   - "Imagina que TravelEase es una nueva plataforma..."
   - Mostrar página principal brevemente
   - "Habla en voz alta mientras navegas"

4. **Ejecución de tareas** (15 min)
   - Presentar cada tarea por escrito
   - Cronometrar tiempo por tarea
   - Anotar errores y observaciones
   - No intervenir a menos que esté completamente bloqueado

5. **Think-aloud reminders** (durante las tareas)
   - "¿Qué estás pensando ahora?"
   - "¿Qué esperabas que pasara?"
   - "¿Cómo te sientes con esto?"

**Post-sesión (5 min)**
6. **Cuestionario SUS** (2 min)
   - Completar 10 items inmediatamente

7. **Entrevista breve** (3 min)
   - "¿Qué fue lo más frustrante?"
   - "¿Qué te gustó más?"
   - "¿Usarías esta plataforma realmente?"
   - "¿Cómo se compara con Booking/Airbnb?"

### Plantillas de Registro

**Template de observación por participante:**

```
PARTICIPANTE #: ___
EDAD: ___ OCUPACIÓN: _____________ EXPERIENCIA VIAJES ONLINE: ___/7
FECHA: _______ HORA: _____ MODERADOR: _____________

TAREA 1: Búsqueda básica
□ Tiempo inicio: ___:___ Tiempo fin: ___:___ Total: ___ seg
□ ¿Completada exitosamente? Sí / No
□ Errores observados: _________________________________
□ Momentos de confusión: _____________________________
□ Citas relevantes: "________________________________"

TAREA 2: Filtrado avanzado
□ Tiempo: ___ seg □ Éxito: Sí/No □ Filtros usados: ___/6
□ Errores: ________________________________________
□ Observaciones: ___________________________________

[Continuar para todas las tareas]

POST-SESIÓN:
□ SUS Score: ___/100
□ NPS: ___/10 (¿Recomendarías TravelEase?)
□ Cita destacada: "__________________________________"
□ Principal frustración: ____________________________
□ Aspecto más valorado: ____________________________

NOTAS GENERALES:
________________________________________________
________________________________________________
```

**Template agregado por sesión:**

```
SESIÓN DE TESTING - FECHA: _______
PARTICIPANTES: ___ COMPLETADOS: ___ CANCELACIONES: ___

MÉTRICAS AGREGADAS:
□ Tasa de finalización Tarea 1: ___% (___/9)
□ Tiempo promedio Tarea 1: ___ seg (rango: ___-___)
□ Tasa de finalización Tarea 2: ___% (___/9)
□ Tiempo promedio Tarea 2: ___ seg (rango: ___-___)
[...]

SUS SCORES:
Participantes 1-3: ___, ___, ___
Participantes 4-6: ___, ___, ___
Participantes 7-9: ___, ___, ___
PROMEDIO: ___/100 MEDIANA: ___/100

OBSERVACIONES EMERGENTES:
□ Patrón de error recurrente: ________________________
□ Funcionalidad más problemática: ____________________
□ Aspecto más elogiado: _____________________________
□ Sorpresa inesperada: ______________________________
```

### Gestión de Roles Durante Testing

**Moderador principal:**
- Guía al participante
- Lee instrucciones de tareas
- Hace preguntas de think-aloud
- Mantiene neutralidad (no ayuda a resolver)

**Observador 1:**
- Cronometra todas las tareas
- Cuenta clicks/taps
- Anota errores específicos
- Registra citaciones relevantes

**Observador 2:**
- Toma notas de comportamiento no-verbal
- Anota momentos de confusión o frustración
- Prepara cuestionarios
- Gestiona aspectos técnicos (grabación, etc.)

**Rotación:** Cambiar roles cada 3 participantes para evitar fatiga.

---

## 📊 Fase 3: Análisis de Datos y Triangulación (4-6 horas)

### Actividad 1: Procesamiento de Datos Cuantitativos (90 min)

#### Paso 1.1: Consolidación de métricas (30 min)

**Crear hoja de cálculo con:**

| Participante | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | PROM | MED | SD |
|--------------|----|----|----|----|----|----|----|----|----|----|-----|----| 
| **Efectividad** | | | | | | | | | | | | |
| Tarea 1 éxito (0/1) | | | | | | | | | | | | |
| Tarea 2 éxito (0/1) | | | | | | | | | | | | |
| Tarea 3 éxito (0/1) | | | | | | | | | | | | |
| Tarea 4 éxito (0/1) | | | | | | | | | | | | |
| Tarea 5 éxito (0/1) | | | | | | | | | | | | |
| **Total efectividad** | | | | | | | | | | | | |
| **Eficiencia** | | | | | | | | | | | | |
| Tiempo Tarea 1 (seg) | | | | | | | | | | | | |
| Tiempo Tarea 2 (seg) | | | | | | | | | | | | |
| Tiempo Tarea 3 (seg) | | | | | | | | | | | | |
| Tiempo Tarea 4 (seg) | | | | | | | | | | | | |
| Clicks totales | | | | | | | | | | | | |
| **Satisfacción** | | | | | | | | | | | | |
| SUS Score | | | | | | | | | | | | |
| NPS | | | | | | | | | | | | |

#### Paso 1.2: Análisis estadístico básico (30 min)

**Calcular para cada métrica:**

**Medidas de tendencia central:**
- Media aritmética
- Mediana (importante para datos con outliers)
- Moda (para datos categóricos)

**Medidas de dispersión:**
- Desviación estándar
- Rango intercuartílico (Q3-Q1)
- Mín/Max valores

**Intervalos de confianza (95%):**
- Para SUS: Media ± 1.96 × (SD/√n)
- Para tiempos: Usar log-transformation si distribución es skewed

**Ejemplo de cálculo:**
```
SUS Scores: [72, 68, 85, 79, 65, 88, 74, 81, 69]
n = 9
Media = 75.7
SD = 8.2
IC 95% = 75.7 ± 1.96 × (8.2/3) = 75.7 ± 5.4 = [70.3, 81.1]

Interpretación: Con 95% confianza, el SUS real está entre 70.3-81.1
```

#### Paso 1.3: Comparación con benchmarks (30 min)

**Benchmarks de referencia:**

| Métrica | TravelEase | Booking.com | Airbnb | Estándar Industria | Interpretación |
|---------|------------|-------------|--------|-------------------|----------------|
| Tasa finalización búsqueda | ___% | 92% | 89% | >85% | Bueno/Regular/Malo |
| Tiempo búsqueda (seg) | ___ | 45 | 52 | <60 | Bueno/Regular/Malo |
| SUS Score | ___ | 71 | 76 | >70 | Bueno/Regular/Malo |
| NPS | ___ | +12 | +24 | >0 | Bueno/Regular/Malo |

**Análisis de gaps:**
- ¿En qué métricas TravelEase está por encima/debajo del estándar?
- ¿Cuáles son las brechas más críticas?
- ¿Qué métricas muestran mayor variabilidad entre usuarios?

### Actividad 2: Análisis Cualitativo (90 min)

#### Paso 2.1: Coding de observaciones (45 min)

**Usar técnica de análisis temático:**

1. **Lectura completa** de todas las notas de observación
2. **Codificación inicial** de incidentes/comentarios relevantes
3. **Agrupación temática** en categorías emergentes
4. **Refinamiento** y definición de temas finales

**Categorías sugeridas:**

**TEMAS POSITIVOS:**
- **Facilidad de uso:** "Es muy intuitivo", "Encontré rápido lo que buscaba"
- **Confianza:** "Me siento seguro reservando aquí", "La información es clara"
- **Eficiencia:** "Más rápido que Booking", "Pocos clicks"

**TEMAS PROBLEMÁTICOS:**
- **Confusión navegacional:** "No sé dónde estoy", "¿Cómo vuelvo atrás?"
- **Información insuficiente:** "No veo el precio total", "Faltan detalles"
- **Errores técnicos:** "No responde", "Se colgó"
- **Expectativas violadas:** "Esperaba que...", "En Airbnb es diferente"

**SUGERENCIAS:**
- **Mejoras específicas:** "Debería tener...", "Sería mejor si..."
- **Funcionalidades faltantes:** "Necesito poder...", "Me gustaría ver..."

#### Paso 2.2: Correlación cuali-cuanti (45 min)

**Análisis de triangulación:**

```
PARTICIPANTE P3: 
Métricas cuantitativas:
- Tarea 1: FALLO (timeout después 6 min)
- SUS: 52/100 (bajo)
- NPS: 4/10 (detractor)

Observaciones cualitativas:
- "No encuentro el filtro de presupuesto"
- Se frustró visiblemente en min 3
- "Es muy complicado comparado con Booking"
- Intentó usar filtros 4 veces sin éxito

INTERPRETACIÓN INTEGRADA:
El fracaso en Tarea 1 se explica por problemas de findabilidad
de filtros básicos. La baja satisfacción correlaciona con
la frustración observada. Problema de diseño confirmado
por múltiples evidencias.
```

**Para cada participante:**
- ¿Las métricas cuantitativas coinciden con observaciones cualitativas?
- ¿Hay discrepancias que requieren explicación?
- ¿Qué insights adicionales aporta cada método?

### Actividad 3: Validación Cruzada con Evaluación Heurística (60 min)

#### Paso 3.1: Mapping de problemas (30 min)

**Objetivo:** Relacionar problemas encontrados en testing con principios ISO 9241-110 evaluados en Lab 2.

**Template de mapeo:**

| Problema observado en testing | Frecuencia | Severidad | Principio ISO violado | Evaluación Lab 2 | ¿Coincidencia? |
|-------------------------------|------------|-----------|---------------------|------------------|----------------|
| Filtro presupuesto difícil de encontrar | 6/9 usuarios | Alta | 2. Autodescripción | Puntuamos 3/5 | ✅ SÍ |
| Usuarios no pueden deshacer filtros | 4/9 usuarios | Media | 5. Controlabilidad | Puntuamos 4/5 | ❌ NO |
| Tiempo búsqueda muy largo | 7/9 usuarios | Alta | 1. Adecuación a tarea | Puntuamos 4/5 | ❌ NO |

**Análisis de coincidencias:**
- **Alta coincidencia (✅):** La evaluación heurística predijo correctamente problemas reales
- **Baja coincidencia (❌):** Falsos negativos (no detectamos problemas reales) o falsos positivos (problemas que no importan a usuarios reales)

#### Paso 3.2: Actualización de evaluación heurística (30 min)

**Basándote en datos de testing, re-evalúa principios:**

```
PRINCIPIO 2: AUTODESCRIPCIÓN
Evaluación original (Lab 2): 4/5
Evidencia de testing: 67% usuarios no encontraron filtro presupuesto
Evaluación actualizada: 2/5
Justificación: Testing reveló que elementos críticos no son autodescriptivos
en contexto de uso real.

PRINCIPIO 5: CONTROLABILIDAD  
Evaluación original (Lab 2): 4/5
Evidencia de testing: Solo 44% usuarios supieron deshacer filtros
Evaluación actualizada: 3/5
Justificación: Control existe pero no es discoverable para usuarios reales.
```

### Actividad 4: Priorización de Mejoras (90 min)

#### Paso 4.1: Matriz de impacto-frecuencia (45 min)

**Para cada problema identificado:**

| Problema | Usuarios afectados | Impacto en métricas | Frecuencia | Severidad | Prioridad |
|----------|-------------------|-------------------|-----------|-----------|-----------|
| Filtro presupuesto no visible | 6/9 (67%) | -15 seg tiempo promedio, -20% éxito tarea | Alta | Crítica | **P1** |
| No puede deshacer filtros | 4/9 (44%) | +8 seg tiempo, frustración media | Media | Mayor | **P2** |
| Falta info precio total | 8/9 (89%) | -15 pts SUS, -2 pts NPS | Alta | Mayor | **P1** |
| Autocompletado lento | 3/9 (33%) | +3 seg tiempo | Baja | Menor | **P3** |

**Criterios de priorización:**
- **P1 (Crítica):** >60% usuarios + impacto alto en métricas
- **P2 (Alta):** >40% usuarios + impacto medio, o <40% usuarios + impacto alto
- **P3 (Media):** <40% usuarios + impacto medio
- **P4 (Baja):** <20% usuarios + cualquier impacto

#### Paso 4.2: Estimación de soluciones (45 min)

**Para problemas P1 y P2, diseñar soluciones:**

```
PROBLEMA P1: Filtro presupuesto no visible

SOLUCIONES POSIBLES:
A) Mover filtro presupuesto a posición prominente (top-left)
   - Esfuerzo: 2 días desarrollo
   - Impacto esperado: +25% tasa éxito, -10 seg tiempo

B) Agregar filtro presupuesto a búsqueda principal
   - Esfuerzo: 5 días desarrollo + UX redesign
   - Impacto esperado: +40% tasa éxito, -20 seg tiempo

C) Tutorial contextual para filtros
   - Esfuerzo: 3 días desarrollo
   - Impacto esperado: +15% tasa éxito (solo primeros usuarios)

RECOMENDACIÓN: Solución A (máximo ROI)
VALIDACIÓN: A/B test con 20 usuarios post-implementación
```

**ROI estimado:**
- Calcular beneficio esperado (mejora en métricas × volumen usuarios)
- Comparar con costo de implementación
- Priorizar por ROI descendente

---

## 📝 Fase 4: Reporte Final y Presentación (2-3 horas)

### Estructura del Informe Técnico

**Formato:** PDF de 4000-5000 palabras + anexos  
**Audiencia:** Stakeholders técnicos y de producto  
**Propósito:** Justificar decisiones de mejora basadas en evidencia

#### **1. Executive Summary (400 palabras)**

**Incluir obligatoriamente:**
- **Método:** "Evaluamos usabilidad de TravelEase con N=9 usuarios usando metodología ISO 9241-11"
- **Hallazgos clave:** "SUS promedio: 75.7 (IC 95%: 70.3-81.1), 78% tasa éxito tareas críticas"
- **Problemas principales:** "Identificamos 3 problemas críticos que afectan 60%+ de usuarios"
- **Recomendaciones:** "5 mejoras priorizadas con ROI estimado de 15-40% mejora en métricas"
- **Próximos pasos:** "Validación A/B recomendada para confirmar impacto de mejoras"

#### **2. Metodología (800 palabras)**

**2.1 Diseño del estudio**
- Marco teórico ISO 9241-11 aplicado
- Preguntas de investigación específicas
- Variables operacionalizadas y métodos de medición

**2.2 Participantes**
- Criterios de selección y proceso de reclutamiento
- Demografía de muestra (tabla + descripción)
- Representatividad respecto a personas del Lab 1

**2.3 Procedimiento**
- Protocolo de sesión detallado
- Instrumentos de medición utilizados
- Control de variables confounding

**2.4 Análisis de datos**
- Técnicas estadísticas para datos cuantitativos
- Método de codificación para datos cualitativos
- Criterios de triangulación metodológica

#### **3. Resultados (1200 palabras)**

**3.1 Métricas de usabilidad ISO 9241-11**

**Efectividad**
```
Tarea de búsqueda básica: 78% éxito (7/9 usuarios)
IC 95%: [40.0%, 97.2%] - estadísticamente inferior a benchmark 
industria (85%, p<0.05, test exacto Fisher)

Principales causas de fallo:
- Filtro presupuesto no encontrado (4/9 intentos fallidos)
- Timeout por confusión navegacional (2/9 casos)
```

**Eficiencia**
```
Tiempo promedio búsqueda: 89.3 seg (SD=21.4)
IC 95%: [73.8, 104.8] - dentro de estándar industria (<120 seg)

Distribución:
- Usuarios exitosos: Media=76.2 seg 
- Usuarios fallidos: Media=180+ seg (timeout)
- Correlación negativa tiempo-éxito: r=-0.67, p<0.05
```

**Satisfacción**
```
SUS Score: 75.7/100 (SD=8.2)
IC 95%: [70.3, 81.1] - por encima de promedio industria (68)

NPS: +11 (6 promotores, 2 neutros, 1 detractor)
Correlación SUS-NPS: r=0.84, p<0.01
```

**Tablas y gráficos obligatorios:**
- Tabla resumen todas las métricas con IC 95%
- Box plot distribución SUS scores vs. benchmarks
- Scatter plot tiempo vs. éxito por tarea
- Heatmap de problemas por principio ISO 9241-110

**3.2 Análisis cualitativo**

**Temas emergentes (con frecuencia):**
- Confusión navegacional: 67% participantes (6/9)
- Expectativas violadas: 44% participantes (4/9)  
- Información insuficiente: 89% participantes (8/9)

**Citas representativas:**
```
"No entiendo dónde está el filtro de precio total, solo veo 
precio por noche" - P3, representa tema de información insuficiente

"Esperaba que funcionara como Booking, pero es confuso" 
- P7, representa tema de expectativas violadas
```

**3.3 Validación cruzada metodológica**

**Convergencia entre métodos:**
- Testing confirmó 80% de problemas identificados en evaluación heurística
- Evaluación heurística perdió 20% de problemas reales (falsos negativos)
- Testing reveló 3 problemas no anticipados por evaluación heurística

**Discrepancias importantes:**
```
Principio "Conformidad con expectativas": 
- Evaluación heurística: 4/5 (bien)
- Testing: 44% usuarios confundidos por navegación
- Conclusión: Evaluación subestimó impacto de diferencias con competencia
```

#### **4. Recomendaciones Priorizadas (1000 palabras)**

**Para cada recomendación P1 y P2:**

**RECOMENDACIÓN #1: Rediseño de filtros de presupuesto**

**Problema validado:**
- 67% usuarios no encuentran filtro presupuesto
- -15 segundos tiempo promedio
- -20% tasa de éxito en búsqueda

**Solución propuesta:**
- Mover filtro presupuesto a sidebar prominente
- Agregar filtro "presupuesto total" además de "por noche"
- Implementar slider visual con rangos sugeridos

**Evidencia de soporte:**
- Principio ISO 9241-110 #2 (Autodescripción) violado
- Benchmarking: Skyscanner muestra presupuesto prominentemente
- 6/9 usuarios pidieron explícitamente esta funcionalidad

**Impacto esperado:**
- +25% tasa de éxito en búsqueda (estimado)
- -10 segundos tiempo promedio
- +8 puntos SUS (extrapolado de correlaciones)

**Esfuerzo de implementación:** 
- 2 días desarrollo frontend
- 1 día testing QA
- Riesgo bajo (cambio cosmético)

**Métrica de validación:**
- A/B test con 40 usuarios post-implementación
- Meta: >90% tasa de éxito en búsqueda

#### **5. Limitaciones y Trabajo Futuro (300 palabras)**

**Limitaciones metodológicas:**
- Muestra pequeña (n=9) limita generalización estadística
- Sesgo de selección: principalmente estudiantes universitarios
- Contexto de laboratorio vs. uso real en contexto natural
- Prototipo vs. sistema completo funcional

**Limitaciones técnicas:**
- Evaluación limitada a flujo de búsqueda (no reserva completa)
- No se evaluó performance en diferentes dispositivos
- No se consideraron usuarios con discapacidades

**Próximos estudios recomendados:**
- Estudio longitudinal con usuarios reales (2-3 semanas uso)
- Evaluación con muestra más diversa (edad, tecnología, geografía)
- Testing en contexto natural (usuarios en casa/oficina)
- Evaluación de accesibilidad siguiendo WCAG 2.1

#### **6. Conclusiones (300 palabras)**

**Síntesis de hallazgos:**
- TravelEase alcanza estándares mínimos de usabilidad pero requiere mejoras específicas
- Metodología ISO 9241-11 efectiva para identificar problemas objetivos
- Triangulación metodológica esencial para validación robusta

**Implicaciones para diseño:**
- Principios ISO 9241-110 son necesarios pero no suficientes
- Testing con usuarios reales revela problemas no anticipados
- Benchmarking competitivo crucial para calibrar expectativas

**Valor del proceso:**
- Evidencia cuantificada justifica inversión en mejoras de UX
- Metodología replicable para evaluaciones futuras
- Base sólida para decisiones de producto data-driven

---

### Anexos

**Anexo A:** Protocolo completo de testing  
**Anexo B:** Datos cuantitativos completos (Excel)  
**Anexo C:** Transcripciones relevantes de sessions  
**Anexo D:** Capturas de pantalla de problemas identificados  
**Anexo E:** Cuestionarios utilizados (SUS, demográfico)

---

## ✅ Criterios de Evaluación

| Criterio | Peso | Indicadores de calidad |
|----------|------|-----------------------|
| **Rigor metodológico** | 25% | Aplicación correcta ISO 9241-11, tamaño muestra justificado, protocolo detallado |
| **Calidad de datos** | 20% | Métricas completas, análisis estadístico apropiado, evidencias cualitativas ricas |
| **Triangulación** | 20% | Validación cruzada efectiva, convergencia/divergencia explicada |
| **Recomendaciones** | 20% | Priorizadas por evidencia, específicas y accionables, ROI estimado |
| **Comunicación** | 15% | Reporte claro y profesional, gráficos informativos, presentación efectiva |

**Escala:**
- **Excelente (90-100):** Estudio de calidad profesional, insights valiosos, metodología impecable
- **Muy bueno (80-89):** Estudio sólido con hallazgos útiles, metodología correcta
- **Bueno (70-79):** Estudio básico pero completo, cumple objetivos mínimos
- **Insuficiente (<70):** Metodología deficiente, datos incompletos, conclusiones no soportadas

---

## 💡 Tips para el Éxito

### Durante la Preparación
✅ **Pilot test es crítico:** Una sesión mal diseñada arruina todo el estudio  
✅ **Recluta participantes diversos:** No solo estudiantes de tu edad/carrera  
✅ **Prepara contingencias:** ¿Qué haces si un participante no aparece?  

### Durante el Testing
✅ **Mantén neutralidad:** Tu trabajo es observar, no ayudar al usuario  
✅ **Graba todo:** Memoria es falible, videos y audios son evidencia objetiva  
✅ **Toma notas inmediatas:** Escribe observaciones entre sesiones  

### Durante el Análisis
✅ **Busca patrones, no anécdotas:** Un usuario frustrando ≠ problema real  
✅ **Cuantifica todo lo posible:** "Varios usuarios" ≠ "67% de usuarios"  
✅ **Triangula siempre:** Un método solo = conclusiones débiles  

### Para el Reporte
✅ **Sé específico en recomendaciones:** "Mejorar usabilidad" ≠ "Mover filtro presupuesto a posición prominente"  
✅ **Incluye intervalos de confianza:** Demuestra rigor estadístico  
✅ **Usa visualizaciones informativas:** Gráficos comunican mejor que tablas  

---

**¡Éxito en tu estudio de usabilidad!** 🚀

*Recuerda: Un buen estudio de usabilidad puede influir decisiones de producto por años. La inversión en metodología rigurosa vale la pena.*
````