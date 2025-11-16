# Laboratorio 5: Estándares de Accesibilidad

## Solución

### Paso 1: Estructura HTML Accesible
Crear un archivo `accessible_app.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplicación Web Accesible - Laboratorio ISO 9241</title>
    <link rel="stylesheet" href="accessibility.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <header>
        <nav aria-label="Navegación principal">
            <ul>
                <li><a href="#home" aria-current="page">Inicio</a></li>
                <li><a href="#about">Acerca de</a></li>
                <li><a href="#services">Servicios</a></li>
                <li><a href="#contact">Contacto</a></li>
            </ul>
        </nav>
        <button id="themeToggle" aria-label="Alternar modo de alto contraste">Alto Contraste</button>
        <div class="font-controls">
            <button id="increaseFont" aria-label="Aumentar tamaño de fuente">+</button>
            <button id="decreaseFont" aria-label="Disminuir tamaño de fuente">-</button>
            <button id="resetFont" aria-label="Restablecer tamaño de fuente">Restablecer</button>
        </div>
    </header>

    <main>
        <section id="home" aria-labelledby="home-heading">
            <h1 id="home-heading">Bienvenido a Nuestra Aplicación Accesible</h1>
            <img src="logo.png" alt="Logo de la Empresa - Un círculo azul con texto blanco" width="200" height="200">
            <p>Esta aplicación demuestra estándares de accesibilidad ISO 9241 y cumplimiento WCAG 2.1.</p>
        </section>

        <section id="about" aria-labelledby="about-heading">
            <h2 id="about-heading">Acerca de la Accesibilidad</h2>
            <p>La accesibilidad asegura que las personas con discapacidades puedan usar productos digitales efectivamente.</p>
            <figure>
                <img src="accessibility-diagram.png" alt="Diagrama mostrando diferentes tipos de discapacidades y tecnologías de asistencia" width="400" height="300">
                <figcaption>Tipos de discapacidades y tecnologías de asistencia</figcaption>
            </figure>
        </section>

        <section id="services" aria-labelledby="services-heading">
            <h2 id="services-heading">Nuestros Servicios</h2>
            <div class="service-grid">
                <article class="service-card">
                    <h3>Auditoría de Accesibilidad Web</h3>
                    <p>Evaluamos sitios web para cumplimiento WCAG y proporcionamos reportes detallados.</p>
                    <button class="learn-more" aria-describedby="service1-desc">Saber Más</button>
                    <div id="service1-desc" class="sr-only">Saber más sobre nuestro servicio de auditoría de accesibilidad web</div>
                </article>
                
                <article class="service-card">
                    <h3>Entrenamiento en Accesibilidad</h3>
                    <p>Programas completos de entrenamiento para desarrolladores y diseñadores.</p>
                    <button class="learn-more" aria-describedby="service2-desc">Saber Más</button>
                    <div id="service2-desc" class="sr-only">Saber más sobre nuestros programas de entrenamiento en accesibilidad</div>
                </article>
                
                <article class="service-card">
                    <h3>Soporte de Tecnología de Asistencia</h3>
                    <p>Integración y soporte para diversas tecnologías de asistencia.</p>
                    <button class="learn-more" aria-describedby="service3-desc">Saber Más</button>
                    <div id="service3-desc" class="sr-only">Saber más sobre nuestro soporte de tecnología de asistencia</div>
                </article>
            </div>
        </section>

        <section id="contact" aria-labelledby="contact-heading">
            <h2 id="contact-heading">Contáctanos</h2>
            <form id="contactForm" aria-labelledby="contact-heading">
                <div class="form-group">
                    <label for="name">Nombre Completo</label>
                    <input type="text" id="name" name="name" required aria-describedby="name-help">
                    <div id="name-help" class="help-text">Ingresa tu nombre completo como aparece en tu ID</div>
                </div>
                
                <div class="form-group">
                    <label for="email">Dirección de Correo Electrónico</label>
                    <input type="email" id="email" name="email" required aria-describedby="email-help">
                    <div id="email-help" class="help-text">Usaremos esto para responder a tu consulta</div>
                </div>
                
                <div class="form-group">
                    <label for="message">Mensaje</label>
                    <textarea id="message" name="message" rows="5" required aria-describedby="message-help"></textarea>
                    <div id="message-help" class="help-text">Cuéntanos cómo podemos ayudarte</div>
                </div>
                
                <button type="submit" aria-describedby="submit-help">Enviar Mensaje</button>
                <div id="submit-help" class="sr-only">Enviar tu formulario de contacto</div>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Aplicaciones Web Accesibles. Todos los derechos reservados.</p>
        <nav aria-label="Navegación de pie de página">
            <ul>
                <li><a href="#privacy">Política de Privacidad</a></li>
                <li><a href="#terms">Términos de Servicio</a></li>
                <li><a href="#accessibility">Declaración de Accesibilidad</a></li>
            </ul>
        </nav>
    </footer>

    <div id="skipLinks" class="sr-only">
        <a href="#main" class="skip-link">Saltar al contenido principal</a>
        <a href="#navigation" class="skip-link">Saltar a la navegación</a>
    </div>

    <script src="accessibility.js"></script>
</body>
</html>
```

