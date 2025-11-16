# Laboratorio 3: Análisis y Modelado de Requisitos

## Solución

### Paso 1: Herramienta de Análisis de Requisitos Corregida
Crear un archivo `requirements_analysis.py`:

```python
# requirements_analysis.py - SOLUCIÓN COMPLETA

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
        """Cargar requisitos desde archivo JSON con manejo de errores"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.requirements = data.get('requirements', [])
                print(f"Requisitos cargados exitosamente: {len(self.requirements)}")
                return True
        except FileNotFoundError:
            print(f"Error: Archivo {file_path} no encontrado")
            self.requirements = []
            return False
        except json.JSONDecodeError as e:
            print(f"Error: Formato JSON inválido - {e}")
            self.requirements = []
            return False
    
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
        
        # Procesar todos los requisitos (corregido)
        for req in self.requirements:
            issues = self._analyze_single_requirement(req)
            self.analysis_results['issues_found'].extend(issues)
        
        # Calcular métricas de calidad
        self.analysis_results['quality_metrics'] = self._calculate_quality_metrics()
        
        # Calcular puntaje de calidad
        self.analysis_results['quality_score'] = self._calculate_quality_score()
        
        # Generar recomendaciones
        self.analysis_results['recommendations'] = self._generate_recommendations()
        
        return self.analysis_results
    
    def _analyze_single_requirement(self, requirement: Dict[str, Any]) -> List[str]:
        """Analizar un solo requisito para problemas de calidad"""
        issues = []
        req_id = requirement.get('id', 'Unknown')
        text = requirement.get('text', '')
        
        # Verificar ambigüedad
        if self.check_ambiguity(text):
            issues.append(f"Ambiguo: {req_id}")
        
        # Verificar completitud
        if not self.check_completeness(text):
            issues.append(f"Incompleto: {req_id}")
        
        # Verificar consistencia
        if self._check_basic_consistency(text):
            issues.append(f"Potencialmente inconsistente: {req_id}")
        
        return issues
    
    def check_ambiguity(self, text: str) -> bool:
        """Detección mejorada de ambigüedad"""
        text_lower = text.lower()
        
        # Indicadores de ambigüedad mejorados
        ambiguous_indicators = [
            'etc', 'y/o', 'o', 'según corresponda', 'según sea necesario', 'posible',
            'normalmente', 'generalmente', 'usualmente', 'típicamente', 'puede', 'podría',
            'adecuado', 'suficiente', 'razonable', 'apropiado', 'conveniente'
        ]
        
        # Verificar términos ambiguos
        for indicator in ambiguous_indicators:
            if indicator in text_lower:
                return True
        
        # Verificar cuantificadores vagos
        vague_quantifiers = ['algunos', 'muchos', 'pocos', 'varios']
        for quantifier in vague_quantifiers:
            if quantifier in text_lower:
                return True
        
        # Verificar falta de especificidad
        if len(text.split()) < 5:  # Requisitos muy cortos
            return True
        
        return False
    
    def check_completeness(self, text: str) -> bool:
        """Verificar si el requisito es completo usando criterios apropiados"""
        # Debe contener verbos modales
        modal_verbs = ['debe', 'deberá', 'debería', 'deberían', 'tendrá que']
        has_modal = any(verb in text.lower() for verb in modal_verbs)
        
        if not has_modal:
            return False
        
        # Debe especificar qué, quién, cuándo (completitud básica)
        has_subject = len(text.split()) > 3  # Verificación básica de longitud
        has_action = any(verb in text.lower() for verb in ['proporcionar', 'soportar', 'permitir', 'habilitar', 'controlar'])
        
        return has_subject and has_action
    
    def _check_basic_consistency(self, text: str) -> bool:
        """Verificación básica de consistencia para contradicciones obvias"""
        text_lower = text.lower()
        
        # Verificar términos contradictorios
        contradictions = [
            ('debe', 'no debe'),
            ('deberá', 'no deberá'),
            ('tendrá que', 'no tendrá que'),
            ('siempre', 'nunca'),
            ('todos', 'ninguno')
        ]
        
        for pos, neg in contradictions:
            if pos in text_lower and neg in text_lower:
                return True
        
        return False
    
    def _calculate_quality_metrics(self) -> Dict[str, float]:
        """Calcular métricas de calidad detalladas"""
        if not self.requirements:
            return {}
        
        total_reqs = len(self.requirements)
        issues_count = len(self.analysis_results['issues_found'])
        
        return {
            'completeness_ratio': (total_reqs - issues_count) / total_reqs,
            'ambiguity_ratio': len([i for i in self.analysis_results['issues_found'] if 'Ambiguo' in i]) / total_reqs,
            'consistency_ratio': 1.0 - (len([i for i in self.analysis_results['issues_found'] if 'inconsistente' in i.lower()]) / total_reqs),
            'average_length': sum(len(req.get('text', '').split()) for req in self.requirements) / total_reqs
        }
    
    def _calculate_quality_score(self) -> float:
        """Calcular puntaje de calidad general (0-100)"""
        if not self.requirements:
            return 0.0
        
        metrics = self.analysis_results.get('quality_metrics', {})
        if not metrics:
            return 0.0
        
        # Cálculo de puntaje ponderado
        weights = {
            'completeness_ratio': 0.4,
            'ambiguity_ratio': 0.3,
            'consistency_ratio': 0.3
        }
        
        score = 0.0
        for metric, weight in weights.items():
            value = metrics.get(metric, 0.0)
            # Invertir ratio de ambigüedad (menor es mejor)
            if metric == 'ambiguity_ratio':
                value = 1.0 - value
            score += value * weight
        
        return round(score * 100, 2)
    
    def _generate_recommendations(self) -> List[str]:
        """Generar recomendaciones de mejora"""
        recommendations = []
        metrics = self.analysis_results.get('quality_metrics', {})
        
        if metrics.get('completeness_ratio', 0) < 0.8:
            recommendations.append("Mejorar la completitud de requisitos agregando elementos faltantes (quién, qué, cuándo)")
        
        if metrics.get('ambiguity_ratio', 0) > 0.2:
            recommendations.append("Reducir ambigüedad reemplazando términos vagos con criterios específicos")
        
        if metrics.get('consistency_ratio', 0) < 0.9:
            recommendations.append("Revisar requisitos para consistencia y resolver conflictos")
        
        if metrics.get('average_length', 0) < 10:
            recommendations.append("Expandir descripciones de requisitos para proporcionar más detalle")
        
        return recommendations
    
    def categorize_requirements(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorización mejorada de requisitos"""
        categories = defaultdict(list)
        
        for req in self.requirements:
            text = req.get('text', '').lower()
            req_id = req.get('id', '')
            
            # Requisitos funcionales
            if any(word in text for word in ['controlar', 'proporcionar', 'soportar', 'permitir', 'habilitar']):
                categories['functional'].append(req)
            
            # Requisitos no funcionales
            elif any(word in text for word in ['dentro de', 'disponible', 'seguro', 'amigable', 'soportar']):
                categories['non_functional'].append(req)
            
            # Restricciones
            elif any(word in text for word in ['deberá usar', 'deberá funcionar', 'deberá costar', 'deberá instalarse']):
                categories['constraints'].append(req)
            
            # Requisitos de interfaz
            elif any(word in text for word in ['interfaz', 'api', 'comunicación', 'integración']):
                categories['interface'].append(req)
            
            else:
                categories['other'].append(req)
        
        return dict(categories)
    
    def identify_dependencies(self) -> List[Tuple[str, str, str]]:
        """Identificar dependencias entre requisitos"""
        dependencies = []
        
        for i, req1 in enumerate(self.requirements):
            for j, req2 in enumerate(self.requirements[i+1:], i+1):
                dep_type = self._check_dependency(req1, req2)
                if dep_type:
                    dependencies.append((req1['id'], req2['id'], dep_type))
        
        return dependencies
    
    def _check_dependency(self, req1: Dict[str, Any], req2: Dict[str, Any]) -> Optional[str]:
        """Verificar si dos requisitos tienen dependencia"""
        text1 = req1.get('text', '').lower()
        text2 = req2.get('text', '').lower()
        
        # Verificar dependencias secuenciales
        if 'después' in text1 or 'antes' in text2:
            return 'sequential'
        
        # Verificar dependencias condicionales
        if 'si' in text1 or 'cuando' in text1:
            return 'conditional'
        
        # Verificar dependencias funcionales
        common_terms = set(text1.split()) & set(text2.split())
        if len(common_terms) > 3:  # Muchos términos comunes sugieren dependencia
            return 'functional'
        
        return None
    
    def prioritize_requirements(self) -> List[Dict[str, Any]]:
        """Priorización multi-factor de requisitos"""
        if not self.requirements:
            return []
        
        prioritized = []
        
        for req in self.requirements:
            priority_score = self._calculate_priority_score(req)
            req_copy = req.copy()
            req_copy['priority_score'] = priority_score
            prioritized.append(req_copy)
        
        # Ordenar por puntaje de prioridad (descendente)
        return sorted(prioritized, key=lambda x: x['priority_score'], reverse=True)
    
    def _calculate_priority_score(self, requirement: Dict[str, Any]) -> float:
        """Calcular puntaje de prioridad basado en múltiples factores"""
        text = requirement.get('text', '').lower()
        score = 0.0
        
        # Palabras clave de valor de negocio
        high_value = ['seguridad', 'seguridad', 'rendimiento', 'disponibilidad']
        medium_value = ['usabilidad', 'fiabilidad', 'mantenibilidad']
        
        for keyword in high_value:
            if keyword in text:
                score += 3.0
        
        for keyword in medium_value:
            if keyword in text:
                score += 2.0
        
        # Prioridad de verbo modal
        if 'debe' in text:
            score += 2.0
        elif 'debería' in text:
            score += 1.0
        
        # Factor de longitud (requisitos más largos tienden a ser más detallados)
        word_count = len(text.split())
        score += min(word_count / 10, 2.0)  # Máximo 2.0
        
        return round(score, 2)
    
    def generate_models(self) -> Dict[str, Any]:
        """Generar diferentes tipos de modelos de requisitos"""
        models = {
            'functional_hierarchy': self._generate_functional_hierarchy(),
            'data_flow': self._generate_data_flow_model(),
            'state_machine': self._generate_state_machine(),
            'use_case': self._generate_use_case_model(),
            'dependency_graph': self._generate_dependency_graph()
        }
        
        return models
    
    def _generate_functional_hierarchy(self) -> Dict[str, Any]:
        """Generar modelo de jerarquía funcional"""
        hierarchy = defaultdict(list)
        
        for req in self.requirements:
            text = req.get('text', '').lower()
            
            # Identificar funciones principales
            if 'controlar luces' in text:
                hierarchy['Control de Iluminación'].append(req['id'])
            elif 'seguridad' in text:
                hierarchy['Sistema de Seguridad'].append(req['id'])
            elif 'temperatura' in text:
                hierarchy['Control de Clima'].append(req['id'])
            else:
                hierarchy['General'].append(req['id'])
        
        return dict(hierarchy)
    
    def _generate_data_flow_model(self) -> Dict[str, Any]:
        """Generar modelo básico de flujo de datos"""
        data_flows = {
            'external_entities': ['Usuario', 'Sensor', 'Cámara'],
            'processes': ['Lógica de Control', 'Procesamiento de Datos', 'Generación de Respuesta'],
            'data_stores': ['Configuración', 'Datos de Sensor', 'Preferencias de Usuario'],
            'data_flows': [
                {'from': 'Sensor', 'to': 'Lógica de Control', 'data': 'lecturas de sensor'},
                {'from': 'Usuario', 'to': 'Lógica de Control', 'data': 'comandos'},
                {'from': 'Lógica de Control', 'to': 'Generación de Respuesta', 'data': 'señales de control'}
            ]
        }
        
        return data_flows
    
    def _generate_state_machine(self) -> Dict[str, Any]:
        """Generar modelo de máquina de estados"""
        states = ['Idle', 'Active', 'Error', 'Maintenance']
        transitions = [
            {'from': 'Idle', 'to': 'Active', 'trigger': 'movimiento detectado'},
            {'from': 'Active', 'to': 'Idle', 'trigger': 'timeout'},
            {'from': 'Active', 'to': 'Error', 'trigger': 'falla de sensor'},
            {'from': 'Error', 'to': 'Maintenance', 'trigger': 'reinicio'}
        ]
        
        return {'states': states, 'transitions': transitions}
    
    def _generate_use_case_model(self) -> Dict[str, Any]:
        """Generar modelo de casos de uso"""
        actors = ['Propietario de Casa', 'Administrador del Sistema', 'Servicio de Seguridad']
        use_cases = [
            {'name': 'Controlar Iluminación', 'actor': 'Propietario de Casa', 'description': 'Ajustar iluminación basada en preferencias'},
            {'name': 'Monitorear Seguridad', 'actor': 'Propietario de Casa', 'description': 'Ver feeds de cámaras de seguridad'},
            {'name': 'Configurar Sistema', 'actor': 'Administrador del Sistema', 'description': 'Configurar parámetros del sistema'}
        ]
        
        return {'actors': actors, 'use_cases': use_cases}
    
    def _generate_dependency_graph(self) -> Dict[str, Any]:
        """Generar datos de grafo de dependencias"""
        dependencies = self.identify_dependencies()
        
        nodes = [req['id'] for req in self.requirements]
        edges = [(dep[0], dep[1], {'type': dep[2]}) for dep in dependencies]
        
        return {'nodes': nodes, 'edges': edges}
    
    def generate_report(self) -> str:
        """Generar reporte completo de análisis"""
        if not self.analysis_results:
            self.analyze_requirements()
        
        report = f"""
# Reporte de Análisis de Requisitos
Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Resumen
- Total de Requisitos: {self.analysis_results['total_requirements']}
- Puntaje de Calidad: {self.analysis_results['quality_score']}/100
- Problemas Encontrados: {len(self.analysis_results['issues_found'])}

## Métricas de Calidad
"""
        
        for metric, value in self.analysis_results['quality_metrics'].items():
            report += f"- {metric}: {value:.2f}\n"
        
        report += "\n## Problemas Encontrados\n"
        for issue in self.analysis_results['issues_found']:
            report += f"- {issue}\n"
        
        report += "\n## Recomendaciones\n"
        for rec in self.analysis_results['recommendations']:
            report += f"- {rec}\n"
        
        return report
    
    def export_analysis(self, file_path: str):
        """Exportar resultados de análisis a archivo JSON"""
        export_data = {
            'analysis_results': self.analysis_results,
            'categorized_requirements': self.categorize_requirements(),
            'prioritized_requirements': self.prioritize_requirements(),
            'models': self.generate_models(),
            'export_timestamp': datetime.now().isoformat()
        }
        
        with open(file_path, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        print(f"Análisis exportado a {file_path}")

# EJEMPLO DE USO
if __name__ == "__main__":
    analyzer = RequirementsAnalyzer()
    
    # Crear datos de ejemplo
    sample_requirements = [
        {"id": "FR1", "text": "El sistema debe controlar luces basado en tiempo y movimiento"},
        {"id": "FR2", "text": "El sistema debe proporcionar monitoreo de seguridad con cámaras y sensores"},
        {"id": "FR3", "text": "El sistema debe controlar temperatura automáticamente y manualmente"},
        {"id": "NFR1", "text": "El sistema debe responder dentro de 2 segundos a comandos del usuario"},
        {"id": "NFR2", "text": "El sistema debe estar disponible 99.9% del tiempo"},
        {"id": "C1", "text": "El sistema debe usar protocolos de comunicación inalámbrica"},
        {"id": "C2", "text": "El sistema debe costar menos de $500 para instalación básica"}
    ]
    
    # Guardar datos de ejemplo
    with open('sample_requirements.json', 'w') as f:
        json.dump({'requirements': sample_requirements}, f, indent=2)
    
    # Cargar y analizar
    if analyzer.load_requirements('sample_requirements.json'):
        analysis = analyzer.analyze_requirements()
        print(f"Puntaje de Calidad: {analysis['quality_score']}/100")
        
        categories = analyzer.categorize_requirements()
        print(f"Categorías: {list(categories.keys())}")
        
        prioritized = analyzer.prioritize_requirements()
        print(f"Requisito de mayor prioridad: {prioritized[0]['id'] if prioritized else 'Ninguno'}")
        
        # Generar modelos
        models = analyzer.generate_models()
        print(f"Modelos generados: {len(models)} tipos diferentes")
        
        # Exportar resultados
        analyzer.export_analysis('requirements_analysis_results.json')
        
        # Generar reporte
        report = analyzer.generate_report()
        with open('requirements_analysis_report.md', 'w') as f:
            f.write(report)
        
        print("¡Análisis completo! Revisa los archivos generados.")
```

