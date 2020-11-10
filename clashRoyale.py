from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3
import requests

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

    #pegando endereço externo dinamicamente
    ip = requests.get('https://api.ipify.org').text

    range_0.send_keys(ip)
    range_0.submit()
    
    #pegando chave
    key_name = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CLASS_NAME, "api-key__name")))
    key_name.click()
    token = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@class='form-control input-lg']/samp")))
    #print(token.text)
except TimeoutError as err:
    isrunning = 0
    print("Exception has been thrown. " + str(err))
finally:
    driver.quit


#acessando api ClashRoyale
try:
    url = 'https://api.clashroyale.com/v1/clans'     
    #token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImYyOTU2NWNkLWU2ZGItNDE5MC1iZmY1LWFlODRhOGJkOGI5OSIsImlhdCI6MTYwNTAxMDAwNiwic3ViIjoiZGV2ZWxvcGVyLzc4Y2E1NmExLWM2MDQtYWFkNC04NGM3LTY2N2I1ODQwOWE5OSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyNTUuMjU1LjI1NS4wIl0sInR5cGUiOiJjbGllbnQifV19.r4Bf7SE2hznXCLfPk4aH3r5Aum8IMCjaNhCKu4iFOE61wmapBbAK4yfW6VhAkGmp9L29saOE7U75TMcxLiYg6Q'
    headers = {'Authorization': 'Bearer ' + token.text}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)





    


