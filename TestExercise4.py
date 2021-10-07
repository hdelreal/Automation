'''
1.- Should be able to add items to shopping cart
2.- This products should be seen in shopping cart
***3.- Delete items from shopping cart***
'''

#In this method we're going to delete some items from shopping cart

from TestExercise3 import *

def deleteCart():
    cart()
    time.sleep(5)

    #Find and press delete button on a specific item
    driver.find_element_by_xpath('//*[@id="1_1_0_0"]/i').click()

    time.sleep(10)

    #Takes a screenshot of the updated shopping cart
    driver.save_screenshot('itemEliminado.png')

    driver.close()

#Calling this function makes all tasks done
deleteCart()

    