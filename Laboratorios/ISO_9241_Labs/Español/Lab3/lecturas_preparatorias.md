# Laboratorio 3: Evaluación Heurística y Testing de Usabilidad
## Lecturas Preparatorias

### Información del Laboratorio
- **Asignatura:** Interacción Persona-Computador
- **Laboratorio:** Lab 3 - Evaluación de Usabilidad de Airbnb
- **Tiempo de estudio requerido:** 60-90 minutos
- **Modalidad:** Lectura individual previa al laboratorio presencial
- **Materiales:** Este documento + recursos online complementarios

---

## OBJETIVOS DE LAS LECTURAS

Al completar estas lecturas preparatorias, deberás ser capaz de:

✅ **Comprender la norma ISO 9241-11** y sus métricas de usabilidad  
✅ **Conocer los 7 principios ISO 9241-110** para evaluación heurística  
✅ **Distinguir entre métodos cuantitativos y cualitativos** de evaluación  
✅ **Aplicar protocolos estandarizados** de testing de usuarios  
✅ **Interpretar métricas de eficacia, eficiencia y satisfacción** según estándares internacionales  

---

## LECTURA 1: FUNDAMENTOS DE USABILIDAD (ISO 9241-11)

### 1.1 Definición Oficial de Usabilidad

**ISO 9241-11:2018 define usabilidad como:**

> *"La medida en que un producto puede ser usado por usuarios específicos para conseguir objetivos específicos con **efectividad**, **eficiencia** y **satisfacción** en un contexto de uso específico."*

Esta definición establece **4 componentes esenciales:**

🎯 **Usuarios específicos:** No existe "el usuario promedio" - debemos definir claramente quién usará el sistema  
🎯 **Objetivos específicos:** Las tareas concretas que los usuarios quieren completar  
🎯 **Contexto específico:** El entorno, dispositivos y situaciones donde ocurre el uso  
🎯 **Tres métricas medibles:** Efectividad, eficiencia y satisfacción  

### 1.2 Las Tres Métricas Fundamentales

#### **📊 EFECTIVIDAD (¿Se logra el objetivo?)**

**Definición ISO:** "La precisión y completitud con que los usuarios alcanzan objetivos específicos."

**Cómo se mide:**
```
Efectividad = (Tareas completadas exitosamente / Total de tareas intentadas) × 100

Ejemplo:
- 8 de 10 usuarios completaron la búsqueda de hotel
- Efectividad = (8/10) × 100 = 80%
```

**Variaciones de medición:**
- **Efectividad binaria:** Sí/No por tarea
- **Efectividad parcial:** % de subtareas completadas
- **Efectividad cualitativa:** Calidad del resultado obtenido

#### **⚡ EFICIENCIA (¿Cuánto esfuerzo requiere?)**

**Definición ISO:** "Los recursos empleados en relación con la precisión y completitud con que los usuarios alcanzan objetivos."

**Formas de medición:**
```
Eficiencia temporal = Tareas completadas / Tiempo invertido
Eficiencia de errores = Tareas exitosas / Número de errores
Eficiencia cognitiva = Objetivos logrados / Esfuerzo mental percibido

Ejemplo:
- Tiempo promedio: 3 minutos por búsqueda
- Errores promedio: 1.2 por tarea
- Eficiencia = 1 tarea exitosa / 3 min = 0.33 tareas/min
```

**Recursos considerados:**
- **Tiempo:** Duración de tareas
- **Esfuerzo físico:** Clicks, desplazamientos
- **Esfuerzo cognitivo:** Carga mental percibida
- **Recursos técnicos:** Ancho de banda, procesamiento

#### **😊 SATISFACCIÓN (¿Qué opina el usuario?)**

**Definición ISO:** "La libertad de incomodidad y las actitudes positivas hacia el uso del producto."

**Métodos de medición:**
```
Cuantitativos:
- System Usability Scale (SUS): 0-100 puntos
- Escalas Likert: 1-5 o 1-7 puntos
- Net Promoter Score (NPS): -100 a +100

Cualitativos:
- Entrevistas post-tarea
- Observación de expresiones/frustración
- Análisis de comentarios verbales
```

