# Rúbrica de Evaluación - Laboratorio 2: Principios de Diálogo

## 📊 Distribución General de la Calificación

| Componente | Peso | Puntos | Requisito Mínimo |
|------------|------|--------|------------------|
| **Informe de Lectura Previa** | 10% | 1.0 | Entregar 24h antes |
| **Participación en Sesión Presencial** | 15% | 1.5 | Asistencia obligatoria |
| **Informe Técnico Final** | 75% | 7.5 | Mínimo 5.0/10 para aprobar |
| **TOTAL** | **100%** | **10.0** | **5.0 puntos** |

---

## 📝 PARTE 1: Informe de Lectura Previa (10% = 1.0 punto)

**Entrega:** 24 horas antes de la sesión presencial  
**Formato:** PDF, 2.5-3 páginas  
**Peso:** 1.0 punto (10% de la nota final)

### Criterios de Evaluación

| Criterio | Excelente (1.0-0.9) | Muy Bueno (0.89-0.75) | Bueno (0.74-0.6) | Insuficiente (<0.6) |
|----------|---------------------|----------------------|------------------|---------------------|
| **Resumen de los 7 principios** (0.5 pts) | Explica los 7 principios con precisión, ejemplos concretos y conexión con usabilidad | Explica los 7 principios correctamente con ejemplos básicos | Explica 5-6 principios o con imprecisiones menores | Explica <5 principios o con errores conceptuales |
| **Análisis comparativo de plataformas** (0.3 pts) | Tabla completa (3 plataformas × 7 principios) con ejemplos específicos y screenshots | Tabla completa pero ejemplos genéricos | Tabla incompleta (falta 1 plataforma o 2-3 principios) | Tabla muy incompleta o sin ejemplos |
| **Preguntas para clase** (0.2 pts) | 3-5 preguntas reflexivas que demuestran pensamiento crítico | 3 preguntas relevantes | 1-2 preguntas básicas | No incluye preguntas o son triviales |

**Penalizaciones:**
- Entrega tarde (1-12h): -10%
- Entrega tarde (12-24h): -25%
- Entrega tarde (>24h): No se acepta
- Formato incorrecto (>3.5 páginas o <2 páginas): -0.1 pts
- No aprobó quiz (70%): -0.3 pts

---

## 👥 PARTE 2: Participación en Sesión Presencial (15% = 1.5 puntos)

**Evaluación:** Observación del docente durante las 2 horas  
**Peso:** 1.5 puntos (15% de la nota final)

### Criterios de Evaluación

| Criterio | Puntos | Excelente | Muy Bueno | Bueno | Insuficiente |
|----------|--------|-----------|-----------|-------|--------------|
| **Asistencia y puntualidad** | 0.3 | Presente desde inicio | Llega <10 min tarde | Llega 10-20 min tarde | Llega >20 min tarde o ausente |
| **Preparación** (trae informe Lab 1, materiales) | 0.3 | Trae TODO (Lab 1, laptop, acceso IA) | Falta 1 elemento (usa del compañero) | Falta 2 elementos | No trae Lab 1 (no puede trabajar) |
| **Contribución al equipo** | 0.5 | Lidera análisis, propone ideas, ayuda a compañeros | Participa activamente en discusiones | Participa solo cuando se le pregunta | No participa o distrae |
| **Cumplimiento de rol asignado** | 0.4 | Ejecuta su rol (Analista ISO / Ing. Prompts / Sintetizador) excelentemente | Ejecuta rol correctamente | Ejecuta rol de forma básica | No ejecuta su rol |

**Evidencias de participación:**
- ✅ Matriz de requisitos completa (Actividad 1.2)
- ✅ Al menos 2 diseños generados (Actividad 2.2)
- ✅ Matriz de evaluación de diseños (Actividad 3.1)
- ✅ Plan de mejoras documentado (Actividad 3.3)

