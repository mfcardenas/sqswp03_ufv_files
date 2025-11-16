# Prompts de IA para Laboratorio 2: Diseño de Interfaz de Búsqueda

## 📋 Guía de Uso

Este documento contiene **prompts probados y optimizados** para generar diseños de interfaz de búsqueda que cumplan con los 7 principios de ISO 9241-110.

### Herramientas Recomendadas

| Herramienta | URL | Qué genera | Mejor para |
|-------------|-----|------------|------------|
| **v0.dev** | https://v0.dev | Código React + UI visual | Resultados rápidos y profesionales |
| **ChatGPT-4** | https://chat.openai.com | HTML/CSS/JS + explicaciones | Iteración y ajustes detallados |
| **Claude** | https://claude.ai | Wireframes + código | Análisis crítico de diseños |
| **Gemini** | https://gemini.google.com | Código + imágenes | Generación de variaciones |

### Estructura de los Prompts

Cada prompt incluye:
- ✅ **Contexto** (qué es TravelEase)
- ✅ **Requisitos por principio ISO 9241-110** (los 7)
- ✅ **Personas objetivo** (del Lab 1)
- ✅ **Funcionalidades específicas**
- ✅ **Formato de salida deseado**

---

## 🎨 Prompt Base: Diseño Completo de Búsqueda

### Versión 1: Para v0.dev (React)

