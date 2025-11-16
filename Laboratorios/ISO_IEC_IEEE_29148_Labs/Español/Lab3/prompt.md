# Laboratorio 3: Análisis y Modelado de Requisitos - Instrucciones para el Estudiante

## 🎯 **Objetivo**
Aplicar técnicas sistemáticas de análisis de requisitos y crear múltiples modelos de requisitos para transformar requisitos crudos en artefactos estructurados y analizables que apoyen el desarrollo de software.

## 📋 **Resultados de Aprendizaje**
Al completar este laboratorio, podrás:
- Analizar requisitos para atributos de calidad (completitud, consistencia, ambigüedad)
- Categorizar requisitos por tipo (funcionales, no funcionales, restricciones)
- Identificar y documentar dependencias de requisitos
- Crear diferentes tipos de modelos de requisitos
- Implementar esquemas de priorización de requisitos
- Validar requisitos contra criterios de calidad

## 🛠️ **Herramientas y Tecnologías**
- **Python 3.x** para motor de análisis
- **HTML/CSS/JavaScript** para dashboard interactivo
- **JSON** para almacenamiento de datos
- **Chart.js** para visualización de datos
- **Framework de pruebas unitarias** para validación

## 📝 **Tareas**

### **Tarea 1: Corregir la Herramienta de Análisis de Requisitos (60 puntos)**

#### **Paso 1.1: Corregir Problemas de Carga de Archivos**
- Localizar el método `load_requirements()` en `requirements_analysis.py`
- Agregar manejo de errores apropiado para archivos no encontrados
- Implementar manejo de errores de formato JSON
- Agregar mensajes de error informativos para diferentes escenarios de falla

#### **Paso 1.2: Corregir Lógica de Análisis**
- Corregir el método `analyze_requirements()` para procesar todos los requisitos correctamente
- Corregir el algoritmo de cálculo de puntaje de calidad
- Implementar seguimiento y reporte apropiados de problemas
- Agregar estructura completa de resultados de análisis

#### **Paso 1.3: Mejorar Detección de Ambigüedad**
- Mejorar el método `check_ambiguity()` con patrones más sofisticados
- Agregar detección de cuantificadores vagos ("algunos", "muchos", "pocos")
- Implementar verificaciones de longitud basadas en ambigüedad
- Agregar detección de ambigüedad dependiente del contexto

#### **Paso 1.4: Implementar Verificación de Completitud**
- Corregir el método `check_completeness()` para validar verbos modales apropiadamente
- Agregar verificaciones de estructura sujeto-verbo-objeto
- Implementar validación de verbos de acción
- Agregar cálculo de puntuación de completitud

#### **Paso 1.5: Agregar Verificación de Consistencia**
- Implementar el método `check_basic_consistency()`
- Agregar detección de términos contradictorios
- Implementar identificación básica de conflictos
- Agregar cálculo de puntuación de consistencia

#### **Paso 1.6: Corregir Lógica de Categorización**
- Corregir el método `categorize_requirements()`
- Mejorar patrones de identificación de tipos de requisitos
- Agregar soporte para requisitos de interfaz
- Implementar asignación apropiada de categorías

#### **Paso 1.7: Implementar Análisis de Dependencias**
- Completar el método `identify_dependencies()`
- Agregar detección de dependencias secuenciales
- Implementar identificación de dependencias condicionales
- Agregar análisis de dependencias funcionales

#### **Paso 1.8: Agregar Sistema de Priorización**
- Implementar el método `prioritize_requirements()`
- Agregar cálculo de prioridad multi-factor
- Implementar evaluación de valor de negocio
- Agregar ordenamiento basado en prioridad

#### **Paso 1.9: Crear Generación de Modelos**
- Completar el método `generate_models()`
- Implementar generación de jerarquía funcional
- Agregar creación de modelo de flujo de datos
- Crear modelos de casos de uso y grafo de dependencias

#### **Paso 1.10: Agregar Funcionalidad de Exportación**
- Implementar el método `export_analysis()`
- Agregar exportación completa de resultados
- Incluir datos de modelos en exportaciones
- Agregar seguimiento de timestamp

