from selenium import webdriver
from selenium.webdriver import Edge
  
# create webdriver object
driver = Edge()
  
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
  
# get element 
element = driver.find_element_by_xpath('//*[@id="hslider"]/li[2]/a')
  
# print value
print(element.isdisplayed())