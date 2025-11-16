# Laboratorio 4: Especificación de Requisitos

## Problema

### Introducción
En este laboratorio, trabajarás en la especificación de requisitos siguiendo el estándar ISO/IEC/IEEE 29148. Has recibido código con errores intencionales que debes corregir para crear un sistema completo de especificación de requisitos.

### Código con Errores Intencionales

#### 1. Generador de Especificaciones Defectuoso
Crea un archivo `specification_generator.py` con el siguiente código que contiene errores:

```python
# specification_generator.py - CÓDIGO CON ERRORES

import json
import yaml
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import re
from collections import defaultdict
import uuid

class SpecificationGenerator:
    def __init__(self):
        self.requirements = []
        self.specifications = {}
        self.traceability_matrix = {}
        self.baselines = {}
        # ERROR: Falta inicializar el ID de especificación
    
    def load_requirements(self, file_path: str) -> bool:
        """Load requirements from JSON file with error handling"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.requirements = data.get('requirements', [])
                print(f"Successfully loaded {len(self.requirements)} requirements")
                return True
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
            self.requirements = []
            return False
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format - {e}")
            self.requirements = []
            return False
    
    def generate_srs(self) -> Dict[str, Any]:
        """Generate complete Software Requirements Specification"""
        # ERROR: No genera SRS completo, falta muchas secciones
        srs = {
            'id': 'SPEC-001',
            'title': 'Software Requirements Specification',
            'version': '1.0',
            'date': datetime.now().isoformat(),
            'status': 'Draft'
        }
        
        # ERROR: Solo genera una sección básica
        srs['sections'] = {
            'introduction': {'purpose': 'Basic purpose'}
        }
        
        self.specifications['srs'] = srs
        return srs
    
    def apply_specification_formats(self) -> Dict[str, Any]:
        """Apply different specification formats to requirements"""
        # ERROR: Solo implementa formato textual básico
        formats = {
            'textual': [f"{req['id']}: {req['text']}" for req in self.requirements]
        }
        return formats
    
    def create_traceability_matrix(self) -> Dict[str, Any]:
        """Create comprehensive requirements traceability matrix"""
        # ERROR: Matriz de trazabilidad incompleta
        matrix = {
            'requirements': [req['id'] for req in self.requirements],
            'design_elements': [],
            'test_cases': [],
            'traceability_links': []
        }
        
        self.traceability_matrix = matrix
        return matrix
    
    def validate_specifications(self) -> Dict[str, Any]:
        """Validate specifications against quality criteria"""
        # ERROR: Validación básica sin criterios completos
        validation_results = {
            'overall_score': 50,
            'issues': ['Validation not fully implemented']
        }
        return validation_results
    
    def create_baseline(self, version: str) -> Dict[str, Any]:
        """Create requirement baseline with version control"""
        # ERROR: Baseline sin información completa
        baseline = {
            'version': version,
            'timestamp': datetime.now().isoformat(),
            'requirements': self.requirements
        }
        
        self.baselines[version] = baseline
        return baseline
    
    def export_specifications(self, format_type: str, file_path: str):
        """Export specifications in different formats"""
        # ERROR: Solo exporta JSON
        if format_type == 'json':
            with open(file_path, 'w') as f:
                json.dump(self.specifications, f, indent=2, default=str)
        else:
            print(f"Format {format_type} not supported")
```

#### 2. Visor de Especificaciones Incompleto
Crea un archivo `specification_viewer.html` con interfaz básica:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visor de Especificaciones</title>
    <style>
        /* ERROR: CSS muy básico */
        body { font-family: Arial, sans-serif; margin: 20px; }
        .section { margin-bottom: 20px; }
        .requirement { background: #f0f0f0; padding: 10px; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Visor de Especificaciones de Requisitos</h1>
    
    <!-- ERROR: Falta navegación completa -->
    <div id="content">
        <div class="section">
            <h2>Requisitos</h2>
            <div id="requirementsList">
                <!-- ERROR: Lista vacía -->
            </div>
        </div>
    </div>

    <script>
        // ERROR: JavaScript muy básico sin funcionalidad
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Visor cargado');
        });
    </script>
</body>
</html>
```

### Tareas a Realizar

#### Tarea 1: Corregir el Generador de Especificaciones
1. **Inicializar correctamente** el ID de especificación
2. **Implementar generación completa de SRS** con todas las secciones requeridas
3. **Aplicar múltiples formatos** de especificación (textual, tabular, gráfico, formal)
4. **Crear matriz de trazabilidad completa** con enlaces apropiados
5. **Implementar validación completa** con criterios de calidad
6. **Agregar gestión de baselines** con control de versiones
7. **Implementar exportación múltiple** (JSON, YAML, HTML)

#### Tarea 2: Completar el Visor Interactivo
1. **Crear navegación completa** con pestañas para diferentes secciones
2. **Implementar visualización de requisitos** con filtros y búsqueda
3. **Agregar gráficos de calidad** usando Chart.js
4. **Crear interfaz de trazabilidad** con matrices interactivas
5. **Implementar sistema de validación** con indicadores visuales
6. **Agregar funcionalidad de reportes** y exportación

#### Tarea 3: Crear Archivos de Soporte
1. **CSS completo** (`specification_styles.css`) con diseño moderno
2. **JavaScript funcional** (`specification_scripts.js`) con todas las características
3. **Datos de ejemplo** (`sample_requirements.json`) con requisitos completos
4. **Suite de pruebas** (`test_specification_generator.py`) con cobertura completa

### Problemas Específicos a Resolver

1. **Generación SRS incompleta**: El código actual solo genera una sección básica
2. **Formatos limitados**: Solo implementa formato textual simple
3. **Trazabilidad faltante**: No hay enlaces entre requisitos, diseño y pruebas
4. **Validación básica**: Solo retorna puntuación fija sin análisis real
5. **Interfaz pobre**: Visor HTML muy básico sin funcionalidad
6. **Exportación limitada**: Solo soporta formato JSON
7. **Gestión de baselines incompleta**: No incluye comparación ni historial

### Resultados Esperados
- Generador de especificaciones completamente funcional
- Visor web interactivo con todas las características
- Sistema de trazabilidad operativo
- Validación automática de calidad
- Múltiples formatos de exportación
- Suite de pruebas completa

### Archivos a Crear
1. `specification_generator.py` (corregido)
2. `specification_viewer.html` (completo)
3. `specification_styles.css`
4. `specification_scripts.js`
5. `sample_requirements.json`
6. `test_specification_generator.py`

### Criterios de Éxito
- ✅ Código Python ejecuta sin errores
- ✅ SRS completo generado correctamente
- ✅ Múltiples formatos aplicados
- ✅ Matriz de trazabilidad funcional
- ✅ Validación de calidad implementada
- ✅ Interfaz web operativa
- ✅ Todos los tests pasan