```
Diseña una interfaz de búsqueda de experiencias turísticas para TravelEase, 
una plataforma que permite encontrar y reservar actividades, tours, 
alojamientos y experiencias gastronómicas en destinos turísticos.

REQUISITOS POR PRINCIPIO ISO 9241-110:

1. ADECUACIÓN A LA TAREA
   - Filtro de presupuesto TOTAL combinado (alojamiento + actividades + transporte)
   - Opción "Búsqueda rápida" con mínimos campos para usuarios con prisa
   - Toggle "Fechas flexibles (±3 días)" para viajeros con flexibilidad
   - Mostrar SOLO información relevante en resultados (precio, duración, 
     valoración, tipo de experiencia)

2. AUTODESCRIPCIÓN
   - Todos los iconos DEBEN tener tooltips explicativos
   - Placeholders descriptivos en campos de texto (ej: "¿A dónde quieres ir? 
     (París, Bali, Tokio...)")
   - Labels claros en todos los filtros
   - Contador de resultados visible: "X experiencias encontradas"
   - Mensajes de estado claros (ej: "Buscando...", "Filtros aplicados: 3")

3. CONFORMIDAD CON EXPECTATIVAS DEL USUARIO
   - Barra de búsqueda en la parte SUPERIOR CENTRAL (patrón estándar)
   - Filtros en SIDEBAR IZQUIERDO (como Amazon, Booking)
   - Botón de búsqueda en COLOR DESTACADO (azul o verde)
   - Logo en esquina superior izquierda, clickable para volver a home
   - Resultados en CARDS con imagen prominente (patrón de e-commerce)

4. ADECUACIÓN AL APRENDIZAJE
   - 5 filtros básicos visibles inicialmente
   - Botón "Más filtros" para opciones avanzadas (progressive disclosure)
   - Tooltips con ejemplos: "Presupuesto total: Incluye alojamiento, 
     transporte y actividades"
   - Opcional: Mini tutorial en primera visita (puede ser un lightbox dismissable)

5. CONTROLABILIDAD
   - Botón "Limpiar todos los filtros" visible
   - Cada filtro aplicado muestra un "x" para quitarlo individualmente
   - Dropdown para ordenar resultados (Relevancia, Precio ↑↓, Valoración, 
     Más recientes)
   - Botón "Guardar esta búsqueda" (icono de estrella)
   - Navegación breadcrumb si aplica

6. TOLERANCIA A ERRORES
   - Autocompletado en campo de destino (previene typos)
   - Validación en tiempo real: Si fecha de vuelta < fecha de ida, mostrar 
     mensaje: "La fecha de vuelta debe ser posterior a la de ida"
   - Si no hay resultados, sugerir: "Intenta ampliar fechas o aumentar 
     presupuesto"
   - Confirmación antes de borrar filtros: "¿Limpiar todos los filtros?"
   - NO perder datos del formulario si usuario navega atrás

7. ADECUACIÓN A INDIVIDUALIZACIÓN
   - Checkbox "Recordar mis preferencias de filtros"
   - Opción "Guardar búsqueda" para repetirla después
   - Mostrar historial de búsquedas recientes (últimas 3-5)
   - Permitir ordenar filtros por preferencia del usuario (drag & drop)

USUARIOS OBJETIVO (del Lab 1):

Persona 1 - Laura García (24 años, mochilera):
- Busca experiencias auténticas, no turísticas
- Presupuesto limitado (€800 total)
- Usa principalmente MÓVIL (iPhone)
- Muy tech-savvy (★★★★★)
- Prioridad: Precio bajo + autenticidad

Persona 2 - Familia Rodríguez (padres 35-38, hijos 5 y 8 años):
- Necesita ver servicios INFANTILES claramente
- Presupuesto medio-alto (€3000)
- Usa TABLET principalmente
- Tech-savvy medio (★★★☆☆)
- Prioridad: Seguridad + servicios para niños

Persona 3 - David Chen (35 años, viajero de negocios):
- Viaja frecuentemente por trabajo
- Necesita FLEXIBILIDAD de cancelación
- Presupuesto alto (empresa paga)
- Usa LAPTOP
- Muy tech-savvy (★★★★★)
- Prioridad: Velocidad + flexibilidad

FUNCIONALIDADES ESPECÍFICAS:

Búsqueda:
- Campo de texto con autocompletado de destinos populares
- Sugerencias basadas en: popularidad, temporada, historial del usuario

Filtros Básicos (siempre visibles):
1. Destino (campo de texto con autocompletado)
2. Fechas (date picker con opción "Flexibles ±3 días")
3. Presupuesto (slider de rango, €0-€5000)
4. Tipo de experiencia (dropdown: Cultural, Aventura, Gastronómica, 
   Naturaleza, Relax, Urbana)
5. Valoración mínima (estrellas clickables: ★★★★★)

Filtros Avanzados (bajo "Más filtros"):
6. Duración (horas/días)
7. Idioma del guía
8. Tamaño del grupo (individual, pequeño <10, mediano 10-30, grande >30)
9. Accesibilidad (silla de ruedas, visual, auditiva)
10. Servicios especiales (infantil, mascotas, vegetariano, etc.)
11. Cancelación gratuita (toggle)
12. Incluye transporte (toggle)
13. Oferta/descuento (toggle)
14. Certificados/premios (eco-friendly, etc.)
15. Nivel de actividad física (bajo, medio, alto)

Visualización de Resultados:
- Cards con:
  * Imagen principal (ratio 16:9)
  * Título de la experiencia (máx 60 caracteres)
  * Tipo de experiencia (badge de color)
  * Duración (icono reloj + texto)
  * Precio total por persona (destacado, grande)
  * Valoración (estrellas + número de reseñas)
  * Badge especial si aplica ("Experiencia auténtica", "Cancelación gratis", 
    "Apto niños")
  * Botón "Ver detalles" + icono de corazón (guardar)

Ordenamiento:
- Por relevancia (default)
- Precio: menor a mayor
- Precio: mayor a menor
- Valoración: mayor a menor
- Más recientes

Responsive:
- Desktop (>1024px): Filtros en sidebar, resultados en grid 3 columnas
- Tablet (768-1024px): Filtros colapsables, grid 2 columnas
- Móvil (<768px): Filtros en modal, lista vertical 1 columna

FORMATO DE SALIDA:

Genera código React con Tailwind CSS (si usas v0.dev) o HTML/CSS/JavaScript 
puro funcional. 

Incluye:
- Componente completo de búsqueda
- Estados interactivos (hover, focus, active)
- Validaciones de formulario
- Responsive design (mobile-first)
- Comentarios explicando qué principio ISO cumple cada elemento

IMPORTANTE:
- Diseño limpio y profesional (inspirado en Booking, Airbnb, pero NO copiar)
- Colores: Paleta cálida para turismo (naranjas, azules, verdes)
- Tipografía legible (sans-serif, tamaño mínimo 14px)
- Espaciado generoso (no saturar)
- Accesibilidad: Contraste WCAG AA mínimo
```

---

### Versión 2: Para ChatGPT/Claude (HTML/CSS/JS)

