# Laboratorio 5: Validación de Requisitos
## ISO/IEC/IEEE 29148 - Ingeniería de Requisitos

### Descripción
Este laboratorio implementa un sistema comprehensivo de validación de requisitos siguiendo el estándar ISO/IEC/IEEE 29148. El sistema valida requisitos en múltiples dimensiones: completitud, consistencia, factibilidad, testeabilidad y cumplimiento de estándares.

### Archivos del Laboratorio

#### Core Files
- `validation_engine.py` - Motor de validación principal con lógica completa
- `validation_dashboard.html` - Dashboard web interactivo
- `validation_styles.css` - Estilos CSS para el dashboard
- `validation_scripts.js` - Scripts JavaScript para funcionalidad interactiva
- `validation_requirements.json` - Datos de ejemplo de requisitos
- `validation_test_suite.py` - Suite de pruebas unitarias

### Requisitos del Sistema

#### Software
- **Python 3.8+** - Para ejecutar el motor de validación
- **Navegador Web Moderno** - Chrome, Firefox, Safari, Edge (para el dashboard)
- **Chart.js** - Librería incluida vía CDN para gráficos

#### Librerías Python
```bash
pip install --upgrade pip
# No se requieren librerías externas adicionales
```

### Instalación y Configuración

1. **Clonar o descargar los archivos del laboratorio**
   ```bash
   # Los archivos deben estar en el mismo directorio
   ls -la
   # validation_engine.py
   # validation_dashboard.html
   # validation_styles.css
   # validation_scripts.js
   # validation_requirements.json
   # validation_test_suite.py
   ```

2. **Verificar instalación de Python**
   ```bash
   python --version
   # Debe ser Python 3.8 o superior
   ```

### Uso del Sistema

#### 1. Motor de Validación (Python)

```python
from validation_engine import ValidationEngine

# Crear instancia del motor
engine = ValidationEngine()

# Cargar requisitos
engine.load_requirements('validation_requirements.json')

# Ejecutar validación completa
results = engine.validate_requirements()
print(f"Puntuación general: {results['overall_score']:.1f}/100")

# Generar casos de prueba
test_cases = engine.generate_test_cases()
print(f"Casos de prueba generados: {len(test_cases)}")

# Ejecutar testing de aceptación
acceptance = engine.perform_acceptance_testing()
print(f"Estado de aceptación: {acceptance['acceptance_status']}")

# Generar reporte
report = engine.generate_validation_report()
with open('validation_report.md', 'w', encoding='utf-8') as f:
    f.write(report)
```

#### 2. Dashboard Web Interactivo

1. **Abrir el dashboard**
   - Abrir `validation_dashboard.html` en un navegador web
   - El dashboard se carga automáticamente

2. **Flujo de trabajo típico**
   - Hacer clic en "Cargar Requisitos" para cargar datos de ejemplo
   - Hacer clic en "Validar" para ejecutar validación completa
   - Revisar resultados en las pestañas de validación
   - Generar casos de prueba con "Generar Pruebas"
   - Ejecutar testing de aceptación
   - Ver reportes generados

#### 3. Ejecutar Pruebas Unitarias

```bash
# Ejecutar suite de pruebas completa
python validation_test_suite.py

# Ejecutar pruebas específicas
python -m unittest validation_test_suite.TestValidationEngine.test_load_requirements_success

# Ejecutar con verbosidad
python validation_test_suite.py -v
```

### Características Implementadas

#### ✅ Motor de Validación
- **Validación de Completitud**: Verifica campos requeridos, criterios de aceptación, longitud de descripción
- **Validación de Consistencia**: Detecta IDs duplicados, requisitos conflictivos, terminología inconsistente
- **Validación de Factibilidad**: Evalúa factibilidad técnica, de recursos y temporal
- **Validación de Testeabilidad**: Verifica criterios medibles, condiciones verificables, posibilidad de automatización
- **Validación de Estándares**: Verifica cumplimiento ISO/IEC/IEEE 29148

#### ✅ Generación de Casos de Prueba
- Creación automática de casos de prueba desde requisitos
- Extracción de precondiciones y pasos de prueba
- Generación de resultados esperados
- Determinación de automatización posible

#### ✅ Framework de Aceptación
- Simulación de ejecución de pruebas
- Cálculo de métricas de cobertura
- Determinación de estado de aceptación
- Reportes detallados de resultados

#### ✅ Dashboard Interactivo
- Interfaz web responsive con navegación por pestañas
- Visualización de métricas con gráficos Chart.js
- Filtros y búsqueda en resultados
- Actualizaciones en tiempo real
- Notificaciones de usuario

#### ✅ Reportes y Exportación
- Reportes en formato Markdown
- Exportación a JSON para integración
- Exportación a HTML con estilos
- Métricas detalladas de calidad

### Estructura de Datos

