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
base_url = 'https://api.clashroyale.com/v1/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
'''
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
'''

#btenha as informações do clã de nome "The resistance", cuja tag começa com #9V2Y e que esteja localizado no Brasil
try:
    url = base_url+'clans?name=The resistance&locationId=57000038&limit=1'     
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM5OTgzMmYyLTQzNjUtNDQzNS1hYmIzLTQyN2U4OGJlODkzMSIsImlhdCI6MTYwNTAxNjA2Miwic3ViIjoiZGV2ZWxvcGVyLzc4Y2E1NmExLWM2MDQtYWFkNC04NGM3LTY2N2I1ODQwOWE5OSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzkuNzAuMTA2LjE5NSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.boPfJ7lLxEfxpo8fzlN9c67CN9GaYDfFfYWGYr8Cg3T9aAG2YlPu2ARDBog8o1OfHTnbODiAg4YrL51HrfyqJQ'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    tag = data['items'][0]['tag']

    print(data)

#pegando lista de membros do clã

    url2 = base_url+'clans?'+tag+'/members'     
    #token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM5OTgzMmYyLTQzNjUtNDQzNS1hYmIzLTQyN2U4OGJlODkzMSIsImlhdCI6MTYwNTAxNjA2Miwic3ViIjoiZGV2ZWxvcGVyLzc4Y2E1NmExLWM2MDQtYWFkNC04NGM3LTY2N2I1ODQwOWE5OSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzkuNzAuMTA2LjE5NSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.boPfJ7lLxEfxpo8fzlN9c67CN9GaYDfFfYWGYr8Cg3T9aAG2YlPu2ARDBog8o1OfHTnbODiAg4YrL51HrfyqJQ'
    response = requests.request("GET", url2, headers=headers)
    #members = response.json()
    print(url2)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)





    