```
Actúa como un diseñador de UX/UI experto especializado en cumplimiento de 
estándares ISO 9241-110 (Principios de diálogo).

Tu tarea: Diseñar la interfaz de búsqueda de experiencias turísticas para 
TravelEase.

CONTEXTO:
TravelEase es una plataforma web/móvil que permite a usuarios buscar y 
reservar experiencias turísticas (tours, actividades, alojamientos, 
gastronomía) en destinos específicos. Compite con Booking, Airbnb 
Experiences y GetYourGuide.

REQUISITOS POR PRINCIPIO ISO 9241-110:

[... copiar los mismos requisitos de Versión 1 ...]

FORMATO DE SALIDA:

1. Descripción textual del diseño (wireframe verbal)
2. Código HTML semántico
3. CSS con diseño responsive (mobile-first)
4. JavaScript para interactividad (validaciones, filtros)
5. Comentarios explicando QUÉ PRINCIPIO ISO cumple cada decisión de diseño

Ejemplo de comentario esperado:
<!-- PRINCIPIO 2: Autodescripción - Tooltip explica qué incluye "Presupuesto total" -->
<div class="filter">
  <label for="budget">Presupuesto total</label>
  <span class="tooltip">ℹ️ Incluye alojamiento, transporte y actividades</span>
  <input type="range" id="budget" min="0" max="5000">
</div>
```

---

## 🔄 Prompts de Refinamiento (Iteraciones)

**Usa estos prompts DESPUÉS de la primera generación para mejorar el diseño.**

### Iteración 1: Mejorar Autodescripción (Principio 2)

```
El diseño anterior cumple bien la mayoría de principios, pero necesita 
mejorar en AUTODESCRIPCIÓN (Principio 2 de ISO 9241-110).

Por favor, ajusta el diseño para:

1. Agregar tooltips en TODOS los iconos
   - Icono de calendario → "Selecciona fechas de tu viaje"
   - Icono de estrella → "Guardar esta búsqueda para más tarde"
   - Icono de ordenamiento → "Cambia cómo se ordenan los resultados"

2. Mejorar placeholders en campos de texto
   - Actual: "Destino"
   - Mejor: "¿A dónde quieres ir? (ej: París, Bali, Tokio)"

3. Agregar mensajes de estado visibles
   - "Buscando experiencias..." (mientras carga)
   - "234 experiencias encontradas" (después de buscar)
   - "Filtros aplicados: Presupuesto (€0-€800), Tipo (Cultural)" (resumen)

4. Explicar filtros complejos con texto de ayuda
   - Filtro "Presupuesto total": Agregar texto pequeño "Incluye alojamiento, 
     transporte y actividades"
   - Filtro "Fechas flexibles": Explicar "Buscaremos 3 días antes y 3 días 
     después de tus fechas"

Mantén el resto del diseño igual, solo mejora estos aspectos de autodescripción.
```

---

### Iteración 2: Evitar Estereotipos y Genericidad

```
El diseño es demasiado genérico. Por favor, hazlo más ESPECÍFICO para el 
caso de TravelEase y las 3 personas identificadas:

PERSONA 1 - Laura (mochilera, €800, móvil):
- Agregar badge "Experiencia auténtica" en resultados (ella odia lo turístico)
- Filtro "Solo experiencias locales" (toggle)
- En resultados, mostrar "Precio por persona" muy destacado (su prioridad #1)

PERSONA 2 - Familia Rodríguez (niños 5 y 8 años, tablet):
- Agregar icono de "familia" en resultados que son aptos para niños
- Filtro "Apto para niños" debe estar en los 5 básicos (no escondido)
- Mostrar edad mínima recomendada en resultados: "Desde 5 años"

PERSONA 3 - David (negocios, laptop, flexibilidad):
- Badge "Cancelación gratuita" MUY visible (su prioridad)
- Filtro "Cancelación flexible" en los 5 básicos
- Opción de ordenar por "Más flexible primero"

Además, usa lenguaje más cálido y humano:
- En vez de "No se encontraron resultados"
- Usa "¡Ups! No encontramos experiencias con estos filtros. ¿Intentamos 
  ampliar las fechas o el presupuesto?"

Ajusta el diseño para que sea menos corporativo y más cercano.
```

---

### Iteración 3: Mejorar Conformidad con ISO 9241-110

