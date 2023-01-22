import csv
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webbrowser.open_new_tab("http:localhost/little")
username = 'asishlittle'
password = 'Asish@2019'
admin_url = 'http://localhost/little/wp-admin'


with open('/Users/asishkantony/Documents/CodeGarages/automator/urls.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url = row[0]
        value = row[1]

        # # Open the URL in a new tab
        # webbrowser.open_new_tab(url)
        # Open the CSV file
        # webbrowser.open_new_tab("http:localhost/little")
        
        driver = webdriver.Chrome()
        driver.get(admin_url)

        assert 'Log In' in driver.title

        wp_login = driver.find_element('id', 'user_login')
        wp_login.send_keys(username)

        wp_passwd = driver.find_element('id', 'user_pass')
        wp_passwd.send_keys(password)

        wp_submit = driver.find_element('id', 'wp-submit')
        wp_submit.click()
        # Use Selenium to interact with the page
        driver.get(url)

        # Find the button with ID "custom-id" and click it
        button = driver.find_element('id', "wp-admin-bar-edit")
        button.click()
       
        assert 'Edit Page' in driver.title

        # Find the input field and fill it with the value from the CSV
        input_field = driver.find_element(
            By.CLASS_NAME, "editor-post-title__input")
        input_field.clear()
        input_field.send_keys(value)
        # time.sleep(5)
        update = driver.find_element(
            By.CLASS_NAME, "editor-post-publish-button")
        update.click()
        time.sleep(3)
        driver.close()
