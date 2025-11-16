# Lab 5: Accessibility Standards

## Solution

### Step 1: Accessible HTML Structure
Create an `accessible_app.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessible Web Application - ISO 9241 Lab</title>
    <link rel="stylesheet" href="accessibility.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <header>
        <nav aria-label="Main navigation">
            <ul>
                <li><a href="#home" aria-current="page">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
        <button id="themeToggle" aria-label="Toggle high contrast mode">High Contrast</button>
        <div class="font-controls">
            <button id="increaseFont" aria-label="Increase font size">+</button>
            <button id="decreaseFont" aria-label="Decrease font size">-</button>
            <button id="resetFont" aria-label="Reset font size">Reset</button>
        </div>
    </header>

    <main>
        <section id="home" aria-labelledby="home-heading">
            <h1 id="home-heading">Welcome to Our Accessible Application</h1>
            <img src="logo.png" alt="Company Logo - A blue circle with white text" width="200" height="200">
            <p>This application demonstrates ISO 9241 accessibility standards and WCAG 2.1 compliance.</p>
        </section>

        <section id="about" aria-labelledby="about-heading">
            <h2 id="about-heading">About Accessibility</h2>
            <p>Accessibility ensures that people with disabilities can use digital products effectively.</p>
            <figure>
                <img src="accessibility-diagram.png" alt="Diagram showing different types of disabilities and assistive technologies" width="400" height="300">
                <figcaption>Types of disabilities and assistive technologies</figcaption>
            </figure>
        </section>

        <section id="services" aria-labelledby="services-heading">
            <h2 id="services-heading">Our Services</h2>
            <div class="service-grid">
                <article class="service-card">
                    <h3>Web Accessibility Audit</h3>
                    <p>We evaluate websites for WCAG compliance and provide detailed reports.</p>
                    <button class="learn-more" aria-describedby="service1-desc">Learn More</button>
                    <div id="service1-desc" class="sr-only">Learn more about our web accessibility audit service</div>
                </article>
                
                <article class="service-card">
                    <h3>Accessibility Training</h3>
                    <p>Comprehensive training programs for developers and designers.</p>
                    <button class="learn-more" aria-describedby="service2-desc">Learn More</button>
                    <div id="service2-desc" class="sr-only">Learn more about our accessibility training programs</div>
                </article>
                
                <article class="service-card">
                    <h3>Assistive Technology Support</h3>
                    <p>Integration and support for various assistive technologies.</p>
                    <button class="learn-more" aria-describedby="service3-desc">Learn More</button>
                    <div id="service3-desc" class="sr-only">Learn more about our assistive technology support</div>
                </article>
            </div>
        </section>

        <section id="contact" aria-labelledby="contact-heading">
            <h2 id="contact-heading">Contact Us</h2>
            <form id="contactForm" aria-labelledby="contact-heading">
                <div class="form-group">
                    <label for="name">Full Name</label>
                    <input type="text" id="name" name="name" required aria-describedby="name-help">
                    <div id="name-help" class="help-text">Enter your full name as it appears on your ID</div>
                </div>
                
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required aria-describedby="email-help">
                    <div id="email-help" class="help-text">We'll use this to respond to your inquiry</div>
                </div>
                
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" rows="5" required aria-describedby="message-help"></textarea>
                    <div id="message-help" class="help-text">Tell us how we can help you</div>
                </div>
                
                <button type="submit" aria-describedby="submit-help">Send Message</button>
                <div id="submit-help" class="sr-only">Submit your contact form</div>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Accessible Web Applications. All rights reserved.</p>
        <nav aria-label="Footer navigation">
            <ul>
                <li><a href="#privacy">Privacy Policy</a></li>
                <li><a href="#terms">Terms of Service</a></li>
                <li><a href="#accessibility">Accessibility Statement</a></li>
            </ul>
        </nav>
    </footer>

    <div id="skipLinks" class="sr-only">
        <a href="#main" class="skip-link">Skip to main content</a>
        <a href="#navigation" class="skip-link">Skip to navigation</a>
    </div>

    <script src="accessibility.js"></script>
</body>
</html>
```