```
Revisemos el cumplimiento de los 7 principios. Ajusta lo siguiente:

PRINCIPIO 1 - Adecuación a la tarea:
- Problema: Hay demasiados campos obligatorios en búsqueda inicial
- Solución: Solo pedir DESTINO y FECHAS inicialmente, el resto es opcional

PRINCIPIO 4 - Adecuación al aprendizaje:
- Problema: No hay ayuda para usuarios novatos
- Solución: Agregar botón "?" en esquina que abre tutorial rápido (30 seg)

PRINCIPIO 5 - Controlabilidad:
- Problema: No hay forma de deshacer filtros uno por uno
- Solución: Cada filtro aplicado debe mostrar un chip con "x" para quitarlo
  Ejemplo: [Presupuesto: €0-€800 ✕] [Cultural ✕] [Valoración 4+ ✕]

PRINCIPIO 6 - Tolerancia a errores:
- Problema: Si usuario pone fecha de vuelta antes de ida, no hay validación
- Solución: Validar en tiempo real y mostrar mensaje amigable:
  "🤔 La fecha de vuelta (12 mayo) es antes de la fecha de ida (15 mayo). 
  ¿Quieres intercambiarlas?"

PRINCIPIO 7 - Individualización:
- Problema: No hay forma de guardar preferencias
- Solución: Agregar checkbox "Recordar estos filtros para próximas búsquedas"

Implementa estas mejoras manteniendo el resto del diseño.
```

---

### Iteración 4: Mejorar Narrativa y Escenario

```
El diseño funciona pero carece de narrativa de uso. Ajústalo pensando en 
estos escenarios REALES:

ESCENARIO 1 - Laura buscando escapada de fin de semana:
Es viernes 23:45h. Laura acaba de terminar un proyecto estresante y ve un 
Reel de Instagram sobre Oporto. Busca en Google "experiencias auténticas 
oporto baratas" y llega a TravelEase.

Su flujo debe ser:
1. Buscar "Oporto" (autocompletado ayuda)
2. Fechas flexibles próximo fin de semana
3. Presupuesto máx €800
4. Filtro "Experiencias auténticas"
5. Ver resultados en 10 segundos
6. Ordenar por precio
7. Guardar 3 favoritas
8. Comparar

Diseña pensando: ¿Cómo hacer que Laura complete esto en <5 minutos desde móvil 
a las 23:45h con mala iluminación y cansada?

ESCENARIO 2 - Familia Rodríguez planificando vacaciones de verano:
Domingo 11:00h. Padres e hijos de 5 y 8 años sentados en sofá con tablet. 
Quieren ir a Málaga en julio pero no saben qué hacer con los niños.

Su flujo:
1. Buscar "Málaga"
2. Fechas: 10-17 julio
3. Filtro "Apto para niños" → Solo mostrar opciones relevantes
4. Ver qué actividades hay para cada edad
5. Padres quieren asegurarse de seguridad → Ver valoraciones y comentarios
6. Niños miran imágenes → Deben ser atractivas visualmente
7. Guardar 10+ opciones para decidir después

Diseña pensando: ¿Cómo hacer que la familia explore MUCHAS opciones sin 
perderse, en tablet con niños mirando?

ESCENARIO 3 - David reservando actividad de última hora:
Martes 14:30h. David está en avión a Barcelona, aterriza en 3 horas. Quiere 
reservar cena + tour nocturno para esa misma noche.

Su flujo:
1. Búsqueda rápida: "Barcelona"
2. Fechas: HOY
3. Filtro: "Disponible hoy" + "Cancelación gratis"
4. Ordenar por "Más cercano al centro"
5. Reservar en <2 minutos

Diseña pensando: ¿Cómo hacer que David reserve en <3 minutos desde móvil en 
avión con WiFi inestable?

Ajusta el diseño para que ESTOS TRES ESCENARIOS funcionen fluidamente. 
Prioriza velocidad, claridad y bajo uso de datos móviles.
```

---

## 🎯 Prompts Especializados por Tipo de Diseño

### Prompt A: Diseño Minimalista (Novatos, Móvil-First)

```
Diseña una interfaz de búsqueda MINIMALISTA para TravelEase, optimizada para:

PÚBLICO OBJETIVO: Usuarios novatos en apps de viajes, principalmente móvil

FILOSOFÍA: "Menos es más"
- Solo 3-4 filtros visibles
- Mucho espacio en blanco
- Tipografía grande (mínimo 16px)
- Iconos + texto (no solo iconos)

INSPIRACIÓN: Google (buscador simple), Apple (diseño limpio)

FILTROS BÁSICOS (solo estos visibles):
1. Destino
2. Fechas
3. Presupuesto
4. Tipo de experiencia

TODO LO DEMÁS bajo "Más opciones" (colapsado por defecto)

RESULTADOS:
- Cards grandes (fácil de tocar en móvil)
- Solo 3 datos por card: Imagen, Título, Precio
- "Ver más" para expandir detalles

PRIORIDAD: Facilidad de aprendizaje >>> Funcionalidad avanzada

Genera código HTML/CSS mobile-first (max-width: 375px base).
```

