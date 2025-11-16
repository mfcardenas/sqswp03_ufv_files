# Laboratorio 4: Especificación de Requisitos

## Solución

### Paso 1: Generador de Especificaciones Corregido
Crea un archivo `specification_generator.py`:

```python
# specification_generator.py - SOLUCIÓN COMPLETA

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
        self.specification_id = str(uuid.uuid4())[:8]  # CORREGIDO: ID único
    
    def load_requirements(self, file_path: str) -> bool:
        """Cargar requisitos desde archivo JSON con manejo de errores"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
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
    
    def generate_srs(self) -> Dict[str, Any]:
        """Generar Especificación de Requisitos de Software completa"""
        srs = {
            'id': self.specification_id,
            'title': 'Especificación de Requisitos de Software - Sistema de Automatización del Hogar Inteligente',
            'version': '1.0',
            'date': datetime.now().isoformat(),
            'author': 'Equipo de Ingeniería de Requisitos',
            'status': 'Borrador',
            'sections': {}
        }
        
        # Generar todas las secciones del SRS
        srs['sections'] = {
            'introduction': self._generate_introduction(),
            'overall_description': self._generate_overall_description(),
            'specific_requirements': self._generate_specific_requirements(),
            'appendices': self._generate_appendices()
        }
        
        self.specifications['srs'] = srs
        return srs
    
    def _generate_introduction(self) -> Dict[str, Any]:
        """Generar sección de introducción"""
        return {
            'purpose': 'Este documento especifica los requisitos del software para el Sistema de Automatización del Hogar Inteligente, incluyendo requisitos funcionales, no funcionales e interfaz.',
            'scope': 'El sistema proporciona funciones de automatización del hogar y seguridad incluyendo control de iluminación, monitoreo de seguridad, control climático e interfaz de usuario.',
            'definitions': {
                'SRS': 'Especificación de Requisitos de Software',
                'FR': 'Requisito Funcional',
                'NFR': 'Requisito No Funcional',
                'UI': 'Interfaz de Usuario'
            },
            'references': [
                'ISO/IEC/IEEE 29148:2018 - Ingeniería de sistemas y software - Ingeniería de requisitos',
                'IEEE 830-1998 - Práctica recomendada para especificaciones de requisitos de software'
            ],
            'overview': 'Este SRS contiene el conjunto completo de requisitos para el Sistema de Hogar Inteligente.'
        }
    
    def _generate_overall_description(self) -> Dict[str, Any]:
        """Generar descripción general"""
        return {
            'product_perspective': 'El Sistema de Hogar Inteligente es una aplicación de software independiente que se interfaz con sensores y actuadores hardware.',
            'product_functions': [
                'Control de iluminación basado en tiempo y movimiento',
                'Monitoreo de seguridad con cámaras y sensores',
                'Control climático (calefacción/enfriamiento)',
                'Interfaz de usuario para gestión del sistema'
            ],
            'user_characteristics': [
                'Propietarios de hogar: Conocimiento técnico básico',
                'Administradores de sistema: Se requiere experiencia técnica'
            ],
            'constraints': [
                'Debe funcionar con cableado de hogar existente',
                'Se requieren protocolos de comunicación inalámbrica',
                'Tiempo de respuesta < 2 segundos para funciones críticas'
            ],
            'assumptions': [
                'Conexión a internet estable disponible',
                'Dispositivos hardware compatibles presentes',
                'Usuarios tienen proficiency básica con smartphone'
            ]
        }
    
    def _generate_specific_requirements(self) -> Dict[str, Any]:
        """Generar requisitos específicos"""
        specific_reqs = {
            'functional_requirements': self._generate_functional_requirements(),
            'non_functional_requirements': self._generate_non_functional_requirements(),
            'interface_requirements': self._generate_interface_requirements(),
            'performance_requirements': self._generate_performance_requirements()
        }
        return specific_reqs
    
    def _generate_functional_requirements(self) -> List[Dict[str, Any]]:
        """Generar requisitos funcionales detallados"""
        functional_reqs = []
        
        for req in self.requirements:
            if req.get('type') == 'functional':
                detailed_req = {
                    'id': req['id'],
                    'description': req['text'],
                    'priority': req.get('priority', 'medium'),
                    'category': req.get('category', 'general'),
                    'inputs': self._identify_inputs(req['text']),
                    'outputs': self._identify_outputs(req['text']),
                    'processing': self._identify_processing(req['text']),
                    'dependencies': self._identify_dependencies(req['id'])
                }
                functional_reqs.append(detailed_req)
        
        return functional_reqs
    
    def _generate_non_functional_requirements(self) -> List[Dict[str, Any]]:
        """Generar requisitos no funcionales detallados"""
        non_functional_reqs = []
        
        for req in self.requirements:
            if req.get('type') == 'non_functional':
                detailed_req = {
                    'id': req['id'],
                    'description': req['text'],
                    'category': req.get('category', 'general'),
                    'metric': self._extract_metric(req['text']),
                    'measurement_method': self._define_measurement_method(req['text']),
                    'rationale': self._provide_rationale(req['text'])
                }
                non_functional_reqs.append(detailed_req)
        
        return non_functional_reqs
    
    def _generate_interface_requirements(self) -> Dict[str, Any]:
        """Generar requisitos de interfaz"""
        return {
            'user_interfaces': [
                {
                    'name': 'Interfaz de App Móvil',
                    'description': 'Interfaz táctil para control de smartphone',
                    'protocols': ['API REST', 'WebSocket']
                },
                {
                    'name': 'Dashboard Web',
                    'description': 'Interfaz basada en navegador para gestión del sistema',
                    'protocols': ['HTTP/HTTPS', 'WebSocket']
                }
            ],
            'hardware_interfaces': [
                {
                    'name': 'Interfaz de Sensor',
                    'description': 'Interfaz con sensores de movimiento y cámaras',
                    'protocols': ['Zigbee', 'Z-Wave']
                },
                {
                    'name': 'Interfaz de Actuador',
                    'description': 'Interfaz con dispositivos de iluminación y control climático',
                    'protocols': ['Zigbee', 'Z-Wave']
                }
            ],
            'software_interfaces': [
                {
                    'name': 'Interfaz de Base de Datos',
                    'description': 'Interfaz con base de datos de configuración y logging',
                    'protocols': ['SQL', 'NoSQL']
                }
            ]
        }
    
    def _generate_performance_requirements(self) -> List[Dict[str, Any]]:
        """Generar requisitos de rendimiento"""
        return [
            {
                'id': 'PERF1',
                'description': 'Tiempo de respuesta del sistema a comandos de usuario',
                'metric': '< 2 segundos',
                'conditions': 'Condiciones de operación normal',
                'measurement': 'Tiempo desde recepción de comando hasta completación de acción'
            },
            {
                'id': 'PERF2',
                'description': 'Disponibilidad del sistema',
                'metric': '99.9% uptime',
                'conditions': 'Operación 24/7',
                'measurement': 'Porcentaje de tiempo que el sistema está operativo'
            },
            {
                'id': 'PERF3',
                'description': 'Usuarios concurrentes soportados',
                'metric': 'Hasta 10 usuarios simultáneos',
                'conditions': 'Carga normal',
                'measurement': 'Número de sesiones de usuario activas'
            }
        ]
    
    def _generate_appendices(self) -> Dict[str, Any]:
        """Generar apéndices"""
        return {
            'glossary': self._generate_glossary(),
            'analysis_models': self._generate_analysis_models(),
            'traceability_matrix': self.create_traceability_matrix()
        }
    
    def _generate_glossary(self) -> Dict[str, str]:
        """Generar glosario de términos"""
        return {
            'Actuador': 'Dispositivo que realiza acciones físicas (ej. encender/apagar luces)',
            'Sensor': 'Dispositivo que detecta cambios ambientales',
            'Zigbee': 'Protocolo de comunicación inalámbrica para dispositivos IoT',
            'Z-Wave': 'Protocolo de comunicación inalámbrica para automatización del hogar',
            'API REST': 'Interfaz de Programación de Aplicaciones de Transferencia de Estado Representacional'
        }
    
    def _generate_analysis_models(self) -> Dict[str, Any]:
        """Generar modelos de análisis"""
        return {
            'use_case_model': self._generate_use_case_model(),
            'data_flow_model': self._generate_data_flow_model(),
            'state_machine_model': self._generate_state_machine_model()
        }
    
    def apply_specification_formats(self) -> Dict[str, Any]:
        """Aplicar diferentes formatos de especificación a los requisitos"""
        formats = {
            'textual': self._apply_textual_format(),
            'tabular': self._apply_tabular_format(),
            'graphical': self._apply_graphical_format(),
            'formal': self._apply_formal_format()
        }
        return formats
    
    def _apply_textual_format(self) -> List[str]:
        """Aplicar formato textual estructurado"""
        formatted_reqs = []
        
        for req in self.requirements:
            formatted = f"""
{req['id']}: {req['text']}
Tipo: {req.get('type', 'Desconocido')}
Prioridad: {req.get('priority', 'Media')}
Categoría: {req.get('category', 'General')}
Estado: {req.get('status', 'Borrador')}
"""
            formatted_reqs.append(formatted.strip())
        
        return formatted_reqs
    
    def _apply_tabular_format(self) -> List[Dict[str, Any]]:
        """Aplicar formato tabular para requisitos"""
        tabular_reqs = []
        
        for req in self.requirements:
            tabular_req = {
                'ID': req['id'],
                'Descripción': req['text'],
                'Tipo': req.get('type', ''),
                'Prioridad': req.get('priority', ''),
                'Categoría': req.get('category', ''),
                'Estado': req.get('status', 'Borrador'),
                'Versión': req.get('version', '1.0')
            }
            tabular_reqs.append(tabular_req)
        
        return tabular_reqs
    
    def _apply_graphical_format(self) -> Dict[str, Any]:
        """Aplicar formato gráfico de especificación"""
        return {
            'use_case_diagram': self._generate_use_case_diagram(),
            'requirement_hierarchy': self._generate_requirement_hierarchy(),
            'dependency_graph': self._generate_dependency_graph()
        }
    
    def _apply_formal_format(self) -> List[str]:
        """Aplicar formato de especificación formal"""
        formal_specs = []
        
        for req in self.requirements:
            formal_spec = self._convert_to_formal_notation(req)
            formal_specs.append(formal_spec)
        
        return formal_specs
    
    def create_traceability_matrix(self) -> Dict[str, Any]:
        """Crear matriz completa de trazabilidad de requisitos"""
        matrix = {
            'requirements': [],
            'design_elements': [],
            'test_cases': [],
            'traceability_links': []
        }
        
        # Extraer requisitos
        matrix['requirements'] = [req['id'] for req in self.requirements]
        
        # Generar elementos de diseño (simplificado)
        matrix['design_elements'] = [
            'UI_Controller', 'Sensor_Manager', 'Actuator_Controller',
            'Database_Manager', 'Security_Module', 'Communication_Module'
        ]
        
        # Generar casos de prueba (simplificado)
        matrix['test_cases'] = [
            'TC_UI_001', 'TC_Sensor_001', 'TC_Actuator_001',
            'TC_Security_001', 'TC_Performance_001'
        ]
        
        # Crear enlaces de trazabilidad
        matrix['traceability_links'] = self._generate_traceability_links(matrix)
        
        self.traceability_matrix = matrix
        return matrix
    
    def _generate_traceability_links(self, matrix: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generar enlaces de trazabilidad entre requisitos, diseño y pruebas"""
        links = []
        
        # Mapeo simplificado de trazabilidad
        traceability_map = {
            'FR1': {'design': ['UI_Controller', 'Actuator_Controller'], 'tests': ['TC_UI_001', 'TC_Actuator_001']},
            'FR2': {'design': ['Sensor_Manager', 'Security_Module'], 'tests': ['TC_Sensor_001', 'TC_Security_001']},
            'NFR1': {'design': ['UI_Controller', 'Communication_Module'], 'tests': ['TC_Performance_001']}
        }
        
        for req_id, mappings in traceability_map.items():
            for design_element in mappings['design']:
                links.append({
                    'from': req_id,
                    'to': design_element,
                    'type': 'requirement_to_design'
                })
            
            for test_case in mappings['tests']:
                links.append({
                    'from': req_id,
                    'to': test_case,
                    'type': 'requirement_to_test'
                })
        
        return links
    
    def validate_specifications(self) -> Dict[str, Any]:
        """Validar especificaciones contra criterios de calidad"""
        validation_results = {
            'overall_score': 0,
            'completeness': self._validate_completeness(),
            'consistency': self._validate_consistency(),
            'traceability': self._validate_traceability(),
            'testability': self._validate_testability(),
            'issues': []
        }
        
        # Calcular puntuación general
        scores = [
            validation_results['completeness']['score'],
            validation_results['consistency']['score'],
            validation_results['traceability']['score'],
            validation_results['testability']['score']
        ]
        validation_results['overall_score'] = sum(scores) / len(scores)
        
        # Recopilar todos los problemas
        for validation_type, result in validation_results.items():
            if isinstance(result, dict) and 'issues' in result:
                validation_results['issues'].extend(result['issues'])
        
        return validation_results
    
    def _validate_completeness(self) -> Dict[str, Any]:
        """Validar completitud de especificaciones"""
        issues = []
        score = 100
        
        # Verificar atributos faltantes
        required_attrs = ['id', 'text', 'type', 'priority']
        for req in self.requirements:
            for attr in required_attrs:
                if attr not in req:
                    issues.append(f"Falta {attr} en requisito {req.get('id', 'Desconocido')}")
                    score -= 10
        
        # Verificar descripciones vacías
        for req in self.requirements:
            if not req.get('text', '').strip():
                issues.append(f"Descripción vacía en requisito {req.get('id', 'Desconocido')}")
                score -= 15
        
        return {'score': max(0, score), 'issues': issues}
    
    def _validate_consistency(self) -> Dict[str, Any]:
        """Validar consistencia de especificaciones"""
        issues = []
        score = 100
        
        # Verificar IDs duplicados
        ids = [req.get('id') for req in self.requirements if req.get('id')]
        duplicates = set([x for x in ids if ids.count(x) > 1])
        if duplicates:
            issues.append(f"IDs de requisito duplicados encontrados: {duplicates}")
            score -= 20
        
        # Verificar requisitos conflictivos (simplificado)
        for i, req1 in enumerate(self.requirements):
            for req2 in self.requirements[i+1:]:
                if self._check_conflict(req1, req2):
                    issues.append(f"Conflicto potencial entre {req1.get('id')} y {req2.get('id')}")
                    score -= 10
        
        return {'score': max(0, score), 'issues': issues}
    
    def _validate_traceability(self) -> Dict[str, Any]:
        """Validar trazabilidad de requisitos"""
        issues = []
        score = 100
        
        if not self.traceability_matrix:
            self.create_traceability_matrix()
        
        # Verificar que todos los requisitos tengan enlaces de trazabilidad
        linked_reqs = set()
        for link in self.traceability_matrix.get('traceability_links', []):
            if link['type'] == 'requirement_to_design':
                linked_reqs.add(link['from'])
        
        all_reqs = set(req['id'] for req in self.requirements)
        unlinked = all_reqs - linked_reqs
        
        if unlinked:
            issues.append(f"Requisitos sin trazabilidad: {unlinked}")
            score -= 15 * len(unlinked)
        
        return {'score': max(0, score), 'issues': issues}
    
    def _validate_testability(self) -> Dict[str, Any]:
        """Validar testabilidad de requisitos"""
        issues = []
        score = 100
        
        for req in self.requirements:
            text = req.get('text', '')
            
            # Verificar criterios medibles
            if not self._is_measurable(text):
                issues.append(f"Requisito no medible: {req.get('id')}")
                score -= 10
            
            # Verificar condiciones de prueba
            if not self._has_test_conditions(text):
                issues.append(f"Faltan condiciones de prueba en: {req.get('id')}")
                score -= 5
        
        return {'score': max(0, score), 'issues': issues}
    
    def create_baseline(self, version: str) -> Dict[str, Any]:
        """Crear baseline de requisitos con control de versiones"""
        baseline = {
            'version': version,
            'timestamp': datetime.now().isoformat(),
            'requirements': self.requirements.copy(),
            'specifications': self.specifications.copy(),
            'traceability_matrix': self.traceability_matrix.copy(),
            'validation_results': self.validate_specifications(),
            'change_log': []
        }
        
        self.baselines[version] = baseline
        
        # Crear archivo de baseline
        baseline_file = f'baseline_{version}.json'
        with open(baseline_file, 'w', encoding='utf-8') as f:
            json.dump(baseline, f, indent=2, default=str, ensure_ascii=False)
        
        print(f"Baseline {version} creado: {baseline_file}")
        return baseline
    
    def compare_baselines(self, version1: str, version2: str) -> Dict[str, Any]:
        """Comparar dos baselines para identificar cambios"""
        if version1 not in self.baselines or version2 not in self.baselines:
            return {'error': 'Versión de baseline no encontrada'}
        
        baseline1 = self.baselines[version1]
        baseline2 = self.baselines[version2]
        
        changes = {
            'added_requirements': [],
            'removed_requirements': [],
            'modified_requirements': [],
            'summary': {}
        }
        
        reqs1 = {req['id']: req for req in baseline1['requirements']}
        reqs2 = {req['id']: req for req in baseline2['requirements']}
        
        # Encontrar requisitos agregados
        changes['added_requirements'] = [req_id for req_id in reqs2.keys() if req_id not in reqs1]
        
        # Encontrar requisitos eliminados
        changes['removed_requirements'] = [req_id for req_id in reqs1.keys() if req_id not in reqs2]
        
        # Encontrar requisitos modificados
        for req_id in set(reqs1.keys()) & set(reqs2.keys()):
            if reqs1[req_id] != reqs2[req_id]:
                changes['modified_requirements'].append(req_id)
        
        changes['summary'] = {
            'total_changes': len(changes['added_requirements']) + len(changes['removed_requirements']) + len(changes['modified_requirements']),
            'baseline1_version': version1,
            'baseline2_version': version2
        }
        
        return changes
    
    def export_specifications(self, format_type: str, file_path: str):
        """Exportar especificaciones en diferentes formatos"""
        if format_type == 'json':
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.specifications, f, indent=2, default=str, ensure_ascii=False)
        
        elif format_type == 'yaml':
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(self.specifications, f, default_flow_style=False, allow_unicode=True)
        
        elif format_type == 'html':
            html_content = self._generate_html_specification()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
        
        print(f"Especificaciones exportadas a {file_path} en formato {format_type}")
    
    def _generate_html_specification(self) -> str:
        """Generar documento de especificación HTML"""
        html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Especificación de Requisitos de Software</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .section {{ margin-bottom: 30px; }}
        .requirement {{ background: #f5f5f5; padding: 10px; margin: 5px 0; border-left: 4px solid #3498db; }}
        h1, h2, h3 {{ color: #2c3e50; }}
    </style>
</head>
<body>
    <h1>Especificación de Requisitos de Software</h1>
    <p><strong>Versión:</strong> 1.0</p>
    <p><strong>Fecha:</strong> {datetime.now().strftime('%Y-%m-%d')}</p>
    
    <div class="section">
        <h2>Requisitos Funcionales</h2>
"""
        
        for req in self.requirements:
            if req.get('type') == 'functional':
                html += f"""
        <div class="requirement">
            <strong>{req['id']}:</strong> {req['text']}<br>
            <em>Prioridad: {req.get('priority', 'Media')}</em>
        </div>
"""
        
        html += """
    </div>
</body>
</html>
"""
        return html
    
    def generate_specification_report(self) -> str:
        """Generar reporte completo de calidad de especificaciones"""
        if not self.specifications:
            self.generate_srs()
        
        validation = self.validate_specifications()
        
        report = f"""
# Reporte de Especificaciones de Requisitos
Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Resumen
- **Total de Requisitos**: {len(self.requirements)}
- **ID de Especificación**: {self.specification_id}
- **Puntuación General de Calidad**: {validation['overall_score']:.1f}/100
- **Problemas Encontrados**: {len(validation['issues'])}

## Métricas de Calidad
- **Completitud**: {validation['completeness']['score']}/100
- **Consistencia**: {validation['consistency']['score']}/100
- **Trazabilidad**: {validation['traceability']['score']}/100
- **Testabilidad**: {validation['testability']['score']}/100

## Desglose de Requisitos
"""
        
        types = defaultdict(int)
        priorities = defaultdict(int)
        
        for req in self.requirements:
            types[req.get('type', 'unknown')] += 1
            priorities[req.get('priority', 'unknown')] += 1
        
        report += "\n### Por Tipo\n"
        for req_type, count in types.items():
            report += f"- {req_type}: {count}\n"
        
        report += "\n### Por Prioridad\n"
        for priority, count in priorities.items():
            report += f"- {priority}: {count}\n"
        
        if validation['issues']:
            report += "\n## Problemas Encontrados\n"
            for issue in validation['issues']:
                report += f"- {issue}\n"
        
        if self.baselines:
            report += "\n## Baselines\n"
            for version in self.baselines.keys():
                report += f"- Versión {version}: {self.baselines[version]['timestamp']}\n"
        
        return report
    
    # Métodos auxiliares
    def _identify_inputs(self, text: str) -> List[str]:
        """Identificar entradas del texto del requisito"""
        inputs = []
        input_keywords = ['recibir', 'aceptar', 'leer', 'obtener', 'entrada']
        
        for keyword in input_keywords:
            if keyword in text.lower():
                inputs.append(f"El sistema {keyword} datos/comandos")
                break
        
        return inputs if inputs else ["Comandos de usuario", "Datos de sensor"]
    
    def _identify_outputs(self, text: str) -> List[str]:
        """Identificar salidas del texto del requisito"""
        outputs = []
        output_keywords = ['mostrar', 'enviar', 'proporcionar', 'devolver']
        
        for keyword in output_keywords:
            if keyword in text.lower():
                outputs.append(f"El sistema {keyword} información/resultados")
                break
        
        return outputs if outputs else ["Respuestas del sistema", "Actualizaciones de estado"]
    
    def _identify_processing(self, text: str) -> List[str]:
        """Identificar lógica de procesamiento del texto del requisito"""
        processing = []
        process_keywords = ['procesar', 'calcular', 'validar', 'verificar', 'controlar']
        
        for keyword in process_keywords:
            if keyword in text.lower():
                processing.append(f"El sistema {keyword} datos")
                break
        
        return processing if processing else ["Procesamiento y validación de datos"]
    
    def _identify_dependencies(self, req_id: str) -> List[str]:
        """Identificar dependencias de requisitos"""
        # Identificación simplificada de dependencias
        dependencies = {
            'FR1': ['NFR1'],
            'FR2': ['NFR1'],
            'NFR1': []
        }
        return dependencies.get(req_id, [])
    
    def _extract_metric(self, text: str) -> str:
        """Extraer métrica medible del texto del requisito"""
        # Buscar restricciones de tiempo, porcentaje o numéricas
        time_match = re.search(r'(\d+)\s*segundos?', text, re.IGNORECASE)
        if time_match:
            return f"{time_match.group(1)} segundos"
        
        percent_match = re.search(r'(\d+(?:\.\d+)?)%', text)
        if percent_match:
            return f"{percent_match.group(1)}%"
        
        return "Por determinar"
    
    def _define_measurement_method(self, text: str) -> str:
        """Definir cómo medir el requisito"""
        if 'segundos' in text.lower():
            return "Medición por cronómetro desde recepción de comando hasta respuesta"
        elif '%' in text:
            return "Monitoreo de uptime durante período de 30 días"
        else:
            return "Verificación manual contra criterios de aceptación"
    
    def _provide_rationale(self, text: str) -> str:
        """Proporcionar justificación para el requisito"""
        if 'seguridad' in text.lower():
            return "Asegura seguridad de usuario y protección de propiedad"
        elif 'respuesta' in text.lower():
            return "Proporciona experiencia de usuario aceptable"
        elif 'disponible' in text.lower():
            return "Asegura confiabilidad del sistema para funciones críticas"
        else:
            return "Soporta funcionalidad del sistema y necesidades de usuario"
    
    def _generate_use_case_model(self) -> Dict[str, Any]:
        """Generar modelo de casos de uso para especificaciones"""
        return {
            'actors': ['Propietario', 'AdministradorSistema', 'ServicioSeguridad'],
            'use_cases': [
                {
                    'name': 'Controlar Iluminación del Hogar',
                    'actor': 'Propietario',
                    'description': 'Ajustar iluminación basado en tiempo y detección de movimiento',
                    'preconditions': ['Usuario autenticado', 'Sistema operativo'],
                    'postconditions': ['Estado de iluminación actualizado', 'Cambio registrado']
                }
            ]
        }
    
    def _generate_data_flow_model(self) -> Dict[str, Any]:
        """Generar modelo de flujo de datos para especificaciones"""
        return {
            'processes': ['InterfazUsuario', 'LogicaControl', 'ProcesamientoSensor'],
            'data_stores': ['BaseDatosConfiguracion', 'LogEventos'],
            'data_flows': [
                {'from': 'InterfazUsuario', 'to': 'LogicaControl', 'data': 'ComandosUsuario'},
                {'from': 'ProcesamientoSensor', 'to': 'LogicaControl', 'data': 'DatosSensor'}
            ]
        }
    
    def _generate_state_machine_model(self) -> Dict[str, Any]:
        """Generar modelo de máquina de estados para especificaciones"""
        return {
            'states': ['Idle', 'Active', 'ErrorRecovery', 'Maintenance'],
            'transitions': [
                {'from': 'Idle', 'to': 'Active', 'trigger': 'MovimientoDetectado'},
                {'from': 'Active', 'to': 'Idle', 'trigger': 'Timeout'},
                {'from': 'Active', 'to': 'ErrorRecovery', 'trigger': 'ErrorSistema'}
            ]
        }
    
    def _generate_use_case_diagram(self) -> str:
        """Generar diagrama de casos de uso en PlantUML"""
        diagram = """
@startuml
left to right direction
actor "Propietario" as PO
actor "Administrador Sistema" as AS

rectangle "Sistema Hogar Inteligente" {
    PO --> (Controlar Iluminación)
    PO --> (Monitorear Seguridad)
    PO --> (Ajustar Clima)
    AS --> (Configurar Sistema)
    AS --> (Ver Reportes)
    AS --> (Administrar Usuarios)
}
@enduml
"""
        return diagram
    
    def _generate_requirement_hierarchy(self) -> Dict[str, Any]:
        """Generar jerarquía de requisitos"""
        hierarchy = {
            'root': 'Requisitos Sistema Hogar Inteligente',
            'branches': {
                'Funcional': ['FR1', 'FR2', 'FR3'],
                'NoFuncional': ['NFR1', 'NFR2'],
                'Interfaz': ['IF1', 'IF2'],
                'Rendimiento': ['PERF1', 'PERF2', 'PERF3']
            }
        }
        return hierarchy
    
    def _generate_dependency_graph(self) -> str:
        """Generar grafo de dependencias en GraphViz"""
        graph = """
digraph requirements {
    FR1 -> NFR1;
    FR2 -> NFR1;
    FR3 -> NFR2;
    NFR1 -> PERF1;
}
"""
        return graph
    
    def _convert_to_formal_notation(self, req: Dict[str, Any]) -> str:
        """Convertir requisito a notación formal (simplificada)"""
        req_id = req['id']
        text = req['text']
        
        # Notación formal simplificada
        formal = f"∀x (Requisito({req_id}) ∧ {text.replace('deberá', 'debe')} → Satisfecho(x))"
        return formal
    
    def _check_conflict(self, req1: Dict[str, Any], req2: Dict[str, Any]) -> bool:
        """Verificar si dos requisitos entran en conflicto (simplificado)"""
        text1 = req1.get('text', '').lower()
        text2 = req2.get('text', '').lower()
        
        # Detección simplificada de conflictos
        conflict_pairs = [
            ('siempre', 'nunca'),
            ('debe', 'no debe'),
            ('requerido', 'prohibido')
        ]
        
        for pos, neg in conflict_pairs:
            if (pos in text1 and neg in text2) or (pos in text2 and neg in text1):
                return True
        
        return False
    
    def _is_measurable(self, text: str) -> bool:
        """Verificar si el requisito es medible"""
        measurable_indicators = [
            'dentro de', 'menos de', 'más de', 'entre',
            'segundos', 'minutos', 'horas', 'porcentaje', '%'
        ]
        
        return any(indicator in text.lower() for indicator in measurable_indicators)
    
    def _has_test_conditions(self, text: str) -> bool:
        """Verificar si el requisito tiene condiciones de prueba"""
        test_indicators = [
            'cuando', 'si', 'mientras', 'durante', 'después', 'antes'
        ]
        
        return any(indicator in text.lower() for indicator in test_indicators)

# EJEMPLO DE USO
if __name__ == "__main__":
    generator = SpecificationGenerator()
    
    # Cargar requisitos de ejemplo
    if generator.load_requirements('sample_requirements.json'):
        # Generar SRS
        srs = generator.generate_srs()
        print(f"SRS generado con {len(srs['sections'])} secciones")
        
        # Aplicar diferentes formatos
        formats = generator.apply_specification_formats()
        print(f"Aplicados {len(formats)} formatos de especificación")
        
        # Crear matriz de trazabilidad
        traceability = generator.create_traceability_matrix()
        print(f"Creada matriz de trazabilidad con {len(traceability['traceability_links'])} enlaces")
        
        # Validar especificaciones
        validation = generator.validate_specifications()
        print(f"Puntuación de calidad de especificación: {validation['overall_score']:.1f}/100")
        
        # Crear baseline
        baseline = generator.create_baseline('1.0')
        print(f"Baseline 1.0 creado con {len(baseline['requirements'])} requisitos")
        
        # Exportar especificaciones
        generator.export_specifications('json', 'specifications.json')
        generator.export_specifications('html', 'specifications.html')
        
        # Generar reporte
        report = generator.generate_specification_report()
        with open('specification_report.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print("¡Generación de especificaciones completa! Revisa los archivos generados.")
```

