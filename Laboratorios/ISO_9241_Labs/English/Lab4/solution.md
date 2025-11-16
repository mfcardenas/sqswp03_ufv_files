# Lab 4: User-Centered Design

## Solution

### Step 1: User Personas and Scenarios
Create user personas based on typical e-commerce users:

**Persona 1: Busy Professional**
- Age: 35-45
- Tech-savvy but time-constrained
- Needs: Quick, secure checkout
- Pain points: Long forms, unnecessary steps

**Persona 2: First-time Online Shopper**
- Age: 55-65
- Less tech-experienced
- Needs: Clear guidance, reassurance
- Pain points: Complex interfaces, unclear processes

**Scenario 1: Quick Purchase**
Busy Professional wants to buy a book quickly during lunch break.

**Scenario 2: First Purchase**
First-time shopper wants to buy a gift but is nervous about online security.

### Step 2: Current Design Analysis
Original checkout form issues:
- Too many form fields on one page
- Poor visual hierarchy
- Lack of progress indication
- No clear error handling
- Mobile-unfriendly design

### Step 3: Improved Checkout Form HTML
Create an `improved_checkout.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Improved Checkout - User-Centered Design</title>
    <link rel="stylesheet" href="checkout.css">
</head>
<body>
    <div class="checkout-container">
        <div class="progress-bar">
            <div class="step active" data-step="1">Cart</div>
            <div class="step" data-step="2">Shipping</div>
            <div class="step" data-step="3">Payment</div>
            <div class="step" data-step="4">Review</div>
        </div>
        
        <form id="checkoutForm">
            <!-- Step 1: Contact Information -->
            <div class="step-content active" id="step1">
                <h2>Contact Information</h2>
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required>
                    <span class="error" id="emailError"></span>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number (optional)</label>
                    <input type="tel" id="phone" name="phone">
                </div>
                <button type="button" class="next-btn">Continue to Shipping</button>
            </div>
            
            <!-- Step 2: Shipping Information -->
            <div class="step-content" id="step2">
                <h2>Shipping Information</h2>
                <div class="form-row">
                    <div class="form-group">
                        <label for="firstName">First Name</label>
                        <input type="text" id="firstName" name="firstName" required>
                        <span class="error" id="firstNameError"></span>
                    </div>
                    <div class="form-group">
                        <label for="lastName">Last Name</label>
                        <input type="text" id="lastName" name="lastName" required>
                        <span class="error" id="lastNameError"></span>
                    </div>
                </div>
                <div class="form-group">
                    <label for="address">Street Address</label>
                    <input type="text" id="address" name="address" required>
                    <span class="error" id="addressError"></span>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="city">City</label>
                        <input type="text" id="city" name="city" required>
                        <span class="error" id="cityError"></span>
                    </div>
                    <div class="form-group">
                        <label for="zipCode">ZIP Code</label>
                        <input type="text" id="zipCode" name="zipCode" required>
                        <span class="error" id="zipCodeError"></span>
                    </div>
                </div>
                <div class="form-group">
                    <label for="country">Country</label>
                    <select id="country" name="country" required>
                        <option value="">Select Country</option>
                        <option value="US">United States</option>
                        <option value="CA">Canada</option>
                        <option value="UK">United Kingdom</option>
                    </select>
                    <span class="error" id="countryError"></span>
                </div>
                <button type="button" class="prev-btn">Back to Contact</button>
                <button type="button" class="next-btn">Continue to Payment</button>
            </div>
            
            <!-- Step 3: Payment Information -->
            <div class="step-content" id="step3">
                <h2>Payment Information</h2>
                <div class="form-group">
                    <label for="cardNumber">Card Number</label>
                    <input type="text" id="cardNumber" name="cardNumber" placeholder="1234 5678 9012 3456" required>
                    <span class="error" id="cardNumberError"></span>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="expiryMonth">Expiry Month</label>
                        <select id="expiryMonth" name="expiryMonth" required>
                            <option value="">MM</option>
                            <option value="01">01</option>
                            <option value="02">02</option>
                            <!-- ... more months ... -->
                            <option value="12">12</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="expiryYear">Expiry Year</label>
                        <select id="expiryYear" name="expiryYear" required>
                            <option value="">YYYY</option>
                            <option value="2024">2024</option>
                            <option value="2025">2025</option>
                            <!-- ... more years ... -->
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
                    Your payment information is secure and encrypted.
                </div>
                <button type="button" class="prev-btn">Back to Shipping</button>
                <button type="button" class="next-btn">Review Order</button>
            </div>
            
            <!-- Step 4: Review and Submit -->
            <div class="step-content" id="step4">
                <h2>Review Your Order</h2>
                <div class="order-summary">
                    <h3>Order Summary</h3>
                    <div class="order-item">
                        <span>Product Name</span>
                        <span>$29.99</span>
                    </div>
                    <div class="order-item">
                        <span>Shipping</span>
                        <span>$5.99</span>
                    </div>
                    <div class="order-total">
                        <span>Total</span>
                        <span>$35.98</span>
                    </div>
                </div>
                
                <div class="shipping-summary">
                    <h3>Shipping Address</h3>
                    <p id="shippingAddress">Address will be displayed here</p>
                </div>
                
                <div class="payment-summary">
                    <h3>Payment Method</h3>
                    <p id="paymentMethod">Card ending in **** 3456</p>
                </div>
                
                <button type="button" class="prev-btn">Back to Payment</button>
                <button type="submit" class="submit-btn">Place Order</button>
            </div>
        </form>
    </div>
    <script src="checkout.js"></script>
</body>
</html>
```

