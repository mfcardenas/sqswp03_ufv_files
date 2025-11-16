# Laboratorio 4: Especificación de Requisitos - Prompt

## Objetivos de Aprendizaje
Al finalizar este laboratorio, los estudiantes podrán:
- Crear Especificaciones de Requisitos de Software (SRS) profesionales siguiendo el estándar ISO/IEC/IEEE 29148
- Aplicar diferentes formatos de especificación (textual, tabular, gráfico, formal)
- Implementar matrices de trazabilidad de requisitos
- Validar especificaciones contra criterios de calidad
- Gestionar baselines de requisitos y control de versiones
- Exportar especificaciones en múltiples formatos para diferentes interesados

## Contexto
Eres un ingeniero de requisitos trabajando para una empresa de desarrollo de software. Tu equipo ha completado la elicitación y análisis de requisitos para un Sistema de Automatización del Hogar Inteligente. Ahora necesitas crear el documento formal de Especificación de Requisitos de Software que servirá como contrato entre los interesados y los desarrolladores.

## Descripción de la Tarea

### Fase 1: Generación de Especificaciones
1. **Cargar Requisitos**: Cargar los requisitos desde `sample_requirements.json`
2. **Generar SRS**: Crear una Especificación de Requisitos de Software completa con:
   - Sección de introducción (propósito, alcance, definiciones, referencias)
   - Descripción general (perspectiva del producto, funciones, características de usuario)
   - Requisitos específicos (funcionales, no funcionales, interfaz, rendimiento)
   - Apéndices (glosario, modelos de análisis, matriz de trazabilidad)

### Fase 2: Aplicación de Formatos
3. **Aplicar Formatos**: Transformar requisitos en diferentes formatos de especificación:
   - **Formato Textual**: Especificaciones en lenguaje natural estructurado
   - **Formato Tabular**: Tablas de requisitos estilo hoja de cálculo
   - **Formato Gráfico**: Diagramas de casos de uso, jerarquías de requisitos
   - **Formato Formal**: Notación matemática/lógica de especificaciones

### Fase 3: Implementación de Trazabilidad
4. **Crear Matriz de Trazabilidad**: Establecer enlaces entre:
   - Requisitos y elementos de diseño
   - Requisitos y casos de prueba
   - Requisitos y otros artefactos

### Fase 4: Validación de Calidad
5. **Validar Especificaciones**: Evaluar calidad contra criterios:
   - **Completitud**: Toda la información necesaria presente
   - **Consistencia**: Sin requisitos conflictivos
   - **Trazabilidad**: Todos los requisitos correctamente enlazados
   - **Testabilidad**: Los requisitos pueden ser verificados

### Fase 5: Gestión de Baselines
6. **Crear Baselines**: Establecer control de versiones para especificaciones:
   - Crear versiones baseline
   - Comparar cambios entre baselines
   - Rastrear evolución de requisitos

### Fase 6: Exportación y Reportes
7. **Exportar Especificaciones**: Generar salidas en múltiples formatos:
   - JSON para acceso programático
   - HTML para visualización web
   - YAML para gestión de configuración
8. **Generar Reportes**: Crear reportes de evaluación de calidad

## Entregables
1. **Generador de Especificaciones Operativo** (`specification_generator.py`)
2. **Visor Interactivo** (`specification_viewer.html`)
3. **Archivos de Soporte**:
   - `specification_styles.css`
   - `specification_scripts.js`
   - `sample_requirements.json`
4. **Suite de Pruebas** (`test_specification_generator.py`)
5. **Salidas Generadas**:
   - Documento SRS completo
   - Matriz de trazabilidad
   - Reporte de validación de calidad
   - Versiones baseline

## Requisitos Técnicos
- Usar Python 3.7+ para el generador de especificaciones
- Implementar principios de diseño orientado a objetos
- Incluir manejo completo de errores
- Crear interfaz web interactiva con JavaScript
- Usar Chart.js para visualización de datos
- Implementar validación apropiada de datos
- Seguir estándares de codificación PEP 8

## Criterios de Calidad
- **Funcionalidad**: Todas las características funcionan como especificado
- **Usabilidad**: La interfaz es intuitiva y fácil de usar
- **Rendimiento**: Las operaciones se completan en tiempo razonable
- **Mantenibilidad**: El código está bien estructurado y documentado
- **Testabilidad**: Cobertura completa de pruebas

## Rúbrica de Evaluación
- **Generación SRS (25%)**: SRS completo con todas las secciones requeridas
- **Implementación de Formatos (20%)**: Aplicación apropiada de diferentes formatos
- **Trazabilidad (20%)**: Creación correcta de matriz y enlaces
- **Validación (15%)**: Implementación de evaluación de calidad
- **Interfaz de Usuario (10%)**: Funcionalidad del visor interactivo
- **Pruebas (10%)**: Completitud del suite de pruebas y cobertura

## Tiempo Estimado
- Fase 1: 45 minutos
- Fase 2: 30 minutos
- Fase 3: 30 minutos
- Fase 4: 30 minutos
- Fase 5: 20 minutos
- Fase 6: 25 minutos
- **Total**: 3.5 horas

## Recursos Provistos
- `sample_requirements.json`: Datos de requisitos de entrada
- Declaración de problema con ejemplos de código con errores
- Framework de pruebas para validación

## Desafíos Esperados
- Implementar notación de especificación formal
- Crear enlaces de trazabilidad comprehensivos
- Diseñar interfaz de usuario intuitiva
- Manejar casos límite en validación
- Gestionar versiones baseline efectivamente

## Criterios de Éxito
- ✅ Código Python ejecuta sin errores
- ✅ SRS completo generado correctamente
- ✅ Múltiples formatos aplicados
- ✅ Matriz de trazabilidad funcional
- ✅ Validación de calidad implementada
- ✅ Interfaz web operativa
- ✅ Todas las pruebas pasan
- ✅ Reportes generados son comprehensivos y legibles

## Actividades de Extensión
1. **Trazabilidad Avanzada**: Implementar trazabilidad bi-direccional
2. **Métricas de Requisitos**: Agregar análisis de complejidad de requisitos
3. **Características Colaborativas**: Capacidades de edición multi-usuario
4. **Integración**: Conectar con herramientas externas de gestión de requisitos
5. **Automatización**: Implementar pipelines de validación continua
