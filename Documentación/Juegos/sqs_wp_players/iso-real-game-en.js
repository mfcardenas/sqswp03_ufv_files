// === ISO LABORATORY - REAL TECHNICAL DECISIONS GAME ===

class ISOGameEngine {
    constructor() {
        this.gameState = {
            currentProject: null,
            metrics: {
                // ISO 25010 - Quality Characteristics
                functionalSuitability: 0,    // Functional Suitability
                performanceEfficiency: 0,    // Performance Efficiency  
                compatibility: 0,            // Compatibility
                usability: 0,                // Usability
                reliability: 0,              // Reliability
                security: 0,                 // Security
                maintainability: 0,          // Maintainability
                portability: 0               // Portability
            },
            resources: {
                budget: 100000,
                time: 12,                     // months
                developmentTeam: 5,
                testingTeam: 2,
                teamExperience: 'intermediate'
            },
            decisions: [],
            phase: 'planning',           // planning, development, testing, deployment
            score: 0,
            penalties: []
        };

        this.projects = {
            ecommerce: {
                name: "E-commerce Platform",
                description: "E-commerce system that must handle 10,000 concurrent users",
                minimumObjectives: {
                    functionalSuitability: 85,
                    performanceEfficiency: 80,
                    usability: 90,
                    security: 95,
                    reliability: 85
                },
                constraints: {
                    maxBudget: 150000,
                    maxTime: 18,
                    pciCompliance: true,
                    availability: 99.9
                },
                riesgos: ['traffic_spikes', 'security_attacks', 'payment_integration', 'user_experience']
            },
            hospital: {
                name: "Hospital Management System",
                description: "Critical medical software for patient and medical record management",
                minimumObjectives: {
                    functionalSuitability: 95,
                    reliability: 98,
                    security: 99,
                    usability: 85,
                    maintainability: 90
                },
                constraints: {
                    maxBudget: 200000,
                    maxTime: 24,
                    fdaCertification: true,
                    availability: 99.99,
                    hipaaCompliance: true
                },
                riesgos: ['critical_failures', 'data_loss', 'unauthorized_access', 'interoperability']
            },
            fintech: {
                name: "Financial Platform",
                description: "Banking system with real-time transactions and regulatory compliance",
                minimumObjectives: {
                    security: 98,
                    reliability: 95,
                    performanceEfficiency: 90,
                    functionalSuitability: 90,
                    compatibility: 85
                },
                constraints: {
                    maxBudget: 300000,
                    maxTime: 30,
                    soxCompliance: true,
                    availability: 99.99,
                    continuousAuditing: true
                },
                riesgos: ['regulatory_changes', 'fraud_attempts', 'system_downtime', 'data_breaches']
            },
            social: {
                name: "Social Network Platform",
                description: "Social media platform with multimedia content and real-time messaging",
                minimumObjectives: {
                    usability: 95,
                    performanceEfficiency: 85,
                    compatibility: 90,
                    functionalSuitability: 85,
                    portability: 80
                },
                constraints: {
                    maxBudget: 180000,
                    maxTime: 20,
                    globalScalability: true,
                    availability: 99.9
                },
                risks: ['viral_growth', 'content_moderation', 'performance_bottlenecks', 'privacy_concerns']
            }
        };

        this.decisions = {
            architecture: {
                monolithic: {
                    impact: { maintainability: -20, performanceEfficiency: +10, functionalSuitability: +5 },
                    cost: 0,
                    time: 0,
                    description: "Traditional monolithic architecture - simpler but less scalable"
                },
                microservices: {
                    impact: { maintainability: +15, performanceEfficiency: -5, compatibility: +20, functionalSuitability: +10 },
                    cost: 15000,
                    time: 3,
                    description: "Microservices - higher complexity but better scalability and maintenance"
                },
                serverless: {
                    impact: { performanceEfficiency: +25, portability: +15, maintainability: +10, functionalSuitability: +5 },
                    cost: -5000,
                    time: 1,
                    description: "Serverless architecture - high efficiency but vendor lock-in"
                }
            },
            database: {
                sql_traditional: {
                    impact: { reliability: +20, functionalSuitability: +10, compatibility: +15 },
                    cost: 5000,
                    time: 1,
                    description: "Traditional SQL database - full ACID compliance, well-known"
                },
                nosql_scalable: {
                    impact: { performanceEfficiency: +25, portability: +10, functionalSuitability: +5 },
                    cost: 8000,
                    time: 2,
                    description: "NoSQL for high scalability - eventual consistency"
                },
                hybrid: {
                    impact: { functionalSuitability: +20, performanceEfficiency: +10, maintainability: -10 },
                    cost: 12000,
                    time: 3,
                    description: "Hybrid SQL+NoSQL approach - maximum flexibility, higher complexity"
                }
            },
            testing: {
                manual_basic: {
                    impact: { reliability: +5, functionalSuitability: +5 },
                    cost: 2000,
                    time: 1,
                    description: "Basic manual testing - economical but limited"
                },
                automated_complete: {
                    impact: { reliability: +30, functionalSuitability: +20, maintainability: +15 },
                    cost: 25000,
                    time: 4,
                    description: "Complete automated testing suite - maximum quality"
                },
                automated_critical: {
                    impact: { reliability: +20, functionalSuitability: +15, security: +10 },
                    cost: 15000,
                    time: 2,
                    description: "Automated testing on critical functions - cost-benefit balance"
                }
            },
            security: {
                basic: {
                    impact: { security: +10 },
                    cost: 3000,
                    time: 1,
                    description: "Basic security measures - minimum acceptable"
                },
                advanced: {
                    impact: { security: +30, reliability: +10, functionalSuitability: -5 },
                    cost: 20000,
                    time: 3,
                    description: "Advanced multi-layer security - very robust"
                },
                extreme: {
                    impact: { security: +50, reliability: +20, usability: -15, performanceEfficiency: -10 },
                    cost: 35000,
                    time: 5,
                    description: "Military-grade security - maximum protection, UX impact"
                }
            },
            ui_ux: {
                functional_basic: {
                    impact: { usability: +10, functionalSuitability: +5 },
                    cost: 5000,
                    time: 2,
                    description: "Basic functional interface - meets minimum requirements"
                },
                professional_design: {
                    impact: { usability: +25, functionalSuitability: +10, performanceEfficiency: +5 },
                    cost: 15000,
                    time: 4,
                    description: "Professional UX design - optimized experience"
                },
                innovador_accesible: {
                    impacto: { usabilidad: +40, funcionalidad: +15, compatibilidad: +20 },
                    costo: 25000,
                    tiempo: 6,
                    descripcion: "Innovative design with full accessibility - inclusive and modern"
                }
            }
        };

        this.eventosAleatorios = [
            {
                nombre: "Requirements Change",
                probabilidad: 0.3,
                impacto: { funcionalidad: -10, tiempo: +2, costo: +5000 },
                descripcion: "Client changes important requirements mid-project"
            },
            {
                nombre: "Security Vulnerability Discovered",
                probabilidad: 0.2,
                impacto: { seguridad: -15, tiempo: +1, costo: +3000 },
                descripcion: "A critical vulnerability is discovered and must be fixed"
            },
            {
                nombre: "Senior Developer Leaves",
                probabilidad: 0.15,
                impacto: { mantenibilidad: -10, tiempo: +3, costo: +8000 },
                descripcion: "A key developer leaves the project"
            },
            {
                nombre: "New Regulation",
                probabilidad: 0.25,
                impacto: { funcionalidad: -5, seguridad: +10, tiempo: +2, costo: +6000 },
                descripcion: "New regulation requires changes to the system"
            }
        ];
    }

