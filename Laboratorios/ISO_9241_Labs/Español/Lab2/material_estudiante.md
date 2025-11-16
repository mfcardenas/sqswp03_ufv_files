# Laboratorio 2: Principios de Diálogo - Diseño de Búsqueda de Experiencias

## 📋 Información General

| Aspecto | Detalle |
|---------|---------|
| **Estándar aplicado** | ISO 9241-110:2020 - Principios de diálogo |
| **Duración total** | 8-9 horas |
| **Distribución** | 3h preparación + 2h presencial + 3-4h informe final |
| **Trabajo en equipo** | SÍ - MISMOS equipos del Lab 1 (2-3 personas) |
| **Modalidad** | Híbrida |
| **Ponderación** | 10% de la asignatura |
| **Prerequisito** | ⚠️ **LAB 1 COMPLETADO** (necesitas las personas que creaste) |

---

## 🎯 Objetivos de Aprendizaje

Al completar este laboratorio, serás capaz de:

✅ **Conocer** los 7 principios de diálogo según ISO 9241-110  
✅ **Aplicar** cada principio al diseño de interfaces interactivas  
✅ **Evaluar** diseños existentes según cumplimiento de principios  
✅ **Crear** interfaces que cumplan los 7 principios usando IA generativa  
✅ **Justificar** decisiones de diseño basándote en estándares internacionales  
✅ **Resolver** conflictos entre principios con soluciones creativas  

---

## 📚 ¿Qué es ISO 9241-110?

**ISO 9241-110:2020** es la parte del estándar ISO 9241 que define los **7 principios de diálogo** para diseño de interfaces de usuario.

### Los 7 Principios

| # | Principio | ¿Qué significa? | Ejemplo |
|---|-----------|-----------------|---------|
| 1 | **Adecuación a la tarea** | El sistema ayuda al usuario a completar su tarea eficientemente, sin pasos innecesarios | Amazon "Comprar ahora con 1-clic" |
| 2 | **Autodescripción** | La interfaz se explica a sí misma, sin necesidad de documentación externa | Tooltips, labels claros, placeholders |
| 3 | **Conformidad con expectativas** | El sistema se comporta como el usuario espera, siguiendo convenciones | Buscador arriba, logo clickable lleva a home |
| 4 | **Adecuación al aprendizaje** | Fácil de aprender para novatos, eficiente para expertos | Tutoriales opcionales, atajos de teclado |
| 5 | **Controlabilidad** | El usuario tiene control sobre el sistema, puede deshacer, cancelar, personalizar | Deshacer (Ctrl+Z), cancelar proceso |
| 6 | **Tolerancia a errores** | El sistema previene errores y facilita su corrección | Validación de formularios, confirmaciones |
| 7 | **Adecuación a individualización** | El sistema se adapta a preferencias y necesidades individuales | Guardar filtros, modo oscuro, idioma |

---

## 🧳 Contexto: Diseñando TravelEase

En este laboratorio diseñarás el **módulo de búsqueda y filtrado de experiencias turísticas** para TravelEase.

### Funcionalidades que debe incluir:

1. **Búsqueda por destino**
   - Campo de texto con autocompletado
   - Sugerencias basadas en popularidad

2. **Filtros principales**
   - Presupuesto (rango)
   - Fechas (con opción de flexibilidad)
   - Tipo de experiencia (cultural, aventura, gastronómica, etc.)
   - Servicios especiales (infantil, accesibilidad, etc.)

3. **Visualización de resultados**
   - Información clave visible (precio, duración, valoraciones)
   - Imágenes representativas
   - Opciones de ordenamiento

4. **Interacciones**
   - Aplicar/quitar filtros
   - Cambiar ordenamiento
   - Guardar búsquedas
   - Comparar opciones

---

## ⏱️ Fase 1: Preparación Obligatoria (3 horas)

### 📖 Actividad 1: Lectura de ISO 9241-110 (90 min)

**Material:** ISO 9241-110:2020 (disponible en el LMS)

**Secciones a leer:**
- Introducción (páginas 1-2)
- Términos y definiciones (páginas 3-4)
- **⭐ Sección 5: Principios de diálogo (páginas 5-18)** ← ESENCIAL

**Estrategia de lectura:**

Para cada uno de los 7 principios:

1. **Lee la definición formal** (1-2 párrafos)
2. **Identifica las palabras clave** (subráyalas)
3. **Busca los ejemplos** que da el estándar
4. **Piensa en un contraejemplo** (interfaz que viole ese principio)

**Preguntas guía mientras lees:**

- ¿Por qué este principio mejora la usabilidad?
- ¿Qué pasa si NO se cumple este principio?
- ¿Este principio puede entrar en conflicto con otros? ¿Cuáles?

**💡 Tip:** No intentes memorizar todo. Enfócate en ENTENDER el propósito de cada principio.

---

### 🔍 Actividad 2: Análisis Comparativo de Plataformas (30 min)

**Plataformas a analizar:**
1. Booking.com (búsqueda de hoteles)
2. Airbnb (búsqueda de alojamientos)
3. Skyscanner (búsqueda de vuelos)

**Tarea:**

Crea una tabla con el siguiente formato:

| Principio | Booking.com | Airbnb | Skyscanner | Mejor |
|-----------|-------------|---------|------------|-------|
| 1. Adecuación a la tarea | ✅ Filtro de presupuesto claro<br>❌ Muchos pasos para reservar | ✅ Proceso de reserva simple<br>❌ Filtros poco claros | ✅ Comparación rápida<br>✅ Búsqueda muy eficiente | Skyscanner |
| 2. Autodescripción | ✅ Tooltips en filtros<br>❌ Algunos iconos ambiguos | ✅ Explicaciones claras<br>✅ Onboarding para novatos | ❌ Muchas abreviaturas sin explicar | Airbnb |
| ... | ... | ... | ... | ... |