**Penalizaciones:**
- Ausencia sin justificación: 0.0 puntos (y no puede entregar informe final)
- Uso de dispositivos para fines no relacionados (redes sociales): -0.3 pts
- Comportamiento disruptivo (distrae a otros equipos): -0.5 pts

---

## 📄 PARTE 3: Informe Técnico Final (75% = 7.5 puntos)

**Entrega:** [Fecha definida por docente, típicamente 1 semana post-sesión]  
**Formato:** PDF, 10-14 páginas (sin anexos)  
**Peso:** 7.5 puntos (75% de la nota final)

---

### Criterio A: Análisis de Requisitos por Principio (20% = 1.5 puntos)

**Qué se evalúa:**
- Matriz de requisitos (7 principios × 3 personas)
- Identificación de conflictos entre principios
- Propuesta de soluciones a conflictos

#### Niveles de Desempeño

**⭐⭐⭐⭐⭐ EXCELENTE (1.5-1.35 pts) - Nota 9.0-10.0**

✅ **Matriz completa y específica:**
- 7 principios × 3 personas = 21 celdas TODAS completas
- Requisitos ESPECÍFICOS (no genéricos)
  - ❌ Malo: "Laura necesita interfaz simple"
  - ✅ Bueno: "Laura necesita filtro 'Presupuesto total' con slider €0-€5000 visible en los 5 filtros básicos, porque busca viajes completos baratos"
- Interpretación correcta de cada principio para TravelEase
- Requisitos alineados con necesidades de personas del Lab 1

✅ **Conflictos identificados con profundidad:**
- Identifica mínimo 3 conflictos entre principios
- Ejemplo excelente:
  ```
  CONFLICTO: Principio 1 (Adecuación a tarea) vs. Principio 4 (Adecuación a aprendizaje)
  
  Descripción: Laura (experta, viaja 3-4 veces/año) necesita acceso rápido a 15 
  filtros avanzados para búsquedas precisas (ej: "solo experiencias grupos <10 personas", 
  "verificado por locales"). Sin embargo, Turista Senior (novato, primer viaje en app) 
  se confunde con más de 5 opciones visibles simultáneamente.
  
  Evidencia del Lab 1: 
  - Laura: Tech-savvy ⭐⭐⭐⭐⭐, usa apps viajes frecuentemente
  - Senior: Tech-savvy ⭐⭐☆☆☆, primera app de viajes
  
  Trade-off: Mostrar muchos filtros (eficiencia para Laura) vs. mostrar pocos 
  (simplicidad para Senior). No se pueden satisfacer ambas necesidades simultáneamente 
  con misma interfaz.
  ```

✅ **Soluciones creativas y bien justificadas:**
- Propone solución concreta a cada conflicto
- Justifica POR QUÉ esa solución balancea ambos principios
- Ejemplo:
  ```
  SOLUCIÓN: Progressive disclosure con adaptación contextual
  
  Implementación:
  1. Vista por defecto: 5 filtros básicos visibles (Principio 4: fácil aprender)
  2. Botón "Más filtros" expande 10 adicionales (Principio 1: eficiencia para expertos)
  3. Sistema recuerda: Si usuario usa filtros avanzados 3+ veces → Los muestra por 
     defecto en próximas visitas (Principio 7: Individualización)
  
  Justificación: 
  - Novatos NUNCA ven interfaz compleja (no están obligados a expandir)
  - Expertos acceden a opciones avanzadas en 1 clic (eficiente)
  - Sistema aprende y adapta (mejor de ambos mundos)
  - Cumple Principios 1, 4 y 7 simultáneamente
  ```

---

**⭐⭐⭐⭐☆ MUY BUENO (1.34-1.2 pts) - Nota 8.0-8.9**

- Matriz completa pero algunos requisitos son genéricos
- Identifica 2-3 conflictos con descripción clara
- Soluciones correctas pero justificación básica
- Falta profundidad en evidencia del Lab 1

---

**⭐⭐⭐☆☆ BUENO (1.19-0.9 pts) - Nota 6.0-7.9**