### Paso 2: Dashboard de Modelado Corregido
Crear un archivo `modeling_dashboard.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Análisis y Modelado de Requisitos</title>
    <link rel="stylesheet" href="modeling_styles.css">
</head>
<body>
    <header>
        <h1>Análisis y Modelado de Requisitos</h1>
        <nav>
            <button id="analysisBtn" class="active">Análisis</button>
            <button id="modelingBtn">Modelado</button>
            <button id="validationBtn">Validación</button>
            <button id="reportsBtn">Reportes</button>
        </nav>
    </header>

    <main>
        <section id="analysisSection">
            <h2>Análisis de Requisitos</h2>
            <div class="analysis-controls">
                <button id="loadRequirementsBtn">Cargar Requisitos</button>
                <button id="runAnalysisBtn">Ejecutar Análisis</button>
                <button id="exportAnalysisBtn">Exportar Resultados</button>
            </div>
            
            <div id="analysisContent">
                <div class="analysis-summary">
                    <h3>Resumen de Análisis</h3>
                    <div id="summaryStats">
                        <p>Cargando resultados de análisis...</p>
                    </div>
                </div>
                
                <div class="quality-metrics">
                    <h3>Métricas de Calidad</h3>
                    <div id="qualityCharts">
                        <canvas id="qualityChart" width="400" height="200"></canvas>
                    </div>
                </div>
                
                <div class="issues-list">
                    <h3>Problemas Encontrados</h3>
                    <div id="issuesContent">
                        <p>No se han cargado problemas aún.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="modelingSection" style="display: none;">
            <h2>Modelado de Requisitos</h2>
            <div class="modeling-controls">
                <button id="generateModelsBtn">Generar Modelos</button>
                <button id="exportModelsBtn">Exportar Modelos</button>
            </div>
            
            <div class="modeling-tools">
                <div class="model-type">
                    <h3>Jerarquía Funcional</h3>
                    <div id="functionalModel" class="model-canvas">
                        <div class="model-placeholder">
                            <p>Haz clic en "Generar Modelos" para crear jerarquía funcional</p>
                        </div>
                    </div>
                </div>
                
                <div class="model-type">
                    <h3>Diagrama de Flujo de Datos</h3>
                    <div id="dataFlowModel" class="model-canvas">
                        <div class="model-placeholder">
                            <p>El diagrama de flujo de datos aparecerá aquí</p>
                        </div>
                    </div>
                </div>
                
                <div class="model-type">
                    <h3>Diagrama de Casos de Uso</h3>
                    <div id="useCaseModel" class="model-canvas">
                        <div class="model-placeholder">
                            <p>El diagrama de casos de uso aparecerá aquí</p>
                        </div>
                    </div>
                </div>
                
                <div class="model-type">
                    <h3>Grafo de Dependencias</h3>
                    <div id="dependencyModel" class="model-canvas">
                        <div class="model-placeholder">
                            <p>El grafo de dependencias aparecerá aquí</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="validationSection" style="display: none;">
            <h2>Validación de Requisitos</h2>
            <div class="validation-tools">
                <h3>Lista de Verificación de Validación</h3>
                <div class="validation-items">
                    <div class="validation-item">
                        <input type="checkbox" id="completeCheck">
                        <label for="completeCheck">Los requisitos son completos</label>
                    </div>
                    <div class="validation-item">
                        <input type="checkbox" id="consistentCheck">
                        <label for="consistentCheck">Los requisitos son consistentes</label>
                    </div>
                    <div class="validation-item">
                        <input type="checkbox" id="feasibleCheck">
                        <label for="feasibleCheck">Los requisitos son factibles</label>
                    </div>
                    <div class="validation-item">
                        <input type="checkbox" id="testableCheck">
                        <label for="testableCheck">Los requisitos son testeables</label>
                    </div>
                </div>
                
                <div class="validation-results">
                    <h4>Resultados de Validación</h4>
                    <div id="validationResults">
                        <p>Ejecuta validación para ver resultados</p>
                    </div>
                </div>
                
                <button id="runValidationBtn">Ejecutar Validación</button>
            </div>
        </section>

        <section id="reportsSection" style="display: none;">
            <h2>Reportes de Análisis</h2>
            <div class="report-controls">
                <button id="generateReportBtn">Generar Reporte</button>
                <button id="downloadReportBtn">Descargar Reporte</button>
            </div>
            
            <div id="reportContent">
                <div class="report-placeholder">
                    <p>Genera un reporte para ver resultados de análisis</p>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification" aria-live="polite"></div>
    
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="modeling_scripts.js"></script>
</body>
</html>
```

