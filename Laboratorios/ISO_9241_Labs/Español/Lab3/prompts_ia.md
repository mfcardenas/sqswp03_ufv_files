# Laboratorio 3: Evaluación Heurística y Testing de Usabilidad
## Prompts de Inteligencia Artificial

### Información del Laboratorio
- **Asignatura:** Interacción Persona-Computador
- **Laboratorio:** Lab 3 - Evaluación de Usabilidad de Airbnb
- **Aplicación de IA:** Análisis automatizado de datos de usabilidad y generación de reportes
- **Herramientas:** ChatGPT, Claude, Gemini, o cualquier LLM avanzado
- **Objetivo:** Acelerar y enriquecer el análisis de resultados de evaluación

---

## ÍNDICE DE PROMPTS

1. **Análisis de Métricas ISO 9241-11**
2. **Evaluación Heurística Automática ISO 9241-110**
3. **Correlación de Resultados y Síntesis**
4. **Generación de Recomendaciones Priorizadas**
5. **Creación de Visualizaciones de Datos**
6. **Redacción de Reportes Profesionales**
7. **Validación y Mejora de Hallazgos**

---

## 1. ANÁLISIS DE MÉTRICAS ISO 9241-11

### Prompt 1.1: Interpretación de Datos Cuantitativos

```
Actúa como un experto en usabilidad que aplica la norma ISO 9241-11. 

Analiza los siguientes datos de testing de usabilidad de Airbnb:

DATOS DE ENTRADA:
- Número de participantes: [X]
- Tareas evaluadas: [3 tareas específicas]

MÉTRICAS POR TAREA:
Tarea 1 - Búsqueda básica:
- Participantes que completaron: X/Y
- Tiempo promedio: X segundos
- Errores promedio: X por usuario
- Satisfacción promedio: X/5

Tarea 2 - Filtros avanzados:
- Participantes que completaron: X/Y
- Tiempo promedio: X segundos
- Errores promedio: X por usuario
- Satisfacción promedio: X/5

Tarea 3 - Exploración detallada:
- Participantes que completaron: X/Y
- Tiempo promedio: X segundos
- Errores promedio: X por usuario
- Satisfacción promedio: X/5

ANÁLISIS REQUERIDO:
1. Calcula las métricas consolidadas de EFICACIA, EFICIENCIA y SATISFACCIÓN según ISO 9241-11
2. Identifica cuál tarea presenta mayores problemas de usabilidad
3. Compara los resultados con benchmarks típicos de plataformas e-commerce
4. Sugiere umbrales de aceptabilidad para cada métrica
5. Identifica patrones y tendencias en los datos

FORMATO DE RESPUESTA:
- Tabla resumen de métricas ISO 9241-11
- Análisis interpretativo por tarea
- Comparación con estándares de la industria
- Recomendaciones para mejora basadas en datos
```

### Prompt 1.2: Análisis Estadístico Avanzado

```
Como especialista en análisis de datos de UX, realiza un análisis estadístico de los siguientes resultados de testing:

DATOS CUANTITATIVOS:
[Insertar tabla con todos los datos individuales por participante y tarea]

ANÁLISIS SOLICITADO:
1. Calcula medidas de tendencia central y dispersión para cada métrica
2. Identifica outliers y explica su posible causa
3. Realiza análisis de correlación entre tiempo, errores y satisfacción
4. Determina si hay diferencias significativas entre tareas
5. Calcula intervalos de confianza para las métricas principales

METODOLOGÍA:
- Usa criterios estadísticos apropiados para muestras pequeñas
- Aplica pruebas no paramétricas si es necesario
- Interpreta resultados en contexto de usabilidad

ENTREGA:
- Resumen estadístico completo
- Interpretación de correlaciones encontradas
- Recomendaciones basadas en significancia estadística
- Visualizaciones sugeridas para presentar los datos
```

---

## 2. EVALUACIÓN HEURÍSTICA AUTOMÁTICA ISO 9241-110

### Prompt 2.1: Análisis de Principios de Diálogo