### **Tarea 2: Corregir el Dashboard de Modelado (30 puntos)**

#### **Paso 2.1: Completar Estructura HTML**
- Corregir el sistema de navegación en `modeling_dashboard.html`
- Agregar funcionalidad de cambio de sección apropiada
- Implementar gestión de área de contenido
- Agregar estados de carga y placeholders

#### **Paso 2.2: Implementar Estilos CSS**
- Completar el archivo `modeling_styles.css`
- Agregar elementos de diseño responsivo
- Implementar estilos de navegación apropiados
- Agregar estilos para canvas de modelos

#### **Paso 2.3: Agregar Funcionalidad JavaScript**
- Completar el archivo `modeling_scripts.js`
- Implementar navegación de secciones
- Agregar display de resultados de análisis
- Crear funciones de visualización de modelos

#### **Paso 2.4: Agregar Integración de Gráficos**
- Integrar Chart.js para visualización de métricas de calidad
- Implementar gráficos interactivos
- Agregar funcionalidad de actualización de gráficos
- Crear múltiples tipos de gráficos

#### **Paso 2.5: Implementar Display de Modelos**
- Agregar visualización de jerarquía funcional
- Implementar display de diagrama de flujo de datos
- Crear representación de diagrama de casos de uso
- Agregar visualización de grafo de dependencias

### **Tarea 3: Crear Suite de Pruebas (10 puntos)**

#### **Paso 3.1: Implementar Pruebas Unitarias**
- Crear casos de prueba completos en `test_requirements_analysis.py`
- Probar todas las funcionalidades principales
- Agregar pruebas de casos extremos
- Implementar gestión de datos de prueba

#### **Paso 3.2: Probar Funciones de Análisis**
- Probar precisión de detección de ambigüedad
- Validar verificación de completitud
- Probar lógica de categorización
- Verificar algoritmos de priorización

#### **Paso 3.3: Probar Generación de Modelos**
- Probar funciones de creación de modelos
- Validar estructuras de datos de modelos
- Probar funcionalidad de exportación
- Verificar manejo de errores

## 📊 **Entregables**

### **Archivos de Código:**
1. `requirements_analysis.py` - Motor de análisis corregido y completo
2. `modeling_dashboard.html` - Interfaz web completa
3. `modeling_styles.css` - Estilos completos y responsivos
4. `modeling_scripts.js` - Funcionalidad JavaScript completa
5. `test_requirements_analysis.py` - Suite de pruebas unitarias completa

### **Archivos de Datos:**
1. `sample_requirements.json` - Archivo de datos de prueba
2. `requirements_analysis_results.json` - Salida de análisis
3. `requirements_analysis_report.md` - Reporte generado

### **Documentación:**
1. Comentarios de código explicando todas las correcciones e implementaciones
2. Resultados de pruebas y reporte de cobertura
3. Ejemplos de uso y demostraciones

## ✅ **Criterios de Validación**

### **Requisitos Funcionales:**
- [ ] Todo el código Python ejecuta sin errores de sintaxis
- [ ] La herramienta de análisis produce resultados correctos para datos de prueba
- [ ] El dashboard web carga y funciona apropiadamente
- [ ] Los gráficos se muestran correctamente
- [ ] La funcionalidad de exportación funciona

### **Requisitos de Calidad:**
- [ ] El código sigue las guías de estilo PEP 8
- [ ] Las funciones tienen docstrings apropiadas
- [ ] El manejo de errores está implementado en todo el código
- [ ] Las pruebas unitarias pasan con cobertura del 100%
- [ ] El HTML valida sin errores
- [ ] El CSS es responsivo y accesible
- [ ] El JavaScript sigue mejores prácticas modernas

### **Precisión de Análisis:**
- [ ] La detección de ambigüedad identifica 90%+ de términos ambiguos
- [ ] La verificación de completitud valida verbos modales correctamente
- [ ] La categorización asigna tipos correctos a 95%+ de requisitos
- [ ] La priorización produce ranking lógico
- [ ] El análisis de dependencias identifica relaciones con precisión

