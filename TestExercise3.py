'''
1.- Should be able to add items to shopping cart
***2.- This products should be seen in shopping cart***
3.- Delete items from shopping cart
'''

#In this method we're going to check Shopping cart

from TestExercise2 import *

#Function to look at shopping cart
def cart():
    selectItems()
    time.sleep(5)

    #Assertion to there are two items in shopping cart
    cantidad = driver.find_element_by_class_name('ajax_cart_quantity')
    assert '2' in cantidad.text

    #Entering to shopping cart
    driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a').click()
    carrito = driver.find_element_by_id('cart_title')

    #Assertion to be in shopping cart
    assert 'SHOPPING-CART SUMMARY' in carrito.text

    #Takes a screenshot of the current shopping cart
    driver.save_screenshot('carrito2productos.png')

    #driver.close()

#Calling function
#cart()