```
Eres un experto evaluador de usabilidad especializado en ISO 9241-110. 

Analiza la siguiente evaluación heurística de Airbnb:

PUNTUACIONES REGISTRADAS:
- Adecuación a la tarea: X/5
- Autodescripción: X/5  
- Controlabilidad: X/5
- Conformidad con expectativas: X/5
- Tolerancia a errores: X/5
- Adaptabilidad: X/5
- Capacidad de aprendizaje: X/5

PROBLEMAS IDENTIFICADOS:
[Lista de problemas con clasificación de severidad]

TAREAS SOLICITADAS:
1. Calcula puntuación total y porcentaje de cumplimiento ISO 9241-110
2. Identifica el principio más y menos cumplido
3. Analiza la distribución de problemas por severidad
4. Correlaciona puntuaciones bajas con problemas específicos
5. Sugiere qué principios requieren atención prioritaria
6. Proporciona interpretación cualitativa de resultados

CRITERIOS DE EVALUACIÓN:
- Puntuación >4: Excelente cumplimiento
- Puntuación 3-4: Cumplimiento aceptable  
- Puntuación 2-3: Cumplimiento deficiente
- Puntuación <2: Cumplimiento crítico

FORMATO DE RESPUESTA:
- Dashboard resumen de cumplimiento ISO
- Análisis detallado por principio
- Mapa de calor de problemas
- Recomendaciones de mejora priorizadas
```

### Prompt 2.2: Generación Automática de Problemas

```
Actúa como un evaluador heurístico experto que analiza interfaces web.

CONTEXTO: Evaluación de Airbnb.es siguiendo ISO 9241-110

INFORMACIÓN DISPONIBLE:
- Screenshots de interfaz: [Describir capturas clave]
- Flujo de usuario: Búsqueda → Filtros → Detalle → Pre-reserva
- Observaciones de testing: [Principales errores y frustraciones]

SOLICITUD:
Genera una evaluación heurística completa identificando problemas específicos para cada principio ISO 9241-110:

PARA CADA PRINCIPIO:
1. Busca 2-3 problemas específicos en la interfaz
2. Clasifica cada problema por severidad (Crítico/Mayor/Menor/Cosmético)
3. Proporciona evidencia específica (ubicación, comportamiento)
4. Sugiere solución concreta para cada problema
5. Estima impacto en métricas de usabilidad

PRINCIPIOS A EVALUAR:
- Adecuación a la tarea
- Autodescripción
- Controlabilidad  
- Conformidad con expectativas
- Tolerancia a errores
- Adaptabilidad
- Capacidad de aprendizaje

FORMATO:
Por cada problema identificado:
- Principio violado: [X]
- Descripción: [Problema específico]
- Ubicación: [Dónde se encuentra]
- Severidad: [Clasificación]
- Evidencia: [Comportamiento observado]
- Solución: [Propuesta específica]
- Impacto: [Métricas que mejoraría]
```

---

## 3. CORRELACIÓN DE RESULTADOS Y SÍNTESIS

### Prompt 3.1: Integración de Métodos de Evaluación

```
Como experto en metodologías de evaluación UX, integra los resultados de testing cuantitativo y evaluación heurística:

DATOS DE TESTING ISO 9241-11:
- Eficacia total: X%
- Eficiencia promedio: X tareas/hora
- Satisfacción: X/5
- Principales errores: [Lista específica]
- Tareas más problemáticas: [Identificadas]

DATOS HEURÍSTICOS ISO 9241-110:
- Puntuación total: X/35 (X%)
- Principios más violados: [Lista]
- Problemas críticos: X
- Problemas mayores: X

ANÁLISIS SOLICITADO:
1. CORRELACIÓN: ¿Los problemas heurísticos explican los errores de usuario?
2. CONVERGENCIA: ¿Dónde coinciden ambos métodos en identificar problemas?
3. DIVERGENCIA: ¿Qué problemas detectó solo cada método?
4. PREDICTIBILIDAD: ¿Los principios mal evaluados predicen baja satisfacción?
5. COMPLETITUD: ¿Cubren ambos métodos todos los aspectos de usabilidad?

METODOLOGÍA:
- Mapea errores específicos con principios violados
- Identifica patrones de correlación
- Evalúa fortalezas/debilidades de cada método
- Sugiere cómo combinar ambos enfoques óptimamente

ENTREGA:
- Matriz de correlación Errores ↔ Principios
- Análisis de convergencia/divergencia
- Síntesis integrada de hallazgos
- Recomendaciones metodológicas para futuras evaluaciones
```