    iniciarProyecto(tipoProyecto) {
        this.gameState.currentProject = this.proyectos[tipoProyecto];
        this.gameState.fase = 'planning';
        this.resetearMetricas();
        this.renderizarInterfazJuego();
    }

    resetearMetricas() {
        Object.keys(this.gameState.metrics).forEach(key => {
            this.gameState.metrics[key] = 0;
        });
    }

    tomarDecision(categoria, opcion) {
        const decision = this.decisiones[categoria][opcion];
        
        // Apply impacts to metrics
        Object.keys(decision.impacto).forEach(metrica => {
            if (metrica === 'tiempo' || metrica === 'costo') {
                this.gameState.recursos[metrica === 'tiempo' ? 'tiempo' : 'presupuesto'] += decision.impacto[metrica];
            } else {
                this.gameState.metrics[metrica] += decision.impacto[metrica];
                // Ensure metrics are between 0 and 100
                this.gameState.metrics[metrica] = Math.max(0, Math.min(100, this.gameState.metrics[metrica]));
            }
        });

        // Register the decision
        this.gameState.decisiones.push({
            fase: this.gameState.fase,
            categoria: categoria,
            opcion: opcion,
            decision: decision
        });

        // Calculate score based on decision effectiveness
        this.calcularPuntuacion();

        // Possible random event
        this.procesarEventoAleatorio();

        // Update interface
        this.actualizarInterfaz();
    }