## 🧪 **Instrucciones de Prueba**

### **Paso 1: Ejecutar la Herramienta de Análisis**
```bash
python requirements_analysis.py
```

### **Paso 2: Abrir el Dashboard**
- Abrir `modeling_dashboard.html` en un navegador web
- Probar todas las secciones de navegación
- Cargar y analizar requisitos
- Generar y ver modelos

### **Paso 3: Ejecutar Pruebas Unitarias**
```bash
python -m unittest test_requirements_analysis.py
```

### **Paso 4: Validar Resultados**
- Verificar resultados de análisis para exactitud
- Validar generación de modelos
- Probar funcionalidad de exportación
- Revisar reportes generados

## 📈 **Rúbrica de Evaluación**

| Criterio | Excelente (90-100) | Bueno (80-89) | Satisfactorio (70-79) | Necesita Mejorar (<70) |
|----------|-------------------|--------------|---------------------|----------------------|
| **Calidad de Código** | Limpio, bien documentado, sigue mejores prácticas | Buena estructura, algo de documentación | Funcionalidad básica, documentación mínima | Estructura pobre, funcionalidad faltante |
| **Correcciones de Bugs** | Todos los problemas identificados y corregidos correctamente | La mayoría de problemas corregidos, problemas menores restantes | Algunos fixes implementados, problemas mayores persistentes | Pocos fixes, problemas significativos restantes |
| **Precisión de Análisis** | 95%+ de precisión en todas las funciones de análisis | 85-94% de precisión | 70-84% de precisión | <70% de precisión |
| **Generación de Modelos** | Todos los modelos creados correctamente con visualización apropiada | La mayoría de modelos funcionan, problemas menores de visualización | Modelos básicos creados, problemas significativos de visualización | Modelos incompletos o no funcionales |
| **Pruebas** | Pruebas completas con 100% de cobertura | Buena cobertura de pruebas, algunos casos extremos faltantes | Pruebas básicas implementadas | Pruebas mínimas o inexistentes |
| **Documentación** | Documentación completa con ejemplos | Buena documentación, algunas áreas poco claras | Documentación básica | Documentación pobre o faltante |

## ✅ **Criterios de Éxito**
- Todo el código Python ejecuta sin errores de sintaxis
- La herramienta de análisis produce resultados correctos para datos de prueba
- El dashboard web es completamente funcional
- Todas las pruebas unitarias pasan
- Los modelos se generan y muestran correctamente
- La funcionalidad de exportación funciona como esperado
- El código está bien documentado y es mantenible

## 💡 **Consejos y Sugerencias**

### **Depurando la Herramienta de Análisis:**
- Comenzar con casos de prueba simples
- Usar declaraciones print para rastrear ejecución
- Verificar tipos de datos y estructuras
- Validar parsing JSON

### **Corrigiendo el Dashboard:**
- Probar estructura HTML primero
- Agregar CSS incrementalmente
- Implementar funciones JavaScript una por una
- Usar herramientas de desarrollador del navegador para depuración

### **Generación de Modelos:**
- Comenzar con modelos simples (jerarquía funcional)
- Construir complejidad gradualmente
- Probar cada tipo de modelo por separado
- Validar estructuras de datos

### **Mejores Prácticas de Pruebas:**
- Escribir pruebas para cada función
- Incluir casos extremos y condiciones de error
- Probar con diferentes conjuntos de datos
- Verificar resultados esperados vs reales

## 🚀 **Próximos Pasos**
Después de completar este laboratorio:
1. Aplicar estas técnicas a requisitos de proyectos reales
2. Explorar técnicas avanzadas de modelado (UML, BPMN)
3. Implementar validación automática de requisitos
4. Integrar con herramientas de gestión de requisitos

Recuerda: El análisis y modelado de requisitos son procesos iterativos. La calidad de tu análisis impacta directamente el éxito del proyecto de desarrollo de software.