- Matriz mayormente completa (1-3 celdas vacías)
- Requisitos mezclados (algunos específicos, otros genéricos)
- Identifica 1-2 conflictos
- Soluciones propuestas sin justificación profunda
- Poca conexión con Lab 1

---

**⭐☆☆☆☆ INSUFICIENTE (<0.9 pts) - Nota <6.0**

- Matriz incompleta (>4 celdas vacías)
- Requisitos muy genéricos o incorrectos
- No identifica conflictos o son triviales
- Sin soluciones o soluciones incorrectas
- No usa información del Lab 1

---

### Criterio B: Calidad de Alternativas de Diseño (25% = 1.875 pts)

**Qué se evalúa:**
- Mínimo 2 alternativas de diseño generadas
- Uso efectivo de IA generativa
- Documentación del proceso iterativo
- Diseños visualmente claros (screenshots/código)

#### Niveles de Desempeño

**⭐⭐⭐⭐⭐ EXCELENTE (1.875-1.69 pts) - Nota 9.0-10.0**

✅ **3+ alternativas distintas y bien definidas:**
- Diseño A: Enfoque minimalista (para novatos)
- Diseño B: Enfoque power user (para expertos)
- Diseño C: Híbrido (balance)
- Cada uno tiene identidad clara y propósito diferente

✅ **Uso avanzado de IA generativa:**
- Prompts específicos (incluidos en Anexo B)
- 3-4 iteraciones documentadas por diseño
- Ejemplo de iteración documentada:
  ```
  Diseño A - Iteración 1 (Prompt genérico):
  [Screenshot]
  Problemas detectados:
  - No tiene tooltips (viola Principio 2)
  - Demasiados filtros visibles (no es minimalista)
  
  Diseño A - Iteración 2 (Prompt mejorado):
  Ajustes solicitados a la IA:
  - "Reduce filtros visibles a 5 máximo"
  - "Agrega tooltip en cada icono con explicación"
  [Screenshot]
  Mejoras: Ahora cumple Principio 2, más simple
  
  Diseño A - Iteración 3 (Refinamiento):
  Ajustes: "Aumenta tamaño de tipografía a 16px mínimo (móvil)"
  [Screenshot]
  FINAL: Cumple objetivos de diseño minimalista
  ```

✅ **Calidad visual profesional:**
- Screenshots claros y legibles
- Diseños se ven coherentes (paleta de colores, tipografía)
- Responsive (desktop + móvil mostrados)
- Código generado funcional (si aplica)

✅ **Diferenciación clara entre alternativas:**
- Tabla comparativa de características
  | Característica | Diseño A | Diseño B | Diseño C |
  |----------------|----------|----------|----------|
  | Filtros visibles | 5 | 15 | 7 + expandir |
  | Target | Novatos | Expertos | Todos |
  | Complejidad | Baja | Alta | Media |

---

**⭐⭐⭐⭐☆ MUY BUENO (1.68-1.5 pts) - Nota 8.0-8.9**

- 2-3 alternativas claras
- 2-3 iteraciones documentadas
- Prompts incluidos pero básicos
- Screenshots claros
- Diferencias entre alternativas evidentes

---

**⭐⭐⭐☆☆ BUENO (1.49-1.13 pts) - Nota 6.0-7.9**

- 2 alternativas
- 1-2 iteraciones mencionadas (poco detalle)
- Screenshots de calidad media
- Diferencias entre alternativas no muy claras
- Prompts no incluidos o muy genéricos

---

**⭐☆☆☆☆ INSUFICIENTE (<1.13 pts) - Nota <6.0**

- 1 alternativa o alternativas muy similares
- Sin iteraciones documentadas
- Screenshots de baja calidad o faltantes
- No se evidencia uso de IA o uso inadecuado

---

### Criterio C: Evaluación de Diseños según Principios ISO (20% = 1.5 pts)

**Qué se evalúa:**
- Matriz de evaluación completa (7 principios × 2-3 diseños)
- Puntuación objetiva y justificada
- Evidencia concreta en los diseños