**Dimensiones de satisfacción:**
- **Utilidad percibida:** ¿Cumple necesidades del usuario?
- **Facilidad de uso:** ¿Es simple de operar?
- **Disfrute:** ¿Es agradable usar?
- **Confianza:** ¿Genera seguridad al usuario?

### 1.3 Contexto de Uso en Evaluación

**ISO 9241-11 enfatiza que la usabilidad NO es una propiedad intrínseca del producto, sino que depende del contexto:**

#### **Usuarios**
- **Características:** Edad, experiencia, limitaciones físicas/cognitivas
- **Conocimiento:** Dominio del área, familiaridad tecnológica
- **Motivación:** Voluntario vs. obligatorio, personal vs. laboral

#### **Tareas**
- **Frecuencia:** Diaria, ocasional, única vez
- **Criticidad:** Rutinaria vs. crítica para objetivos del usuario
- **Complejidad:** Simple vs. multi-paso, individual vs. colaborativa

#### **Equipamiento**
- **Hardware:** Desktop, móvil, tablet, dispositivos específicos
- **Software:** Navegadores, sistemas operativos, versiones
- **Red:** Conectividad, velocidad, estabilidad

#### **Ambiente**
- **Físico:** Oficina, hogar, público, móvil
- **Social:** Individual, equipo, con interrupciones
- **Organizacional:** Políticas, tiempo disponible, presión

### 1.4 Aplicación Práctica en el Laboratorio

**En nuestro Lab 3 con Airbnb:**

```
USUARIOS: Estudiantes universitarios (20-25 años)
TAREAS: Búsqueda de alojamiento para viaje personal
CONTEXTO: Aula universitaria, ordenadores compartidos
EQUIPAMIENTO: PCs con navegadores web estándar

Métricas objetivo:
- Efectividad: >85% de tareas completadas
- Eficiencia: <3 minutos por búsqueda básica  
- Satisfacción: >4/5 en escala de facilidad de uso
```

---

## LECTURA 2: PRINCIPIOS DE DIÁLOGO (ISO 9241-110)

### 2.1 Introducción a los Principios de Diálogo

**ISO 9241-110:2020** establece principios fundamentales para el diseño de interfaces que faciliten la interacción eficiente y efectiva entre usuarios y sistemas informáticos.

**¿Qué es un "diálogo" en este contexto?**
> Es la secuencia de interacciones entre el usuario y el sistema para completar una tarea específica.

**Los 7 principios son aplicables a:**
- Interfaces gráficas (GUI)
- Interfaces web y móviles
- Sistemas de línea de comandos
- Interfaces por voz
- Realidad virtual/aumentada

### 2.2 Los Siete Principios Detallados

#### **🎯 PRINCIPIO 1: ADECUACIÓN A LA TAREA**

**Definición:** *"El diálogo es adecuado para una tarea cuando apoya al usuario en la realización eficaz y eficiente de la tarea."*

**Características de interfaces adecuadas:**
- **Información relevante:** Solo datos necesarios para la tarea
- **Funcionalidad específica:** Herramientas apropiadas para objetivos del usuario
- **Flujo natural:** Secuencia lógica de pasos
- **Minimización:** Eliminación de elementos innecesarios

**Ejemplo en Airbnb:**
```
✅ BUENO: Búsqueda prominente en página principal
✅ BUENO: Filtros relevantes (precio, ubicación, fechas)
❌ MALO: Promociones que distraen durante búsqueda urgente
❌ MALO: Información del host antes que disponibilidad
```

**Preguntas de evaluación:**
- ¿Facilita directamente la tarea principal del usuario?
- ¿Elimina pasos innecesarios del proceso?
- ¿Prioriza información crítica sobre secundaria?

#### **📝 PRINCIPIO 2: AUTODESCRIPCIÓN**