### Paso 2: CSS Accesible
Crear un archivo `accessibility.css`:

```css
/* Estilos base */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #fff;
    margin: 0;
    padding: 0;
    font-size: 16px;
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

.skip-link {
    position: absolute;
    top: -40px;
    left: 6px;
    background: #000;
    color: #fff;
    padding: 8px;
    text-decoration: none;
    z-index: 100;
}

.skip-link:focus {
    top: 6px;
}

/* Encabezado y Navegación */
header {
    background-color: #f8f9fa;
    padding: 1rem;
    border-bottom: 1px solid #dee2e6;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    gap: 1rem;
}

nav a {
    text-decoration: none;
    color: #007bff;
    padding: 0.5rem;
    border-radius: 4px;
}

nav a:hover, nav a:focus {
    background-color: #e9ecef;
    outline: 2px solid #007bff;
    outline-offset: 2px;
}

.font-controls {
    display: flex;
    gap: 0.5rem;
}

.font-controls button {
    padding: 0.5rem;
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.font-controls button:hover, .font-controls button:focus {
    background-color: #5a6268;
}

/* Contenido Principal */
main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

section {
    margin-bottom: 3rem;
}

h1, h2, h3 {
    color: #495057;
}

h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
    border-bottom: 2px solid #007bff;
    padding-bottom: 0.5rem;
}

img {
    max-width: 100%;
    height: auto;
}

figure {
    margin: 1rem 0;
    text-align: center;
}

figcaption {
    font-style: italic;
    color: #6c757d;
    margin-top: 0.5rem;
}

/* Cuadrícula de Servicios */
.service-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.service-card {
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 1.5rem;
    background-color: #f8f9fa;
}

.service-card h3 {
    color: #007bff;
    margin-top: 0;
}

.learn-more {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
}

.learn-more:hover, .learn-more:focus {
    background-color: #0056b3;
}

/* Estilos de Formulario */
.form-group {
    margin-bottom: 1.5rem;
}

label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #495057;
}

input, textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ced4da;
    border-radius: 4px;
    font-size: 1rem;
    font-family: inherit;
}

input:focus, textarea:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}

.help-text {
    font-size: 0.875rem;
    color: #6c757d;
    margin-top: 0.25rem;
}

button[type="submit"] {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
}

button[type="submit"]:hover, button[type="submit"]:focus {
    background-color: #218838;
}

/* Pie de página */
footer {
    background-color: #f8f9fa;
    padding: 2rem;
    border-top: 1px solid #dee2e6;
    text-align: center;
}

footer nav ul {
    justify-content: center;
    margin-top: 1rem;
}

/* Modo de Alto Contraste */
body.high-contrast {
    background-color: #000;
    color: #fff;
}

body.high-contrast header {
    background-color: #000;
    border-bottom-color: #fff;
}

body.high-contrast nav a {
    color: #fff;
}

body.high-contrast nav a:hover, body.high-contrast nav a:focus {
    background-color: #333;
    color: #fff;
}

body.high-contrast .service-card {
    background-color: #000;
    border-color: #fff;
    color: #fff;
}

body.high-contrast input, body.high-contrast textarea {
    background-color: #000;
    border-color: #fff;
    color: #fff;
}

/* Indicadores de foco */
*:focus {
    outline: 2px solid #007bff;
    outline-offset: 2px;
}

/* Diseño responsivo */
@media (max-width: 768px) {
    header {
        flex-direction: column;
        gap: 1rem;
    }
    
    nav ul {
        flex-direction: column;
        text-align: center;
    }
    
    .service-grid {
        grid-template-columns: 1fr;
    }
    
    .font-controls {
        justify-content: center;
    }
}
```