**Para cada principio:**
- ✅ Marca qué hace bien la plataforma
- ❌ Marca qué hace mal o no cumple
- 📸 Captura screenshots si es posible

**Entrega:** Esta tabla formará parte de tu informe de lectura previa.

---

### ✅ Actividad 3: Quiz de Comprensión (45 min)

**Ubicación:** LMS del curso  
**Formato:** 7-10 preguntas (opción múltiple + 2-3 abiertas)  
**Requisito:** Mínimo 70% aciertos  
**Intentos:** 2 permitidos  

**Temas del quiz:**
- Definición de los 7 principios
- Identificación de principios en ejemplos
- Casos donde principios entran en conflicto
- Aplicación de principios a situaciones concretas

**💡 Consejo:** Haz el quiz DESPUÉS de la lectura y el análisis comparativo. No es memorización, es comprensión.

---

### 📝 Actividad 4: Informe de Lectura Previa (45 min)

**Formato:** PDF  
**Extensión:** 2.5-3 páginas  
**Fecha límite:** 24 horas antes de la sesión presencial  

**Estructura:**

#### 1. Resumen de los 7 Principios (1.5 páginas)

Para cada principio incluye:
- **Nombre del principio**
- **Definición breve** (en tus propias palabras, no copies del estándar)
- **Ejemplo concreto** (puede ser de las plataformas analizadas)
- **Por qué es importante** (1-2 oraciones)

**Formato recomendado por principio:**

```
1. ADECUACIÓN A LA TAREA

Definición: El sistema debe permitir al usuario completar su tarea principal 
de forma eficiente, sin pasos innecesarios o información irrelevante.

Ejemplo: En Skyscanner, cuando buscas vuelos, el buscador principal solo 
pide lo ESENCIAL (origen, destino, fechas, pasajeros). No pregunta nombre, 
email, o preferencias hasta que ya seleccionaste un vuelo. Esto hace la 
búsqueda muy rápida.

Importancia: Reduce el tiempo y esfuerzo del usuario, aumentando eficiencia 
(uno de los componentes de usabilidad según ISO 9241-11 del Lab 1).
```

#### 2. Análisis Comparativo (1 página)

- **Tabla de comparación** (la que hiciste en Actividad 2)
- **Conclusión breve** (1 párrafo):
  - ¿Qué plataforma cumple mejor los principios en general?
  - ¿Qué principio es más violado?
  - ¿Qué aprendiste para aplicar a TravelEase?

#### 3. Preguntas para la Clase (3-5 preguntas)

Dudas o temas de discusión, ejemplos:
- "¿Cómo balancear Adecuación a la tarea (muchas opciones) vs. Adecuación al aprendizaje (simplicidad) para usuarios muy diversos?"
- "¿El principio de Conformidad con expectativas limita la innovación en diseño?"
- "¿Cómo medir objetivamente si una interfaz cumple con Autodescripción?"

---

## 🔬 Fase 2: Sesión Presencial en Laboratorio (2 horas)

### Antes de empezar

#### ✅ Checklist de materiales que DEBES traer:

- [ ] **Informe del Lab 1** (IMPRESO o en laptop - necesitas las personas)
- [ ] Laptop con acceso a internet
- [ ] Cuenta en herramientas de IA (ChatGPT, Claude, v0.dev, etc.)
- [ ] Informe de lectura previa completado
- [ ] Quiz aprobado (70%+)

⚠️ **SIN EL INFORME DEL LAB 1 NO PUEDES HACER ESTE LABORATORIO**

---

### 👥 Organización de Equipos

**MISMOS equipos del Lab 1, PERO roles rotan:**

Si en Lab 1 fueron:
- Persona A → Analista ISO
- Persona B → Ingeniero de Prompts  
- Persona C → Sintetizador de Información

En Lab 2 serán:
- Persona A → **Ingeniero de Prompts**
- Persona B → **Sintetizador de Información**
- Persona C → **Analista ISO**

**Responsabilidades por rol:**

**Analista ISO (rota)**
- Lidera análisis de requisitos por principio
- Completa matriz de evaluación de diseños
- Verifica cumplimiento de los 7 principios

**Ingeniero de Prompts (rota)**
- Escribe prompts para IA generativa
- Itera diseños con la IA
- Documenta proceso de generación

**Sintetizador de Información (rota)**
- Toma notas de decisiones de diseño
- Documenta conflictos entre principios
- Coordina trabajo del equipo

---

### 🎯 Actividad 1: Análisis de Requisitos por Principio (30 min)

**Objetivo:** Identificar qué significa cada principio para tu diseño y tus personas del Lab 1.

#### Paso 1.1: Recuperar Personas del Lab 1 (5 min)

Abre tu informe del Lab 1 y revisa:
- Las 3 personas que creaste (nombres, edades, contextos)
- Sus necesidades y frustraciones
- Sus objetivos al usar TravelEase
- Sus dispositivos y nivel tecnológico

**Ejemplo:**
```
Persona 1: Laura García (24 años, mochilera)
- Objetivo: Encontrar experiencias auténticas baratas
- Frustración: Plataformas muestran opciones turísticas caras
- Dispositivo: Principalmente móvil (iPhone)
- Tech-savvy: ⭐⭐⭐⭐⭐
```

#### Paso 1.2: Completar Matriz de Requisitos (20 min)

**Descarga la plantilla Excel** del LMS o crea esta tabla:

| Principio ISO | ¿Qué significa para TravelEase? | Requisitos Persona 1 | Requisitos Persona 2 | Requisitos Persona 3 | Conflictos potenciales |
|--------------|--------------------------------|---------------------|---------------------|---------------------|----------------------|
| 1. Adecuación a la tarea | | | | | |
| 2. Autodescripción | | | | | |
| ... | | | | | |

