from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3


USER='adailton.silva10@live.com'
PASSWORD='12345678'
key_name='chave_random'
new_description= 'gerando chave aleatoria'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


try:
    #autenticando 
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver.exe')
    driver.get('https://developer.clashroyale.com/#/login')
    #driver.maximize_window()
    username = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "email")))
    passwordPage = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "password")))
    
    username.send_keys(USER)
    passwordPage.send_keys(PASSWORD)
    passwordPage.submit()

    #gerando chave 
    WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CLASS_NAME, "col-xs-6")))
    driver.get("https://developer.clashroyale.com/#/new-key")

    name = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "name")))
    description = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "description")))
    range_0 = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "range-0")))

    name.send_keys(key_name)
    description.send_keys(new_description)
    range_0.send_keys('255.255.255.0')
    range_0.submit()
    
    #pegando chave
    key_name = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CLASS_NAME, "api-key__name")))
    key_name.click()
    token = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@class='form-control input-lg']/samp")))
    print(token.text)
except TimeoutError as err:
    isrunning = 0
    print("Exception has been thrown. " + str(err))
finally:
    driver.quit
