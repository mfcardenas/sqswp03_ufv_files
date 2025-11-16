# Lab 2: Usability Principles

## Solution

### Step 1: Original Problematic Code
Here's the original form with usability issues:

```html
<!-- original.html -->
<html>
<body>
<form action="submit.php" method="post">
Username: <input type="text" name="user"><br>
Password: <input type="password" name="pass"><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
```

Issues: Poor layout, no labels, no feedback, no validation.

### Step 2: Improved HTML Structure
Create an `improved.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Improved Login Form</title>
    <link rel="stylesheet" href="improved.css">
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form id="loginForm">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
                <span class="error" id="usernameError"></span>
            </div>
            
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <span class="error" id="passwordError"></span>
            </div>
            
            <button type="submit">Login</button>
        </form>
        <div id="message"></div>
    </div>
    <script src="improved.js"></script>
</body>
</html>
```

### Step 3: Improved CSS
Create an `improved.css` file:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    width: 350px;
}

h1 {
    text-align: center;
    color: #333;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

input:focus {
    border-color: #4CAF50;
    outline: none;
}

.error {
    color: red;
    font-size: 12px;
    display: block;
    margin-top: 5px;
}

button {
    width: 100%;
    padding: 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

#message {
    margin-top: 15px;
    text-align: center;
    font-weight: bold;
}
```

### Step 4: Improved JavaScript
Create an `improved.js` file:

```javascript
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');
    
    // Clear previous errors
    document.getElementById('usernameError').textContent = '';
    document.getElementById('passwordError').textContent = '';
    
    let isValid = true;
    
    if (username.trim() === '') {
        document.getElementById('usernameError').textContent = 'Username is required';
        isValid = false;
    }
    
    if (password.trim() === '') {
        document.getElementById('passwordError').textContent = 'Password is required';
        isValid = false;
    }
    
    if (isValid) {
        if (username === 'admin' && password === 'password') {
            message.textContent = 'Login successful!';
            message.style.color = 'green';
        } else {
            message.textContent = 'Invalid username or password.';
            message.style.color = 'red';
        }
    } else {
        message.textContent = 'Please correct the errors above.';
        message.style.color = 'red';
    }
});
```

### Step 5: Python Usability Testing Script
Create a `usability_test.py` file:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_usability(html_file, test_name):
    driver = webdriver.Chrome()
    driver.get(f'file:///path/to/your/{html_file}')
    
    start_time = time.time()
    
    try:
        # Wait for form to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        
        # Fill form
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys("admin")
        
        password_field = driver.find_element(By.NAME, "pass") if "original" in html_file else driver.find_element(By.ID, "password")
        password_field.send_keys("password")
        
        # Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']") if "original" in html_file else driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        
        # Wait for response
        time.sleep(2)
        
        end_time = time.time()
        task_time = end_time - start_time
        
        print(f"{test_name} - Task completion time: {task_time:.2f} seconds")
        
        return task_time
        
    except Exception as e:
        print(f"Error in {test_name}: {e}")
        return None
    finally:
        driver.quit()

def main():
    original_time = test_form_usability("original.html", "Original Form")
    improved_time = test_form_usability("improved.html", "Improved Form")
    
    if original_time and improved_time:
        improvement = ((original_time - improved_time) / original_time) * 100
        print(f"Usability improvement: {improvement:.1f}% faster task completion")

if __name__ == "__main__":
    main()
```

### Step 6: Documentation of Improvements
The improved form addresses the following usability issues:

1. **Effectiveness**: Added proper labels, validation, and clear error messages.
2. **Efficiency**: Better layout reduces cognitive load and speeds up task completion.
3. **Satisfaction**: Improved visual design and feedback enhance user experience.

The Python script quantifies these improvements by measuring task completion times.
