from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8080')  # port 8000 is not available, use 8080 to run Django server instead 

assert 'Django' in browser.title