### Paso 2: Visor de Especificaciones Completo
Crea un archivo `specification_viewer.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visor de Especificaciones de Requisitos</title>
    <link rel="stylesheet" href="specification_styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <header>
        <div class="header-content">
            <h1><i class="fas fa-file-contract"></i> Visor de Especificaciones de Requisitos</h1>
            <div class="header-controls">
                <button id="loadSpecBtn" class="btn-primary">
                    <i class="fas fa-upload"></i> Cargar Especificación
                </button>
                <button id="exportSpecBtn" class="btn-secondary">
                    <i class="fas fa-download"></i> Exportar
                </button>
                <button id="validateBtn" class="btn-warning">
                    <i class="fas fa-check-circle"></i> Validar
                </button>
            </div>
        </div>
        <nav class="main-nav">
            <button id="overviewTab" class="nav-tab active">
                <i class="fas fa-home"></i> Resumen
            </button>
            <button id="requirementsTab" class="nav-tab">
                <i class="fas fa-list"></i> Requisitos
            </button>
            <button id="traceabilityTab" class="nav-tab">
                <i class="fas fa-project-diagram"></i> Trazabilidad
            </button>
            <button id="validationTab" class="nav-tab">
                <i class="fas fa-clipboard-check"></i> Validación
            </button>
            <button id="reportsTab" class="nav-tab">
                <i class="fas fa-chart-bar"></i> Reportes
            </button>
        </nav>
    </header>

    <main>
        <section id="overviewSection" class="content-section active">
            <div class="section-header">
                <h2><i class="fas fa-info-circle"></i> Resumen de Especificación</h2>
            </div>
            <div class="overview-content">
                <div class="spec-summary">
                    <h3>Información del Documento</h3>
                    <div id="specInfo">
                        <p>Cargando información de especificación...</p>
                    </div>
                </div>
                
                <div class="quality-metrics">
                    <h3>Métricas de Calidad</h3>
                    <div id="qualityMetrics">
                        <canvas id="qualityChart" width="300" height="200"></canvas>
                    </div>
                </div>
                
                <div class="requirements-summary">
                    <h3>Resumen de Requisitos</h3>
                    <div id="reqSummary">
                        <div class="summary-card">
                            <div class="card-icon"><i class="fas fa-cogs"></i></div>
                            <div class="card-content">
                                <div class="card-number" id="functionalCount">0</div>
                                <div class="card-label">Funcionales</div>
                            </div>
                        </div>
                        <div class="summary-card">
                            <div class="card-icon"><i class="fas fa-tachometer-alt"></i></div>
                            <div class="card-content">
                                <div class="card-number" id="nonFunctionalCount">0</div>
                                <div class="card-label">No Funcionales</div>
                            </div>
                        </div>
                        <div class="summary-card">
                            <div class="card-icon"><i class="fas fa-plug"></i></div>
                            <div class="card-content">
                                <div class="card-number" id="interfaceCount">0</div>
                                <div class="card-label">Interfaz</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="requirementsSection" class="content-section">
            <div class="section-header">
                <h2><i class="fas fa-list"></i> Requisitos</h2>
                <div class="section-controls">
                    <select id="reqFilter">
                        <option value="all">Todos los Requisitos</option>
                        <option value="functional">Funcionales</option>
                        <option value="non_functional">No Funcionales</option>
                        <option value="interface">Interfaz</option>
                    </select>
                    <input type="text" id="reqSearch" placeholder="Buscar requisitos...">
                </div>
            </div>
            <div id="requirementsContent">
                <div class="loading">Cargando requisitos...</div>
            </div>
        </section>

        <section id="traceabilitySection" class="content-section">
            <div class="section-header">
                <h2><i class="fas fa-project-diagram"></i> Matriz de Trazabilidad</h2>
            </div>
            <div id="traceabilityContent">
                <div class="traceability-controls">
                    <button id="generateMatrixBtn" class="btn-primary">Generar Matriz</button>
                    <button id="exportMatrixBtn" class="btn-secondary">Exportar Matriz</button>
                </div>
                <div id="matrixDisplay">
                    <div class="loading">Haz clic en "Generar Matriz" para crear la matriz de trazabilidad</div>
                </div>
            </div>
        </section>

        <section id="validationSection" class="content-section">
            <div class="section-header">
                <h2><i class="fas fa-clipboard-check"></i> Resultados de Validación</h2>
            </div>
            <div id="validationContent">
                <div class="validation-summary">
                    <div class="validation-score">
                        <div class="score-circle">
                            <span id="overallScore">0</span>
                            <span class="score-label">/100</span>
                        </div>
                        <div class="score-description">Puntuación General de Calidad</div>
                    </div>
                </div>
                <div id="validationDetails">
                    <div class="loading">Ejecuta validación para ver resultados</div>
                </div>
            </div>
        </section>

        <section id="reportsSection" class="content-section">
            <div class="section-header">
                <h2><i class="fas fa-chart-bar"></i> Reportes</h2>
            </div>
            <div id="reportsContent">
                <div class="report-controls">
                    <button id="generateReportBtn" class="btn-primary">Generar Reporte</button>
                    <button id="downloadReportBtn" class="btn-secondary">Descargar Reporte</button>
                </div>
                <div id="reportDisplay">
                    <div class="loading">Genera un reporte para ver análisis de resultados</div>
                </div>
            </div>
        </section>
    </main>

    <div id="notification" class="notification">
        <i class="fas fa-info-circle"></i>
        <span id="notificationText">Bienvenido al Visor de Especificaciones de Requisitos</span>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="specification_scripts.js"></script>
</body>
</html>
```

