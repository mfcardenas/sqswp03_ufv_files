# Laboratorio 5: Validación de Requisitos

## Descripción del Laboratorio

En este laboratorio, implementarás un sistema comprehensivo de validación de requisitos siguiendo el estándar ISO/IEC/IEEE 29148. El laboratorio se enfoca en crear un motor de validación que pueda verificar requisitos en múltiples dimensiones: completitud, consistencia, factibilidad, testeabilidad y cumplimiento de estándares.

## Objetivos de Aprendizaje

Después de completar este laboratorio, serás capaz de:

1. **Implementar Validación Multi-Tipo**: Crear un motor de validación que verifique requisitos en cinco dimensiones principales
2. **Generar Casos de Prueba Automáticamente**: Desarrollar lógica para crear casos de prueba desde requisitos
3. **Realizar Testing de Aceptación**: Construir un framework para ejecutar pruebas de aceptación con métricas
4. **Validar Cumplimiento de Estándares**: Implementar verificación de cumplimiento ISO/IEC/IEEE 29148
5. **Crear Dashboard Interactivo**: Desarrollar una interfaz web para visualizar resultados de validación
6. **Generar Reportes Comprehensivos**: Crear reportes detallados con métricas de calidad

## Requisitos Técnicos

### Lenguajes y Tecnologías
- **Python**: Para el motor de validación y lógica de negocio
- **HTML/CSS/JavaScript**: Para el dashboard interactivo
- **JSON/YAML**: Para almacenamiento de datos de requisitos
- **Chart.js**: Para visualización de métricas

### Funcionalidades Requeridas

#### 1. Motor de Validación (Python)
```python
class ValidationEngine:
    def __init__(self)
    def load_requirements(file_path: str) -> bool
    def validate_requirements() -> Dict[str, Any]
    def generate_test_cases() -> List[Dict[str, Any]]
    def perform_acceptance_testing() -> Dict[str, Any]
    def validate_against_standards() -> Dict[str, Any]
    def generate_validation_report() -> str
    def export_validation_results(format_type: str, file_path: str)
```

#### 2. Tipos de Validación
- **Completitud**: Verificar campos requeridos, longitud de descripción, criterios de aceptación
- **Consistencia**: Detectar IDs duplicados, requisitos conflictivos, terminología consistente
- **Factibilidad**: Evaluar factibilidad técnica, de recursos y temporal
- **Testeabilidad**: Verificar criterios medibles, condiciones verificables, posibilidad de automatización
- **Cumplimiento de Estándares**: Validar contra ISO/IEC/IEEE 29148

#### 3. Dashboard Web Interactivo
- **Resumen de Validación**: Métricas generales y puntuación
- **Resultados Detallados**: Por tipo de validación con filtros
- **Casos de Prueba**: Visualización y gestión de pruebas generadas
- **Testing de Aceptación**: Estado, métricas y resultados detallados
- **Cumplimiento**: Verificación contra estándares con puntuación
- **Reportes**: Generación y descarga de reportes comprehensivos

## Estructura de Archivos

```
Lab5/
├── validation_engine.py          # Motor de validación principal
├── validation_dashboard.html     # Dashboard web
├── validation_styles.css         # Estilos CSS
├── validation_scripts.js         # Lógica JavaScript
├── validation_requirements.json  # Datos de ejemplo
├── validation_test_suite.py      # Suite de pruebas
└── README.md                     # Documentación
```

## Tareas a Realizar

### Tarea 1: Motor de Validación Básico
1. Crear clase `ValidationEngine` con métodos básicos
2. Implementar carga de requisitos desde JSON
3. Crear estructura de validación con tipos principales
4. Implementar validación de completitud básica

### Tarea 2: Validación Avanzada
1. Implementar validación de consistencia (detectar conflictos, duplicados)
2. Agregar validación de factibilidad (técnica, recursos, tiempo)
3. Crear validación de testeabilidad (criterios medibles, verificables)
4. Implementar validación de cumplimiento de estándares

### Tarea 3: Generación de Casos de Prueba
1. Crear método `generate_test_cases()` 
2. Implementar lógica para extraer precondiciones
3. Generar pasos de prueba automáticos
4. Crear resultados esperados desde requisitos

### Tarea 4: Framework de Aceptación
1. Implementar `perform_acceptance_testing()`
2. Crear simulación de ejecución de pruebas
3. Calcular métricas de cobertura
4. Generar reportes de aceptación

### Tarea 5: Dashboard Interactivo
1. Crear HTML con navegación por pestañas
2. Implementar visualización de métricas con Chart.js
3. Agregar controles para ejecutar validaciones
4. Crear filtros y búsqueda en resultados