    calcularPuntuacion() {
        const proyecto = this.gameState.currentProject;
        let puntosTotales = 0;
        
        Object.keys(proyecto.objetivosMinimos).forEach(metrica => {
            const objetivo = proyecto.objetivosMinimos[metrica];
            const actual = this.gameState.metrics[metrica];
            
            if (actual >= objetivo) {
                puntosTotales += (actual - objetivo) * 2 + objetivo;
            } else {
                puntosTotales += actual * 0.5; // Penalty for not meeting objective
            }
        });

        // Bonus for resource efficiency
        if (this.gameState.recursos.presupuesto > 0) {
            puntosTotales += this.gameState.recursos.presupuesto * 0.01;
        }
        
        if (this.gameState.recursos.tiempo > 0) {
            puntosTotales += this.gameState.recursos.tiempo * 10;
        }

        this.gameState.puntuacion = Math.round(puntosTotales);
    }

    procesarEventoAleatorio() {
        const evento = this.eventosAleatorios.find(e => Math.random() < e.probabilidad);
        if (evento) {
            // Apply event impact
            Object.keys(evento.impacto).forEach(key => {
                if (key === 'tiempo' || key === 'costo') {
                    const recurso = key === 'tiempo' ? 'tiempo' : 'presupuesto';
                    this.gameState.recursos[recurso] += evento.impacto[key];
                } else {
                    this.gameState.metrics[key] += evento.impacto[key];
                    this.gameState.metrics[key] = Math.max(0, Math.min(100, this.gameState.metrics[key]));
                }
            });

            this.mostrarEventoAleatorio(evento);
        }
    }

    renderizarInterfazJuego() {
        const gameInterface = document.getElementById('game-interface');
        if (!gameInterface) return;

        gameInterface.innerHTML = `
            <div class="project-header">
                <h1>🎯 ${this.gameState.currentProject.nombre}</h1>
                <p>${this.gameState.currentProject.descripcion}</p>
                <div class="project-phase">Phase: <span class="phase-name">${this.gameState.fase}</span></div>
            </div>

            <div class="game-dashboard">
                <div class="metrics-panel">
                    <h2>📊 ISO 25010 Metrics</h2>
                    <div class="metrics-grid">
                        ${this.renderizarMetricas()}
                    </div>
                </div>

                <div class="resources-panel">
                    <h2>💰 Available Resources</h2>
                    <div class="resources-grid">
                        <div class="resource-item ${this.gameState.recursos.presupuesto < 0 ? 'negative' : ''}">
                            <span class="resource-icon">💵</span>
                            <span class="resource-label">Budget</span>
                            <span class="resource-value">$${this.gameState.recursos.presupuesto.toLocaleString()}</span>
                        </div>
                        <div class="resource-item ${this.gameState.recursos.tiempo < 0 ? 'negative' : ''}">
                            <span class="resource-icon">⏱️</span>
                            <span class="resource-label">Time</span>
                            <span class="resource-value">${this.gameState.recursos.tiempo} months</span>
                        </div>
                        <div class="resource-item">
                            <span class="resource-icon">🎯</span>
                            <span class="resource-label">Score</span>
                            <span class="resource-value">${this.gameState.puntuacion}</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="decisions-panel">
                <h2>🤔 Technical Decisions</h2>
                <div class="decisions-grid">
                    ${this.renderizarDecisiones()}
                </div>
            </div>

            <div class="objectives-panel">
                <h2>🎯 Project Objectives</h2>
                <div class="objectives-grid">
                    ${this.renderizarObjetivos()}
                </div>
            </div>
        `;
    }

