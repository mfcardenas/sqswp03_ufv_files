# Laboratorio 4: Diseño Centrado en el Usuario

## Solución

### Paso 1: Personas de Usuario y Escenarios
Crear personas de usuario basadas en usuarios típicos de comercio electrónico:

**Persona 1: Profesional Ocupado**
- Edad: 35-45
- Hábil en tecnología pero con restricciones de tiempo
- Necesidades: Pago rápido, seguro
- Puntos de dolor: Formularios largos, pasos innecesarios

**Persona 2: Comprador en Línea por Primera Vez**
- Edad: 55-65
- Menos experiencia en tecnología
- Necesidades: Guía clara, tranquilidad
- Puntos de dolor: Interfaces complejas, procesos poco claros

**Escenario 1: Compra Rápida**
Profesional ocupado quiere comprar un libro rápidamente durante el almuerzo.

**Escenario 2: Primera Compra**
Comprador por primera vez quiere comprar un regalo pero está nervioso por la seguridad en línea.

### Paso 2: Análisis de Diseño Actual
Problemas del formulario de pago original:
- Demasiados campos de formulario en una página
- Jerarquía visual pobre
- Falta de indicación de progreso
- Manejo de errores poco claro
- Diseño no amigable para móviles

### Paso 3: HTML de Formulario de Pago Mejorado
Crear un archivo `improved_checkout.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Pago Mejorado - Diseño Centrado en el Usuario</title>
    <link rel="stylesheet" href="checkout.css">
</head>
<body>
    <div class="checkout-container">
        <div class="progress-bar">
            <div class="step active" data-step="1">Carrito</div>
            <div class="step" data-step="2">Envío</div>
            <div class="step" data-step="3">Pago</div>
            <div class="step" data-step="4">Revisar</div>
        </div>
        
        <form id="checkoutForm">
            <!-- Paso 1: Información de Contacto -->
            <div class="step-content active" id="step1">
                <h2>Información de Contacto</h2>
                <div class="form-group">
                    <label for="email">Dirección de Correo Electrónico</label>
                    <input type="email" id="email" name="email" required>
                    <span class="error" id="emailError"></span>
                </div>
                <div class="form-group">
                    <label for="phone">Número de Teléfono (opcional)</label>
                    <input type="tel" id="phone" name="phone">
                </div>
                <button type="button" class="next-btn">Continuar con Envío</button>
            </div>
            
            <!-- Paso 2: Información de Envío -->
            <div class="step-content" id="step2">
                <h2>Información de Envío</h2>
                <div class="form-row">
                    <div class="form-group">
                        <label for="firstName">Nombre</label>
                        <input type="text" id="firstName" name="firstName" required>
                        <span class="error" id="firstNameError"></span>
                    </div>
                    <div class="form-group">
                        <label for="lastName">Apellido</label>
                        <input type="text" id="lastName" name="lastName" required>
                        <span class="error" id="lastNameError"></span>
                    </div>
                </div>
                <div class="form-group">
                    <label for="address">Dirección</label>
                    <input type="text" id="address" name="address" required>
                    <span class="error" id="addressError"></span>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="city">Ciudad</label>
                        <input type="text" id="city" name="city" required>
                        <span class="error" id="cityError"></span>
                    </div>
                    <div class="form-group">
                        <label for="zipCode">Código Postal</label>
                        <input type="text" id="zipCode" name="zipCode" required>
                        <span class="error" id="zipCodeError"></span>
                    </div>
                </div>
                <div class="form-group">
                    <label for="country">País</label>
                    <select id="country" name="country" required>
                        <option value="">Seleccionar País</option>
                        <option value="ES">España</option>
                        <option value="MX">México</option>
                        <option value="AR">Argentina</option>
                    </select>
                    <span class="error" id="countryError"></span>
                </div>
                <button type="button" class="prev-btn">Volver a Contacto</button>
                <button type="button" class="next-btn">Continuar con Pago</button>
            </div>
            
            <!-- Paso 3: Información de Pago -->
            <div class="step-content" id="step3">
                <h2>Información de Pago</h2>
                <div class="form-group">
                    <label for="cardNumber">Número de Tarjeta</label>
                    <input type="text" id="cardNumber" name="cardNumber" placeholder="1234 5678 9012 3456" required>
                    <span class="error" id="cardNumberError"></span>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="expiryMonth">Mes de Expiración</label>
                        <select id="expiryMonth" name="expiryMonth" required>
                            <option value="">MM</option>
                            <option value="01">01</option>
                            <option value="02">02</option>
                            <!-- ... más meses ... -->
                            <option value="12">12</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="expiryYear">Año de Expiración</label>
                        <select id="expiryYear" name="expiryYear" required>
                            <option value="">AAAA</option>
                            <option value="2024">2024</option>
                            <option value="2025">2025</option>
                            <!-- ... más años ... -->
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="cvv">CVV</label>
                        <input type="text" id="cvv" name="cvv" placeholder="123" required>
                        <span class="error" id="cvvError"></span>
                    </div>
                </div>
                <div class="security-notice">
                    <span class="lock-icon">🔒</span>
                    Tu información de pago está segura y encriptada.
                </div>
                <button type="button" class="prev-btn">Volver a Envío</button>
                <button type="button" class="next-btn">Revisar Pedido</button>
            </div>
            
            <!-- Paso 4: Revisar y Enviar -->
            <div class="step-content" id="step4">
                <h2>Revisar Tu Pedido</h2>
                <div class="order-summary">
                    <h3>Resumen del Pedido</h3>
                    <div class="order-item">
                        <span>Nombre del Producto</span>
                        <span>€29.99</span>
                    </div>
                    <div class="order-item">
                        <span>Envío</span>
                        <span>€5.99</span>
                    </div>
                    <div class="order-total">
                        <span>Total</span>
                        <span>€35.98</span>
                    </div>
                </div>
                
                <div class="shipping-summary">
                    <h3>Dirección de Envío</h3>
                    <p id="shippingAddress">La dirección se mostrará aquí</p>
                </div>
                
                <div class="payment-summary">
                    <h3>Método de Pago</h3>
                    <p id="paymentMethod">Tarjeta terminada en **** 3456</p>
                </div>
                
                <button type="button" class="prev-btn">Volver a Pago</button>
                <button type="submit" class="submit-btn">Realizar Pedido</button>
            </div>
        </form>
    </div>
    <script src="checkout.js"></script>
</body>
</html>
```