### Step 2: Accessible CSS
Create an `accessibility.css` file:

```css
/* Base styles */
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

/* Header and Navigation */
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

/* Main Content */
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

/* Service Grid */
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

/* Form Styles */
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

/* Footer */
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

/* High Contrast Mode */
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

/* Focus indicators */
*:focus {
    outline: 2px solid #007bff;
    outline-offset: 2px;
}

/* Responsive design */
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

### Step 3: Accessibility JavaScript
Create an `accessibility.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Skip links
    const skipLinks = document.querySelectorAll('.skip-link');
    skipLinks.forEach(link => {
        link.addEventListener('focus', function() {
            this.style.top = '6px';
        });
        link.addEventListener('blur', function() {
            this.style.top = '-40px';
        });
    });

    // High contrast toggle
    const themeToggle = document.getElementById('themeToggle');
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('high-contrast');
        const isHighContrast = document.body.classList.contains('high-contrast');
        localStorage.setItem('highContrast', isHighContrast);
        this.setAttribute('aria-pressed', isHighContrast);
        
        // Announce to screen readers
        announceToScreenReader(isHighContrast ? 'High contrast mode enabled' : 'High contrast mode disabled');
    });

    // Load saved theme preference
    const savedHighContrast = localStorage.getItem('highContrast') === 'true';
    if (savedHighContrast) {
        document.body.classList.add('high-contrast');
        themeToggle.setAttribute('aria-pressed', 'true');
    }

    // Font size controls
    let currentFontSize = 16;
    const increaseFont = document.getElementById('increaseFont');
    const decreaseFont = document.getElementById('decreaseFont');
    const resetFont = document.getElementById('resetFont');

    function updateFontSize() {
        document.body.style.fontSize = currentFontSize + 'px';
        localStorage.setItem('fontSize', currentFontSize);
        
        // Update ARIA labels
        increaseFont.setAttribute('aria-disabled', currentFontSize >= 24);
        decreaseFont.setAttribute('aria-disabled', currentFontSize <= 12);
    }

    increaseFont.addEventListener('click', function() {
        if (currentFontSize < 24) {
            currentFontSize += 2;
            updateFontSize();
            announceToScreenReader('Font size increased');
        }
    });

    decreaseFont.addEventListener('click', function() {
        if (currentFontSize > 12) {
            currentFontSize -= 2;
            updateFontSize();
            announceToScreenReader('Font size decreased');
        }
    });

    resetFont.addEventListener('click', function() {
        currentFontSize = 16;
        updateFontSize();
        announceToScreenReader('Font size reset');
    });

    // Load saved font size
    const savedFontSize = localStorage.getItem('fontSize');
    if (savedFontSize) {
        currentFontSize = parseInt(savedFontSize);
        updateFontSize();
    }

    // Keyboard navigation for service cards
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

    // Form validation with accessibility
    const contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');
        
        let isValid = true;
        
        if (!name.value.trim()) {
            announceToScreenReader('Name is required');
            name.focus();
            isValid = false;
        } else if (!email.value.trim()) {
            announceToScreenReader('Email is required');
            email.focus();
            isValid = false;
        } else if (!isValidEmail(email.value)) {
            announceToScreenReader('Please enter a valid email address');
            email.focus();
            isValid = false;
        } else if (!message.value.trim()) {
            announceToScreenReader('Message is required');
            message.focus();
            isValid = false;
        }
        
        if (isValid) {
            announceToScreenReader('Form submitted successfully');
            // In a real application, you would submit the form
            alert('Form submitted successfully!');
            contactForm.reset();
        }
    });

    // Dynamic ARIA live region for announcements
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
        
        // Clear after a delay
        setTimeout(() => {
            announcement.textContent = '';
        }, 1000);
    }

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Alt + H for high contrast toggle
        if (e.altKey && e.key === 'h') {
            e.preventDefault();
            themeToggle.click();
        }
        
        // Alt + + for increase font
        if (e.altKey && e.key === '=') {
            e.preventDefault();
            increaseFont.click();
        }
        
        // Alt + - for decrease font
        if (e.altKey && e.key === '-') {
            e.preventDefault();
            decreaseFont.click();
        }
    });

    // Focus management
    const focusableElements = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
    
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            // Ensure focus is visible
            document.body.style.outline = 'none';
        }
    });

    // Initialize
    announceToScreenReader('Page loaded. Press Alt+H for high contrast, Alt+= to increase font size, Alt+- to decrease font size.');
});
```

### Step 4: Python Accessibility Testing Script
Create an `accessibility_test.py` file:

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
        # Check for ARIA attributes
        aria_elements = soup.find_all(attrs={'aria-label': True, 'aria-labelledby': True, 'aria-describedby': True})
        if len(aria_elements) == 0:
            self.results['tests']['aria_issues'].append('No ARIA attributes found - consider adding them for better screen reader support')
        
        # Check for role attributes
        role_elements = soup.find_all(attrs={'role': True})
        if len(role_elements) == 0:
            self.results['tests']['aria_issues'].append('No role attributes found - consider adding them for semantic clarity')
    
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
            self.results['recommendations'].append('Add alt text to all images for screen reader users')
        
        if self.results['tests']['missing_lang_attribute']:
            self.results['recommendations'].append('Add lang attribute to html element')
        
        if self.results['tests']['missing_title']:
            self.results['recommendations'].append('Add a descriptive title to the page')
        
        if len(self.results['tests']['missing_form_labels']) > 0:
            self.results['recommendations'].append('Associate all form inputs with labels')
        
        if len(self.results['tests']['empty_links']) > 0:
            self.results['recommendations'].append('Ensure all links have meaningful text or aria-labels')
        
        if self.results['tests']['missing_headings']:
            self.results['recommendations'].append('Add at least one H1 heading to the page')
        
        if len(self.results['tests']['aria_issues']) > 0:
            self.results['recommendations'].append('Consider adding ARIA attributes for complex interactions')
    
    def generate_report(self):
        print(f"\n=== Accessibility Test Report ===")
        print(f"URL: {self.results['url']}")
        print(f"Accessibility Score: {self.results['score']:.1f}%")
        
        print(f"\n=== Test Results ===")
        print(f"Images without alt text: {len(self.results['tests']['images_without_alt'])}")
        print(f"Missing lang attribute: {self.results['tests']['missing_lang_attribute']}")
        print(f"Missing title: {self.results['tests']['missing_title']}")
        print(f"Form inputs without labels: {len(self.results['tests']['missing_form_labels'])}")
        print(f"Empty links: {len(self.results['tests']['empty_links'])}")
        print(f"Missing H1 headings: {self.results['tests']['missing_headings']}")
        print(f"ARIA issues: {len(self.results['tests']['aria_issues'])}")
        
        print(f"\n=== Recommendations ===")
        for rec in self.results['recommendations']:
            print(f"- {rec}")
        
        # Save detailed results
        with open('accessibility_report.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\nDetailed report saved to accessibility_report.json")

def main():
    # Test local file
    tester = AccessibilityTester('file:///path/to/accessible_app.html')
    tester.run_tests()
    tester.generate_report()

if __name__ == "__main__":
    main()
```

### Step 5: Documentation
This accessible web application implements WCAG 2.1 Level AA compliance:

1. **Perceivable**: Alt text for images, sufficient color contrast, scalable text
2. **Operable**: Keyboard navigation, sufficient time, no seizures
3. **Understandable**: Readable text, predictable navigation, input assistance
4. **Robust**: Compatible with assistive technologies

Key features:
- Semantic HTML with proper headings and landmarks
- ARIA attributes for complex interactions
- Keyboard-only navigation
- High contrast mode
- Adjustable font sizes
- Screen reader announcements
- Form validation with accessibility feedback

The Python script automates accessibility testing and provides a compliance score with specific recommendations for improvement.