### Tarea 6: Reportes y Exportación
1. Implementar `generate_validation_report()`
2. Crear exportación a múltiples formatos (JSON, HTML, Markdown)
3. Agregar métricas de calidad detalladas
4. Implementar descarga de reportes desde dashboard

## Datos de Ejemplo

Crear archivo `validation_requirements.json` con requisitos de ejemplo:

```json
{
  "requirements": [
    {
      "id": "REQ-001",
      "text": "El sistema debe procesar pedidos en menos de 2 segundos",
      "type": "functional",
      "priority": "high",
      "acceptance_criteria": [
        "Tiempo de respuesta < 2 segundos",
        "Procesamiento exitoso del 99.9% de pedidos"
      ]
    },
    {
      "id": "REQ-002", 
      "text": "El sistema debe autenticar usuarios mediante OAuth 2.0",
      "type": "security",
      "priority": "high",
      "acceptance_criteria": [
        "Autenticación OAuth 2.0 implementada",
        "Tokens válidos generados correctamente"
      ]
    }
  ]
}
```

## Criterios de Evaluación

### Funcionalidad (60%)
- ✅ Motor de validación implementado correctamente
- ✅ Todos los tipos de validación funcionando
- ✅ Generación automática de casos de prueba
- ✅ Framework de testing de aceptación operativo
- ✅ Dashboard web funcional con todas las características

### Calidad de Código (20%)
- ✅ Código bien estructurado y documentado
- ✅ Manejo adecuado de errores y excepciones
- ✅ Uso correcto de estructuras de datos
- ✅ Separación clara de responsabilidades

### Interfaz de Usuario (10%)
- ✅ Dashboard intuitivo y responsive
- ✅ Visualización clara de métricas
- ✅ Navegación fluida entre secciones
- ✅ Feedback visual apropiado

### Reportes y Documentación (10%)
- ✅ Reportes comprehensivos generados
- ✅ Múltiples formatos de exportación
- ✅ Documentación clara del código
- ✅ Instrucciones de uso incluidas

## Pistas y Consejos

### 1. Estructura del Motor de Validación
```python
class ValidationEngine:
    def __init__(self):
        self.requirements = []
        self.validation_results = {}
        self.test_cases = []
        self.validation_rules = self._initialize_rules()
    
    def _initialize_rules(self):
        return {
            'completeness': {...},
            'consistency': {...},
            # ... otros tipos
        }
```

### 2. Validación de Completitud
```python
def _validate_completeness(self):
    required_fields = ['id', 'text', 'type', 'priority']
    for req in self.requirements:
        if not all(field in req for field in required_fields):
            # Marcar como incompleto
```

### 3. Generación de Casos de Prueba
```python
def _generate_test_case_for_requirement(self, req):
    return {
        'id': f"TC_{req['id']}",
        'title': f"Probar {req['text'][:50]}...",
        'steps': self._generate_test_steps(req),
        'expected': req.get('acceptance_criteria', [])
    }
```

### 4. Dashboard con Chart.js
```javascript
const ctx = document.getElementById('scoreChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Aprobado', 'Fallido'],
        datasets: [{
            data: [passed, failed],
            backgroundColor: ['#28a745', '#dc3545']
        }]
    }
});
```

## Preguntas de Reflexión

1. **¿Por qué es importante validar requisitos en múltiples dimensiones?**
2. **¿Cómo afecta la calidad de los requisitos a la generación de casos de prueba?**
3. **¿Qué métricas son más importantes para evaluar la calidad de requisitos?**
4. **¿Cómo se relaciona el cumplimiento de estándares con la calidad del software?**
5. **¿Qué beneficios aporta un dashboard interactivo en el proceso de validación?**

## Recursos Adicionales

- **ISO/IEC/IEEE 29148:2018**: Estándar para especificación de requisitos de software
- **IEEE 830-1998**: Guía recomendada para especificación de requisitos de software
- **ISTQB**: Estándares para testing de software
- **Chart.js Documentation**: Para visualización de datos en el dashboard

## Entrega del Laboratorio

1. **Código Fuente**: Todos los archivos Python, HTML, CSS y JavaScript
2. **Datos de Prueba**: Archivo JSON con requisitos de ejemplo
3. **Documentación**: README con instrucciones de instalación y uso
4. **Demostración**: Capturas de pantalla del dashboard funcionando
5. **Reportes de Prueba**: Resultados de validación con datos de ejemplo

¡Implementa un sistema robusto de validación de requisitos que pueda ser utilizado en entornos profesionales siguiendo los estándares ISO/IEC/IEEE 29148!