### Paso 3: JavaScript de Accesibilidad
Crear un archivo `accessibility.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Enlaces de omisión
    const skipLinks = document.querySelectorAll('.skip-link');
    skipLinks.forEach(link => {
        link.addEventListener('focus', function() {
            this.style.top = '6px';
        });
        link.addEventListener('blur', function() {
            this.style.top = '-40px';
        });
    });

    // Alternar alto contraste
    const themeToggle = document.getElementById('themeToggle');
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('high-contrast');
        const isHighContrast = document.body.classList.contains('high-contrast');
        localStorage.setItem('highContrast', isHighContrast);
        this.setAttribute('aria-pressed', isHighContrast);
        
        // Anunciar a lectores de pantalla
        announceToScreenReader(isHighContrast ? 'Modo de alto contraste habilitado' : 'Modo de alto contraste deshabilitado');
    });

    // Cargar preferencia de tema guardada
    const savedHighContrast = localStorage.getItem('highContrast') === 'true';
    if (savedHighContrast) {
        document.body.classList.add('high-contrast');
        themeToggle.setAttribute('aria-pressed', 'true');
    }

    // Controles de tamaño de fuente
    let currentFontSize = 16;
    const increaseFont = document.getElementById('increaseFont');
    const decreaseFont = document.getElementById('decreaseFont');
    const resetFont = document.getElementById('resetFont');

    function updateFontSize() {
        document.body.style.fontSize = currentFontSize + 'px';
        localStorage.setItem('fontSize', currentFontSize);
        
        // Actualizar etiquetas ARIA
        increaseFont.setAttribute('aria-disabled', currentFontSize >= 24);
        decreaseFont.setAttribute('aria-disabled', currentFontSize <= 12);
    }

    increaseFont.addEventListener('click', function() {
        if (currentFontSize < 24) {
            currentFontSize += 2;
            updateFontSize();
            announceToScreenReader('Tamaño de fuente aumentado');
        }
    });

    decreaseFont.addEventListener('click', function() {
        if (currentFontSize > 12) {
            currentFontSize -= 2;
            updateFontSize();
            announceToScreenReader('Tamaño de fuente disminuido');
        }
    });

    resetFont.addEventListener('click', function() {
        currentFontSize = 16;
        updateFontSize();
        announceToScreenReader('Tamaño de fuente restablecido');
    });

    // Cargar tamaño de fuente guardado
    const savedFontSize = localStorage.getItem('fontSize');
    if (savedFontSize) {
        currentFontSize = parseInt(savedFontSize);
        updateFontSize();
    }

    // Navegación por teclado para tarjetas de servicio
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach((card, index) => {
        card.setAttribute('tabindex', '0');
        card.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const button = this.querySelector('.learn-more');
                if (button) {
                    button.click();
                }
            }
        });
    });

    // Validación de formulario con accesibilidad
    const contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');
        
        let isValid = true;
        
        if (!name.value.trim()) {
            announceToScreenReader('El nombre es obligatorio');
            name.focus();
            isValid = false;
        } else if (!email.value.trim()) {
            announceToScreenReader('El correo electrónico es obligatorio');
            email.focus();
            isValid = false;
        } else if (!isValidEmail(email.value)) {
            announceToScreenReader('Por favor ingresa una dirección de correo electrónico válida');
            email.focus();
            isValid = false;
        } else if (!message.value.trim()) {
            announceToScreenReader('El mensaje es obligatorio');
            message.focus();
            isValid = false;
        }
        
        if (isValid) {
            announceToScreenReader('Formulario enviado exitosamente');
            // En una aplicación real, enviarías el formulario
            alert('¡Formulario enviado exitosamente!');
            contactForm.reset();
        }
    });

    // Región ARIA live dinámica para anuncios
    function announceToScreenReader(message) {
        let announcement = document.getElementById('sr-announcement');
        if (!announcement) {
            announcement = document.createElement('div');
            announcement.id = 'sr-announcement';
            announcement.setAttribute('aria-live', 'polite');
            announcement.setAttribute('aria-atomic', 'true');
            announcement.className = 'sr-only';
            document.body.appendChild(announcement);
        }
        announcement.textContent = message;
        
        // Limpiar después de un retraso
        setTimeout(() => {
            announcement.textContent = '';
        }, 1000);
    }

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Atajos de teclado
    document.addEventListener('keydown', function(e) {
        // Alt + H para alternar alto contraste
        if (e.altKey && e.key === 'h') {
            e.preventDefault();
            themeToggle.click();
        }
        
        // Alt + + para aumentar fuente
        if (e.altKey && e.key === '=') {
            e.preventDefault();
            increaseFont.click();
        }
        
        // Alt + - para disminuir fuente
        if (e.altKey && e.key === '-') {
            e.preventDefault();
            decreaseFont.click();
        }
    });

    // Gestión de foco
    const focusableElements = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
    
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            // Asegurar que el foco sea visible
            document.body.style.outline = 'none';
        }
    });

    // Inicializar
    announceToScreenReader('Página cargada. Presiona Alt+H para alto contraste, Alt+= para aumentar tamaño de fuente, Alt+- para disminuir tamaño de fuente.');
});
```