#### Niveles de Desempeño

**⭐⭐⭐⭐⭐ EXCELENTE (1.5-1.35 pts) - Nota 9.0-10.0**

✅ **Matriz completa y detallada:**

| Principio | Diseño A | Diseño B | Diseño C |
|-----------|----------|----------|----------|
| 1. Adecuación tarea | ⭐⭐⭐☆☆ (3/5)<br>**Cumple:** Filtro presupuesto total visible<br>**No cumple:** Pide email antes de ver resultados (innecesario)<br>**Evidencia:** [Screenshot línea 45]<br>**Mejora:** Quitar campo email del formulario inicial | ⭐⭐⭐⭐⭐ (5/5)<br>**Cumple:** Filtros muy completos, búsqueda rápida<br>**Evidencia:** [Screenshot]<br>Permite a Laura buscar con 15 filtros simultáneos | ⭐⭐⭐⭐☆ (4/5)<br>**Cumple:** 5 filtros básicos + "Más filtros"<br>**No cumple:** Botón "Más filtros" podría ser más visible<br>**Evidencia:** [Screenshot] |
| 2. Autodescripción | ... | ... | ... |
| **TOTAL** | **23/35** | **31/35** | **28/35** |

✅ **Justificaciones OBJETIVAS (no subjetivas):**
- ❌ Subjetivo: "Es bastante autodescriptivo" (vago)
- ✅ Objetivo: "Cumple Principio 2: Todos los iconos tienen tooltip explicativo (ver screenshot), placeholder dice 'ej: París', contador muestra '234 experiencias'"

✅ **Evidencia visual señalada:**
- Screenshots con flechas/anotaciones señalando elementos específicos
- Referencias a líneas de código (si generó código)

✅ **Puntuaciones coherentes:**
- Mismo criterio aplicado a todos los diseños
- Diferencias de puntuación justificadas

---

**⭐⭐⭐⭐☆ MUY BUENO (1.34-1.2 pts) - Nota 8.0-8.9**

- Matriz completa con justificaciones claras
- Evidencia visual presente
- Algunas justificaciones son subjetivas
- Puntuaciones mayormente coherentes

---

**⭐⭐⭐☆☆ BUENO (1.19-0.9 pts) - Nota 6.0-7.9**

- Matriz completa pero justificaciones breves
- Poca evidencia visual
- Justificaciones genéricas
- Puntuaciones inconsistentes

---

**⭐☆☆☆☆ INSUFICIENTE (<0.9 pts) - Nota <6.0**

- Matriz incompleta
- Sin justificaciones o incorrectas
- Sin evidencia visual
- Puntuaciones arbitrarias

---

### Criterio D: Diseño Final Refinado (20% = 1.5 pts)

**Qué se evalúa:**
- Diseño final cumple mínimo 28/35 puntos ISO (80%)
- Decisiones de diseño justificadas
- Mejoras implementadas del plan (Actividad 3.3)
- Responsive design (móvil + desktop)

#### Niveles de Desempeño

**⭐⭐⭐⭐⭐ EXCELENTE (1.5-1.35 pts) - Nota 9.0-10.0**

✅ **Cumplimiento ISO 32-35/35 (91-100%):**
- 6-7 principios con ⭐⭐⭐⭐⭐ (5/5)
- 0-1 principios con ⭐⭐⭐⭐☆ (4/5)