**Definición:** *"El diálogo es autodescriptivo cuando cada paso es inmediatamente comprensible a través de retroalimentación del sistema o se explica al usuario bajo petición."*

**Elementos de autodescripción:**
- **Etiquetas claras:** Texto descriptivo en botones y campos
- **Feedback inmediato:** Respuesta visible a acciones del usuario
- **Estados del sistema:** Indicación de progreso, carga, errores
- **Ayuda contextual:** Información disponible cuando se necesita

**Ejemplo en Airbnb:**
```
✅ BUENO: "Buscar alojamientos" en lugar de solo "Buscar"
✅ BUENO: "234 alojamientos encontrados" después de búsqueda
✅ BUENO: Calendario que muestra fechas no disponibles
❌ MALO: Iconos ambiguos sin texto explicativo
❌ MALO: Errores que no explican cómo solucionarlos
```

**Criterios de evaluación:**
- ¿Puede un usuario nuevo entender qué hacer sin instrucciones?
- ¿Proporciona feedback claro después de cada acción?
- ¿Indica claramente el estado actual del sistema?

#### **🎮 PRINCIPIO 3: CONTROLABILIDAD**

**Definición:** *"El diálogo es controlable cuando el usuario es capaz de iniciar y controlar la dirección y ritmo de la interacción hasta que se logre el objetivo."*

**Aspectos de control:**
- **Iniciativa del usuario:** El usuario decide cuándo actuar
- **Ritmo personal:** Sin presión temporal artificial
- **Navegación libre:** Posibilidad de ir atrás, adelante, saltar pasos
- **Personalización:** Configuración según preferencias

**Ejemplo en Airbnb:**
```
✅ BUENO: Usuario controla cuándo aplicar filtros
✅ BUENO: Posibilidad de modificar fechas sin reiniciar
✅ BUENO: Navegación libre entre resultados
❌ MALO: Aplicación automática de filtros sin confirmación
❌ MALO: Timeouts que resetean formularios
```

**Indicadores de control:**
- ¿Puede el usuario pausar y retomar en cualquier momento?
- ¿Hay opciones de personalización disponibles?
- ¿Se puede deshacer o modificar acciones previas?

#### **🎭 PRINCIPIO 4: CONFORMIDAD CON EXPECTATIVAS**

**Definición:** *"El diálogo se conforma con las expectativas del usuario cuando es consistente y corresponde a las características del usuario (conocimiento de la tarea, educación, experiencia, convenciones de idioma y cultura)."*

**Fuentes de expectativas:**
- **Convenciones de interfaz:** Estándares establecidos (ej. logo arriba-izquierda)
- **Metáforas familiares:** Conceptos del mundo real (ej. "carpeta", "papelera")
- **Experiencia previa:** Comportamiento en aplicaciones similares
- **Cultura y idioma:** Patrones específicos del contexto cultural

**Ejemplo en Airbnb:**
```
✅ BUENO: Icono de lupa para búsqueda
✅ BUENO: Carrito/corazón para guardar favoritos
✅ BUENO: Calendario para selección de fechas
❌ MALO: Botón "Reservar" que solo añade a wishlist
❌ MALO: Navegación diferente a otras webs de viajes
```

**Verificación de conformidad:**
- ¿Usa iconografía y terminología estándar del sector?
- ¿Se comporta como aplicaciones similares?
- ¿Respeta convenciones culturales del mercado objetivo?

#### **🛡️ PRINCIPIO 5: TOLERANCIA A ERRORES**

**Definición:** *"El diálogo es tolerante a errores si, a pesar de errores de entrada evidentes, el resultado pretendido puede lograrse con ninguna o mínima acción correctiva del usuario."*

**Estrategias de tolerancia:**
- **Prevención:** Evitar que errores ocurran
- **Detección temprana:** Validación en tiempo real
- **Recuperación fácil:** Corrección simple de errores
- **Comunicación clara:** Mensajes de error comprensibles

