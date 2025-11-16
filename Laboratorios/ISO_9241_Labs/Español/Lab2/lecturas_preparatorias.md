# Lecturas Preparatorias - Laboratorio 2: Principios de Diálogo

## 📚 Material de Lectura Obligatorio

### Lectura Principal: ISO 9241-110:2020

**Título completo:** Ergonomics of human-system interaction — Part 110: Interaction principles

**Ubicación:** Disponible en el LMS del curso

---

## 🎯 Objetivo de Esta Guía

Esta guía te ayudará a:
- ✅ Entender los 7 principios de diálogo sin perderte en tecnicismos
- ✅ Identificar QUÉ leer y QUÉ puedes omitir
- ✅ Capturar lo esencial para aplicar en el laboratorio
- ✅ Conectar teoría con ejemplos prácticos

⏱️ **Tiempo estimado:** 90 minutos de lectura enfocada

---

## 📖 Sección 1: ISO 9241-110:2020 (Lectura Obligatoria - 60 min)

### Estructura del Documento

El estándar ISO 9241-110 tiene aproximadamente 20 páginas. NO necesitas leer todo.

**LEE ESTAS SECCIONES:**

| Sección | Páginas | ¿Qué contiene? | Importancia | Tiempo |
|---------|---------|----------------|-------------|--------|
| **Introducción** | 1-2 | Contexto, propósito del estándar | ⭐⭐⭐☆☆ | 5 min |
| **Scope** | 1 | Alcance, a qué aplica | ⭐⭐☆☆☆ | 3 min |
| **Términos y Definiciones** | 3-4 | Glosario de conceptos clave | ⭐⭐⭐⭐☆ | 10 min |
| **⭐ Sección 5: Principios de Diálogo** | 5-18 | LOS 7 PRINCIPIOS (ESENCIAL) | ⭐⭐⭐⭐⭐ | 40 min |
| Anexos | 19-20 | Ejemplos adicionales | ⭐⭐☆☆☆ | Opcional |

**PUEDES OMITIR:**
- Sección 4: Relación con otros estándares
- Referencias normativas detalladas
- Notas al pie muy técnicas

---

### Estrategia de Lectura por Sección

#### 📌 Introducción (Páginas 1-2)

**QUÉ BUSCAR:**
- ¿Por qué existen estos principios?
- ¿A qué tipo de sistemas aplican? (web, móvil, desktop, etc.)
- ¿Cómo se relacionan con usabilidad (ISO 9241-11 del Lab 1)?

**PREGUNTAS CLAVE MIENTRAS LEES:**
1. ¿Los principios de diálogo mejoran efectividad, eficiencia o satisfacción (usabilidad)?
2. ¿Aplican solo a interfaces gráficas o también a voz, táctil, etc.?

**TOMA NOTA DE:**
- Definición de "diálogo" en contexto de interfaces
- Relación con usabilidad (concepto del Lab 1)

---

#### 📌 Términos y Definiciones (Páginas 3-4)

**CONCEPTOS CLAVE A ENTENDER:**

**1. Diálogo (Dialogue)**
- No es "conversación" literal
- Es cualquier INTERACCIÓN entre usuario y sistema
- Ejemplos: Llenar formulario, hacer clic, deslizar slider

**2. Usuario (User)**
- Persona que interactúa con el sistema
- Puede ser novato, intermedio o experto (importante para Principio 4)

**3. Tarea (Task)**
- Actividad que el usuario quiere completar
- Ejemplo: "Buscar vuelo barato a París"

**4. Contexto de uso (Context of use)**
- ¡Lo viste en Lab 1!
- Incluye: usuarios, tareas, equipo (dispositivo), entorno

**5. Efectividad, Eficiencia, Satisfacción**
- ¡También del Lab 1!
- Los principios de diálogo mejoran estos 3 aspectos