✅ **Decisiones de diseño documentadas y justificadas:**
- Mínimo 5 decisiones críticas explicadas
- Ejemplo de documentación excelente:
  ```
  DECISIÓN #1: Progressive Disclosure para Filtros
  
  Problema: Conflicto entre Principio 1 (Laura necesita 15 filtros) y Principio 4 
  (Senior se confunde con >5 opciones).
  
  Alternativas consideradas:
  A) Todos los filtros siempre visibles → Intimida novatos (viola Principio 4)
  B) Modo básico/avanzado separados → Usuario debe elegir (fricción)
  C) Progressive disclosure: 5 básicos + botón "Más filtros" → ELEGIDA
  
  Justificación: 
  - Opción C cumple AMBOS principios sin forzar decisión al usuario
  - Novatos ven interfaz simple (5 filtros), aprenden fácilmente
  - Expertos expanden con 1 clic, acceso eficiente
  - Cumple Principios 1 (tarea), 4 (aprendizaje) y 5 (control)
  
  Implementación: [Screenshot mostrando 5 filtros + botón "Más filtros"]
  
  Validación: En evaluación ISO, Diseño C obtuvo 4/5 en Principio 1 y 5/5 
  en Principio 4 (mejor balance que alternativas A y B).
  ```

✅ **Plan de mejoras implementado:**
- 5-7 mejoras del plan (Actividad 3.3) aplicadas
- Tabla de seguimiento:
  | Mejora | Prioridad | Estado | Evidencia |
  |--------|-----------|--------|-----------|
  | Tooltip en "Ordenar por" | Alta | ✅ Implementada | [Screenshot línea 120] |
  | Validación fechas | Alta | ✅ Implementada | [Screenshot código] |
  | ... | ... | ... | ... |

✅ **Responsive design completo:**
- Screenshots de 3 tamaños (desktop >1024px, tablet 768-1024px, móvil <768px)
- Adaptaciones documentadas:
  - Móvil: Filtros en modal, resultados lista vertical
  - Tablet: Filtros colapsables, grid 2 columnas
  - Desktop: Filtros sidebar, grid 3 columnas

---

**⭐⭐⭐⭐☆ MUY BUENO (1.34-1.2 pts) - Nota 8.0-8.9**

- Cumplimiento ISO 28-31/35 (80-89%)
- 3-4 decisiones justificadas
- Plan de mejoras: 4-5 implementadas
- Responsive: 2 tamaños mostrados

---

**⭐⭐⭐☆☆ BUENO (1.19-0.9 pts) - Nota 6.0-7.9**

- Cumplimiento ISO 24-27/35 (69-79%)
- 2-3 decisiones justificadas (básicamente)
- Plan de mejoras: 2-3 implementadas
- Responsive: Solo desktop o móvil

---

**⭐☆☆☆☆ INSUFICIENTE (<0.9 pts) - Nota <6.0**

- Cumplimiento ISO <24/35 (<69%)
- Decisiones no justificadas
- Plan de mejoras no implementado
- Sin responsive

---

### Criterio E: Reflexión y Aprendizajes (10% = 0.75 pts)

**Qué se evalúa:**
- Identificación de desafíos enfrentados
- Aprendizajes sobre ISO 9241-110
- Conexión con Lab 1
- Pensamiento crítico sobre estándares

#### Niveles de Desempeño

**⭐⭐⭐⭐⭐ EXCELENTE (0.75-0.68 pts) - Nota 9.0-10.0**

✅ **Reflexión profunda y personal:**
- 3+ desafíos identificados con soluciones
- Aprendizajes concretos (no genéricos)
- Ejemplo:
  ```
  DESAFÍO #2: IA generó diseños muy genéricos inicialmente
  
  Descripción: En primera iteración, v0.dev generó interfaz que parecía cualquier 
  buscador genérico. No reflejaba necesidades de Laura (presupuesto total, 
  experiencias auténticas) ni de Familia (servicios infantiles visibles).
  
  Cómo lo resolvimos: 
  1. Identificamos que nuestro prompt inicial era vago ("diseña búsqueda turística")
  2. Reescribimos prompt con requisitos ESPECÍFICOS de cada principio ISO
  3. Incluimos ejemplos concretos de personas del Lab 1
  4. Iteramos 3 veces con ajustes incrementales
  
  Aprendizaje: "Calidad del prompt = calidad del resultado". La IA es herramienta 
  poderosa SOLO si le das input específico. No reemplaza pensamiento crítico, 
  sino que ejecuta tu visión. Aprendimos a ser mucho más específicos en prompts 
  (de "agrega filtros" a "agrega filtro 'Presupuesto total €0-€5000' visible en 
  sidebar izquierdo con tooltip explicando 'Incluye alojamiento + transporte + 
  actividades'").
  
  Aplicación futura: En proyectos reales, dedicaremos más tiempo a definir 
  requisitos ANTES de usar IA. La fase de análisis (Actividad 1.2) fue crítica.
  ```