**Ejemplo en Airbnb:**
```
✅ BUENO: Autocompletado de ciudades evita errores tipográficos
✅ BUENO: Validación de fechas (checkout > checkin)
✅ BUENO: Sugerencias cuando no hay resultados
❌ MALO: Error genérico "Algo salió mal"
❌ MALO: Pérdida de datos al encontrar error
```

**Niveles de tolerancia:**
1. **Prevención:** El error no puede ocurrir
2. **Corrección automática:** Sistema corrige sin intervención
3. **Sugerencia:** Sistema propone correcciones
4. **Explicación:** Error claro con pasos para solucionar

#### **🔧 PRINCIPIO 6: ADAPTABILIDAD**

**Definición:** *"El diálogo es adaptable cuando tiene la capacidad de modificar la interacción para ajustarse a las necesidades y preferencias del usuario según el contexto de uso."*

**Tipos de adaptabilidad:**
- **Personalización (user-initiated):** Usuario configura interfaz
- **Adaptación (system-initiated):** Sistema se ajusta automáticamente
- **Configuración:** Opciones de customización
- **Flexibilidad:** Múltiples formas de hacer lo mismo

**Ejemplo en Airbnb:**
```
✅ BUENO: Recordar preferencias de búsqueda
✅ BUENO: Diferentes vistas (lista, mapa, galería)
✅ BUENO: Configuración de idioma y moneda
❌ MALO: Interfaz estática para todos los usuarios
❌ MALO: Sin opciones de accesibilidad configurables
```

**Dimensiones de adaptación:**
- **Contenido:** Información mostrada
- **Presentación:** Layout, colores, tamaños
- **Interacción:** Métodos de entrada/navegación
- **Funcionalidad:** Características disponibles

#### **🎓 PRINCIPIO 7: CAPACIDAD DE APRENDIZAJE**

**Definición:** *"El diálogo apoya la capacidad de aprendizaje cuando guía al usuario durante el aprendizaje del uso del sistema."*

**Facilitadores de aprendizaje:**
- **Descubrimiento intuitivo:** Funciones fáciles de encontrar
- **Progresión gradual:** De básico a avanzado
- **Retroalimentación educativa:** El usuario entiende por qué algo funciona
- **Consistencia:** Patrones predecibles facilitan generalización

**Ejemplo en Airbnb:**
```
✅ BUENO: Tour inicial para nuevos usuarios
✅ BUENO: Tooltips en funciones avanzadas
✅ BUENO: Patrones consistentes entre secciones
❌ MALO: Funciones ocultas sin manera de descubrirlas
❌ MALO: Cambios frecuentes en ubicación de elementos
```

**Estrategias de apoyo:**
- **Onboarding:** Introducción guiada
- **Progressive disclosure:** Revelar complejidad gradualmente
- **Affordances:** Elementos que sugieren su uso
- **Feedback constructivo:** Aprendizaje a través de la interacción

### 2.3 Interrelación entre Principios

**Los principios ISO 9241-110 NO son independientes:**

```
SINERGIA POSITIVA:
Autodescripción + Capacidad de aprendizaje = Interfaces más educativas
Controlabilidad + Adaptabilidad = Experiencias personalizables
Tolerancia a errores + Conformidad expectativas = Sistemas confiables

TENSIONES POTENCIALES:
Adecuación a la tarea vs. Adaptabilidad = Foco vs. flexibilidad
Autodescripción vs. Simplicidad = Información vs. limpieza visual
```

### 2.4 Aplicación en Evaluación Heurística

**Proceso sistemático de evaluación:**

1. **Evaluación individual:** Revisar cada principio por separado
2. **Puntuación:** Escala 1-5 por principio (1=muy mal, 5=excelente)
3. **Evidencias:** Capturas de pantalla y ejemplos específicos
4. **Severidad:** Clasificar problemas (crítico/mayor/menor/cosmético)
5. **Priorización:** Ranking de problemas por impacto e implementación

---

## LECTURA 3: METODOLOGÍAS DE EVALUACIÓN

### 3.1 Testing de Usuarios vs. Evaluación Heurística

#### **Métodos Cuantitativos (Testing de Usuarios)**