**Cómo completar cada fila:**

**Columna 2 - ¿Qué significa para TravelEase?**
- Interpretación general del principio para búsqueda de experiencias
- Ejemplo para Principio 1: "Permitir encontrar y reservar experiencias rápidamente, sin pasos innecesarios"

**Columnas 3-5 - Requisitos por persona**
- ¿Qué necesita específicamente cada persona según este principio?
- Sé ESPECÍFICO, no genérico
- Ejemplo para Principio 1 / Laura: "Filtro de presupuesto TOTAL visible (no solo alojamiento), porque busca viajes completos baratos"

**Columna 6 - Conflictos potenciales**
- ¿Este principio puede chocar con otros?
- ¿Las necesidades de las personas son contradictorias?
- Ejemplo: "Laura (experta) quiere muchos filtros avanzados vs. Turista senior (novato) quiere interfaz simple → Conflicto entre Adecuación a tarea y Adecuación al aprendizaje"

**Preguntas detonantes por principio:**

**Principio 1: Adecuación a la tarea**
- ¿Cuál es la tarea PRINCIPAL de cada persona? (búsqueda rápida vs. exploración detallada)
- ¿Qué información es ESENCIAL ver en resultados?
- ¿Qué pasos se pueden ELIMINAR del flujo?

**Principio 2: Autodescripción**
- ¿Qué elementos necesitan tooltips o ayuda contextual?
- ¿Qué iconos podrían ser ambiguos?
- ¿Qué personas necesitan MÁS explicaciones? (novatos vs. expertos)

**Principio 3: Conformidad con expectativas**
- ¿Qué plataformas similares usan tus personas? (Google, Amazon, Booking)
- ¿Dónde esperan ver el buscador? ¿Los filtros?
- ¿Qué convenciones de UI NO debes romper?

**Principio 4: Adecuación al aprendizaje**
- ¿Tus personas son novatas o expertas en apps de viajes?
- ¿Cómo guiar a novatos SIN molestar a expertos?
- ¿Necesitas tutorial, onboarding, modo avanzado?

**Principio 5: Controlabilidad**
- ¿Los usuarios pueden deshacer acciones? (quitar filtro, volver a resultados)
- ¿Pueden controlar orden de resultados?
- ¿Pueden guardar búsquedas para después?

**Principio 6: Tolerancia a errores**
- ¿Qué errores cometen usuarios al buscar? (typos, fechas imposibles)
- ¿Cómo PREVENIR errores antes de que pasen?
- ¿Cómo facilitar CORRECCIÓN si pasan? (sin perder datos)

**Principio 7: Adecuación a individualización**
- ¿Cómo personalizar la búsqueda para cada tipo de usuario?
- ¿Guardar preferencias, historial, favoritos?
- ¿Recordar filtros de búsquedas anteriores?

#### Paso 1.3: Identificar y Resolver Conflictos (5 min)

Revisa la columna de conflictos y para cada uno propón solución:

**Conflicto típico:**
- **Adecuación a tarea** (usuarios expertos quieren MUCHOS filtros)  
  vs.  
- **Adecuación al aprendizaje** (usuarios novatos se confunden con muchas opciones)

**Soluciones posibles:**
- ✅ Progressive disclosure: Mostrar filtros básicos, ocultar avanzados bajo "Más opciones"
- ✅ Modo básico vs. avanzado (usuario elige)
- ✅ Detectar experiencia y adaptar automáticamente
- ✅ Personalización: Usuario puede elegir qué filtros ver

**Documenta:**
- Conflicto identificado
- Solución elegida
- Justificación (¿por qué esa solución?)

---

### 🎨 Actividad 2: Diseño con IA Generativa (40 min)

**Objetivo:** Crear 2-3 alternativas de diseño de la interfaz de búsqueda usando IA.

#### Paso 2.1: Decidir Enfoque de Diseño (10 min)

Dos opciones:

**Opción A: Diseño Unificado** (recomendado)
- UNA interfaz que funciona para las 3 personas
- Más complejo pero más realista
- Requiere balancear necesidades diferentes

**Opción B: Diseños Especializados**
- 2-3 versiones, cada una optimizada para una persona
- Más fácil de diseñar
- Permite comparar trade-offs claramente

**Decisión de equipo:** Discutan 5 min y elijan. No hay respuesta correcta.

#### Paso 2.2: Generar Diseños con IA (25 min)

**Herramientas recomendadas:**

| Herramienta | ¿Qué genera? | Ventajas | Desventajas |
|-------------|--------------|----------|-------------|
| **v0.dev** (Vercel) | Código React + UI visual | Muy rápido, resultado profesional | Requiere cuenta |
| **ChatGPT-4** | Código HTML/CSS/JS | Flexible, permite iteración | Hay que visualizar el código |
| **Claude** (Anthropic) | Wireframes ASCII + código | Buenas explicaciones | No tan visual |
| **Figma AI** | Diseño visual | Herramienta profesional | Curva de aprendizaje |
| **Diseño manual** | Wireframes en papel | No depende de tecnología | Menos refinado |

**Elige 1-2 herramientas** y genera al menos **2 alternativas de diseño:**

**Diseño A: Enfoque Minimalista**
- Prioriza simplicidad y aprendizaje
- Pocos filtros visibles (3-5 principales)
- Ideal para novatos

**Diseño B: Enfoque de Poder (Power User)**
- Muchos filtros y opciones avanzadas
- Control total sobre búsqueda
- Ideal para expertos

**Diseño C (opcional): Híbrido**
- Balance entre A y B
- Progressive disclosure
- Modos básico/avanzado

**Proceso de generación:**