✅ **Conexión sólida con Lab 1:**
- Menciona específicamente cómo usaron personas del Lab 1
- Identifica qué validaron o corregiríandel Lab 1
- Ejemplo: "Laura necesitaba también filtro de 'Experiencias verificadas por locales' que no habíamos identificado en Lab 1. Su frustración con opciones turísticas era más profunda de lo analizado."

✅ **Pensamiento crítico sobre estándares:**
- Reflexión sobre valor de ISO 9241-110 en práctica
- Limitaciones identificadas
- Ejemplo: "ISO 9241-110 es excelente GUÍA pero no RECETA. Algunos principios entran en conflicto inevitable (Adecuación a tarea vs. Aprendizaje) y el estándar no da respuesta única. El diseñador debe JUSTIFICAR trade-offs, no solo seguir checklist."

---

**⭐⭐⭐⭐☆ MUY BUENO (0.67-0.6 pts) - Nota 8.0-8.9**

- 2-3 desafíos con soluciones
- Aprendizajes claros
- Conexión con Lab 1 presente
- Reflexión sobre estándares básica

---

**⭐⭐⭐☆☆ BUENO (0.59-0.45 pts) - Nota 6.0-7.9**

- 1-2 desafíos mencionados
- Aprendizajes genéricos
- Poca conexión con Lab 1
- Reflexión superficial

---

**⭐☆☆☆☆ INSUFICIENTE (<0.45 pts) - Nota <6.0**

- Sin desafíos identificados
- Sin aprendizajes o muy vagos
- No conecta con Lab 1
- Sin reflexión crítica

---

### Criterio F: Formato y Presentación (5% = 0.375 pts)

**Qué se evalúa:**
- Estructura del informe (secciones 1-9)
- Calidad de escritura
- Referencias APA
- Screenshots legibles

#### Niveles de Desempeño

**⭐⭐⭐⭐⭐ EXCELENTE (0.375-0.34 pts)**

- ✅ 10-14 páginas (sin anexos)
- ✅ 9 secciones completas (estructura del material_estudiante.md)
- ✅ Índice de contenidos
- ✅ Screenshots claros, numerados, referenciados en texto
- ✅ Tablas numeradas (Tabla 1, Tabla 2...)
- ✅ Sin errores ortográficos/gramaticales
- ✅ Referencias en formato APA 7ª ed.
- ✅ Portada profesional
- ✅ Anexos organizados (Prompts, código, screenshots adicionales)

**⭐⭐⭐⭐☆ MUY BUENO (0.33-0.3 pts)**

- 10-14 páginas
- 9 secciones presentes
- Screenshots claros
- 1-3 errores ortográficos menores
- Referencias en APA (con errores menores)

**⭐⭐⭐☆☆ BUENO (0.29-0.23 pts)**

- 9-15 páginas (fuera de rango ideal)
- 7-8 secciones
- Screenshots de calidad media
- 4-6 errores ortográficos
- Referencias presentes pero formato inconsistente

**⭐☆☆☆☆ INSUFICIENTE (<0.23 pts)**

- <9 o >15 páginas
- <7 secciones
- Screenshots ilegibles
- Muchos errores ortográficos
- Sin referencias o formato incorrecto

---

## 🎯 Ejemplo de Cálculo de Nota Final

### Estudiante: Equipo "TravelDesign"