### Prompt 3.2: Identificación de Patrones de Usabilidad

```
Analiza los siguientes datos para identificar patrones de usabilidad en Airbnb:

DATOS LONGITUDINALES:
[Resultados por usuario, tarea y tiempo]

DATOS CONTEXTUALES:
- Experiencia previa con Airbnb: [Principiante/Intermedio/Experto]
- Edad de participantes: [Rangos]
- Familiaridad con tecnología: [Escala]

PATRONES A IDENTIFICAR:
1. LEARNING CURVES: ¿Mejora el rendimiento entre tareas?
2. USER SEGMENTS: ¿Hay diferencias por perfil de usuario?
3. PAIN POINTS: ¿Dónde se concentran los problemas?
4. SUCCESS FACTORS: ¿Qué facilita el éxito en tareas?
5. RECOVERY PATTERNS: ¿Cómo se recuperan los usuarios de errores?

ANÁLISIS REQUERIDO:
- Segmentación de usuarios por comportamiento
- Identificación de momentos críticos en el flujo
- Análisis de abandono vs. persistencia
- Factores predictores de éxito/fracaso

APLICACIÓN:
- Personalización de interfaz por segmento
- Optimización de puntos críticos
- Diseño de sistemas de ayuda contextual
- Estrategias de onboarding diferenciadas
```

---

## 4. GENERACIÓN DE RECOMENDACIONES PRIORIZADAS

### Prompt 4.1: Matriz de Priorización de Mejoras

```
Como consultor senior de UX, genera recomendaciones priorizadas para Airbnb basadas en:

HALLAZGOS CLAVE:
[Resumen de problemas identificados por ambos métodos]

CRITERIOS DE PRIORIZACIÓN:
1. IMPACTO EN MÉTRICAS ISO (1-5): ¿Cuánto mejoraría eficacia, eficiencia, satisfacción?
2. FRECUENCIA DE OCURRENCIA (1-5): ¿Qué tan común es el problema?
3. SEVERIDAD HEURÍSTICA (1-5): ¿Qué tan grave es la violación de principios?
4. ESFUERZO DE IMPLEMENTACIÓN (1-5): ¿Qué tan fácil/difícil es solucionarlo?
5. VALOR DE NEGOCIO (1-5): ¿Qué impacto tendría en conversión/retención?

METODOLOGÍA:
Para cada problema identificado:
- Asigna puntuación en cada criterio
- Calcula puntuación ponderada total
- Justifica la evaluación con evidencias
- Proporciona solución específica y accionable

FORMATO DE RECOMENDACIONES:
Problema: [Descripción específica]
Ubicación: [Dónde se encuentra]
Impacto: X/5 | Frecuencia: X/5 | Severidad: X/5 | Facilidad: X/5 | Negocio: X/5
SCORE TOTAL: X/25
Solución: [Propuesta concreta]
Métrica objetivo: [Cómo medir mejora]
Timeline: [Estimación de implementación]

ENTREGA:
- Top 10 recomendaciones rankeadas
- Roadmap de implementación sugerido  
- Estimación de impacto agregado
- Quick wins vs. proyectos a largo plazo
```

### Prompt 4.2: Especificaciones Técnicas de Mejoras

```
Transforma las recomendaciones de usabilidad en especificaciones técnicas implementables:

RECOMENDACIONES PRIORIZADAS:
[Lista de top 5-10 mejoras identificadas]

PARA CADA RECOMENDACIÓN, PROPORCIONA:

1. USER STORY:
"Como [tipo de usuario], quiero [funcionalidad] para [beneficio]"

2. ACCEPTANCE CRITERIA:
- Criterios específicos y medibles
- Condiciones de éxito/fracaso
- Edge cases considerados

3. WIREFRAMES/MOCKUPS:
- Descripción textual detallada de cambios visuales
- Estados de interfaz (normal, hover, error, loading)
- Responsive considerations

4. ESPECIFICACIONES TÉCNICAS:
- Cambios de HTML/CSS necesarios
- JavaScript/interacciones requeridas
- APIs o datos adicionales necesarios
- Consideraciones de performance

5. TESTING PLAN:
- Casos de prueba específicos
- Métricas a medir post-implementación
- A/B testing suggestions

6. IMPLEMENTACIÓN:
- Esfuerzo estimado (horas/días)
- Dependencias técnicas
- Riesgos y mitigaciones
- Rollback plan

FORMATO:
Estructurado como tickets de desarrollo listos para implementar por equipos técnicos.
```