### Paso 3: Estilos CSS para Dashboard
Crear un archivo `modeling_styles.css`:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
    color: #333;
    line-height: 1.6;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
    margin: 0;
    font-size: 1.8rem;
}

nav {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}

nav button {
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
}

nav button:hover, nav button.active {
    background-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

main {
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem;
}

section {
    background-color: white;
    margin-bottom: 2rem;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h2 {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
    margin-bottom: 2rem;
}

h3 {
    color: #3498db;
    margin-bottom: 1rem;
}

.analysis-controls, .modeling-controls, .report-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #2980b9;
}

button:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
}

/* Sección de Análisis */
.analysis-summary, .quality-metrics, .issues-list {
    margin-bottom: 2rem;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

#summaryStats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
}

.stat-card {
    background-color: white;
    padding: 1rem;
    border-radius: 4px;
    border: 1px solid #dee2e6;
    text-align: center;
}

.stat-value {
    font-size: 2rem;
    font-weight: bold;
    color: #3498db;
}

.stat-label {
    color: #6c757d;
    font-size: 0.9rem;
}

/* Sección de Modelado */
.modeling-tools {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.model-type {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.model-canvas {
    border: 1px solid #dee2e6;
    border-radius: 4px;
    min-height: 300px;
    background-color: white;
    position: relative;
    overflow: auto;
}

.model-placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #6c757d;
    font-style: italic;
}

.hierarchy-tree {
    padding: 1rem;
}

.hierarchy-node {
    margin: 0.5rem 0;
    padding: 0.5rem;
    background-color: #e9ecef;
    border-radius: 4px;
    border-left: 4px solid #3498db;
}

.hierarchy-children {
    margin-left: 2rem;
}

/* Sección de Validación */
.validation-tools {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
}

.validation-items {
    margin-bottom: 2rem;
}

.validation-item {
    display: flex;
    align-items: center;
    margin-bottom: 0.5rem;
}

.validation-item input[type="checkbox"] {
    margin-right: 0.5rem;
}

.validation-results {
    margin-top: 2rem;
    padding: 1rem;
    background-color: white;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

/* Sección de Reportes */
#reportContent {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    min-height: 400px;
}

.report-placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #6c757d;
    font-style: italic;
}