1. **Usa prompts base** del archivo `prompts_ia.md`
2. **Personaliza con:**
   - Requisitos de tu matriz de principios
   - Necesidades de tus personas
   - Funcionalidades específicas

3. **Itera:**
   - Primera generación → probablemente genérica
   - Pide ajustes específicos: "Agrega tooltips en filtros (Principio 2: Autodescripción)"
   - 2-3 iteraciones → diseño refinado

**Ejemplo de prompt inicial:**

```
Diseña una interfaz de búsqueda de experiencias turísticas para la 
plataforma TravelEase. 

CONTEXTO:
TravelEase permite buscar y reservar experiencias turísticas (tours, 
actividades, alojamiento, gastronomía) en destinos específicos.

PRINCIPIOS ISO 9241-110 A CUMPLIR:

1. Adecuación a la tarea:
   - Filtro de presupuesto total (vuelo + alojamiento + actividades) visible
   - Búsqueda rápida para viajeros de negocios (1-2 clics)
   - Opción "Fechas flexibles ±3 días" para mochileros

2. Autodescripción:
   - Tooltips en todos los iconos de filtros
   - Placeholder text descriptivo en buscador
   - Contador de resultados visible ("234 experiencias encontradas")

[... continuar con los 7 principios]

USUARIOS OBJETIVO (del Lab 1):
- Laura, 24 años, mochilera: Busca experiencias auténticas baratas, usa móvil
- Familia Rodríguez: Necesita ver servicios infantiles, usa tablet  
- David Chen, 35, negocios: Prioriza velocidad y flexibilidad, usa laptop

FUNCIONALIDADES REQUERIDAS:
- Campo de búsqueda con autocompletado
- Filtros: presupuesto, fechas, tipo de experiencia, servicios
- Resultados con: imagen, precio, duración, valoraciones
- Ordenamiento: por precio, valoración, relevancia
- Guardar búsquedas

FORMATO DE SALIDA:
Genera código HTML/CSS/JavaScript funcional o wireframe detallado.
Si generas código, usa diseño responsive (mobile-first).
```

#### Paso 2.3: Documentar Proceso (5 min)

Para cada diseño generado:
- 📸 Captura screenshot o guarda código
- 📝 Anota iteraciones realizadas ("Iteración 1: genérica, Iteración 2: agregué tooltips, Iteración 3: ajusté layout móvil")
- 🏷️ Etiqueta el diseño (Diseño A: Minimalista, Diseño B: Power User, etc.)

---

### 📊 Actividad 3: Evaluación de Diseños (25 min)

**Objetivo:** Evaluar objetivamente tus diseños según los 7 principios.

#### Paso 3.1: Matriz de Evaluación (15 min)

Para **cada diseño** (A, B, C), evalúa cumplimiento de **cada principio**:

**Descarga plantilla Excel** o crea esta tabla:

| Principio | Diseño A | Diseño B | Diseño C | Mejor |
|-----------|----------|----------|----------|-------|
| 1. Adecuación a la tarea | ⭐⭐⭐☆☆ (3/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐☆ (4/5) | **B** |
| ... | ... | ... | ... | ... |
| **TOTAL** | **21/35** | **28/35** | **30/35** | **C** |

**Escala de evaluación:**

- ⭐⭐⭐⭐⭐ (5/5): Cumple excelentemente
- ⭐⭐⭐⭐☆ (4/5): Cumple bien, mejoras menores
- ⭐⭐⭐☆☆ (3/5): Cumple parcialmente
- ⭐⭐☆☆☆ (2/5): Cumple mínimamente
- ⭐☆☆☆☆ (1/5): No cumple o viola

**IMPORTANTE:** Para cada celda, justifica la puntuación:

✅ **Buena justificación:**
```
Diseño A - Principio 2 (Autodescripción): ⭐⭐⭐⭐☆ (4/5)

Cumple bien:
- Todos los filtros tienen labels claros ("Presupuesto", "Fechas", "Tipo")
- Campo de búsqueda tiene placeholder: "¿A dónde quieres ir? (ej: París, Tokio)"
- Tooltips en iconos de "Fechas flexibles" y "Búsqueda avanzada"

Mejoras menores:
- El icono de "Ordenar por" no tiene tooltip
- Contador de resultados está en gris claro, poco visible

Evidencia: [screenshot del diseño con flechas señalando elementos]
```

❌ **Mala justificación:**
```
Diseño A - Principio 2: ⭐⭐⭐⭐☆ (4/5)
Es bastante autodescriptivo.
```
*(Demasiado vaga, sin evidencia)*

#### Paso 3.2: Identificar Mejor Diseño (5 min)

- Suma puntajes (máximo 35 puntos)
- Identifica diseño ganador
- Decide si:
  - **Opción 1:** Usar diseño ganador para informe final
  - **Opción 2:** Crear diseño híbrido combinando mejores aspectos de cada uno

Si eliges Opción 2:
- Lista qué tomar de cada diseño
- Ejemplo: "Diseño A: Layout de filtros | Diseño B: Sistema de tooltips | Diseño C: Funcionalidad de guardar búsquedas"

#### Paso 3.3: Plan de Mejoras (5 min)

Para el diseño seleccionado, lista **5-7 mejoras concretas:**

| # | Mejora | Principio(s) afectado(s) | Prioridad |
|---|--------|--------------------------|-----------|
| 1 | Agregar tooltip en icono "Ordenar por" | 2. Autodescripción | Alta |
| 2 | Hacer contador de resultados más visible (negro, negrita) | 2. Autodescripción | Media |
| 3 | Agregar botón "Deshacer últimos filtros" | 5. Controlabilidad, 6. Tolerancia a errores | Alta |
| 4 | Implementar "Modo avanzado" para filtros adicionales | 4. Adecuación al aprendizaje, 7. Individualización | Media |
| 5 | Validar fechas (fecha de vuelta > fecha de ida) | 6. Tolerancia a errores | Alta |

**Prioridad:**
- **Alta:** Afecta usabilidad significativamente
- **Media:** Mejora la experiencia
- **Baja:** Nice to have

---

### 🏁 Cierre de Sesión (5 min)

**Resumen del docente:**
- Aplicaron los 7 principios a diseño real
- Vieron que algunos principios entran en conflicto → es normal
- No hay diseño perfecto, solo trade-offs bien justificados

**Próximos pasos:**
- Refinar diseño seleccionado
- Implementar mejoras del plan
- Redactar informe técnico completo

**Adelanto Lab 3:**
- Harán test de usabilidad del diseño que crearon hoy
- Aplicarán proceso UCD (ISO 9241-210)
- Validarán si los principios realmente funcionan en práctica

---

## 📝 Fase 3: Informe Técnico Final (3-4 horas)

### Estructura del Informe

**Formato:** PDF  
**Extensión:** 10-14 páginas (sin contar anexos)  
**Herramientas:** Word, Google Docs, LaTeX, Markdown  
**Fecha límite:** [Definida por docente, típicamente 1 semana después de sesión]  

---

### Sección 1: Portada y Resumen Ejecutivo (1 página)

**Portada debe incluir:**
- Título: "Laboratorio 2: Aplicación de Principios de Diálogo ISO 9241-110 al Diseño de Búsqueda de TravelEase"
- Nombre de integrantes del equipo
- Fecha
- Curso y universidad

**Resumen ejecutivo** (200-300 palabras):
- ¿Qué hicieron en este lab?
- ¿Cuál fue el principal desafío?
- ¿Cuál es el resultado final? (tipo de diseño creado)
- ¿Principal hallazgo o aprendizaje?

---

### Sección 2: Introducción (1-1.5 páginas)

#### 2.1 Contexto del Proyecto
- Breve descripción de TravelEase
- Módulo específico: Búsqueda de experiencias
- Conexión con Lab 1 (mencionar personas creadas)

#### 2.2 Objetivo del Laboratorio
- Aplicar ISO 9241-110 al diseño de interfaz de búsqueda
- Crear diseños usando IA generativa
- Evaluar cumplimiento de principios

#### 2.3 Alcance
- ¿Qué incluye el diseño? (búsqueda, filtros, resultados)
- ¿Qué NO incluye? (proceso de pago, perfil de usuario, etc.)

---

### Sección 3: Marco Teórico - Los 7 Principios (2-2.5 páginas)

Para cada principio:

**Nombre del principio**

**Definición** (según ISO 9241-110, en tus palabras)

**Importancia para TravelEase** (2-3 oraciones)

**Ejemplo de cumplimiento:** [screenshot de plataforma que lo cumple bien]

**Ejemplo de violación:** [screenshot de plataforma que lo viola]

**Formato sugerido:**

```
3.1 Principio 1: Adecuación a la Tarea

Definición: El sistema debe ayudar al usuario a completar su tarea de forma 
eficiente, minimizando pasos innecesarios y presentando solo información 
relevante para la tarea actual.

Importancia para TravelEase: En la búsqueda de experiencias, los usuarios 
tienen objetivos diversos (encontrar opciones baratas vs. buscar experiencias 
premium) y el sistema debe adaptar la información mostrada a cada tipo de 
búsqueda, evitando abrumar con datos irrelevantes.

Ejemplo de cumplimiento: [Imagen de Amazon "Comprar ahora con 1-clic"]
Amazon permite a usuarios recurrentes completar compra en 1 clic, eliminando 
pasos repetitivos de introducir dirección y pago.

Ejemplo de violación: [Imagen de formulario largo]
Formulario que pide 15 datos antes de mostrar resultados de búsqueda, 
cuando solo origen y destino son necesarios para la tarea de búsqueda.
```

---

### Sección 4: Análisis de Requisitos por Principio (2.5-3 páginas)

#### 4.1 Personas del Lab 1 (Resumen)

Breve recordatorio de las 3 personas (1 párrafo cada una):

```
Persona 1: Laura García (24 años, mochilera)
Diseñadora gráfica freelance de Barcelona que viaja 3-4 veces al año con 
presupuesto de €800. Busca experiencias auténticas, no turísticas. Muy 
tech-savvy, usa principalmente móvil (iPhone 13). Frustrada con plataformas 
que muestran opciones caras y turísticas.
```

#### 4.2 Matriz de Requisitos

Incluir la tabla completa que completaron en Actividad 1.2:

| Principio ISO | Interpretación para TravelEase | Requisitos Persona 1 | Requisitos Persona 2 | Requisitos Persona 3 | Conflictos |
|--------------|-------------------------------|---------------------|---------------------|---------------------|------------|
| ... | ... | ... | ... | ... | ... |

**Después de la tabla, analizar:**

**¿Qué patrones identificaron?** (1 párrafo)
- Ejemplo: "Notamos que Laura (experta) y Turista Senior (novato) tienen necesidades opuestas en cantidad de opciones visibles..."

**¿Qué requisitos son comunes a las 3 personas?** (lista)
- Todos necesitan ver precio total claro
- Todos necesitan filtro de fechas
- Todos necesitan valoraciones visibles

**¿Qué requisitos son únicos por persona?** (lista)
- Solo Laura necesita filtro de "experiencias auténticas / no turísticas"
- Solo Familia necesita ver servicios infantiles destacados
- Solo David necesita filtro de cancelación flexible

#### 4.3 Conflictos entre Principios y Soluciones

Para cada conflicto identificado:

**Conflicto #1:** Adecuación a tarea vs. Adecuación al aprendizaje

**Descripción:** Laura (experta) quiere acceso rápido a 15+ filtros avanzados para búsquedas precisas. Turista Senior (novato) se confunde con más de 5 opciones visibles.

**Solución elegida:** Progressive disclosure con 5 filtros básicos visibles + botón "Más filtros" que expande opciones avanzadas.

**Justificación:** Permite a novatos enfocarse en lo esencial mientras expertos pueden acceder a opciones avanzadas en 1 clic. Cumple con ambos principios sin sacrificar uno completamente.

**Implementación:** [Screenshot mostrando los 5 filtros básicos y el botón "Más filtros"]

---

### Sección 5: Alternativas de Diseño (3-4 páginas)

#### 5.1 Metodología de Diseño

**Herramientas utilizadas:**
- v0.dev para generar código React
- ChatGPT-4 para iteraciones y mejoras
- Figma para refinamiento visual

**Proceso:**
1. Prompt inicial con requisitos de los 7 principios
2. Generación de 3 alternativas (Minimalista, Power User, Híbrido)
3. Iteración con IA (3-4 rondas por diseño)
4. Refinamiento manual

#### 5.2 Diseño A: Enfoque Minimalista

**Descripción:** (1 párrafo)
Prioriza simplicidad y facilidad de aprendizaje. Solo 5 filtros visibles (destino, fechas, presupuesto, tipo de experiencia, valoración mínima). Ideal para usuarios novatos o búsquedas rápidas.

**Screenshot:** [Imagen del diseño completo - desktop y móvil]

**Cumplimiento de principios:**

| Principio | Puntuación | Justificación |
|-----------|------------|---------------|
| 1. Adecuación a tarea | ⭐⭐⭐☆☆ (3/5) | Cumple para búsquedas simples pero limita opciones avanzadas |
| 2. Autodescripción | ⭐⭐⭐⭐⭐ (5/5) | Labels muy claros, placeholders descriptivos, tooltips en todos los iconos |
| ... | ... | ... |
| **TOTAL** | **28/35** | |

**Fortalezas:** (lista de 3-5)
- Curva de aprendizaje muy baja
- Interfaz limpia y no intimidante
- Excelente para móvil (pocos elementos)

**Debilidades:** (lista de 3-5)
- Limitado para usuarios expertos
- No permite búsquedas muy específicas
- Falta personalización

#### 5.3 Diseño B: Enfoque Power User

**Descripción:** (1 párrafo)  
**Screenshot:** [Imagen]  
**Cumplimiento de principios:** [Tabla]  
**Fortalezas:** [Lista]  
**Debilidades:** [Lista]  

#### 5.4 Diseño C: Enfoque Híbrido (si aplica)

**Descripción:** (1 párrafo)  
**Screenshot:** [Imagen]  
**Cumplimiento de principios:** [Tabla]  
**Fortalezas:** [Lista]  
**Debilidades:** [Lista]  

#### 5.5 Comparación de Alternativas

**Tabla comparativa:**

| Criterio | Diseño A | Diseño B | Diseño C |
|----------|----------|----------|----------|
| Cumplimiento ISO (total) | 28/35 | 25/35 | 31/35 |
| Mejor para novatos | ⭐⭐⭐⭐⭐ | ⭐⭐☆☆☆ | ⭐⭐⭐⭐☆ |
| Mejor para expertos | ⭐⭐☆☆☆ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ |
| Usabilidad móvil | ⭐⭐⭐⭐⭐ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ |
| Complejidad de implementación | Baja | Alta | Media |
| **Diseño seleccionado** | | | ✅ |

**Justificación de selección:** (1-2 párrafos)

---

### Sección 6: Diseño Final y Refinamiento (2-3 páginas)

#### 6.1 Diseño Final

**Screenshot principal:** [Vista desktop completa]  
**Screenshot móvil:** [Vista responsive]  
**Screenshot tablet:** [Vista intermedia - si aplica]  

**Descripción detallada de componentes:**

**Barra de búsqueda principal:**
- Campo de texto con autocompletado de destinos
- Icono de lupa a la izquierda
- Placeholder: "¿A dónde quieres ir? (ej: París, Bali, Tokio)"
- Cumple Principios: 2 (Autodescripción), 3 (Conformidad con expectativas), 6 (Tolerancia a errores - autocompletado previene typos)

**Panel de filtros:**
- 5 filtros básicos visibles:
  1. Fechas (con opción "Fechas flexibles ±3 días")
  2. Presupuesto (slider de rango con valores numéricos)
  3. Tipo de experiencia (dropdown con iconos)
  4. Valoración mínima (estrellas clickables)
  5. Servicios especiales (checkboxes: infantil, accesibilidad, mascotas)
- Botón "Más filtros" (expande 10 filtros adicionales)
- Cumple Principios: 1 (Adecuación a tarea), 4 (Adecuación al aprendizaje - progressive disclosure), 5 (Controlabilidad)

**Zona de resultados:**
- Contador: "234 experiencias encontradas"
- Ordenamiento: Dropdown (Relevancia, Precio ↑, Precio ↓, Valoración, Más recientes)
- Cards de resultados con: imagen, título, precio, duración, valoración, badge de "Experiencia auténtica" si aplica
- Cumple Principios: 2 (Autodescripción - info clara), 5 (Controlabilidad - ordenamiento)

**Funcionalidades de individualización:**
- Botón "Guardar búsqueda" (icono de estrella)
- Opción "Recordar mis filtros" (checkbox al final)
- Cumple Principio: 7 (Adecuación a individualización)

**Manejo de errores:**
- Si fechas contradictorias → mensaje: "La fecha de vuelta debe ser posterior a la fecha de ida"
- Si no hay resultados → mensaje: "No encontramos experiencias con estos filtros. Intenta: [sugerencias]"
- Cumple Principio: 6 (Tolerancia a errores)

#### 6.2 Cumplimiento de los 7 Principios (Diseño Final)

**Tabla de evaluación final:**

| Principio | Puntuación | Evidencia en el diseño | Mejoras aplicadas |
|-----------|------------|------------------------|-------------------|
| 1. Adecuación a tarea | ⭐⭐⭐⭐☆ (4/5) | [Screenshot señalando filtros específicos por persona] | Agregamos "Presupuesto total" (Laura), "Servicios infantiles" (Familia), "Cancelación flexible" (David) |
| 2. Autodescripción | ⭐⭐⭐⭐⭐ (5/5) | [Screenshot de tooltips y labels] | Agregamos tooltip en TODOS los iconos, placeholders descriptivos, contador visible |
| ... | ... | ... | ... |
| **TOTAL** | **32/35** | | |

#### 6.3 Mejoras Implementadas

Del plan de mejoras (Actividad 3.3), explicar qué se implementó:

| # | Mejora planificada | Estado | Evidencia |
|---|-------------------|--------|-----------|
| 1 | Agregar tooltip en "Ordenar por" | ✅ Implementada | [Screenshot] |
| 2 | Contador más visible | ✅ Implementada | Cambió de gris a negro, negrita, tamaño 16px |
| 3 | Botón "Deshacer últimos filtros" | ✅ Implementada | [Screenshot] |
| 4 | Modo avanzado | ✅ Implementada | Botón "Más filtros" |
| 5 | Validación de fechas | ✅ Implementada | [Screenshot de mensaje de error] |
| 6 | ... | ⏳ Pendiente | Requiere backend, fuera de alcance |

#### 6.4 Decisiones de Diseño Justificadas

**Decisión #1: Progressive Disclosure para filtros**

**Problema:** Conflicto entre expertos (quieren muchos filtros) y novatos (se confunden con muchas opciones).

**Alternativas consideradas:**
- A) Mostrar todos los filtros siempre → Intimida a novatos
- B) Modo básico vs. avanzado (usuario elige) → Requiere decisión adicional
- C) Progressive disclosure (expandir "Más filtros") → Elegida