**Fortalezas:**
- **Datos objetivos:** Métricas medibles y comparables
- **Comportamiento real:** Observación de uso auténtico
- **Validez ecológica:** Condiciones cercanas al uso real
- **Estadísticamente robustos:** Permiten inferencias poblacionales

**Limitaciones:**
- **Costosos:** Requieren reclutamiento y tiempo significativo
- **Muestra pequeña:** Típicamente 5-12 usuarios por sesión
- **Sesgo de observación:** Usuarios pueden comportarse diferente
- **Enfoque en problemas superficiales:** Pueden perderse issues de diseño profundos

#### **Métodos Cualitativos (Evaluación Heurística)**

**Fortalezas:**
- **Eficientes:** Rápidos de ejecutar y menos costosos
- **Exhaustivos:** Pueden identificar problemas que usuarios no verbalizan
- **Predictivos:** Identifican problemas antes del desarrollo completo
- **Expertise:** Aprovechan conocimiento especializado en UX

**Limitaciones:**
- **Subjetivos:** Dependientes del criterio del evaluador
- **Falsos positivos:** Pueden identificar "problemas" que no afectan usuarios reales
- **Sesgo de experiencia:** Evaluadores expertos no piensan como usuarios típicos
- **Falta de priorización natural:** Todos los problemas parecen igualmente importantes

#### **Complementariedad de Métodos**

```
TESTING DE USUARIOS → Identifica qué problemas ocurren en práctica
EVALUACIÓN HEURÍSTICA → Explica por qué ocurren esos problemas

COMBINACIÓN ÓPTIMA:
1. Evaluación heurística inicial (identificar problemas potenciales)
2. Testing de usuarios (validar cuáles son realmente problemáticos)
3. Análisis integrado (explicaciones + evidencias)
4. Recomendaciones priorizadas (impacto real + severidad teórica)
```

### 3.2 Protocolos de Testing de Usuarios

#### **Diseño de Tareas Representativas**

**Criterios para buenas tareas de testing:**
- **Realistas:** Basadas en objetivos reales de usuarios
- **Específicas:** Con criterios claros de éxito/fracaso
- **Secuenciales:** Que construyan una narrativa coherente
- **Medibles:** Con métricas objetivas definidas

**Estructura de tarea efectiva:**
```
CONTEXTO: Situación que motiva la acción
OBJETIVO: Meta específica a lograr
CRITERIOS DE ÉXITO: Cómo determinar si se completó
PUNTO DE INICIO: Dónde comienza el usuario
DATOS NECESARIOS: Información que necesita el usuario

Ejemplo:
Contexto: Planeas un viaje romántico a París
Objetivo: Encuentra un apartamento céntrico para 2 personas, 3 noches
Criterios: Has seleccionado un alojamiento específico y verificado precio total
Inicio: Página principal de Airbnb
Datos: Fechas flexibles en próximas 6 semanas, presupuesto ~150€/noche
```

#### **Técnicas de Observación**

**Think Aloud Protocol:**
- **Usuario verbaliza:** Pensamientos, confusiones, expectativas
- **Observador registra:** Sin intervenir ni dirigir
- **Beneficios:** Insights sobre procesos cognitivos
- **Riesgos:** Puede alterar comportamiento natural

**Silent Observation:**
- **Observación pura:** Sin solicitar verbalización
- **Análisis post-tarea:** Discusión después de completar
- **Beneficios:** Comportamiento más natural
- **Riesgos:** Menos insight sobre motivaciones internas

**Retrospective Probing:**
- **Video review:** Usuario comenta su propio comportamiento grabado
- **Preguntas específicas:** Sobre momentos de duda o error
- **Beneficios:** Combina naturalidad con insights profundos
- **Riesgos:** Racionalización post-hoc de decisiones

#### **Registro y Análisis de Datos**

