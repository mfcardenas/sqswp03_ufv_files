# Lab 1: Introduction to ISO 9241

## Solution

### Step 1: Create the HTML Structure
Create an `index.html` file with the login form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login Form - ISO 9241 Demo</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form id="loginForm">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            
            <button type="submit">Login</button>
        </form>
        <div id="message"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### Step 2: Add CSS for Usability
Create a `style.css` file:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    width: 300px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

#message {
    margin-top: 10px;
    text-align: center;
}
```

### Step 3: Implement JavaScript for Validation
Create a `script.js` file:

```javascript
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');
    
    if (username === '' || password === '') {
        message.textContent = 'Please fill in all fields.';
        message.style.color = 'red';
    } else if (username === 'admin' && password === 'password') {
        message.textContent = 'Login successful!';
        message.style.color = 'green';
    } else {
        message.textContent = 'Invalid username or password.';
        message.style.color = 'red';
    }
});
```

### Step 4: Python Script for Usability Testing
Create a `test_usability.py` file:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_form():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
    driver.get('file:///path/to/your/index.html')  # Replace with actual path
    
    start_time = time.time()
    
    # Fill in the form
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("admin")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("password")
    
    # Submit the form
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()
    
    # Wait for message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    
    end_time = time.time()
    task_time = end_time - start_time
    
    print(f"Task completion time: {task_time:.2f} seconds")
    
    # Check if login was successful
    message = driver.find_element(By.ID, "message").text
    if "successful" in message:
        print("Usability test passed: Login successful")
    else:
        print("Usability test failed: Login unsuccessful")
    
    driver.quit()

if __name__ == "__main__":
    test_login_form()
```

### Step 5: Run and Evaluate
1. Open `index.html` in a browser to test the form manually.
2. Run `python test_usability.py` to perform automated testing.
3. Analyze the results for effectiveness, efficiency, and satisfaction.

This solution demonstrates ISO 9241 principles by creating a usable interface and providing a method to evaluate it.