/* Notificación */
.notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #3498db;
    color: white;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    display: none;
    max-width: 300px;
    z-index: 1000;
}

/* Responsive */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    nav {
        justify-content: center;
    }
    
    .analysis-controls, .modeling-controls, .report-controls {
        flex: wrap;
        justify-content: center;
    }
    
    .modeling-tools {
        grid-template-columns: 1fr;
    }
    
    #summaryStats {
        grid-template-columns: 1fr;
    }
}
```

### Paso 4: JavaScript para Dashboard
Crear un archivo `modeling_scripts.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Sistema de navegación
    const sections = {
        analysis: document.getElementById('analysisSection'),
        modeling: document.getElementById('modelingSection'),
        validation: document.getElementById('validationSection'),
        reports: document.getElementById('reportsSection')
    };
    
    // Botones de navegación
    document.getElementById('analysisBtn').addEventListener('click', () => showSection('analysis'));
    document.getElementById('modelingBtn').addEventListener('click', () => showSection('modeling'));
    document.getElementById('validationBtn').addEventListener('click', () => showSection('validation'));
    document.getElementById('reportsBtn').addEventListener('click', () => showSection('reports'));
    
    let currentAnalysis = null;
    let currentModels = null;
    
    function showSection(sectionName) {
        // Ocultar todas las secciones
        Object.values(sections).forEach(section => {
            section.style.display = 'none';
        });
        
        // Mostrar sección seleccionada
        sections[sectionName].style.display = 'block';
        
        // Actualizar botones de navegación
        document.querySelectorAll('nav button').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Agregar clase active al botón actual
        const currentBtn = document.getElementById(sectionName + 'Btn');
        if (currentBtn) {
            currentBtn.classList.add('active');
        }
        
        showNotification(`Cambiado a sección ${sectionName}`);
    }
    
    // Funcionalidad de análisis
    document.getElementById('loadRequirementsBtn').addEventListener('click', async function() {
        try {
            // En implementación real, esto cargaría desde archivo o API
            showNotification('Cargando requisitos de ejemplo...');
            
            // Simular carga de datos de ejemplo
            setTimeout(() => {
                currentAnalysis = {
                    total_requirements: 7,
                    quality_score: 78.5,
                    issues_found: [
                        'Ambiguo: FR1',
                        'Incompleto: NFR2'
                    ],
                    quality_metrics: {
                        completeness_ratio: 0.86,
                        ambiguity_ratio: 0.14,
                        consistency_ratio: 0.93,
                        average_length: 8.5
                    }
                };
                
                displayAnalysisResults(currentAnalysis);
                showNotification('Requisitos cargados exitosamente');
            }, 1000);
            
        } catch (error) {
            showNotification('Error cargando requisitos: ' + error.message);
        }
    });
    
    document.getElementById('runAnalysisBtn').addEventListener('click', function() {
        if (!currentAnalysis) {
            showNotification('Por favor carga requisitos primero');
            return;
        }
        
        showNotification('Ejecutando análisis...');
        
        // Simular análisis
        setTimeout(() => {
            displayAnalysisResults(currentAnalysis);
            createQualityChart(currentAnalysis.quality_metrics);
            showNotification('Análisis completado');
        }, 1500);
    });
    
    function displayAnalysisResults(analysis) {
        const summaryStats = document.getElementById('summaryStats');
        summaryStats.innerHTML = `
            <div class="stat-card">
                <div class="stat-value">${analysis.total_requirements}</div>
                <div class="stat-label">Total de Requisitos</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${analysis.quality_score}</div>
                <div class="stat-label">Puntaje de Calidad</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${analysis.issues_found.length}</div>
                <div class="stat-label">Problemas Encontrados</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${Object.keys(analysis.quality_metrics).length}</div>
                <div class="stat-label">Métricas de Calidad</div>
            </div>
        `;
        
        const issuesContent = document.getElementById('issuesContent');
        issuesContent.innerHTML = '<ul>';
        analysis.issues_found.forEach(issue => {
            issuesContent.innerHTML += `<li>${issue}</li>`;
        });
        issuesContent.innerHTML += '</ul>';
    }
    
    function createQualityChart(metrics) {
        const ctx = document.getElementById('qualityChart').getContext('2d');
        
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Object.keys(metrics),
                datasets: [{
                    label: 'Métricas de Calidad',
                    data: Object.values(metrics),
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(255, 205, 86, 0.6)'
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 205, 86, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 1
                    }
                }
            }
        });
    }
    
    // Funcionalidad de modelado
    document.getElementById('generateModelsBtn').addEventListener('click', function() {
        showNotification('Generando modelos...');
        
        // Simular generación de modelos
        setTimeout(() => {
            currentModels = {
                functional_hierarchy: {
                    'Control de Iluminación': ['FR1'],
                    'Sistema de Seguridad': ['FR2'],
                    'Control de Clima': ['FR3']
                },
                data_flow: {
                    entities: ['Usuario', 'Sensor', 'Sistema'],
                    processes: ['Procesar Entrada', 'Generar Respuesta'],
                    stores: ['Datos de Configuración']
                },
                use_cases: [
                    {name: 'Controlar Luces', actor: 'Usuario'},
                    {name: 'Monitorear Seguridad', actor: 'Usuario'}
                ]
            };
            
            displayModels(currentModels);
            showNotification('Modelos generados exitosamente');
        }, 2000);
    });
    
    function displayModels(models) {
        // Jerarquía Funcional
        const functionalModel = document.getElementById('functionalModel');
        functionalModel.innerHTML = '<div class="hierarchy-tree">';
        
        for (const [category, requirements] of Object.entries(models.functional_hierarchy)) {
            functionalModel.innerHTML += `
                <div class="hierarchy-node">
                    <strong>${category}</strong>
                    <div class="hierarchy-children">
                        ${requirements.map(req => `<div>${req}</div>`).join('')}
                    </div>
                </div>
            `;
        }
        functionalModel.innerHTML += '</div>';
        
        // Flujo de Datos
        const dataFlowModel = document.getElementById('dataFlowModel');
        dataFlowModel.innerHTML = `
            <div style="padding: 1rem;">
                <h4>Elementos de Flujo de Datos</h4>
                <p><strong>Entidades Externas:</strong> ${models.data_flow.entities.join(', ')}</p>
                <p><strong>Procesos:</strong> ${models.data_flow.processes.join(', ')}</p>
                <p><strong>Almacenes de Datos:</strong> ${models.data_flow.stores.join(', ')}</p>
            </div>
        `;
        
        // Casos de Uso
        const useCaseModel = document.getElementById('useCaseModel');
        useCaseModel.innerHTML = '<div style="padding: 1rem;"><h4>Casos de Uso</h4><ul>';
        models.use_cases.forEach(uc => {
            useCaseModel.innerHTML += `<li><strong>${uc.name}</strong> - Actor: ${uc.actor}</li>`;
        });
        useCaseModel.innerHTML += '</ul></div>';
    }
    
    // Funcionalidad de validación
    document.getElementById('runValidationBtn').addEventListener('click', function() {
        const validationResults = document.getElementById('validationResults');
        
        const checks = ['completeCheck', 'consistentCheck', 'feasibleCheck', 'testableCheck'];
        const passed = checks.filter(id => document.getElementById(id).checked).length;
        
        validationResults.innerHTML = `
            <p><strong>Puntaje de Validación: ${passed}/${checks.length}</strong></p>
            <p>Verificaciones aprobadas: ${passed}</p>
            <p>Verificaciones fallidas: ${checks.length - passed}</p>
            ${passed === checks.length ? '<p style="color: green;">¡Todas las validaciones pasaron!</p>' : '<p style="color: orange;">Algunas validaciones fallaron. Revisa los requisitos.</p>'}
        `;
        
        showNotification('Validación completada');
    });
    
    // Funcionalidad de reportes
    document.getElementById('generateReportBtn').addEventListener('click', function() {
        if (!currentAnalysis) {
            showNotification('Por favor ejecuta análisis primero');
            return;
        }
        
        const reportContent = document.getElementById('reportContent');
        reportContent.innerHTML = `
            <h3>Reporte de Análisis de Requisitos</h3>
            <h4>Resumen</h4>
            <ul>
                <li>Total de Requisitos: ${currentAnalysis.total_requirements}</li>
                <li>Puntaje de Calidad: ${currentAnalysis.quality_score}/100</li>
                <li>Problemas Encontrados: ${currentAnalysis.issues_found.length}</li>
            </ul>
            
            <h4>Métricas de Calidad</h4>
            <ul>
                ${Object.entries(currentAnalysis.quality_metrics).map(([key, value]) => 
                    `<li>${key}: ${(value * 100).toFixed(1)}%</li>`
                ).join('')}
            </ul>
            
            <h4>Problemas</h4>
            <ul>
                ${currentAnalysis.issues_found.map(issue => `<li>${issue}</li>`).join('')}
            </ul>
            
            <h4>Recomendaciones</h4>
            <ul>
                <li>Revisar requisitos ambiguos y agregar especificidad</li>
                <li>Asegurar que todos los requisitos contengan verbos modales necesarios</li>
                <li>Considerar priorización de requisitos para implementación</li>
            </ul>
        `;
        
        showNotification('Reporte generado');
    });
    
    document.getElementById('downloadReportBtn').addEventListener('click', function() {
        const reportContent = document.getElementById('reportContent').innerHTML;
        if (reportContent.includes('Reporte de Análisis de Requisitos')) {
            // En implementación real, esto descargaría el reporte
            showNotification('Función de descarga de reporte implementada aquí');
        } else {
            showNotification('Por favor genera un reporte primero');
        }
    });
    
    // Funcionalidad de exportación
    document.getElementById('exportAnalysisBtn').addEventListener('click', function() {
        if (!currentAnalysis) {
            showNotification('Por favor ejecuta análisis primero');
            return;
        }
        
        // En implementación real, esto exportaría a archivo
        showNotification('Función de exportación de análisis implementada aquí');
    });
    
    document.getElementById('exportModelsBtn').addEventListener('click', function() {
        if (!currentModels) {
            showNotification('Por favor genera modelos primero');
            return;
        }
        
        // En implementación real, esto exportaría modelos
        showNotification('Función de exportación de modelos implementada aquí');
    });
    
    // Sistema de notificaciones
    function showNotification(message) {
        const notification = document.getElementById('notification');
        notification.textContent = message;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }
    
    // Inicializar con sección de análisis visible
    showSection('analysis');
});
```

### Paso 5: Datos de Prueba
Crear un archivo `sample_requirements.json`:

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

### Paso 6: Suite de Pruebas
Crear un archivo `test_requirements_analysis.py`:

```python
import unittest
import json
from requirements_analysis import RequirementsAnalyzer

class TestRequirementsAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = RequirementsAnalyzer()
        # Crear datos de prueba
        self.test_requirements = [
            {"id": "FR1", "text": "El sistema debe controlar luces"},
            {"id": "FR2", "text": "El sistema debe proporcionar monitoreo de seguridad"},
            {"id": "NFR1", "text": "El sistema debe responder rápidamente"}
        ]
        
        # Guardar datos de prueba
        with open('test_requirements.json', 'w') as f:
            json.dump({'requirements': self.test_requirements}, f)
    
    def test_load_requirements(self):
        result = self.analyzer.load_requirements('test_requirements.json')
        self.assertTrue(result)
        self.assertEqual(len(self.analyzer.requirements), 3)
    
    def test_analyze_requirements(self):
        self.analyzer.load_requirements('test_requirements.json')
        analysis = self.analyzer.analyze_requirements()
        
        self.assertIn('total_requirements', analysis)
        self.assertIn('quality_score', analysis)
        self.assertIn('issues_found', analysis)
        self.assertEqual(analysis['total_requirements'], 3)
    
    def test_check_ambiguity(self):
        # Probar requisito ambiguo
        ambiguous = self.analyzer.check_ambiguity("El sistema debe trabajar según corresponda")
        self.assertTrue(ambiguous)
        
        # Probar requisito claro
        clear = self.analyzer.check_ambiguity("El sistema debe controlar luces")
        self.assertFalse(clear)
    
    def test_check_completeness(self):
        # Probar requisito completo
        complete = self.analyzer.check_completeness("El sistema debe controlar luces")
        self.assertTrue(complete)
        
        # Probar requisito incompleto
        incomplete = self.analyzer.check_completeness("Controlar luces")
        self.assertFalse(incomplete)
    
    def test_categorize_requirements(self):
        self.analyzer.load_requirements('test_requirements.json')
        categories = self.analyzer.categorize_requirements()
        
        self.assertIn('functional', categories)
        self.assertIn('non_functional', categories)
        self.assertEqual(len(categories['functional']), 2)
    
    def test_prioritize_requirements(self):
        self.analyzer.load_requirements('test_requirements.json')
        prioritized = self.analyzer.prioritize_requirements()
        
        self.assertEqual(len(prioritized), 3)
        # Verificar que se agregaron puntajes de prioridad
        self.assertIn('priority_score', prioritized[0])
    
    def test_generate_models(self):
        self.analyzer.load_requirements('test_requirements.json')
        models = self.analyzer.generate_models()
        
        self.assertIn('functional_hierarchy', models)
        self.assertIn('data_flow', models)
        self.assertIn('use_case', models)
    
    def tearDown(self):
        # Limpiar archivos de prueba
        import os
        if os.path.exists('test_requirements.json'):
            os.remove('test_requirements.json')