**EJERCICIO RÁPIDO:**
Lee la definición de "diálogo" y escribe 3 ejemplos de diálogo en TravelEase:
1. _______________________________
2. _______________________________
3. _______________________________

*(Respuesta esperada: "Seleccionar fechas en date picker", "Filtrar por presupuesto con slider", "Ordenar resultados por precio")*

---

#### ⭐ Sección 5: LOS 7 PRINCIPIOS DE DIÁLOGO (Páginas 5-18) - ESENCIAL

**ESTA ES LA SECCIÓN MÁS IMPORTANTE.** Dedícale 40 minutos enfocados.

---

### 🔷 PRINCIPIO 1: Suitability for the Task (Adecuación a la Tarea)

**📍 Ubicación:** Sección 5.1 (páginas 5-6)

**Definición oficial (resumida):**
> El diálogo es adecuado para la tarea cuando apoya al usuario en completar eficientemente su trabajo, sin pasos innecesarios o información irrelevante.

**EN ESPAÑOL CLARO:**
- El sistema debe ayudarte a hacer tu tarea RÁPIDO
- NO debe pedirte información que no necesita
- NO debe tener pasos extra innecesarios

**EJEMPLOS DEL ESTÁNDAR:**
- ✅ **Bueno:** Sistema de reservas que solo pide origen, destino, fecha (lo esencial)
- ❌ **Malo:** Sistema que pide email, teléfono, dirección ANTES de mostrar resultados

**EJEMPLOS PRÁCTICOS (TravelEase):**

✅ **Cumple Principio 1:**
- Filtro de "Presupuesto TOTAL" (alojamiento + transporte + actividades) → Tarea de Laura es encontrar viajes baratos, esto ayuda directamente
- Botón "Búsqueda rápida" → Tarea de David es reservar rápido, esto elimina pasos

❌ **Viola Principio 1:**
- Pedir número de pasaporte ANTES de buscar experiencias → Innecesario para la tarea de búsqueda
- Formulario de 15 campos para ver resultados → Excesivo, ralentiza tarea

**PREGUNTAS CLAVE AL LEER:**
1. ¿Qué caracteriza a un diálogo "adecuado a la tarea"?
2. ¿Qué información es relevante vs. irrelevante para una tarea?
3. ¿Cómo balancear completitud vs. eficiencia?

**TOMA NOTA DE:**
- Lista de sub-principios (ej: "proveer solo la información necesaria")
- Ejemplos específicos del estándar
- Relación con eficiencia (componente de usabilidad)

---

### 🔷 PRINCIPIO 2: Self-Descriptiveness (Autodescripción)

**📍 Ubicación:** Sección 5.2 (páginas 7-8)

**Definición oficial (resumida):**
> El diálogo es autodescriptivo cuando cada paso es inmediatamente comprensible mediante feedback o explicación, sin necesidad de documentación externa.

**EN ESPAÑOL CLARO:**
- La interfaz se explica a sí misma
- Usuario no necesita manual o tutorial para entender qué hacer
- Cada elemento dice claramente qué es y qué hace

**EJEMPLOS DEL ESTÁNDAR:**
- ✅ **Bueno:** Botón con label "Guardar cambios" (claro qué hace)
- ❌ **Malo:** Botón solo con icono "💾" sin texto (ambiguo para algunos usuarios)

**EJEMPLOS PRÁCTICOS (TravelEase):**

✅ **Cumple Principio 2:**
- Placeholder en buscador: "¿A dónde quieres ir? (ej: París, Bali, Tokio)" → Se explica solo
- Tooltip en icono de "Fechas flexibles": "Buscaremos ±3 días de tus fechas" → Explicación contextual
- Contador visible: "234 experiencias encontradas" → Feedback inmediato

❌ **Viola Principio 2:**
- Iconos sin texto ni tooltip → Usuario adivina qué hacen
- Mensajes de error vagos: "Error 404" → No se explica qué pasó ni cómo arreglarlo
- Filtros con abreviaturas: "ACC" (¿accesibilidad? ¿aceptado?) → Ambiguo