---

### Prompt B: Diseño Power User (Expertos, Desktop)

```
Diseña una interfaz de búsqueda AVANZADA para TravelEase, optimizada para:

PÚBLICO OBJETIVO: Usuarios expertos que buscan frecuentemente, principalmente 
desktop

FILOSOFÍA: "Máximo control y eficiencia"
- TODOS los filtros visibles (15+)
- Atajos de teclado
- Búsqueda avanzada con operadores
- Vistas múltiples (grid, lista, mapa)

INSPIRACIÓN: Amazon (filtros completos), Booking (opciones detalladas)

FUNCIONALIDADES AVANZADAS:
- Multi-select en filtros (seleccionar 3 tipos de experiencia a la vez)
- Rangos numéricos con inputs directos (no solo sliders)
- Guardar búsquedas con nombre personalizado
- Comparación lado a lado (hasta 4 experiencias)
- Exportar resultados a PDF/Excel

RESULTADOS:
- Vista de tabla con todas las columnas editables
- Ordenamiento por múltiples criterios (precio + valoración)
- Selección múltiple para comparar
- Vista previa rápida en hover (sin clic)

PRIORIDAD: Velocidad y control >>> Simplicidad

Genera código con MUCHAS opciones, asumiendo usuario experto que sabe lo que 
busca.
```

---

### Prompt C: Diseño Híbrido (Balance, Responsive)

```
Diseña una interfaz de búsqueda BALANCEADA para TravelEase que:

OBJETIVO: Funcionar para TODOS (novatos y expertos, móvil y desktop)

ESTRATEGIA: Progressive disclosure
- Interfaz simple por defecto (5 filtros básicos)
- Opciones avanzadas disponibles con 1 clic
- Detectar nivel de experiencia y adaptar (opcional)

NIVELES DE COMPLEJIDAD:

Nivel 1 - Vista Simple (default):
- 5 filtros básicos
- Resultados en cards simples
- Lenguaje muy claro

Nivel 2 - Vista Intermedia (botón "Más opciones"):
- 10 filtros
- Ordenamiento avanzado
- Comparación básica

Nivel 3 - Vista Avanzada (botón "Modo experto"):
- 15+ filtros
- Multi-criterio
- Exportación

RESPONSIVE:
- Móvil (<768px): Solo Nivel 1
- Tablet (768-1024px): Niveles 1-2
- Desktop (>1024px): Niveles 1-3

Genera código que ADAPTE la UI según tamaño de pantalla y (opcionalmente) 
comportamiento del usuario.
```

---

## 💡 Prompts de Solución a Problemas Comunes

### Problema: IA genera diseño muy genérico

```
El diseño que generaste es demasiado genérico (parece cualquier buscador).

Por favor, hazlo ESPECÍFICO para TravelEase incluyendo:

1. Personalidad de marca única:
   - Lenguaje: Cálido, aventurero, inspirador
   - Tono: "Descubre tu próxima aventura" vs. "Buscar experiencias"
   - Emojis sutiles: 🌍 🗺️ ✨ (sin exagerar)

2. Diferenciadores vs. competencia:
   - TravelEase se enfoca en EXPERIENCIAS AUTÉNTICAS (no masivas)
   - Badge visible: "Verificado por locales" 
   - Filtro único: "Solo experiencias pequeños grupos (<10 personas)"

3. Detalles específicos del dominio turismo:
   - Mostrar clima en destino (icono sol/lluvia)
   - Indicar temporada alta/baja (precio varía)
   - "Mejor época para visitar" en cada destino

4. Elementos emocionales:
   - Frases inspiradoras: "234 aventuras esperándote en París"
   - Fotos de PERSONAS disfrutando (no solo lugares)
   - Testimonios cortos en resultados: "¡Inolvidable!" - María

Rediseña agregando estos elementos específicos.
```

---

### Problema: Diseño viola principios de usabilidad