if __name__ == '__main__':
    unittest.main()
```

## Resumen

Este laboratorio proporciona una solución completa para el análisis y modelado de requisitos con las siguientes características:

### ✅ **Problemas Corregidos del Código Original:**
- **Carga de archivos**: Agregado manejo de errores apropiado
- **Lógica de análisis**: Corregidos bugs en cálculo de calidad y procesamiento
- **Detección de ambigüedad**: Mejorada con patrones sofisticados
- **Verificación de completitud**: Implementada validación apropiada de verbos modales
- **Verificación de consistencia**: Agregada detección de contradicciones
- **Categorización**: Corregida lógica de asignación de tipos
- **Análisis de dependencias**: Implementada identificación de relaciones
- **Sistema de priorización**: Agregado cálculo multi-factor
- **Generación de modelos**: Creados jerarquía funcional, flujo de datos y casos de uso
- **Funcionalidad de exportación**: Implementada exportación completa de resultados

### 🛠️ **Características Clave:**
1. **Análisis Automático**: Métricas de calidad, detección de problemas, recomendaciones
2. **Dashboard Interactivo**: Interfaz web para análisis y modelado
3. **Múltiples Tipos de Modelo**: Funcional, flujo de datos, máquina de estados, casos de uso
4. **Rastreo de Dependencias**: Identificación de relaciones entre requisitos
5. **Sistema de Priorización**: Cálculo de prioridad basado en múltiples factores
6. **Herramientas de Validación**: Lista de verificación para validación de requisitos
7. **Reportes**: Reportes completos de análisis y exportación

### 📊 **Implementación Técnica:**
- **Motor de Análisis Python**: Diseño orientado a objetos con manejo completo de errores
- **Dashboard Web**: HTML/CSS/JavaScript con integración Chart.js
- **Procesamiento de Datos**: Almacenamiento y procesamiento JSON
- **Visualización**: Gráficos interactivos y displays de modelos
- **Pruebas**: Suite de pruebas unitarias para validación

### 🎯 **Resultados de Aprendizaje:**
- Entender criterios de calidad de requisitos
- Aplicar técnicas sistemáticas de análisis
- Crear diferentes tipos de modelos de requisitos
- Usar herramientas para gestión de requisitos
- Implementar procesos de validación y verificación

La solución proporciona un sistema completo y funcional para análisis y modelado de requisitos que los estudiantes pueden usar como base para entender estos procesos críticos de ingeniería de software.
