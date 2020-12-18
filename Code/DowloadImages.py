from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import os
import urllib.request

def html():
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
    driver.get("https://es.wikipedia.org/wiki/Casa")
    title = driver.title
    html = driver.page_source
    file = open("html.txt", "w", encoding="UTF-8")
    file.write(html)
    file.close()
    file = open("links.txt", "w")
    for images in driver.find_elements_by_xpath('.//img'):
        file.write(str(images.get_attribute('src'))+'\n')
    file.close()
    driver.close()
    return title

def makepath():
    title = html()
    if os.path.exists(title):
        print("La carpeta existe.")
    else:
        os.mkdir(title)
    return title
    
def dowload_images():
    title = makepath() 
    time.sleep(5)
    file_links = open("links.txt", "r")
    i = 0
    while(True):
        linea = file_links.readline()
        if(linea != ""):
            filename = "filename"+str(i)+".png"
            filepath = os.path.join(title, filename)
            urllib.request.urlretrieve(linea, filepath)
            i += 1
        if not linea:
            break
    file_links.close()    

if __name__ == "__main__":
    dowload_images()