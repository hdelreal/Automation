import unittest
from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyperclip
from selenium.webdriver import Edge
import time

class EntrarCallCenter(unittest.TestCase):
    
    def setUp(self):
        self.driver = Edge()
        self.UsuarioGBR = "gbr"
        self.ContraGBR = "p@ssw0rdGbrT3ch"
        self.usuario = "dgonzalez"
        self.contrasena = "Shera0810*"

    def iniciar(self):
        driver = self.driver
        driver.get('https://agente.gbr-tech.com/callcenter/')
        driver.set_window_size(1440,930)

    def test_abrir(self):
        self.iniciar()
        driver = self.driver
        pyautogui.moveTo(700,180)
        pyautogui.click()
        pyautogui.write(self.UsuarioGBR, interval=0.25)
        pyautogui.press('tab')
        pyperclip.copy(self.ContraGBR)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('return')
        time.sleep(5)
        
        WebDriverWait(driver,2)\
            .until(EC.element_to_be_clickable((By.ID,'username')))\
                .send_keys(self.usuario)
        contra = driver.find_element_by_id("password")
        contra.send_keys(self.contrasena)
        

        enviar = driver.find_element_by_id("submitForm")
        enviar.click()
        time.sleep(5)

    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()


    #C:\Users\HectorDelReal\AppData\Local\Microsoft\Edge\User Data\Default
    