**Justificación:** Progressive disclosure cumple Principios 1, 4 y 7 simultáneamente sin forzar al usuario a tomar decisión previa. Novatos ven interfaz simple, expertos expanden con 1 clic.

**Decisión #2: Autocompletado en buscador de destinos**

**Problema:** Usuarios cometen errores tipográficos, pierden tiempo.

**Solución:** Autocompletado basado en destinos populares + corrección de typos.

**Justificación:** Cumple Principio 6 (Tolerancia a errores) al PREVENIR errores antes de que pasen. También mejora eficiencia (Principio 1).

**Evidencia:** [GIF o screenshots mostrando autocompletado en acción]

*(Incluir 3-5 decisiones clave)*

#### 6.5 Responsive Design

**Adaptaciones por dispositivo:**

**Desktop (>1024px):**
- Filtros en sidebar izquierdo
- Resultados en grid de 3 columnas
- Todos los filtros básicos visibles

**Tablet (768px - 1024px):**
- Filtros colapsables en panel superior
- Resultados en grid de 2 columnas
- Filtros se ocultan después de aplicar

**Móvil (<768px):**
- Filtros en modal ("Filtrar resultados")
- Resultados en lista vertical (1 columna)
- Buscador sticky en top
- Botón flotante de "Filtros" siempre visible