    renderizarMetricas() {
        return Object.keys(this.gameState.metrics).map(metrica => {
            const valor = this.gameState.metrics[metrica];
            const objetivo = this.gameState.currentProject.objetivosMinimos[metrica] || 50;
            const cumple = valor >= objetivo;
            
            return `
                <div class="metric-card ${cumple ? 'success' : 'pending'}">
                    <div class="metric-name">${this.getNombreMetrica(metrica)}</div>
                    <div class="metric-bar">
                        <div class="metric-fill" style="width: ${valor}%"></div>
                        <div class="metric-target" style="left: ${objetivo}%"></div>
                    </div>
                    <div class="metric-value">${valor}/100 (min: ${objetivo})</div>
                </div>
            `;
        }).join('');
    }

    renderizarDecisiones() {
        return Object.keys(this.decisiones).map(categoria => `
            <div class="decision-category">
                <h3>${this.getNombreCategoria(categoria)}</h3>
                <div class="decision-options">
                    ${Object.keys(this.decisiones[categoria]).map(opcion => {
                        const decision = this.decisiones[categoria][opcion];
                        const yaElegida = this.gameState.decisiones.find(d => d.categoria === categoria);
                        
                        return `
                            <div class="decision-option ${yaElegida?.opcion === opcion ? 'selected' : ''}" 
                                 onclick="isoGame.tomarDecision('${categoria}', '${opcion}')"
                                 ${yaElegida ? 'style="pointer-events: none; opacity: 0.6;"' : ''}>
                                <div class="option-header">
                                    <h4>${this.getNombreOpcion(opcion)}</h4>
                                    <div class="option-cost">
                                        💰 ${decision.costo >= 0 ? '+' : ''}$${decision.costo.toLocaleString()} | 
                                        ⏱️ ${decision.tiempo >= 0 ? '+' : ''}${decision.tiempo}m
                                    </div>
                                </div>
                                <p class="option-description">${decision.descripcion}</p>
                                <div class="option-impact">
                                    <strong>Impact:</strong>
                                    ${Object.keys(decision.impacto).map(metrica => 
                                        `<span class="impact-item ${decision.impacto[metrica] >= 0 ? 'positive' : 'negative'}">
                                            ${this.getNombreMetrica(metrica)}: ${decision.impacto[metrica] >= 0 ? '+' : ''}${decision.impacto[metrica]}
                                        </span>`
                                    ).join(' ')}
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `).join('');
    }

    renderizarObjetivos() {
        return Object.keys(this.gameState.currentProject.objetivosMinimos).map(metrica => {
            const objetivo = this.gameState.currentProject.objetivosMinimos[metrica];
            const actual = this.gameState.metrics[metrica];
            const progreso = Math.min(100, (actual / objetivo) * 100);
            const cumplido = actual >= objetivo;
            
            return `
                <div class="objective-card ${cumplido ? 'completed' : 'pending'}">
                    <div class="objective-name">${this.getNombreMetrica(metrica)}</div>
                    <div class="objective-progress">
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: ${progreso}%"></div>
                        </div>
                        <span class="progress-text">${actual}/${objetivo} ${cumplido ? '✅' : '⏳'}</span>
                    </div>
                </div>
            `;
        }).join('');
    }

    getNombreMetrica(metrica) {
        const nombres = {
            funcionalidad: 'Functionality',
            eficiencia: 'Efficiency',
            compatibilidad: 'Compatibility',
            usabilidad: 'Usability',
            confiabilidad: 'Reliability',
            seguridad: 'Security',
            mantenibilidad: 'Maintainability',
            portabilidad: 'Portability',
            tiempo: 'Time',
            costo: 'Cost'
        };
        return nombres[metrica] || metrica;
    }

    getNombreCategoria(categoria) {
        const nombres = {
            arquitectura: '🏗️ System Architecture',
            baseDatos: '🗄️ Database Strategy',
            testing: '🧪 Testing Strategy',
            seguridad: '🔒 Security Level',
            ui_ux: '🎨 UI/UX Design'
        };
        return nombres[categoria] || categoria;
    }

    getNombreOpcion(opcion) {
        const nombres = {
            monolitica: 'Monolithic',
            microservicios: 'Microservices',
            serverless: 'Serverless',
            sql_tradicional: 'Traditional SQL',
            nosql_escalable: 'Scalable NoSQL',
            hibrida: 'Hybrid SQL+NoSQL',
            manual_basico: 'Basic Manual',
            automatizado_completo: 'Complete Automated',
            automatizado_critico: 'Critical Automated',
            basica: 'Basic',
            avanzada: 'Advanced',
            extrema: 'Extreme',
            funcional_basico: 'Basic Functional',
            diseño_profesional: 'Professional',
            innovador_accesible: 'Innovative + Accessible'
        };
        return nombres[opcion] || opcion;
    }

    mostrarEventoAleatorio(evento) {
        const notification = document.createElement('div');
        notification.className = 'event-notification';
        notification.innerHTML = `
            <div class="notification-content">
                <h3>⚠️ ${evento.nombre}</h3>
                <p>${evento.descripcion}</p>
                <div class="event-impacts">
                    <strong>Impact:</strong>
                    ${Object.keys(evento.impacto).map(key => 
                        `<span>${this.getNombreMetrica(key)}: ${evento.impacto[key] >= 0 ? '+' : ''}${evento.impacto[key]}</span>`
                    ).join(', ')}
                </div>
                <button onclick="this.parentElement.parentElement.remove()">Understood</button>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, 10000);
    }

