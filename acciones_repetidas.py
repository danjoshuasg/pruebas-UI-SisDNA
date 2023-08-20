from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def MoverClick(elemento):
    mover_mouse = webdriver.ActionChains(driver)
    mover_mouse.move_to_element(elemento)
    mover_mouse.perform()
    mover_mouse.move_to_element(elemento).click().perform()
    time.sleep(2)

def Ingresar_Login(url="https://ws01.mimp.gob.pe/sisdna-web/faces/login.xhtml",user="admin",password="123456"):
    driver.get(url)
    print(driver.title)
    driver.implicitly_wait(5) #Esparar 5 segundos
    input_user = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:username")))
    input_user.clear()
    input_user.send_keys(user)
    input_password = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:password")))
    input_password.clear()
    input_password.send_keys(password)
    button = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:j_idt34")))
    button.click()
    respuesta_home = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='j_idt56']/p")))
    print(respuesta_home.text)

if __name__ == "__main__":
    Ingresar_Login()