**ELEMENTOS CLAVE DE AUTODESCRIPCIÓN:**
1. **Labels claros:** "Presupuesto total" > "Budget"
2. **Placeholders descriptivos:** "Introduce destino (ej: París)" > "Destino"
3. **Tooltips contextuales:** Icono ℹ️ que explica concepto
4. **Feedback inmediato:** "Guardando..." → "Guardado ✓"
5. **Mensajes de error constructivos:** "La fecha de vuelta debe ser después de la de ida" > "Error de fecha"

**PREGUNTAS CLAVE AL LEER:**
1. ¿Qué tipo de información debe ser autodescriptiva?
2. ¿Cuándo usar tooltips vs. labels permanentes?
3. ¿Cómo balancear autodescripción sin saturar la interfaz?

**TOMA NOTA DE:**
- Tipos de feedback mencionados (visual, textual, auditivo)
- Relación con curva de aprendizaje
- Ejemplos de mensajes claros vs. ambiguos

---

### 🔷 PRINCIPIO 3: Conformity with User Expectations (Conformidad con Expectativas)

**📍 Ubicación:** Sección 5.3 (páginas 9-10)

**Definición oficial (resumida):**
> El diálogo se conforma con las expectativas del usuario cuando es consistente y corresponde a características predecibles del usuario (experiencia, educación, convenciones).

**EN ESPAÑOL CLARO:**
- El sistema se comporta como el usuario espera
- Sigue convenciones establecidas (patrones de diseño conocidos)
- Es consistente (mismo elemento hace lo mismo siempre)

**EJEMPLOS DEL ESTÁNDAR:**
- ✅ **Bueno:** Logo en esquina superior izquierda que lleva a home (convención web)
- ❌ **Malo:** Botón "Aceptar" que en realidad CANCELA la acción (contradice expectativa)

**EJEMPLOS PRÁCTICOS (TravelEase):**

✅ **Cumple Principio 3:**
- Buscador en parte SUPERIOR CENTRAL → Convención de Google, Booking, Amazon
- Filtros en SIDEBAR IZQUIERDO → Patrón de e-commerce familiar
- Botón azul/verde para acción principal → Color esperado para "continuar"
- Estrellas para valoraciones (★★★★☆) → Símbolo universal

❌ **Viola Principio 3:**
- Buscador al final de la página → Contradice expectativa (usuarios buscan arriba)
- Icono de "X" que GUARDA en vez de cerrar → Confuso
- Botón rojo para "Continuar" → Rojo se asocia a peligro/cancelar

**TIPOS DE EXPECTATIVAS:**

1. **Convenciones universales:**
   - Logo arriba-izquierda lleva a home
   - "X" cierra ventanas
   - Verde = éxito, Rojo = error/peligro, Azul = info
   - Subrayado = enlace

2. **Convenciones del dominio:**
   - En turismo: Fotos grandes de destinos
   - Calendarios para fechas
   - Moneda con símbolo (€, $)

3. **Consistencia interna:**
   - Si un botón dice "Más info" en un lugar, debe decir igual en otros
   - Mismo color para misma acción en toda la app

**PREGUNTAS CLAVE AL LEER:**
1. ¿Cómo se forman las expectativas de los usuarios?
2. ¿Cuándo es aceptable romper una convención?
3. ¿Qué pasa si hay conflicto entre expectativa de novato vs. experto?

**TOMA NOTA DE:**
- Lista de convenciones comunes
- Diferencia entre consistencia interna y externa
- Ejemplos de violaciones graves de expectativas

---

### 🔷 PRINCIPIO 4: Suitability for Learning (Adecuación al Aprendizaje)

**📍 Ubicación:** Sección 5.4 (páginas 11-12)

