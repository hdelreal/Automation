from selenium import webdriver
from selenium.webdriver import Edge
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

driver = Edge()

fechas=[] #List to store name of the product
valores=[] #List to store price of the product
driver.get('https://dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador=158&dfecha=01%2F01%2F2021&hfecha=07%2F09%2F2021')

Filas = driver.find_elements_by_class_name('Celda')
print (len(Filas))
i = 2

for fila in Filas:
    if i < 175:
        try:
            fecha = fila.find_element_by_xpath('//*[@id="tdcontent"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/table/tbody/tr['+str(i)+']/td[1]')
            valor = fila.find_element_by_xpath('//*[@id="tdcontent"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/table/tbody/tr['+str(i)+']/td[2]')

            fechas.append(fecha.text)
            valores.append(valor.text)
            i = i+1

        except NoSuchElementException:
            print('No hay más elementos')
    
df = pd.DataFrame({'Fecha':fechas,'Valor':valores}) 
df.to_csv('precioDolar.csv', index=False, encoding='utf-8')

driver.close()