**Screenshots:** [Incluir los 3 tamaños]

**Justificación:** Laura usa principalmente móvil, Familia usa tablet, David usa laptop → Diseño debe funcionar óptimamente en los 3 dispositivos (cumple Principio 1: Adecuación a tarea de cada persona).

---

### Sección 7: Reflexión y Aprendizajes (1.5-2 páginas)

#### 7.1 Principales Desafíos

**Desafío #1:** Balancear necesidades contradictorias de usuarios novatos vs. expertos.

**Cómo lo resolvimos:** Progressive disclosure + opciones de personalización.

**Aprendizaje:** No existe diseño perfecto para todos. La clave es dar opciones sin forzar decisiones.

**Desafío #2:** IA generó diseños muy genéricos en primera iteración.

**Cómo lo resolvimos:** Prompts mucho más específicos con requisitos de cada principio + ejemplos concretos.

**Aprendizaje:** Calidad de prompts = calidad de resultados. La IA es herramienta, no reemplazo de pensamiento crítico.

**Desafío #3:** Algunos principios entran en conflicto inevitable.

**Ejemplo concreto:** Conformidad con expectativas (buscador arriba-centro, patrón conocido) vs. Innovación en UX.

**Decisión:** Priorizar conformidad en elementos críticos (buscador, filtros), innovar en secundarios (visualización de resultados).

**Aprendizaje:** Estándares no limitan creatividad, sino que guían dónde NO experimentar (para no confundir usuarios).

#### 7.2 Conexión con Lab 1

**¿Cómo se usaron las personas del Lab 1?**
- Personas definieron requisitos específicos por principio
- Ejemplo: Laura necesita "Presupuesto total" → implementamos filtro combinado
- Tareas identificadas en Lab 1 → funcionalidades del buscador

**¿Qué validamos del análisis de Lab 1?**
- Frustración de Laura con plataformas que no filtran por autenticidad → agregamos badge "Experiencia auténtica"
- Necesidad de Familia de ver servicios infantiles → filtro destacado

**¿Qué corregiríamos del Lab 1 ahora?**
- Persona X necesitaba también [funcionalidad Y] que no habíamos identificado
- Contexto de uso móvil de Laura es más crítico de lo pensado → diseño mobile-first

#### 7.3 Aplicación de ISO 9241-110 en Proyectos Reales

**¿Los 7 principios son aplicables en tu área de trabajo?**
(Respuesta personalizada del equipo)