**Definición oficial (resumida):**
> El diálogo es adecuado al aprendizaje cuando guía y apoya al usuario en aprender a usar el sistema, tanto para novatos como para expertos.

**EN ESPAÑOL CLARO:**
- Fácil de aprender para usuarios nuevos
- Eficiente para usuarios expertos (no los aburre con tutoriales obligatorios)
- Ayuda al usuario a mejorar progresivamente

**EJEMPLOS DEL ESTÁNDAR:**
- ✅ **Bueno:** Tooltips opcionales + atajos de teclado para expertos
- ❌ **Malo:** Tutorial de 15 minutos OBLIGATORIO cada vez que abres la app

**EJEMPLOS PRÁCTICOS (TravelEase):**

✅ **Cumple Principio 4:**
- **Progressive disclosure:** 5 filtros básicos visibles + botón "Más filtros" para avanzados
  - Novatos: Usan solo los 5 básicos (simple)
  - Expertos: Expanden en 1 clic (eficiente)
- **Onboarding opcional:** "¿Primera vez? Tour rápido (30 seg)" → Botón "Saltar"
- **Ejemplos en placeholders:** "ej: París, Bali, Tokio" → Enseña formato esperado
- **Feedback educativo:** "Consejo: Para mejores precios, busca con fechas flexibles"

❌ **Viola Principio 4:**
- Tutorial de 10 pasos OBLIGATORIO → Frustra a expertos
- Sin ayuda para novatos → Curva de aprendizaje empinada
- Funciones avanzadas escondidas sin pistas → Expertos no las descubren

**ESTRATEGIAS PARA ADECUACIÓN AL APRENDIZAJE:**

1. **Para novatos:**
   - Tutoriales cortos y opcionales
   - Tooltips contextuales
   - Ejemplos visibles (placeholders, hints)
   - Mensajes educativos sutiles

2. **Para expertos:**
   - Atajos de teclado (Ctrl+F para buscar)
   - Opciones avanzadas accesibles
   - Modo "avanzado" o "experto"
   - Recordar preferencias

3. **Para todos:**
   - Consistencia (aprendes una vez, aplicas siempre)
   - Feedback claro cuando cometen errores
   - Ayuda contextual (disponible pero no intrusiva)

**PREGUNTAS CLAVE AL LEER:**
1. ¿Cómo balancear simplicidad para novatos vs. potencia para expertos?
2. ¿Qué hace que un sistema sea "learnable"?
3. ¿Cuándo usar progressive disclosure vs. opciones siempre visibles?

**TOMA NOTA DE:**
- Diferencia entre learnability (aprendizaje inicial) y memorability (recordar después de no usar)
- Técnicas de progressive disclosure
- Relación con curva de aprendizaje

---

### 🔷 PRINCIPIO 5: Controllability (Controlabilidad)

**📍 Ubicación:** Sección 5.5 (páginas 13-14)

**Definición oficial (resumida):**
> El diálogo es controlable cuando el usuario puede iniciar, dirigir, pausar y finalizar la interacción. El sistema no toma control de forma inesperada.

**EN ESPAÑOL CLARO:**
- El usuario está al mando, no el sistema
- Usuario puede deshacer, cancelar, pausar acciones
- Sistema no hace cosas automáticas sin permiso
- Usuario puede personalizar orden y ritmo de trabajo

**EJEMPLOS DEL ESTÁNDAR:**
- ✅ **Bueno:** Botón "Deshacer" (Ctrl+Z), cancelar proceso, guardar borrador
- ❌ **Malo:** Ventana modal que no se puede cerrar, auto-envío de formulario sin confirmación

**EJEMPLOS PRÁCTICOS (TravelEase):**

✅ **Cumple Principio 5:**
- **Deshacer filtros:** Cada filtro tiene "✕" para quitarlo individualmente + botón "Limpiar todos"
- **Cancelar búsqueda:** Si búsqueda tarda, botón "Cancelar" visible
- **Guardar búsqueda:** Usuario decide SI y CUÁNDO guardar, no automático
- **Ordenar resultados:** Usuario controla orden (precio, valoración, fecha)
- **Pausar proceso:** Puede salir de reserva y volver después (guarda datos)