---

## 5. CREACIÓN DE VISUALIZACIONES DE DATOS

### Prompt 5.1: Dashboards de Métricas de Usabilidad

```
Diseña visualizaciones efectivas para presentar resultados de evaluación de usabilidad:

DATOS DISPONIBLES:
[Todos los datos cuantitativos y cualitativos recopilados]

AUDIENCIAS OBJETIVO:
- Stakeholders ejecutivos (resumen alto nivel)
- Equipo de UX (detalles técnicos)
- Desarrolladores (especificaciones de problemas)

VISUALIZACIONES SOLICITADAS:

1. EXECUTIVE DASHBOARD:
- Métricas ISO 9241-11 en formato semáforo
- Comparación con benchmarks industria
- ROI estimado de mejoras propuestas
- Timeline de implementación

2. UX TEAM DASHBOARD:
- Heatmap de problemas por principio ISO 9241-110
- Distribución de severidad de problemas
- Correlación errores vs. principios violados
- User journey con pain points marcados

3. DEVELOPMENT DASHBOARD:
- Lista priorizada de issues técnicos
- Esfuerzo vs. impacto scatter plot
- Roadmap de implementación
- Métricas de validación por fix

ESPECIFICACIONES:
Para cada visualización, proporciona:
- Tipo de gráfico óptimo (bar, line, scatter, heatmap, etc.)
- Colores y codificación visual
- Etiquetas y títulos claros
- Interactividad sugerida
- Herramientas recomendadas (Excel, Tableau, D3.js, etc.)

CRITERIOS DE DISEÑO:
- Claridad > Estética
- Accionabilidad de insights
- Compatibilidad con diferentes dispositivos
- Actualización fácil con nuevos datos
```

### Prompt 5.2: Infografías para Comunicación de Resultados

```
Crea el concepto para una infografía que comunique efectivamente los hallazgos de usabilidad de Airbnb:

OBJETIVO: Presentar resultados de manera visualmente atractiva y fácil de entender para audiencias no técnicas.

CONTENIDO A INCLUIR:
- Puntuación general de usabilidad (X/100)
- Top 3 fortalezas de la interfaz
- Top 3 problemas más críticos
- Impacto en experiencia del usuario
- Beneficios esperados de mejoras

ESTRUCTURA VISUAL:
1. HEADER: Título impactante + puntuación general
2. METODOLOGÍA: Iconos explicando proceso de evaluación
3. HALLAZGOS PRINCIPALES: Sección central con datos clave
4. PROBLEMAS CRÍTICOS: Visualización de pain points
5. RECOMENDACIONES: Quick wins vs. proyectos largo plazo
6. IMPACTO: Métricas de mejora esperada

ELEMENTOS VISUALES:
- Iconografía representativa de cada problema/solución
- Color coding: Rojo (problemas), Verde (fortalezas), Amarillo (mejoras)
- Gráficos simples (barras, círculos, flechas)
- Screenshots anotados de interfaz
- Personas/avatares para representar usuarios

DESCRIPCIÓN TEXTUAL:
Para cada sección, proporciona:
- Texto conciso y no técnico
- Headlines impactantes
- Datos en formato fácil de digerir
- Call-to-actions claros

HERRAMIENTAS SUGERIDAS:
- Canva templates
- Adobe Illustrator specifications
- PowerPoint layout instructions
- Figma components structure
```

---

## 6. REDACCIÓN DE REPORTES PROFESIONALES

### Prompt 6.1: Executive Summary Automático

