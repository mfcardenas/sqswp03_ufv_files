# Laboratorio 3: Análisis y Modelado de Requisitos

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

## 📝 **Descripción del Problema**

### **Situación**
Eres parte de un equipo de ingeniería de requisitos que está trabajando en un sistema de automatización del hogar inteligente. El equipo ha recopilado una lista inicial de requisitos del cliente, pero estos requisitos necesitan ser analizados y modelados antes de proceder con el desarrollo.

### **Problema Principal**
Los requisitos recopilados tienen varios problemas:
- Algunos son ambiguos y vagos
- Faltan elementos importantes en varios requisitos
- No hay categorización clara de los tipos de requisitos
- No se han identificado dependencias entre requisitos
- No existe priorización para guiar la implementación

### **Tu Tarea**
Debes crear una herramienta completa de análisis y modelado de requisitos que:

1. **Analice automáticamente** la calidad de los requisitos
2. **Categorice** los requisitos por tipo
3. **Identifique dependencias** entre requisitos
4. **Genere múltiples modelos** de requisitos
5. **Proporcione un dashboard web** para visualización interactiva
6. **Permita priorización** basada en múltiples factores

### **Archivos con Problemas**

#### **1. requirements_analysis.py (Motor de Análisis)**
Este archivo contiene múltiples bugs que debes corregir:

```python
# requirements_analysis.py - CONTiene ERRORES INTENCIONALES

import json
import re
from typing import List, Dict, Any, Tuple, Optional
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime

class RequirementsAnalyzer:
    def __init__(self):
        self.requirements = []
        self.issues = []
        self.analysis_results = {}
    
    def load_requirements(self, file_path: str) -> bool:
        """Cargar requisitos desde archivo JSON"""
        # BUG: Sin manejo de errores
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.requirements = data.get('requirements', [])
            return True
    
    def analyze_requirements(self) -> Dict[str, Any]:
        """Análisis completo de requisitos"""
        self.analysis_results = {
            'total_requirements': len(self.requirements),
            'quality_score': 0,
            'issues_found': [],
            'recommendations': [],
            'quality_metrics': {},
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        if not self.requirements:
            return self.analysis_results
        
        # BUG: Loop incorrecto - no procesa todos los requisitos
        for req in self.requirements[:2]:  # Solo procesa los primeros 2
            issues = self._analyze_single_requirement(req)
            self.analysis_results['issues_found'].extend(issues)
        
        # BUG: Cálculo de métricas de calidad incorrecto
        self.analysis_results['quality_metrics'] = self._calculate_quality_metrics()
        
        # BUG: Puntaje de calidad no calculado
        # self.analysis_results['quality_score'] = self._calculate_quality_score()
        
        # BUG: Recomendaciones no generadas
        # self.analysis_results['recommendations'] = self._generate_recommendations()
        
        return self.analysis_results
    
    def _analyze_single_requirement(self, requirement: Dict[str, Any]) -> List[str]:
        """Analizar un solo requisito para problemas de calidad"""
        issues = []
        req_id = requirement.get('id', 'Unknown')
        text = requirement.get('text', '')
        
        # BUG: Detección de ambigüedad incompleta
        if self.check_ambiguity(text):
            issues.append(f"Ambiguous: {req_id}")
        
        # BUG: Verificación de completitud incorrecta
        if not self.check_completeness(text):
            issues.append(f"Incomplete: {req_id}")
        
        # BUG: Verificación de consistencia no implementada
        # if self._check_basic_consistency(text):
        #     issues.append(f"Potentially inconsistent: {req_id}")
        
        return issues
    
    def check_ambiguity(self, text: str) -> bool:
        """Detección de ambigüedad mejorada"""
        text_lower = text.lower()
        
        # BUG: Lista incompleta de indicadores ambiguos
        ambiguous_indicators = [
            'etc', 'and/or'
            # Faltan muchos indicadores
        ]
        
        # BUG: Solo verifica indicadores, ignora otros patrones
        for indicator in ambiguous_indicators:
            if indicator in text_lower:
                return True
        
        return False
    
    def check_completeness(self, text: str) -> bool:
        """Verificar si el requisito es completo"""
        # BUG: Verificación demasiado simple
        return len(text.split()) > 3  # Solo verifica longitud
    
    def _check_basic_consistency(self, text: str) -> bool:
        """Verificación básica de consistencia"""
        # BUG: Método vacío - no implementado
        return False
    
    def _calculate_quality_metrics(self) -> Dict[str, float]:
        """Calcular métricas de calidad detalladas"""
        if not self.requirements:
            return {}
        
        total_reqs = len(self.requirements)
        issues_count = len(self.analysis_results['issues_found'])
        
        # BUG: Cálculos incorrectos
        return {
            'completeness_ratio': issues_count / total_reqs,  # Incorrecto
            'ambiguity_ratio': 0.0,  # No calculado
            'consistency_ratio': 1.0,  # Siempre 1.0
            'average_length': 0.0  # No calculado
        }
    
    def _calculate_quality_score(self) -> float:
        """Calcular puntaje de calidad general (0-100)"""
        # BUG: Método vacío
        return 0.0
    
    def _generate_recommendations(self) -> List[str]:
        """Generar recomendaciones de mejora"""
        # BUG: Método vacío
        return []
    
    def categorize_requirements(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorización mejorada de requisitos"""
        categories = defaultdict(list)
        
        for req in self.requirements:
            text = req.get('text', '').lower()
            req_id = req.get('id', '')
            
            # BUG: Lógica de categorización incorrecta
            if 'control' in text:
                categories['functional'].append(req)
            elif 'security' in text:
                categories['functional'].append(req)  # BUG: Todo va a functional
            else:
                categories['other'].append(req)
        
        return dict(categories)
    
    def identify_dependencies(self) -> List[Tuple[str, str, str]]:
        """Identificar dependencias entre requisitos"""
        # BUG: Método vacío
        return []
    
    def _check_dependency(self, req1: Dict[str, Any], req2: Dict[str, Any]) -> Optional[str]:
        """Verificar si dos requisitos tienen dependencia"""
        # BUG: Método vacío
        return None
    
    def prioritize_requirements(self) -> List[Dict[str, Any]]:
        """Priorización multi-factor de requisitos"""
        # BUG: Método vacío
        return []
    
    def _calculate_priority_score(self, requirement: Dict[str, Any]) -> float:
        """Calcular puntaje de prioridad basado en múltiples factores"""
        # BUG: Método vacío
        return 0.0
    
    def generate_models(self) -> Dict[str, Any]:
        """Generar diferentes tipos de modelos de requisitos"""
        # BUG: Modelos no generados
        return {}
    
    def _generate_functional_hierarchy(self) -> Dict[str, Any]:
        """Generar modelo de jerarquía funcional"""
        # BUG: Método vacío
        return {}
    
    def _generate_data_flow_model(self) -> Dict[str, Any]:
        """Generar modelo de flujo de datos"""
        # BUG: Método vacío
        return {}
    
    def _generate_state_machine(self) -> Dict[str, Any]:
        """Generar modelo de máquina de estados"""
        # BUG: Método vacío
        return {}
    
    def _generate_use_case_model(self) -> Dict[str, Any]:
        """Generar modelo de casos de uso"""
        # BUG: Método vacío
        return {}
    
    def _generate_dependency_graph(self) -> Dict[str, Any]:
        """Generar grafo de dependencias"""
        # BUG: Método vacío
        return {}
    
    def generate_report(self) -> str:
        """Generar reporte completo de análisis"""
        if not self.analysis_results:
            self.analyze_requirements()
        
        # BUG: Reporte básico sin contenido real
        report = f"""
# Reporte de Análisis de Requisitos
Total de requisitos: {self.analysis_results['total_requirements']}
"""
        
        return report
    
    def export_analysis(self, file_path: str):
        """Exportar resultados de análisis a archivo JSON"""
        # BUG: Método vacío
        pass
```