```
Detecto violaciones de ISO 9241-110 en el diseño:

VIOLACIÓN 1 - Principio 2 (Autodescripción):
Hay 5 iconos sin tooltip ni label. Usuario novato no entenderá.
Solución: Agregar texto descriptivo o tooltip en TODOS los iconos.

VIOLACIÓN 2 - Principio 6 (Tolerancia a errores):
Si usuario introduce "pari" en buscador, no hay autocompletado.
Solución: Implementar fuzzy search que sugiera "París".

VIOLACIÓN 3 - Principio 5 (Controlabilidad):
Una vez aplicados filtros, no hay forma de ver cuáles están activos.
Solución: Mostrar chips de filtros aplicados: [Cultural ✕] [€0-€800 ✕]

VIOLACIÓN 4 - Principio 1 (Adecuación a tarea):
Pide email y teléfono ANTES de mostrar resultados. Innecesario.
Solución: Solo pedir esos datos al RESERVAR, no al buscar.

Por favor, corrige estas violaciones manteniendo el resto del diseño.
```

---

### Problema: Diseño no es responsive

```
El diseño funciona en desktop pero se rompe en móvil. Necesito:

MÓVIL (<768px):
- Buscador full-width
- Filtros en modal flotante (botón "Filtrar resultados")
- Resultados en lista vertical (1 columna)
- Cards más simples (menos info visible inicialmente)
- Botón de "Filtros" sticky en bottom

TABLET (768-1024px):
- Filtros en panel colapsable superior
- Resultados en grid 2 columnas
- Tocado con dedo, no mouse hover

DESKTOP (>1024px):
- Filtros en sidebar izquierdo
- Resultados en grid 3 columnas
- Interacciones con mouse (hover states)

Usa Tailwind CSS o media queries para hacer el diseño 100% responsive.

IMPORTANTE: Mobile-first (diseña primero para móvil, luego escala a desktop).
```

---

## 🧪 Prompt de Evaluación de Diseño

**Usa este prompt para que la IA evalúe tu diseño:**

```
Actúa como un auditor de usabilidad experto en ISO 9241-110.

Evalúa el siguiente diseño de interfaz de búsqueda según los 7 principios 
de diálogo:

[PEGA AQUÍ TU DISEÑO: Código HTML/CSS o descripción detallada]

Para cada principio, proporciona:

1. Puntuación (1-5 estrellas)
2. Justificación (¿qué cumple? ¿qué no?)
3. Evidencia específica (señala elementos concretos)
4. Mejoras sugeridas (3 acciones concretas)

Formato de salida:

PRINCIPIO 1: ADECUACIÓN A LA TAREA
Puntuación: ⭐⭐⭐☆☆ (3/5)

Cumple:
- Filtro de presupuesto total visible (bueno)
- Búsqueda rápida con pocos campos (excelente)

No cumple:
- Pide información innecesaria (ciudad de origen) antes de mostrar resultados
- Proceso de reserva tiene 7 pasos (muy largo)

Evidencia:
[Línea 45-50 del HTML: Campo "Ciudad de origen" marcado como required]

Mejoras sugeridas:
1. Quitar campo "Ciudad de origen" del formulario inicial
2. Reducir pasos de reserva de 7 a 3 (búsqueda → selección → pago)
3. Agregar opción "Reserva express" para usuarios recurrentes

---

[Continuar con los 7 principios...]

PUNTUACIÓN TOTAL: 23/35 (66%)

VEREDICTO GENERAL:
El diseño cumple parcialmente con ISO 9241-110. Principales fortalezas: 
autodescripción y conformidad con expectativas. Principales debilidades: 
exceso de pasos (adecuación a tarea) y falta de personalización (individualización).

PRIORIDAD DE MEJORAS:
1. [Alta] Reducir campos obligatorios en búsqueda inicial
2. [Alta] Agregar validación de fechas
3. [Media] Implementar opciones de personalización
4. [Media] Mejorar tooltips en filtros avanzados
5. [Baja] Agregar tutorial para novatos
```

---

## 📚 Biblioteca de Componentes Específicos

### Prompt: Buscador con Autocompletado

```
Genera solo el componente de BUSCADOR de destinos para TravelEase con:

Funcionalidades:
- Campo de texto con icono de lupa
- Autocompletado de destinos populares (París, Tokio, Bali, Barcelona...)
- Sugerencias basadas en: popularidad + temporada + historial usuario
- Corrección de typos: "pari" → sugiere "París"
- Muestra bandera del país + nombre de ciudad
- Placeholder: "¿A dónde quieres ir? (ej: París, Bali, Tokio)"

Cumplimiento ISO 9241-110:
- Principio 2: Labels claros, placeholder descriptivo
- Principio 6: Autocompletado previene errores de typo

Código: HTML + CSS + JavaScript (sin frameworks)
```

