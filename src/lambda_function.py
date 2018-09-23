from selenium import webdriver
from webdriver_wrapper import chrome_options
import json
import os

def lambda_handler(event,contex):

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.facebook.com/")
    title = driver.title
    print ("El Titulo de la pagina es: ",title)
    usr = driver.find_element_by_xpath("//*[@id='email']") 
    usr.send_keys(["usr"])
    passwd = driver.find_element_by_xpath("//*[@id='pass']")
    passwd.send_keys(["passwsd"])
    driver.find_element_by_xpath("//*[@id='u_0_2']").click()
    driver.find_element_by_xpath("//li[@id='navItem_588143690']/a/div").click()
    title = driver.title
    print (title)
    driver.quit()

    return {
        "statusCode": 200,
        "body": json.dumps('Funciona!!!')
    }