#### **2. modeling_dashboard.html (Dashboard Web)**
Archivo HTML incompleto con estructura básica pero funcionalidad faltante:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Modelado de Requisitos</title>
    <!-- BUG: CSS no vinculado -->
    <!-- <link rel="stylesheet" href="modeling_styles.css"> -->
</head>
<body>
    <header>
        <h1>Análisis y Modelado de Requisitos</h1>
        <!-- BUG: Navegación incompleta -->
        <nav>
            <button>Analysis</button>
            <button>Modeling</button>
        </nav>
    </header>

    <main>
        <!-- BUG: Solo una sección implementada -->
        <section id="analysisSection">
            <h2>Análisis de Requisitos</h2>
            <!-- BUG: Controles faltantes -->
            <div id="analysisContent">
                <p>Cargar análisis...</p>
            </div>
        </section>

        <!-- BUG: Secciones faltantes -->
    </main>

    <!-- BUG: JavaScript no vinculado -->
    <!-- <script src="modeling_scripts.js"></script> -->
</body>
</html>
```

#### **3. modeling_styles.css (Estilos)**
Archivo CSS casi vacío:

```css
/* BUG: Estilos mínimos */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

/* BUG: Falta la mayoría de estilos */
```

#### **4. modeling_scripts.js (Funcionalidad JavaScript)**
Archivo JavaScript con estructura básica pero funcionalidad faltante:

```javascript
// BUG: Funcionalidad mínima
document.addEventListener('DOMContentLoaded', function() {
    // BUG: Navegación no implementada
    console.log('Dashboard cargado');
    
    // BUG: Funciones faltantes
});
```

### **Datos de Prueba**
Crear un archivo `sample_requirements.json` con datos de prueba:

```json
{
  "requirements": [
    {
      "id": "FR1",
      "text": "El sistema debe controlar las luces basándose en tiempo y movimiento",
      "type": "functional",
      "priority": "high"
    },
    {
      "id": "FR2", 
      "text": "El sistema debe proporcionar monitoreo de seguridad con cámaras y sensores",
      "type": "functional",
      "priority": "high"
    },
    {
      "id": "FR3",
      "text": "El sistema debe controlar la temperatura automáticamente y manualmente",
      "type": "functional", 
      "priority": "medium"
    },
    {
      "id": "NFR1",
      "text": "El sistema debe responder dentro de 2 segundos a comandos del usuario",
      "type": "non_functional",
      "priority": "high"
    },
    {
      "id": "NFR2",
      "text": "El sistema debe estar disponible el 99.9% del tiempo",
      "type": "non_functional",
      "priority": "high"
    },
    {
      "id": "C1",
      "text": "El sistema debe usar protocolos de comunicación inalámbrica",
      "type": "constraint",
      "priority": "medium"
    },
    {
      "id": "C2",
      "text": "El sistema debe costar menos de $500 para instalación básica",
      "type": "constraint",
      "priority": "medium"
    }
  ]
}
```

## ✅ **Criterios de Éxito**
- El motor de análisis funciona correctamente sin errores
- Los requisitos se analizan completamente con métricas precisas
- Los modelos se generan y visualizan correctamente
- El dashboard web es completamente funcional
- Todas las pruebas unitarias pasan
- El código está bien documentado y es mantenible

## 🎯 **Entregables Esperados**
1. `requirements_analysis.py` - Motor de análisis corregido y completo
2. `modeling_dashboard.html` - Interfaz web completa
3. `modeling_styles.css` - Estilos completos y responsivos
4. `modeling_scripts.js` - Funcionalidad JavaScript completa
5. `test_requirements_analysis.py` - Suite de pruebas unitarias
6. `sample_requirements.json` - Datos de prueba
7. Documentación de las correcciones realizadas

¡Este laboratorio te dará experiencia práctica en las técnicas fundamentales del análisis y modelado de requisitos según la norma ISO/IEC/IEEE 29148!