### Paso 4: CSS para Diseño Centrado en el Usuario
Crear un archivo `checkout.css`:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 20px;
    color: #333;
}

.checkout-container {
    max-width: 800px;
    margin: 0 auto;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    overflow: hidden;
}

.progress-bar {
    display: flex;
    background-color: #e9ecef;
    padding: 20px;
}

.step {
    flex: 1;
    text-align: center;
    position: relative;
    color: #6c757d;
}

.step.active {
    color: #007bff;
    font-weight: bold;
}

.step:not(:last-child)::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 100%;
    width: 100%;
    height: 2px;
    background-color: #dee2e6;
    z-index: 1;
}

.step.active:not(:last-child)::after {
    background-color: #007bff;
}

.step-content {
    display: none;
    padding: 30px;
}

.step-content.active {
    display: block;
}

h2 {
    color: #495057;
    margin-bottom: 20px;
    font-size: 24px;
}

.form-row {
    display: flex;
    gap: 20px;
}

.form-group {
    margin-bottom: 20px;
    flex: 1;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: 500;
    color: #495057;
}

input, select {
    width: 100%;
    padding: 12px;
    border: 1px solid #ced4da;
    border-radius: 4px;
    font-size: 16px;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

input:focus, select:focus {
    outline: 0;
    border-color: #80bdff;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.error {
    color: #dc3545;
    font-size: 14px;
    margin-top: 5px;
    display: block;
}

button {
    padding: 12px 24px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.15s ease-in-out;
}

.next-btn, .submit-btn {
    background-color: #007bff;
    color: white;
    float: right;
}

.next-btn:hover, .submit-btn:hover {
    background-color: #0056b3;
}

.prev-btn {
    background-color: #6c757d;
    color: white;
    margin-right: 10px;
}

.prev-btn:hover {
    background-color: #545b62;
}

.security-notice {
    background-color: #d4edda;
    color: #155724;
    padding: 10px;
    border-radius: 4px;
    margin: 20px 0;
    display: flex;
    align-items: center;
}

.lock-icon {
    margin-right: 10px;
    font-size: 18px;
}

.order-summary, .shipping-summary, .payment-summary {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 4px;
    margin-bottom: 20px;
}

.order-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
}

.order-total {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    font-size: 18px;
    border-top: 1px solid #dee2e6;
    padding-top: 10px;
    margin-top: 10px;
}