**¿Qué principio es más importante en tu opinión? ¿Por qué?**
(Respuesta argumentada)

**¿Has visto violaciones de estos principios en apps que usas? Ejemplos:**
- App X viola Principio 6 (Tolerancia a errores): borra todo el formulario si hay un error
- App Y cumple excelentemente Principio 7 (Individualización): recuerda todas mis preferencias

#### 7.4 Limitaciones del Trabajo

**Limitaciones técnicas:**
- Diseño es wireframe/mockup, no implementación funcional
- No se validó con usuarios reales (se hará en Lab 3)
- No se consideró backend (APIs, base de datos)

**Limitaciones de alcance:**
- Solo diseñamos búsqueda, no reserva completa
- No se consideró accesibilidad (WCAG) en detalle
- No se optimizó rendimiento

**Limitaciones de tiempo:**
- Hubiéramos querido iterar más con la IA
- No se pudo hacer test A/B de alternativas

---

### Sección 8: Conclusiones (1 página)

**Recapitulación:**
- Aplicamos los 7 principios de ISO 9241-110 al diseño de interfaz de búsqueda de TravelEase
- Creamos 3 alternativas de diseño usando IA generativa
- Evaluamos y seleccionamos diseño híbrido que cumple 32/35 puntos
- Implementamos mejoras específicas por principio

**Logros:**
- Diseño que balancea necesidades de 3 tipos de usuarios muy diferentes
- Soluciones creativas a conflictos entre principios
- Aplicación práctica de estándar internacional a caso real

**Próximos pasos (Lab 3):**
- Test de usabilidad con usuarios representativos
- Validar si principios realmente mejoran la experiencia
- Iterar diseño basado en feedback real

**Reflexión final:**
(1-2 párrafos sobre el valor de los estándares de usabilidad)

---

### Sección 9: Referencias

**Formato:** APA 7ª edición

**Referencias mínimas:**

ISO. (2020). *ISO 9241-110:2020 Ergonomics of human-system interaction — Part 110: Interaction principles.* International Organization for Standardization.

ISO. (2018). *ISO 9241-11:2018 Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts.* International Organization for Standardization.

Nielsen, J. (2020). *10 Usability Heuristics for User Interface Design.* Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/

*(Agregar lecturas adicionales del Lab)*

---

### Anexos

**Anexo A:** Matriz de requisitos completa (de Actividad 1.2)

**Anexo B:** Prompts utilizados con IA generativa

**Anexo C:** Código generado (si aplica)

**Anexo D:** Screenshots adicionales de iteraciones de diseño

**Anexo E:** Informe del Lab 1 (resumen de personas) - opcional

---

## ✅ Checklist de Auto-Evaluación

Antes de entregar, verifica:

### Contenido
- [ ] Las 9 secciones están completas
- [ ] Incluye al menos 2 alternativas de diseño evaluadas
- [ ] Matriz de requisitos completa (7 principios × 3 personas)
- [ ] Diseño final tiene screenshots desktop + móvil
- [ ] Cada principio tiene evidencia visual en diseño final
- [ ] Decisiones de diseño están justificadas con principios
- [ ] Reflexión es crítica y personal (no genérica)
- [ ] Referencias en formato APA

### Formato
- [ ] 10-14 páginas (sin anexos)
- [ ] Portada profesional
- [ ] Índice de contenidos
- [ ] Screenshots claros y legibles
- [ ] Tablas numeradas y referenciadas en texto
- [ ] Sin errores ortográficos

### Calidad Técnica
- [ ] Diseño final cumple mínimo 28/35 puntos (80%)
- [ ] Justificaciones son específicas (no genéricas)
- [ ] Evidencia concreta de cada principio
- [ ] Conflictos entre principios identificados y resueltos
- [ ] Conexión clara con Lab 1 (personas usadas)

### Uso de IA
- [ ] Documentado proceso de generación con IA
- [ ] Incluidos prompts utilizados (Anexo B)
- [ ] Explicadas iteraciones realizadas
- [ ] IA usada como herramienta, no sustituto de pensamiento crítico

---

## 📞 ¿Necesitas Ayuda?

### Dudas Frecuentes

**P: ¿Puedo usar un diseño de referencia (Booking, Airbnb) como base?**  
R: Sí, pero debes MEJORARLO según los 7 principios. No copies, itera.

**P: ¿Qué hago si la IA genera diseños malos?**  
R: Itera con prompts más específicos. Si persiste, diseña manualmente wireframes.

**P: ¿Es obligatorio usar IA?**  
R: No, pero facilita mucho el trabajo. Puedes diseñar manualmente con herramientas como Figma, Sketch, o incluso papel.

**P: ¿Qué pasa si dos principios son contradictorios?**  
R: ¡Eso es lo interesante! Documenta el conflicto y justifica tu decisión. No hay respuesta única.

**P: ¿El diseño debe ser funcional (con código)?**  
R: No necesariamente. Un wireframe bien documentado es suficiente. Si generas código con IA, es un plus pero no obligatorio.

**P: ¿Puedo cambiar las personas del Lab 1?**  
R: No. Este lab usa las personas que YA creaste. Si tu Lab 1 tuvo errores, puedes hacer notas de corrección en la Sección 7.2.

---

## 📚 Recursos Adicionales

- **Prompts de IA:** Ver `prompts_ia.md`
- **Lecturas preparatorias:** Ver `lecturas_preparatorias.md`
- **Ejemplos de diseños:** [Carpeta compartida del curso]
- **Plantillas:** Excel de matrices, Word de informe

---

**¡Éxito en el laboratorio! 🚀**

*Recuerda: El objetivo no es crear el diseño más bonito, sino el que mejor cumpla los 7 principios de ISO 9241-110 para tus usuarios específicos.*