    actualizarInterfaz() {
        // Update metrics in real-time
        const metricsGrid = document.querySelector('.metrics-grid');
        if (metricsGrid) {
            metricsGrid.innerHTML = this.renderizarMetricas();
        }

        // Update resources
        const resourcesGrid = document.querySelector('.resources-grid');
        if (resourcesGrid) {
            resourcesGrid.innerHTML = `
                <div class="resource-item ${this.gameState.recursos.presupuesto < 0 ? 'negative' : ''}">
                    <span class="resource-icon">💵</span>
                    <span class="resource-label">Budget</span>
                    <span class="resource-value">$${this.gameState.recursos.presupuesto.toLocaleString()}</span>
                </div>
                <div class="resource-item ${this.gameState.recursos.tiempo < 0 ? 'negative' : ''}">
                    <span class="resource-icon">⏱️</span>
                    <span class="resource-label">Time</span>
                    <span class="resource-value">${this.gameState.recursos.tiempo} months</span>
                </div>
                <div class="resource-item">
                    <span class="resource-icon">🎯</span>
                    <span class="resource-label">Score</span>
                    <span class="resource-value">${this.gameState.puntuacion}</span>
                </div>
            `;
        }

        // Update objectives
        const objectivesGrid = document.querySelector('.objectives-grid');
        if (objectivesGrid) {
            objectivesGrid.innerHTML = this.renderizarObjetivos();
        }

        // Check if project is complete
        this.verificarCompletacion();
    }

    verificarCompletacion() {
        const todasLasDecisiones = Object.keys(this.decisiones).every(categoria =>
            this.gameState.decisiones.find(d => d.categoria === categoria)
        );

        if (todasLasDecisiones) {
            this.mostrarResultadoFinal();
        }
    }

    mostrarResultadoFinal() {
        const proyecto = this.gameState.currentProject;
        const objetivosCumplidos = Object.keys(proyecto.objetivosMinimos).filter(metrica =>
            this.gameState.metrics[metrica] >= proyecto.objetivosMinimos[metrica]
        );

        const porcentajeExito = (objetivosCumplidos.length / Object.keys(proyecto.objetivosMinimos).length) * 100;
        
        let evaluacion = '';
        if (porcentajeExito >= 90) {
            evaluacion = '🏆 EXCEPTIONAL SUCCESS! You have mastered ISO standards.';
        } else if (porcentajeExito >= 70) {
            evaluacion = '✅ SUCCESS! The project meets main objectives.';
        } else if (porcentajeExito >= 50) {
            evaluacion = '⚠️ PARTIAL SUCCESS. The project works but needs improvements.';
        } else {
            evaluacion = '❌ PROJECT FAILED. Minimum objectives not met.';
        }

        const modal = document.createElement('div');
        modal.className = 'game-completion-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <h1>🎯 Project Completed</h1>
                <h2>${evaluacion}</h2>
                
                <div class="final-metrics">
                    <h3>📊 Final Results</h3>
                    ${Object.keys(proyecto.objetivosMinimos).map(metrica => {
                        const objetivo = proyecto.objetivosMinimos[metrica];
                        const actual = this.gameState.metrics[metrica];
                        const cumple = actual >= objetivo;
                        
                        return `
                            <div class="final-metric ${cumple ? 'success' : 'fail'}">
                                <span class="metric-name">${this.getNombreMetrica(metrica)}</span>
                                <span class="metric-result">${actual}/100 (target: ${objetivo}) ${cumple ? '✅' : '❌'}</span>
                            </div>
                        `;
                    }).join('')}
                </div>
                
                <div class="final-score">
                    <h3>🎯 Final Score: ${this.gameState.puntuacion}</h3>
                    <p>Remaining resources: $${this.gameState.recursos.presupuesto.toLocaleString()}, ${this.gameState.recursos.tiempo} months</p>
                </div>
                
                <div class="decision-summary">
                    <h3>📋 Decisions Made</h3>
                    ${this.gameState.decisiones.map(d => `
                        <div class="decision-summary-item">
                            <strong>${this.getNombreCategoria(d.categoria)}:</strong> 
                            ${this.getNombreOpcion(d.opcion)}
                        </div>
                    `).join('')}
                </div>
                
                <div class="modal-actions">
                    <button onclick="this.parentElement.parentElement.remove(); isoGame.volverAlMenu()">🏠 New Project</button>
                    <button onclick="this.parentElement.parentElement.remove(); isoGame.reiniciarProyecto()">🔄 Repeat Project</button>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
    }

