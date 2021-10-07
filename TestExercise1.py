'''
1.- Should be able to add items to shopping cart
2.- This products should be seen in shopping cart
3.- Delete items from shopping cart
'''
#libreries for using in method
from selenium import webdriver
import time

#initialize webDriver
driver = webdriver.Firefox()

#Function to initialize web page
def begining():
    
    #getting Initial Web Page
    driver.get('http://automationpractice.com/index.php')
    driver.maximize_window()
    time.sleep(5)

#Calling function
#begining()