**Datos cuantitativos a capturar:**
```
TIEMPO:
- Tiempo total por tarea
- Tiempo hasta primera acción
- Tiempo en cada página/sección
- Pausas y duraciones de indecisión

ERRORES:
- Clicks incorrectos
- Navegación en dirección equivocada  
- Uso de funciones no apropiadas
- Intentos fallidos de completar acciones

ÉXITO/FRACASO:
- Tareas completadas vs. abandonadas
- Calidad del resultado obtenido
- Nivel de asistencia requerida
```

**Datos cualitativos importantes:**
```
EXPRESIONES VERBALES:
- Confusión expresada ("No entiendo...")
- Frustración ("¿Por qué no funciona...?")
- Satisfacción ("Ah, perfecto!")
- Expectativas ("Esperaba que...")

COMPORTAMIENTO NO VERBAL:
- Expresiones faciales (frustración, concentración)
- Postura corporal (tensión, relajación)
- Patrones de mouse (vacilación, búsqueda)
- Velocidad de interacción (rápida, cautelosa)
```

### 3.3 Métricas y Benchmarks

#### **Establecimiento de Umbrales**

**Criterios para definir niveles aceptables:**

```
EFICACIA:
- Excelente: >95% de tareas completadas
- Bueno: 85-95% de tareas completadas  
- Aceptable: 70-85% de tareas completadas
- Problemático: <70% de tareas completadas

EFICIENCIA (ejemplo e-commerce):
- Búsqueda de producto: <30 segundos
- Aplicar filtros: <15 segundos
- Completar compra: <3 minutos
- Registrarse: <2 minutos

SATISFACCIÓN (escala 1-5):
- Excelente: >4.5 promedio
- Bueno: 4.0-4.5 promedio
- Aceptable: 3.5-4.0 promedio  
- Problemático: <3.5 promedio
```

#### **Benchmarks de Industria**

**Plataformas de viajes/turismo:**
```
CONVERSIÓN (búsqueda → reserva):
- Líder del mercado: 3-5%
- Promedio industria: 1-3%
- Por debajo del promedio: <1%

TIEMPO PROMEDIO DE SESIÓN:
- Búsqueda exploratoria: 8-15 minutos
- Búsqueda con intención: 3-8 minutos
- Reserva decisión tomada: 1-3 minutos

TASA DE ABANDONO:
- Página de búsqueda: <10%
- Página de resultados: 20-30%
- Página de detalle: 40-50%
- Proceso de pago: 60-70%
```

---

## LECTURA 4: PREPARACIÓN ESPECÍFICA PARA AIRBNB

### 4.1 Análisis Previo de la Plataforma

**Antes del laboratorio, familiarízate con:**

#### **Arquitectura de Información**
```
ESTRUCTURA PRINCIPAL:
/ (Página principal) → Búsqueda básica
/s/ (Resultados) → Listado + filtros + mapa
/rooms/ (Detalle) → Información completa del alojamiento
/book/ (Reserva) → Proceso de booking

FLUJO TÍPICO:
Búsqueda → Filtrado → Exploración → Comparación → Reserva
```

#### **Elementos Clave a Evaluar**
- **Barra de búsqueda:** Ubicación, fechas, huéspedes
- **Sistema de filtros:** Precio, tipo, amenidades, ubicación
- **Presentación de resultados:** Lista, mapa, información mostrada
- **Página de detalle:** Fotos, descripción, reseñas, precio
- **Proceso de reserva:** Pasos, información requerida, confianza

### 4.2 Usuarios Tipo de Airbnb

**Segmentos principales para considerar en evaluación:**

#### **Viajero Ocasional**
- **Características:** Usa Airbnb 1-2 veces por año
- **Necesidades:** Simplicidad, confianza, orientación clara
- **Comportamiento:** Explora mucho, compara opciones, busca reseñas

#### **Viajero Frecuente**
- **Características:** Usuario habitual de plataformas de viajes
- **Necesidades:** Eficiencia, funciones avanzadas, personalización
- **Comportamiento:** Búsquedas específicas, menos exploración