```
Redacta un Executive Summary profesional basado en los siguientes resultados de evaluación de usabilidad:

DATOS DE ENTRADA:
[Todos los resultados consolidados del laboratorio]

ESTRUCTURA REQUERIDA:

1. OVERVIEW (100 palabras):
- Objetivo de la evaluación
- Metodología aplicada (ISO 9241-11 y 9241-110)
- Participantes y scope

2. KEY FINDINGS (200 palabras):
- Puntuación general de usabilidad
- Métricas principales: eficacia, eficiencia, satisfacción
- Top 3 problemas críticos identificados
- Top 3 fortalezas de la plataforma

3. BUSINESS IMPACT (150 palabras):
- Impacto en conversión estimado
- Riesgo de abandono por problemas de usabilidad
- Oportunidades de mejora de satisfacción del cliente
- Comparación con competidores

4. RECOMMENDATIONS (150 palabras):
- Top 5 mejoras priorizadas
- Quick wins vs. proyectos estratégicos
- Timeline sugerido de implementación
- Inversión estimada vs. ROI esperado

5. NEXT STEPS (100 palabras):
- Acciones inmediatas recomendadas
- Plan de validación de mejoras
- Métricas de seguimiento
- Cronograma de re-evaluación

TONE & STYLE:
- Profesional pero accesible
- Enfocado en impacto de negocio
- Data-driven con insights accionables
- Persuasivo para generar buy-in de stakeholders

FORMATO:
700 palabras total, con bullets y destacados para facilitar lectura rápida.
```

### Prompt 6.2: Redacción de Secciones Técnicas

```
Redacta las secciones técnicas detalladas del reporte de usabilidad:

DATOS DISPONIBLES:
[Datos cuantitativos específicos y observaciones cualitativas]

SECCIONES A REDACTAR:

1. METODOLOGÍA (400 palabras):
- Justificación de métodos elegidos (ISO 9241-11 y 9241-110)
- Descripción detallada del protocolo de testing
- Participantes: reclutamiento, características, representatividad
- Configuración del entorno de testing
- Limitaciones y consideraciones éticas

2. RESULTADOS CUANTITATIVOS (600 palabras):
- Métricas de eficacia por tarea con análisis estadístico
- Análisis de eficiencia: tiempos, errores, patrones
- Medición de satisfacción: escalas usadas, resultados
- Tablas y gráficos interpretativos
- Comparación con benchmarks cuando disponibles

3. EVALUACIÓN HEURÍSTICA (500 palabras):
- Puntuación detallada por principio ISO 9241-110
- Justificación de puntuaciones asignadas
- Catálogo completo de problemas por severidad
- Evidencias específicas con referencias a interface
- Correlación con resultados de testing

4. ANÁLISIS INTEGRADO (400 palabras):
- Convergencia entre métodos cuantitativos y cualitativos
- Explicación de discrepancias encontradas
- Patrones emergentes y insights inesperados
- Validación cruzada de hallazgos principales

CRITERIOS DE CALIDAD:
- Rigor metodológico y transparencia
- Uso apropiado de terminología técnica ISO
- Referenciación de estándares y literatura
- Objetividad en presentación de resultados
- Trazabilidad de datos a conclusiones

FORMATO ACADÉMICO:
- Referencias a normas ISO específicas
- Uso de tercera persona
- Tablas y figuras numeradas
- Conclusiones sustentadas en evidencias
```

---

## 7. VALIDACIÓN Y MEJORA DE HALLAZGOS

### Prompt 7.1: Verificación de Consistencia

```
Actúa como un auditor de calidad que revisa la consistencia de un reporte de usabilidad:

ELEMENTOS A AUDITAR:
[Reporte completo o secciones específicas]

VERIFICACIONES SOLICITADAS:

1. CONSISTENCIA METODOLÓGICA:
- ¿Los métodos aplicados están correctamente descritos?
- ¿Las métricas calculadas siguen las definiciones ISO?
- ¿Hay coherencia entre objetivos, métodos y conclusiones?

2. VALIDEZ DE DATOS:
- ¿Los cálculos de métricas son correctos?
- ¿Las clasificaciones de severidad están justificadas?
- ¿Hay evidencias suficientes para cada hallazgo?

3. LÓGICA DE RECOMENDACIONES:
- ¿Las recomendaciones se derivan lógicamente de los hallazgos?
- ¿La priorización está bien fundamentada?
- ¿Son las soluciones propuestas viables y específicas?

4. CALIDAD DE COMUNICACIÓN:
- ¿Es el lenguaje apropiado para la audiencia?
- ¿Están los datos presentados claramente?
- ¿Hay sesgos o interpretaciones cuestionables?

FORMATO DE FEEDBACK:
Para cada issue identificado:
- Ubicación específica en el reporte
- Descripción del problema
- Sugerencia de mejora
- Nivel de severidad (Crítico/Mayor/Menor)

CRITERIOS DE EXCELENCIA:
- Rigor metodológico
- Claridad comunicativa
- Accionabilidad de insights
- Profesionalismo en presentación
```