---

### Prompt: Sistema de Filtros con Progressive Disclosure

```
Genera solo el componente de FILTROS para TravelEase con:

Estructura:
- 5 filtros básicos siempre visibles:
  1. Fechas (date picker)
  2. Presupuesto (range slider €0-€5000)
  3. Tipo de experiencia (dropdown)
  4. Valoración mínima (estrellas)
  5. Servicios especiales (checkboxes: infantil, accesibilidad)

- Botón "Más filtros" que expande 10 filtros adicionales

Funcionalidades:
- Cada filtro aplicado muestra chip con "✕" para quitar
- Contador: "3 filtros aplicados"
- Botón "Limpiar todos" (con confirmación)
- Guardar filtros como preset: "Mis viajes familiares"

Cumplimiento ISO 9241-110:
- Principio 4: Progressive disclosure (novatos ven simple, expertos expanden)
- Principio 5: Controlabilidad (quitar filtros individualmente)
- Principio 7: Individualización (guardar presets)

Código: React + Tailwind CSS
```

---

### Prompt: Card de Resultado Optimizada

```
Genera solo el componente de CARD de resultado para una experiencia turística:

Contenido visible:
- Imagen (ratio 16:9, lazy loading)
- Badge de tipo (Cultural, Aventura, etc.) - color-coded
- Título (máx 60 caracteres, truncar con "...")
- Duración (icono reloj + "3 horas" o "2 días")
- Precio por persona (grande, destacado) + "por persona"
- Valoración (★★★★☆ + "124 reseñas")
- Badges especiales si aplica:
  * "Cancelación gratis"
  * "Apto niños"
  * "Experiencia auténtica"
- Botón "Ver detalles"
- Icono de corazón (guardar favorito)

Interacciones:
- Hover: Mostrar preview rápido (snippet descripción + incluye/no incluye)
- Click en corazón: Guardar sin salir de resultados
- Click en card: Ir a página de detalles

Responsive:
- Desktop: 300px ancho
- Tablet: 350px ancho
- Móvil: Full width, layout vertical

Cumplimiento ISO 9241-110:
- Principio 1: Solo info relevante visible
- Principio 2: Labels claros ("por persona", "124 reseñas")
- Principio 3: Patrón familiar (similar a e-commerce)

Código: HTML + CSS + JS (componente reutilizable)
```

---

## ✅ Checklist de Calidad de Prompts

Antes de enviar un prompt, verifica:

- [ ] Incluye CONTEXTO (qué es TravelEase)
- [ ] Especifica los 7 principios ISO 9241-110
- [ ] Menciona las 3 personas del Lab 1
- [ ] Lista funcionalidades específicas (no solo "hacer búsqueda")
- [ ] Indica formato de salida (HTML, React, wireframe, etc.)
- [ ] Especifica responsive (móvil, tablet, desktop)
- [ ] Pide comentarios explicando qué principio cumple cada elemento
- [ ] Usa ejemplos concretos (no "mostrar resultados", sino "234 experiencias encontradas")
- [ ] Lenguaje claro y estructurado (listas, tablas)
- [ ] Incluye restricciones (qué NO hacer)

---

## 🎯 Ejemplos de Conversación Exitosa con IA

### Ejemplo 1: v0.dev (generación rápida)

**Usuario:**
```
[Pega Prompt Base - Versión 1]
```

**v0.dev:**
```
[Genera código React + preview visual]
```

**Usuario (iteración 1):**
```
Mejora la autodescripción: agrega tooltips en los 3 iconos de la barra 
superior (buscar, favoritos, usuario)
```

**v0.dev:**
```
[Actualiza código con tooltips]
```

**Usuario (iteración 2):**
```
El filtro de presupuesto no es claro. Cambia label "Budget" → "Presupuesto 
total" y agrega texto pequeño debajo: "Incluye alojamiento, transporte y 
actividades"
```

**v0.dev:**
```
[Actualiza código]
```

**Usuario (validación final):**
```
Perfecto. Ahora genera versión móvil (<768px) donde los filtros estén en un 
modal flotante activado por botón "Filtrar resultados"
```

