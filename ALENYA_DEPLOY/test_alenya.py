#!/usr/bin/env python3
"""
ALENYA Test Suite
MELANO INC - Versión 3.0.0

Suite completa de tests para verificar el funcionamiento de ALENYA
"""

import sys
import os
import json
import time
import requests
from typing import Dict, Any, List

# Agregar el directorio actual al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from alenya_agent import AlenyaAgent

class AlenyaTestSuite:
    """Suite de tests para ALENYA"""
    
    def __init__(self):
        self.agent = AlenyaAgent()
        self.api_base = "http://localhost:5000/api"
        self.tests_passed = 0
        self.tests_failed = 0
        self.test_results = []
    
    def log_test(self, test_name: str, passed: bool, message: str = ""):
        """Registra el resultado de un test"""
        status = "✅ PASS" if passed else "❌ FAIL"
        result = {
            "test": test_name,
            "passed": passed,
            "message": message,
            "timestamp": time.time()
        }
        
        self.test_results.append(result)
        
        if passed:
            self.tests_passed += 1
            print(f"{status} {test_name}")
        else:
            self.tests_failed += 1
            print(f"{status} {test_name}: {message}")
        
        if message and passed:
            print(f"    ℹ️  {message}")
    
    def test_agent_initialization(self):
        """Test: Inicialización del agente"""
        try:
            assert self.agent.version == "3.0.0"
            assert self.agent.nombre == "ALENYA"
            assert self.agent.empresa == "MELANO INC"
            assert len(self.agent.zonas_horarias) >= 10
            assert len(self.agent.verticales) >= 4
            
            self.log_test("Agent Initialization", True, "Agente inicializado correctamente")
        except Exception as e:
            self.log_test("Agent Initialization", False, str(e))
    
    def test_intencion_detection(self):
        """Test: Detección de intenciones"""
        test_cases = [
            ("Quiero invertir en crypto", "inversión"),
            ("Necesito vender más productos", "ventas"),
            ("Busco propiedades en Buenos Aires", "real_estate"),
            ("Automatizar mi negocio", "automatización"),
            ("Hola, ¿cómo estás?", "consulta_general")
        ]
        
        for mensaje, intencion_esperada in test_cases:
            try:
                resultado = self.agent.detectar_intencion(mensaje)
                
                assert resultado["intencion"] == intencion_esperada
                assert "confidence" in resultado
                assert "emocion" in resultado
                
                self.log_test(f"Intención: '{mensaje}'", True, f"Detectada: {resultado['intencion']}")
            except Exception as e:
                self.log_test(f"Intención: '{mensaje}'", False, str(e))
    
    def test_lead_scoring(self):
        """Test: Sistema de scoring de leads"""
        test_contexts = [
            {
                "context": {
                    "urgencia": "alta",
                    "presupuesto": "100k USD",
                    "experiencia": "experto en inversiones",
                    "numero_mensajes": 5
                },
                "expected_min_score": 80
            },
            {
                "context": {
                    "urgencia": "media",
                    "presupuesto": "50k USD",
                    "experiencia": "algo de experiencia",
                    "numero_mensajes": 3
                },
                "expected_min_score": 40
            },
            {
                "context": {
                    "urgencia": "baja",
                    "presupuesto": "poco presupuesto",
                    "experiencia": "principiante",
                    "numero_mensajes": 1
                },
                "expected_min_score": 0
            }
        ]
        
        for test_case in test_contexts:
            try:
                resultado = self.agent.calcular_score_lead(test_case["context"])
                
                assert "score" in resultado
                assert "clasificacion" in resultado
                assert "recomendaciones" in resultado
                assert resultado["score"] >= test_case["expected_min_score"]
                
                self.log_test(
                    f"Lead Scoring (urgencia: {test_case['context']['urgencia']})",
                    True,
                    f"Score: {resultado['score']}, Clasificación: {resultado['clasificacion']}"
                )
            except Exception as e:
                self.log_test(f"Lead Scoring", False, str(e))
    
    def test_response_generation(self):
        """Test: Generación de respuestas"""
        test_cases = [
            {
                "mensaje": "Quiero invertir 100k USD en real estate",
                "pais": "Argentina",
                "vertical": "real_estate"
            },
            {
                "mensaje": "Necesito automatizar mi proceso de ventas",
                "pais": "España",
                "vertical": "automatización"
            },
            {
                "mensaje": "¿Cuál es la mejor estrategia de inversión actual?",
                "pais": "México",
                "vertical": "inversión"
            }
        ]
        
        for test_case in test_cases:
            try:
                resultado = self.agent.generar_respuesta(**test_case)
                
                assert "respuesta" in resultado
                assert "metadata" in resultado
                assert len(resultado["respuesta"]) > 100  # Respuesta sustancial
                assert "ALENYA" in resultado["respuesta"]
                
                self.log_test(
                    f"Respuesta ({test_case['pais']}, {test_case['vertical']})",
                    True,
                    f"Generada respuesta de {len(resultado['respuesta'])} caracteres"
                )
            except Exception as e:
                self.log_test(f"Generación de respuesta", False, str(e))
    
    def test_timezone_handling(self):
        """Test: Manejo de zonas horarias"""
        test_countries = ["Argentina", "España", "México", "Colombia"]
        
        for pais in test_countries:
            try:
                hora = self.agent.obtener_hora_local(pais)
                assert isinstance(hora, str)
                assert len(hora) > 5  # Formato de hora válido
                
                self.log_test(f"Zona horaria {pais}", True, f"Hora: {hora}")
            except Exception as e:
                self.log_test(f"Zona horaria {pais}", False, str(e))
    
    def test_api_endpoints(self):
        """Test: Endpoints de la API (requiere servidor corriendo)"""
        try:
            # Test status endpoint
            response = requests.get(f"{self.api_base}/status", timeout=5)
            if response.status_code == 200:
                data = response.json()
                assert data["success"] == True
                assert data["agent"] == "ALENYA"
                self.log_test("API Status Endpoint", True, "Servidor respondiendo correctamente")
                
                # Test chat endpoint
                chat_data = {
                    "message": "Hola ALENYA, ¿cómo estás?",
                    "pais": "Argentina"
                }
                
                response = requests.post(f"{self.api_base}/chat", json=chat_data, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    assert data["success"] == True
                    assert "respuesta" in data
                    self.log_test("API Chat Endpoint", True, "Chat funcionando correctamente")
                else:
                    self.log_test("API Chat Endpoint", False, f"Status code: {response.status_code}")
            else:
                self.log_test("API Status Endpoint", False, f"Status code: {response.status_code}")
                
        except requests.ConnectionError:
            self.log_test("API Endpoints", False, "Servidor no disponible (ejecuta app.py primero)")
        except Exception as e:
            self.log_test("API Endpoints", False, str(e))
    
    def test_personalization(self):
        """Test: Personalización por país y vertical"""
        personalization_tests = [
            ("Argentina", "inversión"),
            ("España", "real_estate"),
            ("México", "ventas"),
            ("Colombia", "automatización")
        ]
        
        for pais, vertical in personalization_tests:
            try:
                resultado = self.agent.generar_respuesta(
                    "Necesito ayuda con mi negocio",
                    pais=pais,
                    vertical=vertical
                )
                
                # Verificar que la respuesta contiene referencias específicas
                respuesta = resultado["respuesta"].lower()
                config_pais = self.agent.personalizacion_pais.get(pais, {})
                
                # Verificar metadata
                assert resultado["metadata"]["pais"] == pais
                assert resultado["metadata"]["vertical"] == vertical
                
                self.log_test(
                    f"Personalización {pais}-{vertical}",
                    True,
                    f"Respuesta personalizada generada"
                )
            except Exception as e:
                self.log_test(f"Personalización {pais}-{vertical}", False, str(e))
    
    def run_all_tests(self):
        """Ejecuta todos los tests"""
        print("🚀 ALENYA Test Suite - MELANO INC")
        print("=" * 50)
        print()
        
        # Lista de tests a ejecutar
        tests = [
            self.test_agent_initialization,
            self.test_intencion_detection,
            self.test_lead_scoring,
            self.test_response_generation,
            self.test_timezone_handling,
            self.test_personalization,
            self.test_api_endpoints
        ]
        
        # Ejecutar tests
        start_time = time.time()
        
        for test in tests:
            test()
            print()
        
        end_time = time.time()
        
        # Resultados finales
        total_tests = self.tests_passed + self.tests_failed
        success_rate = (self.tests_passed / total_tests * 100) if total_tests > 0 else 0
        
        print("=" * 50)
        print("📊 RESULTADOS FINALES")
        print(f"✅ Tests pasados: {self.tests_passed}")
        print(f"❌ Tests fallidos: {self.tests_failed}")
        print(f"📈 Tasa de éxito: {success_rate:.1f}%")
        print(f"⏱️ Tiempo total: {end_time - start_time:.2f}s")
        print("=" * 50)
        
        if self.tests_failed == 0:
            print("🎉 ¡Todos los tests pasaron! ALENYA está funcionando perfectamente.")
        else:
            print("⚠️ Algunos tests fallaron. Revisa los errores arriba.")
        
        return self.tests_failed == 0
    
    def export_results(self, filename: str = "alenya_test_results.json"):
        """Exporta los resultados de los tests"""
        results = {
            "timestamp": time.time(),
            "agent_version": self.agent.version,
            "total_tests": self.tests_passed + self.tests_failed,
            "tests_passed": self.tests_passed,
            "tests_failed": self.tests_failed,
            "success_rate": (self.tests_passed / (self.tests_passed + self.tests_failed) * 100) if (self.tests_passed + self.tests_failed) > 0 else 0,
            "test_details": self.test_results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Resultados exportados a: {filename}")

def main():
    """Función principal"""
    test_suite = AlenyaTestSuite()
    
    try:
        success = test_suite.run_all_tests()
        test_suite.export_results()
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n⏹️ Tests interrumpidos por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Error ejecutando tests: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
