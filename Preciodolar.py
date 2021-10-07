from selenium import webdriver

def Dolar():
    driver = webdriver.Firefox()
    Precio = open('Dolar.csv', 'a')
    driver.get('https://dof.gob.mx')
    precio = driver.find_element_by_xpath('//*[@id="table_menu_right"]/tbody/tr[1]/td/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td/p[1]')

    Precio.write(precio.text)
    Precio.write('\n')
    Precio.close()

    driver.close()

    Precio = open('Dolar.csv', 'r')
    print(Precio.read())


Dolar()

    