**v0.dev:**
```
[Genera versión responsive]
```

**Total de iteraciones:** 4  
**Tiempo:** ~15 minutos  
**Resultado:** Diseño completo responsive que cumple 30/35 en ISO 9241-110

---

### Ejemplo 2: ChatGPT-4 (análisis crítico)

**Usuario:**
```
[Pega código HTML/CSS generado por v0.dev]

Actúa como auditor ISO 9241-110. Evalúa este diseño según los 7 principios 
y dame puntuación + mejoras.
```

**ChatGPT:**
```
EVALUACIÓN ISO 9241-110:

PRINCIPIO 1 - Adecuación a la tarea: ⭐⭐⭐⭐☆ (4/5)
Cumple bien: Filtros relevantes, búsqueda rápida
No cumple: Campo "email" antes de ver resultados (innecesario)
Mejora: Quitar email del formulario inicial

[... continúa con los 7 principios ...]

TOTAL: 28/35 (80%)
```

**Usuario:**
```
Implementa las 3 mejoras de prioridad ALTA que sugeriste. Dame código actualizado.
```

**ChatGPT:**
```
[Código mejorado con las 3 mejoras]

CAMBIOS APLICADOS:
1. ✅ Eliminado campo email (línea 45 removida)
2. ✅ Agregada validación de fechas (líneas 78-85)
3. ✅ Implementados chips de filtros activos (líneas 120-135)
```

**Usuario:**
```
Perfecto. Ahora genera documentación: para cada sección del código, explica 
qué principio ISO cumple y por qué.
```

**ChatGPT:**
```
[Código comentado extensamente]

<!-- PRINCIPIO 2: Autodescripción -->
<!-- Tooltip explica qué incluye "Presupuesto total" sin requerir 
documentación externa -->
<div class="filter-tooltip">
  <span class="info-icon">ℹ️</span>
  <div class="tooltip-text">
    Incluye alojamiento, transporte y actividades
  </div>
</div>

[... continúa ...]
```

**Total de iteraciones:** 3  
**Tiempo:** ~25 minutos  
**Resultado:** Diseño mejorado a 32/35 + documentación completa

---

## 🚀 Consejos para Prompts Efectivos

### ✅ DO (Haz)

1. **Sé específico:** "Agregar tooltip en icono de favoritos" > "Mejorar UI"
2. **Usa ejemplos:** "Placeholder: '¿A dónde...?' " > "Placeholder claro"
3. **Menciona principios:** "Para cumplir Principio 2..." > "Mejorar"
4. **Itera paso a paso:** 1 mejora a la vez > 10 mejoras juntas
5. **Pide justificaciones:** "Explica qué principio cumple X"
6. **Usa formatos estructurados:** Listas, tablas, JSON
7. **Incluye restricciones:** "NO usar modals intrusivos"
8. **Pide evidencia:** "Muestra DÓNDE en el código cumples Principio 5"

### ❌ DON'T (No hagas)

1. ❌ Prompts vagos: "Haz una búsqueda bonita"
2. ❌ Sin contexto: No mencionar TravelEase, personas, principios
3. ❌ Muchas peticiones juntas: 10 cambios en 1 prompt
4. ❌ Sin ejemplos: "Autocompletado" (¿qué debe autocompletar?)
5. ❌ Asumir conocimiento: "Cumple ISO 9241-110" (especifica CÓMO)
6. ❌ Solo código: Sin pedir explicaciones o documentación
7. ❌ No validar: No pedir a la IA que evalúe su propio output
8. ❌ Rendirse en 1ra iteración: Primera respuesta siempre es mejorable

---

## 📈 Métricas de Éxito

Un prompt es exitoso cuando genera diseño que:

- ✅ Cumple mínimo 28/35 puntos (80%) en ISO 9241-110
- ✅ Funciona en móvil, tablet y desktop
- ✅ Está específicamente diseñado para las 3 personas del Lab 1
- ✅ Incluye comentarios explicando qué principio cumple cada elemento
- ✅ Requiere máximo 4-5 iteraciones para alcanzar calidad aceptable
- ✅ Genera código funcional (no solo descripción visual)

---

**¡Buena suerte con el diseño! 🎨**

*Recuerda: La IA es una herramienta poderosa, pero TÚ eres quien entiende los 
principios ISO, las personas y el contexto. Usa la IA para ejecutar tu visión, 
no para que decida por ti.*