**PARTE 1: Informe de Lectura Previa (10%)**
- Resumen principios: 0.45/0.5 (muy bien explicados)
- Análisis comparativo: 0.25/0.3 (tabla completa, ejemplos básicos)
- Preguntas: 0.2/0.2 (excelentes preguntas reflexivas)
- **Subtotal:** 0.9/1.0

**PARTE 2: Participación Sesión (15%)**
- Asistencia: 0.3/0.3
- Preparación: 0.3/0.3 (trajeron todo)
- Contribución: 0.45/0.5 (muy activos, buenas ideas)
- Rol: 0.35/0.4 (cumplieron rol bien)
- **Subtotal:** 1.4/1.5

**PARTE 3: Informe Técnico Final (75%)**

| Criterio | Puntos obtenidos | Puntos máximos | Justificación |
|----------|------------------|----------------|---------------|
| A: Análisis de requisitos | 1.45 | 1.5 | Matriz completa, 3 conflictos identificados, soluciones creativas |
| B: Calidad de diseños | 1.7 | 1.875 | 3 alternativas, 3 iteraciones documentadas, screenshots excelentes |
| C: Evaluación ISO | 1.35 | 1.5 | Matriz detallada, justificaciones objetivas, evidencia visual |
| D: Diseño final | 1.4 | 1.5 | Cumple 32/35 ISO, decisiones justificadas, responsive completo |
| E: Reflexión | 0.7 | 0.75 | Reflexión profunda, conecta con Lab 1, pensamiento crítico |
| F: Formato | 0.35 | 0.375 | 12 páginas, estructura perfecta, 2 errores ortográficos menores |
| **Subtotal Informe:** | **6.95** | **7.5** | |

**NOTA FINAL:**
- Lectura previa: 0.9
- Participación: 1.4
- Informe final: 6.95
- **TOTAL: 9.25 / 10.0** ✅ **EXCELENTE**

---

## ⚠️ Penalizaciones Adicionales

### Entrega Tarde (Informe Final)

| Retraso | Penalización |
|---------|--------------|
| 1-12 horas | -10% (máx nota 9.0) |
| 12-24 horas | -25% (máx nota 7.5) |
| 24-48 horas | -50% (máx nota 5.0) |
| >48 horas | No se acepta (0.0) |

### Plagio y Uso Inadecuado de IA

| Infracción | Penalización |
|------------|--------------|
| Copiar diseño de otro equipo sin citar | -50% del criterio B |
| Copiar análisis de otro equipo | -100% del criterio A (0.0) |
| No documentar uso de IA (prompts, iteraciones) | -20% del criterio B |
| Usar IA para escribir reflexión (sin pensar críticamente) | -50% del criterio E |
| Plagio de fuentes externas sin citar | 0.0 en TODO el informe + reporte académico |

**Nota:** Usar IA para GENERAR DISEÑOS es **OBLIGATORIO** y esperado. Usar IA para ESCRIBIR el informe sin pensamiento crítico es **INACEPTABLE**.

### Otros

| Infracción | Penalización |
|------------|--------------|
| No incluir informe del Lab 1 en sesión presencial | No puede hacer Lab 2 (0.0) |
| Formato incorrecto (no PDF, >15 páginas) | -0.5 puntos |
| Sin anexos (prompts, código) | -0.3 puntos |
| Screenshots ilegibles | -0.2 puntos por cada una |

---

## ✅ Checklist de Auto-Evaluación Pre-Entrega

Antes de entregar, verifica que cumples:

### Contenido (Criterios A-E)

- [ ] **Matriz de requisitos completa** (7 principios × 3 personas = 21 celdas)
- [ ] **Requisitos ESPECÍFICOS** (no "Laura necesita interfaz simple")
- [ ] **Mínimo 3 conflictos** entre principios identificados
- [ ] **Soluciones justificadas** a conflictos
- [ ] **Mínimo 2 alternativas de diseño** (idealmente 3)
- [ ] **3+ iteraciones documentadas** (screenshots antes/después)
- [ ] **Prompts incluidos** en Anexo B
- [ ] **Matriz de evaluación ISO completa** (7 principios × 2-3 diseños)
- [ ] **Justificaciones OBJETIVAS** con evidencia visual
- [ ] **Diseño final cumple mínimo 28/35 ISO** (80%)
- [ ] **5+ decisiones de diseño documentadas** con justificación
- [ ] **Plan de mejoras implementado** (mínimo 4-5 mejoras)
- [ ] **Responsive design** (desktop + móvil mostrados)
- [ ] **3+ desafíos identificados** con soluciones
- [ ] **Conexión clara con Lab 1** (uso de personas)
- [ ] **Reflexión crítica** sobre ISO 9241-110

