from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import sys

def extract_description(keyword):
    browser = webdriver.Firefox()

    browser.get('https://google.com')
    search = browser.find_element_by_name('q')

    #print("Enter a keyword to search on google: ", end='')
    #keyword = input()

    while True:
        search.send_keys(keyword+Keys.RETURN)
        browser.find_elements_by_xpath('//div[@class="r"]/a/h3')
        try:
            wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="r"]/a/h3'))).click()
            break
        except NoSuchElementException:
            break
        
    #results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')
    #result.find_element_by_xpath("./div/h3/a").click() 
    text = browser.find_element_by_xpath("//p").text
    if(len(text)<25):
        while True:
            try:
                text = browser.find_element_by_xpath("//p[2]").text
                break
            except NoSuchElementException:
                break
            
    print ("Reached")
    print(text)
    print("======================================================")
    print("======================================================")
    browser.quit()

def extract_acronyms(raw_input):
  


    r = re.findall('([A-Z][A-Z]+)', raw_input)
    a=list(set(r))
    print(a)
    for i in a:
        print(i+"\n")
        extract_description(i+" networking term wikipedia.org")
    #extract_description(r+" telecom")
    
#main
print("Paste text to search here: ")
#raw_input = input()
content = []
while True:
    line = input()
    if line:
        content.append(line)
    else:
        break
raw_input='\n'.join(content)
extract_acronyms(raw_input)
#extract_description(raw_input+" networking term")