❌ **Viola Principio 5:**
- **Auto-aplicar filtros:** Filtros se aplican automáticamente sin botón "Aplicar" → Usuario pierde control del momento
- **Modal sin "X":** Ventana que solo se cierra completando acción → Usuario forzado
- **Auto-redirect:** Después de 5 seg redirige automáticamente → Usuario no controla timing
- **No se puede deshacer:** Borrar filtros sin confirmación y sin "Deshacer" → Irreversible

**ELEMENTOS DE CONTROLABILIDAD:**

1. **Control de inicio:**
   - Usuario decide CUÁNDO buscar (botón "Buscar", no automático)
   - Usuario decide CUÁNDO aplicar filtros

2. **Control de dirección:**
   - Usuario elige orden de resultados
   - Usuario elige QUÉ filtros aplicar (no forzados)

3. **Control de pausar/reanudar:**
   - Guardar búsqueda a mitad
   - Salir de proceso y volver

4. **Control de finalizar:**
   - Cancelar búsqueda en progreso
   - Cerrar modals con "X"

5. **Control de deshacer:**
   - Deshacer acciones (Ctrl+Z)
   - Volver atrás sin perder datos

**PREGUNTAS CLAVE AL LEER:**
1. ¿Qué nivel de control es apropiado? (mucho control puede ser abrumador)
2. ¿Cuándo es aceptable automatizar acciones?
3. ¿Cómo informar al usuario que tiene control?

**TOMA NOTA DE:**
- Tipos de control mencionados (inicio, dirección, ritmo, finalización)
- Concepto de "locus of control"
- Relación con satisfacción (componente de usabilidad)

---

### 🔷 PRINCIPIO 6: Error Tolerance (Tolerancia a Errores)

**📍 Ubicación:** Sección 5.6 (páginas 15-16)

**Definición oficial (resumida):**
> El diálogo es tolerante a errores cuando el resultado deseado puede alcanzarse a pesar de errores evidentes, con mínima o ninguna corrección por el usuario.

**EN ESPAÑOL CLARO:**
- El sistema PREVIENE errores antes de que pasen
- Si pasan errores, son FÁCILES de corregir
- Mensajes de error son CLAROS y CONSTRUCTIVOS (dicen cómo arreglar)
- El usuario NO pierde su trabajo por un error

**EJEMPLOS DEL ESTÁNDAR:**
- ✅ **Bueno:** Validación en tiempo real, confirmación de acciones críticas, autoguardado
- ❌ **Malo:** Formulario que borra TODO si hay un error, mensajes crípticos ("Error 500")

**EJEMPLOS PRÁCTICOS (TravelEase):**

✅ **Cumple Principio 6:**

**PREVENCIÓN de errores:**
- **Autocompletado en destino:** "pari" → sugiere "París" (previene typos)
- **Validación de fechas:** Si fecha vuelta < fecha ida → mensaje inmediato: "La fecha de vuelta debe ser posterior a la de ida. ¿Quieres intercambiarlas?"
- **Deshabilitar opciones inválidas:** Si no hay disponibilidad en julio, ese mes aparece gris en calendario
- **Confirmación de acciones críticas:** "¿Seguro que quieres borrar todos los filtros?" antes de borrar

**CORRECCIÓN fácil:**
- **Mensajes claros:** NO "Error en campo", SÍ "El presupuesto mínimo debe ser menor que el máximo (ahora: Min €1000, Max €500)"
- **Sugerencias:** "No encontramos experiencias con estos filtros. ¿Intentas: [Ampliar fechas] [Aumentar presupuesto] [Quitar filtro X]?"
- **No perder datos:** Si hay error, mantener todos los campos llenos (usuario no reescribe)
- **Deshacer:** Si borró filtros por error, botón "Deshacer" restaura