### Formato (Criterio F)

- [ ] **10-14 páginas** (sin anexos)
- [ ] **9 secciones completas** (Introducción, Marco teórico, Análisis, Alternativas, Comparación, Final, Reflexión, Conclusiones, Referencias)
- [ ] **Portada profesional** (título, integrantes, fecha)
- [ ] **Índice de contenidos**
- [ ] **Screenshots claros y numerados**
- [ ] **Tablas numeradas** (Tabla 1, Tabla 2...)
- [ ] **Referencias en APA 7ª ed.**
- [ ] **Sin errores ortográficos** (revisar con corrector)
- [ ] **Anexos organizados** (A: Matriz, B: Prompts, C: Código, D: Screenshots)
- [ ] **Formato PDF** (no Word, no Google Docs link)

### Integridad Académica

- [ ] **Trabajo es original del equipo**
- [ ] **Citas correctas** si usamos ideas de fuentes externas
- [ ] **Uso de IA documentado** (prompts incluidos)
- [ ] **Reflexión escrita por nosotros** (no por IA)
- [ ] **Diseños son propios** (no copiados de otros equipos)

---

## 📊 Distribución Esperada de Notas

Basado en experiencia previa:

| Rango | Calificación | % Esperado | Descripción |
|-------|--------------|------------|-------------|
| 9.0-10.0 | Excelente | 15-25% | Cumple TODOS los criterios de nivel excelente |
| 8.0-8.9 | Muy Bueno | 30-40% | Cumple mayoría de criterios, algunas mejoras menores |
| 6.0-7.9 | Bueno | 30-35% | Cumple requisitos básicos, falta profundidad |
| 5.0-5.9 | Suficiente | 5-10% | Cumple mínimo, muchas deficiencias |
| <5.0 | Insuficiente | 0-5% | No cumple requisitos mínimos |

---

## 🎯 Consejos para Obtener Excelente (9.0-10.0)

1. **Sé ESPECÍFICO en todo:**
   - No: "Laura necesita filtros"
   - Sí: "Laura necesita filtro 'Presupuesto total €0-€5000' con slider, visible en top 5, tooltip explicando 'Incluye alojamiento + transporte + actividades'"

2. **USA evidencia del Lab 1:**
   - "Laura (24, mochilera, €800 presupuesto, frustrada con opciones turísticas) necesita..."
   - Cita textual del Lab 1 cuando sea relevante

3. **Itera con IA (documenta):**
   - No envíes primera generación
   - 3-4 iteraciones mínimo
   - Screenshots de CADA iteración con qué mejoraste

4. **Justifica TODO:**
   - Cada decisión de diseño: POR QUÉ
   - Cada puntuación ISO: CON QUÉ EVIDENCIA
   - Cada solución a conflicto: POR QUÉ ESA y no otra

5. **Piensa críticamente:**
   - No digas "ISO es excelente" sin reflexión
   - Identifica limitaciones, casos donde principios no bastan
   - Propón mejoras a los principios si aplica

6. **Cuida presentación:**
   - Screenshots de ALTA calidad (legibles en zoom)
   - Tablas bien formateadas
   - Sin errores ortográficos (REVISA 2 veces)

---

**¡Éxito en el laboratorio!** 🚀

*Esta rúbrica busca ser TRANSPARENTE y JUSTA. Si algo no está claro, pregunta al docente ANTES de entregar.*
