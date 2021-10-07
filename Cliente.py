import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Edge
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyautogui



class ConsultaGBR(unittest.TestCase):

    def setUp(self):
        self.driver = Edge()
        self.usuario = "dgonzalez"
        self.contra = "Shera0810*"


    def dothis(self):
        driver = self.driver
        driver.get("https://agente.gbr-tech.com/laravel/login")
        driver.set_window_size(1440, 980)
        
        WebDriverWait(driver, 3)\
            .until(EC.element_to_be_clickable((By.NAME,'username')))\
                .send_keys(self.usuario)
        
        WebDriverWait(driver, 3)\
            .until(EC.element_to_be_clickable((By.NAME,'password')))\
                .send_keys(self.contra)
        
        btn = driver.find_element_by_css_selector(".btn-lg")
        btn.click()
        
        time.sleep(5)
        driver.save_screenshot("PanelDeControl.png")

    """def test_buscar_auto(self):
        driver = self.driver
        vehiculo={}
        self.dothis()

        try:
            buscar = driver.find_element_by_id("searchAll")
            buscar.clear()
            buscar.send_keys("cochiloquita")
            time.sleep(5)

            auto = driver.find_element_by_xpath('//*[@id="vehicleTable_wrapper"]/div[2]/div')
            detalleVehiculo = driver.find_element_by_id('vehicleDetails')
            auto.click()
            time.sleep(5)
            
            if detalleVehiculo.is_displayed():
                pass
            else:
                auto.click()
                time.sleep(5)

            driver.save_screenshot("VehiculoEncontrado.png")
        except:
            print("Auto no encontrado")

        try:
            obtener = driver.find_element(By.XPATH, '//*[@id="details"]/form/div[1]/div/div[2]')
            
            print('Hola Mundo')
            print(obtener.text)
            
            #Empezar aquí
            items = obtener.find_elements_by_tag_name('div')
            

        except:
            print("Aun no sirve")

        

    def test_Idioma_Espanol(self):
        driver = self.driver
        self.dothis()
        time.sleep(5)
        
        try:
            idioma = driver.find_element_by_css_selector(".nav-pull-right > .dropdown-toggle")
            self.assertEqual("Español", idioma.text)
        except AssertionError:
            print(f"Idioma de inicio es {idioma.text}")

    def test_cambiar_idioma(self):
        driver = self.driver
        self.dothis()
        time.sleep(5)
        idio = driver.find_element_by_css_selector(".nav-pull-right > .dropdown-toggle")
        idio.click()
        time.sleep(2)
        sele = driver.find_element_by_link_text('Español')
        sele.click()
        time.sleep(5)

    def test_PaseoPorAdmin(self):
        driver = self.driver
        self.dothis()
        
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav/div/div[2]/ul[1]/li[4]/a')))\
                .click()
        
        driver.find_element_by_id('addButton').click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.ID, 'submitAlias')))\
                .click()

        vacio = driver.find_element_by_id('uNameInput-error')
        print (vacio)

        driver.find_element_by_id('cancelAlias')

    def test_CrearGeoCerca(self):
        driver= self.driver
        self.dothis()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav/div/div[2]/ul[1]/li[4]/a')))\
                .click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/ul/li[3]/a')))\
                .click()

        #Creando geocerca con las siguientes coordenadas:
        time.sleep(3)
        pyautogui.moveTo(860,442)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(860,542)
        pyautogui.click()
        time.sleep(3)
        pyautogui.move(50,80)
        pyautogui.click()
        time.sleep(3)
        pyautogui.move(100,-30)
        pyautogui.click()
        time.sleep(3)
        pyautogui.move(0,-50)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(860,542)
        pyautogui.click()
        time.sleep(3)   

        
        #Llenando formulario de geocerca
        pyautogui.moveTo(576,275)
        pyautogui.click()
        pyautogui.write('NombreGeocerca', interval=0.25)
        pyautogui.press('tab')
        pyautogui.write('Geocerca de Prueba', interval=0.25)
        time.sleep(3)
        
        pyautogui.moveTo(460,382)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(742,357)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(863,353)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(553,473)
        pyautogui.click()
        time.sleep(2)

        pyautogui.press('space')
        pyautogui.press('down', interval=0.25)
        pyautogui.press('return')

        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('down', interval=0.25)
        pyautogui.press('return')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.press('return')
        time.sleep(3)

        WebDriverWait(driver, 3)\
            .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="geofencesTable"]/tbody/tr/td[1]')))\
                .click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="geofencesTable"]/tbody/tr/td[8]/div/button[2]/i').click()
        time.sleep(3)

    def test_jugandoConReportes(self):
        driver = self.driver
        self.dothis()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-reports"]/a')))\
                .click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.ID, 'selectReport'))).click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectReport"]/option[3]')))\
                .click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vehicleColumn"]/div/button/span')))\
                .click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vehicleColumn"]/div/div/ul/li[2]/label/input')))\
                .click()
        
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vehicleColumn"]/div/button/span')))\
                .click()

        time.sleep(4)

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.ID,'runReport'))).click()

        time.sleep(5)
        
        driver.save_screenshot('ReporteLocalizaciones.jpg')"""
        
    def test_historial(self):
        driver = self.driver
        self.dothis()

        #entrar al mapa
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nav-mapping"]/a')))\
                .click()

        try:
            auto = driver.find_element_by_xpath('//*[@id="vehicleTable_wrapper"]/div[2]/div')
            detalleVehiculo = driver.find_element_by_id('vehicleDetails')
            auto.click()
            time.sleep(5)
            
            if detalleVehiculo.is_displayed():
                pass
            else:
                auto.click()
                time.sleep(5)

            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.XPATH,'//*[@id="historyTab"]/a')))\
                    .click()
            
            time.sleep(5)
            aver=[]        
            tabla = driver.find_element_by_xpath('//*[@id="historyTable"]/thead/tr')
            filas = driver.find_elements(By.TAG_NAME,'tr')

            for fila in range(len(filas)):
                columna = fila
            

            time.sleep(5)

        except:
            print("Error bonito")

        
        
    
    def tearDown(self):
        self.driver.close()
        


if __name__ == "__main__":
    unittest.main()