### Step 4: CSS for User-Centered Design
Create a `checkout.css` file:

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

### Step 5: JavaScript for Multi-Step Form
Create a `checkout.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('checkoutForm');
    const steps = document.querySelectorAll('.step');
    const stepContents = document.querySelectorAll('.step-content');
    const nextButtons = document.querySelectorAll('.next-btn');
    const prevButtons = document.querySelectorAll('.prev-btn');
    let currentStep = 1;
    
    // Navigation functions
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
                errorElement.textContent = 'This field is required';
                field.style.borderColor = '#dc3545';
                isValid = false;
            } else {
                errorElement.textContent = '';
                field.style.borderColor = '#ced4da';
            }
        });
        
        // Additional validation for specific fields
        if (stepNumber === 3) {
            const cardNumber = document.getElementById('cardNumber');
            if (cardNumber.value && !/^\d{4}\s\d{4}\s\d{4}\s\d{4}$/.test(cardNumber.value)) {
                document.getElementById('cardNumberError').textContent = 'Please enter a valid card number';
                cardNumber.style.borderColor = '#dc3545';
                isValid = false;
            }
        }
        
        return isValid;
    }
    
    // Event listeners for navigation
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
    
    // Form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (validateStep(4)) {
            alert('Order placed successfully! (This is a demo)');
            // In a real application, you would submit the form data to a server
        }
    });
    
    // Auto-format card number
    document.getElementById('cardNumber').addEventListener('input', function(e) {
        let value = e.target.value.replace(/\s/g, '');
        if (value.length > 0) {
            value = value.match(/.{1,4}/g).join(' ');
        }
        e.target.value = value;
    });
    
    // Update review step with form data
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
    
    // Update review when moving to step 4
    document.querySelectorAll('.next-btn').forEach(button => {
        button.addEventListener('click', function() {
            if (currentStep === 3) {
                setTimeout(updateReview, 100);
            }
        });
    });
    
    // Initialize
    showStep(1);
});
```

### Step 6: Python User Testing Script
Create a `user_testing.py` file:

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
            
            # Simulate user behavior based on type
            if user_type == 'experienced':
                self.simulate_experienced_user()
            elif user_type == 'novice':
                self.simulate_novice_user()
            else:
                self.simulate_typical_user()
            
            # Check if order was placed
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.alert_is_present()
                )
                alert = self.driver.switch_to.alert
                if "successfully" in alert.text:
                    self.results['successful_completions'] += 1
                alert.accept()
            except:
                self.results['usability_issues'].append(f"{scenario_name}: Order not completed")
            
            end_time = time.time()
            completion_time = end_time - start_time
            
            return completion_time
            
        except Exception as e:
            self.results['usability_issues'].append(f"{scenario_name}: {str(e)}")
            return None
        finally:
            # Reset for next test
            self.driver.delete_all_cookies()
    
    def simulate_experienced_user(self):
        # Quick, efficient completion
        self.fill_contact_info()
        self.fill_shipping_info()
        self.fill_payment_info()
        self.review_and_submit()
    
    def simulate_novice_user(self):
        # Slower, with pauses and potential errors
        time.sleep(random.uniform(1, 3))
        self.fill_contact_info()
        time.sleep(random.uniform(2, 5))
        self.fill_shipping_info()
        time.sleep(random.uniform(1, 3))
        # Simulate going back
        self.driver.find_element(By.CLASS_NAME, 'prev-btn').click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'next-btn').click()
        time.sleep(random.uniform(2, 5))
        self.fill_payment_info()
        time.sleep(random.uniform(1, 3))
        self.review_and_submit()
    
    def simulate_typical_user(self):
        # Mix of behaviors
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
        ).send_keys("John")
        
        self.driver.find_element(By.ID, "lastName").send_keys("Doe")
        self.driver.find_element(By.ID, "address").send_keys("123 Main St")
        self.driver.find_element(By.ID, "city").send_keys("Anytown")
        self.driver.find_element(By.ID, "zipCode").send_keys("12345")
        
        country_select = self.driver.find_element(By.ID, "country")
        country_select.click()
        self.driver.find_element(By.CSS_SELECTOR, "option[value='US']").click()
        
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
            scenario_name = f"Test {i+1} ({user_type})"
            
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
        print("\n=== User-Centered Design Testing Report ===")
        print(f"Total Tests: {self.results['total_tests']}")
        print(f"Successful Completions: {self.results['successful_completions']}")
        print(f"Average Completion Time: {self.results['average_completion_time']:.2f} seconds")
        print(f"Error Rate: {self.results['error_rate']:.2%}")
        print(f"Abandonment Rate: {self.results['abandonment_rate']:.2%}")
        
        print("\nUsability Issues:")
        for issue in self.results['usability_issues']:
            print(f"- {issue}")
        
        # Save results
        with open('ucd_test_results.json', 'w') as f:
            json.dump(self.results, f, indent=2)
    
    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    tester = CheckoutTester()
    tester.run_test_suite(5)  # Run 5 tests for demo
    tester.close()
```

### Step 7: Documentation of UCD Process
This lab demonstrates the user-centered design process:

1. **Understand User Needs**: Created personas and scenarios
2. **Specify Requirements**: Identified key usability issues
3. **Produce Design Solutions**: Created multi-step form with progress indication
4. **Evaluate Designs**: Implemented automated testing
5. **Implement and Deploy**: Provided working prototype

Key improvements:
- Reduced cognitive load with step-by-step process
- Clear progress indication
- Better error handling and validation
- Mobile-responsive design
- Security reassurance for users

The Python script simulates different user types and measures key metrics to validate the UCD approach.