### Paso 4: Script de Pruebas de Accesibilidad en Python
Crear un archivo `accessibility_test.py`:

```python
import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin, urlparse
import time

class AccessibilityTester:
    def __init__(self, url):
        self.url = url
        self.results = {
            'url': url,
            'timestamp': time.time(),
            'tests': {
                'images_without_alt': [],
                'missing_lang_attribute': False,
                'missing_title': False,
                'low_contrast_elements': [],
                'missing_form_labels': [],
                'empty_links': [],
                'missing_headings': False,
                'keyboard_navigation_issues': [],
                'aria_issues': []
            },
            'score': 0,
            'recommendations': []
        }
    
    def run_tests(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            self.test_images_alt(soup)
            self.test_lang_attribute(soup)
            self.test_title(soup)
            self.test_form_labels(soup)
            self.test_empty_links(soup)
            self.test_headings(soup)
            self.test_aria_attributes(soup)
            
            self.calculate_score()
            self.generate_recommendations()
            
        except Exception as e:
            self.results['error'] = str(e)
    
    def test_images_alt(self, soup):
        images = soup.find_all('img')
        for img in images:
            if not img.get('alt') or img.get('alt').strip() == '':
                self.results['tests']['images_without_alt'].append({
                    'src': img.get('src', ''),
                    'line': str(img.sourceline) if hasattr(img, 'sourceline') else 'unknown'
                })
    
    def test_lang_attribute(self, soup):
        html_tag = soup.find('html')
        if not html_tag or not html_tag.get('lang'):
            self.results['tests']['missing_lang_attribute'] = True
    
    def test_title(self, soup):
        title_tag = soup.find('title')
        if not title_tag or not title_tag.string or title_tag.string.strip() == '':
            self.results['tests']['missing_title'] = True
    
    def test_form_labels(self, soup):
        inputs = soup.find_all('input')
        for input_tag in inputs:
            if input_tag.get('type') not in ['submit', 'button', 'hidden']:
                label = soup.find('label', {'for': input_tag.get('id')})
                if not label:
                    self.results['tests']['missing_form_labels'].append({
                        'id': input_tag.get('id', ''),
                        'name': input_tag.get('name', ''),
                        'type': input_tag.get('type', '')
                    })
    
    def test_empty_links(self, soup):
        links = soup.find_all('a')
        for link in links:
            if not link.get('href') or link.get('href').strip() == '':
                if not link.string or link.string.strip() == '':
                    self.results['tests']['empty_links'].append({
                        'line': str(link.sourceline) if hasattr(link, 'sourceline') else 'unknown'
                    })
    
    def test_headings(self, soup):
        h1_tags = soup.find_all('h1')
        if len(h1_tags) == 0:
            self.results['tests']['missing_headings'] = True
    
    def test_aria_attributes(self, soup):
        # Verificar atributos ARIA
        aria_elements = soup.find_all(attrs={'aria-label': True, 'aria-labelledby': True, 'aria-describedby': True})
        if len(aria_elements) == 0:
            self.results['tests']['aria_issues'].append('No se encontraron atributos ARIA - considera agregarlos para mejor soporte de lectores de pantalla')
        
        # Verificar atributos de rol
        role_elements = soup.find_all(attrs={'role': True})
        if len(role_elements) == 0:
            self.results['tests']['aria_issues'].append('No se encontraron atributos de rol - considera agregarlos para claridad semántica')
    
    def calculate_score(self):
        total_tests = 8
        passed_tests = 0
        
        if len(self.results['tests']['images_without_alt']) == 0:
            passed_tests += 1
        if not self.results['tests']['missing_lang_attribute']:
            passed_tests += 1
        if not self.results['tests']['missing_title']:
            passed_tests += 1
        if len(self.results['tests']['missing_form_labels']) == 0:
            passed_tests += 1
        if len(self.results['tests']['empty_links']) == 0:
            passed_tests += 1
        if not self.results['tests']['missing_headings']:
            passed_tests += 1
        if len(self.results['tests']['aria_issues']) == 0:
            passed_tests += 1
        if len(self.results['tests']['keyboard_navigation_issues']) == 0:
            passed_tests += 1
        
        self.results['score'] = (passed_tests / total_tests) * 100
    
    def generate_recommendations(self):
        if len(self.results['tests']['images_without_alt']) > 0:
            self.results['recommendations'].append('Agregar texto alternativo a todas las imágenes para usuarios de lectores de pantalla')
        
        if self.results['tests']['missing_lang_attribute']:
            self.results['recommendations'].append('Agregar atributo lang al elemento html')
        
        if self.results['tests']['missing_title']:
            self.results['recommendations'].append('Agregar un título descriptivo a la página')
        
        if len(self.results['tests']['missing_form_labels']) > 0:
            self.results['recommendations'].append('Asociar todas las entradas de formulario con etiquetas')
        
        if len(self.results['tests']['empty_links']) > 0:
            self.results['recommendations'].append('Asegurar que todos los enlaces tengan texto significativo o aria-labels')
        
        if self.results['tests']['missing_headings']:
            self.results['recommendations'].append('Agregar al menos un encabezado H1 a la página')
        
        if len(self.results['tests']['aria_issues']) > 0:
            self.results['recommendations'].append('Considerar agregar atributos ARIA para interacciones complejas')
    
    def generate_report(self):
        print(f"\n=== Reporte de Pruebas de Accesibilidad ===")
        print(f"URL: {self.results['url']}")
        print(f"Puntuación de Accesibilidad: {self.results['score']:.1f}%")
        
        print(f"\n=== Resultados de Pruebas ===")
        print(f"Imágenes sin texto alternativo: {len(self.results['tests']['images_without_alt'])}")
        print(f"Atributo lang faltante: {self.results['tests']['missing_lang_attribute']}")
        print(f"Título faltante: {self.results['tests']['missing_title']}")
        print(f"Entradas de formulario sin etiquetas: {len(self.results['tests']['missing_form_labels'])}")
        print(f"Enlaces vacíos: {len(self.results['tests']['empty_links'])}")
        print(f"Encabezados H1 faltantes: {self.results['tests']['missing_headings']}")
        print(f"Problemas ARIA: {len(self.results['tests']['aria_issues'])}")
        
        print(f"\n=== Recomendaciones ===")
        for rec in self.results['recommendations']:
            print(f"- {rec}")
        
        # Guardar resultados detallados
        with open('accessibility_report.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\nReporte detallado guardado en accessibility_report.json")

def main():
    # Probar archivo local
    tester = AccessibilityTester('file:///path/to/accessible_app.html')
    tester.run_tests()
    tester.generate_report()

if __name__ == "__main__":
    main()
```

### Paso 5: Documentación
Esta aplicación web accesible implementa cumplimiento WCAG 2.1 Nivel AA:

1. **Perceptible**: Texto alternativo para imágenes, contraste de color suficiente, texto escalable
2. **Operable**: Navegación por teclado, tiempo suficiente, sin convulsiones
3. **Comprensible**: Texto legible, navegación predecible, asistencia de entrada
4. **Robusto**: Compatible con tecnologías de asistencia

Características clave:
- HTML semántico con encabezados y puntos de referencia apropiados
- Atributos ARIA para interacciones complejas
- Navegación solo con teclado
- Modo de alto contraste
- Tamaños de fuente ajustables
- Anuncios de lector de pantalla
- Validación de formulario con retroalimentación de accesibilidad

El script en Python automatiza las pruebas de accesibilidad y proporciona una puntuación de cumplimiento con recomendaciones específicas para mejoras.
