'''
***1.- Should be able to add items to shopping cart***
2.- This products should be seen in shopping cart
3.- Delete items from shopping cart
'''
#In this method we're going to add items and search items to shopping cart

#Getting libs, vars and functions from initilize file
from TestExercise1 import *
import pyautogui

#This function moves the mouse to specific place to click and continue
def continueShopping():
    pyautogui.moveTo(1069,481)
    time.sleep(5)
    pyautogui.click()
    #pyautogui.click()

#function to add items to Shopping Cart
def addingToCart():
    driver.find_element_by_id('add_to_cart').click()

#Function to select items and search
def selectItems():
    #initilizing web page
    begining()
      
    driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div').click()
    time.sleep(10)

    #Assertion to know the item's name
    item = driver.find_element_by_xpath('//*[@id="center_column"]/div/div/div[3]/h1')
    assert 'Faded Short Sleeve T-shirts' in item.text

    #adding item to cart
    addingToCart()
    time.sleep(5)

    #continue shopping
    continueShopping()
    time.sleep(5)

    #Searching for Dress items
    driver.find_element_by_id('search_query_top').click()
    pyautogui.write('Dress', interval = 0.25)
    driver.find_element_by_xpath('//*[@id="searchbox"]/button').click()
    time.sleep(5)

    #Selecting second dress
    driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[2]/div').click()
    time.sleep(5)

    #Assertion to know the item's name
    item2 = driver.find_element_by_xpath('//*[@id="center_column"]/div/div/div[3]/h1')
    assert 'Printed Dress' in item2.text

    #adding item to cart
    addingToCart()
    time.sleep(5)
    continueShopping()
    time.sleep(5)

    #driver.close()

#Calling function
#selectItems()