❌ **Viola Principio 6:**
- **Sin validación:** Permite reservar con fecha de vuelta antes de ida
- **Mensajes crípticos:** "ERROR: NULL POINTER EXCEPTION" (usuario no entiende)
- **Perder datos:** Si presupuesto inválido, borra TODOS los filtros
- **Sin confirmación:** Botón "Limpiar filtros" sin preguntar → Fácil clic accidental

**NIVELES DE TOLERANCIA A ERRORES:**

1. **Nivel 1: PREVENIR (mejor):**
   - Autocompletado, sugerencias
   - Validación en tiempo real
   - Deshabilitar opciones inválidas
   - Ejemplos claros de formato esperado

2. **Nivel 2: DETECTAR TEMPRANO:**
   - Validar al salir del campo (no al enviar formulario completo)
   - Mostrar error específico inmediatamente
   - Mantener foco en campo con error

3. **Nivel 3: FACILITAR CORRECCIÓN:**
   - Mensaje dice CÓMO arreglar, no solo QUÉ está mal
   - Ofrecer soluciones ("¿Quieres intercambiar fechas?")
   - No borrar datos válidos

4. **Nivel 4: RECUPERAR:**
   - Autoguardado
   - Deshacer acciones
   - Historial de cambios

**PREGUNTAS CLAVE AL LEER:**
1. ¿Qué tipos de errores son más comunes en interfaces?
2. ¿Cómo prevenir sin frustrar (ej: validación muy estricta)?
3. ¿Qué hace un buen mensaje de error?

**TOMA NOTA DE:**
- Jerarquía de tolerancia a errores (prevención > detección > corrección > recuperación)
- Tipos de errores (deslices vs. errores conceptuales)
- Principios de mensajes de error claros

---

### 🔷 PRINCIPIO 7: Suitability for Individualization (Adecuación a Individualización)

**📍 Ubicación:** Sección 5.7 (páginas 17-18)

**Definición oficial (resumida):**
> El diálogo es adecuado para individualización cuando puede ser modificado para adaptarse a las tareas, preferencias individuales y habilidades del usuario.

**EN ESPAÑOL CLARO:**
- El sistema se adapta a cada usuario
- Usuario puede personalizar interfaz según preferencias
- Sistema recuerda preferencias del usuario
- Se ajusta a diferentes niveles de habilidad

**EJEMPLOS DEL ESTÁNDAR:**
- ✅ **Bueno:** Tema claro/oscuro, idioma, guardar preferencias, atajos personalizables
- ❌ **Malo:** Interfaz rígida igual para todos, no recuerda configuración

**EJEMPLOS PRÁCTICOS (TravelEase):**

✅ **Cumple Principio 7:**

**Personalización de preferencias:**
- **Guardar filtros:** "Recordar estos filtros para próximas búsquedas"
- **Presets de búsqueda:** Guardar búsqueda como "Mis viajes en familia" (con filtros: apto niños, presupuesto €3000, etc.)
- **Historial:** Mostrar últimas 5 búsquedas para repetir rápidamente
- **Moneda preferida:** Elegir € vs. $ vs. £
- **Idioma:** Español, English, Français

**Adaptación a usuario:**
- **Detectar nivel:** Si usuario usa filtros avanzados frecuentemente → Mostrar "Modo experto" por defecto
- **Recordar dispositivo:** Si siempre busca desde móvil → Optimizar para móvil
- **Sugerencias personalizadas:** Basadas en búsquedas anteriores

**Configuración de UI:**
- **Tema claro/oscuro**
- **Tamaño de fuente:** Pequeño / Medio / Grande (accesibilidad)
- **Densidad de información:** Compacto vs. Espaciado
- **Ordenar filtros:** Drag & drop para poner filtros más usados arriba

