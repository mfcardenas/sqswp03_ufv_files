# validation_test_suite.py - Suite de Pruebas para Motor de Validación

import unittest
import json
import os
import tempfile
from validation_engine import ValidationEngine

class TestValidationEngine(unittest.TestCase):
    """Suite de pruebas comprehensiva para ValidationEngine"""

    def setUp(self):
        """Configurar entorno de pruebas"""
        self.engine = ValidationEngine()

        # Crear datos de prueba
        self.test_requirements = {
            "requirements": [
                {
                    "id": "REQ-001",
                    "text": "El sistema debe procesar pedidos en menos de 2 segundos",
                    "type": "functional",
                    "priority": "high",
                    "acceptance_criteria": ["Tiempo < 2s", "Procesamiento exitoso"]
                },
                {
                    "id": "REQ-002",
                    "text": "El sistema debe autenticar usuarios",
                    "type": "security",
                    "priority": "high",
                    "acceptance_criteria": ["Autenticación OAuth", "Tokens válidos"]
                },
                {
                    "id": "REQ-003",
                    "text": "Sistema debe ser usable",
                    "type": "usability",
                    "priority": "medium"
                }
            ]
        }

        # Crear archivo temporal
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        json.dump(self.test_requirements, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        """Limpiar archivos temporales"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_initialization(self):
        """Probar inicialización del motor"""
        self.assertIsInstance(self.engine, ValidationEngine)
        self.assertEqual(len(self.engine.requirements), 0)
        self.assertIsInstance(self.engine.validation_rules, dict)
        self.assertIn('completeness', self.engine.validation_rules)

    def test_load_requirements_success(self):
        """Probar carga exitosa de requisitos"""
        result = self.engine.load_requirements(self.temp_file.name)
        self.assertTrue(result)
        self.assertEqual(len(self.engine.requirements), 3)
        self.assertEqual(self.engine.requirements[0]['id'], 'REQ-001')

    def test_load_requirements_file_not_found(self):
        """Probar manejo de archivo no encontrado"""
        result = self.engine.load_requirements('nonexistent_file.json')
        self.assertFalse(result)

    def test_load_requirements_invalid_json(self):
        """Probar manejo de JSON inválido"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('{"invalid": json}')
            temp_path = f.name

        try:
            result = self.engine.load_requirements(temp_path)
            self.assertFalse(result)
        finally:
            os.unlink(temp_path)

    def test_validate_completeness(self):
        """Probar validación de completitud"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_requirements()

        self.assertIn('validation_types', results)
        self.assertIn('completeness', results['validation_types'])
        completeness = results['validation_types']['completeness']

        self.assertIn('score', completeness)
        self.assertIn('issues', completeness)
        self.assertIsInstance(completeness['score'], (int, float))

    def test_validate_consistency(self):
        """Probar validación de consistencia"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_requirements()

        consistency = results['validation_types']['consistency']
        self.assertIn('score', consistency)
        self.assertIn('issues', consistency)

    def test_validate_feasibility(self):
        """Probar validación de factibilidad"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_requirements()

        feasibility = results['validation_types']['feasibility']
        self.assertIn('score', feasibility)
        self.assertIn('issues', feasibility)

    def test_validate_testability(self):
        """Probar validación de testeabilidad"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_requirements()

        testability = results['validation_types']['testability']
        self.assertIn('score', testability)
        self.assertIn('issues', testability)

    def test_validate_standards_compliance(self):
        """Probar validación de cumplimiento de estándares"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_requirements()

        compliance = results['validation_types']['standards_compliance']
        self.assertIn('score', compliance)
        self.assertIn('issues', compliance)

    def test_generate_test_cases(self):
        """Probar generación de casos de prueba"""
        self.engine.load_requirements(self.temp_file.name)
        test_cases = self.engine.generate_test_cases()

        self.assertIsInstance(test_cases, list)
        self.assertEqual(len(test_cases), 3)

        # Verificar estructura de caso de prueba
        test_case = test_cases[0]
        self.assertIn('id', test_case)
        self.assertIn('title', test_case)
        self.assertIn('test_steps', test_case)
        self.assertIn('expected_result', test_case)

    def test_perform_acceptance_testing(self):
        """Probar testing de aceptación"""
        self.engine.load_requirements(self.temp_file.name)
        self.engine.generate_test_cases()

        results = self.engine.perform_acceptance_testing()

        self.assertIn('acceptance_status', results)
        self.assertIn('passed_tests', results)
        self.assertIn('failed_tests', results)
        self.assertIn('test_results', results)
        self.assertIn('coverage_metrics', results)

    def test_validate_against_standards(self):
        """Probar validación contra estándares"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_against_standards()

        self.assertIn('overall_compliance', results)
        self.assertIn('sections_compliance', results)
        self.assertIn('issues', results)
        self.assertIn('recommendations', results)

    def test_generate_validation_report(self):
        """Probar generación de reporte de validación"""
        self.engine.load_requirements(self.temp_file.name)
        self.engine.validate_requirements()

        report = self.engine.generate_validation_report()

        self.assertIsInstance(report, str)
        self.assertIn('Reporte de Validación', report)
        self.assertIn('Resumen Ejecutivo', report)

    def test_export_validation_results_json(self):
        """Probar exportación de resultados en formato JSON"""
        self.engine.load_requirements(self.temp_file.name)
        self.engine.validate_requirements()

        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            temp_path = f.name

        try:
            self.engine.export_validation_results('json', temp_path)
            self.assertTrue(os.path.exists(temp_path))

            # Verificar que el archivo contiene JSON válido
            with open(temp_path, 'r') as f:
                data = json.load(f)
                self.assertIn('validation_types', data)

        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    def test_export_validation_results_html(self):
        """Probar exportación de resultados en formato HTML"""
        self.engine.load_requirements(self.temp_file.name)
        self.engine.validate_requirements()

        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
            temp_path = f.name

        try:
            self.engine.export_validation_results('html', temp_path)
            self.assertTrue(os.path.exists(temp_path))

            # Verificar que contiene HTML
            with open(temp_path, 'r') as f:
                content = f.read()
                self.assertIn('<html>', content)
                self.assertIn('Reporte de Validación', content)

        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    def test_overall_validation_score(self):
        """Probar cálculo de puntuación general"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_requirements()

        self.assertIn('overall_score', results)
        self.assertIsInstance(results['overall_score'], (int, float))
        self.assertGreaterEqual(results['overall_score'], 0)
        self.assertLessEqual(results['overall_score'], 100)

    def test_requirements_categorization(self):
        """Probar categorización de requisitos aprobados/fallidos"""
        self.engine.load_requirements(self.temp_file.name)
        results = self.engine.validate_requirements()

        self.assertIn('passed_requirements', results)
        self.assertIn('failed_requirements', results)
        self.assertIsInstance(results['passed_requirements'], list)
        self.assertIsInstance(results['failed_requirements'], list)

        total_categorized = len(results['passed_requirements']) + len(results['failed_requirements'])
        self.assertEqual(total_categorized, len(self.engine.requirements))

    def test_empty_requirements_validation(self):
        """Probar validación con lista vacía de requisitos"""
        results = self.engine.validate_requirements()
        self.assertIn('error', results)
        self.assertEqual(results['error'], 'No hay requisitos cargados para validación')

    def test_conflict_detection(self):
        """Probar detección de conflictos entre requisitos"""
        conflicting_requirements = {
            "requirements": [
                {
                    "id": "REQ-001",
                    "text": "El sistema debe siempre procesar pedidos",
                    "type": "functional",
                    "priority": "high"
                },
                {
                    "id": "REQ-002",
                    "text": "El sistema no debe nunca procesar pedidos",
                    "type": "functional",
                    "priority": "high"
                }
            ]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(conflicting_requirements, f)
            temp_path = f.name

        try:
            self.engine.load_requirements(temp_path)
            results = self.engine.validate_requirements()

            consistency = results['validation_types']['consistency']
            self.assertLess(consistency['score'], 100)  # Debe detectar conflicto

        finally:
            os.unlink(temp_path)

    def test_measurable_criteria_detection(self):
        """Probar detección de criterios medibles"""
        measurable_req = {
            "id": "REQ-001",
            "text": "El sistema debe procesar en menos de 2 segundos",
            "type": "functional",
            "priority": "high"
        }

        self.assertTrue(self.engine._has_measurable_criteria(measurable_req['text']))

        non_measurable_req = {
            "id": "REQ-002",
            "text": "El sistema debe ser rápido",
            "type": "functional",
            "priority": "high"
        }

        self.assertFalse(self.engine._has_measurable_criteria(non_measurable_req['text']))

class TestValidationRules(unittest.TestCase):
    """Pruebas específicas para reglas de validación"""

    def setUp(self):
        self.engine = ValidationEngine()

    def test_completeness_rules(self):
        """Probar reglas de completitud"""
        rules = self.engine.validation_rules['completeness']

        self.assertIn('required_fields', rules)
        self.assertIn('min_description_length', rules)
        self.assertIn('must_have_acceptance_criteria', rules)

        self.assertEqual(rules['min_description_length'], 10)
        self.assertTrue(rules['must_have_acceptance_criteria'])

    def test_consistency_rules(self):
        """Probar reglas de consistencia"""
        rules = self.engine.validation_rules['consistency']

        self.assertIn('no_duplicate_ids', rules)
        self.assertIn('no_conflicting_requirements', rules)
        self.assertIn('consistent_terminology', rules)

        self.assertTrue(rules['no_duplicate_ids'])
        self.assertTrue(rules['no_conflicting_requirements'])

    def test_feasibility_rules(self):
        """Probar reglas de factibilidad"""
        rules = self.engine.validation_rules['feasibility']

        self.assertIn('technical_feasibility', rules)
        self.assertIn('resource_feasibility', rules)
        self.assertIn('time_feasibility', rules)

    def test_testability_rules(self):
        """Probar reglas de testeabilidad"""
        rules = self.engine.validation_rules['testability']

        self.assertIn('measurable_criteria', rules)
        self.assertIn('verifiable_conditions', rules)
        self.assertIn('automated_testing_possible', rules)

    def test_standards_compliance_rules(self):
        """Probar reglas de cumplimiento de estándares"""
        rules = self.engine.validation_rules['standards_compliance']

        self.assertIn('iso_29148_compliant', rules)
        self.assertIn('clear_traceability', rules)
        self.assertIn('proper_prioritization', rules)

if __name__ == '__main__':
    # Configurar verbosidad de pruebas
    unittest.main(verbosity=2)