    volverAlMenu() {
        const gameInterface = document.getElementById('game-interface');
        if (gameInterface) {
            gameInterface.innerHTML = this.createProjectMenu();
        }
    }

    reiniciarProyecto() {
        const tipoActual = Object.keys(this.proyectos).find(tipo => 
            this.proyectos[tipo] === this.gameState.currentProject
        );
        this.iniciarProyecto(tipoActual);
    }

    createProjectMenu() {
        return `
            <div class="project-selection">
                <h1>🎯 ISO Laboratory - Project Simulator</h1>
                <p>Select a project and make technical decisions that impact real ISO 25010 metrics</p>
                
                <div class="projects-grid">
                    ${Object.keys(this.proyectos).map(tipo => {
                        const proyecto = this.proyectos[tipo];
                        return `
                            <div class="project-card" onclick="isoGame.iniciarProyecto('${tipo}')">
                                <h3>${proyecto.nombre}</h3>
                                <p>${proyecto.descripcion}</p>
                                
                                <div class="project-objectives">
                                    <h4>Main Objectives:</h4>
                                    ${Object.keys(proyecto.objetivosMinimos).map(metrica => 
                                        `<span class="objective-tag">${this.getNombreMetrica(metrica)}: ${proyecto.objetivosMinimos[metrica]}%</span>`
                                    ).join('')}
                                </div>
                                
                                <div class="project-constraints">
                                    <div class="constraint">💰 Max: $${proyecto.restricciones.presupuestoMaximo.toLocaleString()}</div>
                                    <div class="constraint">⏱️ Max: ${proyecto.restricciones.tiempoMaximo} months</div>
                                </div>
                                
                                <button class="start-project-btn">Start Project</button>
                            </div>
                        `;
                    }).join('')}
                </div>
                
                <div class="game-explanation">
                    <h2>🎮 How to Play</h2>
                    <ol>
                        <li><strong>Choose a project</strong> - Each has specific ISO objectives</li>
                        <li><strong>Make technical decisions</strong> - Architecture, DB, Testing, Security, UI/UX</li>
                        <li><strong>Manage resources</strong> - Limited budget and time</li>
                        <li><strong>Face random events</strong> - Just like in real projects</li>
                        <li><strong>Meet ISO objectives</strong> - Software quality metrics</li>
                    </ol>
                    
                    <div class="iso-standards-info">
                        <h3>📚 Applied ISO Standards</h3>
                        <div class="standards-grid">
                            <div class="standard-info">
                                <strong>ISO 25010</strong>
                                <p>Software product quality model with 8 measurable characteristics</p>
                            </div>
                            <div class="standard-info">
                                <strong>ISO 29148</strong>
                                <p>Requirements engineering processes</p>
                            </div>
                            <div class="standard-info">
                                <strong>ISO 9241</strong>
                                <p>Ergonomics and human-system interaction</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
}

// Global game instance
window.isoGame = new ISOGameEngine();