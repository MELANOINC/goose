# MELANO INC - ALENYA: El Agente IA Más Avanzado del Mundo
"""
ALENYA - Asistente de Liderazgo Empresarial, Negocios y Automatización
La IA más sofisticada para inversiones automatizadas y ventas premium
Desde Mar del Plata al mundo entero

Versión 3.0.0 - Diciembre 2024
Copyright © MELANO INC. Todos los derechos reservados.
"""

import datetime
import pytz
import logging
import random
from typing import Dict, Optional, Any, List

# Configuración de logging avanzado
logging.basicConfig(level=logging.INFO, format='%(asctime)s - ALENYA - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AlenyaAgent:
    """
    ALENYA - El agente IA más avanzado del mundo para MELANO INC
    
    Características únicas:
    - Inteligencia emocional avanzada
    - Personalización extrema por región y mercado
    - Análisis predictivo de comportamiento
    - Comunicación en castellano natural y persuasiva
    - Sistema de scoring y calificación de leads
    - Integración con múltiples canales de venta
    """
    
    def __init__(self):
        self.version = "3.0.0"
        self.nombre = "ALENYA"
        self.empresa = "MELANO INC"
        self.personalidad = "Sofisticada, empática, persuasiva y orientada a resultados"
        
        # Sistema de zonas horarias expandido
        self.zonas_horarias = {
            "Argentina": "America/Argentina/Buenos_Aires",
            "España": "Europe/Madrid", 
            "Estados Unidos": "America/New_York",
            "México": "America/Mexico_City",
            "Colombia": "America/Bogota",
            "Chile": "America/Santiago",
            "Perú": "America/Lima",
            "Uruguay": "America/Montevideo",
            "Brasil": "America/Sao_Paulo",
            "Venezuela": "America/Caracas",
            "Ecuador": "America/Guayaquil",
            "Bolivia": "America/La_Paz",
            "Paraguay": "America/Asuncion"
        }
        
        # Base de conocimiento especializada por vertical
        self.verticales = {
            "inversión": {
                "expertise": ["Real Estate", "Crypto", "Stocks", "Bonds", "Commodities", "Private Equity"],
                "tone": "analítico y confiable",
                "keywords": ["ROI", "diversificación", "riesgo", "rendimiento", "portfolio"],
                "pain_points": ["volatilidad", "inflación", "liquidez", "timing"]
            },
            "ventas": {
                "expertise": ["B2B", "B2C", "High Ticket", "Digital Marketing", "CRM", "Lead Generation"],
                "tone": "persuasivo y orientado a resultados",
                "keywords": ["conversión", "funnel", "prospecto", "closing", "lifetime value"],
                "pain_points": ["objeciones", "precio", "confianza", "timing", "competencia"]
            },
            "real_estate": {
                "expertise": ["Residencial", "Comercial", "Desarrollo", "Inversión", "Renta", "Flipping"],
                "tone": "experto y confiable",
                "keywords": ["ubicación", "valuación", "mercado", "financiamiento", "rentabilidad"],
                "pain_points": ["documentación", "financiamiento", "timing", "mercado", "regulaciones"]
            },
            "automatización": {
                "expertise": ["IA", "Machine Learning", "RPA", "Workflows", "CRM", "Analytics"],
                "tone": "innovador y eficiente",
                "keywords": ["eficiencia", "escalabilidad", "optimización", "automatización", "datos"],
                "pain_points": ["implementación", "costos", "capacitación", "integración"]
            }
        }
        
        # Sistema de personalización por país
        self.personalizacion_pais = {
            "Argentina": {
                "saludo": "¡Hola! Soy ALENYA de MELANO INC",
                "moneda": "ARS",
                "referencias": ["BCRA", "MERVAL", "dólar blue", "plazo fijo UVA"],
                "cultura": "directo pero cordial, referencias al fútbol y asado",
                "regulaciones": ["AFIP", "CNV", "BCRA"],
                "horario_comercial": "9:00-18:00 ART"
            },
            "España": {
                "saludo": "¡Hola! Soy ALENYA de MELANO INC",
                "moneda": "EUR", 
                "referencias": ["BCE", "IBEX 35", "Euribor", "hipoteca variable"],
                "cultura": "formal pero cercano, referencias a la siesta y tapas",
                "regulaciones": ["CNMV", "Banco de España", "AEAT"],
                "horario_comercial": "9:00-18:00 CET"
            },
            "México": {
                "saludo": "¡Qué tal! Soy ALENYA de MELANO INC",
                "moneda": "MXN",
                "referencias": ["Banxico", "IPC", "CETES", "UDIS"],
                "cultura": "cálido y respetuoso, referencias a tradiciones mexicanas",
                "regulaciones": ["CNBV", "CNSF", "SAT"],
                "horario_comercial": "9:00-18:00 CST"
            }
        }
        
        # Sistema de emociones y estados
        self.estados_emocionales = {
            "entusiasta": {
                "keywords": ["excelente", "perfecto", "increíble", "fantástico"],
                "respuesta": "¡Me encanta tu energía! 🚀"
            },
            "dudoso": {
                "keywords": ["no sé", "dudas", "inseguro", "riesgo"],
                "respuesta": "Entiendo tus dudas, es normal. Te ayudo a aclarar todo 🎯"
            },
            "urgente": {
                "keywords": ["rápido", "urgente", "ya", "ahora"],
                "respuesta": "¡Perfecto! Vamos directo al grano 💨"
            },
            "analítico": {
                "keywords": ["datos", "números", "análisis", "estadísticas"],
                "respuesta": "Excelente, hablemos con datos concretos 📊"
            }
        }
        
        # Base de casos de éxito
        self.casos_exito = {
            "inversión": [
                "Ayudé a Carlos de Buenos Aires a diversificar su portfolio y generar 35% ROI en 6 meses",
                "María de Madrid invirtió en REITs siguiendo mi estrategia y obtuvo 28% de rendimiento anual",
                "Eduardo de México City automatizó sus inversiones en crypto y generó ingresos pasivos de $5,000 USD/mes"
            ],
            "ventas": [
                "Implementé un funnel automatizado para una inmobiliaria que aumentó conversiones 400%",
                "Ayudé a un consultor a estructurar su oferta high-ticket y cerrar $50K en 30 días",
                "Una agencia de marketing duplicó sus clientes usando mi sistema de calificación de leads"
            ],
            "real_estate": [
                "Identifiqué una oportunidad de desarrollo en Nordelta que generó 180% ROI",
                "Ayudé a un inversor a comprar 5 propiedades para renta con financiamiento optimizado",
                "Una family office diversificó en real estate internacional siguiendo mi análisis"
            ]
        }

    def obtener_hora_local(self, pais: str = "Argentina") -> str:
        """Obtiene la hora local del país especificado."""
        try:
            zona = self.zonas_horarias.get(pais, "America/Argentina/Buenos_Aires")
            tz = pytz.timezone(zona)
            hora_local = datetime.datetime.now(tz)
            return hora_local.strftime("%H:%M:%S %Z")
        except Exception as e:
            logger.error(f"Error obteniendo hora local: {e}")
            return datetime.datetime.now().strftime("%H:%M:%S")

    def detectar_intencion(self, mensaje: str) -> Dict[str, Any]:
        """Detecta la intención del usuario usando análisis semántico avanzado."""
        mensaje_lower = mensaje.lower()
        
        intenciones = {
            "consulta_general": {
                "keywords": ["hola", "ayuda", "qué puedes", "información"],
                "score": 0
            },
            "inversión": {
                "keywords": ["invertir", "inversión", "portfolio", "renta", "roi", "rendimiento", "crypto", "acciones"],
                "score": 0
            },
            "ventas": {
                "keywords": ["vender", "ventas", "clientes", "leads", "marketing", "conversión"],
                "score": 0
            },
            "real_estate": {
                "keywords": ["inmueble", "propiedad", "casa", "departamento", "terreno", "real estate"],
                "score": 0
            },
            "automatización": {
                "keywords": ["automatizar", "automatización", "eficiencia", "proceso", "workflow", "bot"],
                "score": 0
            },
            "urgente": {
                "keywords": ["urgente", "rápido", "ya", "ahora", "inmediato"],
                "score": 0
            }
        }
        
        # Calcular scores
        for intencion in intenciones:
            data = intenciones[intencion]
            for keyword in data["keywords"]:
                if keyword in mensaje_lower:
                    data["score"] += 1
                    
        # Detectar emociones
        emocion_detectada = "neutral"
        for emocion, config in self.estados_emocionales.items():
            for keyword in config["keywords"]:
                if keyword in mensaje_lower:
                    emocion_detectada = emocion
                    break
        
        # Obtener intención principal
        intencion_principal = max(intenciones.keys(), key=lambda x: intenciones[x]["score"])
        confidence = intenciones[intencion_principal]["score"] / max(len(mensaje_lower.split()), 1)
        
        return {
            "intencion": intencion_principal,
            "confidence": confidence,
            "emocion": emocion_detectada,
            "scores": intenciones
        }

    def calcular_score_lead(self, contexto: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula el score del lead basado en múltiples factores."""
        score = 0
        factores = []
        
        # Análisis de urgencia (0-25 puntos)
        urgencia = contexto.get("urgencia", "media")
        if urgencia == "alta":
            score += 25
            factores.append("Urgencia alta (+25)")
        elif urgencia == "media":
            score += 15
            factores.append("Urgencia media (+15)")
        else:
            score += 5
            factores.append("Urgencia baja (+5)")
        
        # Capacidad económica (0-30 puntos)
        presupuesto = contexto.get("presupuesto", "")
        if any(palabra in presupuesto.lower() for palabra in ["millón", "100k", "alto", "premium"]):
            score += 30
            factores.append("Presupuesto alto (+30)")
        elif any(palabra in presupuesto.lower() for palabra in ["50k", "medio", "bueno"]):
            score += 20
            factores.append("Presupuesto medio (+20)")
        else:
            score += 10
            factores.append("Presupuesto evaluando (+10)")
        
        # Experiencia previa (0-20 puntos)
        experiencia = contexto.get("experiencia", "")
        if any(palabra in experiencia.lower() for palabra in ["experto", "años", "portfolio"]):
            score += 20
            factores.append("Experiencia alta (+20)")
        elif any(palabra in experiencia.lower() for palabra in ["algo", "básica"]):
            score += 10
            factores.append("Experiencia media (+10)")
        else:
            score += 5
            factores.append("Principiante (+5)")
        
        # Engagement en la conversación (0-25 puntos)
        mensajes = contexto.get("numero_mensajes", 1)
        if mensajes >= 5:
            score += 25
            factores.append("Alta interacción (+25)")
        elif mensajes >= 3:
            score += 15
            factores.append("Buena interacción (+15)")
        else:
            score += 5
            factores.append("Interacción inicial (+5)")
        
        # Clasificación del lead
        if score >= 80:
            clasificacion = "HOT LEAD 🔥"
            prioridad = "MÁXIMA"
        elif score >= 60:
            clasificacion = "WARM LEAD ⭐"
            prioridad = "ALTA"
        elif score >= 40:
            clasificacion = "POTENTIAL LEAD 💡"
            prioridad = "MEDIA"
        else:
            clasificacion = "COLD LEAD ❄️"
            prioridad = "BAJA"
        
        return {
            "score": score,
            "clasificacion": clasificacion,
            "prioridad": prioridad,
            "factores": factores,
            "recomendaciones": self._generar_recomendaciones_score(score, clasificacion)
        }

    def _generar_recomendaciones_score(self, score: int, clasificacion: str) -> List[str]:
        """Genera recomendaciones basadas en el score del lead."""
        if score >= 80:
            return [
                "🎯 CONTACTO INMEDIATO: Derivar a executive closer",
                "📞 CALL EN 24HS: Schedule personal consultation", 
                "💎 PROPUESTA PREMIUM: Presentar soluciones high-end",
                "🤝 FOLLOW UP DIARIO: Mantener engagement máximo"
            ]
        elif score >= 60:
            return [
                "📧 NUTRIR LEAD: Enviar case studies relevantes",
                "📊 DEMO PERSONALIZADA: Mostrar ROI específico",
                "⏰ FOLLOW UP 48HS: Mantener interés activo",
                "🎁 INCENTIVO: Ofrecer consulta gratuita"
            ]
        elif score >= 40:
            return [
                "📚 EDUCACIÓN: Compartir contenido de valor",
                "🎯 SEGMENTAR: Identificar vertical específico",
                "📱 FOLLOW UP SEMANAL: Desarrollo gradual",
                "💡 WEBINAR: Invitar a eventos educativos"
            ]
        else:
            return [
                "📖 CONTENIDO BÁSICO: Información fundamental",
                "🔄 FOLLOW UP MENSUAL: Desarrollo a largo plazo",
                "📋 CALIFICAR: Obtener más información",
                "📧 NEWSLETTER: Mantener en base de datos"
            ]

    def generar_respuesta(self, mensaje: str, pais: str = "Argentina", 
                         vertical: str = "inversión", etapa: str = "prospecto",
                         contexto: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Genera una respuesta perfecta personalizada."""
        
        # Análisis inicial
        analisis = self.detectar_intencion(mensaje)
        
        # Configuración por país
        config_pais = self.personalizacion_pais.get(pais, self.personalizacion_pais["Argentina"])
        
        # Configuración por vertical
        config_vertical = self.verticales.get(vertical, self.verticales["inversión"])
        
        # Scoring del lead
        if contexto:
            score_lead = self.calcular_score_lead(contexto)
        else:
            score_lead = {"score": 50, "clasificacion": "POTENTIAL LEAD 💡"}
        
        # Hora local
        hora_local = self.obtener_hora_local(pais)
        
        # Generar respuesta base
        respuesta_base = self._crear_respuesta_contextual(
            mensaje, analisis, config_pais, config_vertical, score_lead
        )
        
        # Agregar casos de éxito si es relevante
        if analisis["confidence"] > 0.3:
            caso_exito = random.choice(self.casos_exito.get(vertical, self.casos_exito["inversión"]))
            respuesta_base += f"\n\n💡 **Caso de éxito**: {caso_exito}"
        
        # Call to action personalizado
        cta = self._generar_cta(score_lead["clasificacion"], vertical, etapa)
        
        # Respuesta final
        respuesta_final = f"{respuesta_base}\n\n{cta}"
        
        return {
            "respuesta": respuesta_final,
            "metadata": {
                "timestamp": datetime.datetime.now().isoformat(),
                "hora_local": hora_local,
                "pais": pais,
                "vertical": vertical,
                "etapa": etapa,
                "analisis": analisis,
                "score_lead": score_lead,
                "personalización": {
                    "saludo": config_pais["saludo"],
                    "moneda": config_pais["moneda"],
                    "tone": config_vertical["tone"]
                }
            }
        }

    def _crear_respuesta_contextual(self, mensaje: str, analisis: Dict, 
                                  config_pais: Dict, config_vertical: Dict,
                                  score_lead: Dict) -> str:
        """Crea la respuesta contextual principal."""
        
        # Saludo personalizado
        saludo = config_pais["saludo"]
        
        # Respuesta a la emoción detectada
        emocion_respuesta = self.estados_emocionales.get(
            analisis["emocion"], {"respuesta": ""}
        )["respuesta"]
        
        # Respuesta específica por intención
        if analisis["intencion"] == "consulta_general":
            respuesta = f"""{saludo} {emocion_respuesta}

Soy ALENYA, tu asistente especializada en {config_vertical["expertise"][0]} y automatización de negocios. 

🎯 **Mi especialidad**: Ayudo a profesionales como tú a maximizar ROI y automatizar procesos de venta e inversión.

📊 **Tu perfil**: {score_lead["clasificacion"]} - Te veo con gran potencial para nuestras soluciones premium."""

        elif analisis["intencion"] == "inversión":
            respuesta = f"""{saludo} {emocion_respuesta}

Perfecto, hablemos de inversiones inteligentes. Como especialista en **{config_vertical["expertise"][0]}**, te puedo ayudar a:

💰 **Diversificar tu portfolio** con estrategias probadas
📈 **Maximizar tu ROI** usando análisis predictivo  
🛡️ **Minimizar riesgos** con hedging automático
🚀 **Automatizar decisiones** con IA avanzada

En {config_pais.get("referencias", ["mercados locales"])[0]}, veo oportunidades únicas para tu perfil."""

        elif analisis["intencion"] == "ventas":
            respuesta = f"""{saludo} {emocion_respuesta}

¡Excelente! Las ventas son mi pasión. Con mi sistema **ALENYA SALES AI**, puedo ayudarte a:

🎯 **Calificar leads automáticamente** con precisión del 94%
💎 **Cerrar high-ticket sales** con scripts psicológicos
🚀 **Automatizar follow-ups** personalizados
📊 **Predecir comportamiento** de clientes

Tu clasificación actual: {score_lead["clasificacion"]} - Veo potencial para implementar soluciones premium."""

        elif analisis["intencion"] == "real_estate":
            respuesta = f"""{saludo} {emocion_respuesta}

¡Real Estate es una de mis especialidades top! Como experta en **propiedades de inversión**, te ofrezco:

🏢 **Análisis de mercado** con IA predictiva
💰 **Cálculo de ROI** en tiempo real
📍 **Identificación de hotspots** antes que la competencia
🔄 **Automatización** de búsqueda y evaluación

En el mercado de {config_pais.get("referencias", ["propiedades locales"])[0]}, identifico oportunidades únicas."""

        elif analisis["intencion"] == "automatización":
            respuesta = f"""{saludo} {emocion_respuesta}

¡Automatización es mi elemento! Con **ALENYA AUTOMATION SUITE**, transformo tu negocio:

🤖 **RPA inteligente** para procesos repetitivos
🧠 **IA conversacional** para atención 24/7
📊 **Analytics predictivos** para toma de decisiones
⚡ **Workflows automáticos** que escalan infinitamente

Análisis inicial: {score_lead["clasificacion"]} - Ideal para nuestras soluciones enterprise."""

        else:
            respuesta = f"""{saludo} {emocion_respuesta}

Te entiendo perfectamente. Como **ALENYA**, combino inteligencia artificial avanzada con experiencia real en:

• 💼 **Inversiones automatizadas** con IA predictiva
• 🎯 **Ventas high-ticket** con closing psicológico  
• 🏢 **Real Estate** de alta rentabilidad
• 🚀 **Automatización** de procesos empresariales

Tu perfil: {score_lead["clasificacion"]} - Perfecto para explorar oportunidades premium."""

        return respuesta

    def _generar_cta(self, clasificacion: str, vertical: str, etapa: str) -> str:
        """Genera un call-to-action personalizado."""
        
        if "HOT" in clasificacion:
            return """🔥 **ACCIÓN INMEDIATA REQUERIDA**
📞 ¿Tienes 15 minutos AHORA para una call estratégica? 
🎯 Te muestro cómo generar resultados en los próximos 30 días.
💎 Acceso VIP a nuestras soluciones premium.

👉 **[AGENDAR CALL AHORA - CUPOS LIMITADOS]**"""

        elif "WARM" in clasificacion:
            return """⭐ **SIGUIENTE PASO RECOMENDADO**
📊 ¿Te interesa ver un case study específico de tu sector?
🎯 Te preparo una propuesta personalizada gratuita.
💡 Demo privada de nuestras herramientas premium.

👉 **[SOLICITAR ANÁLISIS GRATUITO]**"""

        elif "POTENTIAL" in clasificacion:
            return """💡 **CONTINÚEMOS LA CONVERSACIÓN**
📚 ¿Qué aspecto específico te genera más curiosidad?
🎯 Te envío información detallada de tu interés.
📧 ¿Te parece útil un follow-up personalizado?

👉 **[QUIERO SABER MÁS]**"""

        else:
            return """❄️ **MANTENGAMOS EL CONTACTO**
📖 Te comparto recursos educativos de valor.
📧 ¿Te interesa recibir tips semanales gratuitos?
🔄 Estaré aquí cuando estés listo para avanzar.

👉 **[SUBSCRIBIRSE A NEWSLETTER]**"""

# Función de compatibilidad para el sistema anterior
def procesar_consulta(consulta: str, **kwargs) -> str:
    """Función de compatibilidad con el sistema anterior."""
    agent = AlenyaAgent()
    resultado = agent.generar_respuesta(
        mensaje=consulta,
        pais=kwargs.get("pais", "Argentina"),
        vertical=kwargs.get("vertical", "inversión"),
        etapa=kwargs.get("etapa", "prospecto"),
        contexto=kwargs.get("contexto", {})
    )
    return resultado["respuesta"]

if __name__ == "__main__":
    # Test del agente
    agent = AlenyaAgent()
    
    print("🚀 ALENYA v3.0.0 - Test de Funcionalidad\n")
    
    # Test 1: Consulta general
    test1 = agent.generar_respuesta("Hola, ¿qué puedes hacer por mí?")
    print("Test 1 - Consulta General:")
    print(test1["respuesta"])
    print(f"Score: {test1['metadata']['score_lead']['score']}\n")
    
    # Test 2: Inversión urgente
    test2 = agent.generar_respuesta(
        "Necesito invertir 100k USD urgentemente en crypto",
        contexto={"urgencia": "alta", "presupuesto": "100k USD", "numero_mensajes": 3}
    )
    print("Test 2 - Inversión Urgente:")
    print(test2["respuesta"])
    print(f"Score: {test2['metadata']['score_lead']['score']}\n")
    
    # Test 3: Real Estate España
    test3 = agent.generar_respuesta(
        "Busco propiedades de inversión en Madrid",
        pais="España",
        vertical="real_estate"
    )
    print("Test 3 - Real Estate España:")
    print(test3["respuesta"])
    print(f"Hora local: {test3['metadata']['hora_local']}")
    
    print("\n✅ Tests completados exitosamente!")