@media (max-width: 768px) {
    .form-row {
        flex-direction: column;
        gap: 0;
    }
    
    .progress-bar {
        flex-direction: column;
        text-align: left;
    }
    
    .step:not(:last-child)::after {
        top: 100%;
        left: 0;
        width: 2px;
        height: 20px;
    }
}
```

### Paso 5: JavaScript para Formulario Multi-Paso
Crear un archivo `checkout.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('checkoutForm');
    const steps = document.querySelectorAll('.step');
    const stepContents = document.querySelectorAll('.step-content');
    const nextButtons = document.querySelectorAll('.next-btn');
    const prevButtons = document.querySelectorAll('.prev-btn');
    let currentStep = 1;
    
    // Funciones de navegación
    function showStep(stepNumber) {
        stepContents.forEach(content => content.classList.remove('active'));
        steps.forEach(step => step.classList.remove('active'));
        
        document.getElementById(`step${stepNumber}`).classList.add('active');
        document.querySelector(`[data-step="${stepNumber}"]`).classList.add('active');
        
        currentStep = stepNumber;
    }
    
    function validateStep(stepNumber) {
        const stepElement = document.getElementById(`step${stepNumber}`);
        const requiredFields = stepElement.querySelectorAll('input[required], select[required]');
        let isValid = true;
        
        requiredFields.forEach(field => {
            const errorElement = document.getElementById(`${field.id}Error`);
            if (!field.value.trim()) {
                errorElement.textContent = 'Este campo es obligatorio';
                field.style.borderColor = '#dc3545';
                isValid = false;
            } else {
                errorElement.textContent = '';
                field.style.borderColor = '#ced4da';
            }
        });
        
        // Validación adicional para campos específicos
        if (stepNumber === 3) {
            const cardNumber = document.getElementById('cardNumber');
            if (cardNumber.value && !/^\d{4}\s\d{4}\s\d{4}\s\d{4}$/.test(cardNumber.value)) {
                document.getElementById('cardNumberError').textContent = 'Por favor ingresa un número de tarjeta válido';
                cardNumber.style.borderColor = '#dc3545';
                isValid = false;
            }
        }
        
        return isValid;
    }
    
    // Event listeners para navegación
    nextButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (validateStep(currentStep)) {
                if (currentStep < 4) {
                    showStep(currentStep + 1);
                }
            }
        });
    });
    
    prevButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (currentStep > 1) {
                showStep(currentStep - 1);
            }
        });
    });
    
    // Envío del formulario
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (validateStep(4)) {
            alert('¡Pedido realizado exitosamente! (Esto es una demo)');
            // En una aplicación real, enviarías los datos del formulario a un servidor
        }
    });
    
    // Auto-formatear número de tarjeta
    document.getElementById('cardNumber').addEventListener('input', function(e) {
        let value = e.target.value.replace(/\s/g, '');
        if (value.length > 0) {
            value = value.match(/.{1,4}/g).join(' ');
        }
        e.target.value = value;
    });
    
    // Actualizar paso de revisión con datos del formulario
    function updateReview() {
        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        const address = document.getElementById('address').value;
        const city = document.getElementById('city').value;
        const zipCode = document.getElementById('zipCode').value;
        const country = document.getElementById('country').value;
        
        document.getElementById('shippingAddress').textContent = 
            `${firstName} ${lastName}\n${address}\n${city}, ${zipCode}\n${country}`;
    }
    
    // Actualizar revisión al mover al paso 4
    document.querySelectorAll('.next-btn').forEach(button => {
        button.addEventListener('click', function() {
            if (currentStep === 3) {
                setTimeout(updateReview, 100);
            }
        });
    });
    
    // Inicializar
    showStep(1);
});
```

### Paso 6: Script de Pruebas de Usuario en Python
Crear un archivo `user_testing.py`:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json

class CheckoutTester:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.results = {
            'total_tests': 0,
            'successful_completions': 0,
            'average_completion_time': 0,
            'error_rate': 0,
            'abandonment_rate': 0,
            'usability_issues': []
        }
    
    def run_test_scenario(self, scenario_name, user_type):
        self.results['total_tests'] += 1
        start_time = time.time()
        
        try:
            self.driver.get('file:///path/to/improved_checkout.html')
            
            # Simular comportamiento de usuario basado en tipo
            if user_type == 'experienced':
                self.simulate_experienced_user()
            elif user_type == 'novice':
                self.simulate_novice_user()
            else:
                self.simulate_typical_user()
            
            # Verificar si el pedido fue realizado
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.alert_is_present()
                )
                alert = self.driver.switch_to.alert
                if "exitosamente" in alert.text:
                    self.results['successful_completions'] += 1
                alert.accept()
            except:
                self.results['usability_issues'].append(f"{scenario_name}: Pedido no completado")
            
            end_time = time.time()
            completion_time = end_time - start_time
            
            return completion_time
            
        except Exception as e:
            self.results['usability_issues'].append(f"{scenario_name}: {str(e)}")
            return None
        finally:
            # Reiniciar para siguiente prueba
            self.driver.delete_all_cookies()
    
    def simulate_experienced_user(self):
        # Finalización rápida, eficiente
        self.fill_contact_info()
        self.fill_shipping_info()
        self.fill_payment_info()
        self.review_and_submit()
    
    def simulate_novice_user(self):
        # Más lento, con pausas y posibles errores
        time.sleep(random.uniform(1, 3))
        self.fill_contact_info()
        time.sleep(random.uniform(2, 5))
        self.fill_shipping_info()
        time.sleep(random.uniform(1, 3))
        # Simular volver atrás
        self.driver.find_element(By.CLASS_NAME, 'prev-btn').click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'next-btn').click()
        time.sleep(random.uniform(2, 5))
        self.fill_payment_info()
        time.sleep(random.uniform(1, 3))
        self.review_and_submit()
    
    def simulate_typical_user(self):
        # Mezcla de comportamientos
        self.fill_contact_info()
        time.sleep(random.uniform(1, 2))
        self.fill_shipping_info()
        time.sleep(random.uniform(1, 2))
        self.fill_payment_info()
        time.sleep(random.uniform(1, 2))
        self.review_and_submit()
    
    def fill_contact_info(self):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "email"))
        )
        email_field.send_keys("test@example.com")
        
        next_btn = self.driver.find_element(By.CLASS_NAME, 'next-btn')
        next_btn.click()
    
    def fill_shipping_info(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "firstName"))
        ).send_keys("Juan")
        
        self.driver.find_element(By.ID, "lastName").send_keys("Pérez")
        self.driver.find_element(By.ID, "address").send_keys("Calle Principal 123")
        self.driver.find_element(By.ID, "city").send_keys("Madrid")
        self.driver.find_element(By.ID, "zipCode").send_keys("28001")
        
        country_select = self.driver.find_element(By.ID, "country")
        country_select.click()
        self.driver.find_element(By.CSS_SELECTOR, "option[value='ES']").click()
        
        next_btn = self.driver.find_element(By.CLASS_NAME, 'next-btn')
        next_btn.click()
    
    def fill_payment_info(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cardNumber"))
        ).send_keys("1234 5678 9012 3456")
        
        self.driver.find_element(By.ID, "expiryMonth").click()
        self.driver.find_element(By.CSS_SELECTOR, "option[value='12']").click()
        
        self.driver.find_element(By.ID, "expiryYear").click()
        self.driver.find_element(By.CSS_SELECTOR, "option[value='2025']").click()
        
        self.driver.find_element(By.ID, "cvv").send_keys("123")
        
        next_btn = self.driver.find_element(By.CLASS_NAME, 'next-btn')
        next_btn.click()
    
    def review_and_submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-btn"))
        ).click()
    
    def run_test_suite(self, num_tests=10):
        completion_times = []
        
        for i in range(num_tests):
            user_types = ['experienced', 'novice', 'typical']
            user_type = random.choice(user_types)
            scenario_name = f"Prueba {i+1} ({user_type})"
            
            completion_time = self.run_test_scenario(scenario_name, user_type)
            if completion_time:
                completion_times.append(completion_time)
        
        self.calculate_results(completion_times)
        self.generate_report()
    
    def calculate_results(self, completion_times):
        if completion_times:
            self.results['average_completion_time'] = sum(completion_times) / len(completion_times)
        
        self.results['error_rate'] = len(self.results['usability_issues']) / self.results['total_tests']
        self.results['abandonment_rate'] = (self.results['total_tests'] - self.results['successful_completions']) / self.results['total_tests']
    
    def generate_report(self):
        print("\n=== Reporte de Pruebas de Diseño Centrado en el Usuario ===")
        print(f"Total de Pruebas: {self.results['total_tests']}")
        print(f"Finalizaciones Exitosas: {self.results['successful_completions']}")
        print(f"Tiempo Promedio de Finalización: {self.results['average_completion_time']:.2f} segundos")
        print(f"Tasa de Error: {self.results['error_rate']:.2%}")
        print(f"Tasa de Abandono: {self.results['abandonment_rate']:.2%}")
        
        print("\nProblemas de Usabilidad:")
        for issue in self.results['usability_issues']:
            print(f"- {issue}")
        
        # Guardar resultados
        with open('ucd_test_results.json', 'w') as f:
            json.dump(self.results, f, indent=2)
    
    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    tester = CheckoutTester()
    tester.run_test_suite(5)  # Ejecutar 5 pruebas para demo
    tester.close()
```

### Paso 7: Documentación del Proceso UCD
Este laboratorio demuestra el proceso de diseño centrado en el usuario:

1. **Entender Necesidades del Usuario**: Crear personas y escenarios
2. **Especificar Requisitos**: Identificar problemas clave de usabilidad
3. **Producir Soluciones de Diseño**: Crear formulario multi-paso con indicación de progreso
4. **Evaluar Diseños**: Implementar pruebas automatizadas
5. **Implementar y Desplegar**: Proporcionar prototipo funcional

Mejoras clave:
- Reducida carga cognitiva con proceso paso a paso
- Indicación clara de progreso
- Mejor manejo de errores y validación
- Diseño responsivo para móviles
- Tranquilidad de seguridad para usuarios

El script en Python simula diferentes tipos de usuario y mide métricas clave para validar el enfoque UCD.
