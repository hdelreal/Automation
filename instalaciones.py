import unittest
import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Edge
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyautogui

class instalacionesGBR(unittest.TestCase):

    def setUp(self):
        self.driver = Edge()
        self.usuario = 'dinacarlos'
        self.contrasena = '123'

    def doThis(self):
        
        driver = self.driver
        driver.get("http://localhost:8080/instalaciones/cliente/login")
        driver.maximize_window()
        pyautogui.write(self.usuario, interval=0.25)
        pyautogui.press('tab')
        pyautogui.write(self.contrasena, interval=0.25)
        pyautogui.press('return')
        

    """def testGenerarSolicitudVacia(self):
        driver = self.driver
        self.doThis()
        time.sleep(3)
        WebDriverWait(driver, 3)\
            .until(EC.element_to_be_clickable((By.ID, 'btnEnviar'))).click()

        time.sleep(3)
        driver.save_screenshot('camposInstalaciones.jpg')

        
        formulario = driver.find_element_by_xpath('//*[@id="formSolicitud"]')

        grupos = formulario.find_elements_by_class_name('form-group')

        divisiones = formulario.find_elements_by_class_name('control-label')

        cont=0
        while cont < (len(grupos)):
            
            cadena = divisiones[cont].text
            

            if cadena.endswith('*:'):
                
                advertencia = '//*[@id="formSolicitud"]/div['+str(cont+1)+']/div[2]'
                if advertencia != 0:
                    try:
                        assert advertencia in grupos, 'No cuenta con advertencia'
                        mensaje = driver.find_element_by_xpath(advertencia)
                        assert mensaje in divisiones, 'No cuenta con advertencia'
                        print(cadena)
                
                    except AssertionError as msg:
                        print(cadena, msg)

                    cont = cont    

                else:
                    cont = cont+1"""
             
    def testLlenarSolicitud(self):
        driver = self.driver
        self.doThis()
        time.sleep(3)

        #tipo solicitud
        pyautogui.click(868,313)
        time.sleep(5)
        pyautogui.press('down')
        pyautogui.press('return')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        
        #Factura a
        pyautogui.press('down')
        pyautogui.press('down')
        #pyautogui.press('return')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)

        #Promotor
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        time.sleep(1)
        #pyautogui.press('return')
        #time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)

        #Vehículo o contrato
        pyautogui.write('El Vehiculo', interval=0.25)
        pyautogui.press('tab')

        #Marca
        pyautogui.write('LA Marca', interval = 0.25)
        pyautogui.press('tab')

        #Modelo
        pyautogui.write('El Modelo', interval=0.25)
        pyautogui.press('tab')

        #Año
        pyautogui.write('2010', interval=0.25)
        pyautogui.press('tab')

        #Color
        pyautogui.write('Blanco deltecho', interval=0.25)
        pyautogui.press('tab')

        #Placas
        pyautogui.write('JUS6549', interval=0.25)
        pyautogui.press('tab')

        #VIN
        pyautogui.write('3S456BV21', interval=0.25)
        pyautogui.press('tab')

        #Agencia o lugar precargados
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sltAgencias"]/option[9]')))\
                .click()

        time.sleep(2)

        #plazo
        pyautogui.press('tab',presses=8)
        time.sleep(2)
        pyautogui.press('down',presses=2)
        time.sleep(2)
        pyautogui.press('tab')

        #NombreContacto
        pyautogui.write('NombreContacto',interval=0.25)
        pyautogui.press('tab')

        #TelefonoContacto
        pyautogui.write('3311546713')
        pyautogui.press('tab')

        
        
        WebDriverWait(driver, 3)\
            .until(EC.element_to_be_clickable((By.ID, 'btnEnviar'))).click()

        time.sleep(5)

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sub-item-1"]/li[2]/a')))\
                .click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()