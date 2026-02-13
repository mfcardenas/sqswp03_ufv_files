/**
 * questions_fallback.js
 * ─────────────────────────────────────────────────────────
 * Pool de preguntas agrupadas por nivel (1-15).
 * Cada nivel tiene 3 preguntas alternativas.
 * game.js selecciona una al azar por nivel para cada partida.
 * ─────────────────────────────────────────────────────────
 */

export const FALLBACK_POOL = {
    game_title_es: "Quien quiere ser ISOmillonario (reserva)",
    game_title_en: "Who wants to be ISOmillionaire (fallback)",
    iso_focus: ["ISO 9241", "ISO/IEC/IEEE 29148", "ISO/IEC 25010:2023"],
    pool: {
        /* ════════════════════ NIVEL 1 — $100 ════════════════════ */
        1: [
            {
                id: "q1a", level: 1, amount: 100, iso_standard: "ISO 9241",
                context_es: "Una app bancaria oculta el botón de transferencias en un menú poco visible.",
                context_en: "A banking app hides the transfer button in a barely visible menu.",
                question_es: "¿Qué atributo de ISO 9241 se ve más afectado?",
                question_en: "Which ISO 9241 attribute is most impacted?",
                options_es: ["Seguridad", "Eficiencia", "Detectabilidad", "Portabilidad"],
                options_en: ["Security", "Efficiency", "Findability", "Portability"],
                correct_index: 2,
                option_difficulty: ["easy", "medium", "easy", "hard"],
                hint_es: "Piensa en la facilidad para localizar elementos.",
                hint_en: "Think about how easy it is to locate elements.",
                friend_answer_es: "Yo elegiría detectabilidad, es difícil encontrarlo.",
                friend_answer_en: "I'd pick findability; it's hard to find.",
                friend_confidence: "high"
            },
            {
                id: "q1b", level: 1, amount: 100, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un sitio web tarda 12 segundos en mostrar su página de inicio.",
                context_en: "A website takes 12 seconds to display its homepage.",
                question_es: "¿Qué característica de calidad se ve más afectada según ISO 25010?",
                question_en: "Which quality characteristic is most affected according to ISO 25010?",
                options_es: ["Seguridad", "Eficiencia de rendimiento", "Compatibilidad", "Mantenibilidad"],
                options_en: ["Security", "Performance efficiency", "Compatibility", "Maintainability"],
                correct_index: 1,
                option_difficulty: ["hard", "easy", "medium", "medium"],
                hint_es: "Piensa en el tiempo de respuesta.",
                hint_en: "Think about response time.",
                friend_answer_es: "Rendimiento, clarísimo.",
                friend_answer_en: "Performance, obviously.",
                friend_confidence: "high"
            },
            {
                id: "q1c", level: 1, amount: 100, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un requisito dice: 'El sistema debe funcionar bien'.",
                context_en: "A requirement states: 'The system should work well'.",
                question_es: "¿Qué atributo de calidad de requisitos falta?",
                question_en: "Which requirement quality attribute is missing?",
                options_es: ["Trazabilidad", "No ambigüedad", "Consistencia", "Completitud"],
                options_en: ["Traceability", "Unambiguity", "Consistency", "Completeness"],
                correct_index: 1,
                option_difficulty: ["medium", "easy", "hard", "medium"],
                hint_es: "'Funcionar bien' tiene muchos significados.",
                hint_en: "'Work well' has many meanings.",
                friend_answer_es: "Demasiado vago, falta no ambigüedad.",
                friend_answer_en: "Too vague, unambiguity is missing.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 2 — $200 ════════════════════ */
        2: [
            {
                id: "q2a", level: 2, amount: 200, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "El documento de requisitos mezcla reglas de negocio y UI en el mismo apartado.",
                context_en: "The requirements document mixes business rules and UI in the same section.",
                question_es: "¿Qué principio de ISO 29148 se incumple?",
                question_en: "Which ISO 29148 principle is violated?",
                options_es: ["Verificabilidad", "Clasificación lógica", "Trazabilidad", "Consistencia"],
                options_en: ["Verifiability", "Logical structuring", "Traceability", "Consistency"],
                correct_index: 1,
                option_difficulty: ["medium", "easy", "hard", "medium"],
                hint_es: "Piensa en la organización clara de requisitos.",
                hint_en: "Consider clear organization of requirements.",
                friend_answer_es: "Yo apostaría por clasificación lógica.",
                friend_answer_en: "I'd go with logical structuring.",
                friend_confidence: "medium"
            },
            {
                id: "q2b", level: 2, amount: 200, iso_standard: "ISO 9241",
                context_es: "Un formulario web no muestra qué campos son obligatorios hasta enviar.",
                context_en: "A web form doesn't show which fields are required until submission.",
                question_es: "¿Qué principio de ISO 9241 se incumple?",
                question_en: "Which ISO 9241 principle is violated?",
                options_es: ["Adecuación a la tarea", "Autodescriptivo", "Tolerancia a errores", "Flexibilidad"],
                options_en: ["Suitability for the task", "Self-descriptiveness", "Error tolerance", "Flexibility"],
                correct_index: 1,
                option_difficulty: ["medium", "easy", "hard", "medium"],
                hint_es: "El sistema debe informar antes de actuar.",
                hint_en: "The system should inform before acting.",
                friend_answer_es: "Autodescriptivo, seguro.",
                friend_answer_en: "Self-descriptiveness, for sure.",
                friend_confidence: "high"
            },
            {
                id: "q2c", level: 2, amount: 200, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un CRM almacena contraseñas en texto plano en la base de datos.",
                context_en: "A CRM stores passwords as plain text in the database.",
                question_es: "¿Qué subcaracterística de calidad se compromete?",
                question_en: "Which quality sub-characteristic is compromised?",
                options_es: ["Seguridad: confidencialidad", "Fiabilidad: disponibilidad", "Usabilidad: accesibilidad", "Portabilidad: adaptabilidad"],
                options_en: ["Security: confidentiality", "Reliability: availability", "Usability: accessibility", "Portability: adaptability"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "hard"],
                hint_es: "Los datos sensibles deben estar protegidos.",
                hint_en: "Sensitive data must be protected.",
                friend_answer_es: "Confidencialidad, claro.",
                friend_answer_en: "Confidentiality, of course.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 3 — $300 ════════════════════ */
        3: [
            {
                id: "q3a", level: 3, amount: 300, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un sistema POS funciona rápido pero falla con frecuencia en horas pico.",
                context_en: "A POS system is fast but frequently fails during peak hours.",
                question_es: "¿Qué característica de calidad se afecta más?",
                question_en: "Which quality characteristic is most affected?",
                options_es: ["Confiabilidad", "Usabilidad", "Compatibilidad", "Seguridad"],
                options_en: ["Reliability", "Usability", "Compatibility", "Security"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "hard"],
                hint_es: "Piensa en disponibilidad y tolerancia a fallos.",
                hint_en: "Think about availability and fault tolerance.",
                friend_answer_es: "Confiabilidad, porque falla en momentos críticos.",
                friend_answer_en: "Reliability, since it fails at critical times.",
                friend_confidence: "high"
            },
            {
                id: "q3b", level: 3, amount: 300, iso_standard: "ISO 9241",
                context_es: "Una app de mensajería no confirma si un mensaje fue enviado o no.",
                context_en: "A messaging app doesn't confirm whether a message was sent or not.",
                question_es: "¿Qué principio de ISO 9241 se incumple?",
                question_en: "Which ISO 9241 principle is violated?",
                options_es: ["Conformidad con expectativas", "Detectabilidad", "Control del usuario", "Adecuación a la tarea"],
                options_en: ["Conformity with expectations", "Findability", "User control", "Suitability for the task"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "Los usuarios esperan recibir acuse de recibo.",
                hint_en: "Users expect to receive delivery confirmation.",
                friend_answer_es: "Conformidad, los usuarios esperan feedback.",
                friend_answer_en: "Conformity, users expect feedback.",
                friend_confidence: "high"
            },
            {
                id: "q3c", level: 3, amount: 300, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un requisito incluye dos funciones distintas en la misma frase.",
                context_en: "A requirement includes two distinct functions in the same sentence.",
                question_es: "¿Qué atributo de calidad de requisitos se incumple?",
                question_en: "Which requirement quality attribute is violated?",
                options_es: ["Completitud", "Atomicidad", "Verificabilidad", "Trazabilidad"],
                options_en: ["Completeness", "Atomicity", "Verifiability", "Traceability"],
                correct_index: 1,
                option_difficulty: ["medium", "easy", "hard", "medium"],
                hint_es: "Cada requisito debe expresar una sola idea.",
                hint_en: "Each requirement should express one single idea.",
                friend_answer_es: "Atomicidad, cada requisito una función.",
                friend_answer_en: "Atomicity, one function per requirement.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 4 — $500 ════════════════════ */
        4: [
            {
                id: "q4a", level: 4, amount: 500, iso_standard: "ISO 9241",
                context_es: "Usuarios novatos se pierden porque los iconos no describen su función.",
                context_en: "Novice users get lost because icons do not describe their function.",
                question_es: "¿Qué principio de ISO 9241 se viola?",
                question_en: "Which ISO 9241 principle is violated?",
                options_es: ["Adecuación a la tarea", "Autodescriptivo", "Flexibilidad", "Error defensivo"],
                options_en: ["Suitability for the task", "Self-descriptiveness", "Flexibility", "Error tolerance"],
                correct_index: 1,
                option_difficulty: ["medium", "easy", "hard", "medium"],
                hint_es: "El sistema debería explicarse por sí mismo.",
                hint_en: "The system should explain itself.",
                friend_answer_es: "Autodescriptivo, seguro.",
                friend_answer_en: "Self-descriptiveness, for sure.",
                friend_confidence: "high"
            },
            {
                id: "q4b", level: 4, amount: 500, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un sistema hospitalario no puede intercambiar datos con otro hospital.",
                context_en: "A hospital system cannot exchange data with another hospital.",
                question_es: "¿Qué subcaracterística de calidad se ve comprometida?",
                question_en: "Which quality sub-characteristic is compromised?",
                options_es: ["Compatibilidad: interoperabilidad", "Portabilidad: adaptabilidad", "Mantenibilidad: modularidad", "Seguridad: integridad"],
                options_en: ["Compatibility: interoperability", "Portability: adaptability", "Maintainability: modularity", "Security: integrity"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "hard"],
                hint_es: "¿Pueden dos sistemas intercambiar información?",
                hint_en: "Can two systems exchange information?",
                friend_answer_es: "Interoperabilidad, claramente.",
                friend_answer_en: "Interoperability, clearly.",
                friend_confidence: "high"
            },
            {
                id: "q4c", level: 4, amount: 500, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un stakeholder pide un requisito pero no se documenta quién lo solicitó.",
                context_en: "A stakeholder requests a requirement but it's not documented who asked for it.",
                question_es: "¿Qué principio de ISO 29148 se incumple?",
                question_en: "Which ISO 29148 principle is violated?",
                options_es: ["Trazabilidad", "Verificabilidad", "Completitud", "No ambigüedad"],
                options_en: ["Traceability", "Verifiability", "Completeness", "Unambiguity"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "Se debe seguir el origen de cada requisito.",
                hint_en: "Every requirement's origin should be traceable.",
                friend_answer_es: "Trazabilidad, hay que saber quién lo pidió.",
                friend_answer_en: "Traceability, you must know who requested it.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 5 — $1,000 ════════════════════ */
        5: [
            {
                id: "q5a", level: 5, amount: 1000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Los requisitos usan verbos ambiguos como 'optimizar'.",
                context_en: "Requirements use ambiguous verbs like 'optimize'.",
                question_es: "¿Qué atributo de calidad falta?",
                question_en: "Which quality attribute is missing?",
                options_es: ["Realizables", "Completos", "Medibles", "Compatibles"],
                options_en: ["Feasible", "Complete", "Measurable", "Compatible"],
                correct_index: 2,
                option_difficulty: ["medium", "medium", "easy", "hard"],
                hint_es: "Se necesita un objetivo cuantificable.",
                hint_en: "A quantifiable goal is needed.",
                friend_answer_es: "Diría medibles.",
                friend_answer_en: "I'd say measurable.",
                friend_confidence: "medium"
            },
            {
                id: "q5b", level: 5, amount: 1000, iso_standard: "ISO 9241",
                context_es: "Un sistema de reservas no permite deshacer una confirmación accidental.",
                context_en: "A booking system doesn't allow undoing an accidental confirmation.",
                question_es: "¿Qué principio de ISO 9241 falta?",
                question_en: "Which ISO 9241 principle is missing?",
                options_es: ["Tolerancia a errores", "Detectabilidad", "Autodescriptivo", "Adecuación a la tarea"],
                options_en: ["Error tolerance", "Findability", "Self-descriptiveness", "Suitability for the task"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "El usuario necesita poder corregir errores.",
                hint_en: "The user needs to be able to correct mistakes.",
                friend_answer_es: "Tolerancia a errores, necesitas deshacer.",
                friend_answer_en: "Error tolerance, you need undo.",
                friend_confidence: "high"
            },
            {
                id: "q5c", level: 5, amount: 1000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un módulo de facturación no puede probarse de forma aislada.",
                context_en: "A billing module cannot be tested in isolation.",
                question_es: "¿Qué subcaracterística de calidad se ve afectada?",
                question_en: "Which quality sub-characteristic is affected?",
                options_es: ["Mantenibilidad: testeabilidad", "Seguridad: autenticación", "Usabilidad: operabilidad", "Fiabilidad: recuperabilidad"],
                options_en: ["Maintainability: testability", "Security: authentication", "Usability: operability", "Reliability: recoverability"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "¿Se puede verificar cada parte por separado?",
                hint_en: "Can each part be verified separately?",
                friend_answer_es: "Testeabilidad, claramente.",
                friend_answer_en: "Testability, clearly.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 6 — $2,000 ════════════════════ */
        6: [
            {
                id: "q6a", level: 6, amount: 2000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un portal educativo funciona en Chrome pero no en Safari.",
                context_en: "An education portal works in Chrome but not Safari.",
                question_es: "¿Qué subcaracterística está en riesgo?",
                question_en: "Which sub-characteristic is at risk?",
                options_es: ["Compatibilidad co-existencia", "Portabilidad adaptabilidad", "Usabilidad accesibilidad", "Seguridad confidencialidad"],
                options_en: ["Compatibility co-existence", "Portability adaptability", "Usability accessibility", "Security confidentiality"],
                correct_index: 1,
                option_difficulty: ["medium", "easy", "medium", "hard"],
                hint_es: "Piensa en ejecutar en múltiples entornos.",
                hint_en: "Think about running on multiple environments.",
                friend_answer_es: "Adaptabilidad, claro.",
                friend_answer_en: "Adaptability, of course.",
                friend_confidence: "high"
            },
            {
                id: "q6b", level: 6, amount: 2000, iso_standard: "ISO 9241",
                context_es: "Un sistema financiero muestra datos exactos pero el color de fondo dificulta la lectura.",
                context_en: "A financial system shows accurate data but the background color makes it hard to read.",
                question_es: "¿Qué principio de ISO 9241 se ve más afectado?",
                question_en: "Which ISO 9241 principle is most affected?",
                options_es: ["Adecuación a la percepción", "Control del usuario", "Flexibilidad", "Conformidad con expectativas"],
                options_en: ["Suitability for perception", "User control", "Flexibility", "Conformity with expectations"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "¿Puede el usuario percibir bien la información?",
                hint_en: "Can the user perceive the information well?",
                friend_answer_es: "Adecuación a la percepción, el contraste importa.",
                friend_answer_en: "Suitability for perception, contrast matters.",
                friend_confidence: "high"
            },
            {
                id: "q6c", level: 6, amount: 2000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un documento SRS no distingue entre requisitos obligatorios y opcionales.",
                context_en: "An SRS document doesn't distinguish between mandatory and optional requirements.",
                question_es: "¿Qué atributo de calidad de requisitos falta?",
                question_en: "Which requirement quality attribute is missing?",
                options_es: ["Priorización", "Trazabilidad", "No ambigüedad", "Atomicidad"],
                options_en: ["Prioritization", "Traceability", "Unambiguity", "Atomicity"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "No todos los requisitos tienen la misma importancia.",
                hint_en: "Not all requirements have the same importance.",
                friend_answer_es: "Priorización, hay que separar lo obligatorio.",
                friend_answer_en: "Prioritization, you must separate mandatory items.",
                friend_confidence: "medium"
            }
        ],

        /* ════════════════════ NIVEL 7 — $4,000 ════════════════════ */
        7: [
            {
                id: "q7a", level: 7, amount: 4000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Los cambios de requisitos no guardan relación con sus historias originales.",
                context_en: "Requirement changes are not linked to their original stories.",
                question_es: "¿Qué atributo falta?",
                question_en: "Which attribute is missing?",
                options_es: ["Trazabilidad", "Unicidad", "Verificabilidad", "Testabilidad"],
                options_en: ["Traceability", "Uniqueness", "Verifiability", "Testability"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "Debe seguirse el rastro del requisito.",
                hint_en: "One must follow the requirement trail.",
                friend_answer_es: "Trazabilidad me suena correcto.",
                friend_answer_en: "Traceability sounds right.",
                friend_confidence: "high"
            },
            {
                id: "q7b", level: 7, amount: 4000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Una app de salud requiere 30 pasos para completar una acción simple.",
                context_en: "A health app requires 30 steps to complete a simple action.",
                question_es: "¿Qué subcaracterística de calidad se ve más afectada?",
                question_en: "Which quality sub-characteristic is most affected?",
                options_es: ["Usabilidad: operabilidad", "Seguridad: integridad", "Eficiencia: capacidad", "Portabilidad: instalabilidad"],
                options_en: ["Usability: operability", "Security: integrity", "Efficiency: capacity", "Portability: installability"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "hard"],
                hint_es: "¿Cuánto esfuerzo requiere realizar la tarea?",
                hint_en: "How much effort does the task require?",
                friend_answer_es: "Operabilidad, demasiados pasos.",
                friend_answer_en: "Operability, too many steps.",
                friend_confidence: "high"
            },
            {
                id: "q7c", level: 7, amount: 4000, iso_standard: "ISO 9241",
                context_es: "Un editor de texto no permite personalizar atajos de teclado ni la barra de herramientas.",
                context_en: "A text editor doesn't allow customizing keyboard shortcuts or the toolbar.",
                question_es: "¿Qué principio de ISO 9241 se incumple?",
                question_en: "Which ISO 9241 principle is violated?",
                options_es: ["Individualización", "Autodescriptivo", "Conformidad con expectativas", "Tolerancia a errores"],
                options_en: ["Individualization", "Self-descriptiveness", "Conformity with expectations", "Error tolerance"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "Cada usuario tiene preferencias distintas.",
                hint_en: "Each user has different preferences.",
                friend_answer_es: "Individualización, el usuario quiere adaptar la herramienta.",
                friend_answer_en: "Individualization, users want to adapt the tool.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 8 — $8,000 ════════════════════ */
        8: [
            {
                id: "q8a", level: 8, amount: 8000, iso_standard: "ISO 9241",
                context_es: "Un chatbot obliga a reescribir datos tras cada error.",
                context_en: "A chatbot forces users to retype data after each error.",
                question_es: "¿Qué principio falta?",
                question_en: "Which principle is missing?",
                options_es: ["Recuperación de errores", "Control del usuario", "Conformidad con expectativas", "Compatibilidad"],
                options_en: ["Error recovery", "User control", "Conformity with expectations", "Compatibility"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "medium", "hard"],
                hint_es: "Piensa en ayudar tras equivocarse.",
                hint_en: "Think about helping after mistakes.",
                friend_answer_es: "Recuperación, sin duda.",
                friend_answer_en: "Recovery, no doubt.",
                friend_confidence: "high"
            },
            {
                id: "q8b", level: 8, amount: 8000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Una aplicación bancaria no tiene logs de auditoría para las transacciones.",
                context_en: "A banking application has no audit logs for transactions.",
                question_es: "¿Qué subcaracterística de calidad se incumple?",
                question_en: "Which quality sub-characteristic is not met?",
                options_es: ["Seguridad: trazabilidad", "Fiabilidad: recuperabilidad", "Mantenibilidad: analizabilidad", "Usabilidad: protección de errores"],
                options_en: ["Security: accountability", "Reliability: recoverability", "Maintainability: analyzability", "Usability: error protection"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "Las acciones deben poder rastrearse.",
                hint_en: "Actions should be traceable.",
                friend_answer_es: "Trazabilidad de seguridad, hay que tener registros.",
                friend_answer_en: "Security accountability, you need records.",
                friend_confidence: "high"
            },
            {
                id: "q8c", level: 8, amount: 8000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "El mismo requisito aparece definido de forma diferente en dos secciones del SRS.",
                context_en: "The same requirement is defined differently in two sections of the SRS.",
                question_es: "¿Qué atributo de calidad falta?",
                question_en: "Which quality attribute is missing?",
                options_es: ["Consistencia", "Completitud", "Verificabilidad", "Viabilidad"],
                options_en: ["Consistency", "Completeness", "Verifiability", "Feasibility"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "No deben existir contradicciones entre secciones.",
                hint_en: "There should be no contradictions between sections.",
                friend_answer_es: "Consistencia, están en conflicto.",
                friend_answer_en: "Consistency, they're in conflict.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 9 — $16,000 ════════════════════ */
        9: [
            {
                id: "q9a", level: 9, amount: 16000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un motor de IA agrega nuevas funciones sin documentos de instalación claros.",
                context_en: "An AI engine adds new features without clear installation docs.",
                question_es: "¿Qué subcaracterística afecta?",
                question_en: "Which sub-characteristic is affected?",
                options_es: ["Mantenibilidad modularidad", "Portabilidad instalabilidad", "Usabilidad satisfacción", "Seguridad integridad"],
                options_en: ["Maintainability modularity", "Portability installability", "Usability satisfaction", "Security integrity"],
                correct_index: 1,
                option_difficulty: ["medium", "easy", "hard", "medium"],
                hint_es: "Facilidad para instalar en un entorno.",
                hint_en: "Ease of installing in an environment.",
                friend_answer_es: "Instalabilidad parece obvio.",
                friend_answer_en: "Installability seems obvious.",
                friend_confidence: "high"
            },
            {
                id: "q9b", level: 9, amount: 16000, iso_standard: "ISO 9241",
                context_es: "Un sistema médico no se adapta a usuarios con daltonismo.",
                context_en: "A medical system doesn't adapt for color-blind users.",
                question_es: "¿Qué principio de ISO 9241 se incumple?",
                question_en: "Which ISO 9241 principle is violated?",
                options_es: ["Adecuación a la percepción", "Individualización", "Control del usuario", "Autodescriptivo"],
                options_en: ["Suitability for perception", "Individualization", "User control", "Self-descriptiveness"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "La información debe ser perceptible por todos.",
                hint_en: "Information must be perceivable by everyone.",
                friend_answer_es: "Percepción, el color no es accesible para todos.",
                friend_answer_en: "Perception, color isn't accessible for everyone.",
                friend_confidence: "high"
            },
            {
                id: "q9c", level: 9, amount: 16000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Los requisitos del sprint actual contradicen los del sprint anterior.",
                context_en: "Current sprint requirements contradict those from the previous sprint.",
                question_es: "¿Qué principio de ISO 29148 se viola?",
                question_en: "Which ISO 29148 principle is violated?",
                options_es: ["Consistencia", "Completitud", "Atomicidad", "Viabilidad"],
                options_en: ["Consistency", "Completeness", "Atomicity", "Feasibility"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "Los requisitos no deben contradecirse entre sí.",
                hint_en: "Requirements must not contradict each other.",
                friend_answer_es: "Consistencia, no pueden contradecirse.",
                friend_answer_en: "Consistency, they can't contradict.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 10 — $32,000 ════════════════════ */
        10: [
            {
                id: "q10a", level: 10, amount: 32000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "El equipo describe requisitos con pronombres ambiguos como 'ellos'.",
                context_en: "Team describes requirements with ambiguous pronouns like 'they'.",
                question_es: "¿Qué característica se compromete?",
                question_en: "Which characteristic is compromised?",
                options_es: ["Claridad", "Consistencia", "Rastreabilidad", "Viabilidad"],
                options_en: ["Clarity", "Consistency", "Traceability", "Feasibility"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "La redacción debe ser inequívoca.",
                hint_en: "Wording must be unambiguous.",
                friend_answer_es: "Claridad es clave.",
                friend_answer_en: "Clarity is key.",
                friend_confidence: "high"
            },
            {
                id: "q10b", level: 10, amount: 32000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Tras un fallo de red, un sistema de inventario pierde las últimas 50 transacciones.",
                context_en: "After a network failure, an inventory system loses the last 50 transactions.",
                question_es: "¿Qué subcaracterística de calidad se ve afectada?",
                question_en: "Which quality sub-characteristic is affected?",
                options_es: ["Fiabilidad: recuperabilidad", "Seguridad: integridad", "Eficiencia: tiempo de respuesta", "Portabilidad: adaptabilidad"],
                options_en: ["Reliability: recoverability", "Security: integrity", "Efficiency: time behaviour", "Portability: adaptability"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "hard"],
                hint_es: "¿Puede el sistema restaurar datos tras un fallo?",
                hint_en: "Can the system restore data after a failure?",
                friend_answer_es: "Recuperabilidad, se pierden datos.",
                friend_answer_en: "Recoverability, data is lost.",
                friend_confidence: "high"
            },
            {
                id: "q10c", level: 10, amount: 32000, iso_standard: "ISO 9241",
                context_es: "Un sistema de gestión cambia la posición de botones según la pantalla, confundiendo al usuario.",
                context_en: "A management system changes button positions across screens, confusing users.",
                question_es: "¿Qué principio de ISO 9241 se incumple?",
                question_en: "Which ISO 9241 principle is violated?",
                options_es: ["Conformidad con expectativas", "Adecuación a la tarea", "Flexibilidad", "Individualización"],
                options_en: ["Conformity with expectations", "Suitability for the task", "Flexibility", "Individualization"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "hard"],
                hint_es: "El usuario espera consistencia visual.",
                hint_en: "Users expect visual consistency.",
                friend_answer_es: "Conformidad, los botones no deberían moverse.",
                friend_answer_en: "Conformity, buttons shouldn't move around.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 11 — $64,000 ════════════════════ */
        11: [
            {
                id: "q11a", level: 11, amount: 64000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un microservicio se despliega rápido pero su código es difícil de reutilizar.",
                context_en: "A microservice deploys quickly but code is hard to reuse.",
                question_es: "¿Qué característica se ve afectada?",
                question_en: "Which characteristic is affected?",
                options_es: ["Mantenibilidad reutilización", "Rendimiento", "Seguridad autenticación", "Compatibilidad interoperabilidad"],
                options_en: ["Maintainability reusability", "Performance", "Security authentication", "Compatibility interoperability"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "Piensa en replicar componentes.",
                hint_en: "Think about replicating components.",
                friend_answer_es: "Reutilización claramente.",
                friend_answer_en: "Reusability clearly.",
                friend_confidence: "medium"
            },
            {
                id: "q11b", level: 11, amount: 64000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un documento de requisitos no especifica las condiciones de contorno del sistema.",
                context_en: "A requirements document doesn't specify the system's boundary conditions.",
                question_es: "¿Qué atributo de calidad de requisitos falta?",
                question_en: "Which requirement quality attribute is missing?",
                options_es: ["Completitud", "Unicidad", "Trazabilidad", "No ambigüedad"],
                options_en: ["Completeness", "Uniqueness", "Traceability", "Unambiguity"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "Faltan aspectos que deberían estar documentados.",
                hint_en: "Some aspects that should be documented are missing.",
                friend_answer_es: "Completitud, falta información clave.",
                friend_answer_en: "Completeness, key information is missing.",
                friend_confidence: "high"
            },
            {
                id: "q11c", level: 11, amount: 64000, iso_standard: "ISO 9241",
                context_es: "Un sistema ERP requiere formación de 3 semanas para realizar tareas básicas.",
                context_en: "An ERP system requires 3 weeks of training for basic tasks.",
                question_es: "¿Qué principio de ISO 9241 se incumple?",
                question_en: "Which ISO 9241 principle is violated?",
                options_es: ["Adecuación para el aprendizaje", "Autodescriptivo", "Control del usuario", "Tolerancia a errores"],
                options_en: ["Suitability for learning", "Self-descriptiveness", "User control", "Error tolerance"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "hard"],
                hint_es: "El sistema debería ser fácil de aprender.",
                hint_en: "The system should be easy to learn.",
                friend_answer_es: "Adecuación para el aprendizaje.",
                friend_answer_en: "Suitability for learning.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 12 — $125,000 ════════════════════ */
        12: [
            {
                id: "q12a", level: 12, amount: 125000, iso_standard: "ISO 9241",
                context_es: "Una consola industrial bloquea la entrada tras tres errores.",
                context_en: "An industrial console locks input after three mistakes.",
                question_es: "¿Qué principio de usabilidad se afecta?",
                question_en: "Which usability principle is impacted?",
                options_es: ["Control del usuario", "Prevención de errores", "Adecuación al contexto", "Compatibilidad"],
                options_en: ["User control", "Error prevention", "Suitability for context", "Compatibility"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "El usuario debe sentirse al mando.",
                hint_en: "Users should feel in control.",
                friend_answer_es: "Control del usuario, pienso.",
                friend_answer_en: "User control, I think.",
                friend_confidence: "medium"
            },
            {
                id: "q12b", level: 12, amount: 125000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un sistema de e-commerce sufre ataques porque no valida las entradas correctamente.",
                context_en: "An e-commerce system suffers attacks because it doesn't validate inputs properly.",
                question_es: "¿Qué subcaracterística de calidad se compromete?",
                question_en: "Which quality sub-characteristic is compromised?",
                options_es: ["Seguridad: integridad", "Fiabilidad: madurez", "Eficiencia: uso de recursos", "Usabilidad: accesibilidad"],
                options_en: ["Security: integrity", "Reliability: maturity", "Efficiency: resource utilization", "Usability: accessibility"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "hard"],
                hint_es: "Los datos deben estar protegidos contra manipulación.",
                hint_en: "Data must be protected against tampering.",
                friend_answer_es: "Integridad, están manipulando datos.",
                friend_answer_en: "Integrity, data is being tampered with.",
                friend_confidence: "high"
            },
            {
                id: "q12c", level: 12, amount: 125000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un requisito dice: 'El sistema será escalable' sin definir métricas.",
                context_en: "A requirement states: 'The system shall be scalable' without defining metrics.",
                question_es: "¿Qué atributo de calidad falta?",
                question_en: "Which quality attribute is missing?",
                options_es: ["Verificabilidad", "Trazabilidad", "Atomicidad", "Priorización"],
                options_en: ["Verifiability", "Traceability", "Atomicity", "Prioritization"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "medium"],
                hint_es: "¿Cómo puedes comprobar que se cumple?",
                hint_en: "How can you verify it is met?",
                friend_answer_es: "Verificabilidad, sin métricas no se puede probar.",
                friend_answer_en: "Verifiability, without metrics you can't prove it.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 13 — $250,000 ════════════════════ */
        13: [
            {
                id: "q13a", level: 13, amount: 250000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Los requisitos funcionales no describen condiciones de éxito medibles.",
                context_en: "Functional requirements lack measurable success conditions.",
                question_es: "¿Qué atributo de calidad falta?",
                question_en: "Which quality attribute is missing?",
                options_es: ["Testabilidad", "No ambigüedad", "Consistencia", "Modularidad"],
                options_en: ["Testability", "Unambiguity", "Consistency", "Modularity"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "hard"],
                hint_es: "¿Puedes probar que se cumpla?",
                hint_en: "Can you test it is met?",
                friend_answer_es: "Testabilidad, sin duda.",
                friend_answer_en: "Testability, no doubt.",
                friend_confidence: "high"
            },
            {
                id: "q13b", level: 13, amount: 250000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un software monolítico requiere recompilar todo para cambiar una sola función.",
                context_en: "A monolithic software requires rebuilding everything to change a single function.",
                question_es: "¿Qué subcaracterística de calidad se ve afectada?",
                question_en: "Which quality sub-characteristic is affected?",
                options_es: ["Mantenibilidad: modularidad", "Eficiencia: rendimiento", "Seguridad: no repudio", "Portabilidad: reemplazabilidad"],
                options_en: ["Maintainability: modularity", "Efficiency: performance", "Security: non-repudiation", "Portability: replaceability"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "hard", "medium"],
                hint_es: "Los componentes deberían ser independientes.",
                hint_en: "Components should be independent.",
                friend_answer_es: "Modularidad, todo está acoplado.",
                friend_answer_en: "Modularity, everything is coupled.",
                friend_confidence: "high"
            },
            {
                id: "q13c", level: 13, amount: 250000, iso_standard: "ISO 9241",
                context_es: "Un sistema de vuelos muestra precios que cambian entre pantallas sin explicación.",
                context_en: "A flight system shows prices that change between screens without explanation.",
                question_es: "¿Qué principio de ISO 9241 se incumple de forma más grave?",
                question_en: "Which ISO 9241 principle is most severely violated?",
                options_es: ["Conformidad con expectativas", "Tolerancia a errores", "Adecuación a la tarea", "Individualización"],
                options_en: ["Conformity with expectations", "Error tolerance", "Suitability for the task", "Individualization"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "hard"],
                hint_es: "El usuario no espera que los precios cambien sin motivo.",
                hint_en: "Users don't expect prices to change for no reason.",
                friend_answer_es: "Conformidad, los precios deben ser consistentes.",
                friend_answer_en: "Conformity, prices should be consistent.",
                friend_confidence: "high"
            }
        ],

        /* ════════════════════ NIVEL 14 — $500,000 ════════════════════ */
        14: [
            {
                id: "q14a", level: 14, amount: 500000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Una API cumple tiempos pero expone datos sensibles en logs.",
                context_en: "An API meets timing goals but exposes sensitive data in logs.",
                question_es: "¿Qué subcaracterística de calidad se compromete?",
                question_en: "Which quality sub-characteristic is compromised?",
                options_es: ["Seguridad confidencialidad", "Eficiencia temporal", "Protección ante errores", "Compatibilidad"],
                options_en: ["Security confidentiality", "Time efficiency", "Fault protection", "Compatibility"],
                correct_index: 0,
                option_difficulty: ["easy", "medium", "hard", "hard"],
                hint_es: "Los registros no deben filtrar secretos.",
                hint_en: "Logs must not leak secrets.",
                friend_answer_es: "Confidencialidad, clarísimo.",
                friend_answer_en: "Confidentiality, clearly.",
                friend_confidence: "high"
            },
            {
                id: "q14b", level: 14, amount: 500000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un proyecto grande no tiene una matriz de trazabilidad que vincule requisitos con pruebas.",
                context_en: "A large project lacks a traceability matrix linking requirements to tests.",
                question_es: "¿Qué práctica fundamental de ISO 29148 se omite?",
                question_en: "Which fundamental ISO 29148 practice is omitted?",
                options_es: ["Trazabilidad bidireccional", "Priorización de requisitos", "Clasificación lógica", "Consistencia"],
                options_en: ["Bidirectional traceability", "Requirement prioritization", "Logical structuring", "Consistency"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "Cada requisito debe vincularse con su prueba.",
                hint_en: "Each requirement must be linked to its test.",
                friend_answer_es: "Trazabilidad bidireccional, hay que conectar todo.",
                friend_answer_en: "Bidirectional traceability, everything must be connected.",
                friend_confidence: "high"
            },
            {
                id: "q14c", level: 14, amount: 500000, iso_standard: "ISO 9241",
                context_es: "Un sistema SCADA industrial solo funciona de forma correcta si el operador memoriza 40 códigos numéricos.",
                context_en: "An industrial SCADA system only works correctly if the operator memorizes 40 numeric codes.",
                question_es: "¿Qué principio de ISO 9241 se incumple de forma más crítica?",
                question_en: "Which ISO 9241 principle is most critically violated?",
                options_es: ["Adecuación para el aprendizaje", "Flexibilidad", "Detectabilidad", "Conformidad con expectativas"],
                options_en: ["Suitability for learning", "Flexibility", "Findability", "Conformity with expectations"],
                correct_index: 0,
                option_difficulty: ["easy", "hard", "medium", "medium"],
                hint_es: "¿Es razonable pedir que memorice tantos códigos?",
                hint_en: "Is it reasonable to ask someone to memorize so many codes?",
                friend_answer_es: "Aprendizaje, nadie puede memorizar tanto.",
                friend_answer_en: "Learning, nobody can memorize that much.",
                friend_confidence: "medium"
            }
        ],

        /* ════════════════════ NIVEL 15 — $1,000,000 ════════════════════ */
        15: [
            {
                id: "q15a", level: 15, amount: 1000000, iso_standard: "ISO 9241",
                context_es: "Un ERP crítico obliga a usar combinaciones de teclas no documentadas.",
                context_en: "A critical ERP forces undocumented key combinations.",
                question_es: "¿Qué principio es el más grave?",
                question_en: "Which principle is most severely violated?",
                options_es: ["Conformidad con expectativas", "Flexibilidad", "Autodescriptivo", "Adecuación para aprendizaje"],
                options_en: ["Conformity with expectations", "Flexibility", "Self-descriptiveness", "Suitability for learning"],
                correct_index: 0,
                option_difficulty: ["medium", "hard", "medium", "hard"],
                hint_es: "Los usuarios esperan patrones conocidos.",
                hint_en: "Users expect familiar patterns.",
                friend_answer_es: "Conformidad, porque rompen patrones.",
                friend_answer_en: "Conformity, since patterns break.",
                friend_confidence: "medium"
            },
            {
                id: "q15b", level: 15, amount: 1000000, iso_standard: "ISO/IEC 25010:2023",
                context_es: "Un sistema bancario central no puede migrar a nueva infraestructura cloud porque las dependencias están codificadas a nivel de hardware.",
                context_en: "A core banking system cannot migrate to new cloud infrastructure because dependencies are hardcoded at the hardware level.",
                question_es: "Según ISO 25010, ¿qué subcaracterísticas se comprometen simultáneamente?",
                question_en: "According to ISO 25010, which sub-characteristics are simultaneously compromised?",
                options_es: ["Portabilidad: adaptabilidad e instalabilidad", "Seguridad: confidencialidad e integridad", "Eficiencia: tiempo y recursos", "Usabilidad: accesibilidad y operabilidad"],
                options_en: ["Portability: adaptability and installability", "Security: confidentiality and integrity", "Efficiency: time and resources", "Usability: accessibility and operability"],
                correct_index: 0,
                option_difficulty: ["medium", "hard", "medium", "hard"],
                hint_es: "El software está atado a un entorno específico.",
                hint_en: "The software is tied to a specific environment.",
                friend_answer_es: "Portabilidad, está anclado al hardware.",
                friend_answer_en: "Portability, it's anchored to hardware.",
                friend_confidence: "medium"
            },
            {
                id: "q15c", level: 15, amount: 1000000, iso_standard: "ISO/IEC/IEEE 29148",
                context_es: "Un contrato de software define los requisitos con frases como 'el sistema debe ser rápido, seguro y fácil de usar' sin definiciones operacionales.",
                context_en: "A software contract defines requirements with phrases like 'the system must be fast, secure, and easy to use' without operational definitions.",
                question_es: "¿Qué múltiples atributos de calidad de requisitos se incumplen según ISO 29148?",
                question_en: "Which multiple requirement quality attributes are violated according to ISO 29148?",
                options_es: ["Verificabilidad, no ambigüedad y atomicidad", "Trazabilidad, consistencia y completitud", "Priorización, unicidad y viabilidad", "Clasificación lógica, completitud y consistencia"],
                options_en: ["Verifiability, unambiguity, and atomicity", "Traceability, consistency, and completeness", "Prioritization, uniqueness, and feasibility", "Logical structuring, completeness, and consistency"],
                correct_index: 0,
                option_difficulty: ["medium", "hard", "hard", "hard"],
                hint_es: "Cada término vago viola varios atributos a la vez.",
                hint_en: "Each vague term violates several attributes at once.",
                friend_answer_es: "Verificabilidad, no ambigüedad y atomicidad, mezcla tres cosas vagas.",
                friend_answer_en: "Verifiability, unambiguity, and atomicity — it mixes three vague things.",
                friend_confidence: "medium"
            }
        ]
    }
};

/**
 * Builds a random game by picking one question per level.
 * Returns an object with the same shape as the old FALLBACK_GAME.
 */
export function buildRandomFallbackGame() {
    const questions = [];
    for (let level = 1; level <= 15; level++) {
        const bucket = FALLBACK_POOL.pool[level];
        const pick = bucket[Math.floor(Math.random() * bucket.length)];
        questions.push(pick);
    }
    return {
        game_title_es: FALLBACK_POOL.game_title_es,
        game_title_en: FALLBACK_POOL.game_title_en,
        iso_focus: FALLBACK_POOL.iso_focus,
        questions,
    };
}