#### Formato de Requisitos (JSON)
```json
{
  "requirements": [
    {
      "id": "REQ-001",
      "text": "Descripción del requisito",
      "type": "functional|security|usability|performance",
      "priority": "high|medium|low",
      "acceptance_criteria": [
        "Criterio 1",
        "Criterio 2"
      ]
    }
  ]
}
```

#### Resultados de Validación
```python
{
  "session_id": "uuid-v4",
  "timestamp": "ISO-8601",
  "total_requirements": 15,
  "overall_score": 85.5,
  "validation_types": {
    "completeness": {"score": 90, "issues": []},
    "consistency": {"score": 85, "issues": []},
    "feasibility": {"score": 80, "issues": []},
    "testability": {"score": 88, "issues": []},
    "standards_compliance": {"score": 82, "issues": []}
  },
  "passed_requirements": ["REQ-001", "REQ-002"],
  "failed_requirements": [{"id": "REQ-003", "issues": ["..."]}],
  "issues": [...],
  "recommendations": [...]
}
```

### API del Motor de Validación

#### Métodos Principales
- `load_requirements(file_path)` - Carga requisitos desde archivo JSON
- `validate_requirements()` - Ejecuta validación completa
- `generate_test_cases()` - Genera casos de prueba
- `perform_acceptance_testing()` - Ejecuta testing de aceptación
- `validate_against_standards()` - Valida contra estándares ISO
- `generate_validation_report()` - Genera reporte comprehensivo
- `export_validation_results(format, file_path)` - Exporta resultados

### Casos de Prueba Incluidos

La suite de pruebas incluye:
- ✅ Inicialización del motor
- ✅ Carga de requisitos (éxito y error)
- ✅ Validación por tipo (completitud, consistencia, etc.)
- ✅ Generación de casos de prueba
- ✅ Testing de aceptación
- ✅ Validación de estándares
- ✅ Generación de reportes
- ✅ Exportación de resultados
- ✅ Detección de conflictos
- ✅ Validación de criterios medibles

### Métricas y KPIs

#### Métricas de Validación
- **Puntuación General**: Promedio de todas las validaciones (0-100)
- **Tasa de Aprobación**: Porcentaje de requisitos que pasan validación
- **Cobertura de Testing**: Porcentaje de requisitos con casos de prueba
- **Cumplimiento de Estándares**: Puntuación contra ISO/IEC/IEEE 29148

#### Métricas de Calidad
- **Completitud**: Campos requeridos presentes
- **Consistencia**: Sin conflictos ni duplicados
- **Testeabilidad**: Criterios medibles y verificables
- **Factibilidad**: Requisitos realistas técnicamente

### Solución de Problemas

#### Problemas Comunes

1. **Error de importación**
   ```bash
   # Asegurar que todos los archivos estén en el mismo directorio
   ls -la *.py
   ```

2. **Dashboard no carga**
   - Verificar que Chart.js CDN esté accesible
   - Abrir consola del navegador para errores JavaScript
   - Verificar que todos los archivos CSS/JS estén presentes

3. **Pruebas fallan**
   ```bash
   # Ejecutar pruebas individuales
   python -m unittest validation_test_suite.TestValidationEngine.test_initialization
   ```

4. **Resultados de validación bajos**
   - Revisar formato de datos en `validation_requirements.json`
   - Verificar que los requisitos tengan campos requeridos
   - Asegurar criterios de aceptación completos

### Extensiones Sugeridas

#### Mejoras al Motor
- Integración con bases de datos
- Validación en tiempo real durante edición
- Machine learning para detección de patrones
- Integración con herramientas de gestión de requisitos

#### Mejoras al Dashboard
- Autenticación de usuarios
- Colaboración en tiempo real
- Exportación a PDF
- Temas oscuros/claros

#### Integraciones
- Jira, Azure DevOps, IBM DOORS
- Jenkins, GitLab CI, GitHub Actions
- Slack, Microsoft Teams para notificaciones

### Referencias

#### Estándares
- **ISO/IEC/IEEE 29148:2018** - Ingeniería de sistemas y software - Requisitos de software
- **IEEE 830-1998** - Guía recomendada para especificación de requisitos de software
- **ISO 9241-11:2018** - Ergonomía de la interacción persona-sistema

#### Recursos Adicionales
- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Python Testing Documentation](https://docs.python.org/3/library/unittest.html)
- [Web APIs MDN](https://developer.mozilla.org/en-US/docs/Web/API)

### Soporte

Para soporte técnico o preguntas sobre el laboratorio:
1. Revisar esta documentación completa
2. Ejecutar la suite de pruebas para verificar funcionalidad
3. Verificar logs de error en consola
4. Consultar issues en el repositorio del curso

---

**Nota**: Este laboratorio proporciona una implementación completa y funcional de un sistema de validación de requisitos según estándares internacionales. El código está diseñado para ser extensible y se puede adaptar a diferentes contextos de proyecto.