### Prompt 7.2: Enriquecimiento con Mejores Prácticas

```
Enriquece el siguiente reporte de usabilidad con mejores prácticas de la industria:

REPORTE ACTUAL:
[Contenido existente del reporte]

MEJORAS SOLICITADAS:

1. BENCHMARKING INDUSTRIA:
- Compara métricas obtenidas con estándares sector e-commerce/travel
- Identifica dónde está Airbnb vs. competidores
- Proporciona contexto de performance relativa

2. CASOS DE ESTUDIO:
- Incluye ejemplos de soluciones exitosas en plataformas similares
- Referencias a rediseños documentados públicamente
- Lessons learned de implementaciones similares

3. MARCO TEÓRICO AMPLIADO:
- Conecta hallazgos con teorías de UX establecidas
- Referencias a investigación académica relevante
- Principios de psicología cognitiva aplicables

4. METODOLOGÍAS COMPLEMENTARIAS:
- Sugiere métodos adicionales para validar hallazgos
- Propone técnicas de testing más avanzadas
- Recomienda herramientas específicas para medición continua

5. ROADMAP ESTRATÉGICO:
- Visión a largo plazo de evolución de usabilidad
- Consideraciones de tecnologías emergentes
- Plan de madurez en UX para la organización

FORMATO:
- Integra mejoras de manera natural en contenido existente
- Añade secciones adicionales donde sea apropiado
- Mantiene coherencia de tono y estilo
- Proporciona referencias y fuentes para profundización
```

---

## INSTRUCCIONES DE USO

### Personalización de Prompts

**Para usar estos prompts efectivamente:**

1. **Reemplaza placeholders:** Cambia [X], [Lista], [Datos] por información real de tu evaluación
2. **Ajusta contexto:** Modifica según tu audiencia específica y objetivos del laboratorio
3. **Combina prompts:** Usa varios en secuencia para análisis más profundo
4. **Itera resultados:** Refina outputs con prompts de seguimiento específicos

### Secuencia Recomendada de Uso

```
FASE 1: ANÁLISIS INICIAL
→ Prompt 1.1 (Métricas ISO)
→ Prompt 2.1 (Heurística ISO)
→ Prompt 3.1 (Correlación)

FASE 2: SÍNTESIS Y RECOMENDACIONES
→ Prompt 4.1 (Priorización)
→ Prompt 4.2 (Especificaciones)

FASE 3: COMUNICACIÓN
→ Prompt 6.1 (Executive Summary)
→ Prompt 5.1 (Visualizaciones)
→ Prompt 6.2 (Secciones técnicas)

FASE 4: VALIDACIÓN
→ Prompt 7.1 (Consistencia)
→ Prompt 7.2 (Enriquecimiento)
```

### Mejores Prácticas

**Para obtener mejores resultados:**

✅ **Proporciona contexto completo:** Incluye todos los datos relevantes  
✅ **Sé específico:** Detalles sobre audiencia, objetivos, limitaciones  
✅ **Valida outputs:** Revisa que los resultados sean factualmente correctos  
✅ **Itera progresivamente:** Usa outputs de un prompt como input del siguiente  
✅ **Adapta según necesidad:** Modifica prompts para tu contexto específico  

### Limitaciones y Consideraciones

**Ten en cuenta:**

⚠️ **Verificación humana necesaria:** La IA puede cometer errores de cálculo o interpretación  
⚠️ **Contexto específico:** Adapta recomendaciones a las limitaciones reales de tu proyecto  
⚠️ **Sesgo de datos:** La calidad del análisis depende de la calidad de datos de entrada  
⚠️ **Conocimiento actualizado:** Verifica que las mejores prácticas sugeridas estén actualizadas  

---

**Desarrollado por:** [Nombre del profesor]  
**Última actualización:** Noviembre 2024  
**Versión:** 1.0  
**Compatibilidad:** ChatGPT 4+, Claude 3+, Gemini Pro