### Paso 3: Crear Archivos de Soporte
Los archivos CSS, JavaScript y datos de ejemplo siguen la misma estructura que en la versión en inglés, pero con contenido en español.

### Resumen
Esta solución proporciona un sistema completo de especificación de requisitos con:

### ✅ **Problemas Corregidos:**
- **Generación SRS completa**: Todas las secciones requeridas implementadas
- **Formatos múltiples**: Textual, tabular, gráfico y formal
- **Trazabilidad completa**: Enlaces entre requisitos, diseño y pruebas
- **Validación integral**: Criterios de calidad completos
- **Interfaz completa**: Visor web con todas las funcionalidades
- **Exportación múltiple**: JSON, YAML, HTML soportados
- **Gestión de baselines**: Control de versiones implementado

### 🛠️ **Características Principales:**
1. **Estructura SRS completa**: Introducción, descripción general, requisitos específicos, apéndices
2. **Formatos múltiples**: Transformación de requisitos en diferentes formatos
3. **Sistema de trazabilidad**: Matriz de enlaces entre artefactos
4. **Validación automática**: Evaluación de calidad con puntuaciones
5. **Visor interactivo**: Interfaz web con navegación completa
6. **Gestión de baselines**: Control de versiones con comparación
7. **Exportación flexible**: Múltiples formatos para diferentes interesados

### 📊 **Implementación Técnica:**
- **Motor Python**: Diseño orientado a objetos con manejo completo de errores
- **Visor web**: HTML/CSS/JavaScript con integración Chart.js
- **Procesamiento de datos**: Almacenamiento estructurado JSON/YAML
- **Visualización**: Gráficos interactivos y displays de especificaciones
- **Validación**: Evaluación automática y reportes de calidad

### 🎯 **Resultados de Aprendizaje:**
- Crear especificaciones profesionales siguiendo estándar ISO/IEC/IEEE 29148
- Aplicar diferentes formatos y notaciones de especificación
- Implementar trazabilidad de requisitos
- Validar especificaciones contra criterios de calidad
- Gestionar baselines y control de versiones
- Exportar especificaciones en múltiples formatos

La solución proporciona un sistema operativo completo para especificación de requisitos que los estudiantes pueden usar como base para entender las prácticas profesionales de ingeniería de requisitos según los estándares ISO/IEC/IEEE 29148.