❌ **Viola Principio 7:**
- **No guardar preferencias:** Usuario elige € cada vez, sistema no recuerda
- **Sin opciones de UI:** Tema fijo, tamaño de letra fijo
- **Experiencia idéntica para todos:** Laura (experta) y turista senior (novato) ven lo mismo

**TIPOS DE INDIVIDUALIZACIÓN:**

1. **Explícita (usuario configura):**
   - Tema, idioma, moneda
   - Guardar presets de búsqueda
   - Ordenar filtros

2. **Implícita (sistema aprende):**
   - Autocompletado basado en historial
   - Sugerencias basadas en búsquedas previas
   - Detectar nivel de experiencia por comportamiento

3. **Adaptación a contexto:**
   - Móvil → UI simplificada
   - Desktop → UI completa
   - Conexión lenta → Menos imágenes

**PREGUNTAS CLAVE AL LEER:**
1. ¿Cuánta personalización es apropiada? (demasiada puede abrumar)
2. ¿Cuándo personalizar automáticamente vs. dejar que usuario configure?
3. ¿Cómo balancear individualización vs. consistencia para todos?

**TOMA NOTA DE:**
- Diferencia entre adaptabilidad (usuario configura) y adaptatividad (sistema aprende)
- Tipos de preferencias individualizables
- Relación con satisfacción (componente de usabilidad)

---

## 📝 Resumen de los 7 Principios (Tabla de Referencia Rápida)

| # | Principio | Pregunta clave | Ejemplo aplicado a TravelEase |
|---|-----------|----------------|-------------------------------|
| 1 | Adecuación a la tarea | ¿Ayuda a completar la tarea eficientemente? | Filtro "Presupuesto total" (no solo alojamiento) |
| 2 | Autodescripción | ¿La interfaz se explica sola? | Tooltips en iconos, placeholders descriptivos |
| 3 | Conformidad con expectativas | ¿Se comporta como el usuario espera? | Buscador arriba-centro (convención) |
| 4 | Adecuación al aprendizaje | ¿Fácil para novatos, eficiente para expertos? | Progressive disclosure (5 filtros básicos + "Más") |
| 5 | Controlabilidad | ¿El usuario tiene el control? | Deshacer filtros, cancelar búsqueda |
| 6 | Tolerancia a errores | ¿Previene y facilita corrección de errores? | Autocompletado, validación de fechas |
| 7 | Adecuación a individualización | ¿Se adapta a cada usuario? | Guardar preferencias, recordar filtros |

---

## 🔍 Actividad Post-Lectura: Verificación de Comprensión

### Ejercicio 1: Identificar Principios (15 min)

Para cada ejemplo, identifica QUÉ PRINCIPIO cumple o viola:

1. Amazon muestra "Comprar ahora con 1-clic" para usuarios recurrentes.
   - **Principio:** __________
   - **¿Cumple o viola?:** __________
   - **¿Por qué?:** __________

2. Formulario que muestra "*Campo requerido" ANTES de que usuario intente enviar.
   - **Principio:** __________
   - **¿Cumple o viola?:** __________
   - **¿Por qué?:** __________

3. Google permite personalizar tema (claro/oscuro) y recuerda la preferencia.
   - **Principio:** __________
   - **¿Cumple o viola?:** __________
   - **¿Por qué?:** __________

4. App que usa icono de "hamburgesa" (☰) para menú (convención móvil conocida).
   - **Principio:** __________
   - **¿Cumple o viola?:** __________
   - **¿Por qué?:** __________

5. Photoshop tiene atajos de teclado para expertos pero también botones visuales para novatos.
   - **Principio:** __________
   - **¿Cumple o viola?:** __________
   - **¿Por qué?:** __________

*(Respuestas al final)*

---

### Ejercicio 2: Análisis de Interfaz Real (15 min)

Abre Booking.com y analiza su buscador de hoteles:

| Principio | ¿Cumple? (Sí/No/Parcial) | Evidencia | Puntuación (1-5) |
|-----------|--------------------------|-----------|------------------|
| 1. Adecuación a tarea | | | |
| 2. Autodescripción | | | |
| 3. Conformidad expectativas | | | |
| 4. Adecuación aprendizaje | | | |
| 5. Controlabilidad | | | |
| 6. Tolerancia a errores | | | |
| 7. Individualización | | | |
| **TOTAL** | | | __/35 |

---

## ✅ Checklist: ¿Estás Listo para el Lab?

Antes de la sesión presencial, deberías poder responder SÍ a:

- [ ] Puedo **enumerar** los 7 principios de memoria
- [ ] Puedo **explicar** cada principio con 1 ejemplo concreto
- [ ] Puedo **identificar** qué principio cumple/viola una interfaz dada
- [ ] Entiendo la diferencia entre los 7 principios (no los confundo)
- [ ] Sé cómo aplicar cada principio a TravelEase específicamente
- [ ] Completé el análisis comparativo (Booking, Airbnb, Skyscanner)
- [ ] Pasé el quiz con mínimo 70%
- [ ] Redacté informe de lectura previa (2.5-3 páginas)

---

## 📚 Lecturas Complementarias (Opcionales)

Si quieres profundizar:

**1. Nielsen, J. (2020). 10 Usability Heuristics for User Interface Design.**
- Similar a ISO 9241-110 pero más divulgativo
- Ejemplos visuales excelentes
- URL: https://www.nngroup.com/articles/ten-usability-heuristics/

**2. Shneiderman, B. & Plaisant, C. (2016). Designing the User Interface (Cap. 2: Guidelines)**
- Capítulo sobre principios de diseño
- Más profundo que ISO, menos formal

**3. ISO 9241-11:2018 (del Lab 1)**
- Revisar relación entre principios de diálogo y usabilidad
- ¿Cómo los 7 principios mejoran efectividad, eficiencia, satisfacción?

---

## 🤔 Preguntas Frecuentes

**P: ¿Debo memorizar las definiciones exactas del estándar?**
R: NO. Entiende el CONCEPTO, no memorices palabra por palabra. En el lab aplicarás los principios, no recitarás definiciones.

**P: ¿Qué pasa si dos principios entran en conflicto?**
R: ¡Es común! Ejemplo: Adecuación a tarea (muchas opciones) vs. Adecuación a aprendizaje (simplicidad). Documenta el conflicto y justifica tu decisión. No hay respuesta única.

**P: ¿Los principios aplican SOLO a web/móvil?**
R: NO. Aplican a CUALQUIER interfaz interactiva: web, móvil, desktop, voz (Alexa), táctil (cajeros), etc.

**P: ¿Debo leer los anexos del estándar?**
R: Opcional. Los anexos tienen ejemplos adicionales que pueden inspirarte, pero no son esenciales para el lab.

---

## 📊 Respuestas a Ejercicio 1

1. **Principio 1: Adecuación a la tarea** | Cumple | Elimina pasos innecesarios para usuarios recurrentes, hace tarea más eficiente
2. **Principio 2: Autodescripción** | Cumple | Explica qué campos son requeridos antes de intentar enviar
3. **Principio 7: Individualización** | Cumple | Permite personalizar y recuerda preferencia del usuario
4. **Principio 3: Conformidad con expectativas** | Cumple | Sigue convención móvil establecida (☰ = menú)
5. **Principio 4: Adecuación al aprendizaje** | Cumple | Atajos para expertos (eficientes), botones para novatos (fácil aprender)

---

**¡Buena suerte con la lectura! 📖**

*Recuerda: El objetivo NO es memorizar, sino ENTENDER para APLICAR en el laboratorio.*

**Tiempo total estimado:** 90 minutos  
**Resultado esperado:** Comprensión sólida de los 7 principios lista para aplicar en diseño de TravelEase
