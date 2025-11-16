# Laboratorio 5: Validación de Requisitos

## Problema

### Introducción
En este laboratorio, trabajarás en la validación de requisitos siguiendo el estándar ISO/IEC/IEEE 29148. Has recibido código con errores intencionales que debes corregir para crear un sistema completo de validación de requisitos.

### Código con Errores Intencionales

#### 1. Motor de Validación con Errores
Crea un archivo `validation_engine.py` con el siguiente código que contiene errores:

```python
# validation_engine.py - CÓDIGO CON ERRORES

import json
import re
from typing import List, Dict, Any, Tuple
from datetime import datetime
import statistics
from collections import defaultdict

class ValidationEngine:
    def __init__(self):
        self.requirements = []
        self.validation_results = {}
        self.test_cases = []
        # ERROR: Falta inicializar reglas de validación
    
    def load_requirements(self, file_path: str) -> bool:
        """Cargar requisitos desde archivo"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.requirements = data.get('requirements', [])
                return True
        except:
            return False
    
    def validate_requirements(self) -> Dict[str, Any]:
        """Validar todos los requisitos"""
        # ERROR: Solo validación básica
        results = {
            'total_requirements': len(self.requirements),
            'passed': 0,
            'failed': 0,
            'issues': []
        }
        
        for req in self.requirements:
            # ERROR: No hay lógica de validación real
            results['passed'] += 1
        
        return results
    
    def generate_test_cases(self) -> List[Dict[str, Any]]:
        """Generar casos de prueba desde requisitos"""
        # ERROR: Generación de casos de prueba vacía
        return []
    
    def perform_acceptance_testing(self) -> Dict[str, Any]:
        """Realizar pruebas de aceptación"""
        # ERROR: No hay implementación de pruebas de aceptación
        return {'status': 'not_implemented'}
    
    def validate_against_standards(self) -> Dict[str, Any]:
        """Validar contra ISO/IEC/IEEE 29148"""
        # ERROR: No hay validación de estándares
        return {'compliant': True}
```

#### 2. Dashboard de Validación con Errores
Crea un archivo `validation_dashboard.html` con interfaz básica:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Dashboard de Validación</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .section { margin-bottom: 20px; }
        .metric { background: #f0f0f0; padding: 10px; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Dashboard de Validación de Requisitos</h1>
    
    <div class="section">
        <h2>Resultados de Validación</h2>
        <div id="results">
            <!-- ERROR: Sección de resultados vacía -->
        </div>
    </div>
    
    <div class="section">
        <h2>Casos de Prueba</h2>
        <div id="testCases">
            <!-- ERROR: Sección de casos de prueba vacía -->
        </div>
    </div>

    <script>
        // ERROR: No hay funcionalidad JavaScript
        console.log('Dashboard cargado');
    </script>
</body>
</html>
```

### Tareas a Realizar

#### Tarea 1: Corregir el Motor de Validación
1. **Inicializar reglas de validación correctamente**
2. **Implementar métodos de validación comprehensivos**:
   - Validación de completitud
   - Validación de consistencia
   - Validación de factibilidad
   - Validación de testeabilidad
   - Cumplimiento de estándares
3. **Generar casos de prueba automáticamente** desde requisitos
4. **Implementar framework de pruebas de aceptación**
5. **Agregar verificación de cumplimiento ISO/IEC/IEEE 29148**

#### Tarea 2: Completar el Dashboard de Validación
1. **Crear display comprehensivo de métricas de validación**
2. **Implementar interfaz de gestión de casos de prueba**
3. **Agregar controles de pruebas de aceptación**
4. **Crear reportes de cumplimiento**
5. **Agregar gráficos de validación interactivos**

#### Tarea 3: Crear Archivos de Soporte
1. **CSS completo** (`validation_styles.css`) con diseño moderno
2. **JavaScript funcional** (`validation_scripts.js`) con todas las características
3. **Datos de ejemplo** (`validation_requirements.json`) con requisitos completos
4. **Suite de pruebas** (`test_validation_engine.py`) con cobertura completa

### Problemas Específicos a Resolver

1. **Reglas de validación faltantes**: No hay criterios para validación de requisitos
2. **Lógica de validación incompleta**: Solo conteo básico de aprobado/fallado
3. **Generación de casos de prueba vacía**: No hay creación automática de casos de prueba
4. **Pruebas de aceptación faltantes**: No hay implementación de criterios de aceptación
5. **Interfaz pobre**: HTML básico sin funcionalidad
6. **Verificación de cumplimiento faltante**: Falta validación de estándares ISO
7. **Reportes limitados**: No hay reportes detallados de validación

### Resultados Esperados
- Motor de validación completamente funcional
- Dashboard web interactivo con todas las características
- Generación automática de casos de prueba desde requisitos
- Framework de pruebas de aceptación
- Validación de cumplimiento ISO/IEC/IEEE 29148
- Reportes comprehensivos de validación

### Archivos a Crear
1. `validation_engine.py` (corregido)
2. `validation_dashboard.html` (completo)
3. `validation_styles.css`
4. `validation_scripts.js`
5. `validation_requirements.json`
6. `test_validation_engine.py`

### Criterios de Éxito
- ✅ Código Python ejecuta sin errores
- ✅ Todos los tipos de validación implementados
- ✅ Casos de prueba generados automáticamente
- ✅ Framework de pruebas de aceptación funcional
- ✅ Interfaz web operativa
- ✅ Todas las pruebas pasan