#### **Viajero de Negocios**
- **Características:** Viajes por trabajo, decisiones rápidas
- **Necesidades:** Filtros específicos (WiFi, ubicación), cancelación flexible
- **Comportamiento:** Búsquedas dirigidas, menor sensibilidad al precio

### 4.3 Tareas Críticas en Airbnb

**Identifica estas tareas durante tu exploración previa:**

#### **Búsqueda y Filtrado**
- ¿Qué tan fácil es especificar criterios de búsqueda?
- ¿Los filtros son comprensibles y relevantes?
- ¿Se actualiza la información de resultados dinámicamente?

#### **Evaluación de Opciones**
- ¿Qué información es más prominente en resultados?
- ¿Cómo se comparan diferentes alojamientos?
- ¿Es fácil alternar entre vista lista y mapa?

#### **Decisión de Reserva**
- ¿Qué información influye más en la decisión?
- ¿Es claro el precio total incluyendo tasas?
- ¿Las reseñas son fáciles de evaluar?

---

## CHECKLIST DE PREPARACIÓN

### Antes del Laboratorio

**Conocimiento teórico:**
- [ ] He leído y comprendido las definiciones ISO 9241-11
- [ ] Conozco los 7 principios de diálogo ISO 9241-110
- [ ] Entiendo la diferencia entre métodos cuantitativos y cualitativos
- [ ] Sé cómo calcular métricas de eficacia, eficiencia y satisfacción

**Familiarización práctica:**
- [ ] He navegado Airbnb.es como usuario normal
- [ ] Conozco la estructura básica de la plataforma
- [ ] He identificado las funciones principales disponibles
- [ ] Entiendo el flujo típico de búsqueda a reserva

**Materiales:**
- [ ] Tengo acceso a las plantillas de registro
- [ ] Sé cómo usar cronómetro para medir tiempos
- [ ] Tengo claro mi rol en el equipo de trabajo
- [ ] He revisado el protocolo de evaluación heurística

### Durante el Laboratorio

**Actitud de evaluador:**
- [ ] Mantendré objetividad en observaciones
- [ ] Registraré datos precisos sin interpretaciones prematuras  
- [ ] Buscaré evidencias específicas para cada hallazgo
- [ ] Distinguiré entre preferencias personales y problemas de usabilidad

### Después del Laboratorio

**Análisis e interpretación:**
- [ ] Calcularé métricas según definiciones ISO exactas
- [ ] Buscaré correlaciones entre métodos cuantitativos y cualitativos
- [ ] Priorizaré recomendaciones basándome en evidencias
- [ ] Estructuraré el reporte según formato profesional

---

## RECURSOS COMPLEMENTARIOS

### Enlaces de Referencia

**Documentos ISO (abstracts gratuitos):**
- ISO 9241-11:2018 - Usability: Definitions and concepts
- ISO 9241-110:2020 - Interaction principles

**Herramientas de medición:**
- System Usability Scale (SUS) - Cuestionario estándar
- User Experience Questionnaire (UEQ) - Medición integral
- Net Promoter Score (NPS) - Lealtad y recomendación

**Casos de estudio:**
- Nielsen Norman Group - Usability studies de e-commerce
- Baymard Institute - Research específico en UX de comercio
- UX Planet - Casos de redesign de plataformas de viajes

### Glosario de Términos

**Eficacia:** Precisión y completitud en lograr objetivos  
**Eficiencia:** Recursos empleados respecto a resultados obtenidos  
**Satisfacción:** Libertad de incomodidad y actitudes positivas  
**Heurística:** Principio o regla general para evaluación de interfaces  
**Think Aloud:** Técnica donde usuario verbaliza pensamientos durante uso  
**Affordance:** Propiedad que sugiere cómo debe usarse un elemento  
**Progressive Disclosure:** Revelar información/funcionalidad gradualmente  

---

**Tiempo de estudio recomendado:** 90 minutos  
**Revisión previa al lab:** 15 minutos repasando conceptos clave  
**Consultas:** Usar foro del curso o contactar al profesor  

¡Prepárate para una evaluación sistemática y profesional de usabilidad!